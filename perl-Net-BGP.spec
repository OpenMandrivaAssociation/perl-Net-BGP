%define upstream_name    Net-BGP
%define upstream_version 0.18
Name:		perl-%{upstream_name}
Version:	0.18
Release:	1

Summary:	Net-BGP module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://metacpan.org/dist/Net-BGP
Source0:	https://cpan.metacpan.org/authors/id/S/SS/SSCHECK/Net-BGP-0.18.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::Pod)
BuildArch:	noarch

%description
This module is an implementation of the BGP-4 inter-domain
routing protocol. It encapsulates all of the functionality
needed to establish and maintain a BGP peering session and
exchange routing update information with the peer.

%prep
%setup -q -n %{upstream_name}-%{version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Net/BGP
%{perl_vendorlib}/Net/BGP.pm
%{_mandir}/*/*

