/* transliteration.h
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
 /*-----------------------    FUNCTIONS     ----------------------------*/
/*
Transliterate the a dhvani phonetic string to malayalam.
Algorithm:
1)For all vowels, if it is at the 0th position print as it is
2)If the vowel is in between/end of the string print the sign of the vowel except for A
3)For all consonants print the malayalam character
4)If a phonetic  character is not identified print '?'
5)Octal C escaped strings are used for printing the Unicode Malayalam string
*/
char *transliterate_ml (char *, int, int);
