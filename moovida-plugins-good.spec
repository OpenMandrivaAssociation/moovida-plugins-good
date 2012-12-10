%define debug_package	%{nil}

%define oname	elisa-plugins-good

Summary:	'Good' plugins for the Moovida media center
Name:		moovida-plugins-good
Version:	1.0.9
Release:	2
Source0:	http://www.moovida.com/media/public/%{name}-%{version}.tar.gz
License:	GPLv3
Group:		Development/Python
URL:		http://www.moovida.com/
BuildArch:	noarch
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
%rename	elisa-plugins-good

%description
Moovida is a project to create an open source cross platform media center 
solution. This package contains 'good' (well-written and legally clean)
plugins for Moovida.

%prep
%setup -q -n %{oname}-%{version}

%build

%install
python setup.py install --root=%{buildroot} --single-version-externally-managed --compile --optimize=2

%files
%{py_puresitedir}/elisa/plugins/*
%{py_puresitedir}/elisa_plugin_*-py%{py_ver}.egg-info
%{py_puresitedir}/elisa_plugin_*-py%{py_ver}-nspkg.pth

