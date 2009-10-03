#  Spellchecker with language detection
#  coding: utf-8
#
#  Copyright © 2008  Santhosh Thottingal
#  Released under the GPLV3+ license
import string
def detect_lang(word):
    if(word):
        for punct in string.punctuation:
            word = word.replace(punct," ")    
        length = len(word)
        index = 0
        while index < length:
            letter=word[index]
            if not letter.isalpha():
                index=index+1   
                continue
            if ((letter >= u'ം') &  (letter <=u'൯')):
                return "ml_IN"
            if ((letter >= u'ঁ') &  (letter <= u'৺')):
                return "bn_IN"
            if ((letter >= u'ँ') &  (letter <= u'ॿ')):
                return "hi_IN"
            if ((letter >=u'ઁ') &  (letter <= u'૱')):
                return "gu_IN"
            if ((letter >= u'ਁ') &  (letter <=u'ੴ')):
                return "pa_IN"
            if ((letter >= u'ಂ') &  (letter <=u'ೲ')):
                return "kn_IN"
            if ((letter >= u'ଁ') &  (letter <= u'ୱ')):
                return "or_IN"
            if ((letter >=u'ஂ') &  (letter <= u'௺')):
                return "ta_IN"
            if ((letter >=u'ఁ') &  (letter <= u'౯')):
                return "te_IN"
            if ((letter <= u'z')):
                return "en_US"
            index=index+1   
