#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUTEUR: RACHEL SYSTEME
DATE  : 02/03/2022
DATE DE FIN : 02/03/2022
"""
import os
import tkinter as tk
import pickle as pic
from PIL import Image, ImageTk
from tkinter import simpledialog
from tkinter import messagebox

F_icone     = "icones/icone.ico"  
Img_Save    = "icones/Save.png" 
FOLDER 		= "Blue_Mac_Address"
MAX_CHAR 	= 17 # Maximum of characters to be entered

class ConfigMacAddress(tk.simpledialog.Dialog):
	"""
		INFORMATION:
		****Ce module permet de créer un fichier contenant
			l'addresse mac du bluetooth
		****This module allows you to create a file containing
			the mac address of bluetooth

		PARAMETRE:
			parent : Fenêtre à prendre le focus 
				type: tkinter 

			Title  : permet de définir le titre de la fenêtre
				type: str
	"""
	def __init__(self,parent,title="Bluetooth Mac address"):
		self._font = ("Arial","11", "bold")

		# Dernier adresse mac utiliser / Last mac address use
		try:
			with open("{}/macAddress.rachel".format(FOLDER),
			"rb") as fichier:
				mon_pickler	  	   = pic.Unpickler(fichier)
				self._DefaultValue = str(mon_pickler.load())
		except FileNotFoundError:
			self._DefaultValue = "00:00:00:00:00:00"

		super(ConfigMacAddress, self).__init__(parent,title)
		
	# Window
	def body(self,master):
		# Taille de la fenêtre / size of window
		self.geometry("300x120")
		self.iconbitmap(F_icone)
		self.resizable(width=False,height=False)

		# Création d'un combox de saisie d'adresse mac
		# Creating a mac address input combox
		tk.Label(self,text="Write bluetooth mac address\neg: 00:3F:45:11:10:DE",
			font=self._font).pack(pady=5)
		self.Input = tk.StringVar()
		self.Input.set(self._DefaultValue)
		self._macAddress = tk.Entry(self,textvariable=self.Input ,width=20,font=self._font)
		self._macAddress.pack()
		self.Input.trace("w", lambda *args: self.LimitChar(entry_text =self.Input, nb=MAX_CHAR))
		

	# FONCTION PERMETTANT DE LIMITER LE NOMBRE DES CARACTERES A SAISIR
	# FUNCTION TO LIMIT THE NUMBER OF CHARACTERS TO BE ENTERED
	def LimitChar(self, entry_text, nb):
		if len(entry_text.get()) > 0:
			entry_text.set(entry_text.get()[:nb])


	# Sauvegarde l'adresse dans un fichier / Saves the address to a file
	def SaveMacAddress(self):
		try:
			os.mkdir(FOLDER)
		except FileExistsError:
			pass
			
		with open("{}/macAddress.rachel".format(FOLDER),
			"wb") as fichier:
			mon_pickler	 = pic.Pickler(fichier)
			mon_pickler.dump(self.Input.get())
		self.destroy()


	# Button
	def buttonbox(self):
		try:
			# Save Boutton
			img1 = Image.open(Img_Save)
			Image1 = img1.resize((80,40))
			self.ImgSave = ImageTk.PhotoImage(Image1)

			save = tk.Button(self,width=80,height=40,
							 image=self.ImgSave,
							 command=self.SaveMacAddress
							)
			save.pack(padx=10)
		except FileNotFoundError:
			messagebox.showwarning("Error","images missing, close the window please!")
			save = tk.Button(self,text="CONNECT",
							 width=20,height=3,bg="green",
							 command=self.SaveMacAddress
							 )
			save.pack(padx=10)