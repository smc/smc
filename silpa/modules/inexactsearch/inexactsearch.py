#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Approximate Search
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


import sys
import re
from common import *

class ApproximateSearch(SilpaModule):
	
	def syllabalize(self, text):
		mm=ModuleManager()
		syllabalizer = mm.getModuleInstance("Syllabalize")
		return syllabalizer.syllabalize(text)
		
	def bigram_search(self, str1, str2, syllable_search=False):
		"""Return approximate string comparator measure (between 0.0 and 1.0)
		using bigrams.
		USAGE:
		score = bigram(str1, str2)

		ARGUMENTS:
		str1  The first string
		str2  The second string

		DESCRIPTION:
		Bigrams are two-character sub-strings contained in a string. For example,
		'peter' contains the bigrams: pe,et,te,er.

		This routine counts the number of common bigrams and divides by the
		average number of bigrams. The resulting number is returned.
		"""

		# Quick check if the strings are the same - - - - - - - - - - - - - - - - - -
		#
		if (str1 == str2):
			result_string = "<div  style='float: left; background-color: green;' title=\"  Bigram comparator : string1: %s, string2: %s. Exact Match found" % (str1, str2)
			result_string = result_string + "\">"+str1+ "</div>"
			return 	result_string

		bigr1 = []
		bigr2 = []

		# Make a list of bigrams for both strings - - - - - - - - - - - - - - - - - -
		#
		if(syllable_search):
			str1_syllables = self. syllabalize(str1)
			str2_syllables = self. syllabalize(str2)
			for i in range(1,len(str1_syllables)):
				bigr1.append(str1_syllables[i-1:i+1])
			for i in range(1,len(str2_syllables)):
				bigr2.append(str2_syllables[i-1:i+1])
		else:	
			for i in range(1,len(str1)):
				bigr1.append(str1[i-1:i+1])
			for i in range(1,len(str2)):
				bigr2.append(str2[i-1:i+1])


		# Compute average number of bigrams - - - - - - - - - - - - - - - - - - - - -
		#
		average = (len(bigr1)+len(bigr2)) / 2.0
		if (average == 0.0):
			return str1

		# Get common bigrams  - - - - - - - - - - - - - - - - - - - - - - - - - - - -
		#
		common = 0.0

		if (len(bigr1) < len(bigr2)):  # Count using the shorter bigram list
			short_bigr = bigr1
			long_bigr  = bigr2
		else:
			short_bigr = bigr2
			long_bigr  = bigr1
		if(syllable_search):
			for b in short_bigr:
				if (b in long_bigr):
					if long_bigr.index(b) == short_bigr.index(b) :
						common += 1.0
					else:
						dislocation=(long_bigr.index(b) - short_bigr.index(b))/ average
						if dislocation < 0 :
							dislocation = dislocation * -1
						common += 1.0 - dislocation
					long_bigr[long_bigr.index(b)] = []  # Mark this bigram as counted
		else:
			for b in short_bigr:
				if (b in long_bigr):
					common += 1.0
					long_bigr[long_bigr.index(b)] = []  # Mark this bigram as counted

		w = common / average
		if(w>=0.6):
			result_string = "<div  style='float: left; background-color: yellow;' title=\"  Bigram comparator string 1: %s, string 2: %s" % (str1, str2)
		else:
			if((w>0.4) & (w<0.6)):
				result_string = "<div  style='float: left; background-color: grey;' title=\"  Bigram comparator string 1: %s, string 2: %s" % (str1, str2)	
			else:
				result_string = "<div  style='float: left;' title=\"  Bigram comparator string1: %s, string2: %s" % (str1, str2)	
		result_string = result_string + "    Number of bigrams in String1: %i" % (len(bigr1))
		result_string = result_string + "    Number of bigrams in String2: %i" % (len(bigr2))
		result_string = result_string + "    Average: %i" % (average)
		result_string = result_string + "    Common: %i" % (common)
		result_string = result_string + "    Final approximate string weight: " + str(w)
		result_string = result_string + "\">"+str1+ "</div>"
		return 	result_string
	def process(self,form):
		response = """
		<h2>Inexact Search</h2></hr>
		<p>The search performed by search engines on Indic text is not effective.
		It does not take care of the inflective or agglutinative nature of the language.
		This application tries to solve that by using an inexact search algorithm based on maximum common bigram algorithm.
		
		</p>
		<p>Enter the text for searching in the below text area.
		</p>
		<form action="" method="post">
		<textarea cols='100' rows='25' name='input_text' id='input_text'>%s</textarea>
		<br/>
		<p align="center">
		Search :<input type="text" name="search_key" value="%s"/>
		Algorithm : <select id="algorithm" name="algorithm"  value="%s" style="width:12em;">
		  <option value="sb">Syllable Bigram</option>
		  <option value="lb">Letter Bigram</option>
		</select>
		</br>
		<input type="hidden" name="action" value="Approximate Search">
		
		<input  type="submit" id="ApproximateSearch" value="Search" style="width:12em;"/>
		</p>
		</form>
		"""
		algorithm = 'sb'	
		if(form.has_key('algorithm')):		
				algorithm = form['algorithm'].value
		if(form.has_key('input_text')):
			text = action=form['input_text'].value	.decode('utf-8')
			if(form.has_key('search_key')):	
				key =form['search_key'].value	.decode('utf-8')
				response=response % (text,key,algorithm)
				words=text.split(" ")
				response = response+"<h2>Search Results</h2></hr>"
				response = response+"<p>Words in green are with exact match. Words in Yellow are with approximate Match."
				response = response+" Move your mouse pointer over the words to get more information on matching.</p></hr>"
			else:
				response = response+ "Enter a string to search."
				return response % (text,"", algorithm)
			for word in words:
				word=word.strip()
				if(word>""):
					if word[0]>'0' and word[0]<'Z':
						response = response+ self.bigram_search(word, key,False)
					else:	
						if algorithm == 'sb':
							response = response+ self.bigram_search(word, key, True)
						else:
							response = response+ self.bigram_search(word, key, False)	
					response = response+ "<div  style='float: left;'>&nbsp;</div>"
		else:
			response=response % ("","","sb")	
		return response
	def get_module_name(self):
		return "Approximate Search"
	def get_info(self):
		return 	"Approximate Search for a string in the given text. Based on bigram search algorithm"	
		
def getInstance():
	return ApproximateSearch()
