%define debug_package	%{nil}

%define rel	2

%define svn	0
%define pre	0
%if %svn
%define release		%mkrel 0.%svn.%rel
%define distname	%name-%svn.tar.lzma
%define dirname		%name
%else
%if %pre
%define release		%mkrel 0.%pre.%rel
%define distname	%name-%version.%pre.tar.gz
%define dirname		%name-%version.%pre
%else
%define release		%mkrel %rel
%define distname	%name-%version.tar.gz
%define dirname		%name-%version
%endif
%endif

Summary:	'Ugly' plugins for the Elisa media center
Name:		elisa-plugins-ugly
Version:	0.5.37
Release:	%{release}
# For SVN:
# svn co https://code.fluendo.com/elisa/svn/trunk elisa
Source0:	http://elisa.fluendo.com/static/download/elisa/%{distname}
# From https://elisa.fluendo.com/quality/review/request/%3C20081106174059.32406.qmail@kantoor2.datux.nl%3E
# Repeat signal detection for LIRC plugin - AdamW 2008/11
Patch0:		elisa-plugins-ugly-0.5.19-lirc_repeat.patch
License:	GPLv3 and MIT
Group:		Development/Python
URL:		https://elisa.fluendo.com/
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python
BuildRequires:	python-setuptools
BuildRequires:	python-devel
BuildRequires:	python-twisted
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils
BuildRequires:	gstreamer0.10-python
BuildRequires:	elisa-core >= %{version}
Requires:	elisa-plugins-good >= %{version}
Suggests:	twill
# For LIRC input support
Suggests:	python-lirc

%description
Elisa is a project to create an open source cross platform media center 
solution. This package contains 'ugly' plugins for Elisa.

%prep
%setup -q -n %{dirname}
%patch0 -p1 -b .repeat

%build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --single-version-externally-managed --compile --optimize=2
# already in -good
rm -f %{buildroot}%{py_puresitedir}/elisa/plugins/__init__*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{py_puresitedir}/elisa/plugins/*
%{py_puresitedir}/elisa_plugin_*-py%{pyver}.egg-info
%{py_puresitedir}/elisa_plugin_*-py%{pyver}-nspkg.pth

