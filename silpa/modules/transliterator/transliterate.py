#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Any Indian Language to any other Indian language transliterator
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

from common import *
class Transliterator(SilpaModule):
	def transliterate_ml_en(self, word):
		virama=u"്"
		#TODO: how to make this more generic so that more languages can be handled here?
		#idea1: transliterate any langauge to a common language say hindi and the n do conversion?
		#existing transliterate.py can be used?
		#idea2: Have dictionaries for each language like english_xx_dict ?
		#TODO: complete this
		english_ml_dict={u'അ':'a',u'ആ':'a',u'ഇ':'a',u'ഈ':'a',u'ഉ':'a',u'ഊ':'a',u'ഋ':'a',\
				u'എ':'a',u'ഏ':'a',u'ഐ':'a',u'ഒ':'a',u'ഓ':'a',u'ഔ':'a',\
				u'ക':'k',u'ഖ':'kh',u'ഗ':'g',u'ഘ':'gh',u'ങ്ങ':'ng',\
				u'ച':'ch',u'ഛ':'chh',u'ജ':'j',u'ഝ':'jhh',u'ഞ':'nj',\
				u'ട':'t',u'ഠ':'th',u'ഡ':'d',u'ഢ':'dh',u'ണ':'n',\
				u'ത':'th',u'ഥ':'th',u'ദ':'d',u'ധ':'dh',u'ന':'n',\
				u'പ':'p',u'ഫ':'ph',u'ബ':'b',u'ഭ':'bh',u'മ':'m',\
				u'യ':'y',u'ര':'r',u'ല':'l', u'വ':'v', u'റ':'r',\
				u'ശ':'sa',u'ഷ':'sh',u'സ':'s', u'ഹ':'h',u'ള':'l',u'ഴ':'zh',\
				u'ാ':'a',u'ി':'i' ,u'ീ':'ee' ,u'ു':'u',\
				u'ൂ':'uu',u'ൃ':'ri' ,u'െ':'e' ,u'േ':'e',\
				u'ൈ':'ai',u'ൊ':'o' ,u'ോ':'oo' ,u'ൗ':'au'}
		word_length	=len(word)
		index=0
		tx_string=""
		while index<word_length:
			a_vowel=""
			try:
				if(index+1<word_length):
					if(word[index+1]==virama):
						a_vowel=""		
				else:
					if(index+1<word_length):
						if (english_ml_dict[word[index+1]] in ['a','e','i','o','u']):
							a_vowel=""				
					else:	
						a_vowel="a"		
					if (english_ml_dict[word[index]] in ['a','e','i','o','u']):	
						a_vowel=""				
					tx_string=tx_string+ english_ml_dict[word[index]] + a_vowel
			except:		
				tx_string=tx_string+ word[index]
			index=index+1	
		return 	tx_string

	def transliterate(self,text, target_lang_code):
		mm=ModuleManager()
		ld = mm.getModuleInstance("Detect Language")
		tx_str=""
		words=text.split(" ")
		for word in words:
			if(word.strip()>""):
				src_lang_code=ld.detect_lang(word)[word]
				if((target_lang_code=="en_US") and (src_lang_code=="ml_IN")):
					tx_str=tx_str + self.transliterate_ml_en(word)
					continue	
				for chr in word:
					offset=ord(chr) + self.getOffset(src_lang_code, target_lang_code) 
					if(offset>0):
						tx_str=tx_str + unichr (offset) 
				tx_str=tx_str	+ " "
			else:
				tx_str=tx_str	+ word
		return 	tx_str

	def getOffset(self,src,target):
		lang_bases={'en_US':0,'hi_IN': 0x0901,'bn_IN': 0x0981, 'pa_IN':0x0A01,'gu_IN':0x0A81 , 'or_IN': 0x0B01,'ta_IN': 0x0B81,'te_IN' : 0x0C01,	'ka_IN' :0x0C81	,'ml_IN': 0x0D01}
		src_id=0
		target_id=0
		try:
			src_id=lang_bases[src]
			target_id=lang_bases[target]
			return (target_id - src_id)
		except:
			return 0	

	def process(self, form):
		response = """
		<h2>Transliterator</h2></hr>
		<p>Enter the text for transliteration in the below text area.
		 Language of each  word will be detected. 
		 You can give the text in any language and even with mixed language
		</p>
		<form action="" method="post">
		<textarea  name='input_text' id='id1'>%s</textarea></br> 
		<select id="trans-lang" name="trans-lang" style="width:12em;">
		  <option value="hi_IN">Hindi</option>
		  <option value="ml_IN">Malayalam</option>
		  <option value="bn_IN">Bengali</option>
		  <option value="ta_IN">Tamil</option>
		  <option value="te_IN">Telugu</option>
		  <option value="or_IN">Oriya</option>
		  <option value="gu_IN">Gujarai</option>
		  <option value="pa_IN">Panjabi</option>
		  <option value="ka_IN">Kannada</option>
		  <option value="en_US">English</option>
		</select>
		<input  type="submit" id="Transliterate" value="Transliterate"  name="action" style="width:12em;"/>
		<input type="reset" value="Clear" style="width:12em;"/>
		</br>
		</form>
		"""
		if(form.has_key('input_text')):
			text = form['input_text'].value.decode('utf-8')
			target_lang = form['trans-lang'].value.decode('utf-8')
			response=response % text
			response = response+"<h2>Transliterated Text</h2></hr>"
			result = self.transliterate(text,target_lang)
			result = result.replace('\n', '<br/>')
			response = response+result
		else:
			response=response % ""	
		return response		
	def get_module_name(self):
		return "Transliterator"
	def get_info(self):
		return 	"Transliterated the text between any Indian Language"	
		
		
def getInstance():
	return Transliterator()		
		
						
if __name__ == "__main__":
	t=Transliterator () 
	print t.transliterate (u"കരയുന്നോ  കരയുന്നോ?" , "ta_IN")
