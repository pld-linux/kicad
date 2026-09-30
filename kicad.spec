# TODO:
# - fix mimelnk installation
#
# Conditional build:
%bcond_without	packages3D	# do not build packages3D
%bcond_without	tests		# unit tests

%ifarch %{ix86}
%undefine	with_tests
%endif

Summary:	KiCad - is a GPL'd suite of programs for EDA
Summary(pl.UTF-8):	KiCad - zestaw programów na licencji GPL zaliczany do kategorii EDA
Name:		kicad
Version:	10.0.6
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://gitlab.com/kicad/code/kicad/-/archive/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	e4384c57bd078613160fbe2a662893fd
Source1:	https://gitlab.com/kicad/services/kicad-doc/-/archive/%{version}/%{name}-doc-%{version}.tar.bz2
# Source1-md5:	672bb67b5714e4802fa215ac3bab0aa1
Source3:	https://gitlab.com/kicad/libraries/kicad-symbols/-/archive/%{version}/%{name}-symbols-%{version}.tar.bz2
# Source3-md5:	8bc2d351ae26bdb181f29ef6afd14c1d
Source4:	https://gitlab.com/kicad/libraries/kicad-footprints/-/archive/%{version}/%{name}-footprints-%{version}.tar.bz2
# Source4-md5:	71a50e7b5ae2b130c99547da91c7265d
Source5:	https://gitlab.com/kicad/libraries/kicad-packages3D/-/archive/%{version}/%{name}-packages3D-%{version}.tar.bz2
# Source5-md5:	c742ab45edabcd37678f122187b0d9dd
Source6:	https://gitlab.com/kicad/libraries/kicad-templates/-/archive/%{version}/%{name}-templates-%{version}.tar.bz2
# Source6-md5:	073f47ee9b9c24b3afe93d38efcefe56
URL:		http://www.kicad.org/
BuildRequires:	GLM-devel >= 0.9.9.4
BuildRequires:	OpenCASCADE-devel >= 7.5.0
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	boost-devel >= 1.71
BuildRequires:	cairo-devel >= 1.12
BuildRequires:	cmake >= 3.22
BuildRequires:	curl-devel
BuildRequires:	doxygen
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 1:2.11.1
BuildRequires:	gettext-tools
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	harfbuzz-devel
BuildRequires:	libgit2-devel >= 1.5
BuildRequires:	libsecret-devel
BuildRequires:	libspnav-devel
BuildRequires:	ngspice-devel
BuildRequires:	nng-devel
BuildRequires:	perl-Unicode-LineBreak
BuildRequires:	pixman-devel >= 0.30
BuildRequires:	pkgconfig
BuildRequires:	po4a >= 0.51
BuildRequires:	poppler-glib-devel
BuildRequires:	protobuf-devel
%if %{with tests}
BuildRequires:	python3-cairosvg
BuildRequires:	python3-numpy
BuildRequires:	python3-pillow
BuildRequires:	python3-pytest
%endif
BuildRequires:	python3-devel >= 1:3.6
BuildRequires:	python3-wxPython-devel
BuildRequires:	rpmbuild(macros) >= 1.742
BuildRequires:	ruby-asciidoctor
BuildRequires:	sed >= 4.0
BuildRequires:	swig >= 4.0
BuildRequires:	unixODBC-devel
BuildRequires:	wayland-devel >= 1.20
BuildRequires:	which
BuildRequires:	wxGTK3-unicode-devel >= 3.2.2
BuildRequires:	wxGTK3-unicode-gl-devel >= 3.2.2
BuildRequires:	wxWidgets-devel >= 3.2.0
BuildRequires:	zlib-devel
BuildRequires:	zstd-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	shared-mime-info
Requires:	hicolor-icon-theme
# libngspice.so.0 is dlopened by the simulator
Requires:	ngspice-libs
Requires:	python3-wxPython
Obsoletes:	kicad-doc-hu < 1:4.0.6-1
Obsoletes:	kicad-doc-nl < 1:5.1.0-1
Obsoletes:	kicad-doc-pt < 1:4.0.6-1
Obsoletes:	kicad-doc-zh_CN < 1:4.0.6-1
Obsoletes:	kicad-library < 1:7.0.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# TLS symbol _ZN6google8protobuf8internal15ThreadSafeArena13thread_cache_E comes from
# libprotobuf (DT_NEEDED, ldd -r clean); the checker misreads undefined TLS objects
%define		skip_post_check_so	libkiapi.so.*

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

%package packages3D
Summary:	Packages3D for kicad
Summary(pl.UTF-8):	Trójwymiarowe modele obudów dla kicad
Requires:	kicad >= 1:5.0.0
BuildArch:	noarch

%description packages3D
Packages3D for kicad

%description packages3D -l pl.UTF-8
Trójwymiarowe modele obudów dla kicad.

%package doc
Summary:	Documentation for kicad
Summary(fr.UTF-8):	Documentations pour kicad en anglais
License:	GPL v2+
Group:		Documentation
BuildArch:	noarch

%description doc
Documentation and tutorials for kicad in English

%package doc-ca
Summary:	Documentation for Kicad in Catalan
Group:		Documentation
Requires:	%{name}-doc = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description doc-ca
Documentation and tutorials for Kicad in Catalan.

%package doc-de
Summary:	Documentation for Kicad in German
Summary(fr.UTF-8):	Documentations pour kicad en allemand
Group:		Documentation
Requires:	%{name}-doc = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description doc-de
Documentation and tutorials for Kicad in German.

%package doc-es
Summary:	Documentation for Kicad in Spanish
Summary(fr.UTF-8):	Documentations pour kicad en espagnol
Group:		Documentation
Requires:	%{name}-doc = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description doc-es
Documentation and tutorials for Kicad in Spanish.

%package doc-fr
Summary:	Documentation for Kicad in French
Summary(fr.UTF-8):	Documentations pour kicad en français
Group:		Documentation
Requires:	%{name}-doc = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description doc-fr
Documentation and tutorials for Kicad in French.

%package doc-id
Summary:	Documentation for Kicad in Indonesian
Group:		Documentation
Requires:	%{name}-doc = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description doc-id
Documentation and tutorials for Kicad in Indonesian.

%package doc-it
Summary:	Documentation for Kicad in Italian
Summary(fr.UTF-8):	Documentations pour kicad en italien
Group:		Documentation
Requires:	%{name}-doc = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description doc-it
Documentation and tutorials for Kicad in Italian.

%package doc-ja
Summary:	Documentation for Kicad in Japanese
Summary(fr.UTF-8):	Documentations pour kicad en japonais
Group:		Documentation
Requires:	%{name}-doc = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description doc-ja
Documentation and tutorials for Kicad in Japanese.

%package doc-pl
Summary:	Documentation for Kicad in Polish
Summary(fr.UTF-8):	Documentations pour kicad en polonais
Group:		Documentation
Requires:	%{name}-doc = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description doc-pl
Documentation and tutorials for Kicad in Polish.

%package doc-ru
Summary:	Documentation for Kicad in Russian
Summary(fr.UTF-8):	Documentations pour kicad en russe
Group:		Documentation
Requires:	%{name}-doc = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description doc-ru
Documentation and tutorials for Kicad in Russian.

%package doc-zh
Summary:	Documentation for Kicad in Chinese
Summary(fr.UTF-8):	Documentations pour kicad en chinois
Group:		Documentation
Requires:	%{name}-doc = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description doc-zh
Documentation and tutorials for Kicad in Chinese.

%package -n bash-completion-%{name}
Summary:	Bash completion for kicad-cli command
Summary(pl.UTF-8):	Bashowe uzupełnianie nazw dla polecenia kicad-cli
Group:		Applications/Shells
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	bash-completion >= 1:2.0
BuildArch:	noarch

%description -n bash-completion-%{name}
Bash completion for kicad-cli command.

%description -n bash-completion-%{name} -l pl.UTF-8
Bashowe uzupełnianie nazw dla polecenia kicad-cli.

%package -n zsh-completion-%{name}
Summary:	zsh completion for kicad-cli command
Summary(pl.UTF-8):	Uzupełnianie nazw w zsh dla polecenia kicad-cli
Group:		Applications/Shells
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	zsh
BuildArch:	noarch

%description -n zsh-completion-%{name}
zsh completion for kicad-cli command.

%description -n zsh-completion-%{name} -l pl.UTF-8
Uzupełnianie nazw w zsh dla polecenia kicad-cli.

%prep
%setup -q -a 1 -a 3 -a 4 %{?with_packages3D:-a 5} -a 6

%ifarch x32
# fails on x32
%{__sed} -i -e '/test_coroutine.cpp/d' qa/tests/common/CMakeLists.txt
%endif

%build

build_library() {
	mkdir -p "$1/build"
	cd "$1/build"
	%cmake ..
	%{__make} VERBOSE=1
	cd ../..
}
# Symbols libraries
build_library %{name}-symbols-%{version}
build_library %{name}-footprints-%{version}
build_library %{name}-templates-%{version}
%if %{with packages3D}
build_library %{name}-packages3D-%{version}
%endif

# Documentation
mkdir -p %{name}-doc-%{version}/build
cd %{name}-doc-%{version}/build
%cmake .. \
	-DBUILD_FORMATS=html
%{__make} VERBOSE=1
cd ../..

# Core components
mkdir -p build
cd build
%cmake .. \
	-DKICAD_BUILD_VERSION="%{version}-%{release}" \
	-DKICAD_BUILD_I18N=ON \
	-DKICAD_I18N_UNIX_STRICT_PATH=ON \
	-DwxWidgets_CONFIG_EXECUTABLE=%{_bindir}/wx-gtk3-unicode-config \
	-DKICAD_IPC_API=ON \
	-DKICAD_SCRIPTING_WXPYTHON=ON \
	-DKICAD_UPDATE_CHECK=OFF \
	%{cmake_on_off tests KICAD_BUILD_QA_TESTS}

%{__make} VERBOSE=1

%if %{with tests}
# keep user config, caches and temporary files inside the build tree
export HOME=$(pwd)/tests-home
export TMPDIR=$(pwd)/tests-tmp
unset XDG_CACHE_HOME XDG_CONFIG_HOME XDG_DATA_HOME XDG_STATE_HOME
install -d $HOME $TMPDIR
# PLD wxWidgets is built with wxDEBUG_LEVEL=0, these cases expect wxCHECK to raise an assert
export BOOST_TEST_RUN_FILTERS='!ApiEnums/KiCadObjectType:!ApiEnums/ElectricalPinType:!ApiEnums/ViaType'
# reference qa/data/cli/basic_test/basic_test.erc.json carries a hardcoded kicad_version
export PYTEST_ADDOPTS="-k 'not (test_sch_export_erc and json)'"
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__make} test ARGS=--output-on-failure
%endif

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
%if %{with packages3D}
install_library %{name}-packages3D-%{version}
%endif

# Documentation
%{__make} -C %{name}-doc-%{version}/build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{no,nb}

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
%doc AUTHORS.txt README.md
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
%attr(755,root,root) %{_bindir}/kicad-cli
%attr(755,root,root) %{_bindir}/_kipython.kiface
%attr(755,root,root) %{_bindir}/pcb_calculator
%attr(755,root,root) %{_bindir}/_pcb_calculator.kiface
%attr(755,root,root) %{_bindir}/pcbnew
%attr(755,root,root) %{_bindir}/_pcbnew.kiface
%attr(755,root,root) %{_bindir}/pl_editor
%attr(755,root,root) %{_bindir}/_pl_editor.kiface
%{_libdir}/libkiapi.so.*.*.*
%ghost %{_libdir}/libkiapi.so
%{_libdir}/libkicad_3dsg.so.*.*.*
%ghost %{_libdir}/libkicad_3dsg.so
%{_libdir}/libkicommon.so.*.*.*
%ghost %{_libdir}/libkicommon.so
%{_libdir}/libkigal.so.*.*.*
%ghost %{_libdir}/libkigal.so
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/3d
%attr(755,root,root) %{_libdir}/%{name}/plugins/3d/*.so
#python - to subpackage?
%{py3_sitedir}/_pcbnew.so
%{py3_sitedir}/pcbnew.py
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/demos
%{_datadir}/%{name}/footprints
%{_datadir}/%{name}/plugins
%{_datadir}/%{name}/resources
%{_datadir}/%{name}/schemas
%{_datadir}/%{name}/scripting
%{_datadir}/%{name}/symbols
%{_datadir}/%{name}/template
%{_iconsdir}/hicolor/*x*/*/*.png
%{_iconsdir}/hicolor/scalable/*/*.svg
%{_datadir}/mime/packages/kicad-*.xml
%{_metainfodir}/org.kicad.kicad.metainfo.xml
%{_desktopdir}/org.kicad.eeschema.desktop
%{_desktopdir}/org.kicad.kicad.desktop
%{_desktopdir}/org.kicad.bitmap2component.desktop
%{_desktopdir}/org.kicad.gerbview.desktop
%{_desktopdir}/org.kicad.pcbcalculator.desktop
%{_desktopdir}/org.kicad.pcbnew.desktop
#%{_datadir}/mimelnk/application/x-kicad-pcb.desktop
#%{_datadir}/mimelnk/application/x-kicad-project.desktop
#%{_datadir}/mimelnk/application/x-kicad-schematic.desktop

%dir %{_docdir}/%{name}

%if %{with packages3D}
%files packages3D
%defattr(644,root,root,755)
%{_datadir}/%{name}/3dmodels
%endif

%files doc
%defattr(644,root,root,755)
%dir %{_docdir}/%{name}
%dir %{_docdir}/%{name}/help
%{_docdir}/%{name}/help/en

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

%files doc-pl
%defattr(644,root,root,755)
%lang(pl) %{_docdir}/%{name}/help/pl

%files doc-ru
%defattr(644,root,root,755)
%lang(ru) %{_docdir}/%{name}/help/ru

%files doc-zh
%defattr(644,root,root,755)
%lang(zh) %{_docdir}/%{name}/help/zh

%files -n bash-completion-%{name}
%defattr(644,root,root,755)
%{bash_compdir}/kicad-cli

%files -n zsh-completion-%{name}
%defattr(644,root,root,755)
%{zsh_compdir}/_kicad-cli
