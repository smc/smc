# Fortune
# -*- coding: utf-8 -*-
#
#  Copyright © 2009  Santhosh Thottingal <santhosh.thottingal@gmai.com>
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
				continue
			else:
				if(pattern==None):
					result.append(line)
				else:
					if(line.find(pattern)>0):
						result.append(line)		
		if result:
			return result

			
	def fortune_ml(self, pattern):
		filename = os.path.join(os.path.dirname(__file__), 'database/fortune-ml')
		""" Pick a random fortune from a file """
		fortunes_list=self.fortunes(file(filename),pattern)
		chosen=""
		if fortunes_list:
			chosen= random.choice(fortunes_list)
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
			response=response % text
		else:
			text= None
			response=response % ""
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
