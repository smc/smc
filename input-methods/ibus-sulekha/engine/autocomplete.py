# vim:set et sts=4 sw=4:
#
# ibus-sulekha - The Sulekha engine for IBus
#
# Copyright(c) 2009 Santhosh Thottingal <santhosh.thottingal@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import sqlite3
import re
import os
import sys
tz = re.compile('-[0-2]\d:00$')
class Autocomplete():
	def __init__(self, language="en_US"):
		database=os.path.dirname(__file__) +'/sulekha.db'
		self.__connection = sqlite3.connect(database)
		# Create a cursor object to do the interacting.
		self.__cursor = self.__connection.cursor()
		self.__language=language
	def get_autocompletion_suggestions(self, string):
		wordlist=[]
		records =self.__cursor.execute("select word from words_"+ self.__language + \
		" where language = '"+ self.__language +"' \
		and word  like '"+ string + "%' \
		order by frequency desc  limit 5 " )
		for record in records:
			word = tz.sub('', record[0])
			wordlist.append(word)
		return wordlist

	def set_langauge(self, language)	:
		self.language=language


if __name__ == '__main__':
	autocomplete=	Autocomplete()
	candidate_list= autocomplete.get_autocompletion_suggestions(sys.argv[1])	
	for candidate in candidate_list:
		print candidate
	
