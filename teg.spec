Summary:	Risk clone
Summary(pl):	Klon Ryzyka
Name:		teg
Version:	0.10.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/teg/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://teg.sf.net/
BuildRequires:	autoconf
BuildRequires:	gnome-libs-devel
BuildRequires:	libxml-devel
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tenes Emapandas Graciela (TEG) is a clone of 'Plan Táctico y
Estratégico de la Guerra', which is a pseudo-clone of Risk, a
multiplayer turn-based strategy game. Some rules are different.

%description -l pl
Tenes Emapandas Graciela (TEG) jest klonem 'Plan Táctico y Estratégico
de la Guerra', który jest pseudo-klonem Ryzyka, strategicznej gry
turowej dla wielu graczy. Niektóre zasady s± inne.

%prep
%setup -q

%build
cd ggz
%{__autoconf}
cd ..
%{__autoconf}
%configure \
	--with-readline \
	--without-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Games

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog PEOPLE README.GGZ TODO README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gnome/help/teg
%{_pixmapsdir}/teg_icono.png
%{_pixmapsdir}/teg_pix
%{_applnkdir}/Games/*
