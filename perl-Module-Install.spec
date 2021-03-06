#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Module-Install
Version  : 1.19
Release  : 18
URL      : http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/Module-Install-1.19.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/Module-Install-1.19.tar.gz
Summary  : 'Standalone, extensible Perl module installer'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Module-Install-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Build)
BuildRequires : perl(Module::ScanDeps)
BuildRequires : perl(YAML::Tiny)

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
%setup -q -n Module-Install-1.19
cd %{_builddir}/Module-Install-1.19

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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
/usr/share/man/man3/inc::Module::Install::DSL.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/Module/AutoInstall.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install.pod
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/API.pod
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Admin.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Admin/Bundle.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Admin/Compiler.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Admin/Find.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Admin/Include.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Admin/Makefile.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Admin/Manifest.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Admin/Metadata.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Admin/ScanDeps.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Admin/WriteAll.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/AutoInstall.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Base.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Bundle.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Can.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Compiler.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/DSL.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Deprecated.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/External.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/FAQ.pod
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Fetch.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Include.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Inline.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/MakeMaker.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Makefile.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Metadata.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/PAR.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Philosophy.pod
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Run.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Scripts.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Share.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/Win32.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/With.pm
/usr/lib/perl5/vendor_perl/5.30.3/Module/Install/WriteAll.pm
/usr/lib/perl5/vendor_perl/5.30.3/inc/Module/Install.pm
/usr/lib/perl5/vendor_perl/5.30.3/inc/Module/Install/DSL.pm
