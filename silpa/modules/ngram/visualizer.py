#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Ngram
# Copyright 2008 Santhosh Thottingal <santhosh.thottingal@gmail.com>
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
import pydot
import codecs

class NGramVisualizer:
	depth=0
	def loadCorpus(self, corpus_file_name):	
		graph_dict = dict()
		line = []
		line_number = 0
		rule_number = 0
		corpus_file = codecs. open(corpus_file_name,encoding='utf-8', errors='ignore')
		while 1:
			line_number = line_number +1 
   			text = unicode( corpus_file.readline())
			if text == "":
			      break
			if text[0] == '#': 
			      continue 
			line_number = line_number +1       
			line = text.strip()
			if(line == ""):
				  continue 
			words=line.split(" ")
			word_count=len(words)
			prev_word=""
			for word in words:
				word=word.strip()
				if(prev_word==""):
					prev_word=word	
					continue;
				if(prev_word!=""):
					if(graph_dict.has_key(prev_word)):
						graph_dict[prev_word]=graph_dict[prev_word]+" -> "+word
					else:
						graph_dict[prev_word]=word
					prev_word=word	
			prev_word=""		
		return graph_dict
	def generate_full_graph(self, start_word, graph_dict,outputimage):
		
		for key in graph_dict.iterkeys():
			values=graph_dict[key].split("->")
			for value in values:
				value=value.strip()
				#print key, value
				if(start_word>""):
					if(key==start_word):
						graph.add_edge(pydot.Edge(key.encode('utf-8'),value.encode('utf-8')))
				else:
					graph.add_edge(pydot.Edge(key.encode('utf-8'),value.encode('utf-8')))		
		
		
	def generate_graph(self, graph_dict, graph, src):
		self.depth=self.depth+1
		#print self.depth ,src 
		if(graph.get_node(src)!=[]):
			return graph
		if(self.depth>200):
			return graph
		values=[]		
		if(graph_dict.has_key(src))	:
			values=graph_dict[src].split("->")
		for dest in values:
			dest=dest.strip()
			#print src, dest,graph.get_edge(src,dest)
			if(graph.get_edge(src,dest)):
				continue
			else:	
				graph.add_edge(pydot.Edge(src,dest))	
				graph=self.generate_graph(graph_dict, graph, dest)
				
		return graph
		
if __name__ == "__main__":
	ngv=NGramVisualizer () 
	graph_dict=ngv.loadCorpus ("hi.txt")
	graph=pydot.Dot()
	graph=ngv.generate_graph(graph_dict, graph,u"भारत")
	print graph.to_string().encode("utf-8")
	#graph.write("ngvgraph-hi.png","dot", "raw" )
