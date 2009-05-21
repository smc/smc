#! /usr/bin/env python
# -*- coding: utf-8 -*-

from common import *
from modules import *
from utils import *
import traceback
import cgitb
import cgi
cgitb.enable()
def index(form):
	if(form.has_key('action')):
		action=form['action'].value	
	else:	
		action=""
	response=SilpaResponse()
	if(action=="lemmatize"):
		response.setBreadcrumb("Lemmatizer")
		response. setContent("<textarea cols='100' rows='25' name='input_text' id='id1'>%s</textarea>")
	if(action=="Detect Language"):
		response.setBreadcrumb(action)
		ldetector=LangDetect()
		response. setContent(ldetector.process(form))
	if(action=="Hyphenate"):
		response.setBreadcrumb(action)
		hyphenator=Hyphenate()
		response. setContent(hyphenator.process(form))	
	response.setBreadcrumb("Coming Soon")	
	response.setContent("Not implemented in current version...!")	
	return response.toString();
	
if __name__ == '__main__':
	print "Content-Type: text/html\n\n"
	print index(cgi.FieldStorage()).encode('utf-8')
