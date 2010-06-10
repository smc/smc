#!/usr/bin/env python
"""mlsplit - Split Malayalam words into letters

This script splits Malayalam words into letters.
Ref: http://tinyurl.com/3v729s



Copyright (C) 2008 Baiju M <baiju.m.mail AT gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at
your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys
import re
import os
import codecs
from common import *
from utils import *
class Syllabalizer(SilpaModule):
    def __init__(self):
        self.template=os.path.join(os.path.dirname(__file__), 'syllabalizer.html')
    
    def syllabalize_ml(self,text):
        signs = [
        u'\u0d02', u'\u0d03', u'\u0d3e', u'\u0d3f', u'\u0d40', u'\u0d41',
        u'\u0d42', u'\u0d43', u'\u0d44', u'\u0d46', u'\u0d47', u'\u0d48',
        u'\u0d4a', u'\u0d4b', u'\u0d4c', u'\u0d4d', u'\u0d57']
        limiters = ['.','\"','\'','`','!',';',',','?']

        chandrakkala = u'\u0d4d'
        lst_chars = []
        for char in text:
            if char in limiters:
                lst_chars.append(char)
            elif char in signs:
                lst_chars[-1] = lst_chars[-1] + char
            else:
                try:
                    if lst_chars[-1][-1] == chandrakkala:
                        lst_chars[-1] = lst_chars[-1] + char
                    else:
                        lst_chars.append(char)
                except IndexError:
                    lst_chars.append(char)

        return lst_chars
    def syllabalize_kn(self,text):
        signs = [
        u'\u0c82', u'\u0c83', u'\u0cbd', u'\u0cbe', u'\u0cbf', u'\u0cc0', u'\u0cc1',
        u'\u0cc2', u'\u0cc3', u'\u0cc4', u'\u0cc6', u'\u0cc7', u'\u0cc8',
        u'\u0cca', u'\u0ccb', u'\u0ccc', u'\u0ccd']
        limiters = ['.','\"','\'','`','!',';',',','?']

        halant = u'\u0ccd'
        lst_chars = []
        for char in text:
            if char in limiters:
                lst_chars.append(char)
            elif char in signs:
                lst_chars[-1] = lst_chars[-1] + char
            else:
                try:
                    if lst_chars[-1][-1] == halant:
                        lst_chars[-1] = lst_chars[-1] + char
                    else:
                        lst_chars.append(char)
                except IndexError:
                    lst_chars.append(char)

        return lst_chars    
    def syllabalize_bn(self,text):
        signs = [
        u'\u0981', u'\u0982', u'\u0983', u'\u09bd', u'\u09be', u'\u09bf', u'\u09c0', u'\u09c1',
        u'\u09c2', u'\u09c3', u'\u09c4', u'\u09c6', u'\u09c7', u'\u09c8',
        u'\u09ca', u'\u09cb', u'\u09cc', u'\u09cd', u'\u09d7']
        limiters = ['.','\"','\'','`','!',';',',','?']

        halant = u'\u09cd'
        lst_chars = []
        for char in text:
            if char in limiters:
                lst_chars.append(char)
            elif char in signs:
                lst_chars[-1] = lst_chars[-1] + char
            else:
                try:
                    if lst_chars[-1][-1] == halant:
                        lst_chars[-1] = lst_chars[-1] + char
                    else:
                        lst_chars.append(char)
                except IndexError:
                    lst_chars.append(char)

        return lst_chars        
    def syllabalize_hi(self,text):
        signs = [
        u'\u0902', u'\u0903', u'\u093e', u'\u093f', u'\u0940', u'\u0941',
        u'\u0942', u'\u0943', u'\u0944', u'\u0946', u'\u0947', u'\u0948',
        u'\u094a', u'\u094b', u'\u094c', u'\u094d']
        limiters = ['.','\"','\'','`','!',';',',','?']

        chandrakkala = u'\u094d'
        lst_chars = []
        for char in text:
            if char in limiters:
                lst_chars.append(char)
            elif char in signs:
                lst_chars[-1] = lst_chars[-1] + char
            else:
                try:
                    if lst_chars[-1][-1] == chandrakkala:
                        lst_chars[-1] = lst_chars[-1] + char
                    else:
                        lst_chars.append(char)
                except IndexError:
                    lst_chars.append(char)

        return lst_chars    
    #Source: http://www.python-forum.org/pythonforum/viewtopic.php?f=14&t=5810#p42091
    #Author: Cabu
    def syllabalize_en(self,text):
        text = " " + text + " "
        vowel_list       = ['a', 'e', 'i', 'o', 'u', 'y']
        vowel_pairs      = ['ai', 'au', 'aw', 'ee','ea', 'oa', 'oi', 'ou', 'oo', 'ow', 'oy', 'uu']
        consonant_list   = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
        consonant_blends = ['bl', 'br', 'ch', 'chr', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'kn', 'pl', 'pr',
                            'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'spr', 'squ', 'st', 'str', 'sw',
                            'th', 'tr', 'thr', 'nt', 'wh']

        # Cut numbers in digits
        p = re.compile ("([0-9])([0-9])", re.IGNORECASE)
        for i in range (2):
            text = p.sub ("\\1#\\2", text)
           
        # Cut i / vowel (- o) / consonant
        p = re.compile ("i([aeiuy])([bcdfghjklmnpqrstvwxz])", re.IGNORECASE)
        text = p.sub ("i+\\1+\\2", text)
       
        # Cut the / vowel / consonant
        p = re.compile ("the([aeiouy])([bcdfghjklmnpqrstvwxz])", re.IGNORECASE)
        text = p.sub ("the+\\1+\\2", text)
       
        # Cut vowel / vowel except for pairs
        position = 0
        while position < len (text)-1:
            if text [position] in vowel_list and text [position+1] in vowel_list:
                if not (text [position:position+2] in vowel_pairs):
                    if not (text [position-1:position+3] in ["tion", "dual", "nion", "quir", "tiou"]):
                        text = text [:position+1] + "_" + text [position+1:]
            position = position + 1
           
        # Cut consonant / consonant (ll, mm, ...)
        p = re.compile ("([bcdfghjklmnpqrstvwxz])\\1([^ ])", re.IGNORECASE)
        text = p.sub ("\\1-\\1\\2", text)
       
        # Cut vowel / consonant vowel
        start = 0
        end = 0
        while start < len (text)-1:
            if text [start] in vowel_list and text [start+1] in consonant_list:
                end = start + 1
                while end <= len (text)-1 and text [end] in consonant_list:
                    end = end + 1
                if end <= len (text)-1 and (text [start+1:end] in consonant_list or text [start+1:end] in consonant_blends) and text [end] in vowel_list and text [end:end+2] <> "e ":
                    text = text [:start+1] + "/" + text [start+1:]
            start = start + 1
           
        # Cut vowel consonant / consonant+ vowel (trumpet, simple, understanding, ...)
        start = 0
        end = 0
        while start < len (text)-1:
            if text [start] in vowel_list and text [start+1] in consonant_list:
                end = start + 2
                while end <= len (text)-1 and text [end] in consonant_list:
                    end = end + 1
                if end <= len (text)-1 and end > start+2 and text [end] in vowel_list:
                    if not (text [start+1:end] in consonant_blends):
                        text = text [:start+2] + "-" + text [start+2:]
            start = start + 1

        # Return the words splitted
        return text
    def get_module_name(self):
        return "Syllabalizer"
    def get_info(self):
        return  "Syllabalize each word in the given text"
        
    @ServiceMethod  
    def syllabalize(self,text):
        lang=detect_lang(text)[text]
        if(lang=="ml_IN"):
            return self.syllabalize_ml(text)
        if(lang=="hi_IN"):
            return self.syllabalize_hi(text)
        if(lang=="kn_IN"):
            return self.syllabalize_kn(text)    
        if(lang=="bn_IN"):
            return self.syllabalize_bn(text)        
        if(lang=="en_US"):
            return self.syllabalize_en(text)
        lst_chars=[]
        for  char in text:
            lst_chars.append(char)
        return lst_chars    
def getInstance():
        return Syllabalizer()
