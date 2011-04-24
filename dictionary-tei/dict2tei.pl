#!/usr/bin/perl
#
print " $ARGV[0], $ARGV[1] \n";
open(IP,"$ARGV[0]")||die ("could not open file $ARGV[0]\n");
open(OP,">$ARGV[1]");

@ipdata=<IP>;
close IP;
#print @ipdata;

$i=0;
$k=0;
print OP "<TEI>\n\t<text>\n\t\t<body>\n";
foreach(@ipdata)
{
	$i=$i+1;
	if(/^\s*\d|^\W/)
	{
	}
	else{
	if (/(.*)\n/)
	{
		$k=$k+1;
		
		print OP "<entry>\n<form><orth>$1<\/orth><\/form>";
		$j=$i;
		$m=0;
		$m=1;
		while($ipdata[$j] =~ m/^\s*\d\.\s*(.*)\s*\n|^\W/)
		{
			print OP "<sense n=\"$m\"><cit type=\"trans\"><quote>$1<\/quote><\/cit><\/sense>";
			$j=$j+1;
			$m=$m+1;
		}
		print OP "\n<\/entry>\n";
	}
	}
}

print OP "\t\t<\/body>\n\t<\/text>\n<\/TEI>";

