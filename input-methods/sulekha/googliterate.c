/*
 *File name: googliterate.c
 */

#include <gtk/gtk.h>
#include <glib.h>
#include <stdlib.h>
#include "trans.c"
/*-- This function allows the program to exit properly when the window is closed --*/
gint
destroyapp (GtkWidget * widget, gpointer gdata)
{
  g_print ("Quitting...\n");
  gtk_main_quit ();
  return (FALSE);
}

int
main (int argc, char *argv[])
{
  /*-- Declare the GTK Widgets used in the program --*/
  GtkWidget *window;
  GtkWidget *text;

  gchar *buffer = "eda kitilum ";
  char *buffet = NULL;
  char *mal = NULL;
  const char *command;
  /*--  Initialize GTK --*/
  gtk_init (&argc, &argv);

  /*-- Create the new window --*/
  window = gtk_window_new (GTK_WINDOW_TOPLEVEL);

  /*-- Create a text area --*/
  text = gtk_text_new (NULL, NULL);

  /*-- Set text area to be editable --*/
  gtk_text_set_editable (GTK_TEXT (text), TRUE);

  /*-- Connect the window to the destroyapp function  --*/
  gtk_signal_connect (GTK_OBJECT (window), "delete_event",
		      GTK_SIGNAL_FUNC (destroyapp), NULL);

  /*-- Add the text area to the window --*/
  gtk_container_add (GTK_CONTAINER (window), text);

  /*-- Add some text to the window --*/
  gtk_text_insert (GTK_TEXT (text), NULL, NULL, NULL, buffer,
		   strlen (buffer));

/* Get some characters from the text area */
  buffer = gtk_editable_get_chars (GTK_EDITABLE (text), 4, 11);
  buffet = (char *) buffer;
  printf ("buffet=%s\n", buffet);
  buffer = "kakka";
  mal = transliterate_ml (buffer, 0, strlen (buffer));
  printf ("%s\n", mal);
  sprintf (command, "./spell ml %s", mal);
  system (command);
  printf ("%s\n", command);
  gtk_text_insert (GTK_TEXT (text), NULL, NULL, NULL, buffer,
		   strlen (buffer));

  /*-- Set window border to zero so that text area takes up the whole window --*/
  gtk_container_border_width (GTK_CONTAINER (window), 0);

  /*-- Set the window to be 640 x 200 pixels --*/
  gtk_window_set_default_size (GTK_WINDOW (window), 640, 200);

  /*-- Set the window title --*/
  gtk_window_set_title (GTK_WINDOW (window), "Text Area");

  /*-- Display the widgets --*/
  gtk_widget_show (text);
  gtk_widget_show (window);

  /*-- Start the GTK event loop --*/
  gtk_main ();

  /*-- Return 0 if exit is successful --*/
  return 0;
}
