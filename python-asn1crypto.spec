#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module
%bcond_without	tests	# unit tests

%define		module		asn1crypto
%define		egg_name	asn1crypto
%define		pypi_name	asn1crypto
Summary:	Python ASN.1 library with a focus on performance and a pythonic API
Summary(pl.UTF-8):	Biblioteka ASN.1 dla Pythona zorientowana na wydajność i pythonowe API
Name:		python-%{pypi_name}
Version:	1.2.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/asn1crypto/
Source0:	https://files.pythonhosted.org/packages/source/a/asn1crypto/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	fc3815cdd4812505e3ee297740c5f5d3
Source1:	https://files.pythonhosted.org/packages/source/a/asn1crypto_tests/asn1crypto_tests-%{version}.tar.gz
# Source1-md5:	c2eb5724cc6ac0bf35cf9c745a8c2435
URL:		https://pypi.org/project/asn1crypto/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fast ASN.1 parser and serializer with definitions for private keys,
public keys, certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7, PKCS#8,
PKCS#12, PKCS#5, X.509 and TSP.

%description -l pl.UTF-8
Szybki parser i serializer ASN1 z definicjami dla kluczy prywatnych,
kluczy publicznych, certyfikatów, CRL, OCSP, CMS, PKCS#3, PKCS#7,
PKCS#8, PKCS#12, PKCS#5, X.509 i TSP.

%package -n python3-%{pypi_name}
Summary:	Python ASN.1 library with a focus on performance and a pythonic API
Summary(pl.UTF-8):	Biblioteka ASN.1 dla Pythona zorientowana na wydajność i pythonowe API
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{pypi_name}
Fast ASN.1 parser and serializer with definitions for private keys,
public keys, certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7, PKCS#8,
PKCS#12, PKCS#5, X.509 and TSP.

%description -n python3-%{pypi_name} -l pl.UTF-8
Szybki parser i serializer ASN1 z definicjami dla kluczy prywatnych,
kluczy publicznych, certyfikatów, CRL, OCSP, CMS, PKCS#3, PKCS#7,
PKCS#8, PKCS#12, PKCS#5, X.509 i TSP.

%prep
%setup -q -n %{pypi_name}-%{version} %{?with_tests:-a1}

%if %{with tests}
%{__mv} asn1crypto_tests-%{version} tests
%endif

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE changelog.md readme.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc LICENSE changelog.md readme.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
