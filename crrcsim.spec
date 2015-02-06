Summary:	A Model-Airplane Flight Simulation Program
Name:		crrcsim
Version:	0.9.12
Release:	2
License:	GPLv2
Group:		Games/Other 
URL:		http://crrcsim.berlios.de/wiki
Source0:	http://download.berlios.de/crrcsim/%{name}-%{version}.tar.gz
Source1:	CRRCsim.desktop
BuildRequires:	jpeg-devel
BuildRequires:	plib-devel
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xt)
BuildRequires:	desktop-file-utils

%description
Crrcsim is a model-airplane flight simulation program. Using it, you can learn
how to fly model aircraft, test new aircraft designs, and improve your
skills by practicing on your computer. 

It rules! The flight model is very realistic. The flight model parameters are
calculated based on a 3D representation of the aircraft. Stalls are properly
modelled as well. Model control is possible with your own rc transmitter, or
any input device such as joystick, mouse, keyboard ...

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%find_lang %{name}

desktop-file-install --vendor=""                        \
        --dir=%{buildroot}%{_datadir}/applications      \
        %{SOURCE1}

%files -f %{name}.lang
%doc COPYING
%{_datadir}/%{name}/
%{_bindir}/crrcsim
%{_datadir}/applications/CRRCsim.desktop
%{_mandir}/man1/%{name}.1.xz


%changelog
* Sat May 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.9.12-1
+ Revision: 796603
- version update 0.9.12

* Sun Nov 13 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.9.11-1
+ Revision: 730305
- BS jpeg fix
- imported package crrcsim

