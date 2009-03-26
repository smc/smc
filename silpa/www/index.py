#! /usr/bin/env python
# -*- coding: utf-8 -*-

from common import *
from utils import *
import traceback
import cgitb
import cgi
cgitb.enable()
def index(form):
	if(form.has_key('action')):
		action=form['action'].value	
	else:	
		action=None
	response=SilpaResponse()
	if(action):
		module_manager=ModuleManager()
		module_instance =  module_manager.getModuleInstance(action)
		if(module_instance):
			response.setBreadcrumb(module_instance.get_module_name())
			response.setContent(module_instance.process(form))
			response.setErrorMessage(module_instance.get_errormessage())
			response.setSuccessMessage(module_instance.get_successmessage())
		else:
			response.setBreadcrumb("Coming Soon")	
			response.setErrorMessage("Module not available")	
			response.setContent(None)
			response.setSuccessMessage(None)
	return response.toString();
	
if __name__ == '__main__':
	print "Content-Type: text/html\n\n"
	print index(cgi.FieldStorage()).encode('utf-8')
