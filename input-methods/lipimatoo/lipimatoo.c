/*
 *File name: lipimatoo.c
 *
 * Copyright (C) 2007-2008
 *  Praveen Arimbrathodiyil <pravi.a@gmail.com>,
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


*/

#include <gtk/gtk.h>
#include <glib.h>
#include <gdk/gdk.h>
#include <gdk/gdkkeysyms.h>
#include <gtk/gtkwidget.h>
#include <stdlib.h>
#include "transliteration.c"
/*-- This function allows the program to exit properly when the window is closed --*/
gint destroyapp (GtkWidget *widget, gpointer gdata)
{
  g_print ("Quitting...\n");
  gtk_main_quit();
  return (FALSE);
}

static gint 
key_press_cb(GtkWidget* widget, GdkEventKey* event, gpointer data)
{
    gchar *buffer,*mal;
    gint position;
    static gint start_position=0;
/*  if (event->length > 0)
    printf("The key event's string is `%s'\n", event->string);

  printf("The name of this keysym is `%s'\n", 
         gdk_keyval_name(event->keyval));
*/  
  switch (event->keyval)
    {

    case GDK_space:
      printf("Space pressed\n");
      position = gtk_text_get_point(GTK_TEXT(widget));
      printf("text from %d to %d\n",start_position,position);

      buffer = gtk_editable_get_chars (GTK_EDITABLE( widget ),start_position,position);
      start_position+=position+1;
      g_print("%s\n",buffer);

      mal = transliterate_ml(buffer,0,strlen(buffer));
      g_print("%s\n",mal);

      gtk_text_insert(GTK_TEXT(widget), NULL, NULL, NULL, mal, strlen(mal));
      printf("start_position is %d strlen\(mal\) is %d\n",start_position,strlen(mal));
      start_position+=strlen(mal);	
      break;
    default:
      break;
    }

 
}

int main (int argc, char *argv[])
{
  /*-- Declare the GTK Widgets used in the program --*/
  GtkWidget *window;
  GtkWidget *text;

  
  /*--  Initialize GTK --*/
  gtk_init (&argc, &argv);

  /*-- Create the new window --*/
  window = gtk_window_new(GTK_WINDOW_TOPLEVEL);

  /*-- Create a text area --*/
  text = gtk_text_new(NULL, NULL);

  /*-- Set text area to be editable --*/
  gtk_text_set_editable(GTK_TEXT (text), TRUE);

  /*-- Connect the window to the destroyapp function  --*/
  gtk_signal_connect(GTK_OBJECT(window), "delete_event", GTK_SIGNAL_FUNC(destroyapp), NULL);

  /*-- Add the text area to the window --*/
  gtk_container_add(GTK_CONTAINER(window), text);

  /*-- Add some text to the window --*/

//gtk_text_insert(GTK_TEXT(text), NULL, NULL, NULL, buffer, strlen(buffer));

gtk_signal_connect(GTK_OBJECT (text), "key_press_event",
		     (GtkSignalFunc) key_press_cb, NULL);
  /*-- Set window border to zero so that text area takes up the whole window --*/
  gtk_container_border_width (GTK_CONTAINER (window), 0);

  /*-- Set the window to be 640 x 200 pixels --*/
  gtk_window_set_default_size (GTK_WINDOW(window), 640, 200);

  /*-- Set the window title --*/
  gtk_window_set_title(GTK_WINDOW (window), "Googliterate");

  /*-- Display the widgets --*/
  gtk_widget_show(text);
  gtk_widget_show(window);

  /*-- Start the GTK event loop --*/
  gtk_main();

  /*-- Return 0 if exit is successful --*/
  return 0;
}
  
