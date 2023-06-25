Summary:	Wrapper library to disable resource limits and other privilege dropping
Summary(pl.UTF-8):	Biblioteka obudowująca do wyłączania limitów zasobów i innego porzucania uprawnień
Name:		priv_wrapper
Version:	1.0.1
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	https://download.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
# Source0-md5:	e61bb05f98d8dc374fa4d3c1c6677e3a
URL:		https://cwrap.org/priv_wrapper.html
BuildRequires:	cmake >= 3.5.0
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
priv_wrapper aims to help running processes which are dropping
privileges or are restricting resources in test environments. A
disabled call always succeeds (i.e. returns 0) and does nothing.

%description -l pl.UTF-8
priv_wrapper ma pomóc przy uruchamianiu w testowych środowiskach
procesów porzucających uprawnienia lub ograniczających zasoby.
Wyłączone wywołania zawsze się udają (tj. zwracają 0) i nic nie
robią.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG.md README.md
%attr(755,root,root) %{_libdir}/libpriv_wrapper.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpriv_wrapper.so.0
%attr(755,root,root) %{_libdir}/libpriv_wrapper.so
%{_pkgconfigdir}/priv_wrapper.pc
%{_libdir}/cmake/priv_wrapper
%{_mandir}/man1/priv_wrapper.1*
