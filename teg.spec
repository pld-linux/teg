Summary:	Risk clone
Summary(pl):	Klon Riska
Name:		teg
Version:	0.9.2
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://prdownloads.sourceforge.net/teg/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://teg.sf.net/
BuildRequires:	autoconf
BuildRequires:	gnome-libs-devel
BuildRequires:	libxml-devel
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Tenes Emapandas Graciela (TEG) is a clone of 'Plan Táctico y
Estratégico de la Guerra', which is a pseudo-clone of Risk, a
multiplayer turn-based strategy game. Some rules are different.

%description -l pl
Tenes Emapandas Graciela (TEG) jest klonem 'Plan Táctico y Estratégico
de la Guerra', który jest pseudo-klonem Riska, strategicznej gry
turowej dla wielu graczy. Niektóre zasady s± inne.

%prep
%setup -q

%build
(cd ggz; autoconf)
autoconf
%configure \
	--with-readline \
	--without-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Games

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog PEOPLE README.GGZ TODO README

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gnome/help/teg
%{_pixmapsdir}/teg_icono.png
%{_pixmapsdir}/teg_pix
%{_applnkdir}/Games/*
