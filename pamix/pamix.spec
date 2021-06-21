Name:           pamix
Version:        1.6
Release:        2%{?dist}
Summary:        PulseAudio terminal mixer
License:        MIT
URL:            https://github.com/patroclos/PAmix
Source0:        %{url}/archive/master.tar.gz
BuildRequires:  cmake
BuildRequires:  pkg-config
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
BuildRequires:  pulseaudio-libs-devel
# Libs are required automatically, server can be remote
Recommends:     pulseaudio

%description
PAmix is a simple, terminal-based mixer for PulseAudio inspired by pavucontrol.

%prep
%autosetup -n PAmix-master

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
* Fri Dec 25 2020 Arvin Verain <acverain@up.edu.ph> - 1.6-2
- 90bd2ea - Use pkg-config to reliably find ncurses lib.
- 72d8189 - FIX: default XDG_CONFIG_DIRS directory
- 3476aa1 - Merge pull request #35 from Polynomial-C/master
- e203050 - Install: add openSUSE instructions
- fb4449c - Merge pull request #38 from avindra/patch-1
- e3bf53d - change default XDG_CONFIG_DIRS value when searching config file
- c2a8514 - Merge branch 'nilninull-master'
- c215da2 - Merge branch 'master' of github.com:patroclos/PAmix
- 4807a44 - remove redundant ncursesw include
- ea4ab3b - add pkg-config to build dependency list
- c15831c - fix bug preventing entries from being scrolled.
- 3f2215c - fix key binding for cards tab
- f815db4 - Merge pull request #42 from n51/fix_man_page
- fba4613 - Do not allow addVolume for CardEntry
- 3a59db5 - Merge pull request #45 from swegener/card-entry-volumeadd
- 07c9401 - Add installation instructions for Debian-likes, Nix and Void Linux
- a9013d0 - Add TOC entries for new installation instruction distros
- 1e45f22 - Use 25ms as escdelay
- 996034a - Fix typo weather->whether
- 2995c49 - Merge pull request #55 from joachimschmidt557/fix-weather-whether
- 807f5b1 - Fix typo h->l (vim keybinding) in man page
- a25f6d2 - Merge pull request #57 from joachimschmidt557/fix-typo-h-l
- 6aeaa2f - PAmix is now in Fedora stable (i.e. 32+)
- 3bb0aea - Merge pull request #67 from contyk/now-in-fedora
- bf4acb3 - Add Fedora to TOC

* Sat Nov 14 2020 Petr Šabata <contyk@redhat.com> - 1.6-1
- Initial packaging
