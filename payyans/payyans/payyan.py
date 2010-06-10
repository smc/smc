#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Payyans Ascii to Unicode Convertor
# Copyright 2008-2010 Santhosh Thottingal <santhosh.thottingal@gmail.com>,
# Nishan Naseer <nishan.naseer@gmail.com>, Manu S Madhav <manusmad@gmail.com>,
# Rajeesh K Nambiar <rajeeshknambiar@gmail.com>
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


import sys 
import codecs 
import os 
from optparse import OptionParser 
 
class Payyan:

    def __init__(self):
        self.input_filename =""
        self.output_filename=""
        self.mapping_filename=""
        self.rulesDict=None
        self.pdf=0
        
    def word2ASCII(self, unicode_text):
        index = 0
        prebase_letter = ""
        ascii_text=""
        self.direction = "u2a"
        self.rulesDict = self.LoadRules()
        while index < len(unicode_text):
            '''This takes care of conjuncts '''
            for charNo in [3,2,1]:
                letter = unicode_text[index:index+charNo]
                if letter in self.rulesDict:
                    ascii_letter = self.rulesDict[letter]
                    letter = letter.encode('utf-8')
                    '''Fixing the prebase mathra'''
                    '''TODO: Make it generic , so that usable for all indian languages'''
                    if letter == 'ൈ':
                        ascii_text = ascii_text[:-1] + ascii_letter*2 + ascii_text[-1:]
                    elif (letter == 'ോ') | (letter == 'ൊ') | (letter == 'ൌ'):    #prebase+postbase mathra case
                        ascii_text = ascii_text[:-1] + ascii_letter[0] + ascii_text[-1:] + ascii_letter[1]
                    elif (letter == 'െ') | (letter == 'േ') |(letter == '്ര'):    #only prebase
                        ascii_text = ascii_text[:-1] + ascii_letter + ascii_text[-1:]
                    else:
                        ascii_text = ascii_text + ascii_letter                        
                    index = index+charNo
                    break
                else:
                    if(charNo==1):
                        index=index+1
                        ascii_text = ascii_text + letter
                        break;
                    '''Did not get'''                
                    ascii_letter = letter

        return ascii_text
        
    def Uni2Ascii(self):
        if self.input_filename :
            uni_file = codecs.open(self.input_filename, encoding = 'utf-8', errors = 'ignore')
        else :
            uni_file = codecs.open(sys.stdin, encoding = 'utf-8', errors = 'ignore')            
        text = ""
        if self.output_filename :
            output_file = codecs.open(self.output_filename, encoding = 'utf-8', errors = 'ignore',  mode='w+')            
        while 1:
            text =uni_file.readline()
            if text == "":
                break
            ascii_text = ""    
            ascii_text = self.word2ASCII(text)
                                    
            if self.output_filename :
                output_file.write(ascii_text)
            else:
                print ascii_text.encode('utf-8')
        return 0
        
    def word2Unicode(self, ascii_text):
        index = 0
        post_index = 0
        prebase_letter = ""
        postbase_letter = ""
        unicode_text = ""
        next_ucode_letter = ""
        self.direction="a2u"
        self.rulesDict = self.LoadRules()
        while index < len(ascii_text):
            for charNo in [3,2,1]:
                letter = ascii_text[index:index+charNo]
                #print '>'+ letter.encode('utf-8')
                if letter in self.rulesDict:
                    unicode_letter = self.rulesDict[letter]
                    if(self.isPrebase(unicode_letter)):
                        #print (unicode_letter +" is prebase").encode('utf-8')
                        prebase_letter = unicode_letter
                        
                    else:
                        post_index = index+charNo
                        if post_index < len(ascii_text):
                            letter = ascii_text[post_index]
                            if letter in self.rulesDict:
                                next_ucode_letter = self.rulesDict[letter]
                                if self.isPostbase(next_ucode_letter):
                                    postbase_letter = next_ucode_letter
                                    index = index + 1
                        if  ((unicode_letter.encode('utf-8') == "എ") |
                            ( unicode_letter.encode('utf-8') == "ഒ" )):
                            unicode_text = unicode_text + postbase_letter + self.getVowelSign(prebase_letter , unicode_letter)
                        else:
                            unicode_text = unicode_text + unicode_letter + postbase_letter + prebase_letter
                        prebase_letter=""
                        postbase_letter=""
                    index = index + charNo
                    break
                else:
                    if charNo == 1:
                        unicode_text = unicode_text + letter
                        index = index + 1
                        break
                    unicode_letter = letter
        return unicode_text    
    
    def Ascii2Uni(self):
        if self.pdf :
            command = "pdftotext '" + self.input_filename +"'"
            process = os.popen(command, 'r')
            status = process.close()
            if status:
                print "The input file is a PDF file. To convert this the  pdftotext  utility is required. "
                print "This feature is available only for GNU/Linux Operating system."
                return 1    # Error - no pdftotext !
            else:
                self.input_filename =  os.path.splitext(self.input_filename)[0] + ".txt"
        if self.input_filename :
            ascii_file = codecs.open(self.input_filename, encoding = 'utf-8', errors = 'ignore')
        else :
            ascii_file = codecs.open(sys.stdin, encoding = 'utf-8', errors = 'ignore')            
        
        text = ""
        if self.output_filename :
            output_file = codecs.open(self.output_filename, encoding = 'utf-8', errors = 'ignore',  mode='w+')            
    
        while 1:
            text =ascii_file.readline()
            if text == "":
                break
            unicode_text = ""
            unicode_text = self.word2Unicode(text)
            
            if self.output_filename :
                output_file.write(unicode_text)
            else:
                print unicode_text.encode('utf-8')
        return 0

    def getVowelSign(self, vowel_letter, vowel_sign_letter):
        """
        looks like a rare case in malayalam alone
        where a vowel sign will get applied to vowel in ascii fonts
        """
        vowel=  vowel_letter.encode('utf-8')
        vowel_sign=  vowel_sign_letter.encode('utf-8')
        if vowel == "എ":
            if vowel_sign == "െ":
                return "ഐ"
        if vowel == "ഒ":
            if vowel_sign == "ാ":
                return "ഓ"
            if vowel_sign =="ൗ":
                return "ഔ"
        return (vowel_letter+ vowel_sign_letter)

    def isPrebase(self, letter):
         unicode_letter = letter.encode('utf-8')
         #Add the prebase signs in the below table. 
         ml_prebases = ["േ", "ൈ" ,"ൊ","്ര","െ", "ൌ","ൗ"  ]
         hi_prebases = ["ि","र्"]
         gu_prebases = []
         ta_prebases = []
         te_prebases = []
         kn_prebases = []
         bn_prebases = []
         or_prebases = []
         pa_prebases = []
         if( (unicode_letter  in ml_prebases)
            or (unicode_letter  in ml_prebases)
            or (unicode_letter  in hi_prebases)
            or (unicode_letter  in or_prebases)
            or (unicode_letter  in kn_prebases)
            or (unicode_letter  in ta_prebases)
            or (unicode_letter  in bn_prebases)
            or (unicode_letter  in te_prebases)
            or (unicode_letter  in pa_prebases)
            or (unicode_letter  in gu_prebases)
            ):
            return True
         else:
            return False
            
    def isPostbase(self, letter):
        unicode_letter = letter.encode('utf-8')
        ml_postbases = [ "്യ","്വ" ]
        hi_postbases = []
        pa_postbases = []
        gu_postbases = []
        pn_postbases = []
        kn_postbases = []
        te_postbases = []
        ta_postbases = []
        or_postbases = []
        bn_postbases = []
        if ( (unicode_letter in ml_postbases) 
            or (unicode_letter in kn_postbases) 
            or (unicode_letter in ta_postbases) 
            or (unicode_letter in te_postbases) 
            or (unicode_letter in or_postbases) 
            or (unicode_letter in bn_postbases) 
            or (unicode_letter in hi_postbases) 
            or (unicode_letter in pa_postbases) 
            or (unicode_letter in gu_postbases) 
            ):
            return True
        else:
            return False
                    
    def LoadRules(self):    
        if(self.rulesDict):
            return self.rulesDict
        rules_dict = dict()
        line = []
        line_number = 0
        rules_file = codecs. open(self.mapping_filename,encoding='utf-8', errors='ignore')
        while 1:
            ''' Keep the line number. Required for error reporting'''
            line_number = line_number +1 
            text = unicode( rules_file.readline())
            if text == "":
                  break
            '''Ignore the comments'''
            if text[0] == '#': 
                  continue 
            line = text.strip()
            if(line == ""):
                  continue 
            if(len(line.split("=")) != 2):
                    print "Error: Syntax Error in the Ascii to Unicode Map in line number ",  line_number
                    print "Line: "+ text
                    return 2    # Error - Syntax error in Mapping file 
            lhs = line.split("=") [ 0 ]  
            rhs = line.split("=") [ 1 ]  
            lhs=lhs.strip()
            rhs=rhs.strip()
            if self.direction == 'a2u':
                rules_dict[lhs]=rhs
            else:
                rules_dict[rhs]=lhs
        return rules_dict
