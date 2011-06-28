%define	libver 1.0
%define	docver 1.1
Summary:	KiCad - is a GPL'd suite of programs for EDA
Summary(pl.UTF-8):	KiCad - zestaw programów na licencji GPL zaliczany do kategorii EDA
Name:		kicad
Version:	20110429
Release:	0.1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://iut-tice.ujf-grenoble.fr/cao/%{name}-sources_2011-04-29-BZR2986.zip
# Source0-md5:	e5d5311ad8a6387b1e96a9ee63088238
Source1:	http://downloads.sourceforge.net/kicad/%{name}-library-%{libver}.tar.bz2
# Source1-md5:	9c91940aa5f5563bb86c52ff07e8f99a
Source2:	http://downloads.sourceforge.net/kicad/%{name}-doc-%{docver}.tar.bz2
# Source2-md5:	fcfbc94f675a19db51370e97b88803b1
Source3:	%{name}.desktop
URL:		http://kicad.sourceforge.net/
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.6.4
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	sed >= 4.0
BuildRequires:	which
BuildRequires:	wxGTK2-unicode-gl-devel >= 2.8.11
BuildRequires:	wxWidgets-devel >= 2.8.11
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
%setup -q  -n %{name}_sources

%build
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

install -d $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

#for loc in $RPM_BUILD_ROOT%{_localedir}/*; do
#	install -d $loc/LC_MESSAGES
#	mv $loc/*.mo $loc/LC_MESSAGES
#done

for loc in $RPM_BUILD_ROOT%{_datadir}/%{name}/help/*; do
	rm -rf $loc/docs_src
done

#%%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

#%%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%doc AUTHORS.txt CHANGELOG.txt Documentation
%attr(755,root,root) %{_bindir}/cvpcb
%attr(755,root,root) %{_bindir}/eeschema
%attr(755,root,root) %{_bindir}/gerbview
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
#%%attr(755,root,root) %{_libdir}/%{name}/plugins/netlist_form_pads-pcb
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
