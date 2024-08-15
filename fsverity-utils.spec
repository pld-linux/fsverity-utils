Summary:	Userspace utilities for fs-verity
Summary(pl.UTF-8):	Narzędzia przestrzeni użytkownika dla fs-verity
Name:		fsverity-utils
Version:	1.6
Release:	1
License:	MIT
Group:		Applications/System
Source0:	https://git.kernel.org/pub/scm/fs/fsverity/fsverity-utils.git/snapshot/%{name}-%{version}.tar.gz
# Source0-md5:	0c9665923a81efca89c9e36b6ca48f2b
URL:		https://git.kernel.org/pub/scm/fs/fsverity/fsverity-utils.git
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is fsverity-utils, a set of userspace utilities for fs-verity.
fs-verity is a Linux kernel feature that does transparent on-demand
integrity/authenticity verification of the contents of read-only
files, using a hidden Merkle tree (hash tree) associated with the
file. It is similar to dm-verity, but implemented at the file level
rather than at the block device level.

%description -l pl.UTF-8
fsverity-utils to zestaw narzędzi przestrzeni użytkownika dla
fs-verity. fs-verity to funkcja jądra Linuksa wykonująca na żądanie
przezroczystą weryfikację integralności/autentyczności plików tylko do
odczytu przy użyciu ukrytego drzewa Merkle (drzewa skrótów),
powiązanego z plikiem. Jest podobna do dm-verity, ale zaimplementowana
na poziomie plików, a nie urządzenia blokowego.

%package -n libfsverity
Summary:	Shared fs-verity library
Summary(pl.UTF-8):	Współdzielona biblioteka fs-verity
Group:		Libraries

%description -n libfsverity
Shared fs-verity library.

%description -n libfsverity -l pl.UTF-8
Współdzielona biblioteka fs-verity.

%package -n libfsverity-devel
Summary:	Header files for fs-verity library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki fs-verity
Group:		Development/Libraries
Requires:	libfsverity = %{version}-%{release}

%description -n libfsverity-devel
Header files for fs-verity library.

%description -n libfsverity-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki fs-verity.

%package -n libfsverity-static
Summary:	Static fs-verity library
Summary(pl.UTF-8):	Biblioteka statyczna fs-verity
Group:		Development/Libraries
Requires:	libfsverity-devel = %{version}-%{release}

%description -n libfsverity-static
Static fs-verity library.

%description -n libfsverity-static -l pl.UTF-8
Biblioteka statyczna fs-verity.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	CPPFLAGS="%{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}" \
	V=1

%install
rm -rf $RPM_BUILD_ROOT

# build flags needed to avoid rebuilding
%{__make} install \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	CPPFLAGS="%{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}" \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libfsverity -p /sbin/ldconfig
%postun	-n libfsverity -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS.md README.md
%attr(755,root,root) %{_bindir}/fsverity
%{_mandir}/man1/fsverity.1*

%files -n libfsverity
%defattr(644,root,root,755)
%doc LICENSE NEWS.md README.md
%attr(755,root,root) %{_libdir}/libfsverity.so.0

%files -n libfsverity-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfsverity.so
%{_includedir}/libfsverity.h
%{_pkgconfigdir}/libfsverity.pc

%files -n libfsverity-static
%defattr(644,root,root,755)
%{_libdir}/libfsverity.a
