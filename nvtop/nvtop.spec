%global commit 5e9d0456745efaf13cc6336e7d557583377ada28
%global shortc %(c=%{commit}; echo ${c:0:7})

Name:           nvtop
Version:        3.3.1
Release:        1.g%{shortc}%{?dist}
Summary:        GPU & Accelerator process monitoring for AMD, Apple, Huawei, Intel, NVIDIA and Qualcomm

License:        GPLv3
URL:            https://github.com/Syllo/nvtop

Source:         %{url}/archive/%{commit}/%{commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(systemd)

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib


%description
NVTOP stands for Neat Videocard TOP, a (h)top like task monitor for GPUs and
accelerators. It can handle multiple GPUs and print information about them in
a htop-familiar way.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake -DNVIDIA_SUPPORT=ON -DAMDGPU_SUPPORT=ON -DINTEL_SUPPORT=ON
%cmake_build

%install
%cmake_install


%files
%license COPYING
%doc README.markdown
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/%{name}.svg
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/io.github.syllo.nvtop.metainfo.xml

%changelog
%autochangelog
