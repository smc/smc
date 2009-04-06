#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Ngram
# Copyright 2009 Jinesh K J <jinesh.k@gmail.com>
# Copyright 2009 Swathantra Malayalam Computing <smc-discuss@googlegroups.com>
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
# If you find any bugs or have any suggestions email: jinesh.k@gmail.com or smc-discuss@googlegroups.com
# URL: http://www.smc.org.in
import pydot
import codecs
import pickle
import sys 
from visualizer import NGramVisualizer
from optparse import OptionParser

def getData(new_file_name):
	line = []
	line_number = 0
	rule_number = 0
	corpus=""
	data_file = codecs. open(new_file_name,encoding='utf-8', errors='ignore')
	while 1:
		line_number = line_number +1 
		text = unicode( data_file.readline())
		if text == "":
		      break
		if text[0] == '#': 
		      continue 
		line_number = line_number +1       
		line = text.strip()
		if(line == ""):
			  continue 
		corpus=corpus+" "+line
	return corpus

def printGraph(corpus,start_word):
	ngv=NGramVisualizer ()
	graph_dict=pickle.load(open(corpus))
	graph=pydot.Dot()
	uni_start_word = start_word.decode("utf-8")
#	print start_word
#	print uni_start_word
	graph=ngv.generate_graph(graph_dict, graph,uni_start_word)
	print graph.to_string().encode("utf-8")

if __name__ == "__main__":
	usage = "usage: %prog [options] INPUTDATA CORPUSFILE"
	parser = OptionParser(version="%prog 1.0",description="Sample program to add data INPUTDATA to the corpus in CORPUSFILE")
	parser.set_usage(usage)
	parser.add_option("-s", "--start-word", dest="start_word",action="store_true",default=False,help="Creates a graph beginning from INPUTDATA")
	parser.add_option("-f", "--file", action="store_true",default=False,dest="infile",help="Gets Data from file INPUTDATA")
	(options, args) = parser.parse_args()
	if len(args) != 2 :	
		parser.error("incorrect number of arguments")
	if options.infile and options.start_word:
	    parser.error("options -f and -s are mutually exclusive")
	ngv=NGramVisualizer ()
	if options.infile:
		data = getData(args[0])
	#	print data
		ngv.loadCorpus(data,args[1])
	elif options.start_word:
		printGraph(args[1],args[0])
	else:
	#	print args[0]
		data = args[0].decode("utf-8")
		ngv.loadCorpus(data,args[1])
