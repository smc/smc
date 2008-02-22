#!/bin/sh
date +%p > tempfile && dhvani tempfile
date +%l > tempfile && dhvani -l m tempfile
echo മണി > tempfile && dhvani tempfile
date +%M > tempfile && dhvani -l m tempfile
echo മിനിട്ട് > tempfile && dhvani tempfile
