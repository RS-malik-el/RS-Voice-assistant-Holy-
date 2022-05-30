#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""	
	e-mail : rachelsysteme@gmail.com
	gitHub : https://github.com/RS-malik-el
	Donation : paypal.me/RachelSysteme

	@AUTEUR: RACHEL SYSTEME
	DATE   : 02 FEVRIER 2022
	DATE DE FIN : 24/05/2022
	
	Ce programme permet de créer une interface graphique permettant de contrôler 
	la carte arduino via le port série ou le Bluetooth. Les instructions sont 
	envoyées soit en cliquant sur les boutons, soit par commande vocale.

	@Test on the arduino board / Tester sur la carte arduino
 	NB:
		Avant d'exécuter le programme, rassurez - vous d'avoir installé au
		préalable tous les modules nécessaires au bon fonctionnement du
		programme.
	
	MODULES:
		*pillow
		*pyaudio
		*pyserial
		*pygame
		*tktooltip
		*tkhtmlview
		*speech_recognition 
"""
import fenetre.mainWindow as mw

Window = mw.mainWindow()

Window.run()