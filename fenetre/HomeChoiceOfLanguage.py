#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUTEUR: RACHEL SYSTEME
DATE  : 02 FEVRIER 2022
DATE DE FIN : 02/02/2022
"""
import tkinter as tk
from tkinter import simpledialog

F_icone  = "icones/icone.ico"  # icone de la fenêtre / window icon

class homeChoiceLanguage(tk.simpledialog.Dialog):
	""""
	INFORMATION:
	****Ce module permet de créer la fenêtre de choix du langage.
		Il s'exécute au l'ancement du programme.
		Il est utilisé dans le le fichier "WelcomeMessage".
	****This module is used to create the language choice window.
		It runs when the program starts.
		it's used in the "WelcomeMessage" file.
	
	PARAMETRE: / SETTING :
		parent : Fenêtre à prendre le focus / Window to take focus
			type: tkinter 

		Title  : permet de définir le titre de la fenêtre /
				 allows you to define the title of the window
			type: str
	
	ATTRIBUT:
		self.lang 
		type: str
		valeur: "fr" et "en" 
	"""
	
	def __init__(self,parent,Title="choice of language"):
		self.lang = "fr" # for french
		super(homeChoiceLanguage, self).__init__(parent,Title)	

	def body(self,master):
		# Fenêtre choix de langue / Language choice window
		self.geometry("300x150")
		self["bg"]="blue"
		self.iconbitmap(F_icone)
		self.resizable(width=False,height=False)

	def _ChoiceOfFrench(self):
		self.lang = "fr" # for french
		self.destroy()

	def _ChoiceOfEnglish(self):
		self.lang = "en" # for english
		self.destroy()

	def buttonbox(self):
		Fr_choice = tk.Button(self,text="French",width=30,height=3,
			relief=tk.GROOVE,bg="yellow",command=self._ChoiceOfFrench)
		Fr_choice.pack(pady=5)

		En_choice = tk.Button(self,text="English",width=30,height=3,
			relief=tk.GROOVE,bg="yellow",command=self._ChoiceOfEnglish)
		En_choice.pack(pady=5)