#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	AACS support library for Blu-ray playback
Summary(pl.UTF-8):	Biblioteka obsługi AACS do odtwarzania Blu-ray
Name:		libaacs
Version:	0.8.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://download.videolan.org/videolan/libaacs/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	0b6fb63f81d62cd6acc98ae8f8d50c74
URL:		http://www.videolan.org/developers/libaacs.html
BuildRequires:	libgcrypt-devel
BuildRequires:	libgpg-error-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libaacs is a research project to implement the Advanced Access Content
System specification. This research project provides, through an
open-source library, a way to understand how the AACS works.

%description -l pl.UTF-8
libaacs to projekt badawczy mający na celu zaimplementowanie
specyfikacji Advanced Access Content System (zaawansowanego systemu
dostępu do treści). Zapewnia on - poprzez bibliotekę mającą otwarte
źródła - możliwość zrozumienia, jak działa AACS.

%package devel
Summary:	Header files for AACS library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AACS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for AACS library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AACS.

%package static
Summary:	Static AACS library
Summary(pl.UTF-8):	Statyczna biblioteka AACS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static AACS library.

%description static -l pl.UTF-8
Statyczna biblioteka AACS.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README.txt KEYDB.cfg
%attr(755,root,root) %{_bindir}/aacs_info
%attr(755,root,root) %{_libdir}/libaacs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaacs.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaacs.so
%{_includedir}/libaacs
%{_pkgconfigdir}/libaacs.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libaacs.a
%endif
