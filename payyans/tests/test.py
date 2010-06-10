#!/usr/bin/python
# -*- coding: utf-8 -*-
from payyans import Payyan
p=Payyan()
p.mapping_filename="/usr/share/payyans/maps/karthika.map"
#p.mapping_filename="../maps/matweb.map"
print p.word2Unicode(u"hmÀjnI").encode('utf-8')
print p.word2ASCII(u"വാര്‍ഷിക").encode('utf-8')
print p.word2ASCII(u"ആന വായിലമ്പാഴങ്ങ?").encode('utf-8')
print p.word2Unicode(u"B\ hmbne¼mg§?").encode('utf-8')
print p.word2ASCII(u"മോരു തരുമോ!").encode('utf-8')
print p.word2Unicode(u"tamcp Xcptam!").encode('utf-8')
manorama_string=u"ÄßøáÕÈLÉáø¢: çµø{JßW ÈßÏÎÕÞÝíº ÄµVKáæÕKí ¼ÈÄÞÆZ çÈÄÞÕí ®¢.Éß. ÕàçødwµáÎÞV. ÄßøæE¿áMßÈá çÖ×¢ ¼ÈÄÞÆ{ßæa ³ËßØí ¥dµÎß‚ÕVæAÄßæø È¿É¿ß çÕÃæÎKí ¦ÕÖcæMGá Îá~cÎdLßAá ÈßçÕÆÈ¢ ÈWµßÏ çÖ×¢ ÎÞÇcÎBç{Þ¿á Ø¢ØÞøßAáµÏÞÏßøáKá..."
p=Payyan()
p.mapping_filename="../maps/manorama.map"
print p.word2Unicode(manorama_string).encode('utf-8')
p=Payyan()
marathi_string=u"AmË_hË`m  Am° Zm© nmpíM_mË` Xoem§gmaIm Amnë`mH$S>o ~oH$mam§Zm OJVm"
p.mapping_filename="../maps/mr_sample.map"
print p.word2Unicode(marathi_string).encode('utf-8')
