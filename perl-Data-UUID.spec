#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Data
%define		pnam	UUID
Summary:	Data::UUID - Perl extension for generating GUIDs/UUIDs
Summary(pl):	Data::UUID - rozszerzenie Perla do generowania GUID-ów/UUID-ów
Name:		perl-Data-UUID
Version:	0.13
Release:	1
License:	distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8b3f173c66a9e58aebcde85acf1fce6a
Patch0:		%{name}-types.patch
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

%description -l pl
Modu³ Perla Data::UUID udostêpnia szkielet do generowania UUID-ów
(Universally Unique Identifiers - identyfikatorów unikalnych
powszechnie), znanych te¿ jako GUID-y (Globally Unique Identifiers -
identyfikatory unikalne globalnie). UUID-y s± 128-bitowe i
gwarantowana jest ich unikalno¶æ w¶ród wszyskich innych UUID-ów/
/GUID-ów wygenerowanych do roku 3400. UUID-y pierwotnie by³y u¿ywane w
Network Computing System (NCS), a pó¼niej w Rozproszonym ¦rodowisku
Obliczeniowym (Distributed Computing Environment) Fundacji Open
Software (OSF). Obecnie na zagwarantowanych przez UUID-y unikalnych
identyfikatorach dla ró¿nych sk³adników oprogramowania opartych jest
wiele ró¿nych technologii

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor
%{__make} \
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
%{perl_vendorarch}/auto/Data/UUID/*.ix
%{perl_vendorarch}/auto/Data/UUID/UUID.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Data/UUID/UUID.so
%{_mandir}/man3/*
