Name:           perl-MogileFS-Client
Version:        1.17
Release:        1%{?dist}
Summary:        Client library for the MogileFS distributed file system
License:        GPL or Artistic
Group:          Development/Libraries
URL:            https://metacpan.org/release/MogileFS-Client
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DORMANDO/MogileFS-Client-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  perl(IO::WrapTie)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module is a client library for the MogileFS distributed file system.
The class method 'new' creates a client object against a particular
mogilefs tracker and domain. This object may then be used to store and
retrieve content easily from MogileFS.

%prep
%setup -q -n perl-MogileFS-Client-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
rm t/10-basics.t
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGES TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

