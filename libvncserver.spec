%define up_name	LibVNCServer
%define major	1
%define libname	%mklibname vncserver %{major}
%define libclient %mklibname vncclient %{major}
%define devname	%mklibname -d vncserver

Summary:	An easy API to write one's own VNC server
Name:		libvncserver
Version:	0.9.11
Release:	2
Group:		System/Libraries
License:	GPLv2
Url:		http://libvnc.github.io
Source0:	https://github.com/LibVNC/libvncserver/archive/%{up_name}-%{version}.tar.gz
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libva)

%description
LibVNCServer makes writing a VNC server (or more correctly, a program
exporting a framebuffer via the Remote Frame Buffer protocol) easy.

It is based on OSXvnc, which in turn is based on the original Xvnc by
ORL, later AT&T research labs in UK.

It hides the programmer from the tedious task of managing clients and
compression schemata.

%package -n %{libname}
Summary:	An easy API to write one's own VNC server
Group:		System/Libraries

%description -n %{libname}
LibVNCServer makes writing a VNC server (or more correctly, a program
exporting a framebuffer via the Remote Frame Buffer protocol) easy.

It is based on OSXvnc, which in turn is based on the original Xvnc by
ORL, later AT&T research labs in UK.

It hides the programmer from the tedious task of managing clients and
compression schemata.

%package -n %{libclient}
Summary:	An easy API to write one's own VNC server
Group:		System/Libraries
Conflicts:	%{_lib}vncserver0 < 0.9.9-2

%description -n %{libclient}
This package contains a shared library for %{name}.

%package -n %{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libclient} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Static libraries and header files for LibVNCServer.

%prep
%setup -qn %{name}-%{up_name}-%{version}
%apply_patches
autoreconf -fiv

%build
%configure
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libvncserver.so.%{major}*

%files -n %{libclient}
%{_libdir}/libvncclient.so.%{major}*

%files -n %{devname}
%{_includedir}/rfb
%{_bindir}/libvncserver-config
%{_libdir}/*.so
%{_libdir}/pkgconfig/libvncclient.pc
%{_libdir}/pkgconfig/libvncserver.pc
