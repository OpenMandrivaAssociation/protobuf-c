%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Name:		protobuf-c
Version:	1.3.3
Release:	1
Summary:	C bindings for Google's Protocol Buffers
Group:		System/Libraries
License:	ASL 2.0
URL:		https://github.com/protobuf-c
Source0:	https://github.com/protobuf-c/protobuf-c/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: 	pkgconfig(protobuf)

%description
Protocol Buffers are a way of encoding structured data in an efficient yet 
extensible format. This package provides a code generator and run-time
libraries to use Protocol Buffers from pure C (not C++).

It uses a modified version of protoc called protoc-c. 

%package -n %{libname}
Summary:	C bindings for Google's Protocol Buffers
Group:		System/Libraries

%description -n %{libname}
This package contains protobuf-c libraries.

%package -n %{devname}
Summary:	Protocol Buffers C headers and libraries
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
This package contains protobuf-c headers and libraries.

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build

%check
make check

%install
%make_install

%files
%doc TODO LICENSE ChangeLog
%{_bindir}/protoc-c
%{_bindir}/protoc-gen-c

%files -n %{libname}
%{_libdir}/libprotobuf-c.so.%{major}*

%files -n %{devname}
%dir %{_includedir}/google
%{_includedir}/google/protobuf-c
%{_includedir}/protobuf-c/protobuf-c.h
%{_libdir}/libprotobuf-c.so
%{_libdir}/pkgconfig/libprotobuf-c.pc
