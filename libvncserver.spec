%define up_name     LibVNCServer
%define major       0
%define libname     %mklibname vncserver %{major}
%define develname   %mklibname -d vncserver

Name:		libvncserver
Version:	0.9.9
Release:	1
Summary:	An easy API to write one's own VNC server
Group:		System/Libraries
License:	GPL
URL:		http://sourceforge.net/projects/libvncserver/
Source:		http://downloads.sourceforge.net/libvncserver/%{up_name}-%{version}.tar.gz
Patch0:		LibVNCServer-0.9.9-no_x11vnc.patch
Patch1:		LibVNCServer-0.9.9-str-format.patch
Patch2:		libvncserver-automake-1.13.patch
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	zlib-devel
BuildRequires:	jpeg-devel

%track
prog %name = {
	url = http://sourceforge.net/projects/libvncserver/
	version = %version
	regex = LibVNCServer-(__VER__)\.tar\.gz
}

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

%package -n %{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{libname}-devel < 0.9.9

%description -n %{develname}
Static libraries and header files for LibVNCServer.

%package -n linuxvnc
Summary:	VNC server to monitor a text session
Group:		Networking/Remote access

%description -n linuxvnc
With linuxvnc you can export your currently running text sessions to any VNC
client. So it can be useful, if you want to move to another computer without
having to log out and if you've forgotten to attach a 'screen' session to it,
or to help a distant colleague to solve a problem.

Based on the ideas of x0rfbserver and on LibVNCServer, it has evolved
into a versatile and performant while still easy to use program.

%prep
%setup -q -n %{up_name}-%{version}
%apply_patches

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/libvncserver-config

%files -n %{libname}
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_libdir}/*.so.*

%files -n %{develname}
%{_includedir}/rfb
%{_libdir}/*.so
%{_bindir}/libvncserver-config
%{multiarch_bindir}/libvncserver-config
%{_libdir}/pkgconfig/libvncclient.pc
%{_libdir}/pkgconfig/libvncserver.pc

%files -n linuxvnc
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_bindir}/linuxvnc

%changelog
* Tue Apr 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.9.8-3mdv2012.0
+ Revision: 789067
- Rebuild for .la files removal.

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.8-2
+ Revision: 661681
- multiarch fixes

* Wed Apr 06 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.8-1
+ Revision: 650978
- new version

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-4mdv2011.0
+ Revision: 602613
- rebuild

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-3mdv2010.1
+ Revision: 488785
- rebuilt against libjpeg v8

* Sat Aug 15 2009 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-2mdv2010.0
+ Revision: 416627
- rebuilt against libjpeg v7

* Thu Feb 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.7-1mdv2009.1
+ Revision: 337875
- new release
- new devel policy

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.9.1-2mdv2009.0
+ Revision: 219560
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Jun 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.1-1mdv2008.0
+ Revision: 34726
- new version

* Thu May 24 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.9-2mdv2008.0
+ Revision: 30918
- don't ship x11vnc, it is distributed separatly

* Tue May 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.9-1mdv2008.0
+ Revision: 29922
- new version

* Tue Apr 24 2007 Laurent Montel <lmontel@mandriva.org> 0.8.2-3mdv2008.0
+ Revision: 17763
- Fix include when it used with c++


* Mon Feb 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.2-2mdv2007.0
+ Revision: 119029
- fix the binary swap between subpackages (fix #28546)

* Mon Dec 11 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.2-1mdv2007.1
+ Revision: 94802
- Import libvncserver

* Thu Dec 07 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.2-1mdv2007.1
- first mdv release

