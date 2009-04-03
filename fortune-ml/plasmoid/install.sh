#!/bin/bash
rm ../FortuneCookie.zip
zip -r ../FortuneCookie.zip .
plasmapkg -r fortunecookie
plasmapkg -i ../FortuneCookie.zip
echo "invoking Plasmoid Viewer..."
plasmoidviewer fortunecookie
