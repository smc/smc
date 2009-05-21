#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# eng-mal-bot.py A Jabber buddy bot which provide eng-mal dictionary lookup service
#       
# Copyright (c) 2009
#	 Santhosh Thottingal <santhosh.thottingal@gmail.com>
#	 Sarath Lakshman <sarathlakshman@gmail.com> 
#	 Ragsagar <ragsagar@gmail.com>
# Swathanthra Malayalam Computing(http://smc.org.in/)
#       
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#       
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import xmpp
from xmpp.protocol import *
import os
import commands
from dictdlib import DictDB

options = {
	'JID': 'eng.mal.dict@gmail.com',
	'Password': 'eng.mal.', #This is fake password.
}

class ConnectionError: pass
class AuthorizationError: pass
class NotImplemented: pass

class Bot:
	""" The main bot class. """

	def __init__(self, JID, Password):
		""" Create a new bot. Connect to the server and log in. """

		# connect...
		jid = xmpp.JID(JID)
		self.connection = xmpp.Client(jid.getDomain(), debug=[])
		result = self.connection.connect()

		if result is None:
			raise ConnectionError

		# authorize
		result = self.connection.auth(jid.getNode(), Password)

		if result is None:
			raise AuthorizationError

		self.connection.RegisterHandler('presence',self.presenceHandler)
		self.connection.RegisterHandler('message',self.messageHandler)
		# ...become available
		self.connection.sendInitPresence()
		# presence
		#self.connection.sendInitPresence(requestRoster=0)

	def loop(self):
		""" Do nothing except handling new xmpp stanzas. """
		try:
			while self.connection.Process(1):
				pass
		except KeyboardInterrupt:
			pass
			
	def messageHandler(self, conn,message_node):
		word = message_node.getBody()
		if  word :
			output = self.getdef(word)
			conn.send( xmpp.Message( message_node.getFrom() ,output))
			raise NodeProcessed  # This stanza is fully processed			
			
	def getdef(self, word):
		en_ml_db = None
		try:
			#search the dictionary in same directory of program
			en_ml_db = DictDB("freedict-eng-mal")
		except:
			#retry in standard directory of dictd
			en_ml_db = DictDB("/usr/share/dictd/freedict-eng-mal")	
		if en_ml_db == None:
			return "[FATAL ERROR] Dictionary not found."	
		try:
			return en_ml_db.getdef(word)[0]
		except:	
			return "No definitions found"
		
	def presenceHandler(self, conn, presence):
		'''Auto authorizing chat invites''' 
		if presence:
			if presence.getType() == 'subscribe':
				jabber_id = presence.getFrom().getStripped()
				self.connection.getRoster().Authorize(jabber_id)
	
bot = Bot(**options)
bot.loop()


