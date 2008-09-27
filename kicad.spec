Summary:	KiCad - is a GPL'd suite of programs for EDA
Summary(pl.UTF-8):	KiCad - zestaw programów na licencji GPL zaliczany do kategorii EDA
Name:		kicad
Version:	20080825
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kicad/%{name}-%{version}.tar.bz2
# Source0-md5:	fa3d3e0d7e2793073581cf46f23cca8d
Source1:	%{name}.desktop
Patch0:		%{name}-makefile.patch
URL:		http://kicad.sourceforge.net/
BuildRequires:	sed >= 4.0
BuildRequires:	wxGTK2-unicode-devel
BuildRequires:	wxGTK2-unicode-gl-devel
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
%setup -q -n %{name}
%patch0 -p1
%if "%{_lib}" != "lib"
	%{__sed} -i -e "s@/lib/@/%{_lib}/@g" libs.linux
%endif
export WX_CONFIG="`which wx-gtk2-unicode-config`"
%{__sed} -i -e "s@wx-config@$WX_CONFIG@g" libs.linux

%build
export WX_CONFIG="`which wx-gtk2-unicode-config`"
%{__make} -f makefile.gtk \
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
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}
install -d $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

for loc in $RPM_BUILD_ROOT%{_localedir}/*; do
	install -d $loc/LC_MESSAGES
	mv $loc/*.mo $loc/LC_MESSAGES
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
%{_desktopdir}/%{name}.desktop
