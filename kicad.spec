%define	libver 1.0
%define	docver 1.1
Summary:	KiCad - is a GPL'd suite of programs for EDA
Summary(pl.UTF-8):	KiCad - zestaw programów na licencji GPL zaliczany do kategorii EDA
Name:		kicad
Version:	20080825
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kicad/%{name}-%{version}.tar.bz2
# Source0-md5:	fa3d3e0d7e2793073581cf46f23cca8d
Source1:	http://dl.sourceforge.net/kicad/%{name}-library-%{libver}.tar.bz2
# Source1-md5:	9c91940aa5f5563bb86c52ff07e8f99a
Source2:	http://dl.sourceforge.net/kicad/%{name}-doc-%{docver}.tar.bz2
# Source2-md5:	fcfbc94f675a19db51370e97b88803b1
Source3:	%{name}.desktop
URL:		http://kicad.sourceforge.net/
BuildRequires:	boost-devel
BuildRequires:	sed >= 4.0
BuildRequires:	which
BuildRequires:	wxGTK2-unicode-devel
BuildRequires:	wxGTK2-unicode-gl-devel
BuildRequires:	wxWidgets-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KiCad consists of a project manager and four main programs:
- kicad - the project manager.
- eeschema - the schematic editor.
- cvpcb - the footprint selector for components used in the circuit
  design.
- pcbnew - the PCB layout program.
- gerbview - the Gerber (photoplotter documents) viewer.

%description -l pl.UTF-8
KiCad składa się z menadżera projektów oraz czterych głównych
programów:
- kicad - menadżer projektów.
- eeschema - edytor schematów.
- cvpcb - narzędzie do wybierania elementów używanych przy
  projektowaniu płytek drukowanych.
- pcbnew - program do projektowania płytek drukowanych.
- gerbview - przeglądarka plików Gerber (dokumentów dla fotoplotera).

%prep
%setup -q -a1 -a2 -n %{name}
mv kicad/doc/help .
mv kicad-library/library .
mv kicad-library/modules .

%if "%{_lib}" != "lib"
	%{__sed} -i -e "s@/lib/@/%{_lib}/@g" libs.linux
%endif
export WX_CONFIG="`which wx-gtk2-unicode-config`"
%{__sed} -i -e "s@wx-config@$WX_CONFIG@g" libs.linux

%build
export WX_CONFIG="`which wx-gtk2-unicode-config`"
%{__make} -f makefile.gtk \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	LD="%{__cxx}" \
	CLAGS="%{rpmcflags}" \
	CXXLAGS="%{rpmcxxflags}" \
	LDFLAGS="%{rpmldflags} %{rpmcxxflags}" \
	WXXFLAGS="`$WX_CONFIG --cxxflags`" \
	WXPATH=%{_libdir} \
	PREFIX_WX_LIBS="lib`$WX_CONFIG --basename`" \
	SUFFIX_WX_LIBSTD="`$WX_CONFIG --utility=`" \
	SUFFIX_WX_LIBGL="_gl-`$WX_CONFIG --release`" \
	LIBVERSION="`$WX_CONFIG --release`" \
	WXSYSLIB="`$WX_CONFIG --libs std`" \
	WXSYSLIB_WITH_GL="`$WX_CONFIG --libs std,gl`"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -f makefile.gtk install \
	KICAD_INTERNAT=$RPM_BUILD_ROOT%{_localedir} \
	KICAD_PLUGINS=$RPM_BUILD_ROOT%{_libdir}/%{name}/plugins \
	KICAD_DATA=$RPM_BUILD_ROOT%{_datadir}/%{name} \
	KICAD_DOCS=$RPM_BUILD_ROOT%{_datadir}/%{name}/help \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}
install -d $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

for loc in $RPM_BUILD_ROOT%{_localedir}/*; do
	install -d $loc/LC_MESSAGES
	mv $loc/*.mo $loc/LC_MESSAGES
done

for loc in $RPM_BUILD_ROOT%{_datadir}/%{name}/help/*; do
	if [ -d $loc/docs_src ]; then
		rm -rf $loc/docs_src;
	fi
done

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc change_log.txt regex_doc.txt todo.txt version.txt
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
