# TODO:
# - fix mimelnk installation
#
%define	ver	2013.06.11
%define	verlong	20130611
Summary:	KiCad - is a GPL'd suite of programs for EDA
Summary(pl.UTF-8):	KiCad - zestaw programów na licencji GPL zaliczany do kategorii EDA
Name:		kicad
Version:	%{verlong}
Release:	0.1
License:	GPL v2+
Group:		X11/Applications

# Source files created from upstream's bazaar repository
# bzr export -r 4021 kicad-2013.06.11
# bzr export -r 263 kicad-libraries-2013.06.11
# bzr export -r 464 kicad-doc-2013.06.11

Source0:	%{name}-%{ver}.tar.bz2
# Source0-md5:	82ed9a23b9ef332621210eafd08101c2
Source1:	%{name}-doc-%{ver}.tar.bz2
# Source1-md5:	2ef38e351202f80f700a4ae96f898336
Source2:	%{name}-libraries-%{ver}.tar.bz2
# Source2-md5:	5b35e2f2e022fa4be6a03021a6c04493

Source4:	%{name}-2010.05.09.x-kicad-pcbnew.desktop
Source5:	pcbnew.desktop
Source6:	%{name}-icons.tar.bz2
# Source6-md5:	51459cb884444df60e55c95d50564be7
Source7:	Epcos-MKT-1.0.tar.bz2
# Source7-md5:	4dba5eca85fcec9bba491c1815963f80

# Additional librairies from Walter Lain
# http://smisioto.no-ip.org/elettronica/kicad/kicad-en.htm
# kicad-walter-libraries is manually built by downloading all available files

Source8:	%{name}-walter-libraries-%{ver}.tar.bz2
# Source8-md5:	9eba6363258b9efb552222b24b4630f2

Patch0:		%{name}-build.patch
URL:		http://www.kicad-pcb.org/
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.6.4
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	sed >= 4.0
BuildRequires:	which
BuildRequires:	wxGTK2-unicode-gl-devel >= 3.0.0
BuildRequires:	wxWidgets-devel >= 3.0.0
BuildRequires:	zlib-devel
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

%prep
%setup -q -n %{name}-%{ver} -a 1 -a 2 -a 6 -a 7 -a 8
%patch0 -p1

#kicad-doc.noarch: W: file-not-utf8 %{_docdir}/kicad/AUTHORS.txt
iconv -f iso8859-1 -t utf-8 AUTHORS.txt > AUTHORS.conv && mv -f AUTHORS.conv AUTHORS.txt

%if "%{_lib}" != "lib"
	%{__sed} -i -e "s@lib/@%{_lib}/@g" CMakeLists.txt
%endif

%build
# Add Epcos library
cd Epcos-MKT-1.0
cp -pR library ../%{name}-libraries-%{version}/
cp -pR modules ../%{name}-libraries-%{version}/
cd ..

# Add Walter libraries
cd %{name}-walter-libraries-%{ver}
cp -pR library ../%{name}-libraries-%{ver}/
cp -pR modules ../%{name}-libraries-%{ver}/
cd ..

#
# Symbols libraries
#
cd %{name}-libraries-%{ver}
install -d build
cd build
%cmake \
	-DKICAD_STABLE_VERSION=ON \
	..

%{__make} \
	VERBOSE=1
cd ../..

#
# Core components
#
install -d build
cd build
%cmake \
	-DKICAD_STABLE_VERSION=ON \
	-DwxWidgets_USE_STATIC=OFF \
	-DwxWidgets_CONFIG_EXECUTABLE="%{_bindir}/wx-gtk2-unicode-config" \
	-DKICAD_MINIZIP=ON \
	-DKICAD_GOST=ON \
	..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	KICAD_INTERNAT=$RPM_BUILD_ROOT%{_localedir} \
	KICAD_PLUGINS=$RPM_BUILD_ROOT%{_libdir}/%{name}/plugins \
	KICAD_DATA=$RPM_BUILD_ROOT%{_datadir}/%{name} \
	KICAD_DOCS=$RPM_BUILD_ROOT%{_datadir}/%{name}/help \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%{__make} -C %{name}-libraries-%{ver}/build install \
	KICAD_INTERNAT=$RPM_BUILD_ROOT%{_localedir} \
	KICAD_PLUGINS=$RPM_BUILD_ROOT%{_libdir}/%{name}/plugins \
	KICAD_DATA=$RPM_BUILD_ROOT%{_datadir}/%{name} \
	KICAD_DOCS=$RPM_BUILD_ROOT%{_datadir}/%{name}/help \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

# install localization
cd %{name}-doc-%{ver}/internat
for dir in bg ca cs de es fr hu it ko nl pl pt ru sl sv zh_CN
do
  install -m 644 -D ${dir}/%{name}.mo $RPM_BUILD_ROOT%{_localedir}/${dir}/LC_MESSAGES/%{name}.mo
done
cd ../..

# install template
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/template
install template/%{name}.pro $RPM_BUILD_ROOT%{_datadir}/%{name}/template

# install new mime type
install -pm 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/mimelnk/application/x-%{name}-pcbnew.desktop

mv $RPM_BUILD_ROOT%{_datadir}/mimelnk/application/*.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

# install mimetype and application icons
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/32x32/mimetypes/application-x-kicad-eeschema.png \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/mimetypes/application-x-kicad-eeschema.png
install -D -p %{name}-icons/resources/linux/mime/icons/hicolor/32x32/apps/eeschema.png \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/eeschema.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/24x24/mimetypes/application-x-kicad-eeschema.png \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/mimetypes/application-x-kicad-eeschema.png
install -D -p %{name}-icons/resources/linux/mime/icons/hicolor/24x24/apps/eeschema.png \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps/eeschema.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/22x22/mimetypes/application-x-kicad-eeschema.png \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/22x22/mimetypes/application-x-kicad-eeschema.png
install -D -p %{name}-icons/resources/linux/mime/icons/hicolor/22x22/apps/eeschema.png \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/22x22/apps/eeschema.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/16x16/mimetypes/application-x-kicad-eeschema.png \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/mimetypes/application-x-kicad-eeschema.png
install -D -p %{name}-icons/resources/linux/mime/icons/hicolor/16x16/apps/eeschema.png \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/eeschema.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/32x32/mimetypes/application-x-kicad-pcbnew.png \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/mimetypes/application-x-kicad-pcbnew.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/32x32/apps/pcbnew.png \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/pcbnew.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/24x24/mimetypes/application-x-kicad-pcbnew.png \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/mimetypes/application-x-kicad-pcbnew.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/24x24/apps/pcbnew.png \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps/pcbnew.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/22x22/mimetypes/application-x-kicad-pcbnew.png \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/22x22/mimetypes/application-x-kicad-pcbnew.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/22x22/apps/pcbnew.png \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/22x22/apps/pcbnew.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/16x16/mimetypes/application-x-kicad-pcbnew.png \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/mimetypes/application-x-kicad-pcbnew.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/16x16/apps/pcbnew.png \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/pcbnew.png

install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/32x32/apps/kicad.png \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/kicad.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/24x24/apps/kicad.png \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps/kicad.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/22x22/apps/kicad.png \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/22x22/apps/kicad.png
install -pm 644 %{name}-icons/resources/linux/mime/icons/hicolor/16x16/apps/kicad.png \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/kicad.png

# Preparing for documentation pull-ups
%{__rm} -f  %{name}-doc-%{ver}/doc/help/CMakeLists.txt
%{__rm} -f  %{name}-doc-%{ver}/doc/help/makefile
%{__rm} -f  %{name}-doc-%{ver}/doc/tutorials/CMakeLists.txt

%{__cp} -pr %{name}-doc-%{ver}/doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}
%{__cp} -pr AUTHORS.txt CHANGELOG* $RPM_BUILD_ROOT%{_docdir}/%{name}

%find_lang %{name}

%post
%update_mime_database
%update_desktop_database_post
%update_icon_cache hicolor
%update_icon_cache scalable

%postun
%update_mime_database
%update_desktop_database_postun
%update_icon_cache hicolor
%update_icon_cache scalable

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS.txt CHANGELOG.txt Documentation
%attr(755,root,root) %{_bindir}/bitmap2component
%attr(755,root,root) %{_bindir}/cvpcb
%attr(755,root,root) %{_bindir}/eeschema
%attr(755,root,root) %{_bindir}/freeroute.jnlp
%attr(755,root,root) %{_bindir}/gerbview
%attr(755,root,root) %{_bindir}/kicad
%attr(755,root,root) %{_bindir}/pcb_calculator
%attr(755,root,root) %{_bindir}/pcbnew
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/netlist_form_pads-pcb.xsl
%{_datadir}/%{name}
%{_docdir}/%{name}
%{_desktopdir}/eeschema.desktop
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*x*/*/*.png
%{_iconsdir}/hicolor/scalable/*/*.svg
%{_datadir}/mime/packages/kicad.xml
%{_desktopdir}/x-kicad-pcbnew.desktop
%{_desktopdir}/x-kicad-project.desktop
%{_desktopdir}/x-kicad-schematic.desktop
