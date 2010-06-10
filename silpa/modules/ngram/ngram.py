#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ngram
# Copyright 2008-2009 Santhosh Thottingal <santhosh.thottingal@gmail.com>
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
import os,sys
from common import *
from utils import *
from modules.syllabalizer import syllabalizer
class Ngram(SilpaModule):
	def __init__(self):
		self.template=os.path.join(os.path.dirname(__file__), 'ngram.html')
		
	@ServiceMethod							
	def syllableNgram(self, text, window_size=2):
		window_size =  int(window_size)
		words=text.split(" ")
		ngrams = []
		for word in words:
			s = syllabalizer.getInstance()
			#TODO-Normalize before taking ngram!!!
			syllables = s.syllabalize(word)
			syllable_count = len(syllables)
			window_start = 0
			window_end = 0
			while window_start + window_size <= syllable_count:
				if(window_start + window_size < syllable_count):
					window_end = window_start + window_size
				else:
					window_end = syllable_count	
				ngrams.append(syllables[window_start:window_end])
				window_start = window_start+1
		return 	dumps(ngrams)
	@ServiceMethod							
	def letterNgram(self, word, window_size=2):
		window_size =  int(window_size)
		word=word.strip()
		ngrams = []
		#TODO-Normalize before taking ngram!!!
		letter_count = len(word)
		window_start = 0
		window_end = 0
		while window_start + window_size <= letter_count:
			if(window_start + window_size < letter_count):
				window_end = window_start + window_size
			else:
				window_end = letter_count	
			ngrams.append(word[window_start:window_end])
			window_start = window_start+1
		return 	dumps(ngrams)	
	@ServiceMethod							
	def wordNgram(self,text, window_size=2):
		window_size =  int(window_size)
		words = text.split()
		ngrams = []
		word_count = len(words)
		window_start = 0
		window_end = 0
		while window_start + window_size <= word_count:
			if(window_start + window_size < word_count):
				window_end = window_start + window_size
			else:
				window_end = word_count	
			words[window_start:window_end]	
			ngrams.append(words[window_start:window_end])
			window_start = window_start+1
		return 	dumps(ngrams)
	def get_module_name(self):
		return "Ngram Library"
	def get_info(self):
		return 	"Ngram Library for English and Indian languages"	
		
def getInstance():
	return Ngram()

