#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	Hierarchy
Summary:	Data::Hierarchy - handle data in a hierarchical structure
Summary(pl):	Data::Hierarchy - obs³uga danych w strukturze hierarchicznej
Name:		perl-Data-Hierarchy
Version:	0.20
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2823492b86e4a1a74ad4127472412e32
BuildRequires:	perl-Clone
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::Hierarchy provides a simple interface for manipulating
inheritable data attached to a hierarchical environment (like
filesystem).

%description -l pl
Modu³ Data::Hierarchy udostêpnia prosty interfejs do manipulowania
dziedziczonymi danymi umieszczonymi w ¶rodowisku hierarchicznym (takim
jak system plików).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGE*
%{perl_vendorlib}/Data/*.pm
%{_mandir}/man3/*
