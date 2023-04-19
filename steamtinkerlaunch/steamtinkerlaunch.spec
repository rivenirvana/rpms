%global forgeurl https://github.com/sonic2kk/steamtinkerlaunch
%global branch master
%forgemeta -v -i

Name:           steamtinkerlaunch
Version:        12.12
Release:        %autorelease
Summary:        Wrapper tool for use with the Steam client for custom launch options

License:        GPLv3
#URL:            %{forgeurl}
URL:            https://github.com/sonic2kk/steamtinkerlaunch
#Source0:        %{forgesource}
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Patch0:         steamtinkerlaunch-build.patch

BuildArch:      noarch

BuildRequires:  make

Requires:       gawk bash git procps-ng unzip wget xdotool xprop xrandr vim-common xwininfo
Requires:       yad >= 7.2
Recommends:     strace gamemode mangohud winetricks vkBasalt net-tools scummvm gameconqueror
Recommends:     gamescope innoextract usbutils jq ImageMagick rsync p7zip

%description
Steam Tinker Launch is a Linux wrapper tool for use with the Steam client which
allows customizing and start tools and options for games quickly on the fly

%prep
%autosetup
#%forgeautosetup -v

%build

%install
%make_install PREFIX=%{_prefix} BUILDROOT=%{buildroot}

%files
%license LICENSE
%doc README.md
%{_bindir}/steamtinkerlaunch
%{_datadir}/steamtinkerlaunch
%{_datadir}/applications/steamtinkerlaunch.desktop
%{_datadir}/icons/hicolor/scalable/apps/steamtinkerlaunch.svg

%changelog
%autochangelog
