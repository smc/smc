#!/usr/bin/env python
# Copyright 2008 Santhosh Thottingal <santhosh.thottingal@gmail.com>, Nishan Naseer <nishan.naseer@gmail.com>, Rajeesh K Nambiar <rajeeshknambiar@gmail.com>
# http://www.smc.org.in
"""Payyans is a python program to convert the data written for ascii fonts in ascii format to the Unicode format"""

__AUTHORS__ = [ ("Santhosh Thottingal", "santhosh.thottingal@gmail.com", "Nishan Naseer", "nishan.naseer@gmail.com", "Rajeesh K Nambiar", "rajeeshknambiar@gmail.com")]

from payyan import Payyan
import os
import string

class Payyans:
	def __init__(self,input_file, output_file,mapping_file):
		self.payyan= Payyan()
		(inp_file, inp_ext) = os.path.splitext(input_file)
		if string.upper(inp_ext) == ".PDF":
			self.payyan.pdf=1	
		self.payyan.input_filename=input_file 
		self.payyan.output_filename=output_file
		self.payyan.mapping_filename=mapping_file
	
	def word2ASCII(self, unicode_str):
		return self.payyan.word2ASCII(unicode_str)
	def word2Unicode(self, ascii_str):
		return self.payyan.word2ASCII(ascii_str)
	def ascii2unicode(self):
		return self.payyan.Ascii2Uni()
	def unicode2ascii(self):
		return self.payyan.Uni2Ascii()
