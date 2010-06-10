"""
	Anagram Maker
	Copyright 2010 Santhosh Thottingal <santhosh.thottingal@gmail.com>
	
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import random
import array
import os,sys
from common import *
class Anagram(SilpaModule):
	def __init__(self):
		self.template=os.path.join(os.path.dirname(__file__), 'anagram.html')
	
	@ServiceMethod				
	def getRandomWord (self):
		words = [ i.rstrip () for i in file ('./modules/anagram/ml_IN.dic') ]
		len_words = len (words)
		randnum=random.randrange(0,len_words)
		return [randnum,words[randnum].decode("utf-8")]
	
	def syllabalize_ml(self,text):
		signs = [
		u'\u0d02', u'\u0d03', u'\u0d3e', u'\u0d3f', u'\u0d40', u'\u0d41',
		u'\u0d42', u'\u0d43', u'\u0d44', u'\u0d46', u'\u0d47', u'\u0d48',
		u'\u0d4a', u'\u0d4b', u'\u0d4c', u'\u0d4d']
		limiters = ['.','\"','\'','`','!',';',',','?']

		chandrakkala = u'\u0d4d'
		lst_chars = []
		for char in text:
			if char in limiters:
				lst_chars.append(char)
			elif char in signs:
				lst_chars[-1] = lst_chars[-1] + char
			else:
				try:
					if lst_chars[-1][-1] == chandrakkala:
						lst_chars[-1] = lst_chars[-1] + char
					else:
						lst_chars.append(char)
				except IndexError:
					lst_chars.append(char)

		return lst_chars
		
	@ServiceMethod				
	def scramble(self, word):
		newword = ""
		randused = []
		i=0
		while i < len(word):
			randnum=random.randrange(0, len(word))
			if randnum not in randused:
				randused.append(randnum)
				#oldchar=word[i]
				newword=newword+word[randnum]
				i+=1
				#newword[randnum]=oldchar
		return newword
		
	def check_answer(self,ans_hint):
		words = [ i.rstrip () for i in file ('./modules/anagram/ml_IN.dic') ]
		return words[ans_hint].decode("utf-8")
	
	@ServiceMethod				
	def anagram(self):
		ans_hint,orig_word=self.getRandomWord()
		scrambled_word=self.scramble(self.syllabalize_ml(orig_word))
		return [ans_hint, scrambled_word]
	
	def process(self, form):
		response = """
		<h2>Malayalam Anagram</h2></hr>
		<p>Find out the original word from the scrambled word given below.
		</p>
		<form action="" method="post">
		%s
		<br/>
		<input type="hidden" name="ans_hint" value="%s">
		<input type="hidden" name="action" value="Anagram">
		<input type="text" cols='100' name='input_text' id='input_text' value="%s"/>
		<br/>
		<input type="submit" id="anagram" value="Submit"  style="width:12em;"/>
		<br/>
		</form>
		"""
		if(form.has_key('input_text')):
			text = form['input_text'].value	.decode('utf-8')
			ans_hint= int(form['ans_hint'].value)
			answer=self.check_answer(ans_hint)
			if(answer==text):
				response = response+"<h2>You are correct!</h2></hr>"
				response = response+"<b>Answer: "+answer+"</b>"
			else:
				response = response+"<h2>Your Answer is Wrong!</h2></hr>"
				response = response+"<b>Answer: "+answer+"</b>"	
			response=response % (answer ,ans_hint,text)	
		else:
			text=""	
			anagram_pair=self.anagram()
			ans_hint=anagram_pair[0]
			qn_word=anagram_pair[1]
			response=response % (qn_word ,ans_hint,text)
		return response
	def get_module_name(self):
		return "Malayalam Anagram"
	def get_info(self):
		return 	"Find out the original word from scrambled word!"
def getInstance():
	return Anagram()	
	
if __name__ == "__main__":
	anagram = Anagram()
	pair=anagram.anagram()
	print pair[0]+"-->"+pair[1]
