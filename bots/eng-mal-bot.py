#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# eng-mal-bot.py A Jabber buddy bot which provide eng-mal dictionary lookup service
#       
# Copyright (c) 2009
#     Santhosh Thottingal <santhosh.thottingal@gmail.com>
#     Sarath Lakshman <sarathlakshman@gmail.com> 
#     Ragsagar <ragsagar@gmail.com>
#     Ershad K <ershad92@gmail.com>
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
import wiktionary
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
        self.en_ml_db = None
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
        try:
            #search the dictionary in same directory of program
            self.en_ml_db = DictDB("freedict-eng-mal")
        except:
            #retry in standard directory of dictd
            self.en_ml_db = DictDB("/usr/share/dictd/freedict-eng-mal")    

    def loop(self):
        """ Do nothing except handling new xmpp stanzas. """
        try:
            while self.connection.Process(1):
                pass
        except KeyboardInterrupt:
            pass
            
    def messageHandler(self, conn,message_node):
        word = message_node.getBody()
        output= ""
        if  word :
            if word=="hi" or word=="Hi" or word=="Hello" or word=="hello" :
                output = "നമസ്കാരം! \n"    
                output += "ഞാന്‍ സ്വതന്ത്ര മലയാളം കമ്പ്യൂട്ടിങ്ങിന്റെ ഇംഗ്ലീഷ് മലയാളം നിഘണ്ടു."+"\n"
                output += "ഇംഗ്ലീഷ് വാക്കുകളുടെ അര്‍ത്ഥം കണ്ടുപിടിക്കാന്‍ എനിക്കു നിങ്ങളെ സഹായിക്കാന്‍ കഴിയും."+"\n"
                output += "അര്‍ത്ഥമറിയേണ്ട വാക്കു് ചോദിച്ചോളൂ."+"\n"
                output += "ശുഭദിനാശംസകള്‍ നേരുന്നു!"
            else:    
                dictoutput = self.getdef(word)
                if dictoutput:
                    output += "From SMC English-Malayalam Dictionary:\n"
                    output += dictoutput    
                    conn.send( xmpp.Message( message_node.getFrom() ,output))    
                    output = ""
                wikioutput  = wiktionary.get_def(word, "ml","ml")
                if wikioutput:
                    output += "From Malayalam wiktionary:\n"
                    output += wikioutput.encode("utf-8")
                if dictoutput== None and wikioutput==None:
                    output = "ക്ഷമിക്കണം. ഈ  വാക്കിന്റെ അര്‍ത്ഥം കണ്ടെത്താനായില്ല."
                    
                    hun = hunspell.HunSpell('/usr/share/myspell/dicts/en_US.dic', '/usr/share/myspell/dicts/en_US.aff')
                    output += "\nDid you mean: \n"
                    if hun.spell(word) is False:
                        wordlist = hun.suggest(word)
                        #print wordlist
                        for suggword in wordlist:
                            #print suggword
                            hdictoutput = self.getdef(suggword)
                            hwikioutput  = wiktionary.get_def(suggword, "ml","ml")
                            if hdictoutput is not None or hwikioutput is not None:
                                output+= "\t" + suggword + "\n"
                                
            conn.send( xmpp.Message( message_node.getFrom() ,output))    
            raise NodeProcessed  # This stanza is fully processed                    
            
    def getdef(self, word):
        
        if self.en_ml_db == None:
            return "[FATAL ERROR] Dictionary not found."    
        try:
            word = word.lower()
            return self.en_ml_db.getdef(word)[0]
        except:    
            return None
        
    def presenceHandler(self, conn, presence):
        '''Auto authorizing chat invites''' 
        if presence:
            if presence.getType() == 'subscribe':
                jabber_id = presence.getFrom().getStripped()
                self.connection.getRoster().Authorize(jabber_id)
            print presence.getFrom().getStripped()
bot = Bot(**options)
bot.loop()

