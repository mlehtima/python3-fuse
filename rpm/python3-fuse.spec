Name:       python3-fuse
Summary:    Python 3.x bindings for libfuse 2.x
Version:    1.0.9
Release:    1
License:    LGPLv2.1
URL:        https://github.com/sailfishos/python3-fuse
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(fuse)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
This is a Python interface to libfuse (https://github.com/libfuse/libfuse).

%prep
%autosetup -n %{name}-%{version}/python-fuse

%build
%py3_build

%install
%py3_install

%files
%license COPYING
%doc AUTHORS FAQ README.md example
%{python3_sitearch}/*
