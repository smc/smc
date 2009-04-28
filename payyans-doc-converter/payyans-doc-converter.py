#!/usr/bin/env python
#
# Copyright (C) 2009 Rajeesh K Nambiar <rajeeshknambiar@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# at your option) any later version.
#       
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#       
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.

import sys
import os

# import the oorunner helper module we've written
import oorunner
# Payyans
from payyans import Payyans

class OOWrapper:
	def __init__(self):
		# Find OpenOffice.
		_oopaths=(
			  ('/usr/lib64/ooo-2.0/program',   '/usr/lib64/ooo-2.0/program'),
			  ('/opt/openoffice.org3/program', '/opt/openoffice.org/basis3.0/program'),
		 )
		for p in _oopaths:
		    if os.path.exists(p[0]):
			OPENOFFICE_PATH    = p[0]
			OPENOFFICE_BIN     = os.path.join(OPENOFFICE_PATH, 'soffice')
			OPENOFFICE_LIBPATH = p[1]

			# Add to path so we can find uno.
			if sys.path.count(OPENOFFICE_LIBPATH) == 0:
				sys.path.insert(0, OPENOFFICE_LIBPATH)
                		os.putenv('URE_BOOTSTRAP','vnd.sun.star.pathname:' + OPENOFFICE_PATH + '/fundamentalrc')
			# This is required for loadComponentFromURL to work properly                                 	
			break	

		# start the openoffice instance
		oor = oorunner.OORunner()
		# get the central desktop object
		self.desktop = oor.connect()
		self.infile  = None
		self.outfile = None

	def createTextFilter(self):
		# Needed for FilterName - to export to TXT
		import uno
		from com.sun.star.beans import PropertyValue
		TXT	  = PropertyValue()
		TXT.Name  = "FilterName"
		TXT.Value = "Text"
		return TXT

	def convertDocToText(self, docFile):
		''' Convert the Document file to Text format '''
		self.infile = os.path.abspath(docFile)
		if not os.path.exists(self.infile):
			raise SystemExit ("Input file doesn't exist")
		
		self.document = self.desktop.loadComponentFromURL("file://"+self.infile, "_blank", 0, ())
		filter = self.createTextFilter()
		(fname, ext) = os.path.splitext(self.infile)
		self.textfile = fname + ".txt"
		self.document.storeAsURL("file://" + self.textfile, (filter,))
		
		self.closeOffice()

	def closeOffice(self):

		# Close the document
		self.document.dispose()
		# Close the OpenOffice desktop
		self.desktop.terminate()

	def covertDocWithPayyans(self, inFile, mapFile, outFile, direction):
		''' Call Payyans to do the actual conversion '''
		# @direction : a2u/u2a for ASCII-to-Unicode and vice versa
		self.convertDocToText(inFile)
		p=Payyans(self.textfile, os.path.abspath(outFile), os.path.abspath(mapFile))
		if not p:
			raise SystemExit("Couldn't create Payyan instance")
		if direction == "a2u":
			p.ascii2unicode()
		else:
			p.unicode2ascii()


if __name__ == "__main__":
	if sys.argv.__len__() != 5:
		raise SystemExit("usage: "+sys.argv[0]+" <infile> <outfile> <mapfile> <direction>")
	infile    = sys.argv[1]
	outfile   = sys.argv[2]
	mapfile   = sys.argv[3]
	direction = sys.argv[4]
	if not os.path.exists(os.path.abspath(infile)):
		raise SystemExit("Cannot find Input file")
	if not os.path.exists(os.path.abspath(mapfile)):
		raise SystemExit("Cannot find Mapping file")
	if not direction in ['a2u', 'u2a']:
	 	raise SystemExit("Direction should be either 'a2u' or 'u2a'")
	
	app = OOWrapper()	 
	app.covertDocWithPayyans(infile, mapfile, outfile, direction)
