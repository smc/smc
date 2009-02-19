#!/bin/bash
# author: Santhosh Thottingal <santhosh.thottingal@gmail.com>
echo "Compiling...."
strfile fortune-ml fortune-ml.dat
echo "Installing..."
cp fortune-ml.dat /usr/share/games/fortunes/
cp fortune-ml /usr/share/games/fortunes/
echo "Done...!"
