# -*- coding: utf-8 -*-
# Copyright 2009-2010
# Santhosh Thottingal <santhosh.thottingal@gmail.com>
# This code is part of Silpa project.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

from common import *
from utils import *
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
        self.service_methods = None
    
    def handleRequest(self, json):
        """
        Handle the json request,  locate the methods in the modules, invoke, 
        translate the method result to json and return
        """
        err = None
        meth=None
        result = None
        id_ = ''
        args = None
        #Translate the json request to python objects
        try:
            req = self.translate_request(json)
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

        #Locate the method
        if err == None:
            try:
                meth = self.locate(methName)
            except Exception, e:
                err = e
        #Invoke the method 
        if err == None:
            try:
                result = self.call(meth, args)
            except Exception, e:
                err = e
        resultdata = self.translate_result(result, err, id_)
        
        return resultdata

    def translate_request(self, data):
        """
        Translate the json request to python objects
        """
        try:    
            req = loads(data)
        except:
            raise ServiceRequestNotTranslatable(data)
        return req
     
    def locate(self, method_name):
        """
        Locate the service method to the defined methods in the system
        If the method is not found, raise ServiceNotFound exception
        """
        meth=None
        try:
            if self.service_methods == None:
                #initialize the singleton instance. This will take time. but will be invoked only
                #once in the life cycle of application
                module_manager = ModuleManager()
                self.service_methods = module_manager.getServiceMethods()
            if method_name.startswith("system."):
                return  getattr(self, method_name.split(".")[1])
            try:
                return self.service_methods[method_name]
            except KeyError:
                raise ServiceMethodNotFound(method_name)
        except AttributeError:
            raise ServiceMethodNotFound(method_name)
        
        return  meth

    def listMethods(self):
        """
        Serves the system.listMethods calls
        """
        results = []
        if self.service_methods == None:
            module_manager = ModuleManager()
            self.service_methods = module_manager.getServiceMethods()
        for method in self.service_methods:
            results.append(method)
        results.sort()
        return results

    def call(self, method, args):
        """
        Invoke the method with the given arguments
        """
        _args=None
        for  arg in args:
            if arg!='':
                if _args==None: 
                    _args=[]
                _args.append(arg)   
        if _args==None:
            #invoke without arguments
            return method()   
        else:   
            #Call it!
            return method(*_args)
        

    def translate_result(self, result, error, id_):
        """
        Translate the method results back to the json.
        """
        if error != None:
            #Construct the error message json
            error = {"name": error.__class__.__name__, "message":error}
            result = None
        try:
            data = dumps({"result":result, "id":id_, "error":error})
        except JSONEncodeException, e:
            #translate the exception also to the error
            error = {"name": "JSONEncodeException", "message":"Result Object Not Serializable"}
            data = dumps({"result":None, "id":id_, "error":error})
        return data


