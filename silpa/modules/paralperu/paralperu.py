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

     
class Paralperu:
	def paralperu(self,text):
		result = ""
		text=unicode(text)
		index = len(text) - 1
		while index >= 0:
			if  ((index)>= 0 ) :
				if (text[index]== '്'):
					index = index - 2 #skip the letter before chandrakkala
					continue
			if (text[index] == u'ക'):
				result = result + '1'
			if (text[index]== u'ട'):
				result = result + '1'
			if (text[index]== u'പ'):
				result = result + '1'
			if (text[index]== u'യ'):
				result = result + '1'
			if (text[index]== u'ഖ'):
				result = result + '2'
			if (text[index]== u'ഠ'):
				result = result + '2'
			if (text[index]== u'ഫ'):
				result = result + '2'
			if (text[index]== u'ര'):
				result = result + '2'
			if (text[index]== u'ഗ'):
				result = result + '3'
			if (text[index]== u'ഡ'):
				result = result + '3'
			if (text[index]== u'ബ'):
				result = result + '3'
			if (text[index]== u'ല'):
				result = result + '3'
			if (text[index]== u'ഘ'):
				result = result + '4'
			if (text[index]== u'ഢ'):
				result = result + '4'
			if (text[index]== u'ഭ'):
				result = result + '4'
			if (text[index]== u'വ'):
				result = result + '4'
			if (text[index]== u'ങ'):
				result = result + '5'
			if (text[index]== u'ണ'):
				result = result + '5'
			if (text[index]== u'മ'):
				result = result + '5'
			if (text[index]== u'ശ'):
				result = result + '5'
			if (text[index]== u'ച'):
				result = result + '6'
			if (text[index]== u'ത'):
				result = result + '6'
			if (text[index]== u'ഷ'):
				result = result + '6'
			if (text[index]== u'ഛ'):
				result = result + '7'
			if (text[index]== u'ഥ'):
				result = result + '7'
			if (text[index]== u'സ'):
				result = result + '7'
			if (text[index]== u'ജ'):
				result = result + '8'
			if (text[index]== u'ദ'):
				result = result + '8'
			if (text[index]== u'ഹ'):
				result = result + '8'
			if (text[index]== u'ഝ'):
				result = result + '9'
			if (text[index]== u'ധ'):
				result = result + '9'
			if (text[index]== u'ള'):
				result = result + '9'
			if (text[index]== u'ഞ'):
				result = result + '0'
			if (text[index]== u'ന'):
				result = result + '0'
			if (text[index]== u'ഴ'):
				result = result + '0'
			if (text[index]== u'റ'):
				result = result + '0'
			if (text[index]== u'അ'):
				result = result + '0'
			if (text[index]== u'ആ'):
				result = result + '0'
			if (text[index]== u'ഇ'):
				result = result + '0'
			if (text[index]== u'ഈ'):
				result = result + '0'
			if (text[index]== u'ഉ'):
				result = result + '0'
			if (text[index]== u'ഊ'):
				result = result + '0'
			if (text[index]== u'ഋ'):
				result = result + '0'
			if (text[index]== u'ൠ'):
				result = result + '0'
			if (text[index]== u'ഌ'):
				result = result + '0'
			if (text[index]== u'ൡ'):
				result = result + '0'
			if (text[index]== u'എ'):
				result = result + '0'
			if (text[index]== u'ഏ'):
				result = result + '0'
			if (text[index]== u'ഒ'):
				result = result + '0'
			if (text[index]== u'ഓ'):
				result = result + '0'
			if (text[index]== u'ഔ'):
				result = result + '0'
			index = index-1
		return result

