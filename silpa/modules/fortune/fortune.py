#  Spellchecker with language detection
#  coding: utf-8
#
#  Copyright © 2008  Santhosh Thottingal
#  Released under the GPLV3+ license

import commands
class Fortune:
	def fortune(self, word):
		if(word):
			command = "/usr/games/fortune -m" + word
			return commands.getoutput(command)
		else:
			command = "/usr/games/fortune"
			return commands.getoutput(command)

