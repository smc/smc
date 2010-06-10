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

import sys, os
from jsonrpc import ServiceHandler
import traceback
import cgitb
cgitb.enable(True, "logs/")
class CGIServiceHandler(ServiceHandler):
    def __init__(self, service):
        if service == None:
            import __main__ as service
        ServiceHandler.__init__(self, service)

    def handleRequest(self, fin=None, fout=None, env=None):
        if fin==None:
            fin = sys.stdin
        if fout==None:
            fout = sys.stdout
        if env == None:
            env = os.environ
        
        try:
            contLen=int(env['CONTENT_LENGTH'])
            data = fin.read(contLen).decode("utf-8")
        except Exception, e:
            data = ""

        resultData = ServiceHandler.handleRequest(self, data)
        
        response = "Content-Type: text/plain\n"
        response += "Content-Length: %d\n\n" % len(resultData)
        response += resultData
        
        #on windows all \n are converted to \r\n if stdout is a terminal and  is not set to binary mode :(
        #this will then cause an incorrect Content-length.
        #I have only experienced this problem with apache on Win so far.
        if sys.platform == "win32":
            try:
                import  msvcrt
                msvcrt.setmode(fout.fileno(), os.O_BINARY)
            except:
                pass
        #put out the response
        fout.write(response.encode('utf-8'))
        fout.flush()

def handleCGI(service=None, fin=None, fout=None, env=None):
    CGIServiceHandler(service).handleRequest(fin, fout, env)
