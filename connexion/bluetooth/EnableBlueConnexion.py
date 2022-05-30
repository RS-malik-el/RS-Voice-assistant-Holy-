#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUTEUR: RACHEL SYSTEME
DATE  : 02/03/2022
DATE DE FIN : 20/02/2022
MODIFIER    : 22/05/2022
"""

import os
import socket
import pickle as pic
from PIL import Image, ImageTk
from tkinter import messagebox
import recordVoice.BackVoiceExitStatus as bv

fr_noReply 			 ="sounds/french/fr_noReply.mp3"
fr_BLUE_DISCONNECTED ="sounds/french/fr_blue_error/fr_blue_disc_error.mp3"
fr_BLUE_ACCESS_ERROR ="sounds/french/fr_blue_error/fr_blue_Access_error.mp3"

en_noReply 			 ="sounds/english/en_noReply.mp3"
en_BLUE_DISCONNECTED ="sounds/english/en_blue_error/en_blue_disc_error.mp3"
en_BLUE_ACCESS_ERROR ="sounds/english/en_blue_error/en_blue_Access_error.mp3"

PORT 	  = 1
TIMEOUT   = 2
NBRE_BITS = 4 # bits en attente d'être lu / bits waiting to be read

class EnableBlueConnexion:
	"""
		INFORMATION:
			Ce Module permet d'établir la connexion bluetooth avec la carte arduino.
			This module allows you to connect arduino board by bluetooth.
		
		PARAMETRE:
			lang   : Permet de choisir la langue de sortie du fichier audio
				type : str
				valeur : "fr" et "en"

		METHODES UTLISEES DANS LE FICHIER "mainWindow":
			self.Blue_SendDate()	
			self.DisconnectBlue()
			self.getState()	
	"""
	def __init__(self,lang):
		self._Run 		 = False
		self._State 	 = False
		self._Blue  	 = None
		self._lang 		 = lang
		self._MacAddress = ""
		self._ExtractMacAddress()
		self._ConnectBlue()


	# Extraction de l'addresse Mac/ Extraction of Mac Address
	def _ExtractMacAddress(self):
		FOLDER = "Blue_Mac_Address"
		try:
			with open("{}/macAddress.rachel".format(FOLDER),
			"rb") as fichier:
				mon_pickler	  	   = pic.Unpickler(fichier)
				self._MacAddress   = str(mon_pickler.load())
			self._Run = True
		except FileNotFoundError:
			self._Run = False


	# Connexion bluetooth / Connection to bluetooth
	def _ConnectBlue(self):
		if self._Run == True:
			try:
				self._Blue = socket.socket(socket.AF_BLUETOOTH,
								  		   socket.SOCK_STREAM,
								  		   socket.BTPROTO_RFCOMM
								  		   )
				self._Blue.connect((self._MacAddress,PORT))
				self._Blue.settimeout(TIMEOUT)
				self._State = True

			# Impossible d'établir une connexion / Unable to establish a connection
			except TimeoutError:
				if self._lang == "fr":
					bv.BackVoice(fr_BLUE_ACCESS_ERROR)
				else:
					bv.BackVoice(en_BLUE_ACCESS_ERROR)
				self._Error()
			except OSError:
				if self._lang == "fr":
					bv.BackVoice(fr_BLUE_DISCONNECTED)
				else:
					bv.BackVoice(en_BLUE_DISCONNECTED)
				self._Error()

	# Message d'erreur / Error message
	def _Error(self):
		self._State = False
		self._Run   = False
		messagebox.showwarning("Error","Unable to establish connexion")


	# Permet de fermer le connexion bluetooth 
	# Close the bluetooth connexion
	def DisconnectBlue(self):
		if self._Run == True:
			self._Blue.close()
			self._State = False
			self._Run   = False

	
	"""
		Envoie des données et réception du feedback 
		Send data and receive feedback
		paramètres : 
			liste : liste des données à envoyés
				type : list
			lang : langage de sortie du fichier audio
				type : str
	"""
	def Blue_SendDate(self,liste,lang):
		try:
			self._lang = lang
			if self._Run == True:
				i = 0
				while i < len(liste):
					self._Blue.send(bytes(str(liste[i]),'ASCII'))
					i += 1
				
				# Feedback
				FeedBack = self._Blue.recv(NBRE_BITS)
				FeedBack = str(FeedBack)
				if FeedBack == "b'TRUE'":
					FeedBack = "TRUE"
				else:
					FeedBack = "FALSE"
					if self._lang == "fr":
						bv.BackVoice(fr_noReply)
					else:
						bv.BackVoice(en_noReply) 
				return FeedBack
		except TimeoutError:
			FeedBack 	= "FALSE"
			if self._lang == "fr":
				bv.BackVoice(fr_noReply)
			else:
				bv.BackVoice(en_noReply)
			return FeedBack
		except ConnectionAbortedError:
			messagebox.showwarning("Error","Unable to send data")
			self._Blue.close()
			self._State = False
			self._Run   = False
			FeedBack 	= None
			return FeedBack
		

	def getState(self):
		return self._State