#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUTEUR: RACHEL SYSTEME
DATE  : 03 FEVRIER 2022
DATE DE FIN : 03/02/2022
"""
import speech_recognition as sr
import fenetre.welcomeMessage as WM
import pyaudio
import pygame
import wave
import os

# Enregistrement en morceaux de 1024 échantillons
# Record in chunks of 1024 samples
chunk = 1024  
# 16 bits per sample / 16 bits par échantillon
sample_format = pyaudio.paInt16  
channels = 2
# Enregistrement à 44100 échantillons par seconde
# Record at 44100 samples per second
fs = 44100  
seconds = 4
filename = "INPUT.wav"


class InputVoice:
	"""
		INFORMATION:
		****Ce fichier permet d'accéder au micro du pc, d'enregistrer un fichier
			audio de 4 secondes puis de le traduire en texte.
			Utiliser dans le fichier "mainWindow".
		****This file allows you to access the pc's microphone, to save an audio file
			of 4 seconds and then translate it into text.
			Use in the "mainWindow" file.

		PARAMETRE: / SETTING:
			parent: fenêtre à prendre le focus
				value: None
			lang : permet de choisir la langue de sortie du texte
				value: "fr" et "en" 

		METHODES:
			 Recording()
			 Voice_To_Text()
			 DeleteFile()

		ATTRIBUTS:
			self.state: Indique l'état du micro (enregistrement ou fin) 
				type: str
			self.text: Contient l'audio traduit en texte
				type : str
	"""

	def __init__(self, lang, parent=None):
		self.fen 	= parent
		self.langue = lang
		self.text 	= None
		if self.langue == "en":
			self.state = "Recording..."
		else:
			self.state = "Enregistrement..."

		pygame.mixer.init()
		pygame.mixer.music.stop()


	# Enregistrement de l'audio / Audio recording
	def Recording(self):
		# Créer une interface vers PortAudio
		# Create an interface to PortAudio
		p = pyaudio.PyAudio() 

		stream = p.open(format=sample_format,
		                channels=channels,
		                rate=fs,
		                frames_per_buffer=chunk,
		                input=True)

		# Initialiser le tableau pour stocker les cadres
		# Initialize array to store frames
		frames = []  

		# Stocker les données en morceaux pendant 4 secondes
		# Store data in chunks for 4 seconds
		for i in range(0, int(fs / chunk * seconds)):
		    data = stream.read(chunk)
		    frames.append(data)

		# Stop and close the stream / Arrêter et fermer le flux
		stream.stop_stream()
		stream.close()
		# Terminate the PortAudio interface
		p.terminate()

		# Enregistrez les données enregistrées dans un fichier WAV
		# Save the recorded data as a WAV file
		wf = wave.open(filename, 'wb')
		wf.setnchannels(channels)
		wf.setsampwidth(p.get_sample_size(sample_format))
		wf.setframerate(fs)
		wf.writeframes(b''.join(frames))
		wf.close()


	# Traduction du fichier audio en texte
	# Translation of audio file to text
	def Voice_To_Text(self):
		# initialize the recognizer / initialise le reconnaisseur
		r = sr.Recognizer()
		try:
			# Open the file
			with sr.AudioFile(filename) as source:
			    # listen for the data (load audio to memory)
				audio_data = r.record(source)
			    # recognize (convert from speech to text)
				self.text = r.recognize_google(audio_data,language=self.langue)

		except sr.UnknownValueError:
			pass
		except sr.RequestError:
			# Message d'erreur / Error message
			voice = WM.WelcomeMessage(self.fen,lang=self.langue,
						Title="Error connexion",
						choiceLanguage=False,menu="error")


	# Suppression du fichier / Delete file 
	def DeleteFile(self):
		os.remove(filename)