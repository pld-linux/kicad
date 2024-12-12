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
Version:	8.0.2
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://gitlab.com/kicad/code/kicad/-/archive/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	957ba90492d8bf60f4ff55b3910f1cbd
Source1:	https://gitlab.com/kicad/services/kicad-doc/-/archive/%{version}/%{name}-doc-%{version}.tar.bz2
# Source1-md5:	5c1b5dc997be84b08d59d78a5a9fcd3e
Source3:	https://gitlab.com/kicad/libraries/kicad-symbols/-/archive/%{version}/%{name}-symbols-%{version}.tar.bz2
# Source3-md5:	060c52586965f15b867ee0683aa642ae
Source4:	https://gitlab.com/kicad/libraries/kicad-footprints/-/archive/%{version}/%{name}-footprints-%{version}.tar.bz2
# Source4-md5:	c9537b5ccaa9581ff32d157837a13c38
Source5:	https://gitlab.com/kicad/libraries/kicad-packages3D/-/archive/%{version}/%{name}-packages3D-%{version}.tar.bz2
# Source5-md5:	d6e3242a55c5c28699b50cd4f85e191c
Source6:	https://gitlab.com/kicad/libraries/kicad-templates/-/archive/%{version}/%{name}-templates-%{version}.tar.bz2
# Source6-md5:	20932897d55d49386a1e2431a2aeef5f
Patch0:		libgit2-1.8.patch
URL:		http://www.kicad.org/
BuildRequires:	EGL-devel
BuildRequires:	GLM-devel >= 0.9.9.4
BuildRequires:	OpenCASCADE-devel >= 7.3.0
BuildRequires:	OpenGL-devel
BuildRequires:	appstream-glib
BuildRequires:	asciidoc
BuildRequires:	boost-devel >= 1.71
BuildRequires:	cairo-devel >= 1.12
BuildRequires:	cmake >= 2.6.4
BuildRequires:	curl-devel
BuildRequires:	dblatex
BuildRequires:	desktop-file-utils
BuildRequires:	doxygen
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	gettext-tools
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	harfbuzz-devel
BuildRequires:	libgit2-devel
BuildRequires:	libsecret-devel
BuildRequires:	ngspice-devel
BuildRequires:	openssl-devel
BuildRequires:	perl-Unicode-LineBreak
BuildRequires:	pixman-devel >= 0.30
BuildRequires:	pkgconfig
BuildRequires:	po4a >= 0.51
%if %{with tests}
BuildRequires:	python3-cairosvg
BuildRequires:	python3-pytest
# TODO
#BuildRequires:	python3-pytest-image-diff
%endif
BuildRequires:	python3-devel >= 1:3.6
BuildRequires:	python3-pybind11
BuildRequires:	python3-wxPython-devel
BuildRequires:	rpmbuild(macros) >= 1.742
BuildRequires:	ruby-asciidoctor
BuildRequires:	sed >= 4.0
BuildRequires:	swig >= 4.0
BuildRequires:	unixODBC-devel
BuildRequires:	wayland-devel
BuildRequires:	which
BuildRequires:	wxGTK3-unicode-devel >= 3.2.2
BuildRequires:	wxGTK3-unicode-gl-devel >= 3.2.2
BuildRequires:	wxWidgets-devel >= 3.2.0
BuildRequires:	zlib-devel
Obsoletes:	kicad-doc-hu < 1:4.0.6-1
Obsoletes:	kicad-doc-nl < 1:5.1.0-1
Obsoletes:	kicad-doc-pt < 1:4.0.6-1
Obsoletes:	kicad-doc-zh_CN < 1:4.0.6-1
Obsoletes:	kicad-library < 1:7.0.7
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

%prep
%setup -q -a 1 -a 3 -a 4 %{?with_packages3D:-a 5} -a 6
%patch -P 0 -p1

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
# Use bundled GLEW because GLEW compiled with EGL support is required
# See thirdparty/glew/README.md
%cmake .. \
	-DKICAD_BUILD_VERSION="%{version}-%{release}" \
	-DKICAD_BUILD_I18N=ON \
	-DKICAD_I18N_UNIX_STRICT_PATH=ON \
	-DwxWidgets_CONFIG_EXECUTABLE=%{_bindir}/wx-gtk3-unicode-config \
	-DKICAD_USE_OCC=ON \
	-DKICAD_USE_EGL=ON \
	-DKICAD_USE_BUNDLED_GLEW=ON \
	-DKICAD_SCRIPTING=ON \
	-DKICAD_SCRIPTING_PYTHON3=ON \
	-DKICAD_SCRIPTING_MODULES=ON \
	-DKICAD_SCRIPTING_WXPYTHON=OFF \
	-DKICAD_SCRIPTING_WXPYTHON_PHOENIX=ON \
	%{cmake_on_off tests KICAD_BUILD_QA_TESTS}

%{__make} VERBOSE=1

%if %{with tests}
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
%attr(755,root,root) %{_libdir}/libkicad_3dsg.so.*.*.*
%ghost %{_libdir}/libkicad_3dsg.so
%attr(755,root,root) %{_libdir}/libkicommon.so.*.*.*
%ghost %{_libdir}/libkicommon.so
%attr(755,root,root) %{_libdir}/libkigal.so.*.*.*
%ghost %{_libdir}/libkigal.so
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/3d
%attr(755,root,root) %{_libdir}/%{name}/plugins/3d/*.so
#python - to subpackage?
%attr(755,root,root) %{py3_sitedir}/_pcbnew.so
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
