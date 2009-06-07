#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2009 Santhosh Thottingal <santhosh.thottingal@gmail.com>
# http://www.smc.org.in
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# If you find any bugs or have any suggestions email: santhosh.thottingal@gmail.com
# URL: http://www.smc.org.in

import charmap
import sys
import re
from common import *
class Soundex(SilpaModule):
	def soundexDigit(self,char):
		index=0
		cm=charmap.charmap
		lang= charmap.language(char)
		try:
			if lang == "en_US":
				return cm["soundex_en"][cm[lang].index(char)]
			else:
				return cm["soundex"][cm[lang].index(char)]	
		except:
			'''In case of any exception- Mostly because of character not found in charmap'''
			return 0		
		return None		

	def soundex(self,name, len=5, indic=False):
		""" soundex module conforming to Knuth's algorithm
		implementation 2000-12-24 by Gregory Jorgensen
		public domain
		"""
		sndx =''
		fc = ''
		# translate alpha chars in name to soundex digits
		for c in name.lower():
			if not fc: fc = c   # remember first letter
			d = str(self.soundexDigit(c))
			# duplicate consecutive soundex digits are skipped
			if not sndx or (d != sndx[-1]):
				sndx += d
		
		# replace first digit with first alpha character
		if not indic:	sndx = fc + sndx[1:]

		# remove all 0s from the soundex code
		sndx = sndx.replace('0','')

		# return soundex code padded to len characters
		return (sndx + (len * '0'))[:len]

	def compare(self,string1, string2, indic=True):
		if indic:
			if charmap.charCompare( string1[0] , string2[0]) >=0  :
				return self.soundex(string1, indic=True)==self.soundex(string2, indic=True)
		else:		
			   return self.soundex(string1, indic=False)==self.soundex(string2, indic=False)	
			   
	def process(self,form):
		response = """
		<h2>Soundex</h2></hr>
		<p>'Sounds like' search across Indian Languages.
		</p>
		<p>Enter the text for searching in the below text area. You can enter the text in say, Hindi and search a Malayalam word in that. If the pronunciation of the search key is similar to any word in the text, it will be highlighted.
		All Indian Languages and English are supported. <a href="http://en.wikipedia.org/wiki/Soundex">More about soundex</a></p>
		<form action="" method="post">
		<textarea cols='100' rows='25' name='input_text' id='input_text'>%s</textarea>
		<br/>
		<p align="center">
		Search :<input type="text" name="search_key" value="%s"/>
		</br>
		<input type="hidden" name="action" value="Soundex">
		<input  type="submit" id="ApproximateSearch" value="Search" style="width:12em;"/>
		</p>
		</form>
		"""
		if(form.has_key('input_text')):
			text = action=form['input_text'].value	.decode('utf-8')
			if(form.has_key('search_key')):	
				key =form['search_key'].value	.decode('utf-8')
				response=response % (text,key)
				words=text.split(" ")
				response = response+"<h2>Search Results</h2></hr>"
			else:
				response = response+ "Enter a string to search."
				return response % (text,"", algorithm)
			for word in words:
				word=word.strip()
				if(word>""):
					if word[0]>'0' and word[0]<'Z':
						if self.compare(word, key, False) :
							response += "<div  style='float: left; background-color: yellow;'>"+word+"</div>"
						else:
							response += "<div  style='float: left;'>"+word+"</div>"
					else:
						if self.compare(word, key,  True) :
							response += "<div  style='float: left; background-color: yellow;'>"+word+"</div>"
						else:
							response += "<div  style='float: left;'>"+word+"</div>"
							
					response = response+ "<div  style='float: left;'>&nbsp;</div>"
		else:
			response=response % ("","")	
		return response
	def get_module_name(self):
		return "Soundex"
	def get_info(self):
		return 	"Soundex Algorithm for Indian Languages and 'sounds like' search across Indian Languages"	
		
def getInstance():
	return Soundex()

					
