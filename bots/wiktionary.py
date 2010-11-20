#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Dictionary
# Copyright 2010 Santhosh Thottingal <santhosh.thottingal@gmail.com>
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


import re
import urllib
import urllib2
import os,sys
from BeautifulSoup import BeautifulSoup
import sqlite3

def get_def(word, src_lang,dest_lang):
    meaning_from_db = get_meaning_from_database(word)
    if meaning_from_db!=None:
        return meaning_from_db[1]
    quotedfilename = urllib.quote(word.encode('utf-8')) 
    link = "http://"+dest_lang+".wiktionary.org/w/api.php?action=parse&format=xml&prop=text|revid|displaytitle&callback=?&page="+quotedfilename
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    soup=None
    meanings = None
    try:
        soup = BeautifulSoup(opener.open(link).read())
        text=  BeautifulSoup(bs_preprocess(soup('text')[0].string))

        for li in text('li'):
            try:
                if meanings==None:
                    meanings =""
                if li.a:
                    meanings+=li.a.string+"\n"
                else:    
                    meanings+=li.string+"\n"
            except:
                pass   
        if meanings!= None:        
            meanings = normalize_ml(meanings)
            add_to_database(word, meanings)             
    except:
		return None        
    return meanings
def bs_preprocess(html):
    html = html.replace("&lt;","<")
    html = html.replace("&gt;",">")
    html = html.replace('&quot;','\'')
    return html 
    
def add_to_database(word, meaning)   :
    conn = sqlite3.connect('wiktionary.sqlite')
    c = conn.cursor()
    c.execute("INSERT INTO mlwiktionary(word, meaning) values ('" + word + "','"+  meaning+"')")
    conn.commit()
    c.close()
    conn.close()

def get_meaning_from_database(word):
    conn = sqlite3.connect('wiktionary.sqlite')
    c = conn.cursor()
    rows = c.execute("SELECT word, meaning from mlwiktionary where word='" + word+"'")
    result = None
    for row in rows:
        result = row
    conn.commit()
    c.close()
    conn.close()
    return result 
    
def normalize_ml (text):
    text = text.replace(u"ൺ" , u"ണ്‍")
    text = text.replace(u"ൻ", u"ന്‍")
    text = text.replace(u"ർ", u"ര്‍")
    text = text.replace(u"ൽ", u"ല്‍")
    text = text.replace(u"ൾ", u"ള്‍")
    text = text.replace(u"ൿ", u"ക്‍")
    text = text.replace(u"ന്‍റ", u"ന്റ")
    return text   
    
if __name__ == '__main__':
    #add_to_database("hi","hello")
    #get_meaning_from_database("hi")
    print get_def(u'ഉര്‍വീധരന്‍','ml','ml')
    print get_def('Mars','ml','ml')
    print get_def('help','ml','ml')
    print get_def('father','ml','ml')
    print get_def('fathehghghghr','ml','ml')
    print get_def('fat','ml','ml')
