# TODO:
# - fix mimelnk installation
#
Summary:	KiCad - is a GPL'd suite of programs for EDA
Summary(pl.UTF-8):	KiCad - zestaw programów na licencji GPL zaliczany do kategorii EDA
Name:		kicad
Version:	4.0.6
Release:	0.1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://launchpad.net/kicad/4.0/%{version}/+download/%{name}-%{version}.tar.xz
# Source0-md5:	24eca1f22bbb0a88acbba321a4b1c4aa
Source1:	https://github.com/KiCad/kicad-doc/archive/%{version}/%{name}-doc-%{version}.tar.gz
# Source1-md5:	f68105a04132fc8a4412d75ffe0d0b16
Source2:	https://github.com/KiCad/kicad-library/archive/%{version}/%{name}-library-%{version}.tar.gz
# Source2-md5:	325ca078191584cd063835e01ecabd67
Source3:	https://github.com/KiCad/kicad-i18n/archive/%{version}/%{name}-i18n-%{version}.tar.gz
# Source3-md5:	6680338a8b23e7d651bb30cbba04e2b3
# perl -ne 'BEGIN {$s=4} /uri \$\{KIGITHUB}\/([^)]*)/ and printf "%-16shttps://github.com/KiCad/$1/archive/%{version}/$1-%{version}.tar.gz#/$1-%{version}.tar.gz\n", "Source".$s++.":"' \
# kicad-*/kicad-library-*/template/fp-lib-table.for-github
Source4:	https://github.com/KiCad/Air_Coils_SML_NEOSID.pretty/archive/%{version}/Air_Coils_SML_NEOSID.pretty-%{version}.tar.gz
# Source4-md5:	e343fb1de9debbfca640879433964bf5
Source5:	https://github.com/KiCad/Buttons_Switches_SMD.pretty/archive/%{version}/Buttons_Switches_SMD.pretty-%{version}.tar.gz
# Source5-md5:	4d3bd10d0d7c29dd03e91f3ee999a4cf
Source6:	https://github.com/KiCad/Buttons_Switches_THT.pretty/archive/%{version}/Buttons_Switches_THT.pretty-%{version}.tar.gz
# Source6-md5:	8e83e77abd4a2699cabcf10ca2452a37
Source7:	https://github.com/KiCad/Buzzers_Beepers.pretty/archive/%{version}/Buzzers_Beepers.pretty-%{version}.tar.gz
# Source7-md5:	0be5ca79b86e23022b9ce5947fce4657
Source8:	https://github.com/KiCad/Capacitors_SMD.pretty/archive/%{version}/Capacitors_SMD.pretty-%{version}.tar.gz
# Source8-md5:	a132bacf9268f67caa9c504398b485f6
Source9:	https://github.com/KiCad/Capacitors_Tantalum_SMD.pretty/archive/%{version}/Capacitors_Tantalum_SMD.pretty-%{version}.tar.gz
# Source9-md5:	591a022e35a0d4eb3338e36cbfc2b111
Source10:	https://github.com/KiCad/Capacitors_THT.pretty/archive/%{version}/Capacitors_THT.pretty-%{version}.tar.gz
# Source10-md5:	d2b3ec61381efeda3787c306a5f20c4d
Source11:	https://github.com/KiCad/Choke_Axial_ThroughHole.pretty/archive/%{version}/Choke_Axial_ThroughHole.pretty-%{version}.tar.gz
# Source11-md5:	9e5ac090fc1d5a8145c93c6846d1242d
Source12:	https://github.com/KiCad/Choke_Common-Mode_Wurth.pretty/archive/%{version}/Choke_Common-Mode_Wurth.pretty-%{version}.tar.gz
# Source12-md5:	1b1b159c5f598cc0487b39fbfdc854ad
Source13:	https://github.com/KiCad/Choke_Radial_ThroughHole.pretty/archive/%{version}/Choke_Radial_ThroughHole.pretty-%{version}.tar.gz
# Source13-md5:	d90b7adb66b4f8535667875cb10f4fba
Source14:	https://github.com/KiCad/Choke_SMD.pretty/archive/%{version}/Choke_SMD.pretty-%{version}.tar.gz
# Source14-md5:	ffbbec04a597c3f8313df6d52020d7a7
Source15:	https://github.com/KiCad/Choke_Toroid_ThroughHole.pretty/archive/%{version}/Choke_Toroid_ThroughHole.pretty-%{version}.tar.gz
# Source15-md5:	4bdf6343c75887d67dc80e69b8e080ba
Source16:	https://github.com/KiCad/Connectors_Harwin.pretty/archive/%{version}/Connectors_Harwin.pretty-%{version}.tar.gz
# Source16-md5:	c103d987a87bde089155421af2216c93
Source17:	https://github.com/KiCad/Connectors_Hirose.pretty/archive/%{version}/Connectors_Hirose.pretty-%{version}.tar.gz
# Source17-md5:	8d10a6d792b1a1b55459494d0374326f
Source18:	https://github.com/KiCad/Connectors_JAE.pretty/archive/%{version}/Connectors_JAE.pretty-%{version}.tar.gz
# Source18-md5:	08db63855dc67995ed483a58af85f9f7
Source19:	https://github.com/KiCad/Connectors_JST.pretty/archive/%{version}/Connectors_JST.pretty-%{version}.tar.gz
# Source19-md5:	5ce5e2bac3bf25bbeb98a4dd33632609
Source20:	https://github.com/KiCad/Connectors_Mini-Universal.pretty/archive/%{version}/Connectors_Mini-Universal.pretty-%{version}.tar.gz
# Source20-md5:	9977b9592e4789c9b1b20ab26fe301a6
Source21:	https://github.com/KiCad/Connectors_Molex.pretty/archive/%{version}/Connectors_Molex.pretty-%{version}.tar.gz
# Source21-md5:	ef7d14f881e09be9a882b0e71f4474c7
Source22:	https://github.com/KiCad/Connectors_Multicomp.pretty/archive/%{version}/Connectors_Multicomp.pretty-%{version}.tar.gz
# Source22-md5:	951ba83ee8f34e51465c75d38c246ce8
Source23:	https://github.com/KiCad/Connectors_Phoenix.pretty/archive/%{version}/Connectors_Phoenix.pretty-%{version}.tar.gz
# Source23-md5:	7d9a232d0cd195f9d2b9ed82010c2ffe
Source24:	https://github.com/KiCad/Connectors_Samtec.pretty/archive/%{version}/Connectors_Samtec.pretty-%{version}.tar.gz
# Source24-md5:	b2610848de6e1c91b2c8d30d9cd518d5
Source25:	https://github.com/KiCad/Connectors_TE-Connectivity.pretty/archive/%{version}/Connectors_TE-Connectivity.pretty-%{version}.tar.gz
# Source25-md5:	43e70e5d21e1119f8981eed40d082a8f
Source26:	https://github.com/KiCad/Connectors_Terminal_Blocks.pretty/archive/%{version}/Connectors_Terminal_Blocks.pretty-%{version}.tar.gz
# Source26-md5:	cbb75de29fe23cab12519de5c314d738
Source27:	https://github.com/KiCad/Connectors_WAGO.pretty/archive/%{version}/Connectors_WAGO.pretty-%{version}.tar.gz
# Source27-md5:	219367a04e3917ba84a61341b9a5d939
Source28:	https://github.com/KiCad/Connectors.pretty/archive/%{version}/Connectors.pretty-%{version}.tar.gz
# Source28-md5:	53358aaf6319b4963df7ed988985a13a
Source29:	https://github.com/KiCad/Converters_DCDC_ACDC.pretty/archive/%{version}/Converters_DCDC_ACDC.pretty-%{version}.tar.gz
# Source29-md5:	8876b6ace69520adc78dd752ea872fcb
Source30:	https://github.com/KiCad/Crystals.pretty/archive/%{version}/Crystals.pretty-%{version}.tar.gz
# Source30-md5:	3d156ccfcc43216f96ecfa7c3f8345b8
Source31:	https://github.com/KiCad/Diodes_SMD.pretty/archive/%{version}/Diodes_SMD.pretty-%{version}.tar.gz
# Source31-md5:	bea39235640355298ea6f14332627a18
Source32:	https://github.com/KiCad/Diodes_THT.pretty/archive/%{version}/Diodes_THT.pretty-%{version}.tar.gz
# Source32-md5:	ec77db0c94cfae709d145bcad133ed4f
Source33:	https://github.com/KiCad/Discret.pretty/archive/%{version}/Discret.pretty-%{version}.tar.gz
# Source33-md5:	49598b208de48dd7ec87586950348112
Source34:	https://github.com/KiCad/Displays_7-Segment.pretty/archive/%{version}/Displays_7-Segment.pretty-%{version}.tar.gz
# Source34-md5:	7f05ebc80504e122961ea020b42e8c3c
Source35:	https://github.com/KiCad/Displays.pretty/archive/%{version}/Displays.pretty-%{version}.tar.gz
# Source35-md5:	fae3bd280525583ab8669c3b2f48e4a7
Source36:	https://github.com/KiCad/Divers.pretty/archive/%{version}/Divers.pretty-%{version}.tar.gz
# Source36-md5:	87a7ea52f622289d4486e5c4f9f4f308
Source37:	https://github.com/KiCad/Enclosures.pretty/archive/%{version}/Enclosures.pretty-%{version}.tar.gz
# Source37-md5:	af7c0066f10c3c449c36b23559ffddf0
Source38:	https://github.com/KiCad/EuroBoard_Outline.pretty/archive/%{version}/EuroBoard_Outline.pretty-%{version}.tar.gz
# Source38-md5:	305424a4e6b51de49856e3cb12b5eedb
Source39:	https://github.com/KiCad/Fiducials.pretty/archive/%{version}/Fiducials.pretty-%{version}.tar.gz
# Source39-md5:	45c7652cfbd5e2aba589e7e594f2f401
Source40:	https://github.com/KiCad/Filters_HF_Coils_NEOSID.pretty/archive/%{version}/Filters_HF_Coils_NEOSID.pretty-%{version}.tar.gz
# Source40-md5:	52bb487182bd6a1a2245f8076259c328
Source41:	https://github.com/KiCad/Fuse_Holders_and_Fuses.pretty/archive/%{version}/Fuse_Holders_and_Fuses.pretty-%{version}.tar.gz
# Source41-md5:	cadfa005debdfc7d0c469ef48b8d26d0
Source42:	https://github.com/KiCad/Hall-Effect_Transducers_LEM.pretty/archive/%{version}/Hall-Effect_Transducers_LEM.pretty-%{version}.tar.gz
# Source42-md5:	ebb9c1b12d906f0e69376fe3fa4e5ee7
Source43:	https://github.com/KiCad/Heatsinks.pretty/archive/%{version}/Heatsinks.pretty-%{version}.tar.gz
# Source43-md5:	4a7696b52a217c1af3d76310cefc9276
Source44:	https://github.com/KiCad/Housings_BGA.pretty/archive/%{version}/Housings_BGA.pretty-%{version}.tar.gz
# Source44-md5:	1a52287e9101f75ea0a013c8896ea5ad
Source45:	https://github.com/KiCad/Housings_DFN_QFN.pretty/archive/%{version}/Housings_DFN_QFN.pretty-%{version}.tar.gz
# Source45-md5:	bfca29af9ec269b811e95f5a12d49327
Source46:	https://github.com/KiCad/Housings_DIP.pretty/archive/%{version}/Housings_DIP.pretty-%{version}.tar.gz
# Source46-md5:	806e69140a65217b6124c0c0649d6474
Source47:	https://github.com/KiCad/Housings_LCC.pretty/archive/%{version}/Housings_LCC.pretty-%{version}.tar.gz
# Source47-md5:	79a0b216aa186eab822b45fb2ab48b81
Source48:	https://github.com/KiCad/Housings_LGA.pretty/archive/%{version}/Housings_LGA.pretty-%{version}.tar.gz
# Source48-md5:	0e3ef9347f68ab03fd9e4960ef652f6c
Source49:	https://github.com/KiCad/Housings_PGA.pretty/archive/%{version}/Housings_PGA.pretty-%{version}.tar.gz
# Source49-md5:	e008414845d6d1928a4607b2511a7fed
Source50:	https://github.com/KiCad/Housings_QFP.pretty/archive/%{version}/Housings_QFP.pretty-%{version}.tar.gz
# Source50-md5:	36ff18521539dcc036a421af4a3eeea1
Source51:	https://github.com/KiCad/Housings_SIP.pretty/archive/%{version}/Housings_SIP.pretty-%{version}.tar.gz
# Source51-md5:	5d5d071ba919c686fee70c1fe33360d7
Source52:	https://github.com/KiCad/Housings_SOIC.pretty/archive/%{version}/Housings_SOIC.pretty-%{version}.tar.gz
# Source52-md5:	6cf7b9bf4f6fba01c3bef5d4b81b7b01
Source53:	https://github.com/KiCad/Housings_SSOP.pretty/archive/%{version}/Housings_SSOP.pretty-%{version}.tar.gz
# Source53-md5:	462ad43dc28523cbd148f661aac26190
Source54:	https://github.com/KiCad/Inductors_NEOSID.pretty/archive/%{version}/Inductors_NEOSID.pretty-%{version}.tar.gz
# Source54-md5:	6fc983a43dccd17739d3cefa637a6005
Source55:	https://github.com/KiCad/Inductors.pretty/archive/%{version}/Inductors.pretty-%{version}.tar.gz
# Source55-md5:	99cfe2b7fcbfa170259c5ad94694ffee
Source56:	https://github.com/KiCad/Inductors_SMD.pretty/archive/%{version}/Inductors_SMD.pretty-%{version}.tar.gz
# Source56-md5:	6e2e634595a9f0bcb8a1ba9c884fee5f
Source57:	https://github.com/KiCad/Inductors_THT.pretty/archive/%{version}/Inductors_THT.pretty-%{version}.tar.gz
# Source57-md5:	ed47a1aed878619170cb2d104bf34992
Source58:	https://github.com/KiCad/IR-DirectFETs.pretty/archive/%{version}/IR-DirectFETs.pretty-%{version}.tar.gz
# Source58-md5:	baad0378907a45ce847e7c53d9d0fc36
Source59:	https://github.com/KiCad/Labels.pretty/archive/%{version}/Labels.pretty-%{version}.tar.gz
# Source59-md5:	e094fa074bd2252fa99e92021c1e3c3d
Source60:	https://github.com/KiCad/LEDs.pretty/archive/%{version}/LEDs.pretty-%{version}.tar.gz
# Source60-md5:	f40658749082dbb8f2b123dc3d8b9e6b
Source61:	https://github.com/KiCad/Measurement_Points.pretty/archive/%{version}/Measurement_Points.pretty-%{version}.tar.gz
# Source61-md5:	be7400d113165b932c38a83d0e1a81c6
Source62:	https://github.com/KiCad/Measurement_Scales.pretty/archive/%{version}/Measurement_Scales.pretty-%{version}.tar.gz
# Source62-md5:	f1d2226dcb04a6bbd83aba8b701d9df0
Source63:	https://github.com/KiCad/Mechanical_Sockets.pretty/archive/%{version}/Mechanical_Sockets.pretty-%{version}.tar.gz
# Source63-md5:	904a2beaf0b3cd03465aa50b22577f3f
Source64:	https://github.com/KiCad/Microwave.pretty/archive/%{version}/Microwave.pretty-%{version}.tar.gz
# Source64-md5:	c370a2b3cf5b284f98e6b264f0818726
Source65:	https://github.com/KiCad/Modules.pretty/archive/%{version}/Modules.pretty-%{version}.tar.gz
# Source65-md5:	4a501a24a6355fe814a884b94d162b22
Source66:	https://github.com/KiCad/Mounting_Holes.pretty/archive/%{version}/Mounting_Holes.pretty-%{version}.tar.gz
# Source66-md5:	7cc6b71a4e1f4c15db62fa8ba1c97d37
Source67:	https://github.com/KiCad/NF-Transformers_ETAL.pretty/archive/%{version}/NF-Transformers_ETAL.pretty-%{version}.tar.gz
# Source67-md5:	819b22b813b3fb7d09125cb4c3f05639
Source68:	https://github.com/KiCad/Oddities.pretty/archive/%{version}/Oddities.pretty-%{version}.tar.gz
# Source68-md5:	a93fa061e420ea397efa790f01e2a462
Source69:	https://github.com/KiCad/Opto-Devices.pretty/archive/%{version}/Opto-Devices.pretty-%{version}.tar.gz
# Source69-md5:	e5de89a96ca7bbabc3f1c82df09d2f90
Source70:	https://github.com/KiCad/Oscillators.pretty/archive/%{version}/Oscillators.pretty-%{version}.tar.gz
# Source70-md5:	8e38ea216c960a56fad2a32ab491bff7
Source71:	https://github.com/KiCad/PFF_PSF_PSS_Leadforms.pretty/archive/%{version}/PFF_PSF_PSS_Leadforms.pretty-%{version}.tar.gz
# Source71-md5:	597792f8c3b5a9e12902d597ea1fc132
Source72:	https://github.com/KiCad/Pin_Headers.pretty/archive/%{version}/Pin_Headers.pretty-%{version}.tar.gz
# Source72-md5:	5130d2e64fb526b5e037b9c04499a098
Source73:	https://github.com/KiCad/Potentiometers.pretty/archive/%{version}/Potentiometers.pretty-%{version}.tar.gz
# Source73-md5:	3db69082756229d2ec4c3a50848ffd28
Source74:	https://github.com/KiCad/Power_Integrations.pretty/archive/%{version}/Power_Integrations.pretty-%{version}.tar.gz
# Source74-md5:	ddbcc3767e163fe5789454de8735ba80
Source75:	https://github.com/KiCad/Relays_THT.pretty/archive/%{version}/Relays_THT.pretty-%{version}.tar.gz
# Source75-md5:	51494d7db9eabccea483c7f4c5d17f50
Source76:	https://github.com/KiCad/Resistors_SMD.pretty/archive/%{version}/Resistors_SMD.pretty-%{version}.tar.gz
# Source76-md5:	32f760a5bd68397bf7d8bfb2622b7038
Source77:	https://github.com/KiCad/Resistors_THT.pretty/archive/%{version}/Resistors_THT.pretty-%{version}.tar.gz
# Source77-md5:	7f3e3a656b94b4ec3ad59f841f8e1149
Source78:	https://github.com/KiCad/Resistors_Universal.pretty/archive/%{version}/Resistors_Universal.pretty-%{version}.tar.gz
# Source78-md5:	c35311f20f8c816244000b4d85fb6e8f
Source79:	https://github.com/KiCad/RF_Modules.pretty/archive/%{version}/RF_Modules.pretty-%{version}.tar.gz
# Source79-md5:	22df000a3a8fb16f9306015f2decea6a
Source80:	https://github.com/KiCad/Shielding_Cabinets.pretty/archive/%{version}/Shielding_Cabinets.pretty-%{version}.tar.gz
# Source80-md5:	7afa82ede121a46158d30a848002947d
Source81:	https://github.com/KiCad/SMD_Packages.pretty/archive/%{version}/SMD_Packages.pretty-%{version}.tar.gz
# Source81-md5:	ee99961ab96b360a446a5790c184a129
Source82:	https://github.com/KiCad/Sockets_MOLEX_KK-System.pretty/archive/%{version}/Sockets_MOLEX_KK-System.pretty-%{version}.tar.gz
# Source82-md5:	9c5f6f092156c138856e819cd245cb43
Source83:	https://github.com/KiCad/Socket_Strips.pretty/archive/%{version}/Socket_Strips.pretty-%{version}.tar.gz
# Source83-md5:	7ab96152fe961849944936e69671f99b
Source84:	https://github.com/KiCad/Sockets.pretty/archive/%{version}/Sockets.pretty-%{version}.tar.gz
# Source84-md5:	bd381d3f2222675e4f259f15f918c512
Source85:	https://github.com/KiCad/Symbols.pretty/archive/%{version}/Symbols.pretty-%{version}.tar.gz
# Source85-md5:	16185826b1eb27200c30ef972f7468cd
Source86:	https://github.com/KiCad/TO_SOT_Packages_SMD.pretty/archive/%{version}/TO_SOT_Packages_SMD.pretty-%{version}.tar.gz
# Source86-md5:	38addd895c3711539e291d5f86f27807
Source87:	https://github.com/KiCad/TO_SOT_Packages_THT.pretty/archive/%{version}/TO_SOT_Packages_THT.pretty-%{version}.tar.gz
# Source87-md5:	3a0c96fcec348fd7daf856e0351d0435
Source88:	https://github.com/KiCad/Transformers_CHK.pretty/archive/%{version}/Transformers_CHK.pretty-%{version}.tar.gz
# Source88-md5:	c9f4c477a7b3ee99258f0eb8d07eb2ad
Source89:	https://github.com/KiCad/Transformers_SMD.pretty/archive/%{version}/Transformers_SMD.pretty-%{version}.tar.gz
# Source89-md5:	9f3a326a296b10ea529d349d670b593e
Source90:	https://github.com/KiCad/Transformers_SMPS_ThroughHole.pretty/archive/%{version}/Transformers_SMPS_ThroughHole.pretty-%{version}.tar.gz
# Source90-md5:	bd6a05c82e5fa34771dc9b039c38279a
Source91:	https://github.com/KiCad/Transformers_THT.pretty/archive/%{version}/Transformers_THT.pretty-%{version}.tar.gz
# Source91-md5:	8f1fafb159a5890abb9cc1fe3f24543a
Source92:	https://github.com/KiCad/Transistors_OldSowjetAera.pretty/archive/%{version}/Transistors_OldSowjetAera.pretty-%{version}.tar.gz
# Source92-md5:	bad332b6c0097a4179611a7f86eddee2
Source93:	https://github.com/KiCad/Valves.pretty/archive/%{version}/Valves.pretty-%{version}.tar.gz
# Source93-md5:	0cef210c06a05af4f011fe73bd9d8f83
Source94:	https://github.com/KiCad/Varistors.pretty/archive/%{version}/Varistors.pretty-%{version}.tar.gz
# Source94-md5:	a18138206bf52efbdc37d448648b7e04
Source95:	https://github.com/KiCad/Wire_Connections_Bridges.pretty/archive/%{version}/Wire_Connections_Bridges.pretty-%{version}.tar.gz
# Source95-md5:	1724a3899fb5b483bf224da6a6db2650
Source96:	https://github.com/KiCad/Wire_Pads.pretty/archive/%{version}/Wire_Pads.pretty-%{version}.tar.gz
# Source96-md5:	06e3b9d0bb1be074b5693000736797db
Patch0:		nostrip.patch
# https://code.launchpad.net/~lkundrak/kicad/appstream-data/+merge/293391
Patch1:		appstream.patch
Patch2:		boost-1.61.patch
Patch3:		cmake.patch
URL:		http://www.kicad-pcb.org/
BuildRequires:	appstream-glib
BuildRequires:	asciidoc
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.6.4
BuildRequires:	curl-devel
BuildRequires:	dblatex
BuildRequires:	desktop-file-utils
BuildRequires:	doxygen
BuildRequires:	glew-devel
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
Summary:	Documentation for Kicad in German
Summary(fr.UTF-8):	Documentations pour kicad en allemand
Group:		Documentation
Requires:	%{name}-doc = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-ca
Documentation and tutorials for Kicad in German

%package doc-de
Summary:	Documentation for Kicad in German
Summary(fr.UTF-8):	Documentations pour kicad en allemand
Group:		Documentation
Requires:	%{name}-doc = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-de
Documentation and tutorials for Kicad in German

%package doc-es
Summary:	Documentation for Kicad in Spanish
Summary(fr.UTF-8):	Documentations pour kicad en espagnol
Group:		Documentation
Requires:	%{name}-doc = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-es
Documentation and tutorials for Kicad in Spanish

%package doc-fr
Summary:	Documentation for Kicad in French
Summary(fr.UTF-8):	Documentations pour kicad en français
Group:		Documentation
Requires:	%{name}-doc = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-fr
Documentation and tutorials for Kicad in French

%package doc-id
Summary:	Documentation for Kicad in Hungarian
Summary(fr.UTF-8):	Documentations pour kicad en hongrois
Group:		Documentation
Requires:	%{name}-doc = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-id
Documentation and tutorials for Kicad in Hungarian

%package doc-it
Summary:	Documentation for Kicad in Italian
Summary(fr.UTF-8):	Documentations pour kicad en italien
Group:		Documentation
Requires:	%{name}-doc = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-it
Documentation and tutorials for Kicad in Italian

%package doc-ja
Summary:	Documentation for Kicad in Japanese
Summary(fr.UTF-8):	Documentations pour kicad en japonais
Group:		Documentation
Requires:	%{name}-doc = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-ja
Documentation and tutorials for Kicad in Japanese

%package doc-nl
Summary:	Documentation for Kicad in Portuguese
Summary(fr.UTF-8):	Documentations pour kicad en portugais
Group:		Documentation
Requires:	%{name}-doc = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-nl
Documentation and tutorials for Kicad in Portuguese

%package doc-pl
Summary:	Documentation for Kicad in Polish
Summary(fr.UTF-8):	Documentations pour kicad en polonais
Group:		Documentation
Requires:	%{name}-doc = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-pl
Documentation and tutorials for Kicad in Polish

%package doc-ru
Summary:	Documentation for Kicad in Russian
Summary(fr.UTF-8):	Documentations pour kicad en russe
Group:		Documentation
Requires:	%{name}-doc = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-ru
Documentation and tutorials for Kicad in Russian

%prep
%setup -q -a 1 -a 2 -a 3
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
# Symbols libraries
cd %{name}-library-%{version}
%cmake .
%{__make} -j1 VERBOSE=1
cd ..

# Documentation
cd %{name}-doc-%{version}
%cmake . -DBUILD_FORMATS=html
%{__make} -j1 VERBOSE=1
cd ..

# Translations
mkdir %{name}-i18n-%{version}/build
cd %{name}-i18n-%{version}/build
%cmake .. \
	-DKICAD_I18N_UNIX_STRICT_PATH=ON
%{__make} -j1 VERBOSE=1
cd ../..

# Core components
%cmake . \
	-DKICAD_SKIP_BOOST=ON \
	-DKICAD_BUILD_VERSION="%{version}-%{release}" \
	-DwxWidgets_CONFIG_EXECUTABLE=%{_bindir}/wx-gtk2-unicode-config

%{__make} VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT

# KiCAD itself
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Symbols libraries
%{__make} -C %{name}-library-%{version} install \
	DESTDIR=$RPM_BUILD_ROOT

# install template
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/template
cp -p template/%{name}.pro $RPM_BUILD_ROOT%{_datadir}/%{name}/template

# Footprints
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/modules
for S in %{sources}; do
	P=$(basename $S |sed -n 's/\.pretty-.*/.pretty/p')
	[ "$P" ] || continue
	install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/$P
	tar xzf $S --strip-components=1 -C $RPM_BUILD_ROOT%{_datadir}/%{name}/modules/$P
done
ln -f $RPM_BUILD_ROOT%{_datadir}/%{name}/template/fp-lib-table{.for-pretty,}

# Documentation
%{__make} -C %{name}-doc-%{version} install \
	DESTDIR=$RPM_BUILD_ROOT

# Translations
%{__make} -C %{name}-i18n-%{version}/build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%post
%update_mime_database
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_mime_database
%update_desktop_database_postun
%update_icon_cache hicolor

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS.txt CHANGELOG.txt Documentation
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
%attr(755,root,root) %{_bindir}/pcb_calculator
%attr(755,root,root) %{_bindir}/_pcb_calculator.kiface
%attr(755,root,root) %{_bindir}/pcbnew
%attr(755,root,root) %{_bindir}/_pcbnew.kiface
%attr(755,root,root) %{_bindir}/pl_editor
%attr(755,root,root) %{_bindir}/_pl_editor.kiface
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/bom2csv.xsl
%{_libdir}/%{name}/plugins/bom_cvs.xsl
%{_libdir}/%{name}/plugins/bom_with_title_block_2_csv.xsl
%{_libdir}/%{name}/plugins/netlist_form_cadstar-RINF.xsl
%{_libdir}/%{name}/plugins/netlist_form_cadstar.xsl
%{_libdir}/%{name}/plugins/netlist_form_OrcadPcb2.xsl
%{_libdir}/%{name}/plugins/netlist_form_pads-pcb.xsl
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*x*/*/*.png
%{_iconsdir}/hicolor/scalable/*/*.svg
%{_datadir}/mime/packages/kicad.xml
%{_datadir}/appdata/kicad.appdata.xml
%{_desktopdir}/eeschema.desktop
%{_desktopdir}/%{name}.desktop
%{_desktopdir}/bitmap2component.desktop
%{_desktopdir}/cvpcb.desktop
%{_desktopdir}/gerbview.desktop
%{_desktopdir}/pcbcalculator.desktop
%{_desktopdir}/pcbnew.desktop
#%{_datadir}/mimelnk/application/x-kicad-pcb.desktop
#%{_datadir}/mimelnk/application/x-kicad-project.desktop
#%{_datadir}/mimelnk/application/x-kicad-schematic.desktop

%dir %{_docdir}/%{name}
%{_docdir}/%{name}/*.txt

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
