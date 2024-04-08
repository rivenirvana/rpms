%global debug_package   %{nil}
%global app_name        Soundux
%global app_uuid        io.github.%{app_name}.metainfo
%global repo_url        https://github.com/%{app_name}/%{app_name}
%global libtiny         libtiny-process-library.so

%bcond_with embedded

Name:           soundux
Version:        0.2.7
Release:        1%{?dist}
Summary:        A cross-platform soundboard
License:        GPLv3+
URL:            https://soundux.rocks

Source0:        %{repo_url}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel
BuildRequires:  libappindicator-gtk3-devel
BuildRequires:  libdwarf-devel
BuildRequires:  libwnck3-devel
BuildRequires:  libX11-devel
BuildRequires:  openssl-devel
BuildRequires:  pipewire-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  webkit2gtk3-devel

Requires:       libappindicator-gtk3
Requires:       libwnck3
Requires:       (pipewire or pulseaudio)
Requires:       redhat-lsb-core
Requires:       webkit2gtk3

Recommends:     ffmpeg
Recommends:     youtube-dl

%description
Soundux is a cross-platform soundboard that features a simple user interface.
With Soundux you can play audio to a specific application on Linux.

%prep
%autosetup -n %{app_name}

#sed -i -e "s/-Werror//g" -e "s/-Wno-gnu//g" -e "s/-Wno-unused-lambda-capture//g" CMakeLists.txt
#sed -i -e "s/-Werror//g" CMakeLists.txt

%build
%set_build_flags
%cmake \
    -DCMAKE_CXX_FLAGS="-include cstdint \
    -Wno-error=deprecated-declarations  \
    -fPIC $CXXFLAGS                     \
    %{?with_embedded:-DEMBED_PATH=ON}"
%cmake_build --config Release

%install
%cmake_install

install -Dm 0755 %{__cmake_builddir}/lib/tiny-process-library/%{libtiny} %{buildroot}/%{_libdir}/%{libtiny}
install -dm 0755 %{buildroot}/%{_bindir}
ln -s /opt/%{name}/%{name} %{buildroot}%{_bindir}/%{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_uuid}.xml

%files
%license LICENSE
%doc README.md
/opt/%{name}
%{_bindir}/%{name}
%{_libdir}/%{libtiny}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_metainfodir}/%{app_uuid}.xml

%changelog
* Mon Apr 08 2024 Arvin Verain <arvinverain@proton.me> - 0.2.7-1
- Initial COPR package
