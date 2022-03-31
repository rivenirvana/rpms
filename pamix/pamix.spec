%global packager rivenirvana
%global commit   1609e387ee37a5be53b457f5da9b67ac45c4be70
%global short    1609e38
%global date     20220401

Name:            pamix
Version:         1.6
Release:         4.%{date}git%{short}%{?dist}.%{packager}
Summary:         PulseAudio terminal mixer
License:         MIT
URL:             https://github.com/patroclos/PAmix
Source0:         %{url}/archive/%{commit}.tar.gz
BuildRequires:   cmake
BuildRequires:   pkg-config
BuildRequires:   gcc-c++
BuildRequires:   ncurses-devel
BuildRequires:   pulseaudio-libs-devel
# Libs are required automatically, server can be remote
Recommends:      pulseaudio

%description
PAmix is a simple, terminal-based mixer for PulseAudio inspired by pavucontrol.

%prep
%autosetup -n PAmix-%{commit}

%build
%cmake -DCMAKE_BUILD_TYPE=RELEASE -DWITH_UNICODE=1
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/xdg/%{name}.conf

%changelog
* Fri Apr 01 2022 Arvin Verain <acverain@up.edu.ph> - 1.6-4.20220401git1609e38
- Rebuild git-master - commit 1609e38

* Sat Nov 14 2020 Petr Šabata <contyk@redhat.com> - 1.6-1
- Initial packaging
