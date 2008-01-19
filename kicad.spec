%define		_release	r304
Summary:	KiCad - is a GPL'd suite of programs for EDA
Summary(pl.UTF-8):	KiCad - zestaw programów na licencji GPL zaliczany do kategorii EDA
Name:		kicad
Version:	20071004
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kicad/%{name}-%{version}-%{_release}.tar.bz2
# Source0-md5:	8ef6310123e9361c5780d321ec07cc8b
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
%if "%{_lib}" != "lib"
	%{__sed} -i -e "s@/lib/@/%{_lib}/@g" libs.linux
%endif

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
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc change_log.txt news.txt regex_doc.txt todo.txt version.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_docdir}/%{name}
