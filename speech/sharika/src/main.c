/* This file is a part of gnome-voice-control
 *
 * Copyright (C) 2007  Shyam Karanattu <aeshyamae@gmail.com>
 *
 * main.c:
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330,
 * Boston, MA 02111-1307, USA.
 *
 */
 #define WNCK_I_KNOW_THIS_IS_UNSTABLE
 #include <libwnck/libwnck.h>
 #include <gtk/gtk.h>
 #include <X11/Xlib.h>
#include <sys/types.h>
#include <sys/time.h>
#include <stdio.h>
#include <signal.h>
WnckScreen *scr;
WnckWindow *win;
GList *tmp,*head;
#define DHVANISCRIPT GNOMEDATADIR"/sharika/parser.sh"

#include <setjmp.h>
#include <string.h>

#include "s2types.h"
#include "err.h"
#include "ad.h"
#include "cont_ad.h"
#include "fbs.h"

#define SAMPLE_RATE   16000

static ad_rec_t *ad;

/* Sleep for specified msec */
static void sleep_msec (int32 ms)
{
    struct timeval tmo;
    
    tmo.tv_sec = 0;
    tmo.tv_usec = ms*1000;
    
    select(0, NULL, NULL, NULL, &tmo);
}

static void utterance_loop(int argc,char *argv[])
{
  int16 adbuf[4096];
  int32 k, fr, ts, rem;
  char *hyp;
  cont_ad_t *cont;
  int count=0,i=1,flag;
  char word[256];
  /* Initialize continuous listening module */
  if ((cont = cont_ad_init (ad, ad_read)) == NULL)
    E_FATAL("cont_ad_init failed\n");
  if (ad_start_rec (ad) < 0)
    E_FATAL("ad_start_rec failed\n");
  if (cont_ad_calib (cont) < 0)
    E_FATAL("cont_ad_calib failed\n");
  
  for (;;)
    {
           /* Indicate listening for next utterance */
      printf ("READY....\n");
      fflush (stdout); fflush (stderr);
      
      /* Await data for next utterance */
      while ((k = cont_ad_read (cont, adbuf, 4096)) == 0)
	sleep_msec(200);
      
      if (k < 0)
	E_FATAL("cont_ad_read failed\n");
      
      /*
       * Non-zero amount of data received; start recognition of new utterance.
       * NULL argument to uttproc_begin_utt => automatic generation of utterance-id.
       */
      if (uttproc_begin_utt (NULL) < 0)
	E_FATAL("uttproc_begin_utt() failed\n");
      uttproc_rawdata (adbuf, k, 0);
      printf ("Listening...\n"); fflush (stdout);
      
      /* Note timestamp for this first block of data */
      ts = cont->read_ts;
      
      /* Decode utterance until end (marked by a "long" silence, >1sec) */
      for (;;) {
	/* Read non-silence audio data, if any, from continuous listening module */
	if ((k = cont_ad_read (cont, adbuf, 4096)) < 0)
	  E_FATAL("cont_ad_read failed\n");
	if (k == 0) {
	  /*
	   * No speech data available; check current timestamp with most recent
	   * speech to see if more than 1 sec elapsed.  If so, end of utterance.
	   */
	  if ((cont->read_ts - ts) > DEFAULT_SAMPLES_PER_SEC)
	    break;
	} else {
	  /* New speech data received; note current timestamp */
	  ts = cont->read_ts;
	}
	
	/*
	 * Decode whatever data was read above.  NOTE: Non-blocking mode!!
	 * rem = #frames remaining to be decoded upon return from the function.
	 */
	rem = uttproc_rawdata (adbuf, k, 0);
	
	/* If no work to be done, sleep a bit */
	if ((rem == 0) && (k == 0))
	  sleep_msec (20);
      }
      
      /*
       * Utterance ended; flush any accumulated, unprocessed A/D data and stop
       * listening until current utterance completely decoded
       */
      ad_stop_rec (ad);
      while (ad_read (ad, adbuf, 4096) >= 0);
      cont_ad_reset (cont);
      
      printf ("Stopped listening, please wait...\n"); fflush (stdout);
#if 0
      /* Power histogram dump (FYI) */
      cont_ad_powhist_dump (stdout, cont);
#endif
      /* Finish decoding, obtain and print result */
      uttproc_end_utt ();
      if (uttproc_result (&fr, &hyp, 1) < 0)
	E_FATAL("uttproc_result failed\n");
      
      
      /*obtaining the results*/
      sscanf (hyp, "%s", word);
      printf ("%d: %s\n", fr,word); fflush (stdout);
 	  win=wnck_screen_get_active_window(scr);
	  tmp=wnck_screen_get_windows(wnck_window_get_screen(win));
	
      i=g_list_index(tmp,win);/*the place value  of window in the list*/
      printf("<<<<<<<<<<<<<<>>>>>>>>>>>>>>i:%d,%s\n\n\n",i,wnck_window_get_name(win));
      count=0;
      while(tmp!=NULL)
	{
	  printf("%d:%s\n\n",count,wnck_window_get_name(tmp->data));
	  tmp=tmp->next;count++;
	}
            /*comparison and action for DAKKU */
      if(strcmp(word,"PADU")==0)
	g_spawn_command_line_async("totem --play",NULL);
      if(strcmp(word,"EMACS")==0)
	g_spawn_command_line_async("emacs",NULL);
      if(strcmp(word,"SAMAYAM")==0)
	g_spawn_command_line_async(DHVANISCRIPT,NULL);
      if(strcmp(word,"VALAPARATHU")==0)
	g_spawn_command_line_async("epiphany",NULL);
      if(strcmp(word,"EAZHUTHIDAM")==0)
      g_spawn_command_line_async("gedit",NULL);
      /*Minimizing current active window*/
           if (strcmp (word, "CHURUKKU") == 0)
	      wnck_window_minimize(win);
      /*Moving focus(active window)towards the left of the panel.The active window is changed to
 the next normal window on the left.effect of alt+tab key press*/
      if(strcmp(word,"ADUTHATHU")==0)
	{
	  win=wnck_screen_get_active_window(scr);
	  tmp=wnck_screen_get_windows(wnck_window_get_screen(win));
	
	  while(tmp!=NULL)/*while traces the current active window through the list*/
	    {
	      printf("tracing:current:%s\n\ntmp:%s\n\n",wnck_window_get_name(win),wnck_window_get_name(tmp->data));	   
	      if(tmp->data==win)
		{   
			  printf("BREAKED with tmp:%s\n",wnck_window_get_name(tmp->data));
		  break;
		}
	    
	      tmp=tmp->next;
	      
	    }
	  if(tmp==NULL){printf("BULL SHIT GIVE A WINDOW IN THE LIST\n\n");}//exit(1);}
	  if(tmp->next==NULL)/*shifting back to the first window by refreshing the list*/
	    tmp=wnck_screen_get_windows(wnck_window_get_screen(win));
	  else
	    tmp=tmp->next;
	  printf("cuow:%s\n\n",wnck_window_get_name(tmp->data));
	
		
	  
	  while(tmp!=NULL)
	    {
	      printf("tmp in while:%s\n\n",wnck_window_get_name(tmp->data));
	      if(wnck_window_get_window_type(tmp->data)==WNCK_WINDOW_NORMAL)
		{
		  wnck_window_activate(tmp->data,0);
		  flag=1;
		  break;
		}
	      else
		tmp=tmp->next;
	    }
	  
	  if(flag==0)
	    {
	      printf("FLAG==0 DETECTED:\n");
	      tmp=wnck_screen_get_windows(wnck_window_get_screen(win));
	      while(tmp!=NULL)
		{
		  printf("tmp in last while:%s\n",wnck_window_get_name(tmp->data));
		  if(wnck_window_get_window_type(tmp->data)==WNCK_WINDOW_NORMAL)
		    {
		      wnck_window_activate(tmp->data,0);
		      break;
		    }
		  else
		    tmp=tmp->next;
		}
	    }
	
	 
	}
      if(strcmp(word,"VALUTHAKKU")==0)
	{
	  if(wnck_window_get_window_type(win)!= WNCK_WINDOW_NORMAL)
	    {
	      if(wnck_window_get_window_type(wnck_screen_get_previously_active_window(scr))==WNCK_WINDOW_NORMAL)
		win=wnck_screen_get_previously_active_window(scr);
	    }
	      wnck_window_unminimize(win,0);
	    
	}

      while(gtk_events_pending())/*gtk probing and refreshing the win and tmp*/
	{
	  gtk_main_iteration();
	  win=wnck_screen_get_active_window(scr);
	  tmp=wnck_screen_get_windows(wnck_window_get_screen(win));
	  
	}
      
      /* Resume A/D recording for next utterance */
      if (ad_start_rec (ad) < 0)
	E_FATAL("ad_start_rec failed\n");
    }
  
  cont_ad_close (cont);
}

static char *sphinx_command =
  "sharika "
  "-bestpath yes "
  "-fsgfn " GNOMEDATADIR "/sharika/sharika.fsg "
  "-dictfn " GNOMEDATADIR "/sharika/sharika.dic "
  "-hmmdirlist " GNOMEDATADIR "/sharika/model "
  "-hmmext chmm "
  "-mdeffn "GNOMEDATADIR "/sharika/mdef "
  "-meanfn " GNOMEDATADIR "/sharika/means "
  "-varfn " GNOMEDATADIR "/sharika/variances "
  "-mixwfn " GNOMEDATADIR "/sharika/mixture_weights ";

static jmp_buf jbuf;
static void sighandler(int signo)
{
    longjmp(jbuf, 1);
}

int main (int argc, char *argv[])
{
    /* Make sure we exit cleanly (needed for profiling among other things) */
  g_shell_parse_argv(sphinx_command,&argc,&argv,NULL);
     gtk_init(&argc, &argv);
 
     scr = wnck_screen_get_default();
     while(gtk_events_pending()) gtk_main_iteration();
     win = wnck_screen_get_active_window(scr);
      tmp=wnck_screen_get_windows(wnck_window_get_screen(win));
     signal(SIGINT, &sighandler);

    fbs_init (argc, argv);
    
    if ((ad = ad_open_sps (SAMPLE_RATE)) == NULL)
	E_FATAL("ad_open_sps failed\n");

    // E_INFO("%s COMPILED ON: %s, AT: %s\n\n", argv[0], __DATE__, __TIME__);

    if (setjmp(jbuf) == 0) {
      utterance_loop (argc,argv);
    }

    fbs_end ();
    ad_close (ad);

    return 0;
}
