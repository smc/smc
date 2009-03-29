#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys  
import codecs  
import os  
import string
import curses.ascii 
from common import SilpaModule
class Lemmatizer(SilpaModule):

	def __init__(self):
		self.rules_file = "./modules/lemmatizer/lemmatizer_ml.rules"
		self.rulesDict = dict()
		
	def lemmatize(self, text):
		result = ""
		self.rulesDict = self.LoadRules()
		words=text.split(" ")
		word_count=len(words)
		result_dict = dict()
		word_iter=0
		word=""
		while word_iter < word_count:
			word = words[word_iter]
			word = self.trim(word)
			word_length = len(word)
			suffix_pos_itr = 2
			word_lemmatized=""
			while suffix_pos_itr < word_length :
				suffix = word[suffix_pos_itr:word_length]
				if suffix in self.rulesDict:
					word_lemmatized= word[0:suffix_pos_itr] +  self.rulesDict[suffix]
					break;
				suffix_pos_itr = suffix_pos_itr+1	
			word_iter = word_iter+1
			if(word_lemmatized==""):
				word_lemmatized=word
			result_dict[ word ] = word_lemmatized
		return result_dict
					
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
	def process(self, form):
		response = """
		<h2>Lemmatization</h2></hr>
		<p>Enter the text for lemmatization in the below text area.
		 Language of each  word will be detected. 
		 You can give the text in any language and even with mixed language
		</p>
		<form action="" method="post">
		<textarea cols='100' rows='25' name='input_text' id='id1'>%s</textarea>
		<input  type="submit" id="Lemmatize" value="Lemmatize"  name="action" style="width:12em;"/>
		<input type="reset" value="Clear" style="width:12em;"/>
		</br>
		</form>
		"""
		if(form.has_key('input_text')):
			text = action=form['input_text'].value	.decode('utf-8')
			response=response % text
			result_dict = self.lemmatize(text)
			response = response+"<h2>Lemmatization Results</h2></hr>"
			response = response+"<table class=\"table1\"><tr><th>Word</th><th>Lemmatized form</th></tr>"
			for key in result_dict:
				response = response+"<tr><td>"+key+"</td><td>"+result_dict[key]+"</td></tr>"
			response = response+"</table>	"
		else:
			response=response % ""	
		return response
	def get_module_name(self):
		return "Lemmatizer"
	def get_info(self):
		return 	"Malayalam Lemmatizer(Experimental)"
		
def getInstance():
	return Lemmatizer()	
if __name__ == "__main__":
	lemmatizer= Lemmatizer()
	lemmatizer.rules_file="/home/santhosh/www/malayalam.map"
	lemmatizer.lemmatize("മുദ്രാവാക്യവുമായി മുറ്റത്തില്‍")
	
