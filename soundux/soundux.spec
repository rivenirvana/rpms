%global debug_package   %{nil}
%global app_name        Soundux
%global app_uuid        io.github.%{app_name}.metainfo
%global repo_url        https://github.com/%{app_name}/%{app_name}
%global libtiny         libtiny-process-library.so
%global httplib         cpp-httplib
%global httplib_ver     0.15.3
%global httplib_url     https://github.com/yhirose/%{httplib}

%bcond embedded 0

Name:           soundux
Version:        0.2.7
Release:        4%{?dist}
Summary:        A cross-platform soundboard
License:        GPLv3+
URL:            https://soundux.rocks

Source0:        %{repo_url}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        %{httplib_url}/archive/refs/tags/v%{httplib_ver}.tar.gz
Source2:        youtube-dl

Patch0:         webviewpp-build-fix.patch
Patch1:         guardpp-build-fix.patch
Patch2:         include.patch
Patch3:         desktop-exec.patch

BuildRequires:  cmake
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel
BuildRequires:  libappindicator-gtk3-devel
BuildRequires:  libappstream-glib
BuildRequires:  libdwarf-devel
BuildRequires:  libwnck3-devel
BuildRequires:  libX11-devel
BuildRequires:  openssl-devel
BuildRequires:  pipewire-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  webkit2gtk4.1-devel

Requires:       ffmpeg
Requires:       libappindicator-gtk3
Requires:       libwnck3
Requires:       (pipewire or pulseaudio)
Requires:       redhat-lsb
Requires:       yt-dlp

# Provide own youtube-dl script that uses yt-dlp compat
Conflicts:      youtube-dl

%description
Soundux is a cross-platform soundboard that features a simple user interface.
With Soundux you can play audio to a specific application on Linux.

%prep
%autosetup -p1 -n %{app_name}
rm -rf lib/%{httplib}
tar -xf %{SOURCE1} -C lib/
mv lib/%{httplib}-%{httplib_ver} lib/%{httplib}

%build
%set_build_flags
%cmake \
    -DCMAKE_BUILD_TYPE=Release          \
    -DCMAKE_CXX_FLAGS="-include cstdint \
    -Wno-error=deprecated-declarations  \
    -fPIC $CXXFLAGS                     \
    %{?with_embedded:-DEMBED_PATH=ON}"
%cmake_build --config Release

%install
%cmake_install

install -dm 0755 %{buildroot}%{_bindir}/
install -dm 0755 %{buildroot}%{_libdir}/
install -dm 0755 %{buildroot}%{_datadir}/%{name}
install -Dm 0755 %{__cmake_builddir}/lib/tiny-process-library/%{libtiny} %{buildroot}%{_libdir}/%{libtiny}
install -Dm 0755 %{__cmake_builddir}/soundux-%{version} %{buildroot}%{_datadir}/%{name}/%{name}-%{version}
install -Dm 0755 %{SOURCE2} %{buildroot}%{_bindir}/youtube-dl
ln -s %{_datadir}/%{name}/%{name}-%{version} %{buildroot}%{_datadir}/%{name}/%{name}
ln -s %{_datadir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}
cp -r %{buildroot}/opt/%{name}/dist/ %{buildroot}%{_datadir}/%{name}/dist/
rm -r %{buildroot}/opt

chrpath --delete %{buildroot}/%{_datadir}/%{name}/%{name}-%{version}

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_uuid}.xml

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/youtube-dl
%{_libdir}/%{libtiny}
%{_datadir}/%{name}/dist/
%{_datadir}/%{name}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_metainfodir}/%{app_uuid}.xml

%changelog
* Thu May 30 2024 Arvin Verain <arvinverain@proton.me> - 0.2.7-3
- Update spec

* Mon Apr 08 2024 Arvin Verain <arvinverain@proton.me> - 0.2.7-2
- Update spec

* Wed May 26 2021 Arvin Verain <arvinverain@proton.me> - 0.2.7-1
- Initial COPR package
