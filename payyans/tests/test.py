#!/usr/bin/python
# -*- coding: utf-8 -*-
from payyans import Payyan
p=Payyan()
p.mapping_filename="/usr/share/payyans/maps/karthika.map"
print p.word2Unicode(u"hmÀjnI").encode('utf-8')
print p.word2ASCII(u"വാര്‍ഷിക").encode('utf-8')
print p.word2ASCII(u"ആന വായിലമ്പാഴങ്ങ?").encode('utf-8')
print p.word2Unicode(u"B\ hmbne¼mg§?").encode('utf-8')
print p.word2ASCII(u"മോരു തരുമോ!").encode('utf-8')
print p.word2Unicode(u"tamcp Xcptam!").encode('utf-8')
