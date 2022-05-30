#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUTEUR: RACHEL SYSTEME
DATE  : 02 FEVRIER 2022
DATE DE FIN : 02/02/2022
"""
import tkinter as tk
import pygame
from PIL import Image, ImageTk
from tkinter import simpledialog
from tkinter import messagebox
import fenetre.HomeChoiceOfLanguage as HCOL
import recordVoice.BackVoiceExitStatus as bv

F_icone  = "icones/icone.ico"  # icone de la fenêtre
IMG_BOT  = "icones/ImgBot.png" # Image du robot

FR_MSG_ABOUT_SOFTWARE = "sounds/french/fr_acceuil.mp3"
FR_MSG_ABOUT_RS 	  = "sounds/french/fr_AboutRS.mp3"
FR_HOW_IT_WORKS 	  = "sounds/french/fr_HowItWorks.mp3"
FR_MSG_ERROR 	      = "sounds/french/fr_Error.mp3"

EN_MSG_ABOUT_SOFTWARE = "sounds/english/en_acceuil.mp3"
EN_MSG_ABOUT_RS 	  = "sounds/english/en_AboutRS.mp3"
EN_HOW_IT_WORKS       = "sounds/english/en_HowItWorks.mp3"
EN_MSG_ERROR 	      = "sounds/english/en_Error.mp3"

class WelcomeMessage(tk.simpledialog.Dialog):
	"""
		INFORMATION:
		****Ce module permet de créer une fenêtre d'accueil afin d'annoncer le message d'acceuil.
			Aussi utiliser dans le menu help et dans le fichier "voiceRecording"
			Cliquer sur le bouton pour tout arreter.
		****This module allows you to create a welcome window to announce the welcome message.
			Also use in the help menu and in the "voiceRecording" file.
			Click on the button to stop everything.

		PARAMETRE: / SETTING :
			parent : Fenêtre à prendre le focus / Window to take focus
				type: tkinter 

			Title  : permet de définir le titre de la fenêtre /
					 allows you to define the title of the window
				type: str

			lang   : Permet de choisir la langue de sortie du fichier audio /
					 Allows you to choose the output language of the audio file
				type : str
				valeur : "fr" et "en"

			choiceLanguage: permet de créer la fenêtre "choix de langue" /
							used to create the "choice of language" window
				type : bool

			menu : permet d'indiquer le fichier audio à lire /
				   allows you to indicate the audio file to play
				type : str
				valeur: "acceuil", "howitworks", et "about_rs"
	"""

	def __init__(self,parent,Title="Welcome message",lang="fr",
			choiceLanguage=True,menu="acceuil"):
		pygame.mixer.init()
		self.MENU = menu 

		if choiceLanguage == True:
			LANG = HCOL.homeChoiceLanguage(parent)
			self.LANG = LANG.lang
		else:
			self.LANG = lang
		
		super(WelcomeMessage, self).__init__(parent,Title)
		pygame.mixer.music.stop()
		
	# Window / fenêtre
	def body(self,master):
		# Fenêtre d'acceuil de l'assistant vocal / Voice assistant home window
		self.geometry("250x320")
		self.iconbitmap(F_icone)
		self["bg"]="blue"
		self.resizable(width=False,height=False)

		# Insertion de l'image / Insert image 
		try:
			img1 = Image.open(IMG_BOT)
			Image1 = img1.resize((210,250))
			self.image_robot = ImageTk.PhotoImage(Image1)

			self.CanvaImage = tk.Canvas(self ,width=200, height=250, relief=tk.SUNKEN)
			self.CanvaImage.pack(padx=20,pady=10,fill="both", expand=True)
			self.CanvaImage.create_image(0, 0, image=self.image_robot,anchor="nw")
		except:
			if self.LANG == "fr":
				messagebox.showwarning("ERROR","Fichier manquant: image de l'assistant vocal")
			if self.LANG == "en":
				messagebox.showwarning("ERROR","Missing file: voice assistant image")
		self._PlayMp3File() # Appel a la méthode / Call to the method


	# Méthode pour jouer lire les fichiers mp3 / Method to play play mp3 files
	def _PlayMp3File(self):
		if self.LANG == "fr" and self.MENU == "acceuil":
			bv. BackVoice(FR_MSG_ABOUT_SOFTWARE)
		if self.LANG == "en" and self.MENU == "acceuil":
			bv. BackVoice(EN_MSG_ABOUT_SOFTWARE)
				
		if self.LANG == "fr" and self.MENU == "howitworks":
			bv. BackVoice(FR_HOW_IT_WORKS)
		if self.LANG == "en" and self.MENU == "howitworks":
			bv. BackVoice(EN_HOW_IT_WORKS)	

		if self.LANG == "fr" and self.MENU == "about_rs":
			bv. BackVoice(FR_MSG_ABOUT_RS)
		if self.LANG == "en" and self.MENU == "about_rs":
			bv. BackVoice(EN_MSG_ABOUT_RS)

		if self.LANG == "fr" and self.MENU == "error":
			bv. BackVoice(FR_MSG_ERROR)
		if self.LANG == "en" and self.MENU == "error":
			bv. BackVoice(EN_MSG_ERROR)


	# Close de window
	def _Close(self):
		# vérifie si l'audio est toujours en cours d'exécution et l'arrête
		# checks if audio is still running and stop it
		if pygame.mixer.music.get_busy() == True:
			pygame.mixer.music.stop()
		# Destruction de la fenêtre / Destruction of the window
		self.destroy()


	# bouton pour fermer la fenêtre / button to close the window
	def buttonbox(self):
		close = tk.Button(self,text="Close",width=20, height=10, command=self._Close)
		close.pack()