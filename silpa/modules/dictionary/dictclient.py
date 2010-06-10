#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Dictionary Client
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

from dictdlib import DictDB
en_ml_db=DictDB("/usr/share/dictd/freedict-eng-mal")
print en_ml_db.getdef('help')[0]
ml_ml_db=DictDB("/usr/share/dictd/dict-ml-ml")
print en_ml_db.getdef('ഭയങ്കരം')

