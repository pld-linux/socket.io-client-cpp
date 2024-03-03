Summary:	Socket.IO C++ Client library
Summary(pl.UTF-8):	Biblioteka kliencka Socket.IO dla C++
Name:		socket.io-client-cpp
Version:	3.1.0
Release:	3
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/socketio/socket.io-client-cpp/releases
Source0:	https://github.com/socketio/socket.io-client-cpp/archive/%{version}/socket.io-client-cpp-%{version}.tar.gz
# Source0-md5:	942f8b519ec411cde08772f3cf83dd1e
Patch0:		socket.io-client-cpp-git.patch
Patch1:		socket.io-client-cpp-asio.patch
URL:		https://github.com/socketio/socket.io-client-cpp
BuildRequires:	asio-devel
BuildRequires:	cmake >= 2.8
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	openssl-devel
BuildRequires:	rapidjson-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	websocketpp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Socket.IO C++ Client library. Features:
- 100% written in modern C++11
- Binary support
- Automatic JSON encoding
- Multiplex support
- Similar API to the Socket.IO JS client
- Cross platform

%description -l pl.UTF-8
Biblioteka klienta Socket.IO C++. Cechy:
- napisana w 100% we współczesnym C++11
- obsługa trybu binarnego
- automatyczne kodowanie JSON
- obsługa multipleksowania
- API podobne do klienta Socket.IO dla JS
- wieloplatformowość

%package devel
Summary:	Header files for Socket.IO C++ Client library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki klienta Socket.IO dla C++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:4.7

%description devel
Header files for Socket.IO C++ Client library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki klienta Socket.IO dla C++.

%prep
%setup -q -n socket.io-client-cpp-%{version}
%patch0 -p1
%patch1 -p1

%build
install -d build
cd build
%cmake .. \
	-DBUILD_TESTING=OFF \
	-DUSE_SUBMODULES=OFF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -pr examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%attr(755,root,root) %{_libdir}/libsioclient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsioclient.so.3
%attr(755,root,root) %{_libdir}/libsioclient_tls.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsioclient_tls.so.3

%files devel
%defattr(644,root,root,755)
%doc API.md
%attr(755,root,root) %{_libdir}/libsioclient.so
%attr(755,root,root) %{_libdir}/libsioclient_tls.so
%{_includedir}/sio_client.h
%{_includedir}/sio_message.h
%{_includedir}/sio_socket.h
%{_libdir}/cmake/sioclient
%{_examplesdir}/%{name}-%{version}
