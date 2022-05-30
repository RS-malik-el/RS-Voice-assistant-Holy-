#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AUTEUR: RACHEL SYSTEME
DATE  : 18/02/2022
DATE DE FIN : 18/02/2022
"""
import serial.tools.list_ports

class ListePortCom:
	"""
	INFORMATION:
		*Ce fichier permet de trouver les ports série disponible
		*This file is used to find available serial ports

	Attribut: 
		self.PortDispo : Contient la liste des ports disponible
		self.PortDispo : Contains the list of available ports
			
	"""

	def __init__(self):
		super(ListePortCom, self).__init__()
		self.PortDispo = [] 
		
		# Obtention des ports disponible / Obtain available ports
		for port in list(serial.tools.list_ports.comports(include_links=False)):
			self.PortDispo.append(port)