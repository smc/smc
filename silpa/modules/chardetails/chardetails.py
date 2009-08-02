#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Dictionary
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
from unicodedata import *
class CharDetails(SilpaModule):
	
	def getdetails(self, character):
		details= "<table  class=\"table1\"><tr><th>Property</th><th>Value</th></tr>"
		details+= "<tr><td>Name</td><td>"+ name(character) + "</td></tr>"
		details+= "<tr><td>HTML Entity</td><td>"+str( ord(character)) +"</td></tr>"
		details+= "<tr><td>Code point</td><td>"+ repr(character)+ "</td></tr>"
		try:
			details+= "<tr><td>Numeric Value</td><td>"+ numeric (character)+ "</td></tr>"
		except:
			pass	
		try:		
			details+= "<tr><td>Decimal Value</td><td>"+ decimal (character)+ "</td></tr>"
		except:
			pass	
		try:		
			details+= "<tr><td>Digit</td><td>"+digit(mychar)+ "</td></tr>"
		except:
			pass	
		details+= "<tr><td>Alphabet</td><td>"+ str(character.isalpha())+ "</td></tr>"
		details+= "<tr><td>Digit</td><td>"+str(character.isdigit())+ "</td></tr>"
		details+= "<tr><td>AlphaNumeric</td><td>"+ str(character.isalnum())+ "</td></tr>"
		details+= "<tr><td>Canonical Decomposition</td><td>"+ decomposition(character)+ "</td></tr>"
		details+= "</table>"
		return details
	def process(self,form):
		response = """
		<h2>Unicode Character Details</h2></hr>
		<p>Enter a character to get the unicode details
		</p>
		<form action="" method="post">
		 <p align="center">
		Character : <input type="text" value="%s" name="character" style="width:3em;"/>
		<input type="hidden" name="action" value="CharDetails">
		<input  type="submit" id="Char_Details" value="Get Details"  style="width:12em;"/>
		</br>
		</p>
		</form>
		"""
		if(form.has_key('character')):
			character = form['character'].value	.decode('utf-8')
			character = character [0] 
			response=response % character
			response = response+"<h2>Character Details</h2></hr>"
			response = response+ self.getdetails(character)
		else:
			response=response % ""	
		return response
	def get_module_name(self):
		return "Unicode Character Details"
	def get_info(self):
		return 	"Shows the Unicode Character Details of a given character"	
		
def getInstance():
	return CharDetails()

	
