%define name        libvncserver
%define up_name     LibVNCServer
%define version     0.9
%define release     %mkrel 1
%define major       0
%define libname     %mklibname vncserver %{major}

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    An easy API to write one's own VNC server
Group:      System/Libraries
License:    GPL
URL:        http://sourceforge.net/projects/libvncserver/
Source:     http://downloads.sourceforge.net/libvncserver/%{up_name}-%{version}.tar.gz
BuildRequires:  libx11-devel
BuildRequires:  libxdamage-devel
BuildRequires:  libxext-devel
BuildRequires:  libxrandr-devel
BuildRequires:  libxtst-devel
BuildRequires:  libxinerama-devel
BuildRequires:  libxfixes-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires:  jpeg-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}

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

%package -n %{libname}-devel
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{libname}-devel
Static libraries and header files for LibVNCServer.

%package -n x11vnc
Summary:      VNC server to monitor a X11 session
Group:        Networking/Remote access

%description -n x11vnc
With x11vnc you can export your currently running X11 session to any VNC
client. You do not have to launch another session as the regular VNC server
does. So it's very useful, if you want to move to another computer without
having to log out, or to help a distant colleague to solve a problem with their
desktop.

%package -n linuxvnc
Summary:      VNC server to monitor a text session
Group:        Networking/Remote access

%description -n linuxvnc
With linuxvnc you can export your currently running text sessions to any VNC
client. So it can be useful, if you want to move to another computer without
having to log out and if you've forgotten to attach a 'screen' session to it,
or to help a distant colleague to solve a problem.

Based on the ideas of x0rfbserver and on LibVNCServer, it has evolved
into a versatile and performant while still easy to use program.

%prep
%setup -q -n %{up_name}-%{version}

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/libvncserver-config

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_libdir}/*-%{major}.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/rfb
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/*.la
%{_bindir}/libvncserver-config
%multiarch %{multiarch_bindir}/libvncserver-config

%files -n linuxvnc
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_bindir}/LinuxVNC

%files -n x11vnc
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_bindir}/x11vnc
%{_mandir}/man1/x11vnc.1*
