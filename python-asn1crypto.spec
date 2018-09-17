# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		asn1crypto
%define		egg_name	asn1crypto
%define		pypi_name	asn1crypto
Summary:	Python ASN.1 library with a focus on performance and a pythonic API
Name:		python-%{pypi_name}
Version:	0.24.0
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/fc/f1/8db7daa71f414ddabfa056c4ef792e1461ff655c2ae2928a2b675bfed6b4/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	de3520426e81a6581352d4366f310eb1
URL:		https://pypi.org/project/asn1crypto/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fast ASN.1 parser and serializer with definitions for private keys,
public keys, certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7, PKCS#8,
PKCS#12, PKCS#5, X.509 and TSP.

%package -n python3-%{pypi_name}
Summary:	Python ASN.1 library with a focus on performance and a pythonic API
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{pypi_name}
Fast ASN.1 parser and serializer with definitions for private keys,
public keys, certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7, PKCS#8,
PKCS#12, PKCS#5, X.509 and TSP.

%prep
%setup -q -n %{pypi_name}-%{version}

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

# when files are installed in other way that standard 'setup.py
# they need to be (re-)compiled
# change %{py_sitedir} to %{py_sitescriptdir} for 'noarch' packages!
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

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
%doc changelog.md readme.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc changelog.md readme.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
