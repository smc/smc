#!/home/smcweb/bin/python
# -*- coding: utf-8 -*-
from common import *
from utils import *
import traceback
import cgitb
import cgi
cgitb.enable(True, "logs/")
def index(form):
	action=None
	if(form.has_key('action')):
		action=form['action'].value	
	handleStats()	
	response=SilpaResponse()
	if(action):
		action=action.replace(" ","_")
		#static content?
		if action.endswith('.html') or action.endswith('.htm'):
			response.setContent(getStaticContent(action))
			return response.toString()
		else:	
			module_manager=ModuleManager()
			module_instance =  module_manager.getModuleInstance(action)
			if(module_instance):
				response= module_instance.process(form, response)
				return response.toString()
	else:
		return response.toString()				
if __name__ == '__main__':
	print "Content-Type: text/html\n\n"
	print index(cgi.FieldStorage()).encode('utf-8')
