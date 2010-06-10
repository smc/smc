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
#

import sys
from utils import *

class ModuleManager:

    def import_module(self,name):
        parts = name.split(".")
        try:
            obj= sys.modules[name]
        except KeyError:
            obj  = __import__(name)
        if(len(parts)>1):   
            for part in parts[1:]:
                try:
                    obj = getattr(obj,part)
                except:
                    pass
        return obj

    def getModuleInstance(self,action):
        action=action.replace(" ","_")
        if action == 'AllModules':
            #List the available modules
            return self
        module_name = self.find_module(action)
        if(module_name):
            try:
                return self.import_module(module_name).getInstance()
            except:
                print "Failed to get instance for " +  module_name
            
    def find_module(self,action):
        if action == 'AllModules':
            #List the available modules
            return True #Well, that was not good
        try:
            return getModulesList()[action]
        except: 
            return None
            
    def getModulesInfoAsHTML(self):
        module_dict=getModulesList  ()
        response = "<h2>Available Modules</h2></hr>"
        response = response+"<table class=\"table1\"><tr><th>Module</th><th>Description</th></tr>"
        for action in   module_dict:
            module_instance=self.getModuleInstance(action)
            if(module_instance!=None):
                response = response+"<tr><td><a href='"+ action +"'>"+module_instance.get_module_name()+"</a></td>"
                response = response+"<td>"+module_instance.get_info()+"</td></tr>"
            else:
                response = response+"<tr><td>"+action.replace("_"," ")+"</td>"
                response = response+"<td>Error while retrieving module details</td></tr>"   
        return  response+"</table>" 

    def get_form(self):
        return  self.getModulesInfoAsHTML()

    def getAllModules(self):
        """
        return a list of all the modules available in the system
        """
        modules=[]
        module_dict=getModulesList  ()
        for action in   module_dict:
            module_instance=self.getModuleInstance(action)
            modules.append(module_instance)
        modules.sort()
        return modules  

    def getServiceMethods(self):
        """
        Return the dictionary of service methods defined in all modules
        dictionary key: the method name. for eg: modules.spellchecker.suggest.
        dictionary value : The invocable method.
        """
        service_methods = dict()
        modules = self.getAllModules()
        for module in modules:
            for key in dir(module):
                try:
                    method = getattr(module, key)
                    if getattr(method, "IsServiceMethod"):
                        service_methods["modules."+module.__class__.__name__ + "." + key] = method
                except AttributeError:
                    #ignore it!
                    pass
        return service_methods
