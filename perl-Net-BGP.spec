%define upstream_name    Net-BGP
Name:		perl-%{upstream_name}
Version:	0.18
Release:	2

Summary:	Net-BGP module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://metacpan.org/dist/Net-BGP
Source0:	https://cpan.metacpan.org/authors/id/S/SS/SSCHECK/Net-BGP-%{version}.tar.gz

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

%changelog
* Mon Oct 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.140.0-1mdv2011.0
+ Revision: 589352
- new version

* Fri Jul 17 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.130.0-1mdv2011.0
+ Revision: 396744
- update to 0.13

* Tue Jul 07 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.0
+ Revision: 393271
- update to 0.12
- using %0.18 fixed license field

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.08-6mdv2009.0
+ Revision: 241759
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.08-4mdv2008.0
+ Revision: 25448
- rebuild

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 0.08-3mdv2008.0
+ Revision: 25293
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.08-2mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL
- use mkrel

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 0.08-1mdk
- initial Mandriva package

