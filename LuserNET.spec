Summary:	Mail application for GNUstep
Summary(pl):	Aplikacja pocztowa dla ¶rodowiska GNUstep
Name:		LuserNET
Version:	0.4.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://w1.423.telia.com/~u42308495/alex/LuserNET/%{name}-%{version}.tar.gz
# Source0-md5:	3d17d7462a3aba295246362a90db3ea1
Patch0:		%{name}-initializeWithArguments.patch
URL:		http://www.collaboration-world.com/gnumail/
BuildRequires:	Pantomime-devel >= 1.1.2-4
BuildRequires:	gnustep-gui-devel >= 0.9.1
Requires:	Pantomime >= 1.1.2-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/%{_lib}/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

%description
A GNUStep news reader

%prep
%setup -q
%patch0 -p1

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changes README

%dir %{_prefix}/System/Applications/LuserNET.app
%attr(755,root,root) %{_prefix}/System/Applications/LuserNET.app/LuserNET
%attr(755,root,root) %{_prefix}/System/Applications/LuserNET.app/%{gscpu}/%{gsos}/%{libcombo}/LuserNET
%{_prefix}/System/Applications/LuserNET.app/%{gscpu}/%{gsos}/%{libcombo}/library_paths.openapp

%dir %{_prefix}/System/Applications/LuserNET.app/Resources
%{_prefix}/System/Applications/LuserNET.app/Resources/*.desktop
%{_prefix}/System/Applications/LuserNET.app/Resources/*.plist
%{_prefix}/System/Applications/LuserNET.app/Resources/*.tiff
%{_prefix}/System/Applications/LuserNET.app/Resources/English.lproj
%lang(fr) %{_prefix}/System/Applications/LuserNET.app/Resources/French.lproj
%lang(de) %{_prefix}/System/Applications/LuserNET.app/Resources/German.lproj
%lang(es) %{_prefix}/System/Applications/LuserNET.app/Resources/Spanish.lproj
%lang(sv) %{_prefix}/System/Applications/LuserNET.app/Resources/Swedish.lproj
