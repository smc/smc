#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2010 Santhosh Thottingal <santhosh.thottingal@gmail.com>
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
# URL: http://www.smc.org.in

import sys  
import codecs  
import os  
import string
from common import *
from utils import *
class Stemmer(SilpaModule):

	def __init__(self):
		self.template=os.path.join(os.path.dirname(__file__), 'stemmer.html')
		self.rules_file = os.path.join(os.path.dirname(__file__), 'stemmer_ml.rules')
		self.rulesDict = None
	@ServiceMethod	
	def stem(self, text):
		result = ""
		text =  normalize(text)
		if self.rulesDict == None:
			self.rulesDict = self.LoadRules()
		words=text.split(" ")
		word_count=len(words)
		result_dict = dict()
		word_iter=0
		word=""
		while word_iter < word_count:
			word = words[word_iter]
			word = self.trim(word)
			word= word.strip('!,.?:')
			word_length = len(word)
			suffix_pos_itr = 2
			word_stemmed=""
			while suffix_pos_itr < word_length :
				suffix = word[suffix_pos_itr:word_length]
				if suffix in self.rulesDict:
					word_stemmed= word[0:suffix_pos_itr] +  self.rulesDict[suffix]
					break;
				suffix_pos_itr = suffix_pos_itr+1	
			word_iter = word_iter+1
			if(word_stemmed==""):
				word_stemmed=word
			result_dict[ word ] = word_stemmed
		return dumps(result_dict)
					
	def LoadRules(self):	
		print "Loading the rules..."
		rules_dict = dict()
		line = []
		line_number = 0
		rule_number = 0
		rules_file = codecs. open(self.rules_file,encoding='utf-8', errors='ignore')
		while 1:
			line_number = line_number +1 
   			text = unicode( rules_file.readline())
			if text == "":
			      break
			if text[0] == '#': 
			      continue  #this is a comment - ignore
			text = text.split("#")[0]   #remove the comment part of the line     
			line_number = line_number +1       
			line = text.strip()  # remove unwanted space
			if(line == ""):
				  continue 
			if(len(line.split("=")) != 2):
					print "[Error] Syntax Error in the Rules. Line number: ",  line_number
				  	print "Line: "+ text
				  	continue 
	 		lhs = line.split("=") [ 0 ]  .strip()
	 		rhs = line.split("=") [ 1 ]  .strip()
	 		if(len(rhs)>0):
	 			if(lhs[0]=='"'):
	 				lhs=lhs[1:len(lhs)] # if the string is "quoted"
	 			if(lhs[len(lhs)-1]=='"'):
	 				lhs=lhs[0:len(lhs)-1] # if the string is "quoted"
	 		if(len(rhs)>0):
	 			if(rhs[0]=='"'):
	 				rhs=rhs[1:len(rhs)]  # if the string is "quoted"
	 			if(rhs[len(rhs)-1]=='"'):
	 				rhs=rhs[0:len(rhs)-1]	 # if the string is "quoted"			
	 		rule_number=rule_number+1
			rules_dict[lhs]=rhs
			#print "[", rule_number ,"] " +lhs + " : " +rhs
		print "Found ",rule_number, " rules."
		return rules_dict
	
	def trim(self,word):
		punctuations=['~','!','@','#','$','%','^','&','*','(',')','-','+','_','=','{','}','|' ,':',';','<','>','\,','.','?']
		word=word.strip()
		index=len(word)-1
		while index>0:
			if word[index] in punctuations:
				word=word[0:index]
			else:
				break 
			index=index-1	
		return word
	
	def get_module_name(self):
		return "Stemmer"
	def get_info(self):
		return 	"Malayalam Stemmer(Experimental)"
		
def getInstance():
	return Stemmer()	

	
