# TODO:
# - fix mimelnk installation
#
Summary:	KiCad - is a GPL'd suite of programs for EDA
Summary(pl.UTF-8):	KiCad - zestaw programów na licencji GPL zaliczany do kategorii EDA
Name:		kicad
Version:	5.0.0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://launchpad.net/kicad/5.0/%{version}/+download/%{name}-%{version}.tar.xz
# Source0-md5:	99a39910a3f7d8320b605bb9a9ff3af8
Source1:	https://github.com/KiCad/kicad-doc/archive/%{version}/%{name}-doc-%{version}.tar.gz
# Source1-md5:	0d6e78e1087a04c8e6385f76c0727bf7
Source2:	https://github.com/KiCad/kicad-i18n/archive/%{version}/%{name}-i18n-%{version}.tar.gz
# Source2-md5:	1e1503b89c575c80ff51583d40667c14
Source3:	https://github.com/KiCad/kicad-symbols/archive/%{version}/%{name}-symbols-%{version}.tar.gz
# Source3-md5:	03cb33312062571118a277bafd01c06d
Source4:	https://github.com/KiCad/kicad-footprints/archive/%{version}/%{name}-footprints-%{version}.tar.gz
# Source4-md5:	e8ce40c47b108280d7878f858899ab10
Source5:	https://github.com/KiCad/kicad-packages3D/archive/%{version}/%{name}-packages3D-%{version}.tar.gz
# Source5-md5:	aac66499bbbd9f21ad3e90af7ba854d2
Source6:	https://github.com/KiCad/kicad-templates/archive/%{version}/%{name}-templates-%{version}.tar.gz
# Source6-md5:	d8a5c09a33588a73eb8552c83bdb0381
Patch0:		nostrip.patch
# https://code.launchpad.net/~lkundrak/kicad/appstream-data/+merge/293391
Patch1:		lto.patch
Patch2:		python.patch
Patch3:		3d_plugindir.patch
URL:		http://www.kicad-pcb.org/
BuildRequires:	GLM
BuildRequires:	OCE-devel
BuildRequires:	appstream-glib
BuildRequires:	asciidoc
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.6.4
BuildRequires:	curl-devel
BuildRequires:	dblatex
BuildRequires:	desktop-file-utils
BuildRequires:	doxygen
BuildRequires:	glew-devel
BuildRequires:	ngspice-devel
BuildRequires:	openssl-devel
BuildRequires:	perl-Unicode-LineBreak
BuildRequires:	po4a >= 0.51
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	sed >= 4.0
BuildRequires:	which
BuildRequires:	wxGTK2-unicode-devel >= 3.0.0
BuildRequires:	wxGTK2-unicode-gl-devel >= 3.0.0
BuildRequires:	wxWidgets-devel >= 3.0.0
BuildRequires:	zlib-devel
Obsoletes:	kicad-doc-hu < 1:4.0.6-1
Obsoletes:	kicad-doc-pt < 1:4.0.6-1
Obsoletes:	kicad-doc-zh_CN < 1:4.0.6-1
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
KiCad składa się z menadżera projektów oraz czterech głównych
programów:
- kicad - menadżer projektów.
- eeschema - edytor schematów.
- cvpcb - narzędzie do wybierania elementów używanych przy
  projektowaniu płytek drukowanych.
- pcbnew - program do projektowania płytek drukowanych.
- gerbview - przeglądarka plików Gerber (dokumentów dla fotoplotera).

%package library
Summary:	Symbols, footprints and templates for kicad
Summary(pl.UTF-8):	Symbole, obudowy i wzorce dla kicad
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif
Requires:	kicad >= 1:5.0.0

%description library
Symbols, footprints and templates for kicad.

%description -l pl.UTF-8
Symbole, obudowy i wzorce dla kicad.

%package packages3D
Summary:	Packages3D for kicad
Summary(pl.UTF-8):	Trójwymiarowe modele obudów dla kicad
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif
Requires:	kicad >= 1:5.0.0

%description packages3D
Packages3D for kicad

%description -l pl.UTF-8
Trójwymiarowe modele obudów dla kicad.

%package doc
Summary:	Documentation for kicad
Summary(fr.UTF-8):	Documentations pour kicad en anglais
License:	GPL v2+
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc
Documentation and tutorials for kicad in English

%package doc-ca
Summary:	Documentation for Kicad in Catalan
Group:		Documentation
Requires:	%{name}-doc = %{epoch}:%{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-ca
Documentation and tutorials for Kicad in Catalan.

%package doc-de
Summary:	Documentation for Kicad in German
Summary(fr.UTF-8):	Documentations pour kicad en allemand
Group:		Documentation
Requires:	%{name}-doc = %{epoch}:%{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-de
Documentation and tutorials for Kicad in German.

%package doc-es
Summary:	Documentation for Kicad in Spanish
Summary(fr.UTF-8):	Documentations pour kicad en espagnol
Group:		Documentation
Requires:	%{name}-doc = %{epoch}:%{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-es
Documentation and tutorials for Kicad in Spanish.

%package doc-fr
Summary:	Documentation for Kicad in French
Summary(fr.UTF-8):	Documentations pour kicad en français
Group:		Documentation
Requires:	%{name}-doc = %{epoch}:%{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-fr
Documentation and tutorials for Kicad in French.

%package doc-id
Summary:	Documentation for Kicad in Indonesian
Group:		Documentation
Requires:	%{name}-doc = %{epoch}:%{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-id
Documentation and tutorials for Kicad in Indonesian.

%package doc-it
Summary:	Documentation for Kicad in Italian
Summary(fr.UTF-8):	Documentations pour kicad en italien
Group:		Documentation
Requires:	%{name}-doc = %{epoch}:%{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-it
Documentation and tutorials for Kicad in Italian.

%package doc-ja
Summary:	Documentation for Kicad in Japanese
Summary(fr.UTF-8):	Documentations pour kicad en japonais
Group:		Documentation
Requires:	%{name}-doc = %{epoch}:%{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-ja
Documentation and tutorials for Kicad in Japanese.

%package doc-nl
Summary:	Documentation for Kicad in Dutch
Group:		Documentation
Requires:	%{name}-doc = %{epoch}:%{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-nl
Documentation and tutorials for Kicad in Dutch.

%package doc-pl
Summary:	Documentation for Kicad in Polish
Summary(fr.UTF-8):	Documentations pour kicad en polonais
Group:		Documentation
Requires:	%{name}-doc = %{epoch}:%{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-pl
Documentation and tutorials for Kicad in Polish.

%package doc-ru
Summary:	Documentation for Kicad in Russian
Summary(fr.UTF-8):	Documentations pour kicad en russe
Group:		Documentation
Requires:	%{name}-doc = %{epoch}:%{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-ru
Documentation and tutorials for Kicad in Russian.

%package doc-zh
Summary:	Documentation for Kicad in Chinese
Summary(fr.UTF-8):	Documentations pour kicad en chinois
Group:		Documentation
Requires:	%{name}-doc = %{epoch}:%{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-zh
Documentation and tutorials for Kicad in Chinese.

%prep
%setup -q -a 1 -a 2 -a 3 -a 4 -a 5 -a 6
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build

build_library() {
  mkdir "$1/build"
  cd "$1/build"
  %cmake ..
  %{__make} VERBOSE=1
  cd ../..
}
# Symbols libraries
build_library %{name}-symbols-%{version}
build_library %{name}-footprints-%{version}
build_library %{name}-templates-%{version}
build_library %{name}-packages3D-%{version}

# Documentation
mkdir %{name}-doc-%{version}/build
cd %{name}-doc-%{version}/build
%cmake .. \
	-DBUILD_FORMATS=html
%{__make} VERBOSE=1
cd ../..

# Translations
mkdir %{name}-i18n-%{version}/build
cd %{name}-i18n-%{version}/build
%cmake .. \
	-DKICAD_I18N_UNIX_STRICT_PATH=ON
%{__make} VERBOSE=1
cd ../..

# Core components
mkdir build
cd build
%cmake .. \
	-DKICAD_SKIP_BOOST=ON \
	-DKICAD_BUILD_VERSION="%{version}-%{release}" \
	-DwxWidgets_CONFIG_EXECUTABLE=%{_bindir}/wx-gtk2-unicode-config \
	-DKICAD_SCRIPTING=ON -DKICAD_SCRIPTING_MODULES=ON -DKICAD_SCRIPTING_WXPYTHON=ON

%{__make} VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT

install_library() {
  %{__make} -C $1/build install \
	DESTDIR=$RPM_BUILD_ROOT
}

# KiCAD itself
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# Symbols libraries
install_library %{name}-symbols-%{version}
install_library %{name}-footprints-%{version}
install_library %{name}-templates-%{version}
install_library %{name}-packages3D-%{version}

# Documentation
%{__make} -C %{name}-doc-%{version}/build install \
	DESTDIR=$RPM_BUILD_ROOT

# Translations
%{__make} -C %{name}-i18n-%{version}/build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%post
/sbin/ldconfig
%update_mime_database
%update_desktop_database_post
%update_icon_cache hicolor

%postun
/sbin/ldconfig
%update_mime_database
%update_desktop_database_postun
%update_icon_cache hicolor

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS.txt Documentation
%attr(755,root,root) %{_bindir}/bitmap2component
%attr(755,root,root) %{_bindir}/_cvpcb.kiface
%attr(755,root,root) %{_bindir}/dxf2idf
%attr(755,root,root) %{_bindir}/eeschema
%attr(755,root,root) %{_bindir}/_eeschema.kiface
%attr(755,root,root) %{_bindir}/gerbview
%attr(755,root,root) %{_bindir}/_gerbview.kiface
%attr(755,root,root) %{_bindir}/idf2vrml
%attr(755,root,root) %{_bindir}/idfcyl
%attr(755,root,root) %{_bindir}/idfrect
%attr(755,root,root) %{_bindir}/kicad
%attr(755,root,root) %{_bindir}/kicad-ogltest
%attr(755,root,root) %{_bindir}/kicad2step
%attr(755,root,root) %{_bindir}/pcb_calculator
%attr(755,root,root) %{_bindir}/_pcb_calculator.kiface
%attr(755,root,root) %{_bindir}/pcbnew
%attr(755,root,root) %{_bindir}/_pcbnew.kiface
%attr(755,root,root) %{_bindir}/pl_editor
%attr(755,root,root) %{_bindir}/_pl_editor.kiface
%attr(755,root,root) %{_libdir}/libkicad_3dsg.so.*.*.*
%ghost %{_libdir}/libkicad_3dsg.so
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/3d
%attr(755,root,root) %{_libdir}/%{name}/plugins/3d/*.so
#python - to subpackage?
%attr(755,root,root) %{_libdir}/python2.7/site-packages/_pcbnew.so
%{_libdir}/python2.7/site-packages/pcbnew.py
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/demos
%{_datadir}/%{name}/plugins
%{_datadir}/%{name}/scripting
%dir %{_datadir}/%{name}/library
%dir %{_datadir}/%{name}/modules
%dir %{_datadir}/%{name}/modules/packages3d
%dir %{_datadir}/%{name}/template
%{_iconsdir}/hicolor/*x*/*/*.png
%{_iconsdir}/hicolor/scalable/*/*.svg
%{_datadir}/mime/packages/kicad-*.xml
%{_datadir}/appdata/kicad.appdata.xml
%{_desktopdir}/eeschema.desktop
%{_desktopdir}/%{name}.desktop
%{_desktopdir}/bitmap2component.desktop
%{_desktopdir}/gerbview.desktop
%{_desktopdir}/pcbcalculator.desktop
%{_desktopdir}/pcbnew.desktop
#%{_datadir}/mimelnk/application/x-kicad-pcb.desktop
#%{_datadir}/mimelnk/application/x-kicad-project.desktop
#%{_datadir}/mimelnk/application/x-kicad-schematic.desktop

%dir %{_docdir}/%{name}

%files library
%defattr(644,root,root,755)
%{_datadir}/%{name}/library/*
%{_datadir}/%{name}/modules/*.pretty
%{_datadir}/%{name}/template/*

%files packages3D
%defattr(644,root,root,755)
%{_datadir}/%{name}/modules/packages3d/*

%files doc
%defattr(644,root,root,755)
%dir %{_docdir}/%{name}
%dir %{_docdir}/%{name}/help
%{_docdir}/%{name}/help/en
%{_docdir}/%{name}/scripts

%files doc-ca
%defattr(644,root,root,755)
%lang(ca) %{_docdir}/%{name}/help/ca

%files doc-de
%defattr(644,root,root,755)
%lang(de) %{_docdir}/%{name}/help/de

%files doc-es
%defattr(644,root,root,755)
%lang(es) %{_docdir}/%{name}/help/es

%files doc-fr
%defattr(644,root,root,755)
%lang(fr) %{_docdir}/%{name}/help/fr

%files doc-id
%defattr(644,root,root,755)
%lang(id) %{_docdir}/%{name}/help/id

%files doc-it
%defattr(644,root,root,755)
%lang(it) %{_docdir}/%{name}/help/it

%files doc-ja
%defattr(644,root,root,755)
%lang(ja) %{_docdir}/%{name}/help/ja

%files doc-nl
%defattr(644,root,root,755)
%lang(nl) %{_docdir}/%{name}/help/nl

%files doc-pl
%defattr(644,root,root,755)
%lang(pl) %{_docdir}/%{name}/help/pl

%files doc-ru
%defattr(644,root,root,755)
%lang(ru) %{_docdir}/%{name}/help/ru

%files doc-zh
%defattr(644,root,root,755)
%lang(zh) %{_docdir}/%{name}/help/zh
