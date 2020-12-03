%global srcname typing_extensions

Name:           python-typing-extensions
Version:        3.7.4.3
Release:        1
Summary:        Python Typing Extensions

License:        Python
URL:            https://pypi.org/project/typing-extensions/
Source0:        https://files.pythonhosted.org/packages/e7/dd/f1713bc6638cc3a6a23735eff6ee09393b44b96176d3296693ada272a80b/typing_extensions-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-test
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python-%{srcname}}

%description
Typing Extensions - Backported and Experimental Type Hints for Python

The typing module was added to the standard library in Python 3.5 on a
provisional basis and will no longer be provisional in Python 3.7.
However, this means users of Python 3.5 - 3.6 who are unable to upgrade will not
be able to take advantage of new types added to the typing module, such as
typing.Text or typing.Coroutine.

The typing_extensions module contains both backports of these changes as well as
experimental types that will eventually be added to the typing module, such as
Protocol.

Users of other Python versions should continue to install and use the typing
module from PyPi instead of using this one unless specifically writing code that
must be compatible with multiple Python versions or requires experimental types.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/%{srcname}-*.egg-info/
%{python_sitelib}/%{srcname}.py
%{python_sitelib}/__pycache__/*
