#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from utils import *
class ModuleManager:
	def import_module(self,name):
		parts = name.split(".")
		try:
			obj= sys.modules[name]
		except KeyError:
			obj  = __import__(".".join(parts[:-1]))
		if(len(parts)>1):	
			for part in parts[1:]:
				try:
					obj = getattr(obj,part)
				except:
					obj = None	
		return obj

	def getModuleInstance(self,action):
		action=action.replace(" ","_")
		module_name = self.find_module(action)
		if(module_name):
			try:
				return self.import_module(module_name).getInstance()
			except:
				print dir(self.import_module(module_name))	
		else:
			return None	
	def find_module(self,action):
		try:
			return getModulesList()[action]
		except:	
			return None
	def getModulesInfoAsHTML(self):
		module_dict=getModulesList	()
		response = "<h2>Available Modules</h2></hr>"
		response = response+"<table class=\"table1\"><tr><th>Module</th><th>Description</th></tr>"
		for action in 	module_dict:
			module_instance=self.getModuleInstance(action)
			if(module_instance!=None):
				response = response+"<tr><td><a href='"+ action +"'>"+module_instance.get_module_name()+"</a></td>"
				response = response+"<td>"+module_instance.get_info()+"</td></tr>"
			else:
				response = response+"<tr><td>"+action.replace("_"," ")+"</td>"
				response = response+"<td>Error while retrieving module details</td></tr>"	
		return  response+"</table>"	
if __name__ == '__main__':
	mm=ModuleManager()
	print mm.getModuleInstance("lemmatize")
	print mm.import_module("modules.lemmatizer").getInstance()
	 
