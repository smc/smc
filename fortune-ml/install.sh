#!/bin/bash
# author: Santhosh Thottingal <santhosh.thottingal@gmail.com>
echo "Compiling...."
strfile fortune-ml fortune-ml.dat
echo "Installing..."
cp fortune-ml.dat /usr/share/games/fortune/
cp fortune-ml /usr/share/games/fortune/
echo "Done...!"
