#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# eng-mal-bot.py A Jabbe buddy bot which provide eng-mal dictionary lookup service
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

options = {
	'JID': 'eng.mal.dict@gmail.com',
	'Password': '*******',
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
			
	def messageHandler(self, conn,mess_node):
	
		if(mess_node.getBody()):
			command = "dict --database dict-en-ml '" + mess_node.getBody() +"'"
			output = commands.getoutput(command)
			if output.find('No definitions found') is not -1:
				print "No definitions found"
				conn.send( xmpp.Message( mess_node.getFrom(),'No Definitions Found'))
			else :
                             	print "definition found"
				conn.send( xmpp.Message( mess_node.getFrom() ,output))
			raise NodeProcessed  # This stanza is fully processed			
			
			
			
	def presenceHandler(self, conn, presence):

		'''Auto authorizing chat invites''' 
		if presence:
			if presence.getType()=='subscribe':
				jid = presence.getFrom().getStripped()
				self.connection.getRoster().Authorize(jid)
	
		targetJID='node@domain.org'
		print presence.getFrom()
		if presence.getFrom().bareMatch(targetJID):
			# play a sound
			pass
    	    


bot = Bot(**options)
bot.loop()


