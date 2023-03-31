%define major 1
%define clibname %mklibname woff2common %{major}
%define dlibname %mklibname woff2dec %{major}
%define elibname %mklibname woff2enc %{major}
%define devname %mklibname -d woff2
%define cdevname %mklibname -d woff2common
%define ddevname %mklibname -d woff2dec
%define edevname %mklibname -d woff2enc

Name:		woff2
Summary:	Library for handling fonts in the WOFF 2.0 format
Version:	1.0.2
Release:	2
Group:		System/Libraries
URL:		https://github.com/google/woff2
Source0:	https://github.com/google/woff2/archive/v%{version}/%{name}-%{version}.tar.gz
License:	MIT
BuildRequires:	cmake ninja
BuildRequires:	pkgconfig(libbrotlidec)
BuildRequires:	pkgconfig(libbrotlienc)

%description
Library for handling fonts in the WOFF 2.0 format

%package -n %{clibname}
Summary:	Library for handling fonts in the WOFF 2.0 format
Group:		System/Libraries

%description -n %{clibname}
Library for handling fonts in the WOFF 2.0 format

%files -n %{clibname}
%{_libdir}/libwoff2common.so.%{major}*

%package -n %{dlibname}
Summary:	Library for decoding fonts in the WOFF 2.0 format
Group:		System/Libraries
Requires:	%{clibname} = %{EVRD}

%description -n %{dlibname}
Library for decoding fonts in the WOFF 2.0 format

%files -n %{dlibname}
%{_libdir}/libwoff2dec.so.%{major}*

%package -n %{elibname}
Summary:	Library for encoding fonts in the WOFF 2.0 format
Group:		System/Libraries
Requires:	%{clibname} = %{EVRD}

%description -n %{elibname}
Library for encoding fonts in the WOFF 2.0 format

%files -n %{elibname}
%{_libdir}/libwoff2enc.so.%{major}*

%package -n %{devname}
Summary:	Development files for the WOFF 2.0 font handling library
Group:		Development/C++ and C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{ddevname} = %{EVRD}
Requires:	%{edevname} = %{EVRD}

%description -n %{devname}
Development files for the WOFF 2.0 font handling library

%files -n %{devname}
%{_libdir}/*.so

%package -n %{cdevname}
Summary:	Core development files for the WOFF 2.0 font handling library
Group:		Development/C++ and C

%description -n %{cdevname}
Core development files for the WOFF 2.0 font handling library

This package contains files needed by both the WOFF 2.0 decoder
and the WOFF 2.0 encoder.

%files -n %{cdevname}
%{_libdir}/pkgconfig/libwoff2common.pc
%dir %{_includedir}/woff2

%package -n %{ddevname}
Summary:	Development files for the WOFF 2.0 font decoding library
Group:		Development/C++ and C
Requires:	%{cdevname} = %{EVRD}
Requires:	%{dlibname} = %{EVRD}

%description -n %{ddevname}
Development files for the WOFF 2.0 font decoding library

%files -n %{ddevname}
%{_libdir}/libwoff2dec.so
%{_libdir}/pkgconfig/libwoff2dec.pc
%{_includedir}/woff2/decode.h

%package -n %{edevname}
Summary:	Development files for the WOFF 2.0 font encoding library
Group:		Development/C++ and C
Requires:	%{cdevname} = %{EVRD}
Requires:	%{elibname} = %{EVRD}

%description -n %{edevname}
Development files for the WOFF 2.0 font encoding library

%files -n %{edevname}
%{_libdir}/libwoff2enc.so
%{_libdir}/pkgconfig/libwoff2enc.pc
%{_includedir}/woff2/encode.h
%{_includedir}/woff2/output.h

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
