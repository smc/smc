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
	"""
		python sample_ngram.py <input file> <corpus path> 1 
		this will generate the corpus for the given input file, if corpus specified at 
		corpus path is empty. Else it will recreate the corpus with the additional data.

		python sample_ngram.py <corpus path> <start word> 2
		this will generate the graph for the given start word in the given corpus at corpus path.

		This is just a crude attempt, a lot more improvement is to be done. 		 
	"""
	if sys.argv[3] == "1":
		ngv=NGramVisualizer ()
		ngv.loadCorpus(sys.argv[1],sys.argv[2])
	elif sys.argv[3] == "2":
		printGraph(sys.argv[1],sys.argv[2])
