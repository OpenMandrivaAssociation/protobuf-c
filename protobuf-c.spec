%global optflags %{optflags} -DPROTOBUF_USE_DLLS
%global build_ldflags %{build_ldflags} -Wl,--undefined-version

%define major 1
%define oldlibname %mklibname %{name} 1
%define libname %mklibname %{name}
%define devname %mklibname -d %{name}

Name:		protobuf-c
Version:	1.4.1
Release:	11
Summary:	C bindings for Google's Protocol Buffers
Group:		System/Libraries
License:	ASL 2.0
URL:		https://github.com/protobuf-c
Source0:	https://github.com/protobuf-c/protobuf-c/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:		protobuf-c-c++17.patch
Patch1:		protobuf-c-protobuf-22.1.patch
Patch2:		protobuf-c-1.4.1-protobuf-23.0.patch
BuildRequires:	cmake ninja
BuildRequires:	cmake(absl)
BuildRequires: 	pkgconfig(protobuf)

%description
Protocol Buffers are a way of encoding structured data in an efficient yet 
extensible format. This package provides a code generator and run-time
libraries to use Protocol Buffers from pure C (not C++).

It uses a modified version of protoc called protoc-c. 

%package -n %{libname}
Summary:	C bindings for Google's Protocol Buffers
Group:		System/Libraries
%rename %{oldlibname}

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
%configure

%build
%make_build

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
%{_includedir}/protobuf-c/protobuf-c.proto
%{_libdir}/libprotobuf-c.so
%{_libdir}/pkgconfig/libprotobuf-c.pc
