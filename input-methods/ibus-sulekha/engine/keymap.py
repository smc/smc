# -*- coding: utf-8 -*-
#
# Sulekha
#
# Copyright (c) 2009 Santhosh Thottingal <santhosh.thiotttingal@gmail.com>
#
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330,
# Boston, MA  02111-1307  USA
import os
class Keymap:
	def __init__(self, map="inscript_ml_IN"):
		self. keymap_dict = self.load_key_map(map)

	def get_candidates(self,key):
		if self. keymap_dict == None :
			return None
		if self. keymap_dict.has_key(key) :
			value = self.keymap_dict[key]
			candidate_list=value.split(":")
			for candidate in candidate_list:
				candidate = candidate.replace("\"","");
				candidate_list[candidate_list.index(candidate)] = candidate
			return 	candidate_list
		else :
			return None
	def load_key_map(self, map):
		keymap_dict=dict()
		try:
			keymap_file = open("/usr/share/ibus-sulekha/engine/keymaps/"+map, 'r')
		except:
			print "Could not find keymaps/"+map + " file."
			return None
		while True:
			line =	 keymap_file .readline()
			if line == "":
				break
			line=line.strip()
			try:
				key = line.split("=")[0].strip()
				value = line.split("=")[1].strip()
				key = key.replace("\"","")
				value = value.replace("\"","")
				keymap_dict[key]=value
			except:
				continue
		return keymap_dict
if __name__ == '__main__':
	keymap=	Keymap("swanalekha_ml_IN")
	candidate_list= keymap.get_candidates("k")	
	for candidate in candidate_list:
		print candidate
	
