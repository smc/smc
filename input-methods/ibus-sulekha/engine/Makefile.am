# vim:set noet ts=4:
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

engine_sulekha_PYTHON = \
	factory.py \
	main.py \
	sulekha.py \
	keymap.py \
	autocomplete.py \
	sulekha.db \
	$(NULL)
engine_sulekha_DATA = \
	$(NULL)
engine_sulekhadir = $(datadir)/ibus-sulekha/engine

libexec_SCRIPTS = ibus-engine-sulekha

engine_DATA = sulekha.xml
enginedir = $(datadir)/ibus/component

EXTRA_DIST = \
	ibus-engine-sulekha.in \
	sulekha.xml.in \
	$(NULL)

CLEANFILES = \
	sulekha.xml \
	*.pyc \
	$(NULL)

sulekha.xml: sulekha.xml.in
	( \
		libexecdir=${libexecdir}; \
		pkgdatadir=${pkgdatadir}; \
		s=`cat $<`; \
		eval "echo \"$${s}\""; \
	) > $@

test:
	$(ENV) \
		IBUS_SULEKHA_LOCATION=$(abs_top_srcdir) \
		DBUS_DEBUG=true \
		LANG=en_US \
		PYTHONPATH=$(abs_top_srcdir):$(pyexecdir) \
		$(PYTHON) $(srcdir)/main.py

