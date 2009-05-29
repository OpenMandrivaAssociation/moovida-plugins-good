%define debug_package	%{nil}

%define oname	elisa-plugins-good

%define rel	1

%define svn	0
%define pre	0
%if %svn
%define release		%mkrel 0.%svn.%rel
%define distname	%name-%svn.tar.lzma
%define dirname		%oname
%else
%if %pre
%define release		%mkrel 0.%pre.%rel
%define distname	%name-%version.%pre.tar.gz
%define dirname		%oname-%version.%pre
%else
%define release		%mkrel %rel
%define distname	%name-%version.tar.gz
%define dirname		%oname-%version
%endif
%endif

Summary:	'Good' plugins for the Moovida media center
Name:		moovida-plugins-good
Version:	1.0.1
Release:	%{release}
Source0:	http://elisa.fluendo.com/static/download/elisa/%{distname}
License:	GPLv3
Group:		Development/Python
URL:		http://elisa.fluendo.com/
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python
BuildRequires:	python-setuptools
BuildRequires:	python-devel
BuildRequires:	python-twisted
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils
BuildRequires:	gstreamer0.10-python
BuildRequires:	moovida-core = %{version}
Requires:	moovida = %{version}
# For UPnP support
Suggests:	python-coherence
# For the weather report plugin
Suggests:	python-pymetar
Provides:	elisa-plugins-good = %{version}-%{release}
Obsoletes:	elisa-plugins-good < %{version}-%{release}

%description
Elisa is a project to create an open source cross platform media center 
solution. This package contains 'good' (well-written and legally clean)
plugins for Elisa.

%prep
%setup -q -n %{dirname}

%build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --single-version-externally-managed --compile --optimize=2

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{py_puresitedir}/elisa/plugins/*
%{py_puresitedir}/elisa_plugin_*-py%{pyver}.egg-info
%{py_puresitedir}/elisa_plugin_*-py%{pyver}-nspkg.pth

