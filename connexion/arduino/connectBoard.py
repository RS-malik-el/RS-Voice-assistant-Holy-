#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUTEUR: RACHEL SYSTEME
DATE  : 02 FEVRIER 2022
DATE DE FIN : 03/02/2022
MODIFIER    : 22/05/2022
"""
import serial 
import pickle as pic
from tkinter import messagebox
import recordVoice.BackVoiceExitStatus as bv

fr_noReply 			 ="sounds/french/fr_noReply.mp3"
en_noReply 			 ="sounds/english/en_noReply.mp3"

TIMEOUT   = 2
NBRE_BITS = 4 # bits en attente d'être lu / bits waiting to be read

class connectBoard:
	"""
		INFORMATION:
			Ce Module permet d'établir la connexion série avec la carte arduino.
			This module allows you to connect arduino board by serial port.
		
		METHODES UTILISEES DANS LE FICHIER "mainWindow":
			self.Serial_SendDate()	
			self.DisablePort()
			self.get_state()	
	"""
	def __init__(self):
		super(connectBoard, self).__init__()
		self._port 	   = None
		self._BaudRate = None
		self._state    = False
		self._Extract_Port_And_Baudrate()
		self._Connect()


	# Extraction du port et du baudRate 
	# Extraction of port and baudRate
	def _Extract_Port_And_Baudrate(self):
		try:
			with open("serial_port_access/serial.rachel","rb") as fichier:
				mon_pickler	  = pic.Unpickler(fichier)
				self._port     = str(mon_pickler.load())
				self._BaudRate = mon_pickler.load()
			self._run = True
		except FileNotFoundError:
			messagebox.showerror("Error","Connexion type not configure")
			self._run = False

	
	# Connexion à la carte via le port série
	# Connexion to the card via the serial port
	def _Connect(self):
		if self._run == True:
			try:
				self.board = serial.Serial(	port=self._port,
											baudrate=self._BaudRate,
											timeout=TIMEOUT
											)
				self._state= True
			except serial.serialutil.SerialException:
				messagebox.showwarning("Error","Unable to establish connection")
				self._state = False
				self._run   = False


	"""
		Envoie des données et réception du feedback 
		Send data and receive feedback
		paramètres : 
			liste : liste des données à envoyés
				type : list
			langage : langage de sortie du fichier audio
				type : str
	"""
	def Serial_SendDate(self,liste,langage):
		if self._run == True:
			try:
				FeedBack = None
				self.board.flushOutput()
				self.board.flushInput()
				self.board.write(liste)

				# Feedback
				FeedBack = self.board.read(size=NBRE_BITS)
				FeedBack = str(FeedBack)
				FeedBack = FeedBack.upper()

				if FeedBack=="B'TRUE'":
					FeedBack = "TRUE"
				else:
					FeedBack = "FALSE"
					if langage == "fr":
						bv.BackVoice(fr_noReply)
					else:
						bv.BackVoice(en_noReply) 
				return FeedBack
			except serial.serialutil.SerialException:
				messagebox.showwarning("Error","Unable to send data")
				self.board.close()
				self._run   = False
				self._state = False
				FeedBack 	= None
				return FeedBack


	# Permet de fermer le connexion série 
	# Close the serial connection
	def DisablePort(self):
		if self._run == True:
			self.board.close()
			self._state = False
			self._run   = False
			

	def get_state(self):
		return self._state