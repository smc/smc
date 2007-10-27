#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "aspell.h"
AspellConfig *spell_config = NULL;
AspellSpeller *spell_checker = 0;
/*int
main(int argc, const char *argv[])*/
int
check_word (char *lang, char *word)
{
  int correct = 0;

  int word_length = 0;

  if (lang == NULL)
    {
      lang = "ml";
    }

  word_length = strlen (word);
  spell_config = new_aspell_config ();
  aspell_config_replace (spell_config, "lang", lang);
  aspell_config_replace (spell_config, "encoding", "utf-8");
  AspellCanHaveError *possible_err = new_aspell_speller (spell_config);

  if (aspell_error_number (possible_err) != 0)
    puts (aspell_error_message (possible_err));
  else
    spell_checker = to_aspell_speller (possible_err);
  correct = aspell_speller_check (spell_checker, word, word_length);

  if (correct == 0)
    {
      printf ("word \"%s\" is wrong.\n", word);

    }
  else
    {
      printf ("word \"%s\" is correct.\n", word);
      exit (0);
    }


  return correct;
}

void
get_suggestion_list (char *word)
{

  const char *sugg_word;
  int suggestion_count = 0;
  int word_length = 0;
  AspellWordList *suggestions = NULL;
  suggestions = aspell_speller_suggest (spell_checker, word, word_length);
  AspellStringEnumeration *aspell_elements =
    aspell_word_list_elements (suggestions);

  while ((sugg_word =
	  aspell_string_enumeration_next (aspell_elements)) != NULL)
    {
      printf ("%d. %s\n", ++suggestion_count, sugg_word);
    }
  delete_aspell_string_enumeration (aspell_elements);




}
