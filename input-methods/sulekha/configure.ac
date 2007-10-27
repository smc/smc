AC_INIT([Spell],[0.8],[santhosh],[Spell])
AM_INIT_AUTOMAKE
AC_PROG_CC
CFLAGS="-g -O -Wall"
AC_PATH_PROGS(BASH, bash)
AC_PROG_INSTALL

dnl ================================================================
dnl Start of pkg-config checks
dnl ================================================================

PKG_CHECK_MODULES(SULEKHA, [
	gtk+-2.0 >= 2.10.0
])
GEDIT_LIBS="${SULEKHA_LIBS}"
AC_SUBST(SULEKHA_LIBS)
AC_SUBST(SULEKHA_CFLAGS)
AC_CONFIG_FILES([
Makefile
])
AC_OUTPUT
