#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	AUTEUR: RACHEL SYSTEME
	DATE  : 02 FEVRIER 2022
	DATE DE FIN : 03/02/2022
"""
import tkinter as tk
from tkhtmlview import HTMLLabel as html
from tkinter import simpledialog

F_icone  = "icones/icone.ico"  # icone de la fenêtre

class Contact(tk.simpledialog.Dialog):
	def __init__(self,parent,Title="How to reach us"):
		super(Contact, self).__init__(parent,Title)

	# Window / Fenêtre
	def body(self,master):
		self.geometry("400x300")
		self.iconbitmap(F_icone)
		self.resizable(width=False,height=False)

		html(self, html="""
			<p>YOUTUBE CHANNEL:    		
			<a href="https://www.youtube.com/channel/UCf4jGfp-BFp6GLd6eTptVMg">Rachel Système</a></p><br>
    		<p>LINKEDIN:
    		<a href="www.linkedin.com/in/rachel-système-82360b227">clique-moi</a></p><br>
    		<p>GROUPE FACEBOOK:
    		<a href="http://www.facebook.com/groups/4524577010939125/">clique-moi</a></p><br>
    		<p>DONATION VIA PayPal:
    		<a href="paypal.me/RachelSysteme">clique-moi</a></p><br>
    		<p>MERCI DE VOTRE CONFIANCE</p>
    		""").pack(padx=20, pady=20)


	def buttonbox(self):
		pass