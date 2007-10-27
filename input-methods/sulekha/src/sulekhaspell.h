/* sulekhaspell - a spell-checking addon for GTK's TextView widget based on sulekhaspell by Evan Martin.
 *
 * Copyright (C) 2007-2008
 *  Santhosh Thottingal<santhosh00@gmail.com>,
 *  Praveen Arimprathodiyil <pravi.a@gmail.com>
 *  Swathanthra Malayalam Computing.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or (at
 * your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 *
  * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
*/


#ifndef SULEKHASPELL_H
#define SULEKHASPELL_H

#define SULEKHASPELL_ERROR sulekhaspell_error_quark()

typedef enum {
	SULEKHASPELL_ERROR_BACKEND,
} SulekhaSpellError;

GQuark sulekhaspell_error_quark();

typedef struct _SulekhaSpell SulekhaSpell;

/* the idea is to have a SulekhaSpell object that is analagous to the
 * GtkTextBuffer-- it lives as an attribute of the GtkTextView but
 * it can be referred to directly. */

SulekhaSpell* sulekhaspell_new_attach(GtkTextView *view,
                                     const gchar *lang, GError **error);
SulekhaSpell* sulekhaspell_get_from_text_view(GtkTextView *view);
void      sulekhaspell_detach(SulekhaSpell *spell);

gboolean  sulekhaspell_set_language(SulekhaSpell *spell,
                                       const gchar *lang, GError **error);

void      sulekhaspell_recheck_all(SulekhaSpell *spell);


/*** old API-- deprecated. ***/
#ifndef SULEKHASPELL_DISABLE_DEPRECATED
#define SULEKHASPELL_ERROR_PSPELL SULEKHASPELL_ERROR_BACKEND

int sulekhaspell_init();
/* no-op. */

void sulekhaspell_attach(GtkTextView *view);
/* sulekhaspell_new_attach(view, NULL, NULL); */

#endif /* SULEKHASPELL_DISABLE_DEPRECATED */

#endif /* SULEKHASPELL_H */
