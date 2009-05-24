#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Dictionary
# Copyright 2008 Santhosh Thottingal <santhosh.thottingal@gmail.com>
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


from common import *
import os
from dictdlib import DictDB
class Dictionary(SilpaModule):
	
	def getdef(self, word, dictionary):
		dict_dir=os.path.join(os.path.dirname(__file__), 'dictionaries')
		dictdata=dict_dir+ "/"+dictionary
		dict=DictDB(dictdata)
		meanings =  dict.getdef(word)
		meaningstring= ""
		if (meanings==None):
			meaningstring = "No definition found"
			return meaningstring
		for meaning in meanings:
			meaningstring += meaning
		return meaningstring.decode("utf-8")
	def process(self,form):
		response = """
		<h2>Dictionary</h2></hr>
		<p>Enter the word to lookup in the dictionary
		</p>
		<form action="" method="post">
		 <p align="center">
		Word : <input type="text" value="%s" name="word"/>
		Dictionary :<select id="dictionary" name="dictionary" style="width:12em;">
		  <option value="freedict-eng-hin">English-Hindi</option>
		  <option value="freedict-eng-mal">English-Malayalam</option>
		</select>
		<input type="hidden" name="action" value="Dictionary">
		</br>
		<input  type="submit" id="Find_Meaning" value="Find Meaning"  style="width:12em;"/>
		</br>
		</p>
		</form>
		"""
		if(form.has_key('word')):
			search_key = form['word'].value
			dictionary =  form['dictionary'].value
			response=response % search_key
			response = response+"<h2>Search Results</h2></hr>"
			if(search_key==None):
				response = response+ "Enter a word to find meaning."
			else:		
				response = response+ "<pre> "+ self.getdef(search_key,dictionary) + "</pre> "
		else:
			response=response % ""	
		return response
	def get_module_name(self):
		return "Dictionary"
	def get_info(self):
		return 	"Bilingual Dictionaries"	
		
def getInstance():
	return Dictionary()
