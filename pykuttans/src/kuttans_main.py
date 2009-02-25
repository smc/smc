#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2009 Rajeesh K Nambiar <rajeeshknambiar@gmail.com>,
# 					 Rahul <rahulrs@gmx.com>
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

_app_name = "Kuttans"
_app_version = "0.1"

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
		self.connect(Ui.actionOpen, QtCore.SIGNAL("triggered()"), self.openFile)	#രേഖ തുറക്കാനുള്ള ആജ്ഞ open() എന്ന പ്രവൃത്തിയുമായി ബന്ധിപ്പിക്കുക
		self.connect(Ui.actionSave, QtCore.SIGNAL("triggered()"), self.saveFile)
		self.connect(Ui.actionSaveAs, QtCore.SIGNAL("triggered()"), self.saveFileAs)
		self.connect(Ui.actionAbout, QtCore.SIGNAL("triggered()"), self.About)
		self.connect(Ui.actionClose, QtCore.SIGNAL("triggered()"), self, QtCore.SLOT("close()"))
		
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
		
		self.readSettings()
		self.setCurrentFile(self.tr("untitled.txt"))
		self.x = 1
	
	def textSize(self, qString):
		fmt = QtGui.QTextCharFormat()
     		fmt.setFontPointSize(float(qString));
     		self.mergeFormatOnWordOrSelection(fmt)
		
	def textFamily(self, qString):
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
		fName = QtGui.QFileDialog.getOpenFileName(self, self.tr("Select Input file"),"", "*.txt *.pdf")
		self.curFile = str(fName)
		path, extn = os.path.splitext(self.curFile)
		if os.path.isfile(fName):
			if extn == ".txt":
				QApplication.setOverrideCursor(Qt.WaitCursor)
				self.ui.textEdit.setPlainText(codecs.open(fName, 'r', 'utf-8').read())
				QApplication.restoreOverrideCursor()
				self.setCurrentFile(fName)
				self.ui.statusbar.showMessage("File " + self.strippedFileName(fName) + " Opened", 2000) #/൨൦൦൦ മില്ലി സെക്കന്റ് നേരം സ്റ്റാറ്റസ് ബാറില്‍ പ്രദര്‍ശിപ്പിക്കുക
				self.InputFile = str(fName)
				self.x = 0
			if extn == ".pdf":
				print "Need to implement displaying PDF file, with QtPoppler"
			
	def save(self):
		if self.x==1:
			return self.saveFileAs()
		if self.curFile.isEmpty():
			return self.saveFileAs()
		else:
		  return self.saveFile(self.curFile)
			
	def saveFile(self,fileName):
		QApplication.setOverrideCursor(Qt.WaitCursor)	  
		s = codecs.open(fileName,'w','utf-8')
		s.write(unicode(self.ui.textEdit.toPlainText()))
		s.close()
		QApplication.restoreOverrideCursor()
		self.setCurrentFile(fileName)
		self.ui.statusbar.showMessage(self.tr("File ") + self.strippedFileName(fileName) + self.tr(" Saved"), 2000)
	
	def saveFileAs(self):
		fileName = QtGui.QFileDialog.getSaveFileName()
		if (fileName.isEmpty() != 0):
			return False
		else:
			self.x = 0
			return self.saveFile(fileName)
			
	def maybeSave(self):
		if self.ui.textEdit.document().isModified():
			ret = QtGui.QMessageBox.warning(self, self.tr("Warning"),
                        self.tr("<h4 align=\"center\">The document has been modified.\n"
                                "<h4 align=\"center\">Do you want to save your changes?"),
                        QtGui.QMessageBox.Yes | QtGui.QMessageBox.Default,
                        QtGui.QMessageBox.No,
                        QtGui.QMessageBox.Cancel | QtGui.QMessageBox.Escape)
			if ret == QtGui.QMessageBox.Yes:
				return self.save()
			elif ret == QtGui.QMessageBox.Cancel:
				return False
		return True	
		
	def setCurrentFile(self, fileName):
		self.curFile = fileName
		self.ui.textEdit.document().setModified(False)
		self.setWindowModified(False)
		if self.curFile.isEmpty():
		  shownName = self.tr("untitled.txt")
		else:
			shownName = self.strippedFileName(self.curFile)
			self.setWindowTitle(self.tr("%1[*] - %2").arg(shownName).arg(self.tr("Kuttans")))
		
	def About(self):
		QtGui.QMessageBox.about(self, self.tr("About"+ _app_name),
            self.tr("<h1 align=\"center\">"+_app_name+" "+_app_version+"<p><h4 align=\"center\">A GUI frontend for Payyans<p><h4 align=\"center\"><a href=\"www.smc.org.in\">Swathanthra Malayalam Computing</a>"))
		
	def newFile(self):
		if self.maybeSave():
			self.ui.textEdit.clear()
			self.setCurrentFile(QtCore.QString())
		
	def filePrintPDF(self):
		document = self.ui.textEdit.document()
		printer = QtGui.QPrinter(QPrinter.HighResolution)
		fileName = QFileDialog.getSaveFileName()
		if (fileName.isEmpty()):
			return
		else:
			if (QFileInfo(fileName).suffix().isEmpty()):
				fileName.append(".pdf")
			printer.setOutputFormat(QPrinter.PdfFormat)
			printer.setOutputFileName(fileName)
			document.print_(printer)
		
	def filePrint(self):
		document = self.ui.textEdit.document()
		printer = QtGui.QPrinter()
		dialog = QtGui.QPrintDialog(printer, self)
		dialog.setWindowTitle(self.tr("Print Document"))
		if dialog.exec_() != QtGui.QDialog.Accepted:
			return
		document.print_(printer)
		
	def filePrintPreview(self):
		printer = QtGui.QPrinter()
		preview = QtGui.QPrintPreviewDialog(printer)
		def render():
			doc = self.ui.textEdit.document()
			doc.print_(printer)
		preview.connect(preview, QtCore.SIGNAL('paintRequested(QPrinter*)'), render)
		preview.exec_()
		
	def documentWasModified(self):
		self.setWindowModified(self.ui.textEdit.document().isModified())
		
	def Revathi_a2u(self):
		if self.InputFile == None:
			QtGui.QMessageBox.about(self, self.tr("Message"),
            self.tr("<h3 align=\"center\">No file selected<p><h4 align=\"center\">Open or enter the document to convert"))
			return
		self.OutputFile  = self.directoryName(self.InputFile) + "/unicode-" + self.strippedFileName(self.InputFile)
		self.ui.statusbar.showMessage(self.tr("Converting... Please wait"))
		if self.ConvertFiles("revathi.map", "a2u") == 0:
			self.ui.statusbar.showMessage(self.tr("Converted successfully!"), 2000)
		else:
			self.ui.statusbar.showMessage(self.tr("Conversion failed!"), 2000)
				
	def Revathi_u2a(self):
		if self.InputFile == None:
			QtGui.QMessageBox.about(self, self.tr("Message"),
            self.tr("<h3 align=\"center\">No file selected<p><h4 align=\"center\">Open or enter the document to convert"))
			return
		self.OutputFile  = self.directoryName(self.InputFile) + "/ascii-" + self.strippedFileName(self.InputFile)
		self.ui.statusbar.showMessage(self.tr("Converting... Please wait"))
		if self.ConvertFiles("revathi.map", "u2a") == 0:
			self.ui.statusbar.showMessage(self.tr("Converted successfully!"), 2000)
		else:
			self.ui.statusbar.showMessage(self.tr("Conversion failed!"), 2000)
		
	def Indulekha_a2u(self):
		if self.InputFile == None:
			QtGui.QMessageBox.about(self, self.tr("Message"),
            self.tr("<h3 align=\"center\">No file selected<p><h4 align=\"center\">Open or enter the document to convert"))
			return
		self.OutputFile  = self.directoryName(self.InputFile) + "/unicode-" + self.strippedFileName(self.InputFile)
		self.ui.statusbar.showMessage(self.tr("Converting... Please wait"))
		if self.ConvertFiles("indulekha.map", "a2u") == 0:
			self.ui.statusbar.showMessage(self.tr("Converted successfully!"), 2000)
		else:
			self.ui.statusbar.showMessage(self.tr("Conversion failed!", 2000))
		
	def Indulekha_u2a(self):
		if self.InputFile == None:
			QtGui.QMessageBox.about(self, self.tr("Message"),
            self.tr("<h3 align=\"center\">No file selected<p><h4 align=\"center\">Open or enter the document to convert"))
			return
		self.OutputFile  = self.directoryName(self.InputFile) + "/ascii-" + self.strippedFileName(self.InputFile)
		self.ui.statusbar.showMessage(self.tr("Converting... Please wait"))
		if self.ConvertFiles("indulekha.map", "u2a") == 0:
			self.ui.statusbar.showMessage(self.tr("Converted successfully!"), 2000)
		else:
			self.ui.statusbar.showMessage(self.tr("Conversion failed!"), 2000)

	def Karthika_a2u(self):
		if self.InputFile == None:
			QtGui.QMessageBox.about(self, self.tr("Message"),
            self.tr("<h3 align=\"center\">No file selected<p><h4 align=\"center\">Open or enter the document to convert"))
			return
		self.OutputFile  = self.directoryName(self.InputFile) + "/unicode-" + self.strippedFileName(self.InputFile)
		self.ui.statusbar.showMessage(self.tr("Converting... Please wait"))
		if self.ConvertFiles("karthika.map", "a2u") == 0:
			self.ui.statusbar.showMessage(self.tr("Converted successfully!"), 2000)
		else:
			self.ui.statusbar.showMessage(self.tr("Conversion failed!"), 2000)
		
	def Karthika_u2a(self):
		if self.InputFile == None:
			QtGui.QMessageBox.about(self, self.tr("Message"),
            self.tr("<h3 align=\"center\">No file selected<p><h4 align=\"center\">Open or enter the document to convert"))
			return
		self.OutputFile  = self.directoryName(self.InputFile) + "/ascii-" + self.strippedFileName(self.InputFile)
		self.ui.statusbar.showMessage(self.tr("Converting... Please wait"))
		if self.ConvertFiles("karthika.map", "u2a") == 0:
			self.ui.statusbar.showMessage(self.tr("Converted successfully!"), 2000)
		else:
			self.ui.statusbar.showMessage(self.tr("Conversion failed!"), 2000)	
		
	def customMap_a2u(self):
		if self.InputFile == None:
			QtGui.QMessageBox.about(self, self.tr("Message"),
            self.tr("<h3 align=\"center\">No file selected<p><h4 align=\"center\">Open or enter the document to convert"))
			return
		#fileName = QFileDialog.getOpenFileName(, self.tr("Select the fontmap file"), QDir.homePath (), self.tr("Font Maps (*.map);;All Files (*)"))
		fileName = QFileDialog.getOpenFileName()
		self.OutputFile  = self.directoryName(self.InputFile) + "/unicode-" + self.strippedFileName(self.InputFile)
		self.ui.statusbar.showMessage(self.tr("Converting... Please wait"))
		if self.ConvertFilesCustom(fileName, "a2u") == 0:
			self.ui.statusbar.showMessage(self.tr("Converted successfully!"), 2000)
		else:
			self.ui.statusbar.showMessage(self.tr("Conversion failed!"), 2000)
		
	def customMap_u2a(self):
		if self.InputFile == None:
			QtGui.QMessageBox.about(self, self.tr("Message"),
            self.tr("<h3 align=\"center\">No file selected<p><h4 align=\"center\">Open or enter the document to convert"))
			return
		fileName = QFileDialog.getOpenFileName()
		self.OutputFile  = self.directoryName(self.InputFile) + "/ascii-" + self.strippedFileName(self.InputFile)
		self.ui.statusbar.showMessage(self.tr("Converting... Please wait"))
		if self.ConvertFiles("karthika.map", "u2a") == 0:
			self.ui.statusbar.showMessage(self.tr("Converted successfully!"), 2000)
		else:
			self.ui.statusbar.showMessage(self.tr("Conversion failed!"), 2000)
		
	def ConvertFiles(self, map_name, direction):
		self.MappingFile = sys.prefix + "/share/payyans/maps/" + map_name
		p = Payyans(self.InputFile, self.OutputFile, self.MappingFile)
		if direction == "a2u":
			return p.ascii2unicode()
		elif direction == "u2a":
			return p.unicode2ascii()
			
	def ConvertFilesCustom(self, map_name, direction):
		self.MappingFile = map_name
		p = Payyans(self.InputFile, self.OutputFile, self.MappingFile)
		if direction == "a2u":
			return p.ascii2unicode()
		elif direction == "u2a":
			return p.unicode2ascii()
		
	def asciiToUnicodePDF(self):
		# poppler-qt4 can be made use of, to render PDF files
		pass
		
	def closeEvent(self, event):
		if self.maybeSave():
			self.writeSettings()
			event.accept()
		else:
			event.ignore()
			
	def writeSettings(self):
		settings = QtCore.QSettings("SMC", "Kuttans")
		settings.setValue("pos", QtCore.QVariant(self.pos()))
		settings.setValue("size", QtCore.QVariant(self.size()))
    
	def readSettings(self):
		settings = QtCore.QSettings("SMC", "Kuttans")
		pos = settings.value("pos", QtCore.QVariant(QtCore.QPoint(200, 200))).toPoint()
		size = settings.value("size", QtCore.QVariant(QtCore.QSize(400, 400))).toSize()
		self.resize(size)
		self.move(pos)

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = StartKuttans()
	myapp.show()
	sys.exit(app.exec_())

