%global packager rivenirvana
%global commit   9b5e8d12b58f8a4ab42e0b61c22e8ed9ee54abb4
%global short    9b5e8d1
%global date     20220402

Name:           steamtinkerlaunch
Version:        9.2
Release:        1.%{date}git%{short}%{?dist}.%{packager}
Summary:        Wrapper tool for use with the Steam client for custom launch options

License:        GPLv3
URL:            https://github.com/frostworx/steamtinkerlaunch
Source0:        %{url}/archive/%{commit}.tar.gz
Patch0:         steamtinkerlaunch-build.patch

BuildArch:      noarch

BuildRequires:  make

Requires:       gawk bash git procps-ng unzip wget xdotool xprop xrandr vim-common xwininfo
Requires:       yad >= 7.2
Recommends:     strace gamemode mangohud winetricks vkBasalt net-toolsa scummvm gameconqueror
Recommends:     gamescope innoextract usbutils jq ImageMagick rsync p7zip

%description
Steam Tinker Launch is a Linux wrapper tool for use with the Steam client which
allows customizing and start tools and options for games quickly on the fly

%prep
%autosetup -n %{name}-%{commit}

%build

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install PREFIX=%{_prefix} BUILDROOT=%{buildroot}

%files
%license LICENSE
%doc README.md
%{_bindir}/steamtinkerlaunch
%{_datadir}/steamtinkerlaunch
%{_datadir}/applications/steamtinkerlaunch.desktop
%{_datadir}/icons/hicolor/scalable/apps/steamtinkerlaunch.svg

%changelog
* Sat Apr 02 2022 Arvin Verain <acverain@up.edu.ph> - 9.2-1.20220402git9b5e8d1
- Rebuild git-master - commit 9b5e8d1

* Fri Apr 01 2022 Arvin Verain <acverain@up.edu.ph> - 9.2-1.20220401git6d636c9
- Rebuild git-master - commit 6d636c9
