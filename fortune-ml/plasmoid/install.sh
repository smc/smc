#!/bin/bash
rm ../FortuneCookie.zip
zip -r ../FortuneCookie.zip .
plasmapkg -r fortunecookie
plasmapkg -i ../FortuneCookie.zip

#--- Uncomment the following lines to see the plasmoid in a test cotainer.
#echo "invoking Plasmoid Viewer..."
#plasmoidviewer fortunecookie
