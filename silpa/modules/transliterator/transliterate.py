#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Paralperu
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
from langdetect import LangDetect
class Transliterator:
	def transliterate(self,text, target_lang_code):
		ld=LangDetect()
		tx_str=""
		words=text.split(" ")
		for word in words:
			src_lang_code= ld.detect_lang(word) 
			tx_str = tx_str
			for chr in word:
				offset=ord(chr) + self.getOffset(src_lang_code, target_lang_code) 
				if(offset>0):
					tx_str=tx_str + unichr (offset) 
			tx_str=tx_str	+ " "
		return 	tx_str
	def getOffset(self,src,target):
		hi_IN = 0x0901
		bn_IN = 0x0981
		pa_IN = 0x0A01
		gu_IN = 0x0A81 
		or_IN = 0x0B01
		ta_IN = 0x0B81
		te_IN = 0x0C01
		ka_IN = 0x0C81	
		ml_IN = 0x0D01
		src_id=0
		target_id=0
		if(src=="en_US"):
			return 0
		if(src=="hi_IN"):
			src_id=hi_IN
		if(src=="bn_IN"):
			src_id=bn_IN
		if(src=="pa_IN"):
			src_id=pa_IN
		if(src=="gu_IN"):
			src_id=gu_IN
		if(src=="or_IN"):
			src_id=or_IN
		if(src=="ta_IN"):
			src_id=ta_IN
		if(src=="te_IN"):
			src_id=te_IN
		if(src=="ka_IN"):
			src_id=ka_IN
		if(src=="ml_IN"):
			src_id=ml_IN
		if(target=="hi_IN"):
			target_id=hi_IN
		if(target=="bn_IN"):
			target_id=bn_IN
		if(target=="pa_IN"):
			target_id=pa_IN
		if(target=="gu_IN"):
			target_id=gu_IN
		if(target=="or_IN"):
			target_id=or_IN
		if(target=="ta_IN"):
			target_id=ta_IN
		if(target=="te_IN"):
			target_id=te_IN
		if(target=="ka_IN"):
			target_id=ka_IN
		if(target=="ml_IN"):
			target_id=ml_IN	
		if(src=="Unknown"):
			return 0	
		return (target_id - src_id)					
if __name__ == "__main__":
	t=Transliterator () 
	print t.transliterate (u"കരയുന്നോ  കരയുന്നോ?" , "ta_IN")
