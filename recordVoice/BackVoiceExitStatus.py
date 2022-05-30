#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUTEUR: RACHEL SYSTEME
DATE  : 11 FEVRIER 2022
DATE DE FIN : 11/02/2022

Ce fichier contient une fonction permettant de lire les fichiers audios
en arrière-plan afin d'annoncer l'état de sortie de nos pins.
Affiche un message d'erreur au cas où le fichier ne serait pas trouvé.

This file contains a function to play audio files
in the background to announce the release status of our pins.
Displays an error message in case the file is not found.
"""

import pygame
from tkinter import messagebox

pygame.mixer.init()

def BackVoice(file):
	try:
		pygame.mixer.music.load(file)	
		pygame.mixer.music.play()
	except pygame.error:
		messagebox.showwarning("ERROR","fichier mp3 non trouvé / mp3 file not found")