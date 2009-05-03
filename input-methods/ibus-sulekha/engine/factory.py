# vim:set et sts=4 sw=4:
#
# ibus-tmpl - The Input Bus template project
#
# Copyright (c) 2007-2008 Huang Peng <shawn.p.huang@gmail.com>
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

import ibus
import os
import sulekha
from gettext import dgettext
_  = lambda a : dgettext("ibus-sulekha", a)
N_ = lambda a : a


class EngineFactory(ibus.EngineFactoryBase):
	FACTORY_PATH = "/org/smc/IBus/engines/Sulekha/Factory"
	ENGINE_PATH = "/org/smc/IBus/engines/Sulekha/Engine"
	NAME = _("Sulekha")
	LANG = "ml_IN"
	ICON = os.getenv("IBUS_SULEKHA_LOCATION") + "/icons/ibus-sulekha.svg"
	AUTHORS = "Santhosh Thottingal <santhosh.thottingal@gmail.com>"
	CREDITS = "GPLv2+"
	def __init__(self, bus):
		self.__bus = bus
		#pinyin.PinYinEngine.CONFIG_RELOADED(bus)
		super(EngineFactory, self).__init__(bus)

		self.__id = 0
		self.__config = self.__bus.get_config()

		self.__config.connect("reloaded", self.__config_reloaded_cb)
		self.__config.connect("value-changed", self.__config_value_changed_cb)
	def create_engine(self, engine_name):
		if engine_name == "sulekha":
			self.__id += 1
			return sulekha.SulekhaEngine(self.__bus, "%s/%d" % (self.ENGINE_PATH, self.__id))
		return super(EngineFactory, self).create_engine(engine_name)

	def __config_reloaded_cb(self, config):
		#pinyin.PinYinEngine.CONFIG_RELOADED(self.__bus)
		print "Configuration reloaded"

	def __config_value_changed_cb(self, config, section, name, value):
		#pinyin.PinYinEngine.CONFIG_VALUE_CHANGED(self.__bus, section, name, value)
		print "Configuration changed"

