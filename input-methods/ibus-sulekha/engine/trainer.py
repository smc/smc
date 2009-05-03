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
import codecs
import getopt
import sys
tz = re.compile('-[0-2]\d:00$')
class Trainer():
	def __init__(self, language="en_US"):
		self.__connection = sqlite3.connect('sulekha.db')
		# Create a cursor object to do the interacting.
		self.__cursor = self.__connection.cursor()
		self.__language=language
		
	def get_frequency(self, string):
		freq=0
		records = self.__cursor.execute("select frequency \
			 from words_" + self.__language + \
			 " where \
			 language = ? and word  = ?" , (self.__language, string))
		#print records.fetchall()
		for record in records	:
			freq = int(record[0])
		return freq
		
	def __insert_word(self, word):
		self.__cursor.execute("INSERT INTO words_"+self.__language + \
			" (id, word, frequency, language) \
			VALUES(NULL, ? , 1, ?)" , (word, self.__language))
		print ">* "+ word  + " ("+ 	 self.__language  + " : 0)" 
		self.__connection .commit()
	def __update_word(self, word, frequency):
		self.__cursor.execute("UPDATE words_"+self.__language + \
			" set  frequency= ?,  \
			language = ?  where word = ? " , (frequency, self.__language, word))
		print "> "+ word  + " ("+ 	 self.__language  + " : ",frequency ,  ")" 	
		self.__connection .commit()	
	def learn_from_file(self, file_name):
		corpus_file = codecs. open(file_name,encoding='utf-8', errors='ignore')
		while 1:
			text=corpus_file.readline()
			if text=="":
				break
			text = unicode(text)
			words=text.split()
			for word in words:
				word=word.strip()
				self.add_word(word)
				
	def create_tables(self, recreate):
		try:
			self.__cursor.execute("select count(word) from words_"+self.__language )
		except:
			recreate=True
		if recreate:
			print "Creating tables"
			self.__cursor.execute("drop TABLE words_"+self.__language)
			self.__cursor.execute("CREATE TABLE words_"+self.__language + \
				" ( id INTEGER PRIMARY KEY, \
				word VARCHAR(100),      \
				frequency NUMERIC(8),  \
				language VARCHAR(10) )")
			self.__connection .commit()
			
	def add_word(self, word):
		freq=self.get_frequency(word)
		if(freq==0):
			self.__insert_word(word)
		else:
			freq= freq+1
			self.__update_word(word, freq)	
	def set_langauge(self, language)	:
		self.language=language
	def close(self):
		self.__connection .close()
		self.__curser .close()
def print_help(out, v = 0):
	print >> out, "-l, --lang             language."
	print >> out, "-i, --input-file       input text file."
	print >> out, "-h, --help             show this message."
	print >> out, "-r, --recreate         recreate the database"
	sys.exit(v)


if __name__ == '__main__':
	shortopt = "hl:i:r"
	longopt = ["help", "lang", "input-file", "recreate"]
	language="en_US"
	input_file="/usr/share/dict/words"
	recreate=False
	opts=None
	try:
		opts, args = getopt.getopt(sys.argv[1:], shortopt, longopt)
	except getopt.GetoptError, err:
		print_help(sys.stderr, 1)
	if len(opts)==0:
		print_help(sys.stderr, 1)    

	for o, a in opts:
		if o in("-h", "--help"):
			print_help(sys.stdout)
		elif o in ("-l", "--lang"):
			language = a
		elif o in ("-i", "--input-file"):
			input_file = a
		elif o in ("-r", "--recreate"):
			recreate=True
		else:
			print >> sys.stderr, "Unknown argument: %s" % o
			print_help(sys.stderr, 1)    
	trainer =	Trainer(language)
	trainer.create_tables(recreate)
	trainer.learn_from_file	(input_file)
	
