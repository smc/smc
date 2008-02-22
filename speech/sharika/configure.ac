AC_INIT([sharika],[0.1],[aeshyamae@gmail.com])
AM_INIT_AUTOMAKE([-Wall -Werror foreign])
AC_PROG_CC
AC_CONFIG_HEADERS([config.h])
hmmdata=`ls -1 $srcdir/lang/model | egrep -v '(Makefile|CVS)'`
hmmdata=`echo $hmmdata`
AM_PROG_LIBTOOL
PKG_CHECK_MODULES(Libwnck,libwnck-1.0 )
AC_SUBST(Libwnck_CFLAGS)
AC_SUBST(Libwnck_LIBS)
PKG_CHECK_MODULES(GTK,gtk+-2.0)
AC_SUBST(GTK_CFLAGS)
AC_SUBST(GTK_LIBS)
PKG_CHECK_MODULES(SPHINX,sphinx2)
AC_SUBST(SPHINX_CFLAGS)
AC_SUBST(SPHINX_LIBS)

AC_SUBST(hmmdata)
AC_CONFIG_FILES([
	Makefile
	src/Makefile
	lang/Makefile
	lang/model/Makefile
	])
AC_OUTPUT
