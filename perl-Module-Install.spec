#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Module-Install
Version  : 1.21
Release  : 30
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Module-Install-1.21.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Module-Install-1.21.tar.gz
Summary  : 'Standalone, extensible Perl module installer'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Module-Install-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::ScanDeps)
BuildRequires : perl(YAML::Tiny)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Module::Install - Standalone, extensible Perl module installer
SYNOPSIS
In your Makefile.PL: (Recommended Usage)

%package dev
Summary: dev components for the perl-Module-Install package.
Group: Development
Provides: perl-Module-Install-devel = %{version}-%{release}
Requires: perl-Module-Install = %{version}-%{release}

%description dev
dev components for the perl-Module-Install package.


%package perl
Summary: perl components for the perl-Module-Install package.
Group: Default
Requires: perl-Module-Install = %{version}-%{release}

%description perl
perl components for the perl-Module-Install package.


%prep
%setup -q -n Module-Install-1.21
cd %{_builddir}/Module-Install-1.21

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Module::AutoInstall.3
/usr/share/man/man3/Module::Install.3
/usr/share/man/man3/Module::Install::API.3
/usr/share/man/man3/Module::Install::Admin.3
/usr/share/man/man3/Module::Install::Admin::Include.3
/usr/share/man/man3/Module::Install::Admin::Manifest.3
/usr/share/man/man3/Module::Install::Base.3
/usr/share/man/man3/Module::Install::Bundle.3
/usr/share/man/man3/Module::Install::Can.3
/usr/share/man/man3/Module::Install::Compiler.3
/usr/share/man/man3/Module::Install::Deprecated.3
/usr/share/man/man3/Module::Install::External.3
/usr/share/man/man3/Module::Install::FAQ.3
/usr/share/man/man3/Module::Install::Makefile.3
/usr/share/man/man3/Module::Install::PAR.3
/usr/share/man/man3/Module::Install::Philosophy.3
/usr/share/man/man3/Module::Install::Share.3
/usr/share/man/man3/Module::Install::With.3
/usr/share/man/man3/inc::Module::Install.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
