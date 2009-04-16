#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ngram
# Copyright 2008-2009 Santhosh Thottingal <santhosh.thottingal@gmail.com>
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

import codecs
import pickle
import pydot
import os,sys
from optparse import OptionParser
VERSION=0.1
MAX_TREE_DEPTH=1000
PICKLED_TREE="ngram.pyo"
class NgramNode:
	def __init__(self, node_value="*", rank=1, child_list=None):
		self.node_value=node_value
		self.rank=rank
		self.child_list=child_list
		self.desc="Start Node"
	def setNode(self, node_value="*", rank=None,childs=None, child_list=None):
		self.node_value=node_value
		self.rank=rank
		self.child_list=child_list
	def getName(self):
		return self.node_value	
	def getDesc(self):
		return self.desc
	def setDesc(self,desc):
		self.desc	=  desc
		return self.desc	
	def getRank(self):
		return self.rank	
	def setRank(self, rank):
		self.rank = rank
	def incrRank(self, incr=1):
		self.rank =  self.rank	+ incr
		return self.rank		
	def getChildList(self):
		if(self.child_list!=None):
			return self.child_list
		else:
			return None	
	def getChildByName(self,child_name):
		if(self.child_list==None):
			return None
		for child in self.child_list:
			if(child.getName()==child_name):
				return child
	def childIndex(self,childnode):
		if(self.child_list==None):
			return -1
		for child in self.child_list:
			if(child.getName()==childnode.getName()):
				return self.child_list.index(child)
		return -2		
	def printChildList(self):
		if(self.child_list==None):
			return None
		for child in self.child_list:
			print child,
	def addChildNode(self, node):
		if(node!=None):
			if(self.child_list==None):
				self.child_list=[]
			#Check whether this node is already present in the Ngram Tree	
			member_index=self.childIndex(node)
			if(member_index>=0):
				#Node already present.Incrementing Rank
				self.child_list[member_index].incrRank()
			else:
				self.child_list.append(node)		
		#Keep it sorted as per the ranks		
		self.child_list.sort()		
	def removeChildNode(self, node):
		if(node!=None & self.child_list!=None):
			self.child_list.remove(node)		
	def __str__(self):
		return "Node:  %s[%d]" % (self.node_value, self.rank)
	'''Recursively traverse through the tree and print the nodes-Depth First Traversal'''	
	def toString(self):
		print "Node:  %s[%d]" % (self.node_value, self.rank)
		child_list=self.getChildList()
		if(child_list!=None):
			for child_node in child_list :
				child_node.toString()
	'''Defining the less than operater of the object'''			
	def __lt__(self, node):
		return 	self.getRank() < node.getRank()
	'''Defining the greater than operater of the object'''
	def __gt__(self, node):
		return 	self.getRank() > node.getRank()
	'''Defining the equal-to operater of the object'''	
	def __eq__(self, node):
		if(node==None):
			return False
		return 	(self.getName() == node.getName()) & (self.getRank() == node.getRank())
	'''Defining the comparison of two object instances. Required for sorting the list of objects'''	
	def __cmp__(self, node):
		if(node==None):
			return 1
		if(self.getName()==node.getName()):
			return cmp(self.getRank(), node.getRank())
		else:
			return 1	
	

#Syllable Node Class
#Extends NgramNode class
class SyllableNode(NgramNode):
	def __str__(self):
		return ("Syllable: %s[%d]" % (self.node_value, self.rank )).encode('utf-8')
#Word Node Class
#Extends NgramNode class
class WordNode(NgramNode):
	def __str__(self):
		return  ("Word: %s[%d]" % (self.node_value, self.rank )).encode('utf-8')

class NGram:
	def __init__(self, text=None, language=None):
		self.text=None
		self.language=None
		try:
			#Try loading picked tree object
			self.ngrams=pickle.load(open(PICKLED_TREE))
			print "Loaded the ngram from " + PICKLED_TREE
		except:	
			#Initialize with empty node
			self.ngrams=NgramNode()
			print "New one"
		self.search_depth=0	
	def getRoot(self, node_name=None):
		if(node_name==None):
			return self.ngrams
		else:
			return self.searchNode(node_name)
				
	def searchNodeByName(self, node_name, current_node=None, depth=MAX_TREE_DEPTH):
		if(current_node==None):
			current_node=self.getRoot()
			self.search_depth = 0
		if(self.search_depth==depth):
			return None
		if(current_node.getName() == node_name):
			print "Found at depth", self.search_depth
			return current_node
		else:
			child_list=current_node.getChildList()
			if(child_list==None):
				return None
			else:
				child_list=child_list	
			self.search_depth = self.search_depth+1				
			for child_node in child_list :
				result_node=self.searchNodeByName(node_name,child_node, depth)
				if(result_node!=None):
					return result_node
	def printNgram(self, current_node=None):
		if(current_node==None):
			current_node=self.getRoot()
		print current_node
		child_list=current_node.getChildList()
		
		if(child_list==None):
			return None
		else:
			child_list.sort()	
		for child_node in child_list :
			self.printNgram(child_node)
	def toDot(self,  graph , current_node=None):
		if(current_node==None):
			current_node=self.getRoot()
		child_list=current_node.getChildList()
		if(child_list!=None):
			key=current_node.getName()
			for child_node in child_list:
				value=child_node.getName()
				if((key!=None) & ord(key[len(key)-1])<=0x0901 & len(key)>1):
					key=key[0:len(key)-1]
				if(value!=None):	
					if((ord(value[len(value)-1])<=0x0901) & len(value)>1):
						value=value[0:len(value)-2]	
					graph.add_edge(pydot.Edge(key.encode('utf-8'),value.encode('utf-8')))
					self.toDot(graph,child_node)
	def toGraph(self, output_image_file):
		graph=pydot.Dot()
		self.toDot(graph)
		#print graph.to_string().encode('utf-8')
		graph.write(output_image_file,"dot", "png" )
		
	def addSyllables(self,text, window_size=2):
		words=text.split(" ")
		ngrams = []
		for word in words:
			#TODO-Normalize before taking ngram!!!
			word = "*"+word+"]"
			syllables = self.syllabalize_ml(word)
			syllable_count = len(syllables)
			window_start = 0
			window_end = 0
			while window_start + window_size <= syllable_count:
				if(window_start + window_size < syllable_count):
					window_end = window_start + window_size
				else:
					window_end = syllable_count	
				ngrams.append(syllables[window_start:window_end])
				window_start = window_start+1
		return 	ngrams
	'''Syllabalize a given Malayalam string. Based on ml-split code by Baiju M'''		
	def syllabalize_ml(self,text):
		signs = [
		u'\u0d02', u'\u0d03', u'\u0d3e', u'\u0d3f', u'\u0d40', u'\u0d41',
		u'\u0d42', u'\u0d43', u'\u0d44', u'\u0d46', u'\u0d47', u'\u0d48',
		u'\u0d4a', u'\u0d4b', u'\u0d4c', u'\u0d4d']
		limiters = ['.','\"','\'','`','!',';',',','?', ']']
		chandrakkala = u'\u0d4d'
		lst_chars = []
		for char in text:
			if char in limiters:
				lst_chars.append(char)
			elif char in signs:
				lst_chars[-1] = lst_chars[-1] + char
			else:
				try:
					if lst_chars[-1][-1] == chandrakkala :
						lst_chars[-1] = lst_chars[-1] + char
					else:
						lst_chars.append(char)
				except IndexError:
					lst_chars.append(char)

		return lst_chars	
	def addWords(self,text, window_size=2):
		text = "* "+text+" ]"
		words = text.split(" ")
		ngrams = []
		word_count = len(words)
		window_start = 0
		window_end = 0
		while window_start + window_size <= word_count:
			if(window_start + window_size < word_count):
				window_end = window_start + window_size
			else:
				window_end = word_count	
			words[window_start:window_end]	
			ngrams.append(words[window_start:window_end])
			window_start = window_start+1
		return 	ngrams
	def populateSyllableNgram(self, text):
		ngrams = self.addSyllables(text)
		for ngram in ngrams:
			ngram_str=""
			for item in ngram:
				if(item.strip()>""):
					if(ngram_str==""):
						ngram_str=ngram_str+ item 
					else:
						
						if(ngram_str=="["):
							parent_node=self.getRoot()
						else:	
							parent_node=self.searchNodeByName(ngram_str,self.getRoot())
						if(parent_node==None):
							print "Parent node not found for " + item
						else:	
							parent_node.addChildNode(SyllableNode(item))
							print ngram_str+ " -> "+item 	
		#pickle the tree				
		pickle.dump(self.getRoot(),open(PICKLED_TREE,'w'))
 	def populateWordNgram(self, text):
		ng = NGram () 
		ngrams = ng.addWords(text)
		for ngram in ngrams:
			ngram_str=""
			for item in ngram:
				if(item.strip()>""):
					if(ngram_str==""):
						ngram_str=ngram_str+ item 
					else:
						if(ngram_str=="*"):
							parent_node=self.getRoot()
						else:	
							parent_node=self.searchNodeByName(ngram_str,self.getRoot())
						if(parent_node==None):
							print "Parent node not found for " + item
						else:	
							parent_node.addChildNode(WordNode(item))
							print ngram_str+ " -> "+item 	
		#pickle the tree				
		pickle.dump(self.getRoot(),open(PICKLED_TREE,'w'))	
if __name__ == "__main__":
	usage = "usage: %prog [options] inputfile"
	parser = OptionParser(version="%prog 0.1",description="Malayalama NGram Analyser")
	parser.set_usage(usage)
	parser.add_option("-g", "--generate-graph", dest="gen_graph",help="Generates a graph in png format to visualize the ngram")
	parser.add_option("-p", "--print", action="store_true",default=False,dest="print_ngram",help="Print the Ngram")
	parser.add_option("-i", "--input-file", dest="input_file",help="Input File for learning")
	parser.add_option("-s", "--suggest-syllables", dest="suggest_syllables",help="Suggest next possible syllables for the given letter/syllable ")
	parser.add_option("-w", "--suggest-words", dest="suggest_words",help="Suggest next possible words for the given word ")
	(options, args) = parser.parse_args()
	
	if(options.gen_graph):
		ng = NGram () 	
		ng.toGraph(options.gen_graph)
	if(options.	input_file):
		if not os.path.exists(options.input_file):
			print "File Doesnot Existis"
			sys.exit(1)
		else:
			corpus_file = codecs. open(options.input_file,encoding='utf-8', errors='ignore')
			ng = NGram () 	
			while 1:
	   			text = unicode( corpus_file.readline())	
	   			if text == "":
					break
				text= text + " ]"	
				ng.populateSyllableNgram(text)
				ng.populateWordNgram(text)
			print "Populated"
	if(options.	print_ngram):
		ng = NGram () 	
		print ng.getRoot().toString()
	if(options.	suggest_syllables):
		ng = NGram () 	
		print "Searching for" + options.suggest_words
		print ng.searchNodeByName(unicode(options.	suggest_syllables))
	if(options.	suggest_syllables):
		ng = NGram () 	
		print "Searching  for "+ options.suggest_words
		print ng.searchNodeByName(unicode(options.	suggest_words))

	
