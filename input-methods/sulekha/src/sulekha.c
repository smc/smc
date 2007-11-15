/* sulekha.c
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

#include <gtk/gtk.h>
#include "../config.h"
#include "sulekhaspell.h"

const char *langs[] =
  { "ml", "hi", "kn", "or", "ta", "en_US", "de_DE", "ja_JP", NULL };

GtkWidget *window, *languagelist, *attached, *view;


static void
activate_action (GtkAction * action)
{
  const gchar *name = gtk_action_get_name (action);
  const gchar *typename = G_OBJECT_TYPE_NAME (action);

  GtkWidget *dialog;

  dialog = gtk_message_dialog_new (GTK_WINDOW (window),
				   GTK_DIALOG_DESTROY_WITH_PARENT,
				   GTK_MESSAGE_INFO,
				   GTK_BUTTONS_CLOSE,
				   "You activated action: \"%s\" of type \"%s\"",
				   name, typename);

  /* Close dialog on user response */
  g_signal_connect (dialog,
		    "response", G_CALLBACK (gtk_widget_destroy), NULL);

  gtk_widget_show (dialog);
}


static void
activate_email (GtkAboutDialog * about, const gchar * link, gpointer data)
{
  g_print ("send mail to %s\n", link);
}

static void
activate_url (GtkAboutDialog * about, const gchar * link, gpointer data)
{
  g_print ("show url %s\n", link);
}
static void
about (GtkAction * action, GtkWidget * window)
{
  GdkPixbuf *pixbuf, *transparent;
  gchar *filename;

  const gchar *authors[] = {
    "Santhosh Thottongal <santhosh00@gmail.com>",
    "Praveen Arimbrathodiyil <pravi.a@gmail.com>",
    NULL
  };

  const gchar *documentors[] = {
    "Santhosh Thottongal <santhosh00@gmail.com>",
    "Praveen Arimbrathodiyil <pravi.a@gmail.com>",
    NULL
  };

  const gchar *license =
    "This library is free software; you can redistribute it and/or\n"
    "modify it under the terms of the GNU Library General Public License as\n"
    "published by the Free Software Foundation; either version 3 of the\n"
    "License, or (at your option) any later version.\n"
    "\n"
    "This library is distributed in the hope that it will be useful,\n"
    "but WITHOUT ANY WARRANTY; without even the implied warranty of\n"
    "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU\n"
    "Library General Public License for more details.\n"
    "\n"
    "You should have received a copy of the GNU Library General Public\n"
    "License along with the Gnome Library; see the file COPYING.LIB.  If not,\n"
    "write to the Free Software Foundation, Inc., 59 Temple Place - Suite 330,\n"
    "Boston, MA 02111-1307, USA.\n";

  gtk_about_dialog_set_email_hook (activate_email, NULL, NULL);
  gtk_about_dialog_set_url_hook (activate_url, NULL, NULL);
  gtk_show_about_dialog (GTK_WINDOW (window),
			 "name", "Sulekha",
			 "version", PACKAGE_VERSION,
			 "copyright",
			 "(C) 2007-2008 Santhosh Thottingal, Praveen Arimbrathodiyil",
			 "license", license, "website", "http://smc.org.in",
			 "comments", "Intelligent Typing System", "authors",
			 authors, "documenters", documentors, "logo",
			 NULL, NULL);

  //g_object_unref (transparent);
}
static GtkActionEntry entries[] = {
  {"FileMenu", NULL, "_File"},	/* name, stock id, label */
  {"EditMenu", NULL, "_Edit"},	/* name, stock id, label */
  {"OptionsMenu", NULL, "_Options"},	/* name, stock id, label */
  {"HelpMenu", NULL, "_Help"},	/* name, stock id, label */
  {"New", GTK_STOCK_NEW,	/* name, stock id */
   "_New", "<control>N",	/* label, accelerator */
   "Create a new file",		/* tooltip */
   G_CALLBACK (activate_action)},
  {"Open", GTK_STOCK_OPEN,	/* name, stock id */
   "_Open", "<control>O",	/* label, accelerator */
   "Open a file",		/* tooltip */
   G_CALLBACK (activate_action)},
  {"Save", GTK_STOCK_SAVE,	/* name, stock id */
   "_Save", "<control>S",	/* label, accelerator */
   "Save current file",		/* tooltip */
   G_CALLBACK (activate_action)},
  {"SaveAs", GTK_STOCK_SAVE,	/* name, stock id */
   "Save _As...", NULL,		/* label, accelerator */
   "Save to a file",		/* tooltip */
   G_CALLBACK (activate_action)},
  {"ClearSessionDictionary", NULL,	/* name, stock id */
   "Clear Session Dictionary", NULL,	/* label, accelerator */
   "Clear Session Dictionary",	/* tooltip */
   G_CALLBACK (activate_action)},
  {"SynchronizeDictionaries", NULL,	/* name, stock id */
   "Synchronize Dictionaries", NULL,	/* label, accelerator */
   "Synchronize Dictionaries",	/* tooltip */
   G_CALLBACK (activate_action)},
  {"Quit", GTK_STOCK_QUIT,	/* name, stock id */
   "_Quit", "<control>Q",	/* label, accelerator */
   "Quit",			/* tooltip */
   G_CALLBACK (activate_action)},
  {"SelectAll", NULL,		/* name, stock id */
   "Select _All", "<control>A",	/* label, accelerator */
   "Select All",		/* tooltip */
   G_CALLBACK (activate_action)},
  {"ClearAll", NULL,		/* name, stock id */
   "Clear All", "<control>C",	/* label, accelerator */
   "Clear All",			/* tooltip */
   G_CALLBACK (activate_action)},
  {"Paste", NULL,		/* name, stock id */
   "Paste", "<control>V",	/* label, accelerator */
   "Paste",			/* tooltip */
   G_CALLBACK (activate_action)},
  {"SaveDictionariesonExit", NULL,	/* name, stock id */
   "Save Dictionaries on Exit", "<control>V",	/* label, accelerator */
   "Save Dictionaries on Exit",	/* tooltip */
   G_CALLBACK (activate_action)},
  {"About", GTK_STOCK_ABOUT,	/* name, stock id */
   "_About", "<control>B",	/* label, accelerator */
   "About",			/* tooltip */
   G_CALLBACK (about)},
  {"Logo", "demo-gtk-logo",	/* name, stock id */
   NULL, NULL,			/* label, accelerator */
   "GTK+",			/* tooltip */
   G_CALLBACK (activate_action)},
};
static guint n_entries = G_N_ELEMENTS (entries);


static const gchar *ui_info =
  "<ui>"
  "  <menubar name='MenuBar'>"
  "    <menu action='FileMenu'>"
  "      <menuitem action='New'/>"
  "      <menuitem action='Open'/>"
  "      <menuitem action='Save'/>"
  "      <menuitem action='SaveAs'/>"
  "      <separator/>"
  "      <menuitem action='ClearSessionDictionary'/>"
  "      <menuitem action='SynchronizeDictionaries'/>"
  "        <separator/>"
  "      <menuitem action='Quit'/>"
  "    </menu>"
  "  <menu action='EditMenu'>"
  "      <menuitem action='SelectAll'/>"
  "      <menuitem action='ClearAll'/>"
  "      <menuitem action='Paste'/>"
  "    </menu>"
  "    <menu action='OptionsMenu'>"
  "      <menuitem action='SaveDictionariesonExit'/>"
  "    </menu>"
  "    <menu action='HelpMenu'>"
  "      <menuitem action='About'/>"
  "    </menu>"
  "  </menubar>"
  "  <toolbar  name='ToolBar'>"
  "    <toolitem action='New'/>"
  "    <toolitem action='Open'/>"
  "    <toolitem action='Save'/>"
  "    <toolitem action='Quit'/>"
  "    <separator action='Sep1'/>"
  "    <toolitem action='Logo'/>" "  </toolbar>" "</ui>";


static void
report_sulekhaspell_error (const char *err)
{
  GtkWidget *dlg;
  dlg = gtk_message_dialog_new (GTK_WINDOW (window),
				GTK_DIALOG_DESTROY_WITH_PARENT,
				GTK_MESSAGE_ERROR,
				GTK_BUTTONS_CLOSE,
				"SulekhaSpell error: %s", err);
  gtk_dialog_run (GTK_DIALOG (dlg));
  gtk_widget_destroy (dlg);
}

static void
attach_cb ()
{
  SulekhaSpell *spell;
  GError *error = NULL;

  if (gtk_toggle_button_get_active (GTK_TOGGLE_BUTTON (attached)))
    {
      int lang;

      lang = gtk_option_menu_get_history (GTK_OPTION_MENU (languagelist));

      spell =
	sulekhaspell_new_attach (GTK_TEXT_VIEW (view), langs[lang], &error);

      if (spell == NULL)
	{
	  report_sulekhaspell_error (error->message);
	  g_error_free (error);
	}
    }
  else
    {
      sulekhaspell_detach (sulekhaspell_get_from_text_view
			   (GTK_TEXT_VIEW (view)));
    }
}

static void
setlang_cb ()
{
  SulekhaSpell *spell;
  int lang;
  GError *error = NULL;

  spell = sulekhaspell_get_from_text_view (GTK_TEXT_VIEW (view));
  if (spell == NULL)
    return;

  lang = gtk_option_menu_get_history (GTK_OPTION_MENU (languagelist));
  if (!sulekhaspell_set_language (spell, langs[lang], &error))
    {
      report_sulekhaspell_error (error->message);
      g_error_free (error);
    }
}

static void
build_languagelist ()
{
  int i;
  GtkWidget *menu, *mi;

  languagelist = gtk_option_menu_new ();
  menu = gtk_menu_new ();
  for (i = 0; langs[i] != NULL; i++)
    {
      mi = gtk_menu_item_new_with_label (langs[i]);
      gtk_widget_show (mi);
      g_signal_connect (G_OBJECT (mi), "activate",
			G_CALLBACK (setlang_cb), NULL);
      gtk_menu_shell_append (GTK_MENU_SHELL (menu), mi);
    }
  gtk_option_menu_set_menu (GTK_OPTION_MENU (languagelist), menu);
}

int
main (int argc, char *argv[])
{
  GtkWidget *box, *hbox, *scroll;
  GtkUIManager *ui;
  GtkActionGroup *actions;
  GtkWidget *menu;
  GtkWidget *menuitem;
  GtkWidget *sw;
  GtkWidget *menubar;
  GtkWidget *menubox;
  GError *error = NULL;
  GtkWidget *label;
  if (argc > 1)
    {
      printf ("%s-->%s\n", argv[1],
	      transliterate_ml (argv[1], 0, strlen (argv[1])));
      exit (0);
    }
  gtk_init (&argc, &argv);

  window = gtk_window_new (GTK_WINDOW_TOPLEVEL);

  actions = gtk_action_group_new ("Actions");
  gtk_action_group_add_actions (actions, entries, n_entries, NULL);
  ui = gtk_ui_manager_new ();
  gtk_ui_manager_insert_action_group (ui, actions, 0);
  g_object_unref (actions);
  gtk_window_add_accel_group (GTK_WINDOW (window),
			      gtk_ui_manager_get_accel_group (ui));



  if (!gtk_ui_manager_add_ui_from_string (ui, ui_info, -1, &error))
    {
      g_message ("building menus failed: %s", error->message);
      g_error_free (error);
    }
  menubox = gtk_vbox_new (FALSE, 0);
  menubar = gtk_vbox_new (FALSE, 0);
//      gtk_container_add (GTK_CONTAINER (box), menubox);
  gtk_widget_show (menubox);
// gtk_container_add (GTK_CONTAINER (box), box1);

  gtk_box_pack_start (GTK_BOX (menubox),
		      gtk_ui_manager_get_widget (ui, "/MenuBar"), FALSE,
		      FALSE, 0);
  gtk_box_pack_start (GTK_BOX (menubar),
		      gtk_ui_manager_get_widget (ui, "/ToolBar"), FALSE,
		      FALSE, 0);



  view = gtk_text_view_new ();
  gtk_text_view_set_wrap_mode (GTK_TEXT_VIEW (view), GTK_WRAP_WORD);

  scroll = gtk_scrolled_window_new (NULL, NULL);
  gtk_scrolled_window_set_policy (GTK_SCROLLED_WINDOW (scroll),
				  GTK_POLICY_AUTOMATIC, GTK_POLICY_AUTOMATIC);
  gtk_scrolled_window_set_shadow_type (GTK_SCROLLED_WINDOW (scroll),
				       GTK_SHADOW_IN);
  gtk_container_add (GTK_CONTAINER (scroll), view);

  build_languagelist ();

  hbox = gtk_hbox_new (FALSE, 5);
  label = gtk_label_new ("Languages");
  attached = gtk_toggle_button_new_with_label ("Attached");
  g_signal_connect (G_OBJECT (attached), "toggled",
		    G_CALLBACK (attach_cb), NULL);
  gtk_toggle_button_set_active (GTK_TOGGLE_BUTTON (attached), TRUE);
  gtk_box_pack_start (GTK_BOX (hbox), attached, FALSE, FALSE, 0);
  gtk_box_pack_end (GTK_BOX (hbox), languagelist, FALSE, FALSE, 0);
  gtk_box_pack_end (GTK_BOX (hbox), label, FALSE, FALSE, 0);
  box = gtk_vbox_new (FALSE, 5);
  gtk_box_pack_start (GTK_BOX (box), menubox, FALSE, FALSE, 0);
  gtk_box_pack_start (GTK_BOX (box), menubar, FALSE, FALSE, 0);
  gtk_box_pack_start (GTK_BOX (box), scroll, TRUE, TRUE, 0);
  gtk_box_pack_start (GTK_BOX (box), hbox, FALSE, FALSE, 0);

  gtk_widget_show_all (box);

  gtk_window_set_default_size (GTK_WINDOW (window), 1200, 800);
  gtk_window_set_title (GTK_WINDOW (window), "Sulekha");
  gtk_container_set_border_width (GTK_CONTAINER (window), 1);
  g_signal_connect (G_OBJECT (window), "delete-event",
		    G_CALLBACK (gtk_main_quit), NULL);
  gtk_container_add (GTK_CONTAINER (window), box);

  gtk_widget_show (window);
  gtk_window_maximize (window);
  gtk_main ();

  return 0;
}
