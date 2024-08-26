Name:		python-typing-extensions
Version:	4.12.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/t/typing-extensions/typing_extensions-%{version}.tar.gz
Summary:	Backported and Experimental Type Hints for Python 3.7+
URL:		https://pypi.org/project/typing-extensions/
License:	GPL
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Backported and Experimental Type Hints for Python 3.7+

%prep
%autosetup -p1 -n typing_extensions-%{version}

%build
%py_build

%install
%py_install
rm -rf %{buildroot}%{py_sitedir}/__pycache__

%files
%{py_sitedir}/typing_extensions.py
%{py_sitedir}/typing_extensions-*.*-info
