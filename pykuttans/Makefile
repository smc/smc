# Copyright (c) 2009 Rajeesh <rajeeshknambiar@gmail.com>
# Use this Makefile to update source files (ui and qrc)

all: src/kuttans_ui.py src/kuttans_rc.py src/kuttans.py src/kuttans
	python src/kuttans

src/kuttans_ui.py: ui/kuttans.ui
	pyuic4 $< > $@
src/kuttans_rc.py: qrc/kuttans.qrc
	pyrcc4 $< > $@
