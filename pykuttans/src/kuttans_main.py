#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2009 Rajeesh K Nambiar <rajeeshknambiar@gmail.com>
#
# This program is free software you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation either version 3 of the License, or
# (at your option) any later version.
#       
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#       
# You should have received a copy of the GNU General Public License
# along with this program if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.

import sys
import os
import codecs

from payyans import Payyans

from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *
from kuttans_ui import Ui_Kuttans

QObj = QtCore.QObject	# Short name ;-)

class StartKuttans(QtGui.QMainWindow):
	def __init__(self, parent=None):
		
		self.direction		= None
		self.InputFile		= None
		self.MappingFile	= None
		self.OutputFile 	= None
		
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_Kuttans()
		self.ui.setupUi(self)
		Ui = self.ui		# Another short name ;-)
		
		Ui.actionCut.setEnabled(False)
		Ui.actionCopy.setEnabled(False)
		Ui.actionDelete.setEnabled(False)
		Ui.actionASCIIToUnicodePDF.setEnabled(False)
		Ui.actionUnicodeToASCIIPDF.setEnabled(False)
		
		Ui.toolBar.setAllowedAreas(Qt.TopToolBarArea | Qt.BottomToolBarArea)
		Ui.toolBar.setWindowTitle("Format Actions")
		Ui.comboFont = QtGui.QFontComboBox(Ui.toolBar)
		Ui.toolBar.addWidget(Ui.comboFont)
		self.connect(Ui.comboFont, QtCore.SIGNAL("activated(QString)"), self.textFamily)
		Ui.comboSize = QtGui.QComboBox(Ui.toolBar)
		Ui.comboSize.setObjectName("comboSize")
		Ui.comboSize.setEditable(True)
		#Ui.comboSize.setCurrentIndex(Ui.comboSize.findText(str(QtGui.QApplication.font().pointSize())))
		Ui.toolBar.addWidget(Ui.comboSize)
		fontDb = QtGui.QFontDatabase
		for size in fontDb.standardSizes():
			Ui.comboSize.addItem(str(size))
		self.connect(Ui.comboSize, QtCore.SIGNAL("activated(QString)"), self.textSize)
		
		self.connect(Ui.textEdit, QtCore.SIGNAL("copyAvailable(bool)"), Ui.actionCut, QtCore.SLOT("setEnabled(bool)"))	#ഉപയോക്താവ് ഏതെങ്കിലും പാഠഭാഗം തിരഞ്ഞെടുത്തെങ്കില്‍ മാത്രം...
		self.connect(Ui.textEdit, QtCore.SIGNAL("copyAvailable(bool)"), Ui.actionCopy, QtCore.SLOT("setEnabled(bool)"))	#'cut', 'copy' എന്നിവ സജ്ജീവമാക്കുക
		self.connect(Ui.actionOpen, QtCore.SIGNAL("triggered()"), self.openFile)				#രേഖ തുറക്കാനുള്ള ആജ്ഞ open() എന്ന പ്രവൃത്തിയുമായി ബന്ധിപ്പിക്കുക
		self.connect(Ui.actionSave, QtCore.SIGNAL("triggered()"), self.saveFile)
		self.connect(Ui.actionSaveAs, QtCore.SIGNAL("triggered()"), self.saveFileAs)
		self.connect(Ui.actionAbout, QtCore.SIGNAL("triggered()"), self.About)
		
		self.connect(Ui.actionNew, QtCore.SIGNAL("triggered()"), self.newFile)
		self.connect(Ui.actionExportPDF, QtCore.SIGNAL("triggered()"), self.filePrintPDF)
		self.connect(Ui.actionPrint, QtCore.SIGNAL("triggered()"), self.filePrint)
		self.connect(Ui.actionPrintPreview, QtCore.SIGNAL("triggered()"), self.filePrintPreview)
		self.connect(Ui.textEdit.document(), QtCore.SIGNAL("contentsChanged()"), self.documentWasModified)
		
		self.connect(Ui.actionRevathi_a2u, QtCore.SIGNAL("triggered()"), self.Revathi_a2u)
		self.connect(Ui.actionIndulekha_a2u, QtCore.SIGNAL("triggered()"), self.Indulekha_a2u)
		self.connect(Ui.actionKarthika_a2u, QtCore.SIGNAL("triggered()"), self.Karthika_a2u)
		self.connect(Ui.actionSelectFontMap_a2u, QtCore.SIGNAL("triggered()"), self.customMap_a2u)
		self.connect(Ui.actionASCIIToUnicodePDF, QtCore.SIGNAL("triggered()"), self.asciiToUnicodePDF)
		
		self.connect(Ui.actionRevathi_u2a, QtCore.SIGNAL("triggered()"), self.Revathi_u2a)
		self.connect(Ui.actionIndulekha_u2a, QtCore.SIGNAL("triggered()"), self.Indulekha_u2a)
		self.connect(Ui.actionKarthika_u2a, QtCore.SIGNAL("triggered()"), self.Karthika_u2a)
		self.connect(Ui.actionSelectFontMap_u2a, QtCore.SIGNAL("triggered()"), self.customMap_u2a)
	
	def textSize(self, qString):
		fmt = QtGui.QTextCharFormat()
     		fmt.setFontPointSize(float(qString));
     		self.mergeFormatOnWordOrSelection(fmt)
		
	def textFamily(self, qString):
		print "In textFamily"
		fmt = QtGui.QTextCharFormat()
		fmt.setFontFamily(qString);
		self.mergeFormatOnWordOrSelection(fmt)
		
	def mergeFormatOnWordOrSelection(self, format):
		cursor = self.ui.textEdit.textCursor()
		if not cursor.hasSelection():
			cursor.select(QtGui.QTextCursor.WordUnderCursor)
		cursor.mergeCharFormat(format)
		self.ui.textEdit.mergeCurrentCharFormat(format)
		
	def directoryName(self, fullname):
		return QtCore.QFileInfo(fullname).absolutePath()
		
	def strippedFileName(self, fullname):
		return QtCore.QFileInfo(fullname).fileName()
		
	def openFile(self):
		fName = QtGui.QFileDialog.getOpenFileName()
		if os.path.isfile(fName):
			self.ui.textEdit.setPlainText(codecs.open(fName, 'r', 'utf-8').read())
			self.ui.statusbar.showMessage("File " + self.strippedFileName(fName) + " Opened", 2000) #/൨൦൦൦ മില്ലി സെക്കന്റ് നേരം സ്റ്റാറ്റസ് ബാറില്‍ പ്രദര്‍ശിപ്പിക്കുക
			self.InputFile = str(fName)
			
	def saveFile(self):
		pass
	
	def saveFileAs(self):
		pass
		
	def About(self):
		pass
		
	def newFile(self):
		pass
		
	def filePrintPDF(self):
		pass
		
	def filePrint(self):
		pass
		
	def filePrintPreview(self):
		pass
		
	def documentWasModified(self):
		pass
		
	def Revathi_a2u(self):
		self.OutputFile  = self.directoryName(self.InputFile) + "/unicode-" + self.strippedFileName(self.InputFile)
		self.ui.statusbar.showMessage("Converting... Please wait")
		if self.ConvertFiles("revathi.map", "a2u") == 0:
			self.ui.statusbar.showMessage("Converted successfully!")
		else:
			self.ui.statusbar.showMessage("Conversion failed!")
				
	def Revathi_u2a(self):
		self.OutputFile  = self.directoryName(self.InputFile) + "/ascii-" + self.strippedFileName(self.InputFile)
		self.ui.statusbar.showMessage("Converting... Please wait")
		if self.ConvertFiles("revathi.map", "u2a") == 0:
			self.ui.statusbar.showMessage("Converted successfully!")
		else:
			self.ui.statusbar.showMessage("Conversion failed!")
		
	def Indulekha_a2u(self, direction):
		pass
		
	def Indulekha_u2a(self, direction):
		pass
		
	def Karthika_a2u(self, direction):
		pass
		
	def Karthika_u2a(self, direction):
		pass
		
	def customMap_a2u(self, direction):
		pass
		
	def customMap_u2a(self, direction):
		pass
		
	def ConvertFiles(self, map_name, direction):
		self.MappingFile = sys.prefix + "/share/payyans/maps/" + map_name
		p = Payyans(self.InputFile, self.OutputFile, self.MappingFile)
		if direction == "a2u":
			return p.ascii2unicode()
		elif direction == "u2a":
			return p.unicode2ascii()
		
	def asciiToUnicodePDF(self):
		# poppler-qt4 can be made use of, to render PDF files
		pass


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = StartKuttans()
	myapp.show()
	sys.exit(app.exec_())

