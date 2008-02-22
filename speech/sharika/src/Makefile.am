bin_PROGRAMS =sharika
sharika_SOURCES = main.c
AM_CPPFLAGS = \
		-DGNOMEDATADIR=\"$(datadir)\"   	\
		$(Libwnck_CFLAGS)			\
		$(GTK_CFLAGS)				\
		$(SPHINX_CFLAGS)
sharika_LDADD= -lm $(SPHINX_LIBS) -lwnck-1


