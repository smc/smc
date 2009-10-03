import chardataeffect, inkex, string
from hyphenator import Hyphenator
class C(chardataeffect.CharDataEffect):
  def process_chardata(self,text, line=False, par=False):
    # insert softhyphens
    return Hyphenator().hyphenate(text, u'\u00AD')
	
c = C()
c.affect()
