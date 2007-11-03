#!/bin/bash
echo "Installing ml-typewriter..."
mkdir -p /usr/share/doc/typewriter-ml
cp doc/* /usr/share/doc/typewriter-ml/
cp ml-typewriter.mim /usr/share/m17n/
sleep 1
echo "Done"
