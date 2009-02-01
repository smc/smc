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
import locale
import gettext
from gettext import gettext as _

try:
	import gtk
except ImportError:
	''' ചാത്തന്‍സിന് കള്‍സില്ലെന്നോ? '''
	print _("Chathans requires PyGTK")
	raise SystemExit
	
try:
	from payyans import Payyans
except ImportError:
	''' ഹൈയ്, പയ്യന്റെ ദുര്‍ജ്ജനസംസര്‍ഗ്ഗമില്ലാതെ നോം സാധനം തൊടാറില്ല! '''
	print _("Chathans requires Payyans")
	raise SystemExit


PACKAGE = "chathans"
gettext.bindtextdomain(PACKAGE, sys.prefix+"/share/locale/")
gettext.textdomain(PACKAGE)
#_ = gettext.gettext

name = _("Chathans")
version = "0.5"
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
		ascii_lbl   = gtk.Label(_("ASCII File : "))
		mapping_lbl = gtk.Label(_("Mapping File : "))
		unicode_lbl = gtk.Label(_("Unicode File : "))
		
		# പ്രമാണോം പത്രോം ആധാരോം എടുക്ക്വാ..
		#ascii_btn   = gtk.FileChooserButton(_("Select the ASCII File (.txt,.pdf)"))
		ascii_btn   = gtk.Button("ASCII File...",None)
		ascii_btn.connect("clicked", self.__choose_ascii_file)
		unicode_btn = gtk.Button("Unicode File...",None)
		unicode_btn.connect("clicked", self.__choose_unicode_file)
		mapping_btn = gtk.FileChooserButton(_("Select the ASCII-Unicode Mapping File"))
		#unicode_btn = gtk.FileChooserButton(_("Select Output Unicode File"))

		# ആസ്കി-യൂണിക്കോഡ് ആണോ, അതോ യൂണിക്കോഡ്-ആസ്കിയോ?
		a2u_radio   = gtk.RadioButton(None, (_("ASCII-to-Unicode")))
		u2a_radio   = gtk.RadioButton(a2u_radio, (_("Unicode-to-ASCII")))
		
		# മാപ്പ്, സാധാരണ എവിടെ കിട്ടും? അല്ല, എവിടെ കിട്ടും?
		mapping_dir = sys.prefix + "/share/payyans/maps/"
		mapping_btn.set_current_folder(mapping_dir)
		
		# Define the Actions. Lets get some action, baby!
		convert_btn = gtk.Button(_("Convert"), gtk.STOCK_CONVERT)
		convert_btn.connect("clicked", self.__convert_file)
		cancel_btn = gtk.Button(_("Quit"), gtk.STOCK_QUIT)
		cancel_btn.connect("clicked", self.__quit)
		about_btn = gtk.Button(_("About"), gtk.STOCK_ABOUT)
		about_btn.connect("clicked", self.__show_about)
		
		self.a2u_radio 	 = a2u_radio
		self.u2a_radio	 = u2a_radio

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
					
		radio_box = gtk.HBox()
		radio_box.set_border_width(12)
		radio_box.pack_start(a2u_radio)
		radio_box.pack_start(u2a_radio)
		
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
		vbox1.pack_start(radio_box)
		vbox1.pack_end(btn_box)
		
		frame = gtk.Frame()
		frame.set_border_width(5)
		frame.add(vbox1)	
		self.add(frame)
		
		self.show_all()
		
	def __choose_ascii_file(self, event):
		if self.u2a_radio.get_active() == True:
			the_action = gtk.FILE_CHOOSER_ACTION_SAVE
		else:
			the_action = gtk.FILE_CHOOSER_ACTION_OPEN
		filechooser = gtk.FileChooserDialog(title=_("Select the ASCII File (.txt,.pdf)"),
						    action=the_action,
						    buttons=(gtk.STOCK_OPEN, gtk.RESPONSE_ACCEPT,
					 		     gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL))
		# Add File Filter for ASCII input file. അരിപ്പ!
		ascii_filter = gtk.FileFilter()
		ascii_filter.set_name("*.txt,*.pdf")
		ascii_filter.add_pattern("*.[Tt][Xx][Tt]")
		ascii_filter.add_pattern("*.[Pp][Dd][Ff]")
		filechooser.add_filter(ascii_filter)
		filechooser.connect("response", self.__get_file, "a")
		filechooser.run()
		
	def __get_file(self, dialog, response, in_data):
		dialog.hide()
		if response == gtk.RESPONSE_ACCEPT:
			if in_data == "a":
				self.AsciiFile = dialog.get_filename()
				self.ascii_btn.set_label(os.path.basename(self.AsciiFile))
			else:
				self.UnicodeFile = dialog.get_filename()
				self.unicode_btn.set_label(os.path.basename(self.UnicodeFile))
		
	def __choose_unicode_file(self, event):
		if self.a2u_radio.get_active() == True:
			the_action = gtk.FILE_CHOOSER_ACTION_SAVE
		else:
			the_action = gtk.FILE_CHOOSER_ACTION_OPEN
		filechooser = gtk.FileChooserDialog(title=_("Select the Unicode File"),
						    action=the_action,
						    buttons=(gtk.STOCK_OPEN, gtk.RESPONSE_ACCEPT,
					 		     gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL))
		filechooser.connect("response", self.__get_file, "u")
		filechooser.run()
		
	def __convert_file(self, event):
		''' പയ്യനെ വിളിക്ക്യാ, ഇനി നോം ഗ്യാലറിയിലിരുന്ന് കളി കാണട്ടെ. '''
		#self.AsciiFile   = self.ascii_btn.get_filename()
		self.MappingFile = self.mapping_btn.get_filename()
		#self.UnicodeFile = self.unicode_btn.get_filename()

		if self.a2u_radio.get_active() == True:
			direction = "a2u"
			from_file = self.AsciiFile
			to_file	  = self.UnicodeFile
		else:
			direction = "u2a"
			from_file = self.UnicodeFile
			to_file	  = self.AsciiFile
		
		if (   from_file 	== None
		   or  self.MappingFile == None ):
			   dlg = gtk.MessageDialog(self.get_toplevel(),
					gtk.DIALOG_MODAL,
					gtk.MESSAGE_INFO,
					gtk.BUTTONS_OK,
					_("Please select both Input file and Mapping file"))
			   dlg.run()
			   dlg.destroy()
			   return
			   
		if to_file == None:
			(inp_file, inp_ext) = os.path.splitext(from_file)
			if direction == "a2u":
				self.UnicodeFile = inp_file + "-unicode" + ".txt"
			else:
				self.AsciiFile   = inp_file + "-ascii"   + ".txt"
			   
		# ഓഹ്, പയ്യന്‍! നീ വ്യാഘ്രമാകുന്നു.
		if direction == "a2u":
			payyan = Payyans(self.AsciiFile, self.UnicodeFile, self.MappingFile)
			status = payyan.ascii2unicode()
		else:
			payyan = Payyans(self.UnicodeFile, self.AsciiFile, self.MappingFile)
			status = payyan.unicode2ascii()
		print status
		if status == 0:
			if direction == "a2u":
				msg = _("Coversion Done - Unicode file : ") + self.UnicodeFile
			else:
				msg = _("Conversion Done - ASCII file : ") + self.AsciiFile
		if status == 1:
			msg = _("Could not find the pdftotext utility. Exiting...")
		if status == 2:
			msg = _("Syntax Error in Mapping file. Exiting...")
		# കത്തിച്ചു കഴിഞ്ഞു.
		dlg = gtk.MessageDialog(self.get_toplevel(),
					gtk.DIALOG_MODAL,
					gtk.MESSAGE_INFO,
					gtk.BUTTONS_OK,
					msg)
		dlg.run()
		dlg.destroy()
				
		return
		
	def __show_about(self, event):
		''' അധികപ്രസംഗം !!! '''
		dlg = gtk.AboutDialog()
		autxt1  = _("Chathans: Rajeesh K Nambiar <rajeeshknambiar@gmail.com>")
		autxt2  = _("Payyans : Santhosh Thottingal, Nishan Naseer,\n\t\t  Manu S Madhav, Rajeesh K Nambiar")
		authors = ["\n" + autxt1 + "\n\n" + autxt2]
		comments= _("Chathans is an easy to use GUI frontend to Payyans ASCII<->Unicode Converter")
		dlg.set_name(name)
		dlg.set_version(version)
		dlg.set_authors(authors)
		dlg.set_comments(comments)
		dlg.set_copyright(_("Copyright (c) Rajeesh K Nambiar"))
		dlg.set_license(_("Chathans is licensed under GNU GPL version 3"))
		dlg.set_website("http://smc.org.in/Payyans")
		
		dlg.run()
		dlg.destroy()
		
	def __quit(self, event):
		''' ന്നാ, കട്ടേം പടോം മടക്കാം ! '''
		dlg = gtk.MessageDialog(self.get_toplevel(),
					gtk.DIALOG_MODAL|gtk.DIALOG_DESTROY_WITH_PARENT,
					gtk.MESSAGE_QUESTION,
					gtk.BUTTONS_YES_NO,
					_("Do you really want to Quit?"))
		if ( dlg.run() == gtk.RESPONSE_YES ):
			dlg.destroy()
			gtk.main_quit()
		dlg.destroy()
		return
	

if __name__ == '__main__':
	chathans = Chathans()
	gtk.main()
