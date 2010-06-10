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

from utils import *
from PyMeld import Meld

class SilpaResponse(Meld):
    def __init__(self):
        Meld.__init__(self,get_template())
    def populate_form(self,request):
        #try to populate the html form with the values from the request.
        for key in request:
            try:
                value = request.get(key)
                field = self.__getattr__(key)
                field.value = value
                self.__getattr__(value).selected= 'selected' 
            except:
                pass
        return self   
        
     
        
