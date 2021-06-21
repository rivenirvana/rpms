%global appname Komikku
%global uuid    info.febvre.%{appname}

Name:           komikku
Version:        0.29.2
Release:        1%{?dist}
Summary:        A manga, comic and BD reader for GNOME
BuildArch:      noarch

License:        GPLv3+
URL:            https://gitlab.com/valos/Komikku
Source0:        %{url}/-/archive/master/%{appname}-master.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.50.0
BuildRequires:  python3-devel >= 3.8
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.1
BuildRequires:  pkgconfig(libhandy-1) >= 1.2.1

Requires:       hicolor-icon-theme
Requires:       libhandy >= 1.2.1
Requires:       libnotify
Requires:       webkit2gtk3

Requires:       python3-beautifulsoup4
Requires:       python3-brotli
Requires:       python3-cloudscraper
Requires:       python3-dateparser
Requires:       python3-gobject
Requires:       python3-keyring >= 21.6.0
Requires:       python3-lxml

# The conflict between python-magic and python-file-magic should be brought to FESCO
Requires:       python3dist(file-magic)

Requires:       python3-pillow
Requires:       python3-pure-protobuf
Requires:       python3-unidecode

%description
Komikku is a manga, comic and BD reader for GNOME. It focuses on providing a clean, intuitive and responsive interface.

%prep
%setup -q -n %{appname}-master

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_datadir}/icons/hicolor/symbolic/*/*.svg
%{_metainfodir}/*.xml
%{python3_sitelib}/%{name}/

%changelog
* Thu Jun 10 2021 Arvin Verain <acverain@up.edu.ph> - 0.29.2-1
- Release 0.29.2-1

* Thu Jun 10 2021 Arvin Verain <acverain@up.edu.ph> - 0.29.1-3
- Improve servers: Mangadex, MangaKawaii

* Thu Jun 10 2021 Arvin Verain <acverain@up.edu.ph> - 0.29.1-2
- Fix server: MangaSee

* Sun Jun 06 2021 Arvin Verain <acverain@up.edu.ph> - 0.29.1-1
- Release 0.29.1-1

* Thu Jun 03 2021 Arvin Verain <acverain@up.edu.ph> - 0.29.0-1
- Release 0.29.0-1

* Wed Jun 02 2021 Arvin Verain <acverain@up.edu.ph> - 0.28.1-11
- Mangadex: Remove unnecessary login at this time
- Card: Default view to `Chapters page`

* Mon May 31 2021 Arvin Verain <acverain@up.edu.ph> - 0.28.1-10
- Refine Mangadex server commits

* Mon May 31 2021 Arvin Verain <acverain@up.edu.ph> - 0.28.1-9
- Fix server: Mangadex
- Improve server: JapScan
- Improve headless browser

* Sat May 29 2021 Arvin Verain <acverain@up.edu.ph> - 0.28.1-8
- Improve server: Manganelo

* Fri May 28 2021 Arvin Verain <acverain@up.edu.ph> - 0.28.1-7
- Fix server: Manganelo

* Thu May 27 2021 Arvin Verain <acverain@up.edu.ph> - 0.28.1-6
- Fix server: MangaHub

* Tue May 25 2021 Arvin Verain <acverain@up.edu.ph> - 0.28.1-5
- Update German translation

* Mon May 24 2021 Arvin Verain <acverain@up.edu.ph> - 0.28.1-4
- L10n: Sync `*.po` files
- Code cleanup

* Sun May 23 2021 Arvin Verain <acverain@up.edu.ph> - 0.28.1-3
- Fix Card shadows
- Fix Category management

* Thu May 20 2021 Arvin Verain <acverain@up.edu.ph> - 0.28.1-2
- Ellipsize category labels spanning more than 2 lines
- Fix typos

* Sun May 16 2021 Arvin Verain <acverain@up.edu.ph> - 0.28.1-1
- Release 0.28.1-1

* Sat May 15 2021 Arvin Verain <acverain@up.edu.ph> - 0.28.0-1
- Release 0.28.0-1

* Thu May 13 2021 Arvin Verain <acverain@up.edu.ph> - 0.27.0-19
- Leave chapter list selection mode when page is changed

* Thu May 13 2021 Arvin Verain <acverain@up.edu.ph> - 0.27.0-18
- Use `Handy.ViewSwitcherTitle` as Card title widget

* Wed May 12 2021 Arvin Verain <acverain@up.edu.ph> - 0.27.0-17
- Update German translation

* Wed May 12 2021 Arvin Verain <acverain@up.edu.ph> - 0.27.0-16
- Replace Card's `Gtk.StackSwitcher` for `Handy.ViewSwitcherBar`
- Update translations
- Prevent updating of comics from disabled servers
- Update server: MangaSee

* Tue May 11 2021 Arvin Verain <acverain@up.edu.ph> - 0.27.0-15
- Fix Library `Start Page`
- Code cleanup

* Tue May 11 2021 Arvin Verain <acverain@up.edu.ph> - 0.27.0-14
- Refine Explorer UI
- Update server: Scantrad France
- Add search toggle on Ctrl+F

* Sun May 09 2021 Arvin Verain <acverain@up.edu.ph> - 0.27.0-13
- Move Explorer to main window

* Wed May 05 2021 Arvin Verain <acverain@up.edu.ph> - 0.27.0-12
- Move Download Manager to main window

* Tue May 04 2021 Arvin Verain <acverain@up.edu.ph> - 0.27.0-11
- Move Categories Editor to main window
- Move Preferences to main window

* Mon May 03 2021 Arvin Verain <acverain@up.edu.ph> - 0.27.0-10
- Change searchbox from `Handy.HeaderBar` to `Handy.Searchbar`

* Sat May 01 2021 Arvin Verain <acverain@up.edu.ph> - 0.27.0-9
- Feature: Pin favorite servers

* Tue Apr 27 2021 Arvin Verain <acverain@up.edu.ph> - 0.27.0-8
- Add server: Dongman Manhua (ZH Hans)
- Improve server: Madara
- Improve component: Webtoon reader

* Sun Apr 25 2021 Arvin Verain <acverain@up.edu.ph> - 0.27.0-7
- Bump minimum version of dependency `libhandy` to 1.2.1 (packaged for F34 onwards for now)
- Improve Madara multi server: 24hRomance (EN), AkuManga (AR), ArazNovel (TR), Argos Scan (PT), Atikrost (TR)

* Thu Apr 22 2021 Arvin Verain <acverain@up.edu.ph> - 0.27.0-6
- Deprecate: `Gdk.cairo_surface_create_from_pixbuf` for native `create_cairo_surface_from_pixbuf`

* Mon Apr 19 2021 Arvin Verain <acverain@up.edu.ph> - 0.27.0-5
- Bugfix: Webtoon reader memory leak

* Sun Apr 18 2021 Arvin Verain <acverain@up.edu.ph> - 0.27.0-4
- Add server: CatManga (Black Cat Scanlations)
- Bugfix: Crashes with `Save Page` feature

* Tue Mar 13 2021 Arvin Verain <acverain@up.edu.ph> - 0.27.0-3
- Add Madara multi server: Aloalivn (EN), Apoll Comics (ES), Wakascan (FR)
- Bugfix: Explorer search filters

* Mon Apr 12 2021 Arvin Verain <acverain@up.edu.ph> - 0.27.0-2
- Release 0.27.0
- Bump minimum version of dependency `libhandy` to 1.2.0 (packaged for F34 onwards for now)
- Bump minimum version of dependency `python3` to 3.8
- Add Categories/Shelves feature to organize material
- Add servers: MangaFreak (EN), AllHentai (RU)
- Update servers
- Update translations
- Update tests
- General component bugfixes and UX improvements

* Tue Mar 02 2021 Arvin Verain <acverain@up.edu.ph> - 0.26.1-7
- 7ea638a6 - [Servers] MangaDex: Fix issue #120

* Tue Mar 02 2021 Arvin Verain <acverain@up.edu.ph> - 0.26.1-6
- 20eb6432 - [Servers] MangaDex: Partial revert of c6915daf
- 8a66f7ec - [L10n] Sync all .po files

* Mon Mar 01 2021 Arvin Verain <acverain@up.edu.ph> - 0.26.1-5
- 5d4f112c - Merge branch 'italian-translation' into 'master'
- cbf50d00 - Add network state detection
- ab8443f0 - [Servers] Login is now done at the moment when it's needed, and no longer at instantiation
- c6915daf - Used UTC time everywhere

* Fri Feb 26 2021 Arvin Verain <acverain@up.edu.ph> - 0.26.1-4
- 1cd851c8 -  [Servers] Add ability to sync read progress with server

* Fri Feb 12 2021 Arvin Verain <acverain@up.edu.ph> - 0.26.1-3
- 4160f254 - [Servers] MangaSee: Fix #116

* Wed Feb 10 2021 Arvin Verain <acverain@up.edu.ph> - 0.26.1-2
- ab7536ed - Code cleanup
- b917a5e7 - [Servers] Komga: Improve get_manga_data()
- 861b9897 - Merge branch 'german-translation' into 'master'
- 0db5a91d - [Servers] Add Read Comics Online (EN)

* Tue Feb 09 2021 Arvin Verain <acverain@up.edu.ph> - 0.26.1-1
- d040eaf1 -  New release 0.26.1

* Sat Feb 06 2021 Arvin Verain <acverain@up.edu.ph> - 0.26.0-2
- 6d7f8995 - [Preferences] BIG oops

* Thu Feb 04 2021 Arvin Verain <acverain@up.edu.ph> - 0.26.0-1
- bdac6ee3 - New release 0.26.0
- e363ac64 - [L10n] Sync all .po files
- 259cbf26 - Refine ac3edf09
- ac3edf09 - [Explorer] Add button to open servers' Website in browser
- 5158c59d - [Servers] NineManga: Update all base_url to https
- c54471ba - Refine b09e1786

* Wed Feb 03 2021 Arvin Verain <acverain@up.edu.ph> - 0.25.1-9
- b09e1786 - Renaming AddDialog to Explorer
- 5ec9a7f6 - [Add dialog] Card: Add last chapter

* Mon Feb 01 2021 Arvin Verain <acverain@up.edu.ph> - 0.25.1-8
- 2af19c75 - Refine 9d7f95a2
- 986ee96e - [Servers] Add View Comics (EN)
- 4171b06f - [Servers] Scan Manga: Update

* Sun Jan 31 2021 Arvin Verain <acverain@up.edu.ph> - 0.25.1-7
- 4225ddf8 - [Servers] MangaKawaii: Update
- 767f3336 - [Servers] Update default user agent

* Wed Jan 27 2021 Arvin Verain <acverain@up.edu.ph> - 0.25.1-6
- 8390e336 - Bump version of Python keyring library to 22.0.1
- 33647431 - [Keyring] Avoid creation of a new credential when a server credential is updated
- 7a4526ab - [Servers] Komga: Improve get_manga_data()

* Mon Jan 25 2021 Arvin Verain <acverain@up.edu.ph> - 0.25.1-5
- 291aee9e - Update README
- bf028324 - [Add dialog] Servers list: Add a 'key' icon when a server requires a user account
- 8cb8630b - [Servers] Refine 0c9f54e2
- 2876e41e - Refine ab6a92bc

* Mon Jan 25 2021 Arvin Verain <acverain@up.edu.ph> - 0.25.1-4
- 0c9f54e2 - [Servers] Add Komga
- d56770b9 - [Card] Chapters list: Display last page read number even if number of pages of the chapter are unknown
- ab6a92bc - [Servers/Settings] Add possibility to store an additional attribute 'address' in servers credentials

* Sat Jan 23 2021 Arvin Verain <acverain@up.edu.ph> - 0.25.1-3
- 55ae00f8 - [Servers] Webtoon: Add command line support

* Fri Jan 22 2021 Arvin Verain <acverain@up.edu.ph> - 0.25.1-2
- 66afd258 - [Servers] Refine 9d7f95a2
- fab1cab5 - [Servers] Refine 9d7f95a2

* Wed Jan 20 2021 Arvin Verain <acverain@up.edu.ph> - 0.25.1-1
- ee1ad718 - New release 0.25.1
- f74ea02c - Fixes an error/omission in 71327df0

* Tue Jan 19 2021 Arvin Verain <acverain@up.edu.ph> - 0.25.0-2
- deps: Update libhandy1

* Tue Jan 19 2021 Arvin Verain <acverain@up.edu.ph> - 0.25.0-1
- 7efe5478 - New release 0.25.0
- 37086f91 - [Servers] Scan Manga: Fix get_manga_data()
- 71327df0 - Fix circular import errors
- e49658ad - [Tests] Central de Mangás: Fix typo
- 991f7e9e - [Servers] Scantrad France: Fix images URLs

* Wed Jan 06 2021 Arvin Verain <acverain@up.edu.ph> - 0.24.0-4
- a84901ba - Refine 9d7f95a2

* Tue Jan 05 2021 Arvin Verain <acverain@up.edu.ph> - 0.24.0-3
- 929e67d0 - Merge branch 'dev-command-line-handler' into 'master'
- 9d7f95a2 - Added ability to add comics via the command line
- b5dc3d1d - [Servers] Add Scan Manga (FR)

* Thu Dec 24 2020 Arvin Verain <acverain@up.edu.ph> - 0.24.0-2
- 45101d37 - [Servers] Mangahub: Fix issue #107
- 27170725 - [Servers] MangaKawaii: Typo

* Thu Dec 17 2020 Arvin Verain <acverain@up.edu.ph> - 0.24.0-1
- 7f2aeee7 - New release 0.24.0

* Wed Dec 16 2020 Arvin Verain <acverain@up.edu.ph> - 0.23.0-16
- b9d439b2 - Remove Python Cloudscraper package dependency
- 0c77e286 - [Servers] Submanga: Update url

* Wed Dec 16 2020 Arvin Verain <acverain@up.edu.ph> - 0.23.0-15
- 581c0073 - Code cleanup

* Mon Nov 30 2020 Arvin Verain <acverain@up.edu.ph> - 0.23.0-14
- 3bfbfd11 - Refine 5827db54: Decrease of the file size: 80kb is a bit too much for a 24x24 logo
- adbaad57 - Merge branch 'hunlight-icon' into 'master'
- 5827db54 - [Servers] Add Hunlight Scans icon

* Sun Nov 29 2020 Arvin Verain <acverain@up.edu.ph> - 0.23.0-13
- 0d3cd494 - [Card] Refine 920fd5cc

* Sun Nov 29 2020 Arvin Verain <acverain@up.edu.ph> - 0.23.0-12
- f5d97b1b - Merge branch 'dev-qol' into 'master'
- 32e6e0c7 - [Card] Fix issue #101
- 920fd5cc - [Card] Handle key press events.

* Sat Nov 28 2020 Arvin Verain <acverain@up.edu.ph> - 0.23.0-11
- 57b0892d - Refine 74dd410d: Fix typo
- 58023e7e - Merge branch 'dev-servers' into 'master'
- 18c18d6c - Merge branch 'german-translation' into 'master'
- 7b92d61b - [Card] Chapters list: Fix issue #102
- 74dd410d - [Servers] Update Webtoon.
- c47ee2ab - [Tests] Improve README

* Fri Nov 27 2020 Arvin Verain <acverain@up.edu.ph> - 0.23.0-10
- c7b1fe85 - [Servers] Fix #100

* Thu Nov 26 2020 Arvin Verain <acverain@up.edu.ph> - 0.23.0-9
- 487e006d - [Card] The chapter `Reset` action is now proposed as soon as chapter pages are known

* Wed Nov 25 2020 Arvin Verain <acverain@up.edu.ph> - 0.23.0-8
- f3db064b - Refine d93c6ae4: Better calculation of paths to server logos

* Tue Nov 24 2020 Arvin Verain <acverain@up.edu.ph> - 0.23.0-7
- a397c163 - [L10n] Sync all .po files
- c4a623f5 - [Flatpak] Manifest: Update Libhandy version
- 8c67d9d4 - Update README
- 1733d6c2 - Update screenshots

* Mon Nov 23 2020 Arvin Verain <acverain@up.edu.ph> - 0.23.0-6
- cbe6a8f5 - Refine d93c6ae4: Forgotten file

* Mon Nov 23 2020 Arvin Verain <acverain@up.edu.ph> - 0.23.0-5
- *broken*
- d93c6ae4 - [Servers] Tranform modules into packages

* Sat Nov 21 2020 Arvin Verain <acverain@up.edu.ph> - 0.23.0-4
- f23e6de2 - Refine 1991b2d8

* Sat Nov 21 2020 Arvin Verain <acverain@up.edu.ph> - 0.23.0-3
- e5800c7c - [Servers] Add Read Comic Online (EN)

* Fri Nov 20 2020 Arvin Verain <acverain@up.edu.ph> - 0.23.0-2
- 1991b2d8 - [Library] Allow Selection mode while in search and search in Selection mode

* Fri Nov 20 2020 Arvin Verain <acverain@up.edu.ph> - 0.23.0-1
- 2b5814c8 - New release 0.23.0

* Wed Nov 18 2020 Lyes Saadi <fedora@lyes.eu> - 0.22.1-1
- Updating to 0.22.1

* Sun Nov 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.22.0-1
- build(update): 0.22.0

* Mon Oct 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.21.1-1
- build(update): 0.21.1

* Tue Sep 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.0-1
- Update to 0.20.0

* Sat Aug 08 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.19.0-1
- Update to 0.19.0

* Wed Jul 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.18.0-2
- Add new dep: python3-keyring

* Wed Jul 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.18.0-1
- Update to 0.18.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.17.0-2
- Add explicitly dep: libhandy1

* Fri May 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.17.0-1
- Update to 0.17.0
- Build with system libhandy-1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.16.0-2
- Rebuilt for Python 3.9

* Sun May 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.16.0-1
- Update to 0.16.0
- Bundle libhandy-1

* Fri Apr 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.15.0-1
- Update to 0.15.0

* Tue Apr 14 2020 Lyes Saadi <fedora@lyes.eu> - 0.14.0-3
- Compatibility with python3-file-magic

* Thu Apr 02 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.14.0-2
- Specify required version of 'python3-magic' | RHBZ#1790100#c9

* Thu Apr 02 2020 Lyes Saadi <fedora@lyes.eu> - 0.14.0-1
- Update to 0.14.0

* Sun Mar 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13.0-1
- Update to 0.13.0

* Fri Feb 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.11.1-1
- Initial package
