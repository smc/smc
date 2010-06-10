# -*- coding: utf-8 -*-
# Copyright 2009-2010 Santhosh Thottingal <santhosh.thottingal@gmail.com>
# http://www.smc.org.in
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
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

import sys,os
sys.path.append(os.path.dirname(__file__))
import common
import modules
from  utils import *
from silpa import Silpa
if __name__ == '__main__':
    print("Silpa server loading ...")
    port = 8080
    if len(sys.argv)> 1:
        port = int(sys.argv[1])
    try:
        from wsgiref import simple_server
        silpa = Silpa()
        print("Listening on port : " + str(port))
        print("Silpa is ready!!!")
        simple_server.make_server('', port, silpa.serve).serve_forever()
    except KeyboardInterrupt:
        print("Ctrl-C caught, Silpa server exiting...")



