#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Data
%define		pnam	UUID
Summary:	Data::UUID - Perl extension for generating GUIDs/UUIDs
Summary(pl):	Data::UUID - rozszerzenie Perla do generacji GUID-�w/UUID-�w
Name:		perl-Data-UUID
Version:	0.09
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a framework for generating UUIDs (Universally
Unique Identifiers, also known as GUIDs (Globally Unique Identifiers).
A UUID is 128 bits long, and is guaranteed to be different from all
other UUIDs/GUIDs generated until 3400 A.D. UUIDs were originally used
in the Network Computing System (NCS) and later in the Open Software
Foundation's (OSF) Distributed Computing Environment. Currently many
different technologies rely on UUIDs to provide unique identity for
various software components.

%description -l pl
Modu� Perla Data::UUID udost�pnia szkielet generacji UUID-�w
(Universally Unique Identifiers - identyfikator�w unikalnych
powszechnie), znanych tez jako GUID-y (Globally Unique Identifiers -
identyfikatory unikalne globalnie). UUID-y s� 128-bitowe i
gwarantowana jest ich unikalno�� w�r�d wszyskich innych UUID-�w/
/GUID-�w wygenerowanych do roku 3400. UUID-y pierwotnie by�y u�ywane w
(Network Computing System (NCS), a p�niej w Rozproszonym �rodowisku
Obliczeniowym (Distributed Computing Environment) Fundacji Open
Software (OSF). Obecnie na zagwarantowanych przez UUID-y unikalnych
identyfikatorach dla r�nych sk�adnik�w oprogramowania opartych jest
wiele r�nych technologii

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
# Don't use pipes here: they generally don't work. Apply a patch.
%{__perl} Makefile.PL </dev/null
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitearch}/Data/UUID.pm
%dir %{perl_sitearch}/auto/Data/UUID
%{perl_sitearch}/auto/Data/UUID/UUID.bs
%attr(755,root,root) %{perl_sitearch}/auto/Data/UUID/UUID.so
%{_mandir}/man3/*
