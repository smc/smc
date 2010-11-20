#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# eng-hin-bot.py A Jabber buddy bot which provide eng-hin dictionary lookup service
#       
# Copyright (c) 2009
#     Santhosh Thottingal <santhosh.thottingal@gmail.com>
#     Sarath Lakshman <sarathlakshman@gmail.com> 
#     Ragsagar <ragsagar@gmail.com>
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
        'JID': 'username',
        'Password': 'password',
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
            if word=="hi" or word=="Hi" or word=="Hello" or word=="hello" :
                name=self.connection.getRoster().getName(message_node.getFrom().getNode()+"@"+message_node.getFrom().getDomain())
                if name:
                    output = "Hello "+ name +",\n"
                else:
                    output = "Hello \n"    
                output += "Greetings from English-Hindi Bilingual Dictionary bot by SMC!"+"\n"
                output += "I can help you to find meaning of a Hindi or English word."+"\n"
                output += "To get a meaning of a word, send me the word."+"\n"
                output += "Have a nice day!"
            else:    
                output = self.getdef(word)
            conn.send( xmpp.Message( message_node.getFrom() ,output))
            raise NodeProcessed  # This stanza is fully processed            
            
    def getdef(self, word):
        en_hi_db = None
        hi_en_db = None
        meaning_str = ""
        #search the dictionary in same directory of program
        en_hi_db = DictDB("/usr/share/dictd/freedict-eng-hin")
        hi_en_db = DictDB("/usr/share/dictd/freedict-hin-eng")
        if en_hi_db == None or hi_en_db == None:
            return "[FATAL ERROR] Dictionary not found."    
        try:
            meanings = en_hi_db.getdef(word)
            for meaning in meanings:
                meaning_str+=meaning
            meanings = hi_en_db.getdef(word.encode("utf-8"))
            for meaning in meanings:
                meaning_str+=meaning
            if meaning_str == ""    :
                return "Sorry, No definition found."
            else:
                return meaning_str
        except:
            return "Sorry, No definition found."
                
        
    def presenceHandler(self, conn, presence):
        '''Auto authorizing chat invites''' 
        if presence:
            if presence.getType() == 'subscribe':
                jabber_id = presence.getFrom().getStripped()
                self.connection.getRoster().Authorize(jabber_id)
        print presence.getFrom().getStripped()
bot = Bot(**options)
bot.loop()


