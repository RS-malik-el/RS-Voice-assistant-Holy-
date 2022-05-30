#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUTEUR: RACHEL SYSTEME
DATE  : 02 FEVRIER 2022
DATE DE FIN : 24/05/2022
"""
import os
import pygame
import tkinter as tk
from tktooltip import ToolTip
from tkinter import messagebox
from PIL import Image, ImageTk
import fenetre.contacts as cont
import fenetre.welcomeMessage as WM
import recordVoice.voiceRecording as record
import recordVoice.BackVoiceExitStatus as BV
import recordVoice.voiceProcessing as VP
import connexion.arduino.SavePortAndBaudToUse as port
import connexion.arduino.connectBoard as board
import connexion.bluetooth.ConfigMacAddress as MAC_ADDRESS
import connexion.bluetooth.EnableBlueConnexion as bluetooth

F_icone 	= "icones/icone.ico"
IMG_BG  	= "icones/BackGround.png" # Arrière plan de la fenêtre
IMG_BOT 	= "icones/ImgBot.png"     # Image du robot
IMG_START	= "icones/Bouton_ok.png"

Coleur = "blue" 		  # barre inférieur
C_Voyant_Act 	= "green" # couleur du voyant actif
C_Voyant_NonAct = "red"   # couleur du voyant non-actif

LOW   = 0
HIGH  = 1
OPEN  = 90
CLOSE = 0

######################_TEXT_TO_DISPLAY####################################
Fr_INFOBULLE = "Cliquer sur le bouton"
En_INFOBULLE = "Click on the button"

En_No_Act_text_L1  = "Light 1 : OFF"
En_No_Act_text_L2  = "Light 2 : OFF"
En_No_Act_text_L3  = "Light 3 : OFF"
En_No_Act_text_L4  = "Light 4 : OFF"
En_No_Act_text_L5  = "Servomotor : 0°"

En_Act_text_L1 = "Light 1 : ON"
En_Act_text_L2 = "Light 2 : ON"
En_Act_text_L3 = "Light 3 : ON"
En_Act_text_L4 = "Light 4 : ON"
En_Act_text_L5 = "Servomotor : 90°"

Fr_No_Act_text_L1 = "Led 1 : ETEINT"
Fr_No_Act_text_L2 = "Led 2 : ETEINT"
Fr_No_Act_text_L3 = "Led 3 : ETEINT"
Fr_No_Act_text_L4 = "Led 4 : ETEINT"
Fr_No_Act_text_L5 = "Servomoteur : 0°"

Fr_Act_text_L1 = "Led 1 : ALLUME"
Fr_Act_text_L2 = "Led 2 : ALLUME"
Fr_Act_text_L3 = "Led 3 : ALLUME"
Fr_Act_text_L4 = "Led 4 : ALLUME"
Fr_Act_text_L5 = "Servomoteur : 90°"

Text_BottomBar= "Developed by Rachel System............. Year 2022"

######################_FICHIERS_AUDIO_####################################
#-----------------------------ENGLISH-------------------------------------
en_InvalidCommand 	= "sounds/english/en_Command_Error.mp3"
en_disableConnexion ="sounds/english/en_disableConnexion.mp3"
en_voice_led1_off   ="sounds/english/stateOuput/en_light_1_off.mp3"
en_voice_led2_off   ="sounds/english/stateOuput/en_light_2_off.mp3"
en_voice_led3_off   ="sounds/english/stateOuput/en_light_3_off.mp3"
en_voice_led4_off   ="sounds/english/stateOuput/en_light_4_off.mp3"
en_servoClose       ="sounds/english/stateOuput/ServoClose.mp3"

en_led1_already_off    ="sounds/english/answer2/en_led1_already_off.mp3"
en_led2_already_off    ="sounds/english/answer2/en_led2_already_off.mp3"
en_led3_already_off    ="sounds/english/answer2/en_led3_already_off.mp3"
en_led4_already_off    ="sounds/english/answer2/en_led4_already_off.mp3"
en_all_already_off     ="sounds/english/answer2/en_all_already_off.mp3"
en_already_servoClose  ="sounds/english/answer2/en_servo_already_off.mp3"

en_enableConnexion = "sounds/english/en_enableConnexion.mp3"
en_voice_led1_on   ="sounds/english/stateOuput/en_light_1_on.mp3"
en_voice_led2_on   ="sounds/english/stateOuput/en_light_2_on.mp3"
en_voice_led3_on   ="sounds/english/stateOuput/en_light_3_on.mp3"
en_voice_led4_on   ="sounds/english/stateOuput/en_light_4_on.mp3"
en_servo_open      ="sounds/english/stateOuput/Servo_Open.mp3"

en_led1_already_on    ="sounds/english/answer2/en_led1_already_on.mp3"
en_led2_already_on    ="sounds/english/answer2/en_led2_already_on.mp3"
en_led3_already_on    ="sounds/english/answer2/en_led3_already_on.mp3"
en_led4_already_on    ="sounds/english/answer2/en_led4_already_on.mp3"
en_all_already_on     ="sounds/english/answer2/en_all_already_on.mp3"
en_already_servo_open ="sounds/english/answer2/en_servo_already_on.mp3"
#-----------------------------FRENCH--------------------------------------
fr_InvalidCommand	= "sounds/french/fr_Command_Error.mp3"
fr_disableConnexion ="sounds/french/fr_disableConnexion.mp3"
fr_voice_led1_off   ="sounds/french/etatSortie/fr_light_1_off.mp3"
fr_voice_led2_off   ="sounds/french/etatSortie/fr_light_2_off.mp3"
fr_voice_led3_off   ="sounds/french/etatSortie/fr_light_3_off.mp3"
fr_voice_led4_off   ="sounds/french/etatSortie/fr_light_4_off.mp3"
fr_servoClose       ="sounds/french/etatSortie/fr_servoClose.mp3"

fr_led1_already_off    ="sounds/french/reponse2/fr_led1_already_off.mp3"
fr_led2_already_off    ="sounds/french/reponse2/fr_led2_already_off.mp3"
fr_led3_already_off    ="sounds/french/reponse2/fr_led3_already_off.mp3"
fr_led4_already_off    ="sounds/french/reponse2/fr_led4_already_off.mp3"
fr_all_already_off     ="sounds/french/reponse2/fr_all_already_off.mp3"
fr_already_servoClose  ="sounds/french/reponse2/fr_servo_alredy_off.mp3"

fr_enableConnexion ="sounds/french/fr_enableConnexion.mp3"
fr_voice_led1_on   ="sounds/french/etatSortie/fr_light_1_on.mp3"
fr_voice_led2_on   ="sounds/french/etatSortie/fr_light_2_on.mp3"
fr_voice_led3_on   ="sounds/french/etatSortie/fr_light_3_on.mp3"
fr_voice_led4_on   ="sounds/french/etatSortie/fr_light_4_on.mp3"
fr_servo_open      ="sounds/french/etatSortie/fr_servo_open.mp3"

fr_led1_already_on    ="sounds/french/reponse2/fr_led1_already_on.mp3"
fr_led2_already_on    ="sounds/french/reponse2/fr_led2_already_on.mp3"
fr_led3_already_on    ="sounds/french/reponse2/fr_led3_already_on.mp3"
fr_led4_already_on    ="sounds/french/reponse2/fr_led4_already_on.mp3"
fr_all_already_on     ="sounds/french/reponse2/fr_all_already_on.mp3"
fr_already_servo_open ="sounds/french/reponse2/fr_servo_already_on.mp3"

class mainWindow:
	"""
		INFORMATION:
		*** Cette classe permet de créer la fenêtre principale et tout
			son contenu. Fait apppel à plusieurs fichiers pour le bon 
			fonctionnement de l'application.
		*** This class is used to create the main window and all
			its content. Makes use of multiple files for good
			operation of the app.
	"""
	def __init__(self):
		"""
		Variable contenant l'état de sortie des pins.Les valeurs de la liste
		varient entre 1 et 0 sauf le dernier élément qui varie entre 0 et 90 
		pour positionner le servomoteur.

		Variable containing the output state of the pins. The values of the list 
		vary between 1 and 0 except the last element which varies between 0 and 90 
		to position the servomotor.
		"""
		self._OUTPUT_STATE_PIN 	= [LOW,LOW,LOW,LOW,CLOSE]
		self._TypeConnexion 	= None
		self._Board 			= None
		self._Feedback 			= None
		self._font = ("Arial","10", "bold")
		
		# Création de l'objet tkinter / Creating the tkinter object
		self._window = tk.Tk()
		self._window.title("RS : Voice assistant (Holy)")

		self._TextLabel1 = tk.StringVar()
		self._TextLabel2 = tk.StringVar()
		self._TextLabel3 = tk.StringVar()
		self._TextLabel4 = tk.StringVar()
		self._TextLabel5 = tk.StringVar()

		self._SizeOfWindow()
		self._Menu()
		self._PositionOfWidgets()
		self._CentrolZone()
		self._ImageVoiceAssistant()
		self._StartButton()
		self._ConnectButton()
		self._ZoneText()
		self._BottomBar()

		# Création de l'objet et initialisation de l'attribut 
		# Object creation and attribute initialization
		fen_welcome   = WM.WelcomeMessage(self._window)
		self._Language = fen_welcome.LANG

		self._InitLabel()
		self._OutputState()
		self._InfoBulle()

	#_________________________Fenêtre et sous fenêtres____________________
	######################################################################
	"""
		Cette méthode permet d'initialiser les messages affichés
		sur les labels après lancement du programme (mainWindow)
		
		This method is used to initialize the messages displayed 
		on the labels after launching the program (mainWindow)
	"""
	def _InitLabel(self):
		if self._Language == "fr":
			self._TextLabel1.set(Fr_No_Act_text_L1)
			self._TextLabel2.set(Fr_No_Act_text_L2)
			self._TextLabel3.set(Fr_No_Act_text_L3)
			self._TextLabel4.set(Fr_No_Act_text_L4)
			self._TextLabel5.set(Fr_No_Act_text_L5)

		else:
			self._TextLabel1.set(En_No_Act_text_L1)
			self._TextLabel2.set(En_No_Act_text_L2)
			self._TextLabel3.set(En_No_Act_text_L3)
			self._TextLabel4.set(En_No_Act_text_L4)
			self._TextLabel5.set(En_No_Act_text_L5)

	# Création des infos bulle lors du lancement du programme
	# Creation of tooltips when launching the program
	def _InfoBulle(self):
		if self._Language == "fr":
			ToolTip(self._StartButton, msg=Fr_INFOBULLE)
			ToolTip(self._Button_1, msg=Fr_INFOBULLE)
			ToolTip(self._Button_2, msg=Fr_INFOBULLE)
			ToolTip(self._Button_3, msg=Fr_INFOBULLE)
			ToolTip(self._Button_4, msg=Fr_INFOBULLE)
			ToolTip(self._Button_5, msg=Fr_INFOBULLE)
			ToolTip(self._ConnectButton, msg=Fr_INFOBULLE)
		else:
			ToolTip(self._StartButton, msg=En_INFOBULLE)
			ToolTip(self._Button_1, msg=En_INFOBULLE)
			ToolTip(self._Button_2, msg=En_INFOBULLE)
			ToolTip(self._Button_3, msg=En_INFOBULLE)
			ToolTip(self._Button_4, msg=En_INFOBULLE)
			ToolTip(self._Button_5, msg=En_INFOBULLE)
			ToolTip(self._ConnectButton, msg=En_INFOBULLE)

	# Définition de la taille de la fenêtre / Setting window size
	def _SizeOfWindow(self):
		# obtention de la taille de l'écran / get screen size
		H_ecran = int(self._window.winfo_screenheight())
		W_ecran = int(self._window.winfo_screenwidth())
		
		# Taille de la fenetre / window size
		self._HAUTEUR = int(H_ecran/1.5)
		self._LARGEUR = int(W_ecran/1.7)
		
		# Centrage de la fenêtre / Window centering
		pos_x = int((W_ecran - self._LARGEUR)/2)
		pos_y = int((H_ecran - self._HAUTEUR)/2)

		# Taille minimale de la fenêtre / Minimum window size
		if self._LARGEUR < 803 or self._HAUTEUR < 512 :
			self._LARGEUR = 512
			self._HAUTEUR = 803
		# Taille maximale de la fenêtre / Maximum window size
		if self._LARGEUR > 903 or self._HAUTEUR > 576 :
			self._LARGEUR = 576
			self._HAUTEUR = 903

		self._window.resizable(width=False, height=False)
		self._window.geometry("{}x{}+{}+{}".format(self._LARGEUR,self._HAUTEUR,pos_x,pos_y))
		self._window.iconbitmap(F_icone)# Icone de la fenêtre / window icon


	# Barre de Menu de l'application /  Application Menu Bar
	def _Menu(self):
		self._Menubar = tk.Menu(self._window)
		# TOOLS
		self._MenuTool = tk.Menu(self._Menubar, tearoff=0)
		self._MenuTool.add_separator()
		self._MenuTool.add_command(label="Bluetooth connexion",command=self._BlueConfig)
		self._MenuTool.add_separator()
		self._MenuTool.add_command(label="Serial connexion",command=self._SerialConfig)
		self._MenuTool.add_separator()
		self._MenuTool.add_command(label="Close",command=self._Clean)
		self._Menubar.add_cascade(label="Tools",menu=self._MenuTool)
		# LANGUAGE
		self._MenuLang = tk.Menu(self._Menubar, tearoff=0)
		self._MenuLang.add_command(label="French",command=self._Fr_Choice)
		self._MenuLang.add_separator()
		self._MenuLang.add_command(label="English",command=self._En_Choice)
		self._Menubar.add_cascade(label="Language",menu=self._MenuLang)
		# HELP
		self._MenuHelp = tk.Menu(self._Menubar, tearoff=0)
		self._MenuHelp.add_command(label="About software",command=self._Aboutsoftware)
		self._MenuHelp.add_separator()
		self._MenuHelp.add_command(label="How it works",command=self._HowItWorks)
		self._MenuHelp.add_separator()
		self._MenuHelp.add_command(label="About Rachel System",command=self._AboutRachelSystem)
		self._MenuHelp.add_separator()
		self._MenuHelp.add_command(label="Contacts",command=self._contacts)
		self._Menubar.add_cascade(label="Help", menu=self._MenuHelp)

		# Configuration du Menu / Menu Setup
		self._window.config(menu=self._Menubar)

	""" 
		Méthode permettant de créer le canvas central et insert l'image
	 	de fond de la fenêtre.
		Method to create the central canvas and insert the image
		window background.
	"""
	def _CentrolZone(self):
		# Image de fond de la fenetre / Window background image
		img = Image.open(IMG_BG) # Ouverture d'image / Image opening
		# Redimensionnement de l'image / Image resizing
		image = img.resize((self._LARGEUR,self._HAUTEUR-(self._H_BOTTOM_BAR+20)))
		# Convertion d'image en image utilisable par Tk
		# Convert image to image usable by Tk
		self.image_bg = ImageTk.PhotoImage(image)

		# Canvas central / Central Canvas
		self._mainCanvas = tk.Canvas(self._window,width=self._LARGEUR,
			height=(self._HAUTEUR-(self._H_BOTTOM_BAR+20)),relief=tk.GROOVE)
		self._mainCanvas.pack(fill="both", expand=True)
		self._mainCanvas.create_image(0, 0, image=self.image_bg,anchor="nw") 

	# Position des différents widgets sur la fenetre
	# Position of the different widgets on the window
	def _PositionOfWidgets(self):
		# Hauteur du frame inférieur / lower frame height
		self._H_BOTTOM_BAR 	= int((self._HAUTEUR*5.9)/100)
		# Taille et position de l'assistante vocal sur la fenêtre
		# Size and position of the voice assistant on the window
		self._HEIGHT 		= int((self._HAUTEUR*42.97)/100) # Height of Image, Frame and Canvas 
		self._WIDTH  		= int((self._LARGEUR*24.91)/100) # Width of Image, Frame and Canvas
		self._XPOS   		= int((self._LARGEUR*7.48)/100)  # Position along X on the window
		self._YPOS   		= int((self._HAUTEUR*9.77)/100)  # Position along Y on the window
		
		# largeur et hauteur des voyants de sortie / width and height of the output lights
		self._V_height   	= int((self._HAUTEUR*0.5)/100) 
		self._V_width    	= int((self._HAUTEUR*1.2)/100)  

		# position des voyants suivant X / position of the lights along X
		self._X_pos_Voyant   = int((self._LARGEUR*43.59)/100) 

		# position des labels suivant X / position of labels along X
		self._X_pos_Label   = int((self._LARGEUR*52.31)/100) 

		# Largeur et hauteur du label / Label width and height
		self._L_Label = int((self._LARGEUR*4)/100) 
		self._H_Label = int((self._LARGEUR*0.38)/100) 

		# Position suivant Y des voyants et des labels
		# Position along Y of indicators and labels
		ecart =  int((self._HAUTEUR*12)/100)
		self._Y_Pos0 = int((self._HAUTEUR*2.1)/100) 
		self._Y_Pos1 = self._Y_Pos0 + ecart
		self._Y_Pos2 = self._Y_Pos1 + ecart
		self._Y_Pos3 = self._Y_Pos2 + ecart
		self._Y_Pos4 = self._Y_Pos3 + ecart

	# Méthode permettant d'ajouter l'image du chatbot sur la fenêtre
	# Method to add the image of the chatbot on the window
	def _ImageVoiceAssistant(self):
		# Image de l'assistant vocal / Voice assistant image
		img = Image.open(IMG_BOT)
		image = img.resize((self._WIDTH,self._HEIGHT)) 
		self.image_bot = ImageTk.PhotoImage(image)

		# Frame contenant le canvas de l'assistant vocal
		# Frame containing the voice assistant canvas
		ImgBotFrame = tk.Frame(self._mainCanvas,width=self._WIDTH,
			height=self._HEIGHT,relief=tk.GROOVE)
		ImgBotFrame.pack()

		# Canvas contenant l'image de l'assistant vocal
		# Canvas containing the voice assistant image
		ImgBotCanvas = tk.Canvas(ImgBotFrame,width=self._WIDTH,
			height=self._HEIGHT,relief=tk.GROOVE)
		ImgBotCanvas.pack(fill="both", expand=True)
		ImgBotCanvas.create_image(0, 0, image=self.image_bot ,anchor="nw") 
		# Ajout de l'image sur la fenêtre principal / Adding the image to the main window
		self._mainCanvas.create_window(self._XPOS,self._YPOS ,anchor="nw",window=ImgBotFrame)

	# Bouton permettant de démarrer l'écoute / Button to start listening
	def _StartButton(self):
		BUTTON_HEIGHT = int((self._HAUTEUR*5.86)/100)
		YPOS_BUTTON   = int((self._HAUTEUR*54.69)/100)

		img = Image.open(IMG_START)
		image = img.resize((self._WIDTH,BUTTON_HEIGHT)) 
		self.image_button = ImageTk.PhotoImage(image)
		
		self._StartButton = tk.Button(self._mainCanvas,width=self._WIDTH,height=BUTTON_HEIGHT,
			image=self.image_button, relief=tk.GROOVE,command=self._StartListening)

		self._mainCanvas.create_window(self._XPOS,YPOS_BUTTON,anchor="nw",
			window=self._StartButton)

	# Bouton permettant de connecter la carte / Button to connect card
	def _ConnectButton(self):
		x = int((self._LARGEUR*87.18)/100)
		self._ConnectButton = tk.Button(self._mainCanvas,text="Disconnected",
			width=10,bg=C_Voyant_NonAct, relief=tk.GROOVE,
			command=self._DisconnectBoard)
		self._mainCanvas.create_window(x,self._Y_Pos0,anchor="nw",window=self._ConnectButton)
	
	"""
		Methode permettant de créer les labels et boutons afin de commander
		et d'afficher les etats de sortie des objects connecté à la carte. 
	"""
	def _OutputState(self):	
		# Bouton pour allumer ou éteindre la led 1
		# Button to turn led 1 on or off
		self._Button_1 = tk.Button(self._mainCanvas,width=self._V_width,
			height=self._V_height,relief=tk.GROOVE,bg=C_Voyant_NonAct,
			command = self._UpDateLabel_1)
		self._Button_1.pack()
		self._mainCanvas.create_window(self._X_pos_Voyant,self._Y_Pos0,anchor="nw",
			window=self._Button_1)

		# Frame contenant le Label de la led 1 / Frame containing the Label of led 1
		FrameLabel1 = tk.Frame(self._mainCanvas)
		FrameLabel1.pack()

		tk.Label(FrameLabel1,textvariable=self._TextLabel1,height=self._H_Label,
			width=self._L_Label, font = self._font).pack()
		self._mainCanvas.create_window(self._X_pos_Label,self._Y_Pos0,anchor="nw",
			window=FrameLabel1)

		# Bouton pour allumer ou éteindre la led 2
		# Button to turn led 2 on or off
		self._Button_2 = tk.Button(self._mainCanvas,width=self._V_width,
			height=self._V_height,relief=tk.GROOVE,bg=C_Voyant_NonAct,
			command = self._UpDateLabel_2)
		self._Button_2.pack()
		self._mainCanvas.create_window(self._X_pos_Voyant,self._Y_Pos1,anchor="nw",
			window=self._Button_2)

		# Frame contenant le Label de la led 2 / Frame containing the Label of led 2
		FrameLabel2 = tk.Frame(self._mainCanvas)
		FrameLabel2.pack()
		
		tk.Label(FrameLabel2,textvariable=self._TextLabel2,height=self._H_Label,
			width=self._L_Label, font = self._font).pack()
		self._mainCanvas.create_window(self._X_pos_Label,self._Y_Pos1,anchor="nw",
			window=FrameLabel2)

		# Bouton pour allumer ou éteindre la led 3
		# Button to turn led 3 on or off
		self._Button_3 = tk.Button(self._mainCanvas,width=self._V_width,
			height=self._V_height,relief=tk.GROOVE,bg=C_Voyant_NonAct,
			command = self._UpDateLabel_3)
		self._Button_3.pack()
		self._mainCanvas.create_window(self._X_pos_Voyant,self._Y_Pos2,anchor="nw",
			window=self._Button_3)

		# Frame contenant le Label de la led 3 / Frame containing the Label of led 1
		FrameLabel3 = tk.Frame(self._mainCanvas)
		FrameLabel3.pack()
	
		tk.Label(FrameLabel3,textvariable=self._TextLabel3,height=self._H_Label,
			width=self._L_Label, font = self._font).pack()
		self._mainCanvas.create_window(self._X_pos_Label,self._Y_Pos2,anchor="nw",
			window=FrameLabel3)

		# Bouton pour allumer ou éteindre la led 4
		# Button to turn led 4 on or off
		self._Button_4 = tk.Button(self._mainCanvas,width=self._V_width,
			height=self._V_height,relief=tk.GROOVE,bg=C_Voyant_NonAct,
			command = self._UpDateLabel_4)
		self._Button_4.pack()
		self._mainCanvas.create_window(self._X_pos_Voyant,self._Y_Pos3,anchor="nw",
			window=self._Button_4)

		# Frame contenant le Label de la led 4 / Frame containing the Label of led 1
		FrameLabel4 = tk.Frame(self._mainCanvas)
		FrameLabel4.pack()
		
		tk.Label(FrameLabel4,textvariable=self._TextLabel4,height=self._H_Label,
			width=self._L_Label, font = self._font).pack()
		self._mainCanvas.create_window(self._X_pos_Label,self._Y_Pos3,anchor="nw",
			window=FrameLabel4)

		# Bouton permettant de mettre le servomoteur à 0° et 90°
		# Button for setting the servomotor to 0° and 90°
		self._Button_5 = tk.Button(self._mainCanvas,width=self._V_width,
			height=self._V_height,relief=tk.GROOVE,bg=C_Voyant_NonAct,
			command = self._UpDateLabel_5)
		self._Button_5.pack()
		self._mainCanvas.create_window(self._X_pos_Voyant,self._Y_Pos4,anchor="nw",
			window=self._Button_5)

		# Frame contenant le Label du servomoteur / Frame containing the label of the servo motor
		FrameLabel5 = tk.Frame(self._mainCanvas)
		FrameLabel5.pack()
		
		tk.Label(FrameLabel5,textvariable=self._TextLabel5,height=self._H_Label,
			width=self._L_Label, font = self._font).pack()
		self._mainCanvas.create_window(self._X_pos_Label,self._Y_Pos4,anchor="nw",
			window=FrameLabel5)

	# Zone/Frame ou l'audio traduit en texte est affiché
	def _ZoneText(self):
		# Position et taille
		XPOS_FRA_ZONE_TEXT = int((self._HAUTEUR*3)/100)
		YPOS_FRA_ZONE_TEXT = int((self._HAUTEUR*63.48)/100)
		W = int((self._LARGEUR*9.5)/100)
		H = int((self._HAUTEUR*1)/100)
		
		labelframe = tk.LabelFrame(self._mainCanvas, text="Voice to text ",
			bg="gray", font=("Arial","15", "bold"))
		labelframe.pack(fill="both",expand="yes")

		# create a Text widget
		self._Text = tk.Label(labelframe, width = W, height = H, 
			font= ("Arial","12", "bold"))
		self._Text.pack()
		self._mainCanvas.create_window(XPOS_FRA_ZONE_TEXT,YPOS_FRA_ZONE_TEXT,
			anchor="nw", window=labelframe)
		
	# Barre inférieur / lower bar
	def _BottomBar(self):
		Frame_BottomBar = tk.Frame(self._window, relief=tk.GROOVE,
			height= self._H_BOTTOM_BAR, bd=2, bg=Coleur)
		Label_BottomBar = tk.Label(Frame_BottomBar, text=Text_BottomBar, bg=Coleur)
		Label_BottomBar.pack()
		Frame_BottomBar.pack(side=tk.BOTTOM, fill=tk.X)

	# Message à propos du logiciel / Message about software
	def _Aboutsoftware(self):
		WM.WelcomeMessage(self._window,lang=self._Language,choiceLanguage=False)

	# Message à propos Rachel Système / Message About Rachel System
	def _AboutRachelSystem(self):
		WM.WelcomeMessage(self._window,lang=self._Language,
			choiceLanguage=False,menu="about_rs")

	# Message à propos comment ça marche / Message About How It Works
	def _HowItWorks(self):
		WM.WelcomeMessage(self._window,lang=self._Language,
			choiceLanguage=False,menu="howitworks")
	
	# Comment nous joindre / How to reach us
	def _contacts(self):
		cont.Contact(self._window)

	#____________________________Choix langage____________________________
	######################################################################
	# methods for modifying the self._Language attribute
	# methode permettant la modification de l'attribut self._Language 
	def _Fr_Choice(self):
		self._Language = "fr"
		self._UpDateLabelLang()

	def _En_Choice(self):
		self._Language = "en"
		self._UpDateLabelLang()

	# Mise à jour des textes dans les labels après changement de langue
	# Update of texts in labels after language change
	def _UpDateLabelLang(self):
		if self._Language == "fr":
			if self._OUTPUT_STATE_PIN[0] == LOW:
				self._TextLabel1.set(Fr_No_Act_text_L1)
			else:
				self._TextLabel1.set(Fr_Act_text_L1)

			if self._OUTPUT_STATE_PIN[1] == LOW:
				self._TextLabel2.set(Fr_No_Act_text_L2)
			else:
				self._TextLabel2.set(Fr_Act_text_L2)

			if self._OUTPUT_STATE_PIN[2] == LOW:
				self._TextLabel3.set(Fr_No_Act_text_L3)
			else:
				self._TextLabel3.set(Fr_Act_text_L3)

			if self._OUTPUT_STATE_PIN[3] == LOW:
				self._TextLabel4.set(Fr_No_Act_text_L4)
			else:
				self._TextLabel4.set(Fr_Act_text_L4)

			if self._OUTPUT_STATE_PIN[4] == LOW:
				self._TextLabel5.set(Fr_No_Act_text_L5)
			else:
				self._TextLabel5.set(Fr_Act_text_L5)
				
		else:
			if self._OUTPUT_STATE_PIN[0] == LOW:
				self._TextLabel1.set(En_No_Act_text_L1)
			else:
				self._TextLabel1.set(En_Act_text_L1)

			if self._OUTPUT_STATE_PIN[1] == LOW:
				self._TextLabel2.set(En_No_Act_text_L2)
			else:
				self._TextLabel2.set(En_Act_text_L2)

			if self._OUTPUT_STATE_PIN[2] == LOW:
				self._TextLabel3.set(En_No_Act_text_L3)
			else:
				self._TextLabel3.set(En_Act_text_L3)

			if self._OUTPUT_STATE_PIN[3] == LOW:
				self._TextLabel4.set(En_No_Act_text_L4)
			else:
				self._TextLabel4.set(En_Act_text_L4)

			if self._OUTPUT_STATE_PIN[4] == CLOSE:
				self._TextLabel5.set(En_No_Act_text_L5)
			else:
				self._TextLabel5.set(En_Act_text_L5)
	
	#________________________Restauration des états_______________________
	######################################################################
	# mise à low des sorties et mise a jour des boutons
	# si la connextion n'est pas etablie et la carte
	def _Restore(self):
		self._InitLabel()
		self._Button_1.config(bg = C_Voyant_NonAct)
		self._Button_2.config(bg = C_Voyant_NonAct)
		self._Button_3.config(bg = C_Voyant_NonAct)
		self._Button_4.config(bg = C_Voyant_NonAct)
		self._Button_5.config(bg = C_Voyant_NonAct)

		self._OUTPUT_STATE_PIN = [LOW,LOW,LOW,LOW,CLOSE]

		if self._Language == "fr":
			BV.BackVoice(fr_disableConnexion)
		else:
			BV.BackVoice(en_disableConnexion)

	# mise à low des sorties et mise à jour des boutons
	# apres perte de connexion ou si la connexion n'est pas etablie et la carte
	def _Restore_State_After_Lose_Connexion(self):
		if self._TypeConnexion == "serial":
			if self._SerialBoard.get_state() == False:
				self._Restore()
		if self._TypeConnexion == "bluetooth":
			if self._BluetoothBoard.getState() == False:
				self._Restore()
		if self._TypeConnexion == None:
			self._Restore()

	#_________________________Mise à jour des états_______________________
	######################################################################
	# mise à jour des labels et boutons après envois des instructions
	# update labels and buttons after sending instructions
	def _Update_Button_And_Label(self,pos,state,lang):
		# FRENCH Mise à jour des labels
		if pos == 1 and state == "on" and lang == "fr":
			self._TextLabel1.set(Fr_Act_text_L1)
			BV.BackVoice(fr_voice_led1_on)
		if pos == 1 and state == "off" and lang == "fr":
			self._TextLabel1.set(Fr_No_Act_text_L1)
			BV.BackVoice(fr_voice_led1_off)

		if pos == 2 and state == "on" and lang == "fr":
			self._TextLabel2.set(Fr_Act_text_L2)
			BV.BackVoice(fr_voice_led2_on)
		if pos == 2 and state == "off" and lang == "fr":
			self._TextLabel2.set(Fr_No_Act_text_L2)
			BV.BackVoice(fr_voice_led2_off)

		if pos == 3 and state == "on" and lang == "fr":
			self._TextLabel3.set(Fr_Act_text_L3)
			BV.BackVoice(fr_voice_led3_on)
		if pos == 3 and state == "off" and lang == "fr":
			self._TextLabel3.set(Fr_No_Act_text_L3)
			BV.BackVoice(fr_voice_led3_off)

		if pos == 4 and state == "on" and lang == "fr":
			self._TextLabel4.set(Fr_Act_text_L4)
			BV.BackVoice(fr_voice_led4_on)
		if pos == 4 and state == "off" and lang == "fr":
			self._TextLabel4.set(Fr_No_Act_text_L4)
			BV.BackVoice(fr_voice_led4_off)

		if pos == 5 and state == "on" and lang == "fr":
			self._TextLabel5.set(Fr_Act_text_L5)
			BV.BackVoice(fr_servo_open)
		if pos == 5 and state == "off" and lang == "fr":
			self._TextLabel5.set(Fr_No_Act_text_L5)
			BV.BackVoice(fr_servoClose)
		
		# ANGLISH Mise à jour des labels
		if pos == 1 and state == "on" and lang == "en":
			self._TextLabel1.set(En_Act_text_L1)
			BV.BackVoice(en_voice_led1_on)
		if pos == 1 and state == "off" and lang == "en":
			self._TextLabel1.set(En_No_Act_text_L1)
			BV.BackVoice(en_voice_led1_off)

		if pos == 2 and state == "on" and lang == "en":
			self._TextLabel2.set(En_Act_text_L2)
			BV.BackVoice(en_voice_led2_on)
		if pos == 2 and state == "off" and lang == "en":
			self._TextLabel2.set(En_No_Act_text_L2)
			BV.BackVoice(en_voice_led2_off)

		if pos == 3 and state == "on" and lang == "en":
			self._TextLabel3.set(En_Act_text_L3)
			BV.BackVoice(en_voice_led3_on)
		if pos == 3 and state == "off" and lang == "en":
			self._TextLabel3.set(En_No_Act_text_L3)
			BV.BackVoice(en_voice_led3_off)

		if pos == 4 and state == "on" and lang == "en":
			self._TextLabel4.set(En_Act_text_L4)
			BV.BackVoice(en_voice_led4_on)
		if pos == 4 and state == "off" and lang == "en":
			self._TextLabel4.set(En_No_Act_text_L4)
			BV.BackVoice(en_voice_led4_off)

		if pos == 5 and state == "on" and lang == "en":
			self._TextLabel5.set(En_Act_text_L5)
			BV.BackVoice(en_servo_open)
		if pos == 5 and state == "off" and lang == "en":
			self._TextLabel5.set(En_No_Act_text_L5)
			BV.BackVoice(en_servoClose)

		# Mise à jour des boutons
		if pos == 1 and state == "on":
			self._Button_1.config(bg = C_Voyant_Act)
		if pos == 2 and state == "on":
			self._Button_2.config(bg = C_Voyant_Act)
		if pos == 3 and state == "on":
			self._Button_3.config(bg = C_Voyant_Act)
		if pos == 4 and state == "on":
			self._Button_4.config(bg = C_Voyant_Act)
		if pos == 5 and state == "on":
			self._Button_5.config(bg = C_Voyant_Act)

		if pos == 1 and state == "off":
			self._Button_1.config(bg = C_Voyant_NonAct)
		if pos == 2 and state == "off":
			self._Button_2.config(bg = C_Voyant_NonAct)
		if pos == 3 and state == "off":
			self._Button_3.config(bg = C_Voyant_NonAct)
		if pos == 4 and state == "off":
			self._Button_4.config(bg = C_Voyant_NonAct)
		if pos == 5 and state == "off":
			self._Button_5.config(bg = C_Voyant_NonAct)

	"""
		Ces méthodes permettent de mettre à jour les informations affichées
		dans les labels indiquant l'état des sorties si le bouton est appuyé

		These methods are used to update the information displayed in
		the labels indicating the state of the outputs if the button is clicked
	"""
	def _UpDateLabel_1(self):	
		if self._OUTPUT_STATE_PIN[0] == LOW:
			self._OUTPUT_STATE_PIN[0] = HIGH
			self._SendData()
					
			if self._TypeConnexion != None and self._Feedback == "TRUE":
				if self._Language == "fr":
					self._Update_Button_And_Label(1,"on","fr")
				else:
					self._Update_Button_And_Label(1,"on","en")
			else:
				self._OUTPUT_STATE_PIN[0] = LOW
			self._Restore_State_After_Lose_Connexion()

		else:
			self._OUTPUT_STATE_PIN[0] = LOW
			self._SendData()
					
			if self._TypeConnexion != None and self._Feedback == "TRUE":
				if self._Language == "fr":
					self._Update_Button_And_Label(1,"off","fr")
				else:
					self._Update_Button_And_Label(1,"off","en")
			else:
				self._OUTPUT_STATE_PIN[0] = HIGH
			self._Restore_State_After_Lose_Connexion()


	def _UpDateLabel_2(self):
		if self._OUTPUT_STATE_PIN[1] == LOW:
			self._OUTPUT_STATE_PIN[1] = HIGH
			self._SendData()
					
			if self._TypeConnexion != None and self._Feedback == "TRUE":
				if self._Language == "fr":
					self._Update_Button_And_Label(2,"on","fr")
				else:
					self._Update_Button_And_Label(2,"on","en")
			else:
				self._OUTPUT_STATE_PIN[1] = LOW
			self._Restore_State_After_Lose_Connexion()

		else:
			self._OUTPUT_STATE_PIN[1] = LOW
			self._SendData()
					
			if self._TypeConnexion != None and self._Feedback == "TRUE":
				if self._Language == "fr":
					self._Update_Button_And_Label(2,"off","fr")
				else:
					self._Update_Button_And_Label(2,"off","en")
			else:
				self._OUTPUT_STATE_PIN[1] = HIGH
			self._Restore_State_After_Lose_Connexion()


	def _UpDateLabel_3(self):
		if self._OUTPUT_STATE_PIN[2] == LOW:
			self._OUTPUT_STATE_PIN[2] = HIGH
			self._SendData()
					
			if self._TypeConnexion != None and self._Feedback == "TRUE":
				if self._Language == "fr":
					self._Update_Button_And_Label(3,"on","fr")
				else:
					self._Update_Button_And_Label(3,"on","en")
			else:
				self._OUTPUT_STATE_PIN[2] = LOW
			self._Restore_State_After_Lose_Connexion()

		else:
			self._OUTPUT_STATE_PIN[2] = LOW
			self._SendData()
					
			if self._TypeConnexion != None and self._Feedback == "TRUE":
				if self._Language == "fr":
					self._Update_Button_And_Label(3,"off","fr")
				else:
					self._Update_Button_And_Label(3,"off","en")
			else:
				self._OUTPUT_STATE_PIN[2] = HIGH
			self._Restore_State_After_Lose_Connexion()


	def _UpDateLabel_4(self):
		if self._OUTPUT_STATE_PIN[3] == LOW:
			self._OUTPUT_STATE_PIN[3] = HIGH
			self._SendData()
					
			if self._TypeConnexion != None and self._Feedback == "TRUE":
				if self._Language == "fr":
					self._Update_Button_And_Label(4,"on","fr")
				else:
					self._Update_Button_And_Label(4,"on","en")
			else:
				self._OUTPUT_STATE_PIN[3] = LOW
			self._Restore_State_After_Lose_Connexion()

		else:
			self._OUTPUT_STATE_PIN[3] = LOW
			self._SendData()
					
			if self._TypeConnexion != None and self._Feedback == "TRUE":
				if self._Language == "fr":
					self._Update_Button_And_Label(4,"off","fr")
				else:
					self._Update_Button_And_Label(4,"off","en")
			else:
				self._OUTPUT_STATE_PIN[3] = HIGH
			self._Restore_State_After_Lose_Connexion()


	def _UpDateLabel_5(self):
		if self._OUTPUT_STATE_PIN[4] == CLOSE:
			self._OUTPUT_STATE_PIN[4] = OPEN
			self._SendData()

			if self._TypeConnexion != None and self._Feedback == "TRUE":
				if self._Language == "fr":
					self._Update_Button_And_Label(5,"on","fr")
				else:
					self._Update_Button_And_Label(5,"on","en")
			else:
				self._OUTPUT_STATE_PIN[4] = CLOSE
			self._Restore_State_After_Lose_Connexion()

		else:
			self._OUTPUT_STATE_PIN[4] = CLOSE
			self._SendData()

			if self._TypeConnexion != None and self._Feedback == "TRUE":
				if self._Language == "fr":
					self._Update_Button_And_Label(5,"off","fr")
				else:
					self._Update_Button_And_Label(5,"off","en")
			else:
				self._OUTPUT_STATE_PIN[4] = OPEN
			self._Restore_State_After_Lose_Connexion()

	#______________________Connexion et déconnection______________________
	######################################################################
	# Création d'une connexion bluetooth / Creating a bluetooth connection
	def _BlueConfig(self):
		self._Text.config(text="")
		# Si une carte est déjà connecté, on déconnecte avant d'établir 
		# une nouvelle connexion
		self._DisconnectBoard() 
		MAC_ADDRESS.ConfigMacAddress(self._window)
		self._BluetoothBoard = bluetooth.EnableBlueConnexion(self._Language)
		
		if self._BluetoothBoard.getState() == True:
			self._TypeConnexion = "bluetooth"
			self._ConnectButton.config(text="Connect",bg=C_Voyant_Act)
			if self._Language == "fr":
				BV.BackVoice(fr_enableConnexion)
			else:
				BV.BackVoice(en_enableConnexion)


	# Création d'une connexion série / Creating a serial connection
	def _SerialConfig(self):
		self._Text.config(text="")
		# Si une carte est déjà connecté, on déconnecte avant d'établir 
		# une nouvelle connexion
		self._DisconnectBoard() 
		port.UsablePort(self._window)
		self._SerialBoard = board.connectBoard()
		
		if self._SerialBoard.get_state() == True:
			self._TypeConnexion = "serial"
			self._ConnectButton.config(text="Connect",bg=C_Voyant_Act)
			if self._Language == "fr":
				BV.BackVoice(fr_enableConnexion)
			else:
				BV.BackVoice(en_enableConnexion)


	# Déconnexion de la communication / Communication Disconnect
	def _DisconnectBoard(self):
		self._Text.config(text="")
		# Port Série
		if self._TypeConnexion == "serial":
			if 	self._SerialBoard.get_state() == True:
				self._SerialBoard.DisablePort()
				self._ConnectButton.config(text="Disconnected",bg=C_Voyant_NonAct)
				self._TypeConnexion = None
				self._Restore()
				
				if self._Language == "fr":
					BV.BackVoice(fr_disableConnexion)
				else:
					BV.BackVoice(en_disableConnexion)
		# bluetooth
		if self._TypeConnexion == "bluetooth":
			if 	self._BluetoothBoard.getState() == True:
				self._BluetoothBoard.DisconnectBlue()
				self._ConnectButton.config(text="Disconnected",bg=C_Voyant_NonAct)
				self._TypeConnexion = None
				self._Restore()

				if self._Language == "fr":
					BV.BackVoice(fr_disableConnexion)
				else:
					BV.BackVoice(en_disableConnexion)			
		# Aucun type de connexion
		if self._TypeConnexion == None:
			if self._Language == "fr":
				BV.BackVoice(fr_disableConnexion)
			else:
				BV.BackVoice(en_disableConnexion)

  	#_________________________Enregistrement vocal________________________
	######################################################################
	"""
		Méthode permettant de démarrer l'écoute et d'envoyer les instructions
		via l'appel de la méthode : self._Processing_Voice_Instructions(self,sentence)
	"""
	def _StartListening(self):
		if self._TypeConnexion == "bluetooth" or self._TypeConnexion == "serial":
			Rec   = record.InputVoice(parent =self._window ,lang = self._Language)
			State = Rec.state

			self._Text.config(text=State)
			self._window.update()

			Rec.Recording()
			Rec.Voice_To_Text()
			Rec.DeleteFile()
			
			self.inputVoiceToText = Rec.text

			if self.inputVoiceToText != None:
				self._Text.config(text = self.inputVoiceToText)
			if  self.inputVoiceToText == None and self._Language == "en":
				self._Text.config(text="Finished")
			if  self.inputVoiceToText == None and self._Language == "fr":
				self._Text.config(text="Fin")

			self._window.update()

			# mise a jour des sorties
			if self.inputVoiceToText != None:
				self._Processing_Voice_Instructions(self.inputVoiceToText)
		else:
			if self._Language == "fr":
				self._Text.config(text="Aucune carte n'est connectée")
				self._Restore()
			else:
				self._Text.config(text="No board is connected")
				self._Restore()

	#______________________________Envoie données_________________________
	######################################################################
	# Envoi des données à la carte concerné / sending data to the card concerned
	def _SendData(self):
		# Port série
		if self._TypeConnexion == "serial":
			self._Feedback = self._SerialBoard.Serial_SendDate( liste = self._OUTPUT_STATE_PIN,
																langage = self._Language
																)
			if self._SerialBoard.get_state() == False:
				self._ConnectButton.config(text="Disconnected",bg=C_Voyant_NonAct)
				self._TypeConnexion = None

				if self._Language == "fr":
					BV.BackVoice(fr_disableConnexion)
				else:
					BV.BackVoice(en_disableConnexion)

		# bluetooth
		if self._TypeConnexion == "bluetooth":
			self._Feedback = self._BluetoothBoard.Blue_SendDate(liste = self._OUTPUT_STATE_PIN,
																lang = self._Language
																)
			if self._BluetoothBoard.getState() == False:
				self._ConnectButton.config(text="Disconnected",bg=C_Voyant_NonAct)
				self._TypeConnexion = None

				if self._Language == "fr":
					BV.BackVoice(fr_disableConnexion)
				else:
					BV.BackVoice(en_disableConnexion)


	# mise à jour des labels et boutons après envois des instructions vocal
	# update labels and buttons after sending voice instructions
	def _Processing_Voice_Instructions(self,sentence):
		reception = VP.String_processing(sentence,self._Language)
		# vérifie si l'audio est toujours en cours d'exécution et attend
		# checks if audio is still running and wait
		while pygame.mixer.music.get_busy() == True:
			pass

		# Pour allumer
		if reception == "led 1 on":
			run = False
			if self._OUTPUT_STATE_PIN[0] == LOW:
				self._OUTPUT_STATE_PIN[0] = HIGH
				self._SendData()
				run = True
			else:
				if self._Language =="fr" and self._Feedback == "TRUE":
					BV.BackVoice(fr_led1_already_on)
				else:
					BV.BackVoice(en_led1_already_on)
					
			if self._TypeConnexion != None and run == True and self._Feedback == "TRUE":
				self._Update_Button_And_Label(1,"on",self._Language)
			self._Restore_State_After_Lose_Connexion()
	
		if reception == "led 2 on":
			run = False
			if self._OUTPUT_STATE_PIN[1] == LOW:
				self._OUTPUT_STATE_PIN[1] = HIGH
				self._SendData()
				run = True
			else:
				if self._Language =="fr" and self._Feedback == "TRUE":
					BV.BackVoice(fr_led2_already_on)
				else:
					BV.BackVoice(en_led2_already_on)
					
			if self._TypeConnexion != None and run == True and self._Feedback == "TRUE":
				self._Update_Button_And_Label(2,"on",self._Language)
			self._Restore_State_After_Lose_Connexion()

		if reception == "led 3 on":
			run = False
			if self._OUTPUT_STATE_PIN[2] == LOW:
				self._OUTPUT_STATE_PIN[2] = HIGH
				self._SendData()
				run = True
			else:
				if self._Language =="fr" and self._Feedback == "TRUE":
					BV.BackVoice(fr_led3_already_on)
				else:
					BV.BackVoice(en_led3_already_on)
					
			if self._TypeConnexion != None and run == True and self._Feedback == "TRUE":
				self._Update_Button_And_Label(3,"on",self._Language)
			self._Restore_State_After_Lose_Connexion()

		if reception == "led 4 on":
			run = False
			if self._OUTPUT_STATE_PIN[3] == LOW:
				self._OUTPUT_STATE_PIN[3] = HIGH
				self._SendData()
				run = True
			else:
				if self._Language =="fr" and self._Feedback == "TRUE":
					BV.BackVoice(fr_led4_already_on)
				else:
					BV.BackVoice(en_led4_already_on)
					
			if self._TypeConnexion != None and run == True and self._Feedback == "TRUE":
				self._Update_Button_And_Label(4,"on",self._Language)
			self._Restore_State_After_Lose_Connexion()

		if reception == "all on":
			run = False
			if self._OUTPUT_STATE_PIN[0] == HIGH and \
			   self._OUTPUT_STATE_PIN[1] == HIGH and \
			   self._OUTPUT_STATE_PIN[2] == HIGH and \
			   self._OUTPUT_STATE_PIN[3] == HIGH:

				if self._Language =="fr" and self._Feedback == "TRUE":
					BV.BackVoice(fr_all_already_on)
				else:
					BV.BackVoice(en_all_already_on)
			else:
				self._OUTPUT_STATE_PIN[0] = HIGH
				self._OUTPUT_STATE_PIN[1] = HIGH
				self._OUTPUT_STATE_PIN[2] = HIGH
				self._OUTPUT_STATE_PIN[3] = HIGH
				
				self._SendData()
				run = True
				if self._TypeConnexion != None and run == True and self._Feedback == "TRUE":
					self._Update_Button_And_Label(1,"on",self._Language)
					self._Update_Button_And_Label(2,"on",self._Language)
					self._Update_Button_And_Label(3,"on",self._Language)
					self._Update_Button_And_Label(4,"on",self._Language)
				self._Restore_State_After_Lose_Connexion()
		
		if reception == "open the door":
			run = False
			if self._OUTPUT_STATE_PIN[4] == CLOSE:
				self._OUTPUT_STATE_PIN[4] = OPEN
				self._SendData()
				run = True
			else:
				if self._Language == "fr" and self._Feedback == "TRUE":
					BV.BackVoice(fr_already_servo_open)
				else:
					BV.BackVoice(en_already_servo_open)

			if self._TypeConnexion != None and run == True and self._Feedback == "TRUE":
				self._Update_Button_And_Label(5,"on",self._Language)	
			self._Restore_State_After_Lose_Connexion()					

		# Pour éteindre
		if reception == "led 1 off":
			run = False
			if self._OUTPUT_STATE_PIN[0] == HIGH:
				self._OUTPUT_STATE_PIN[0] = LOW
				self._SendData()
				run = True
			else:
				if self._Language =="fr" and self._Feedback == "TRUE":
					BV.BackVoice(fr_led1_already_off)
				else:
					BV.BackVoice(en_led1_already_off)
					
			if self._TypeConnexion != None and run == True and self._Feedback == "TRUE":
				self._Update_Button_And_Label(1,"off",self._Language)
			self._Restore_State_After_Lose_Connexion()

		if reception == "led 2 off":
			run = False
			if self._OUTPUT_STATE_PIN[1] == HIGH:
				self._OUTPUT_STATE_PIN[1] = LOW
				self._SendData()
				run = True
			else:
				if self._Language =="fr" and self._Feedback == "TRUE":
					BV.BackVoice(fr_led2_already_off)
				else:
					BV.BackVoice(en_led2_already_off)
					
			if self._TypeConnexion != None and run == True and self._Feedback == "TRUE":
				self._Update_Button_And_Label(2,"off",self._Language)
			self._Restore_State_After_Lose_Connexion()

		if reception == "led 3 off":
			run = False
			if self._OUTPUT_STATE_PIN[2] == HIGH:
				self._OUTPUT_STATE_PIN[2] = LOW
				self._SendData()
				run = True
			else:
				if self._Language =="fr" and self._Feedback == "TRUE":
					BV.BackVoice(fr_led3_already_off)
				else:
					BV.BackVoice(en_led3_already_off)
					
			if self._TypeConnexion != None and run == True and self._Feedback == "TRUE":
				self._Update_Button_And_Label(3,"off",self._Language)
			self._Restore_State_After_Lose_Connexion()

		if reception == "led 4 off":
			run = False
			if self._OUTPUT_STATE_PIN[3] == HIGH:
				self._OUTPUT_STATE_PIN[3] = LOW
				self._SendData()
				run = True
			else:
				if self._Language =="fr" and self._Feedback == "TRUE":
					BV.BackVoice(fr_led4_already_off)
				else:
					BV.BackVoice(en_led4_already_off)
					
			if self._TypeConnexion != None and run == True and self._Feedback == "TRUE":
				self._Update_Button_And_Label(4,"off",self._Language)
			self._Restore_State_After_Lose_Connexion()

		if reception == "all off":
			run = False
			if self._OUTPUT_STATE_PIN[0] == LOW and \
			   self._OUTPUT_STATE_PIN[1] == LOW and \
			   self._OUTPUT_STATE_PIN[2] == LOW and \
			   self._OUTPUT_STATE_PIN[3] == LOW:

				if self._Language =="fr" and self._Feedback == "TRUE":
					BV.BackVoice(fr_all_already_off)
				else:
					BV.BackVoice(en_all_already_off)
			else:
				self._OUTPUT_STATE_PIN[0] = LOW
				self._OUTPUT_STATE_PIN[1] = LOW
				self._OUTPUT_STATE_PIN[2] = LOW
				self._OUTPUT_STATE_PIN[3] = LOW

				self._SendData()
				run = True
					
				if self._TypeConnexion != None and run == True and self._Feedback == "TRUE":
					self._Update_Button_And_Label(1,"off",self._Language)
					self._Update_Button_And_Label(2,"off",self._Language)
					self._Update_Button_And_Label(3,"off",self._Language)
					self._Update_Button_And_Label(4,"off",self._Language)
				self._Restore_State_After_Lose_Connexion()
					
		if reception == "close the door":
			run = False
			if self._OUTPUT_STATE_PIN[4] == OPEN:
				self._OUTPUT_STATE_PIN[4] = CLOSE
				self._SendData()
				run = True
			else:
				if self._Language == "fr" and self._Feedback == "TRUE":
					BV.BackVoice(fr_already_servoClose)
				else:
					BV.BackVoice(en_already_servoClose)

			if self._TypeConnexion != None and run == True and self._Feedback == "TRUE":
				self._Update_Button_And_Label(5,"off",self._Language)	
			self._Restore_State_After_Lose_Connexion()

		#  En cas de commande invalide 
		if reception == "invalid command":
			if self._Language == "fr":
				BV.BackVoice(fr_InvalidCommand)
			else:
				BV.BackVoice(en_InvalidCommand)

	#___________________________Fermeture fenêtre_________________________
	######################################################################
	# Suppression du fichier contenant le port série s'il existe
	# en cas de fermeture de fenêtre 
	def _Clean(self):
		r = messagebox.askquestion("Closing the window",
			"Do you want to close the window ?")
		if r == "yes":
			if self._TypeConnexion == "serial":
				self._SerialBoard.DisablePort()

			if self._TypeConnexion == "bluetooth":
				self._BluetoothBoard.DisconnectBlue()
			try:
				os.remove("serial_port_access/serial.rachel")	
			except FileNotFoundError:
				pass
			self._window.destroy()
			
	#__________________________Méthode principale_________________________
	######################################################################
	# Méthode qui permet d'affiché et de gérer les évements tkinter
	# Method to display and manage tkinter events
	def run(self):
		self._window.protocol("WM_DELETE_WINDOW", self._Clean)
		self._window.mainloop()		