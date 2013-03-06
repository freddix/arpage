Summary:	MIDI arpeggiator with transport and tempo sync
Name:		arpage
Version:	0.3.3
Release:	1
License:	GPL/GPL v3
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/project/arpage/Alpha%20Release%20%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	987070a6efb4c9e9f3dbe4ca43ddc6a4
Patch0:		%{name}-build.patch
BuildRequires:	gtkmm-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libxml++-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIDI arpeggiator with transport and tempo sync.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install src/arpage.png $RPM_BUILD_ROOT%{_pixmapsdir}

cat > $RPM_BUILD_ROOT%{_desktopdir}/arpage.desktop <<EOF
[Desktop Entry]
Type=Application
Exec=arpage
Icon=arpage
Terminal=false
Name=Arpage
Comment=MIDI Arpeggiator
Categories=GTK;AudioVideo;Audio;Midi;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/arpage
%attr(755,root,root) %{_bindir}/zonage
%{_datadir}/arpage
%{_desktopdir}/arpage.desktop
%{_pixmapsdir}/arpage.png

