#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys  
import codecs  
import os  
import string
import curses.ascii 
class Lemmatizer:

	def __init__(self):
		self.input_filename =""
		self.output_filename = ""
		self.rules_file = ""
		self.rulesDict = dict()
		
	def Lemmatize(self):
		result = ""
		self.rulesDict = self.LoadRules()
		if self.input_filename :
			uni_file = codecs.open(self.input_filename, encoding = 'utf-8', errors = 'ignore')
		else :
			uni_file = codecs.open(sys.stdin, encoding = 'utf-8', errors = 'ignore')			
		text = ""
		if self.output_filename :
			output_file = codecs.open(self.output_filename, encoding = 'utf-8', errors = 'ignore',  mode='w+')			
		line_number = 0
		while 1:
   			text = uni_file.readline()
   			line_number = line_number + 1
			if text == "":
				break
			words = text.split(" ")
			word_count = len(words)
			word_iter = 0
			word = ""
			while word_iter < word_count:
				word = words[word_iter]
				word_length = len(word)
				print word_length
				suffix_pos_itr = 2
				while suffix_pos_itr   <  word_length : 
					suffix = word[suffix_pos_itr:word_length]
					if suffix in self.rulesDict:
						word = word[0:suffix_pos_itr] +  self.rulesDict[suffix]
						break
					suffix_pos_itr = suffix_pos_itr + 1	
				word_iter = word_iter + 1
				print word	
				result = result + word + ""
			result="\n"	
		return result
	def Lemmatize(self, text):
		result = ""
		self.rulesDict = self.LoadRules()
		words=text.split(" ")
		word_count=len(words)
		word_iter=0
		word=""
		while word_iter < word_count:
			word = words[word_iter]
			word = self.trim(word)
			word_length = len(word)
			suffix_pos_itr = 2
			while suffix_pos_itr < word_length :
				suffix = word[suffix_pos_itr:word_length]
				if suffix in self.rulesDict:
					word= word[0:suffix_pos_itr] +  self.rulesDict[suffix]
					break;
				suffix_pos_itr = suffix_pos_itr+1	
			word_iter = word_iter+1
			#print word	
			result = result + word + " "
		return result
					
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
if __name__ == "__main__":
	lemmatizer= Lemmatizer()
	lemmatizer.rules_file="/home/santhosh/www/malayalam.map"
	lemmatizer.Lemmatize("മുദ്രാവാക്യവുമായി മുറ്റത്തില്‍")
	
