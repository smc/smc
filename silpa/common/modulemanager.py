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
			print "Loading " , obj
		if(len(parts)>1):	
			for part in parts[1:]:
				obj = getattr(obj,part)
		return obj

	def getModuleInstance(self,action):
		module_name = self.find_module(action)
		if(module_name):
			return self.import_module(module_name).getInstance()
		else:
			return None	
	def find_module(self,action):
		try:
			return getModulesList()[action]
		except:	
			return None
if __name__ == '__main__':
	mm=ModuleManager()
	print mm.getModuleInstance("lemmatize")
	print mm.import_module("modules.lemmatizer").getInstance()
	 
