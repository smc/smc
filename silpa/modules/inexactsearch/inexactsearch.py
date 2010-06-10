#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Approximate Search
# Copyright 2008 Santhosh Thottingal <santhosh.thottingal@gmail.com>
# http://www.smc.org.in
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# If you find any bugs or have any suggestions email: santhosh.thottingal@gmail.com


import sys,os
import re
from common import *
from modules.soundex import soundex
class InexactSearch(SilpaModule):
	def __init__(self):
		self.template=os.path.join(os.path.dirname(__file__), 'approxsearch.html')
		
	@ServiceMethod			
	def bigram_average(self,str1, str2):
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
			return 	1
		bigr1 = []
		bigr2 = []
		# Make a list of bigrams for both strings - - - - - - - - - - - - - - - - - -
		#
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

		w = common / average
		return w
		
	@ServiceMethod			
	def compare (self, string1, string2):
		weight = 0
		if string1 == string2 :
			return 1
		sx = soundex.getInstance() 
		soundex_match  = sx.compare(string1,string2)
		if soundex_match == 0 : 
			weight = 1.0 
		if soundex_match == 1 : 
			weight = 0.9 
		if soundex_match == 2 :
			weight = 0.8
		if weight == 0 :
			return self.bigram_average(string1,string2) 
		else :
			return weight	
			
	@ServiceMethod			
	def search(self, text, key):
		key = key.strip()
		words = text.split()
		search_results={}
		for word in words:
			word = word.strip()
			search_results[word]= self.compare(word, key)	
		return dumps(search_results)	
	def get_module_name(self):
		return "Approximate Search"
	def get_info(self):
		return 	"Approximate Search for a string in the given text. Based on bigram search algorithm and indic soundex algorithms"	
		
def getInstance():
	return InexactSearch()
