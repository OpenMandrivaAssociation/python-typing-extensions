Name:		python-typing-extensions
Version:	4.16.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/t/typing-extensions/typing_extensions-%{version}.tar.gz
Summary:	Backported and Experimental Type Hints for Python 3.9+
URL:		https://pypi.org/project/typing-extensions/
License:	GPL
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Backported and Experimental Type Hints for Python 3.9+

%install -a
rm -rf %{buildroot}%{py_sitedir}/__pycache__

%files
%{py_sitedir}/typing_extensions.py
%{py_sitedir}/typing_extensions-*.*-info
