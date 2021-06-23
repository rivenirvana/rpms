%global appname Komikku
%global uuid    info.febvre.%{appname}

Name:           komikku
Version:        0.29.2
Release:        2%{?dist}
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

# The conflict between python-magic and python-file-magic should be brought to FESCO
Requires:       python3dist(file-magic)

Requires:       python3-beautifulsoup4
Requires:       python3-brotli
Requires:       python3-cloudscraper
Requires:       python3-dateparser
Requires:       python3-gobject
Requires:       python3-keyring >= 21.6.0
Requires:       python3-lxml
Requires:       python3-natsort
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
* Wed Jun 23 2021 Arvin Verain <acverain@up.edu.ph> - 0.29.2-2
- Partial fix: BadAllocs for very large images
- Update server: ReadManhwa
- Chapter list: Add sorting by name

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
