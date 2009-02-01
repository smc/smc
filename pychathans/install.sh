#!/bin/bash
#
# Copyright (c) 2009 Rajeesh K Nambiar <rajeeshknambiar@gmail.com>
# This program is a free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#       
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

if [ $UID -ne 0 ]; then
	echo "You need to be root to install Chathans"
	exit 1
fi

install -m 0755 chathans.py /usr/bin/chathans
install -m 0644 chathans.desktop /usr/share/applications/chathans.desktop
for lc in po/chathans-*.po; do
	mo_file=po/`basename ${lc} .po`.mo
        msgfmt -o ${mo_file} ${lc}
	_lang=`echo ${lc} | cut -d - -f2 | cut -d . -f1`
       	mkdir -p /usr/share/locale/${_lang}/LC_MESSAGES/
	install -m 0644 ${mo_file} /usr/share/locale/${_lang}/LC_MESSAGES/chathans.mo
done
echo "Installation complete"
exit 0
