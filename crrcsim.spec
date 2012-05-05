Summary:	A Model-Airplane Flight Simulation Program
Name:		crrcsim
Version:	0.9.12
Release:	1
License:	GPLv2
Group:		Games/Other 
URL:		http://crrcsim.berlios.de/wiki
Source0:	http://download.berlios.de/crrcsim/%{name}-%{version}.tar.gz
Source1:	CRRCsim.desktop
BuildRequires:	SDL-devel
BuildRequires:	portaudio-devel
#BuildRequires:	freeglut-devel
BuildRequires:	libmesaglut-devel
BuildRequires:	plib-devel
BuildRequires:	jpeg-devel
BuildRequires:	libxi-devel
BuildRequires:	libxt-devel
BuildRequires:	libxmu-devel
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
