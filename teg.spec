Summary:	Risk clone
Summary(pl.UTF-8):	Klon Ryzyka
Name:		teg
Version:	0.11.2
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/teg/%{name}-%{version}.tar.bz2
# Source0-md5:	880c18eb586c4642fe14e6b41e8a642f
Patch0:		%{name}-desktop.patch
URL:		http://teg.sourceforge.net/
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libgnome-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libxml2-devel >= 2.4.0
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2
Requires:	glib2 >= 2.0.0
Requires:	libgnome >= 2.0.0
Requires:	libgnomeui >= 2.0.0
Requires:	libxml2 >= 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tenes Emapandas Graciela (TEG) is a clone of 'Plan Táctico y
Estratégico de la Guerra', which is a pseudo-clone of Risk,
a multiplayer turn-based strategy game. Some rules are different.

%description -l pl.UTF-8
Tenes Emapandas Graciela (TEG) jest klonem 'Plan Táctico y Estratégico
de la Guerra', który jest pseudo-klonem Ryzyka, strategicznej gry
turowej dla wielu graczy. Niektóre zasady są inne.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.* .
%configure \
	--with-readline \
	--without-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONFTOOL=/bin/true \
	Gamesdir=%{_desktopdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install teg.schemas

%preun
%gconf_schema_uninstall teg.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog PEOPLE README README.GGZ TODO
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/teg_icono.png
%{_pixmapsdir}/teg_pix
%{_desktopdir}/*.desktop
%{_sysconfdir}/gconf/schemas/*.schemas
