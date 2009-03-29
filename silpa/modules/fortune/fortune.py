#  Spellchecker with language detection
#  coding: utf-8
#
#  Copyright © 2008  Santhosh Thottingal
#  Released under the GPLV3+ license

import os
from common import *
class Fortune(SilpaModule):
	def fortune_ml(self, word):
		if(word>""):
			command = "/usr/games/fortune -m " + word + " ./modules/fortune/database/fortune-ml"
		else:
			command = "/usr/games/fortune ./modules/fortune/database/fortune-ml"	
		command=command.encode('utf-8')	
		pipe = os.popen('{ ' + command + '; } 2>&1', 'r')
		text = pipe.read().decode('utf-8')
		pipe.close()
		return text

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
