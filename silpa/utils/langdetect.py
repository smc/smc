#  Spellchecker with language detection
#  coding: utf-8
#
#  Copyright © 2008  Santhosh Thottingal
#  Released under the GPLV3+ license

from common import *

class LangDetect(SilpaModule):
		
	def detect_lang(self, text):
		words=text.split(" ")
		word_count=len(words)
		word_iter=0
		word=""
		result_dict=dict()
		while word_iter < word_count:
			word=words[word_iter]
			if(word):
				length = len(word)
				index = 0
				while index < length:
					letter=word[index]
					if not letter.isalpha():
						index=index+1	
						continue
					if ((letter >= u'ം') &  (letter <=u'൯')):
						result_dict[word]= "ml_IN"
						break;
					if ((letter >= u'ঁ') &  (letter <= u'৺')):
						result_dict[word]= "bn_IN"
						break
					if ((letter >= u'ँ') &  (letter <= u'ॿ')):
						result_dict[word]= "hi_IN"
						break
					if ((letter >=u'ઁ') &  (letter <= u'૱')):
						result_dict[word]= "gu_IN"
						break
					if ((letter >= u'ਁ') &  (letter <=u'ੴ')):
						result_dict[word]= "pa_IN"
						break
					if ((letter >= u'ಂ') &  (letter <=u'ೲ')):
						result_dict[word]= "kn_IN"
						break
					if ((letter >= u'ଁ') &  (letter <= u'ୱ')):
						result_dict[word]= "or_IN"
						break
					if ((letter >=u'ஂ') &  (letter <= u'௺')):
						result_dict[word]= "ta_IN"
						break
					if ((letter >=u'ఁ') &  (letter <= u'౯')):
						result_dict[word]= "te_IN"
						break
					if ((letter <= u'z')):
						result_dict[word]= "en_US"
						break
					index=index+1	
			word_iter=word_iter+1	
		return result_dict
	def process(self,form):
		response = """
		<h2>Language Detection</h2></hr>
		<p>Enter the text for detecting the language in the below text area.
		 Language of each  word will be detected. 
		 You can give the text in any language and even with mixed language
		</p>
		<form action="" method="post">
		<textarea cols='100' rows='25' name='input_text' id='id1'>%s</textarea>
		<input  type="submit" id="Detect Language" value="Detect Language"  name="action" style="width:12em;"/>
		<input type="reset" value="Clear" style="width:12em;"/>
		</br>
		</form>
		"""
		if(form.has_key('input_text')):
			text = action=form['input_text'].value	.decode('utf-8')
			response=response % text
			detected_lang_dict = self.detect_lang(text)
			response = response+"<h2>Language Detection Results</h2></hr>"
			response = response+"<table class=\"table1\"><tr><th>Word</th><th>Language</th></tr>"
			for key in detected_lang_dict:
				response = response+"<tr><td>"+key+"</td><td>"+detected_lang_dict[key]+"</td></tr>"
			response = response+"</table>	"
		else:
			response=response % ""	
		return response
	def get_module_name(self):
		return "Indian Language Detector"
	def get_info(self):
		return 	"Detects the language of the given text word by word. Supports only Indian Language"	
def getInstance():
	return LangDetect()
