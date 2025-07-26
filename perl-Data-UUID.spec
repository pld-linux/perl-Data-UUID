#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%define		pdir	Data
%define		pnam	UUID
Summary:	Data::UUID - Perl extension for generating GUIDs/UUIDs
Summary(pl.UTF-8):	Data::UUID - rozszerzenie Perla do generowania GUID-ów/UUID-ów
Name:		perl-Data-UUID
Version:	1.224
Release:	8
License:	distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Data/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	71510bbcce760c394591fca83a9b5e6d
Patch0:		%{name}-types.patch
URL:		http://search.cpan.org/dist/Data-UUID/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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

%description -l pl.UTF-8
Moduł Perla Data::UUID udostępnia szkielet do generowania UUID-ów
(Universally Unique Identifiers - identyfikatorów unikalnych
powszechnie), znanych też jako GUID-y (Globally Unique Identifiers -
identyfikatory unikalne globalnie). UUID-y są 128-bitowe i
gwarantowana jest ich unikalność wśród wszyskich innych UUID-ów/
/GUID-ów wygenerowanych do roku 3400. UUID-y pierwotnie były używane w
Network Computing System (NCS), a później w Rozproszonym Środowisku
Obliczeniowym (Distributed Computing Environment) Fundacji Open
Software (OSF). Obecnie na zagwarantowanych przez UUID-y unikalnych
identyfikatorach dla różnych składników oprogramowania opartych jest
wiele różnych technologii

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Data/UUID.pm
%dir %{perl_vendorarch}/auto/Data/UUID
%attr(755,root,root) %{perl_vendorarch}/auto/Data/UUID/UUID.so
%{_mandir}/man3/*
