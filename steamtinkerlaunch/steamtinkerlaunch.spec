%global commit  6e5aba78c03e7e473dec243df5270bfc164613b6
%global shortc  %(c=%{commit}; echo ${c:0:7})

Name:           steamtinkerlaunch
Version:        12.12
Release:        22.g%{shortc}%{?dist}
Summary:        Linux wrapper tool for use with the Steam client for custom launch options and 3rd party programs

License:        GPLv3
URL:            https://github.com/sonic2kk/steamtinkerlaunch
Source0:        %{url}/archive/%{commit}.tar.gz
Patch0:         steamtinkerlaunch-no-sed-prefix.patch

BuildArch:      noarch

BuildRequires:  make

Requires:       gawk bash git procps-ng unzip wget xdotool xprop xrandr xxd xwininfo
Requires:       yad >= 7.2
Recommends:     strace gamemode mangohud winetricks vkBasalt net-tools scummvm gameconqueror
Recommends:     gamescope innoextract usbutils jq ImageMagick rsync p7zip

%description
Steam Tinker Launch is a versatile Linux wrapper tool for use with the Steam
client which allows for easy graphical configuration of game tools, such as
GameScope, MangoHud, modding tools and a bunch more. It supports both games
using Proton and native Linux games, and works on both X11 and Wayland.

%prep
%autosetup -p1 -n %{name}-%{commit}

%build

%install
%make_install PREFIX=%{buildroot}%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/steamtinkerlaunch
%{_datadir}/steamtinkerlaunch
%{_datadir}/applications/steamtinkerlaunch.desktop
%{_datadir}/icons/hicolor/scalable/apps/steamtinkerlaunch.svg

%changelog
%autochangelog
