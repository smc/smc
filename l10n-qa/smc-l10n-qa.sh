
### Main script stars here ###
# Store file name
FILE=""
ERRORPATTERNS=""
# Make sure we get file name as command line argument
# Else read it from standard input device
if [ "$2" == "" ]; then
   FILE="/dev/stdin"
else
   FILE="$2"
   # make sure file exist and readable
   if [ ! -f $FILE ]; then
  	echo "$FILE : does not exists"
  	exit 1
   elif [ ! -r $FILE ]; then
  	echo "$FILE: can not read"
  	exit 2
   fi
fi
# Make sure we get file name as command line argument
# Else read it from standard input device

if [ "$1" == "" ]; then
   	echo "Usage: smc-l10n-qa.sh errorpattern-file pofile"
  	exit 1
else
   ERRORPATTERNS="$1"
   # make sure file exist and readable
   if [ ! -f $ERRORPATTERNS ]; then
  	echo "$ERRORPATTERNS : does not exists"
  	exit 1
   elif [ ! -r $ERRORPATTERNS ]; then
  	echo "$ERRORPATTERNS: can not read"
  	exit 2
   fi
fi
 
while read line
do
	 grep --color -nTwrC3 "$line" $FILE # 2> /dev/null 
done <$ERRORPATTERNS 
echo "Done"
echo "Now trying to compile...." 
msgfmt -c --statistics $FILE
echo "Done"

