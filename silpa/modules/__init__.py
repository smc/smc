#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(__file__))
dirs = os.listdir(os.path.dirname(__file__))
for dir in dirs:
    if os.path.isdir(os.path.join(os.path.dirname(__file__),dir)):
        try:
            __import__(dir)
            #print "Loading Module " + dir + " OK"
        except:
            print "Loading Module " + dir + " Failed"
