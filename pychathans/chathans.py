#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# chathans.py
#       
# Copyright (c) 2009 Rajeesh K Nambiar <rajeeshknambiar@gmail.com>
# http://smc.org.in/
#       
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#       
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import os
import sys
import string

try:
	import gtk
except ImportError:
	''' ചാത്തന്‍സിന് കള്‍സില്ലെന്നോ? '''
	print "Chathans requires PyGTK"
	raise SystemExit
	
try:
	from payyans import Payyans
except ImportError:
	''' ഹൈയ്, പയ്യന്റെ ദുര്‍ജ്ജനസംസര്‍ഗ്ഗമില്ലാതെ നോം സാധനം തൊടാറില്ല! '''
	print "Chathans require Payyans"
	raise SystemExit

name = "Chathans"
version = "0.2"
title = name + " " + version

class Chathans (gtk.Window):
	''' ചാത്തന്‍സ് അഥവാ സര്‍ ചാത്തു. വിക്ടോറിയാ രാജ്ഞിയില്‍ നിന്നും നേരിട്ട് പ്രഭുത്വം ! '''
	def __init__(self):
		self.AsciiFile 	 = None
		self.MappingFile = None
		self.UnicodeFile = None
		self.PdfFile	 = None
		self.__init_gui()
		
	def __init_gui(self):
		''' പൂമുഖം തുറന്ന്, ദര്‍ശനം നല്‍കാം... '''
		gtk.Window.__init__(self, gtk.WINDOW_TOPLEVEL)
		self.set_title(title)
		self.set_default_size(340, 160)
                self.set_position(gtk.WIN_POS_CENTER_ALWAYS)
		self.connect("destroy", self.__quit)
		
		# ലേബലടിക്ക്.
		ascii_lbl   = gtk.Label("ASCII File : ")
		mapping_lbl = gtk.Label("Mapping File : ")
		unicode_lbl = gtk.Label("Unicode File : ")
		
		# പ്രമാണോം പത്രോം ആധാരോം എടുക്ക്വാ..
		ascii_btn   = gtk.FileChooserButton("Select the ASCII File (.txt,.pdf)")
		mapping_btn = gtk.FileChooserButton("Select the ASCII-Unicode Mapping File")
		unicode_btn = gtk.FileChooserButton("Select Output Unicode File")
		
		# മാപ്പ്, സാധാരണ എവിടെ കിട്ടും? അല്ല, എവിടെ കിട്ടും?
		mapping_dir = sys.prefix + "/share/payyans/maps/"
		mapping_btn.set_current_folder(mapping_dir)
		
		# Define the Actions. Lets get some action, baby!
		convert_btn = gtk.Button("Convert", gtk.STOCK_CONVERT)
		convert_btn.connect("clicked", self.__convert_file)
		cancel_btn = gtk.Button("Quit", gtk.STOCK_QUIT)
		cancel_btn.connect("clicked", self.__quit)
		about_btn = gtk.Button("About", gtk.STOCK_ABOUT)
		about_btn.connect("clicked", self.__show_about)
		
		# Add File Filter for ASCII input file. അരിപ്പ!
		ascii_filter = gtk.FileFilter()
		ascii_filter.set_name("*.txt,*.pdf")
		ascii_filter.add_pattern("*.[Tt][Xx][Tt]")
		ascii_filter.add_pattern("*.[Pp][Dd][Ff]")
		ascii_btn.add_filter(ascii_filter)
		
		self.ascii_btn   = ascii_btn
		self.mapping_btn = mapping_btn
		self.unicode_btn = unicode_btn
		
		# Pack the widgets. പാക്കു ചെയ്യ്, പാക്കു വെട്ട്.
		hbox1 = gtk.HBox()
		hbox1.set_border_width(4)
		hbox1.pack_start(ascii_lbl)
		hbox1.pack_end(ascii_btn)
		
		hbox2 = gtk.HBox()
		hbox2.set_border_width(4)
		hbox2.pack_start(mapping_lbl)
		hbox2.pack_end(mapping_btn)
		
		hbox3 = gtk.HBox()
		hbox3.set_border_width(4)
		hbox3.pack_start(unicode_lbl)
		hbox3.pack_end(unicode_btn)
					
		btn_box = gtk.HButtonBox()
		btn_box.set_border_width(4)
		btn_box.pack_start(convert_btn)
		btn_box.pack_start(about_btn)
		btn_box.pack_start(cancel_btn)
		
		vbox1 = gtk.VBox()
		vbox1.set_border_width(4)
		vbox1.pack_start(hbox1)
		vbox1.pack_start(hbox2)
		vbox1.pack_start(hbox3)
		vbox1.pack_end(btn_box)
		
		frame = gtk.Frame()
		frame.set_border_width(5)
		frame.add(vbox1)	
		self.add(frame)
		
		self.show_all()
		
	def __convert_file(self, event):
		''' പയ്യനെ വിളിക്ക്യാ, ഇനി നോം ഗ്യാലറിയിലിരുന്ന് കളി കാണട്ടെ. '''
		self.AsciiFile   = self.ascii_btn.get_filename()
		self.MappingFile = self.mapping_btn.get_filename()
		self.UnicodeFile = self.unicode_btn.get_filename()
		
		if (   self.AsciiFile 	== None
		   or  self.MappingFile == None
		   or  self.UnicodeFile == None ):
			   dlg = gtk.MessageDialog(self.get_toplevel(),
					gtk.DIALOG_MODAL,
					gtk.MESSAGE_INFO,
					gtk.BUTTONS_OK,
					"Please select all the files")
			   dlg.run()
			   dlg.destroy()
			   return
			   
		# Check the extenstion of ASCII file for Text/PDF '''
		#(inp_file, inp_ext) = os.path.splitext(self.AsciiFile)
		#if string.upper(inp_ext) == ".PDF":
		#	self.PdfFile = self.AsciiFile
		#	self.AsciiFile = None
			   
		# ഓഹ്, പയ്യന്‍! നീ വ്യാഘ്രമാകുന്നു.
		payyan = Payyans(self.AsciiFile, self.UnicodeFile, self.MappingFile)
		payyan.ascii2unicode()
		# കത്തിച്ചു കഴിഞ്ഞു.
		dlg = gtk.MessageDialog(self.get_toplevel(),
					gtk.DIALOG_MODAL,
					gtk.MESSAGE_INFO,
					gtk.BUTTONS_OK,
					"Conversion Done !!")
		dlg.run()
		dlg.destroy()
				
		return
		
	def __show_about(self, event):
		''' അധികപ്രസംഗം !!! '''
		dlg = gtk.AboutDialog()
		dlg.set_name(name)
		dlg.set_version(version)
		autxt1 = "Chathans frontend : Rajeesh K Nambiar <rajeeshknambiar@gmail.com>"
		autxt2 = "Payyans : Santhosh Thottingal, Nishan Naseer, Manu S Madhav"
		authors = ["\n" + autxt1 + "\n" + autxt2]
		dlg.set_authors(authors)
		dlg.set_copyright("Copyright (c) Rajeesh K Nambiar")
		dlg.set_license("Licensed under GNU GPL version 3")
		dlg.set_website("http://smc.org.in/Payyans")
		
		dlg.run()
		dlg.destroy()
		
	def __quit(self, event):
		''' ന്നാ, കട്ടേം പടോം മടക്കാം ! '''
		dlg = gtk.MessageDialog(self.get_toplevel(),
					gtk.DIALOG_MODAL,
					gtk.MESSAGE_QUESTION,
					gtk.BUTTONS_YES_NO,
					"Do you really want to Quit?")
		if ( dlg.run() == gtk.RESPONSE_YES ):
			dlg.destroy()
			gtk.main_quit()
		dlg.destroy()
		return
	

if __name__ == '__main__':
	chathans = Chathans()
	gtk.main()
