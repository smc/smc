#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Dictionary
# Copyright 2008 Santhosh Thottingal <santhosh.thottingal@gmail.com>
# http://www.smc.org.in
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# If you find any bugs or have any suggestions email: santhosh.thottingal@gmail.com
# URL: http://www.smc.org.in


from common import *
import os
from dictdlib import DictDB
from jsonrpc import *
class Dictionary(SilpaModule):
    
    def __init__(self):
        self.template=os.path.join(os.path.dirname(__file__), 'dictionary.html')    
        
    def get_json_result(self):
        error=None
        _id = 0
        try:
            if self.request.get('word'):
                definition = self.getdef(self.request.get('word'),self.request.get('dictionary'))
            data = dumps({"result":definition, "id":_id, "error":error})
        except JSONEncodeException:
            #translate the exception also to the error
            error = {"name": "JSONEncodeException", "message":"Result Object Not Serializable"}
            data = dumps({"result":None, "id":id_, "error":error})
        return data
        
    def get_form(self):
        page = open(self.template,'r').read()
        return page
    def get_free_dict(self, src, dest):
        dict_dir=os.path.join(os.path.dirname(__file__), 'dictionaries')
        dictdata=dict_dir+ "/freedict-"+src+"-"+dest
        if os.path.isfile(dictdata+".index"):
            return dictdata
        return None    

    @ServiceMethod  
    def getdef(self, word, dictionary):
        meaningstring= ""
        src = dictionary.split("-")[0]
        dest = dictionary.split("-")[1]
        dictdata = self.get_free_dict(src,dest)
        if dictdata:
            dict = DictDB(dictdata)
            meanings =  dict.getdef(word)
            for meaning in meanings:
                meaningstring += meaning
        if meaningstring == "None":
            meaningstring = "No definition found"
            return meaningstring
        return meaningstring
        
    def get_module_name(self):
        return "Dictionary"
        
    def get_info(self):
        return  "Bilingual Dictionaries"    
        
def getInstance():
    return Dictionary()
