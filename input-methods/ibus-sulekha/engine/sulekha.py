# vim:set et sts=4 sw=4:
#
# ibus-sulekha - The Sulekha engine for IBus
#
# Copyright(c) 2009 Santhosh Thottingal <santhosh.thottingal@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import gobject
import pango
import ibus
import keymap
import autocomplete
from ibus import keysyms
from ibus import modifier

class SulekhaEngine(ibus.EngineBase):
    
    def __init__(self, bus, object_path):
        super(SulekhaEngine, self).__init__(bus, object_path)
        self.__keymap = keymap.Keymap("swanalekha_ml_IN")
        self.__input_method="en_US"
        self.__autocomplete=autocomplete.Autocomplete()
        self.__is_invalidate = False
        self.__preedit_string = u""
        self.__current_word = u""
        self.__lookup_table = ibus.LookupTable()
        self.__prop_list = ibus.PropList()
        self.__prop_list.append(ibus.Property(u"test", icon = u"ibus-locale"))

    def process_key_event(self, keyval, state):
        # ignore key release events
        is_press = ((state & modifier.RELEASE_MASK) == 0)
        if not is_press:
            return False

        if self.__preedit_string:
            if keyval == keysyms.Return:
                if self.__lookup_table.get_number_of_candidates() > 0:
                    self.__commit_string(self.__lookup_table.get_current_candidate().text)
                else:
                    self.__commit_string(self.__preedit_string)
                return True
            elif keyval == keysyms.Escape:
                self.__preedit_string = u""
                self.__update()
                return True
            elif keyval == keysyms.BackSpace:
                self.__preedit_string = self.__preedit_string[:-1]
                self.__current_word = self.__current_word[:-1]
                self.__invalidate()
                return True
            elif keyval == keysyms.space:
                self.__commit_string(self.__preedit_string)
                previous_word=self.__current_word
                self.__current_word = u""
                self.__update_prediction(previous_word)
                return False
            elif keyval >= keysyms._1 and keyval <= keysyms._9:
                index = keyval - keysyms._1
                candidates = self.__lookup_table.get_candidates_in_current_page()
                if index >= len(candidates):
                    return False
                candidate = candidates[index].text
                self.__commit_string(candidate)
                return True
            elif keyval == keysyms.Page_Up or keyval == keysyms.KP_Page_Up:
                self.page_up()
                return True
            elif keyval == keysyms.Page_Down or keyval == keysyms.KP_Page_Down:
                self.page_down()
                return True
            elif keyval == keysyms.Up:
                self.cursor_up()
                return True
            elif keyval == keysyms.Down:
                self.cursor_down()
                return True
            elif keyval == keysyms.Left or keyval == keysyms.Right:
                return True
        if keyval in xrange(keysyms.a, keysyms.z + 1) or \
            keyval in xrange(keysyms.A, keysyms.Z + 1):
            if state & (modifier.CONTROL_MASK | modifier.ALT_MASK) == 0:
            	current_string = self.__preedit_string
            	if self.__input_method ==  "en_US":
            		self.__preedit_string += unichr(keyval)   
               	else:
            		if self.__keymap.get_candidates(current_string+unichr(keyval))== None:
            			current_list =  self.__keymap.get_candidates(current_string)
            			self.__commit_string(current_list[0])	
                		self.__preedit_string = unichr(keyval)
                		self.__update()
                	else:
                		self.__preedit_string += unichr(keyval)   
                self.__invalidate()
                return True
        else:
            if keyval < 128 and self.__preedit_string:
                self.__commit_string(self.__preedit_string)

        return False

    def __invalidate(self):
        if self.__is_invalidate:
            return
        self.__is_invalidate = True
        gobject.idle_add(self.__update, priority = gobject.PRIORITY_LOW)


    def page_up(self):
        if self.__lookup_table.page_up():
            self.page_up_lookup_table()
            return True
        return False

    def page_down(self):
        if self.__lookup_table.page_down():
            self.page_down_lookup_table()
            return True
        return False

    def cursor_up(self):
        if len(self.__lookup_table.get_candidates_in_current_page()) == 0:
            return False
        if self.__lookup_table.cursor_up():
            self.update_lookup_table(self.__lookup_table, True, True)
            curr_text=self.__lookup_table.get_current_candidate().text
            self.update_preedit(curr_text, None, len(curr_text), True)
        return True


    def cursor_down(self):
        if len(self.__lookup_table.get_candidates_in_current_page()) == 0:
            return False
        if self.__lookup_table.cursor_down():
            self.update_lookup_table(self.__lookup_table, True, True)
            curr_text=self.__lookup_table.get_current_candidate().text
            self.update_preedit(curr_text, None, len(curr_text), True)
        return True

    def __commit_string(self, text):
        self.commit_text(ibus.Text(text))
        self.__current_word =  self.__current_word  + text
        self.__preedit_string = u""
        self.__update()

    def __update(self):
        preedit_len = len(self.__preedit_string)
        attrs = ibus.AttrList()
        self.__lookup_table.clean()
        if self.__input_method ==  "en_US":
        	if preedit_len > 0  :
        		autocompletion_list = self.__get_autocompletion()
        		for text in autocompletion_list:
        			self.__lookup_table.append_candidate(ibus.Text(text))     
        else:
	        if preedit_len > 0:
    			attrs.append(ibus.AttributeForeground(0xff0000, 0, preedit_len))
        		candidate_list = self.__keymap.get_candidates(self.__preedit_string)
        		for text in candidate_list:
        			self.__lookup_table.append_candidate(ibus.Text(text))
        		
        self.update_auxiliary_text(ibus.Text(self.__preedit_string, attrs), preedit_len > 0)
        attrs.append(ibus.AttributeUnderline(pango.UNDERLINE_SINGLE, 0, preedit_len))
        self.update_preedit_text(ibus.Text(self.__preedit_string, attrs), preedit_len, preedit_len > 0)
        self.__update_lookup_table()
        self.__is_invalidate = False
    def __update_prediction(self, previous_word):
        #self.__lookup_table.clean()
        
        #if previous_word:
        #    self.__lookup_table.append_candidate(ibus.Text(previous_word+"Prediction1"))        
        #    self.__lookup_table.append_candidate(ibus.Text(previous_word+"Prediction2"))        
        #self.update_preedit_text(ibus.Text(self.__preedit_string, None), 0, False)
        #self.__update_lookup_table()
        #self.__is_invalidate = False
            
    def __get_autocompletion(self):
    	if self.__input_method ==  "en_US":
    		if(len(self.__preedit_string)<3):
    			return [self.__current_word]
    		autocompletion_candidates=self.__autocomplete.get_autocompletion_suggestions(self.__preedit_string)
    	else:	
    		if(len(self.__current_word)<3):
    			return [self.__current_word]
    		autocompletion_candidates=self.__autocomplete.get_autocompletion_suggestions(self.__current_word)
    	return autocompletion_candidates
    	
    def __update_lookup_table(self):
        visible = self.__lookup_table.get_number_of_candidates() > 0
        self.update_lookup_table(self.__lookup_table, visible)
 
    def update_preedit(self, preedit_string, preedit_attrs, cursor_pos, visible):
        if preedit_attrs == None:
            preedit_attrs = ibus.AttrList()
            attr = ibus.AttributeUnderline(ibus.ATTR_UNDERLINE_SINGLE, 0, len(preedit_string))
            preedit_attrs.append(attr)
        super(SulekhaEngine, self).update_preedit_text(ibus.Text(preedit_string, preedit_attrs), cursor_pos, visible)

    def focus_in(self):
        self.register_properties(self.__prop_list)

    def focus_out(self):
        pass

    def reset(self):
        pass

    def property_activate(self, prop_name):
        print "PropertyActivate(%s)" % prop_name

