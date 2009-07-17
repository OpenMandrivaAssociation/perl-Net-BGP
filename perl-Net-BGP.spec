%define upstream_name    Net-BGP
%define upstream_version 0.13

Name:	 perl-%{upstream_name}
Version: %perl_convert_version %{upstream_version}
Release: %mkrel 1

Summary:	Net-BGP module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::Pod)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module is an implementation of the BGP-4 inter-domain
routing protocol. It encapsulates all of the functionality
needed to establish and maintain a BGP peering session and
exchange routing update information with the peer.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Net/BGP
%{perl_vendorlib}/Net/BGP.pm
%{_mandir}/*/*

