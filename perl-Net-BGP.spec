%define real_name Net-BGP

Summary:	Net-BGP module for perl 
Name:		perl-%{real_name}
Version:	0.08
Release: %mkrel 4
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:  perl(Test::Pod)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module is an implementation of the BGP-4 inter-domain
routing protocol. It encapsulates all of the functionality
needed to establish and maintain a BGP peering session and
exchange routing update information with the peer.

%prep
%setup -q -n %{real_name}-%{version} 

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


