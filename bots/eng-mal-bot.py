#!/usr/bin/python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# eng-mal-bot.py A Jabbe buddy bot which provide eng-mal dictionary lookup service
#       
# Copyright (c) 2009 Santhosh Thottingal <santhosh.thottingal@gmail.com>
# http://smc.org.in/
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
from xmpp.roster import *
import os

options = {
	'JID': 'eng.mal.dict@gmail.com',
	'Password': 'രഹസ്യം(പറയൂല!) !',
}

def presenceHandler(conn,presence_node):
    """ Handler for playing a sound when particular contact became online """
    targetJID='node@domain.org'
    print presence_node.getFrom()
    if presence_node.getFrom().bareMatch(targetJID):
        # play a sound
        pass
def iqHandler(conn,iq_node):
    """ Handler for processing some "get" query from custom namespace"""
    reply=iq_node.buildReply('result')
    # ... put some content into reply node
    conn.send(reply)
    raise NodeProcessed  # This stanza is fully processed

        
def messageHandler(conn,message):
	user = message.getFrom()
	text = message.getBody()
	if(text):
		if " " in text:
			command, args = text.split(" ", 1)
		else:
			command, text = text, ""
		command = command.upper()
		#ഇതു വര്‍ക്കു ചെയ്യുന്നില്ല! :(
		if command == "SUBSCRIBE":
			rost=Roster().PlugIn(conn)
			rost=Roster.getRoster() 
			ros.Authorize(user)
			reply = "Authorized."
			conn.send(reply)
			raise NodeProcessed  # This stanza is fully processed
		else:
			command = "dict --database dict-en-ml '" + message.getBody() +"'"
			stdin, stdout = os.popen2(command)
			# ... put some content into reply node
			conn.send( xmpp.Message( user,stdout.read()))
			stdout.close()
			raise NodeProcessed  # This stanza is fully processed

class ConnectionError: pass
class AuthorizationError: pass
class NotImplemented: pass

class Bot:
	""" The main bot class. """

	def __init__(self, JID, Password):
		""" Create a new bot. Connect to the server and log in. """

		# connect...
		jid = xmpp.JID(JID)
		self.connection = xmpp.Client(jid.getDomain(), debug=['always', 'browser', 'testcommand'])
		result = self.connection.connect()
		
		if result is None:
			raise ConnectionError

		# authorize
		result = self.connection.auth(jid.getNode(), Password)

		if result is None:
			raise AuthorizationError

		self.connection.RegisterHandler('presence',presenceHandler)
		self.connection.RegisterHandler('iq',iqHandler)
		self.connection.RegisterHandler('message',messageHandler)
		# ...become available
		self.connection.sendInitPresence()
		# presence
		self.connection.sendInitPresence(requestRoster=0)

	def loop(self):
		""" Do nothing except handling new xmpp stanzas. """
		try:
			while self.connection.Process(1):
				pass
		except KeyboardInterrupt:
			pass

bot = Bot(**options)
bot.loop()

