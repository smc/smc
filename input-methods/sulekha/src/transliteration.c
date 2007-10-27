/* Transliteration.c
 *
 * Copyright (C) 2007-2008
 *  Santhosh Thottingal<santhosh00@gmail.com>,
 *  Swathanthra Malayalam Computing.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or (at
 * your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
 */

#include<stdio.h>
#include<string.h>

#include<stdlib.h>
#include "transliteration.h"
/*
Transliterate the a dhvani phonetic string to malayalam.
Algorithm:
1)For all vowels, if it is at the 0th position print as it is
2)If the vowel is in between/end of the string print the sign of the vowel except for A
3)For all consonants print the malayalam character
4)If a phonetic  character is not identified print '?'
5)Octal C escaped strings are used for printing the Unicode Malayalam string
*/

main1 (int argc, const char *argv[])
{
  const char *word;
  const char *transliterated_word;
  int word_length = 0;
  if (argc == 1)
    {
      printf ("Usage: %s word\n", argv[0]);
      exit (0);
    }
  word = argv[1];
  transliterated_word = transliterate_ml (word, 0, strlen (word));
// printf ("%s\n",word);
  printf ("%s\n", transliterated_word);
  return 0;
}

int
isVowel (char c)
{
  if ((c == 'a') || (c == 'A') || (c == 'e') || (c == 'E') || (c == 'i')
      || (c == 'I') || (c == 'o') || (c == 'O') || (c == 'u') || (c == 'U'))
    return 1;
  else
    return 0;
}

int
isChillu (char c)
{
  if ((c == 'n') || (c == 'N') || (c == 'r') || (c == 'R') || (c == 'l')
      || (c == 'L') || (c == 'm'))
    return 1;
  else
    return 0;
}


char *
transliterate_ml (char *phonetic_string, int start, int end)
{
  char *ml_string = NULL;
  int length = 0;
  int i = start;
  length = end - start;
  ml_string = (char *) malloc (length * 4 * sizeof (char));
  ml_string[0] = '\0';
  while (i < end)
    {

      switch (phonetic_string[i])
	{
	  //Vowels
	case 'a':
	  if (i == 0)		//first letter, use swaram as such
	    {			// as in amaram

	      if (i < end && phonetic_string[i + 1] == 'a')
		{		// as in aana
		  strcat (ml_string, "\340\264\206");	//aa letter
		  i++;
		}
	      else if (i < end && phonetic_string[i + 1] == 'i')
		{		// as in airaavatham
		  strcat (ml_string, "\340\264\202");	//ai letter
		  i++;
		}
	      else if (i < end && phonetic_string[i + 1] == 'u')
		{		// as in airaavatham
		  strcat (ml_string, "\340\264\224");	//au aushadham
		  i++;
		}
	      else
		{
		  strcat (ml_string, "\340\264\205");	//a letter
		}
	    }
	  else
	    {			//swara chihnam
	      if (i < end && phonetic_string[i + 1] == 'a')	//aa sign
		{		// as in kaazhcha
		  strcat (ml_string, "\340\264\276");
		  i++;
		}
	      else if (i < end && phonetic_string[i + 1] == 'i')
		{		// as in kaitha
		  strcat (ml_string, "\340\265\210");	//ai sign
		  i++;
		}
	      else if (i < end && phonetic_string[i + 1] == 'u')
		{		// as in kauravar
		  strcat (ml_string, "\340\265\227");	//au sign
		  i++;
		}
	    }
	  break;

	case 'A':
	  (i == 0) ? strcat (ml_string, "\340\264\206") : strcat (ml_string,
								  "\340\264\276");
	  break;
	case 'i':
	  if (i == 0)
	    {
	      if (i < end
		  && ((phonetic_string[i + 1] == 'i')
		      || (phonetic_string[i + 1] == 'e')))
		{		//ii/ee letter
		  strcat (ml_string, "\340\264\210");
		  i++;
		}
	      else
		{
		  strcat (ml_string, "\340\264\207");	// i/e letter 
		}
	    }
	  else
	    {
	      if (i < end && ((phonetic_string[i + 1] == 'i') || (phonetic_string[i + 1] == 'e')))	//ii/ee sign
		{
		  strcat (ml_string, "\340\265\200");
		  i++;
		}
	      else
		{
		  strcat (ml_string, "\340\264\277");	// i/e sign
		}
	    }
	  break;
	case 'I':
	  (i == 0) ? strcat (ml_string, "\340\264\210") : strcat (ml_string,
								  "\340\265\200");
	  break;
	case 'u':
	  if (i == 0)
	    {
	      if (i < end
		  && ((phonetic_string[i + 1] == 'o')
		      || (phonetic_string[i + 1] == 'u')))
		{		//ii/ee letter
		  strcat (ml_string, "\340\264\212");
		  i++;
		}
	      else
		{
		  strcat (ml_string, "\340\264\211");	// u letter 
		}
	    }
	  else
	    {
	      if (i < end && ((phonetic_string[i + 1] == 'u') || (phonetic_string[i + 1] == 'o')))	//ii/ee sign
		{
		  strcat (ml_string, "\340\265\202");	//uu sign 
		  i++;
		}
	      else
		{
		  strcat (ml_string, "\340\265\201");	// u sign
		}
	    }
	  break;
	case 'U':
	  (i == 0) ? strcat (ml_string, "\340\264\212") : strcat (ml_string,
								  "\340\265\202");
	  break;
	case '^':
	  (i == 0) ? strcat (ml_string, "\340\264\213") : strcat (ml_string,
								  "\340\265\203");
	  break;
	case 'e':
	  if (i == 0)
	    {
	      if (i < end
		  && ((phonetic_string[i + 1] == 'e')
		      || (phonetic_string[i + 1] == 'a')))
		{		//ii/ee letter
		  strcat (ml_string, "\340\264\217");
		  i++;
		}
	      else
		{
		  strcat (ml_string, "\340\264\207");	// e letter 
		}
	    }
	  else
	    {
	      if (i < end && ((phonetic_string[i + 1] == 'e')))	//e/ee sign
		{
		  strcat (ml_string, "\340\265\200");	//ee sign 
		  i++;
		}
	      else
		{
		  strcat (ml_string, "\340\265\206");	// u sign
		}
	    }
	  break;
	case 'E':
	  (i == 0) ? strcat (ml_string, "\340\264\217") : strcat (ml_string,
								  "\340\265\207");
	  break;
//      case '@':               //ai
//        (i == 0) ? strcat (ml_string, "\340\264\220") : strcat (ml_string,
//                                                                "\340\265\210");
//        break;
	case 'o':
	  if (i == 0)
	    {
	      if (i < end && ((phonetic_string[i + 1] == 'o')))
		{		//oo letter
		  strcat (ml_string, "\340\264\222");
		  i++;
		}
	      else
		{
		  strcat (ml_string, " \340\264\223");	// o letter 
		}
	    }
	  else
	    {
	      if (i < end && ((phonetic_string[i + 1] == 'o')))	//oo sign
		{
		  strcat (ml_string, "\340\265\202");	//oo sign 
		  i++;
		}
	      else if (i < end && ((phonetic_string[i + 1] == 'u')))	//ou sign
		{
		  strcat (ml_string, "\340\265\214");	//ou sign 
		  i++;
		}
	      else
		{
		  strcat (ml_string, "\340\265\212");	// o sign
		}
	    }
	  break;
	case 'O':
	  (i == 0) ? strcat (ml_string, "\340\264\223") : strcat (ml_string,
								  "\340\265\213");
	  break;
	case '`':
	  (i == 0) ? strcat (ml_string, "\340\264\224") : strcat (ml_string,
								  "\340\265\227");
	  break;
//      case '.':               //am
//        strcat (ml_string, "\340\264\202");
//        break;
	case '~':		//chandrakkala
	  strcat (ml_string, "\340\265\215");
	  break;
	case ':':		//Ah
	  strcat (ml_string, "\340\264\203");
	  break;
	  //Consonants
	case 'k':


	  if (i < end && (phonetic_string[i + 1] == phonetic_string[i]))
	    {			//koottaxaram - put a virama
	      strcat (ml_string, "\340\264\225");
	      strcat (ml_string, "\340\265\215");
	      strcat (ml_string, "\340\264\225");
	      i++;
	    }
	  else if (i < end && (phonetic_string[i + 1] == 'h'))
	    {			//kh
	      strcat (ml_string, "\340\264\226");
	      i++;
	    }
	  else
	    {
	      strcat (ml_string, "\340\264\225");	//just a k

	    }
	  break;
	case 'K':
	  if (i == start)
	    {			//start of a word- may be a Name.Place..starting with K
	      strcat (ml_string, "\340\264\225");	//just a k
	    }

	  else if (i < end && (phonetic_string[i + 1] == phonetic_string[i]))
	    {			//KK
	      strcat (ml_string, "\340\264\225");
	      strcat (ml_string, "\340\265\215");
	      strcat (ml_string, "\340\264\225");
	      i++;
	    }
	  else if (i < end && (phonetic_string[i + 1] == 'h'))
	    {			//Kh as in Khalid
	      strcat (ml_string, "\340\264\226");
	      i++;
	    }
	  else
	    {
	      strcat (ml_string, "\340\264\226");	//just a k

	    }

	  break;
	case 'g':
	  if (i < end && (phonetic_string[i + 1] == phonetic_string[i]))
	    {			//koottaxaram - put a virama
	      strcat (ml_string, "\340\264\227");
	      strcat (ml_string, "\340\265\215");
	      strcat (ml_string, "\340\264\227");
	      i++;
	    }
	  else if (i < end && (phonetic_string[i + 1] == 'h'))
	    {			//gh
	      strcat (ml_string, "\340\264\230");
	      i++;
	    }
	  else
	    {
	      strcat (ml_string, "\340\264\227");	//just a g as in gaanam

	    }
	  break;
	case 'G':

	  if (i == start)
	    {			//start of a word- may be a Name.Place..starting with G
	      strcat (ml_string, "\340\264\227");	//just a g
	    }

	  else if (i < end && (phonetic_string[i + 1] == 'h'))
	    {			//Kh as in Gha
	      strcat (ml_string, "\340\264\230");
	      i++;
	    }
	  else
	    {
	      strcat (ml_string, "\340\264\230");	//just a G

	    }
	  break;
	case 'c':


	  if (i < end && (phonetic_string[i + 1] == phonetic_string[i]))
	    {			//kk/cc
	      strcat (ml_string, "\340\264\225");
	      strcat (ml_string, "\340\265\215");
	      strcat (ml_string, "\340\264\225");
	      i++;
	    }
	  else if (i < end && (phonetic_string[i + 1] == 'h'))
	    {
	      if (i == start)
		{
		  //Ch as in chaaya
		  strcat (ml_string, "\340\264\232");
		  i++;

		}
	      else
		{
//most of the time the ch in side the manglish means chcha as an pacha *wild guess. leaving this to aspell :)
//let he decides
		  strcat (ml_string, "\340\264\232");
		  strcat (ml_string, "\340\265\215");
		  strcat (ml_string, "\340\264\232");
		  i++;
		}
	    }
	  else if (i == start && (phonetic_string[i + 1] != 'h'))
	    {			//start of a word- may be a Name. as in cibu
	      strcat (ml_string, "\340\264\270");	//just a c/k
	    }
	  else
	    {
	      strcat (ml_string, "\340\264\226");	//just a k/c

	    }

	  break;
	case 'C':


	  if (i < end && (phonetic_string[i + 1] == phonetic_string[i]))
	    {			//kk/CC
	      strcat (ml_string, "\340\264\225");
	      strcat (ml_string, "\340\265\215");
	      strcat (ml_string, "\340\264\225");
	      i++;
	    }
	  else if (i < end
		   && ((phonetic_string[i + 1] == 'h')
		       || (phonetic_string[i + 1] == 'H')))
	    {
	      if (i == start)
		{
		  //Ch as in chaaya
		  strcat (ml_string, "\340\264\232");
		  i++;

		}
	      else
		{
//most of the time the ch in side the manglish means chcha as an pacha *wild guess. leaving this to aspell :)
//let he decides
		  strcat (ml_string, "\340\264\232");
		  strcat (ml_string, "\340\265\215");
		  strcat (ml_string, "\340\264\232");
		  i++;
		}
	    }
	  else if (i == start && (phonetic_string[i + 1] != 'h'))
	    {			//start of a word- may be a Name. as in cibu
	      strcat (ml_string, "\340\264\270");	//just a c/k
	    }
	  else
	    {
	      strcat (ml_string, "\340\264\226");	//just a k/c

	    }

	  break;
	case 'j':
	  if (i < end && (phonetic_string[i + 1] == phonetic_string[i]))
	    {			//koottaxaram - put a virama //jja
	      strcat (ml_string, "\340\264\234");	//ja
	      strcat (ml_string, "\340\265\215");
	      strcat (ml_string, "\340\264\234");	//ja
	      i++;
	    }
	  else if (i < end && (phonetic_string[i + 1] == 'h'))
	    {			//jh
	      strcat (ml_string, "\340\264\235");
	      i++;
	    }
	  else
	    {
	      strcat (ml_string, "\340\264\234");	//just a j as in janam

	    }
	  break;
	case 'J':
	  if (i < end && (phonetic_string[i + 1] == phonetic_string[i]))
	    {			//koottaxaram - put a virama //jja
	      strcat (ml_string, "\340\264\234");	//ja
	      strcat (ml_string, "\340\265\215");
	      strcat (ml_string, "\340\264\234");	//ja
	      i++;
	    }
	  else if (i < end && (phonetic_string[i + 1] == 'h'))
	    {			//jh
	      strcat (ml_string, "\340\264\235");
	      i++;
	    }
	  else
	    {
	      strcat (ml_string, "\340\264\234");	//just a j as in janam
	    }
	  break;
	case 't':
	  if (i < end && (phonetic_string[i + 1] == phonetic_string[i]))
	    {			//koottaxaram - put a virama //tta
	      strcat (ml_string, "\340\264\237");	//ja
	      strcat (ml_string, "\340\265\215");
	      strcat (ml_string, "\340\264\237");	//ja
	      i++;
	    }
	  else if (i < end
		   && ((phonetic_string[i + 1] == 'h')
		       || (phonetic_string[i + 1] == 'H')))
	    {			//th
	      strcat (ml_string, "\340\264\244");
	      i++;
	    }
	  else
	    {
	      //usually the words starting with t is very less. A t in the starting is tha most probably.
	      if (i == start)
		{
		  strcat (ml_string, "\340\264\244");	//tha
		}
	      else
		{
		  strcat (ml_string, "\340\264\237");	//just a t  
		}
	    }
	  break;
	case 'T':
	  if (i < end && (phonetic_string[i + 1] == phonetic_string[i]))
	    {			//koottaxaram - put a virama //tta
	      strcat (ml_string, "\340\264\237");	//ja
	      strcat (ml_string, "\340\265\215");
	      strcat (ml_string, "\340\264\237");	//ja
	      i++;
	    }
	  else if (i < end
		   && ((phonetic_string[i + 1] == 'h')
		       || (phonetic_string[i + 1] == 'H')))
	    {			//th
	      strcat (ml_string, "\340\264\244");
	      i++;
	    }
	  else
	    {
	      //usually the words starting with t is very less. A t in the starting is tha most probably.
	      if (i == start)
		{
		  strcat (ml_string, "\340\264\244");	//tha
		}
	      else
		{
		  strcat (ml_string, "\340\264\237");	//just a t  
		}
	    }
	  break;
	case 'd':
	  if (i < end && (phonetic_string[i + 1] == phonetic_string[i]))
	    {			//koottaxaram - put a virama //dda
	      strcat (ml_string, "\340\264\246");	//da
	      strcat (ml_string, "\340\265\215");
	      strcat (ml_string, "\340\264\246");	//da
	      i++;
	    }
	  else if (i < end
		   && ((phonetic_string[i + 1] == 'h')
		       || (phonetic_string[i + 1] == 'H')))
	    {			//th
	      strcat (ml_string, "\340\264\247");
	      i++;
	    }
	  else
	    {
	      strcat (ml_string, "\340\264\246");	//da
	    }
	  break;
	case 'D':
	  if (i < end && (phonetic_string[i + 1] == phonetic_string[i]))
	    {			//koottaxaram - put a virama //dda
	      strcat (ml_string, "\340\264\246");	//Da
	      strcat (ml_string, "\340\265\215");
	      strcat (ml_string, "\340\264\246");	//Da
	      i++;

	    }
	  else if (i < end
		   && ((phonetic_string[i + 1] == 'h')
		       || (phonetic_string[i + 1] == 'H')))
	    {			//Dh as in viDhi 
	      strcat (ml_string, "\340\264\242");
	      i++;
	    }
	  else
	    {
	      if (i == start)
		{
		  strcat (ml_string, "\340\264\246");	//Da
		}
	      else
		{
		  strcat (ml_string, "\340\264\241");	//Da
		}
	    }
	  break;
	case 'N':

	  if (i < end && (phonetic_string[i + 1] == phonetic_string[i]))
	    {			//koottaxaram - put a virama
	      strcat (ml_string, "\340\264\243");
	      strcat (ml_string, "\340\265\215");
	      strcat (ml_string, "\340\264\243");
	      i++;
	    }
	  else if (i == start)
	    {
	      strcat (ml_string, "\340\264\250");
	    }
	  else
	    {

	      if (isVowel (phonetic_string[i + 1]))
		{
		  strcat (ml_string, "\340\264\243");
		}
	      else if ((i < end))
		{
		  //chillu N
		  strcat (ml_string, "\340\264\243");
		  strcat (ml_string, "\340\265\215");	//virama
		  strcat (ml_string, "\342\200\215");	//zwj
		}
	    }
	  //words ending with N chillu is  less 
	  break;

	case 'n':

	  if (i < end && (phonetic_string[i + 1] == phonetic_string[i]))
	    {			//koottaxaram - put a virama
	      strcat (ml_string, "\340\264\250");
	      strcat (ml_string, "\340\265\215");
	      strcat (ml_string, "\340\264\250");
	      i++;
	    }
	  else if (i < end && (phonetic_string[i + 1] == 'j'))
	    {			//nja as in njaan
	      strcat (ml_string, "\340\264\236");
	      i++;
	    }
	  else if (i < end && (phonetic_string[i + 1] == 't'))
	    {
	      if (i + 1 < end && (phonetic_string[i + 2] == 'h'))
		{
//nthaa as in enthaa
		  strcat (ml_string, "\340\264\250");
		  strcat (ml_string, "\340\265\215");
		  strcat (ml_string, "\340\264\244");
		  i++;
		  i++;
		}
	      else
		{
		  //nta as in ente
		  strcat (ml_string, "\340\264\250");
		  strcat (ml_string, "\340\265\215");
		  strcat (ml_string, "\340\264\261");
		  i++;
		}
	    }
	  else if (i < end && (phonetic_string[i + 1] == 'g'))
	    {			//nga as in thenga
	      strcat (ml_string, "\340\264\231");
	      strcat (ml_string, "\340\265\215");
	      strcat (ml_string, "\340\264\231");
	      i++;
	    }
	  else if (i < end && (phonetic_string[i + 1] == 'k'))
	    {			//nka as in thankakkutam
	      strcat (ml_string, "\340\264\231");
	      strcat (ml_string, "\340\265\215");
	      strcat (ml_string, "\340\264\225");
	      i++;
	    }
	  else if (i == start)
	    {
	      strcat (ml_string, "\340\264\250");
	    }
	  else
	    {

	      if (isVowel (phonetic_string[i + 1]))
		{
		  strcat (ml_string, "\340\264\250");
		}
	      else if ((i < end))
		{

		  //chillu n
		  strcat (ml_string, "\340\264\250");
		  strcat (ml_string, "\340\265\215");	//virama
		  strcat (ml_string, "\342\200\215");	//zwj
		}
	    }
	  //words ending with N chillu is  less 
	  break;
	case 'p':

	  if (i < end && (phonetic_string[i + 1] == phonetic_string[i]))
	    {			//koottaxaram - put a virama
	      strcat (ml_string, "\340\264\252");
	      strcat (ml_string, "\340\265\215");
	      strcat (ml_string, "\340\264\252");
	      i++;
	    }
	  else if (i < end && (phonetic_string[i + 1] == 'h'))
	    {			//ph
	      strcat (ml_string, "\340\264\253");
	      i++;
	    }
	  else
	    {
	      strcat (ml_string, "\340\264\252");	//just a p

	    }
	  break;
	case 'f':
	  if (i < end && (phonetic_string[i + 1] == phonetic_string[i]))
	    {			//koottaxaram - put a virama
	      strcat (ml_string, "\340\264\253");
	      strcat (ml_string, "\340\265\215");
	      strcat (ml_string, "\340\264\253");
	      i++;
	    }
	  else
	    {
	      strcat (ml_string, "\340\264\253");	//just a f

	    }
	  break;
	case 'b':

	  if (i < end && (phonetic_string[i + 1] == phonetic_string[i]))
	    {			//koottaxaram - put a virama
	      strcat (ml_string, "\340\264\254");
	      strcat (ml_string, "\340\265\215");
	      strcat (ml_string, "\340\264\254");
	      i++;
	    }
	  else if (i < end && (phonetic_string[i + 1] == 'h'))
	    {			//ph
	      strcat (ml_string, "\340\264\255");
	      i++;
	    }
	  else
	    {
	      strcat (ml_string, "\340\264\254");	//just a b

	    }
	  break;
	case 'B':
	  if (i < end && (phonetic_string[i + 1] == phonetic_string[i]))
	    {			//koottaxaram - put a virama
	      strcat (ml_string, "\340\264\255");
	      strcat (ml_string, "\340\265\215");
	      strcat (ml_string, "\340\264\255");
	      i++;
	    }
	  else
	    {
	      strcat (ml_string, "\340\264\255");	//just a B

	    }
	  break;
	case 'm':
	  if (i == end - 1 && phonetic_string[i] != phonetic_string[i - 1])	//end of word. most probably it is an anuswaram
	    {
	      strcat (ml_string, "\340\264\202");

	    }
	  else if (i < end && (phonetic_string[i + 1] == phonetic_string[i]))
	    {			//koottaxaram - put a virama
	      strcat (ml_string, "\340\264\256");
	      strcat (ml_string, "\340\265\215");
	      strcat (ml_string, "\340\264\256");
	      i++;
	    }
	  else
	    {
	      if (i + 1 < end && !isVowel (phonetic_string[i + 1]))
		{
		  strcat (ml_string, "\340\264\256");
		  strcat (ml_string, "\340\265\215");
		}
	      else
		strcat (ml_string, "\340\264\256");
	    }

	  break;
	case 'y':
	  if (i < end && (phonetic_string[i + 1] == phonetic_string[i]))
	    {			//koottaxaram - put a virama
	      strcat (ml_string, "\340\264\257");
	      strcat (ml_string, "\340\265\215");
	      strcat (ml_string, "\340\264\257");
	      i++;
	    }
	  else
	    {
	      strcat (ml_string, "\340\264\257");	//just a y

	    }
	  break;
	case 'r':
	  if ((i + 1 < end)
	      && ((phonetic_string[i + 1] == 'a')
		  || (phonetic_string[i + 1] == 'A')
		  || (phonetic_string[i + 1] == 'e')
		  || (phonetic_string[i + 1] == 'E')
		  || (phonetic_string[i + 1] == 'i')
		  || (phonetic_string[i + 1] == 'I')
		  || (phonetic_string[i + 1] == 'o')
		  || (phonetic_string[i + 1] == 'O')))
	    {
	      strcat (ml_string, "\340\264\260");	//just r
	    }
	  else if ((i < end))
	    {

	      //chillu r
	      strcat (ml_string, "\340\264\260");
	      strcat (ml_string, "\340\265\215");	//virama
	      strcat (ml_string, "\342\200\215");	//zwj
	    }

	  break;
	case 'l':
	  if ((i + 1 < end) && (isVowel (phonetic_string[i + 1])))
	    {
	      strcat (ml_string, "\340\264\262");	//just l
	    }
	  else if ((i < end))
	    {

	      //chillu l
	      strcat (ml_string, "\340\264\262");
	      strcat (ml_string, "\340\265\215");	//virama
	      strcat (ml_string, "\342\200\215");	//zwj
	    }

	  break;
	case 'v':
	  strcat (ml_string, "\340\264\265");
	  break;
	case 's':

	  if (i + 1 < end && phonetic_string[i + 1] == 'h')
	    {
	      strcat (ml_string, "\340\264\267");	//sha
	      i++;
	    }
	  else
	    {
	      strcat (ml_string, "\340\264\270");	//sa as in santhosh
	    }
	  break;
	case 'S':
	  strcat (ml_string, "\340\264\267");	//sha
	  break;
	case 'h':
	  strcat (ml_string, "\340\264\271");
	  break;
	case 'L':
	  strcat (ml_string, "\340\264\263");
	  break;
	case 'z':
	  if (i + 1 < end && phonetic_string[i + 1] == 'h')
	    {
	      strcat (ml_string, "\340\264\264");	//zha
	      i++;
	    }
	  else
	    {
	      strcat (ml_string, "\340\264\270");	//zoo
	    }
	  break;
	case 'R':
	  strcat (ml_string, "\340\264\261");
	  break;
	default:
	  strcat (ml_string, phonetic_string[i]);	//Not recognized
	  break;
	}

      if ((i + 1 < end) && !isVowel (phonetic_string[i])
	  && !isVowel (phonetic_string[i + 1])
	  && !isChillu (phonetic_string[i]))
	{
	  strcat (ml_string, "\340\265\215");	//virama - implicit virama for conjuct formation
	}
      else
	if ((i + 1 == end) && !isVowel (phonetic_string[i])
	    && !isChillu (phonetic_string[i]))
	{
	  strcat (ml_string, "\340\265\215");	//virama - implicit virama for conjuct formation

	}
      i++;


    }

  printf ("%s\n", ml_string);
  return ml_string;
}
