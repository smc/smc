/*Copyright (c) 2008, Rajeesh K Nambiar							*
 *											*
 * Chathans is a free software; you can redistribute it and/or modify it under the terms*
 * of GNU General Public License as published by the Free Software Foundation, either	*
 * version 3 of the License, or (at your option) any later version.			*
 *											*
 * Chathans is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;*
 * without even implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.*
 * See the GNU General Public License for more details.					*
 */

#ifdef HAVE_CONFIG_H
#  include <config.h>
#endif

#include <gtk/gtk.h>

#include "callbacks.h"
#include "interface.h"
#include "support.h"

//Widgets - they are private to interface.c, so make them available here
GtkWidget *ascii_button, *mapping_button, *unicode_button;
GtkWidget *status_bar;

//Constants
const gchar *prog_name = "Chathans",
	    *version   = "0.1",
	    *prog_descr= "\nChathans - a forontend to Payyans\nASCII to Unicode Converter\n",
	    *authors[]= {"Chathans:\n\tRajeesh K Nambiar <rajeeshknambiar@gmail.com>\n",
			  "Payyans:\n\tSanthosh Thottingal <santhosh.thottingal@gmail.com>",
			  "\tNishan Naseer <nishan.naseer@gmail.com>", NULL},
	    *copyright = "(c) 2008 Rajeesh K Nambiar",
	    *comments  = "Chathans is a GTK frontend to Payyans ASCII to Unicode Converter",
	    *license   = "Licensed under GNU GPL, version 3 or later",
	    *website   = "http://smc.org.in/Payyans";

//Global Variables
static gchar *ascii_file, *mapping_file, *unicode_file;

//Function Prototypes
void init_file_choosers (GtkWidget *, GtkWidget *, GtkWidget *);
gboolean confirm_file_overwrite(const gchar *);

void start_new_project (GtkMenuItem *menuitem, gpointer user_data)
{
	/* Starting a new project would clear the entries in file chooser
	 * buttons. But, is it a good idea? Many files might be put together
	 * in the same folder or so... lets see
	 */
	initialize_widgets(GTK_WIDGET(menuitem));
}


void display_help_topics (GtkMenuItem *menuitem, gpointer user_data)
{

}


void
display_about (GtkMenuItem *menuitem, gpointer user_data)
{
	GtkWidget *AboutWidget;
	
	AboutWidget = gtk_about_dialog_new();
	gtk_about_dialog_set_program_name(GTK_ABOUT_DIALOG(AboutWidget), prog_name);
	gtk_about_dialog_set_version(GTK_ABOUT_DIALOG(AboutWidget), version);
	gtk_about_dialog_set_authors(GTK_ABOUT_DIALOG(AboutWidget), authors);
	gtk_about_dialog_set_copyright(GTK_ABOUT_DIALOG(AboutWidget), copyright);
	gtk_about_dialog_set_comments(GTK_ABOUT_DIALOG(AboutWidget), comments);
	gtk_about_dialog_set_license(GTK_ABOUT_DIALOG(AboutWidget), license);
	gtk_about_dialog_set_website(GTK_ABOUT_DIALOG(AboutWidget), website);
	gtk_dialog_run(GTK_DIALOG(AboutWidget));
	gtk_widget_destroy(AboutWidget);
}

void initialize_widgets (GtkWidget *window)
{        
	//Since all the Widgets are private members in interface.c, lookup is needed
	ascii_button   = lookup_widget(GTK_WIDGET(window),"AsciiFileButton");
	mapping_button = lookup_widget(GTK_WIDGET(window),"MappingFileButton");
	unicode_button = lookup_widget(GTK_WIDGET(window),"UnicodeFileButton");
	// Set the Filters and default directories for FileChooser buttons
	init_file_choosers(ascii_button, mapping_button, unicode_button);
			
	status_bar = lookup_widget(GTK_WIDGET(window), "StatusBar");
	gtk_statusbar_push(GTK_STATUSBAR(status_bar),
			gtk_statusbar_get_context_id(GTK_STATUSBAR(status_bar),"convert"),
			g_strconcat(prog_name," ",version,NULL));
}


void init_file_choosers (GtkWidget *ascii_button, GtkWidget *mapping_button, GtkWidget *unicode_button)
{
	const gchar* const *sys_data_dir;	//IMP: Note the "gchar* *" thing. "gchar **" won't work!
	gchar *path;
	GFileTest exists = G_FILE_TEST_EXISTS;
	GtkFileFilter *filter = gtk_file_filter_new();
			
	if (ascii_file == NULL)
		ascii_file = g_strdup(g_get_home_dir()); // Default to user's home
	if (unicode_file == NULL)
		unicode_file = g_strdup(g_get_home_dir());
	if (mapping_file == NULL){
		//Here we get the system data dirs, and we should search for payyan's
		//mapping file. Alternatively, if we can find payyan's data dir, will be better
		sys_data_dir = g_get_system_data_dirs(); // Array of gchar*
		guint i;
		for (i=0; *(sys_data_dir+i) != NULL; i++) {
			path = g_strconcat(*(sys_data_dir+i), "payyans/maps", NULL);
			if (g_file_test(path, exists)){
				mapping_file = g_strdup(path);
				break;
			}
		}
	}

	gtk_file_filter_set_name(filter, "*.txt");
	// output Unicode file of type '.txt'
	gtk_file_filter_add_pattern(filter, "*.txt");
	gtk_file_chooser_add_filter(GTK_FILE_CHOOSER(unicode_button), filter);
	// input ASCII file can be of type '.txt' or '.pdf'
	gtk_file_filter_set_name(filter, "*.txt, *.pdf");
	gtk_file_filter_add_pattern(filter, "*.pdf");
	gtk_file_chooser_add_filter(GTK_FILE_CHOOSER(ascii_button), filter);
	// Set the default directories
        gtk_file_chooser_set_current_folder(GTK_FILE_CHOOSER(ascii_button), ascii_file);
        gtk_file_chooser_set_current_folder(GTK_FILE_CHOOSER(mapping_button), mapping_file); 
        gtk_file_chooser_set_current_folder(GTK_FILE_CHOOSER(unicode_button), unicode_file);

	return;
}


// Here is where we interface with Payyans, who does the real job of conversion
void convert_asccii_to_unicode (GtkButton *button, gpointer user_data)
{
	GFileTest test_cond = G_FILE_TEST_IS_REGULAR;
	gchar *ascii_dir, *ascii_base, *temp=NULL;
	gchar *payyans=NULL, *args=NULL, *msg=NULL;
	gint result = -1;
	guint context_id = gtk_statusbar_get_context_id(GTK_STATUSBAR(status_bar),"convert");
			
	ascii_file = gtk_file_chooser_get_filename(GTK_FILE_CHOOSER(ascii_button));
	mapping_file = gtk_file_chooser_get_filename(GTK_FILE_CHOOSER(mapping_button));
	unicode_file = gtk_file_chooser_get_filename(GTK_FILE_CHOOSER(unicode_button));

	if (! g_file_test(ascii_file, test_cond)){
		msg = g_strdup("Choose an ASCII file as input !!");
		goto conv_quit;
	}
	
	if (! g_file_test(mapping_file, test_cond)){
		msg = g_strdup("Choose a Mapping file for conversion !!");
		goto conv_quit;
	}

	//If Unicode file name is not input, create one.
	if (! g_file_test(unicode_file, test_cond)){
		temp = unicode_file;	//Keep the backup. If conversion failed,
					//we need to restore this value
		ascii_base = g_path_get_basename(ascii_file);
		ascii_dir  = g_path_get_dirname(ascii_file);
		gchar *s,*p = g_strrstr(ascii_base, ".txt");
		if (p == NULL)
			p = g_strrstr(ascii_base, ".pdf");
		s = g_strdup(ascii_base);
		s[p - ascii_base] = '\0'; //Strip the extension from filename
		unicode_file = g_strconcat(ascii_dir,"/",s, "_unicode.txt",NULL);
	}
	
	// Check if output file overwrites itself
	if ( g_file_test(unicode_file, G_FILE_TEST_EXISTS) )
		if (! confirm_file_overwrite(unicode_file) )
			goto conv_quit;
			
	// Now locate the 'payyans' binary
	payyans = g_find_program_in_path("payyans");
	if (payyans == NULL){	// Whoops, you don't have payyans installed??
		msg = g_strdup("Error: Payyans is not installed !!");
		gtk_statusbar_push(GTK_STATUSBAR(status_bar), context_id, msg);
		goto conv_quit;
	}
	
	// Prepare the arguments to be passed
	// 'payyans (-p if pdf) -i ascii_file -m mapping_file -o unicode_file'
	args = g_strconcat(g_str_has_suffix(ascii_file,".pdf")?" -p":"",
				" -i \"", ascii_file, "\" -m \"",mapping_file,
				"\" -o \"", unicode_file,"\"",NULL);
	payyans = g_strconcat(payyans, " ", args, NULL);
	result = system(payyans)/256;	// I don't know why system() returns exit status
					// multiplied by 256 !!!
	switch (result)
	{
		case 0:
			gtk_file_chooser_set_filename(GTK_FILE_CHOOSER(unicode_button), unicode_file);
			msg = g_strconcat("Converted Successfully to ",unicode_file,NULL);
			break;
		case 1:
			msg = g_strdup("Error: pdftotext utility is not found !");
			break;
		case 2:
			msg = g_strconcat("Error in mapping file ",mapping_file,NULL);
			break;
		default:
			msg = g_strdup("Error in conversion !");
			break;
	}
	
conv_quit:
	//Display the log message
	gtk_statusbar_push(GTK_STATUSBAR(status_bar), context_id, msg);
	//Restore unicode file path, if conversion isn't successfull
	if (result != 0)
		unicode_file = temp;
	g_free((gpointer)msg);
	g_free((gpointer)payyans);
	g_free((gpointer)args);
	return;
}

gboolean confirm_file_overwrite(const gchar* ucode_file)
{
	GtkWidget *dialog, *label;
	gchar *mesg;
	dialog = gtk_dialog_new_with_buttons("Overwrite?",
						NULL,
						GTK_DIALOG_MODAL, // | GTK_DIALOG_DESTROY_WITH_PARENT,
                                                GTK_STOCK_OK,
                                                GTK_RESPONSE_ACCEPT,
                                                GTK_STOCK_NO,
                                                GTK_RESPONSE_REJECT,
                                                NULL);
	mesg = g_strconcat("\nFile \"", ucode_file, "\" exists.\nDo you wish to overwrite?\n", NULL);
	label = gtk_label_new(mesg);
	gtk_container_add(GTK_CONTAINER(GTK_DIALOG(dialog)->vbox), label);
	gtk_widget_show_all(dialog);
	if (gtk_dialog_run(GTK_DIALOG(dialog)) != GTK_RESPONSE_ACCEPT) {
		gtk_statusbar_push(GTK_STATUSBAR(status_bar),
					gtk_statusbar_get_context_id(GTK_STATUSBAR(status_bar),"convert"),
					"Conversion cancelled.");
		gtk_widget_destroy(dialog);
		return FALSE;
	}
	gtk_widget_destroy(dialog);
	return TRUE;
}
