#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUTEUR: RACHEL SYSTEME
DATE  : 11 FEVRIER 2022
DATE DE FIN : 15/02/2022

"""
# Module permettant de lire les fichiers audio en arrière plan
# Module to play audio files in the background
import recordVoice.BackVoiceExitStatus as bv

# Fichiers audio pour confirmer l'exécution de la tâche
# Audio files to confirm task completion
fr_answer_led1_on ="sounds/french/reponse/fr_answer_led1_on.mp3"
fr_answer_led2_on ="sounds/french/reponse/fr_answer_led2_on.mp3"
fr_answer_led3_on ="sounds/french/reponse/fr_answer_led3_on.mp3"
fr_answer_led4_on ="sounds/french/reponse/fr_answer_led4_on.mp3"
fr_answer_all_on  ="sounds/french/reponse/fr_answer_all_on.mp3"
fr_servo_on       ="sounds/french/reponse/fr_answer_servo_on.mp3"

fr_answer_led1_off ="sounds/french/reponse/fr_answer_led1_off.mp3"
fr_answer_led2_off ="sounds/french/reponse/fr_answer_led2_off.mp3"
fr_answer_led3_off ="sounds/french/reponse/fr_answer_led3_off.mp3"
fr_answer_led4_off ="sounds/french/reponse/fr_answer_led4_off.mp3"
fr_answer_all_off  ="sounds/french/reponse/fr_answer_all_off.mp3"
fr_servo_off       ="sounds/french/reponse/fr_answer_servo_off.mp3"

# Instructions pour gerer les composants connecté à l'assistant vocal
# Instructions for managing components connected to the voice assistant
fr_led1_on  	= "ALLUME LA LED 1"
fr_led2_on  	= "ALLUME LA LED 2"
fr_led3_on  	= "ALLUME LA LED 3"
fr_led4_on  	= "ALLUME LA LED 4"
fr_all_led_on   = "ALLUME TOUTES LES LED"
fr_servom_on 	= "OUVRE LA PORTE"

fr_lamp1_on  	= "ALLUME LA LAMPE 1"
fr_lamp2_on  	= "ALLUME LA LAMPE 2"
fr_lamp3_on  	= "ALLUME LA LAMPE 3"
fr_lamp4_on  	= "ALLUME LA LAMPE 4"
fr_all_lamp_on  = "ALLUME TOUTES LES LAMPES"

fr_led1_off  	= "ÉTEINS LA LED 1"
fr_led2_off  	= "ÉTEINS LA LED 2"
fr_led3_off  	= "ÉTEINS LA LED 3"
fr_led4_off  	= "ÉTEINS LA LED 4"
fr_all_led_off  = "ÉTEINS TOUTES LES LED"
fr_servom_off 	= "FERME LA PORTE"

fr_lamp1_off  	 = "ÉTEINS LA LAMPE 1"
fr_lamp2_off  	 = "ÉTEINS LA LAMPE 2"
fr_lamp3_off  	 = "ÉTEINS LA LAMPE 3"
fr_lamp4_off  	 = "ÉTEINS LA LAMPE 4"
fr_all_lamp_off  = "ÉTEINS TOUTES LES LAMPES"

# Fichiers audio pour confirmer l'exécution de la tâche
# Audio files to confirm task completion
en_answer_led1_on ="sounds/english/answer/en_answer_led1_on.mp3"
en_answer_led2_on ="sounds/english/answer/en_answer_led2_on.mp3"
en_answer_led3_on ="sounds/english/answer/en_answer_led3_on.mp3"
en_answer_led4_on ="sounds/english/answer/en_answer_led4_on.mp3"
en_answer_all_on  ="sounds/english/answer/en_answer_all_on.mp3"
en_servo_on       ="sounds/english/answer/en_answer_servo_on.mp3"

en_answer_led1_off ="sounds/english/answer/en_answer_led1_off.mp3"
en_answer_led2_off ="sounds/english/answer/en_answer_led2_off.mp3"
en_answer_led3_off ="sounds/english/answer/en_answer_led3_off.mp3"
en_answer_led4_off ="sounds/english/answer/en_answer_led4_off.mp3"
en_answer_all_off  ="sounds/english/answer/en_answer_all_off.mp3"
en_servo_off       ="sounds/english/answer/en_answer_servo_off.mp3"

# Instructions pour gerer les composants connecté à l'assistant vocal
# Instructions for managing components connected to the voice assistant
en_led1_on  	 = "LIGHT ONE ON"
en_led2_on  	 = "LIGHT TWO ON"
en_led3_on  	 = "LIGHT THREE ON"
en_led4_on  	 = "LIGHT FOUR ON"
en_all_led_on    = "ALL LIGHTS ON"
en_all_led_on_   = "ALL LIGHT ON"
en_servom_on 	 = "OPEN THE DOOR"

en_led1_off  	 = "LIGHT ONE-OFF"
en_led2_off  	 = "LIGHT TWO OFF"
en_led3_off 	 = "LIGHT THREE OFF"
en_led4_off 	 = "LIGHT FOUR OFF"
en_all_led_off   = "ALL LIGHTS OFF"
en_all_led_off_  = "ALL LIGHT OFF"
en_servom_off 	 = "CLOSE THE DOOR"


"""
	INFORMATION:
	****Fonction permettant de traiter le texte provenant du fichier 
		audio enregistré via le micro du pc en instruction.
		Si le teste renseigné en paramètre correspond aux instructions
		pré-enregistré alors la fonction renvoi un message permettant ainsi 
		à la fonction : Processing_Voice_Instructions()	
		contenu dans le fichier "mainWindow" d'effectuer la tâche demandé.
	****Function to process text from file audio recorded via pc mic in 
		instruction. If the test given in parameter corresponds to the instructions
		pre-recorded then the function returns a message thus allowing
		to the function: Processing_Voice_Instructions()
		contained in the "mainWindow" file to perform the requested task

	PARAMETRE:
		sentence : Texte à traiter (instruction envoyée)
			type : str
		lang     : langue de sortie
			type : str
"""
def String_processing(sentence,lang):

	SENTENCE = sentence.upper()

	# Pour allumer / To turn on 
	if fr_led1_on == SENTENCE or fr_lamp1_on == SENTENCE or \
	   en_led1_on == SENTENCE:

		if lang == "fr":
			bv. BackVoice(fr_answer_led1_on)
		else:
			bv. BackVoice(en_answer_led1_on)
		return "led 1 on"

	if fr_led2_on == SENTENCE or fr_lamp2_on == SENTENCE or \
	   en_led2_on == SENTENCE:

		if lang == "fr":
			bv. BackVoice(fr_answer_led2_on)
		else:
			bv. BackVoice(en_answer_led2_on)
		return "led 2 on"

	if fr_led3_on == SENTENCE or fr_lamp3_on == SENTENCE or \
	   en_led3_on == SENTENCE:

		if lang == "fr":
			bv. BackVoice(fr_answer_led3_on)
		else:
			bv. BackVoice(en_answer_led3_on)
		return "led 3 on"

	if fr_led4_on == SENTENCE or fr_lamp4_on == SENTENCE or \
	   en_led4_on == SENTENCE:
		if lang == "fr":

			bv. BackVoice(fr_answer_led4_on)
		else:
			bv. BackVoice(en_answer_led4_on)
		return "led 4 on"

	if fr_all_led_on == SENTENCE or fr_all_lamp_on == SENTENCE or \
	   en_all_led_on == SENTENCE or en_all_led_on_ == SENTENCE:

		if lang == "fr":
			bv. BackVoice(fr_answer_all_on)
		else:
			bv. BackVoice(en_answer_all_on)
		return "all on"

	if fr_servom_on == SENTENCE or en_servom_on == SENTENCE:
		if lang == "fr":
			bv. BackVoice(fr_servo_on)
		else:
			bv. BackVoice(en_servo_on)
		return "open the door"


	# Pour éteindre / To turn off
	if fr_led1_off == SENTENCE or fr_lamp1_off == SENTENCE or \
	   en_led1_off == SENTENCE:

		if lang == "fr":
			bv. BackVoice(fr_answer_led1_off)
		else:
			bv. BackVoice(en_answer_led1_off)
		return "led 1 off"

	# pour eteindre
	if fr_led2_off == SENTENCE or fr_lamp2_off == SENTENCE or \
	   en_led2_off == SENTENCE:

		if lang == "fr":
			bv. BackVoice(fr_answer_led2_off)
		else:
			bv. BackVoice(en_answer_led2_off)
		return "led 2 off"

	if fr_led3_off == SENTENCE or fr_lamp3_off == SENTENCE or \
	   en_led3_off == SENTENCE:

		if lang == "fr":
			bv. BackVoice(fr_answer_led3_off)
		else:
			bv. BackVoice(en_answer_led3_off)
		return "led 3 off"

	if fr_led4_off == SENTENCE or fr_lamp4_off == SENTENCE or \
	   en_led4_off == SENTENCE:
	   
		if lang == "fr":
			bv. BackVoice(fr_answer_led4_off)
		else:
			bv. BackVoice(en_answer_led4_off)
		return "led 4 off"

	if fr_all_led_off == SENTENCE or fr_all_lamp_off == SENTENCE or \
	   en_all_led_off == SENTENCE or en_all_led_off_ == SENTENCE:

		if lang == "fr":
			bv. BackVoice(fr_answer_all_off)
		else:
			bv. BackVoice(en_answer_all_off)
		return "all off"

	if fr_servom_off == SENTENCE:
		if lang == "fr":
			bv. BackVoice(fr_servo_off)
		else:
			bv. BackVoice(en_servo_off)
		return "close the door"
		
	# Retour par défaut
	return "invalid command"