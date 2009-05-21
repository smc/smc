Name:		kuttans
Version:	0.1
Release:	1%{?dist}
Summary:	Kuttans is a PyQt4 frontend to Payyans ASCII to Unicode converter

Group:		Applications/Text
License:	GPLv3+
URL:		http://smc.org.in/Kuttans
Source0:	http://download.savannah.nongnu.org/releases/smc/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	python-devel
BuildRequires:	PyQt4-devel
#BuildRequires:	gettext
BuildRequires:	desktop-file-utils
Requires:	PyQt4
Requires:	payyans

%description
Kuttans is a PyQt4 frontend to Payyans ASCII to Unicode converter
The name is a pun of Qt+Payyans

%prep
%setup -q

%build
pyuic4 ui/kuttans.ui > src/kuttans_ui.py
pyrcc4 qrc/kuttans.qrc > src/kuttans_rc.py
#for lc in po/%{name}-*.po; do
#	msgfmt -o po/`basename ${lc} .po`.mo ${lc}
#done

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/%{name}
install -m 755 src/kuttans ${RPM_BUILD_ROOT}%{_bindir}/%{name}
install -m 644 src/*.py{,c} ${RPM_BUILD_ROOT}%{_datadir}/%{name}/
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications/ %{name}.desktop
#Install the translation files
#for lc in po/*.mo; do
#	_lang=`echo ${lc} | cut -d - -f2 | cut -d . -f1`
#	mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/locale/${_lang}/LC_MESSAGES/
#	install -m 0644 ${lc} ${RPM_BUILD_ROOT}%{_datadir}/locale/${_lang}/LC_MESSAGES/%{name}.mo 
#done
#%find_lang %{name}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files 
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*.py
%{_datadir}/%{name}/*.pyc
%doc README LICENSE

%changelog
* Mon Apr 13 2009 Rajeesh K Nambiar <rajeeshknambiar@gmail.com> - 0.1-1
- Initial build for Fedora.
