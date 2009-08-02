
"""
  Copyright (c) 2007 Jan-Klaas Kollhof

  This file is part of jsonrpc.

  jsonrpc is free software; you can redistribute it and/or modify
  it under the terms of the GNU Lesser General Public License as published by
  the Free Software Foundation; either version 2.1 of the License, or
  (at your option) any later version.

  This software is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Lesser General Public License for more details.

  You should have received a copy of the GNU Lesser General Public License
  along with this software; if not, write to the Free Software
  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
"""

from common import *
from jsonrpc import JSONEncodeException
from jsonrpc import dumps
from jsonrpc import loads
from utils import *


def ServiceMethod(fn):
	fn.IsServiceMethod = True
	return fn

class ServiceException(Exception):
	pass

class ServiceRequestNotTranslatable(ServiceException):
	pass

class BadServiceRequest(ServiceException):
	pass

class ServiceMethodNotFound(ServiceException):
	def __init__(self, name):
		self.methodName = name

class ServiceHandler(object):

	def __init__(self, service):
		self.service = service
	
	def handleRequest(self, json):
		err = None
		result = None
		id_ = ''
		args = None
		try:
			req = self.translateRequest(json)
		except ServiceRequestNotTranslatable, e:
			err = e
			req = {'id':id_}

		if err == None:
			try:
				id_ = req['id']
				methName = req['method']
				try:
					args = req['params']	
				except:
					pass		
			except:
				err = BadServiceRequest(json)
		module_instance=None		
		if err == None:
			try:
				meth = self.locate(methName)
			except Exception, e:
				err = e

		if err == None:
			try:
				result = self.call(meth, args)
			except Exception, e:
				err = e

		resultdata = self.translateResult(result, err, id_)
		return resultdata

	def translateRequest(self, data):
		try:	
			req = loads(data)
		except:
			raise ServiceRequestNotTranslatable(data)
		return req
	 
	def locate(self, name):
		try:
			if name.startswith("system."):
				return  getattr(self, name.split(".")[1])
			module_manager = ModuleManager()
			modules = module_manager.getAllModules()
			for module in modules:
				for key in dir(module):
					try:
						method = getattr(module, key)
						if getattr(method, "IsServiceMethod"):
							if ("modules."+module.__class__.__name__ + "." + key) == name :
								meth = method
								break
					except AttributeError:
						pass
			if meth==None :
				raise ServiceMethodNotFound(name)
		except AttributeError:
			raise ServiceMethodNotFound(name)
		
		return  meth
	def listMethods(self):
		results = []
		module_manager = ModuleManager()
		modules = module_manager.getAllModules()
		for module in modules:
			for key in dir(module):
				method = getattr(module, key)
				try:
					if getattr(method, "IsServiceMethod"):
						results.append("modules."+module.__class__.__name__ + "." + key)
				except:
					pass		
		results.sort()
		return results

	def call(self, meth, args=None):
		if args == None :
			return meth()
		else:	
			return meth(args)			#return meth(*args)

	def translateResult(self, rslt, err, id_):
		if err != None:
			err = {"name": err.__class__.__name__, "message":err.message}
			rslt = None

		try:
			data = dumps({"result":rslt, "id":id_, "error":err})
		except JSONEncodeException, e:
			err = {"name": "JSONEncodeException", "message":"Result Object Not Serializable"}
			data = dumps({"result":None, "id":id_, "error":err})
			
		return data
# --------------------------------------------------------------------
# request dispatcher

