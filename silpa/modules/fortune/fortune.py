# Fortune
# -*- coding: utf-8 -*-
#
#  Copyright © 2008  Santhosh Thottingal
#  Released under the GPLV3+ license

import os,random
from common import *
class Fortune(SilpaModule):
	def fortunes(self,infile,pattern=None):
		""" Yield fortunes as lists of lines """
		result = []
		for line in infile:
			line=line.decode("utf-8")
			if line == "%\n":
				yield result
				result = []
			else:
				if(pattern==None):
					result.append(line)
				else:
					if(line.find(pattern)==-1):
						result.append(line)		
		if result:
			yield result
			
	def fortune_ml(self, word):
		filename="./modules/fortune/database/fortune-ml"
		""" Pick a random fortune from a file """
		for index, fortune in enumerate(self.fortunes(file(filename),None)):
			if random.random() < (1.0 / (index+1)):
				chosen = fortune

		return "".join(chosen)

	def process(self, form):
		response = """
		<h2>Fortune Malayalam</h2></hr>
		<p>Enter the text for getting a random quote with the given string in the below text area.
		</p>
		<form action="" method="post">
		<input type="text" cols='100' name='input_text' id='id1' value="%s"/>
		<input  type="submit" id="Fortune" value="Fortune"  name="action" style="width:12em;"/>
		</br>
		</form>
		"""
		if(form.has_key('input_text')):
			text = form['input_text'].value	.decode('utf-8')
		else:
			text=""	
		response=response % text
		result = self.fortune_ml(text)
		response = response+"<h2>Random Quote</h2></hr>"
		response = response+"<b>"+result+"</b>"
		return response
	def get_module_name(self):
		return "Fortune Malayalam"
	def get_info(self):
		return 	"Get/Search a random Malayalam quote "
def getInstance():
	return Fortune()	
