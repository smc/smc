AC_PREREQ(2.57)
AC_INIT([sulekha],[0.0.11],[santhosh00@gmail.com])
AM_INIT_AUTOMAKE(AC_PACKAGE_NAME, AC_PACKAGE_VERSION)
AC_CHECK_HEADER(aspell.h, [AC_DEFINE(HAVE_ASPELL_H,1, 
   [Define to 1 if you have the <aspell.h> header file.] )] )
AC_CONFIG_HEADERS([config.h])
AC_CHECK_HEADER(pspell/pspell.h, [AC_DEFINE(HAVE_PSPELL_H,1, 
   [Define to 1 if you have the <pspell/pspell.h> header file.] )] )
AC_CHECK_LIB(aspell, new_aspell_speller, SPELLER_LIB="-laspell",
   [AC_CHECK_LIB(pspell, new_pspell_manager, SPELLER_LIB="-lpspell",
      [AC_MSG_ERROR([You must have the aspell or pspell dev libraries to build gtkspell.]) ] ) ] )
      
AC_SUBST(SPELLER_LIB)
SULEKHA_PACKAGES=gtk+-2.0
AC_SUBST(SULEKHA_PACKAGES)
PKG_CHECK_MODULES(SULEKHA, $SULEKHA_PACKAGES)
AC_SUBST(SULEKHA_CFLAGS)
AC_SUBST(SULEKHA_LIBS)

DEBUG=1
AC_SUBST(DEBUG)

# check Pango version so we can use PANGO_UNDERLINE_ERROR when available:
PKG_CHECK_MODULES(PANGO, [pango >= 1.3.5],
   [AC_DEFINE(HAVE_PANGO_UNDERLINE_ERROR, 1, [Define to 1 if PANGO_UNDERLINE_ERROR is available.])],
   [AC_MSG_WARN([Disabling new error underlining since pango < 1.3.5])])

# check Pango version to see if word breaking bug is fixed:
#PKG_CHECK_MODULES(PANGO, [pango >= 1.8.0],
#   [AC_DEFINE(FIXED_PANGO, 1, [Define to 1 if pango >= 1.8.0.])],
#   [AC_MSG_WARN([Enabling word-breaking workarounds since pango < 1.8.0])])

# gtk-doc check:
# gtk-doc check:
# from http://cvs.gnome.org/lxr/source/gtk-doc/examples/configure.in
AC_ARG_WITH(html-dir, AC_HELP_STRING([--with-html-dir=PATH],[path to installed docs]))

if test "x$with_html_dir" = "x" ; then
  HTML_DIR='${datadir}/gtk-doc/html'
else
  HTML_DIR=$with_html_dir
fi

AC_SUBST(HTML_DIR)

gtk_doc_min_version=1.0
AC_MSG_CHECKING([gtk-doc version >= $gtk_doc_min_version])
if pkg-config --atleast-version=$gtk_doc_min_version gtk-doc; then
  AC_MSG_RESULT(yes)
  GTKDOC=true
else
  AC_MSG_RESULT(no)
  GTKDOC=false
fi

dnl Let people disable the gtk-doc stuff.
AC_ARG_ENABLE(gtk-doc, AC_HELP_STRING([--enable-gtk-doc],[Use gtk-doc to build documentation [[default=auto]]]), enable_gtk_doc="$enableval", enable_gtk_doc=auto)

if test x$enable_gtk_doc = xauto ; then
  if test x$GTKDOC = xtrue ; then
    enable_gtk_doc=yes
  else
    enable_gtk_doc=no 
  fi
fi

AM_CONDITIONAL(ENABLE_GTK_DOC, test x$enable_gtk_doc = xyes)

# end gtk-doc check.

AC_PROG_CC
#AC_PROG_LIBTOOL

AC_C_CONST

dnl AM_MAINTAINER_MODE

AC_CONFIG_FILES(Makefile src/Makefile)
AC_OUTPUT
