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
#include "Transliteration.h"
/*
Transliterate the a dhvani phonetic string to malayalam.
Algorithm:
1)For all vowels, if it is at the 0th position print as it is
2)If the vowel is in between/end of the string print the sign of the vowel except for A
3)For all consonants print the malayalam character
4)If a phonetic  character is not identified print '?'
5)Octal C escaped strings are used for printing the Unicode Malayalam string
*/


char *
transliterate_ml (char *phonetic_string, int start, int end)
{
  char *ml_string;
  int length = 0;
  int i = start;
  length = end - start;
  ml_string = (char *) malloc (length * 4 * sizeof (char));
  while (i < end)
    {

      switch (phonetic_string[i])
 {
   //Vowels
 case 'a':
   if (i == 0)  //first letter, use swaram as such
     {   // as in amaram

       if (i < end && phonetic_string[i + 1] == 'a')
  {  // as in aana
    strcat (ml_string, "\340\264\206"); //aa letter
    i++;
  }
       else if (i < end && phonetic_string[i + 1] == 'i')
  {  // as in airaavatham
    strcat (ml_string, "\340\264\202"); //ai letter
    i++;
  }
       else if (i < end && phonetic_string[i + 1] == 'u')
  {  // as in airaavatham
    strcat (ml_string, "\340\264\224"); //au aushadham
    i++;
  }
       else
  {
    strcat (ml_string, "\340\264\205"); //a letter
  }
     }
   else
     {   //swara chihnam
       if (i < end && phonetic_string[i + 1] == 'a') //aa sign
  {  // as in kaazhcha
    strcat (ml_string, "\340\264\276");
    i++;
  }
       else if (i < end && phonetic_string[i + 1] == 'i')
  {  // as in kaitha
    strcat (ml_string, "\340\265\210"); //ai sign
    i++;
  }
       else if (i < end && phonetic_string[i + 1] == 'u')
  {  // as in kauravar
    strcat (ml_string, "\340\265\227"); //au sign
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
  {  //ii/ee letter
    strcat (ml_string, "\340\264\210");
    i++;
  }
       else
  {
    strcat (ml_string, "\340\264\207"); // i/e letter 
  }
     }
   else
     {
       if (i < end && ((phonetic_string[i + 1] == 'i') || (phonetic_string[i + 1] == 'e'))) //ii/ee sign
  {
    strcat (ml_string, "\340\265\200");
    i++;
  }
       else
  {
    strcat (ml_string, "\340\264\277"); // i/e sign
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
  {  //ii/ee letter
    strcat (ml_string, "\340\264\212"); 
    i++;
  }
       else
  {
    strcat (ml_string, "\340\264\211"); // u letter 
  }
     }
   else
     {
       if (i < end && ((phonetic_string[i + 1] == 'u') || (phonetic_string[i + 1] == 'o'))) //ii/ee sign
  {
    strcat (ml_string, "\340\265\202"); //uu sign 
    i++;
  }
       else
  {
    strcat (ml_string, "\340\265\201"); // u sign
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
  {  //ii/ee letter
    strcat (ml_string, "\340\264\217"); 
    i++;
  }
       else
  {
    strcat (ml_string, "\340\264\207"); // e letter 
  }
     }
   else
     {
       if (i < end && ((phonetic_string[i + 1] == 'e') )) //e/ee sign
  {
    strcat (ml_string, "\340\265\200"); //ee sign 
    i++;
  }
       else
  {
    strcat (ml_string, "\340\265\206"); // u sign
  }
     }
   break;
 case 'E':
   (i == 0) ? strcat (ml_string, "\340\264\217") : strcat (ml_string,
          "\340\265\207");
   break;
//  case '@':  //ai
//    (i == 0) ? strcat (ml_string, "\340\264\220") : strcat (ml_string,
//           "\340\265\210");
//    break;
 case 'o':
   if (i == 0)
     {
       if (i < end
    && ((phonetic_string[i + 1] == 'o')))
  {  //oo letter
    strcat (ml_string, "\340\264\222"); 
    i++;
  }
       else
  {
    strcat (ml_string, " \340\264\223"); // o letter 
  }
     }
   else
     {
       if (i < end && ((phonetic_string[i + 1] == 'o') )) //oo sign
  {
    strcat (ml_string, "\340\265\213"); //oo sign 
    i++;
  }
       else
  {
    strcat (ml_string, "\340\265\212"); // o sign
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
 case '.':  //am
   strcat (ml_string, "\340\264\202");
   break;
 case '~':  //chandrakkala
   strcat (ml_string, "\340\265\215");
   break;
 case ':':  //Ah
   strcat (ml_string, "\340\264\203");
   break;
   //Consonants
 case 'k':
   strcat (ml_string, "\340\264\225");
  
  if (i < end &&  (phonetic_string[i + 1] == phonetic_string[i]))
     {   //koottaxaram - put a virama
        strcat (ml_string, "\340\265\215");
     }
   break;
 case 'K':
   strcat (ml_string, "\340\264\226");
   break;
 case 'g':
   strcat (ml_string, "\340\264\227");
   break;
 case '-':
   strcat (ml_string, "\340\264\231");
   break;
 case 'G':
   strcat (ml_string, "\340\264\230");
   break;
 case 'c':
   strcat (ml_string, "\340\264\232");
   break;
 case 'C':
   strcat (ml_string, "\340\264\233");
   break;
 case 'j':
   strcat (ml_string, "\340\264\234");
   break;
 case 'J':
   strcat (ml_string, "\340\264\235");
   break;
 case '#':
   strcat (ml_string, "\340\264\236");
   break;
 case 't':
   strcat (ml_string, "\340\264\237");
   break;
 case 'T':
   strcat (ml_string, "\340\264\240");
   break;
 case 'd':
   strcat (ml_string, "\340\264\241");
   break;
 case 'D':
   strcat (ml_string, "\340\264\242");
   break;
 case 'N':
   strcat (ml_string, "\340\264\243");
   break;
 case 'x':
   strcat (ml_string, "\340\264\244");
   break;
 case 'X':
   strcat (ml_string, "\340\264\245");
   break;
 case 'w':
   strcat (ml_string, "\340\264\246");
   break;
 case 'W':
   strcat (ml_string, "\340\264\247");
   break;
 case 'n':
   strcat (ml_string, "\340\264\250");
   break;
 case 'p':
   strcat (ml_string, "\340\264\252");
   break;
 case 'f':
   strcat (ml_string, "\340\264\253");
   break;
 case 'b':
   strcat (ml_string, "\340\264\254");
   break;
 case 'B':
   strcat (ml_string, "\340\264\255");
   break;
 case 'm':
   if (i == end - 1 && phonetic_string[i] != phonetic_string[i-1] ) //end of word. most probably it is an anuswaram
     {
       strcat (ml_string, "\340\264\202");

     }
   else
     {
       strcat (ml_string, "\340\264\256");
     }
  
   if (i < end &&  (phonetic_string[i + 1] == phonetic_string[i]))
     {   //koottaxaram - put a virama
       strcat (ml_string, "\340\265\215");
     }
   break;
 case 'y':
   strcat (ml_string, "\340\264\257");
   break;
 case 'r':
   strcat (ml_string, "\340\264\260");
   break;
 case 'l':
   strcat (ml_string, "\340\264\262");
   break;
 case 'v':
   strcat (ml_string, "\340\264\265");
   break;
 case '$':
   strcat (ml_string, "\340\264\266");
   break;
 case 's':
   strcat (ml_string, "\340\264\270");
   break;
 case 'S':
   strcat (ml_string, "\340\264\267");
   break;
 case 'h':
   strcat (ml_string, "\340\264\271");
   break;
 case 'L':
   strcat (ml_string, "\340\264\263");
   break;
 case 'z':
   strcat (ml_string, "\340\264\264");
   break;
 case 'R':
   strcat (ml_string, "\340\264\261");
   break;
 default:
   strcat (ml_string, "?"); //Not recognized
   break;
 }

      i++;
    }
//printf(":%s:\n",ml_string);
  return ml_string;
}
