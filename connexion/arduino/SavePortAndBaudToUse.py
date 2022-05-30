#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AUTEUR: RACHEL SYSTEME
DATE  : 18/02/2022
DATE DE FIN : 20/02/2022
"""
import os
import tkinter as tk
from tkinter import ttk
import pickle as pic
from PIL import Image, ImageTk
from tkinter import simpledialog
from tkinter import messagebox
import connexion.arduino.AvailablePort as AP

F_icone     = "icones/icone.ico"  
Img_Save    = "icones/Save.png"  
Img_UpDate  = "icones/UpDate.png"  

class UsablePort(tk.simpledialog.Dialog):
	"""
		INFORMATION:
			Ce module permet de créer une fenêtre de sélection
			du port et du baudrate pour connecter la carte via 
			la connection série. un fichier contenant
			le port et le baudrate sera créé à la fin.

		INFORMATION:
			This module allows you to create a port and baudrate 
			selection window to connect the card via the serial connection.
			a file containing the port and the baudrate will be created at the end.

		PARAMETRE:
			parent : Fenêtre à prendre le focus 
				type: tkinter 

			Title  : permet de définir le titre de la fenêtre
				type: str
	"""
	def __init__(self,parent,title="Select port and baudrate"):
		self.font = ("Arial","15", "bold")
		super(UsablePort, self).__init__(parent,title)
		
	# Fenêtre / Window
	def body(self,master):
		# Taille de la fenêtre / size of window
		self.geometry("300x200")
		self.iconbitmap(F_icone)
		self.resizable(width=False,height=False)

		# Création d'un combox affichant la liste des ports disponible
		# Creation of a combox displaying the list of available ports
		tk.Label(self,text="Select the arduino board",font=self.font).pack(pady=5)
		self.ComboPort = ttk.Combobox(	self,width=20,height=20,
									  	state ="readonly",font=("Arial","10")
									  	)
		self.ComboPort.set("Arduino not Available")
		self.ComboPort.pack(pady=10)
		self.ListePortDispo()

		# Création d'un combox affichant la liste des valeurs de baudRate
		# Creation of a combox displaying the list of baudRate values
		listOfBaudRateValue = ["1200","2400","4800","9600","19200","38400","57600","115200"]
		tk.Label(self,text="Select the baudRate",font=self.font).pack(pady=10)
		self.ComboBaudRate = ttk.Combobox(	self,values=listOfBaudRateValue,
											width=20,height=20,state ="readonly",
											font=("Arial","10")
											)
		self.ComboBaudRate.set("9600")
		self.ComboBaudRate.pack(pady=5)
	

	# Méthode permettant de metre à jour le nombre de port disponible
	# Method to update the number of available ports
	def ListePortDispo(self):
		listOfPortValue =[]
		com = AP.ListePortCom()
		
		tour= 1
		index = 0
		while tour <= len(com.PortDispo):
			listOfPortValue.append(str(com.PortDispo[index]))
			tour+=1
			index+=1

		self.ComboPort.config(values=listOfPortValue)


	# Méthode permettant d'enregistrer le port et baudrate dans un fichier
	# Method to save port and baudrate to a file
	def Save(self):
		# Obtention du port serie et du du baudrate
		# Get serial port and baudrate
		getport = self.ComboPort.get()
		getbaud = str(self.ComboBaudRate.get())
		getbaud = int(getbaud)

		"""
		Lecture des caractères correspondant au port disponible jusqu'au vide(" ")
			exemple : "COM5 - (Arduino Mega at COM5)"
			Available_port = "COM5" à la fin de la boucle for

		Reading the characters corresponding to the available port until the void(" ")
			example: "COM5 - (Arduino Mega at COM5)"
			Available_port = "COM5" at the end of the for loop
		"""
		Available_port =""
		
		for x in getport:
			if x == " ":
				if Available_port == "Arduino":
					Available_port = ""
				break
			Available_port += x 
	

		# Création du dossier s'il existe pas / Create folder if it doesn't exist
		try:
			os.mkdir("serial_port_access")
		except FileExistsError:
			pass

		# Stockage des infos du PORT et du BAUDRATE pour utilisation future
		# Storing PORT and BAUDRATE info for future use
		with open("{}".format("serial_port_access/serial.rachel"),
			"wb") as fichier:
			mon_pickler	 = pic.Pickler(fichier)
			mon_pickler.dump(Available_port)
			mon_pickler.dump(getbaud)

		self.typeConnexion = "serial"
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
							command=self.Save
							)
			save.pack(side=tk.RIGHT,padx=10)

			# Update Boutton
			img2 = Image.open(Img_UpDate)
			Image2 = img2.resize((80,40))
			self.ImgUpdate = ImageTk.PhotoImage(Image2)

			update = tk.Button(self,width=80,height=40,
								image=self.ImgUpdate,
								command=self.ListePortDispo
								)
			update.pack(side=tk.LEFT,padx=10)
		except FileNotFoundError:
			messagebox.showwarning("Error","images missing, close the window please!")

			update = tk.Button(self,text="UpDate",
								width=20,height=3,bg="yellow",
								command=self.ListePortDispo
								)
			update.pack(side=tk.LEFT,padx=10)

			save = tk.Button(self,text="Save",width=20,
							height=3,bg="green",
							command=self.Save
							)
			save.pack(side=tk.RIGHT,padx=10)