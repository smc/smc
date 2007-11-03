#!/bin/bash
echo "Installing Lalitha-in..."
mkdir -p /usr/share/doc/Lalitha-ml
cp /usr/share/X11/xkb/symbols/in /usr/share/doc/Lalitha-ml/in.orig
cp /usr/share/X11/xkb/rules/base.lst /usr/share/doc/Lalitha-ml/base.lst.orig
cp /usr/share/X11/xkb/rules/base.xml /usr/share/doc/Lalitha-ml/base.xml.orig
cp /usr/share/X11/xkb/rules/base /usr/share/doc/Lalitha-ml/base.orig
cp doc/* /usr/share/doc/Lalitha-ml/
cp in /usr/share/X11/xkb/symbols/
cp base base.xml base.lst /usr/share/X11/xkb/rules/
sleep 1
echo "Done"
