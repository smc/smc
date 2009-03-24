#! /usr/bin/env python
# -*- coding: utf-8 -*-
from templates import *
class SilpaResponse:
	def __init__(self):
		self.response =getBaseHTML()

	def toUnicode(self):
		return self.response.encode('utf-8')
	def toString(self):
		return self.response
	def getResponse(self):
		return self.response	
	def setBreadcrumb(self,navPath):
		html=	"<div id=\"breadcrumb\"><a href=\"http://planet.smc.org.in/exp/silpa/silpa.py\">Home</a> /"
		html=html+navPath+"</div>"
		self.response=self.getResponse().replace("$$SILPA_BREADCRUMB$$",html)
	def setContent(self,value):
		self.response=self.getResponse().replace("$$SILPA_CONTENT$$",value)
