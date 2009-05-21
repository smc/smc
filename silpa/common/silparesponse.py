#! /usr/bin/env python
# -*- coding: utf-8 -*-
from utils import *
class SilpaResponse:
	def __init__(self):
		self.response =getTemplate()
	def toUnicode(self):
		self.response=self.response.replace("$$SILPA_COPYRIGHT$$",getCopyrightInfo());
		return self.response.encode('utf-8')
	def toString(self):
		self.response=self.response.replace("$$SILPA_COPYRIGHT$$",getCopyrightInfo());
		return self.response
	def getResponse(self):
		self.response=self.response.replace("$$SILPA_COPYRIGHT$$",getCopyrightInfo());
		return self.response	
	def setBreadcrumb(self,navPath):
		if(navPath):
			html=	"<div id=\"breadcrumb\"><a href=\"http://smc.org.in/silpa\">Home</a> /"
			html=html+navPath+"</div>"
			self.response=self.response.replace("$$SILPA_BREADCRUMB$$",html)
	def setContent(self,value):
		if(value):
			self.response=self.response.replace("$$SILPA_CONTENT$$",value)
		else:
			self.response=self.response.replace("$$SILPA_CONTENT$$","")	
	def setErrorMessage(self,value):
		if(value):
			self.response=self.response.replace("$$SILPA_ERROR$$",value)
		else:
			self.response=self.response.replace("$$SILPA_ERROR$$","")	
	def setSuccessMessage(self,value):
		if(value):
			self.response=self.response.replace("$$SILPA_SUCCESS$$",value)
		else:
			self.response=self.response.replace("$$SILPA_SUCCESS$$","")
	
