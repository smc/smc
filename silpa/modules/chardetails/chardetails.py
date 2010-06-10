#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Unicode Character Details
# Copyright 2008-2010 Santhosh Thottingal <santhosh.thottingal@gmail.com>
# http://www.smc.org.in
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# If you find any bugs or have any suggestions email: santhosh.thottingal@gmail.com
# URL: http://www.smc.org.in
from common import *
import os,sys
from unicodedata import *
class CharDetails(SilpaModule):
    def __init__(self):
        self.template=os.path.join(os.path.dirname(__file__), 'chardetails.html')
    
    @ServiceMethod          
    def getdetails(self, text):
        chardetails={}
        details={}
        for character in text:
            details['Name']= name(character) 
            details['HTML Entity']=str(ord(character)) 
            details['Code point']= repr(character)
            try:
                details['Numeric Value'] = numeric (character)
            except:
                pass    
            try:        
                details['Decimal Value']=decimal (character)
            except:
                pass    
            try:        
                details['Digit']=digit(mychar)
            except:
                pass    
            details['Alphabet']=str(character.isalpha())
            details['Digit']=str(character.isdigit())
            details['AlphaNumeric']=str(character.isalnum())
            details['Canonical Decomposition']=  decomposition(character)
            chardetails[character] = details
        chardetails['Characters'] = list(text)
        print  dumps(chardetails)
        return dumps(chardetails)
    
    def get_module_name(self):
        return "Unicode Character Details"
    def get_info(self):
        return  "Shows the Unicode Character Details of a given character"  
        
def getInstance():
    return CharDetails()

    
