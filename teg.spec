Summary:	Risk clone
Summary(pl):	Klon Ryzyka
Name:		teg
Version:	0.11.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/teg/%{name}-%{version}.tar.bz2
# Source0-md5:	b7c778b07a22c34bd21942a8be26e095
Source1:	%{name}.desktop
URL:		http://teg.sf.net/
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libgnome-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libxml2-devel >= 2.4.0
BuildRequires:	readline-devel
Requires(post):	Gconf2
Requires:	glib2 >= 2.0.0
Requires:	libgnome >= 2.0.0
Requires:	libgnomeui >= 2.0.0
Requires:	libxml2 >= 2.4.0
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
%configure \
	--with-readline \
	--without-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Games

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog PEOPLE README.GGZ TODO README
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/teg_icono.png
%{_pixmapsdir}/teg_pix
%{_applnkdir}/Games/*
%{_sysconfdir}/gconf/schemas/*.schemas
