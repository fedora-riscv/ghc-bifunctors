# generated by cabal-rpm-0.12.1
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name bifunctors
%global pkgver %{pkg_name}-%{version}

%bcond_without tests

Name:           ghc-%{pkg_name}
Version:        5.5
Release:        2%{?dist}
Summary:        Bifunctors

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-base-orphans-devel
BuildRequires:  ghc-comonad-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-semigroups-devel
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-th-abstraction-devel
BuildRequires:  ghc-transformers-compat-devel
BuildRequires:  ghc-transformers-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-hspec-devel
%endif
# End cabal-rpm deps

%description
Haskell 98 bifunctors, bifoldables and bitraversables.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%prep
%setup -q -n %{pkgver}


%build
%ghc_lib_build


%install
%ghc_lib_install


%check
%cabal_test


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files
%doc CHANGELOG.markdown README.markdown


%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 5.5-1
- update to 5.5

* Sun Sep 17 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 5.4.2-2
- Expand description a bit.

* Sat Jul 22 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 5.4.2-1
- Update to latest version.

* Fri Jul 21 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 5.3-4
- Bump for Fedora 26.

* Sat Dec 17 2016 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.3-3
- Bump to rebuild against new dependencies

* Fri Dec 16 2016 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.3-2
- Update release to be newer than previous builds

* Fri Dec 16 2016 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 5.3-1
- spec file generated by cabal-rpm-0.10.0
