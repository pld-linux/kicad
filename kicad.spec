%define		_release	r304
Summary:	KiCad - is a GPL'd suite of programs for EDA
Summary(pl.UTF-8):	KiCad jest zestawem programów na licencji GPL zaliczanym do kategorii EDA
Name:		kicad
Version:	20071004
Release:	0.5
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/kicad/%{name}-%{version}-%{_release}.tar.bz2
# Source0-md5:	8ef6310123e9361c5780d321ec07cc8b
URL:		http://kicad.sourceforge.net/
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
- cvpcb - the footprint selector for components used in the circuit
  design.
- pcbnew - the PCB layout program.
- gerbview - the Gerber (photoplotter documents) viewer.

%prep
%setup -q -n %{name}

%build
%{__make} -f makefile.gtk

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
