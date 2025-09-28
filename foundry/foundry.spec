%global commit  ce1e9ad4e05fdf0df926d0ff2471be38e9ded04a
%global shortc  %(c=%{commit}; echo ${c:0:7})

%global blurb   GNOME IDE in a box
%global lib     libfoundry
%global lib_gtk libfoundry-gtk

%global glib_ver            2.82
%global gom_ver             0.5.0
%global libdex_ver          1.1.alpha
%global json_glib_ver       1.8
%global gtk4_ver            4.20
%global gsv_ver             5.18
%global vte_ver             0.80
%global libpeas_ver         2.0
%global libgit2_ver         1.6
%global template_glib_ver   3.37.0
%global libcmark_ver        0.29.0
%global libspelling_ver     0.4

Name:           foundry
Version:        1.0.0
Release:        3.g%{shortc}%{?dist}
Summary:        %{blurb}

License:        LGPL-2.1-only
URL:            https://gitlab.gnome.org/GNOME/foundry
Source0:        %{url}/-/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  redhat-rpm-config libappstream-glib
BuildRequires:  meson gcc cmake

BuildRequires:  pkgconfig(gio-2.0) >= %{glib_ver}
BuildRequires:  pkgconfig(gom-1.0) >= %{gom_ver}
BuildRequires:  pkgconfig(libdex-1) >= %{libdex_ver}
BuildRequires:  pkgconfig(json-glib-1.0) >= %{json_glib_ver}
BuildRequires:  pkgconfig(gtk4) >= %{gtk4_ver}
BuildRequires:  pkgconfig(gtksourceview-5) >= %{gsv_ver}
BuildRequires:  pkgconfig(vte-2.91-gtk4) >= %{vte_ver}
BuildRequires:  pkgconfig(libpeas-2) >= %{libpeas_ver}
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(libgit2) >= %{libgit2_ver}
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(template-glib-1.0) >= %{template_glib_ver}
BuildRequires:  pkgconfig(libcmark) >= %{libcmark_ver}
BuildRequires:  pkgconfig(webkitgtk-6.0)
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(editorconfig)
BuildRequires:  pkgconfig(libspelling-1) >= %{libspelling_ver}
BuildRequires:  pkgconfig(gobject-introspection-1.0)

%description
This tool aims to extract much of what makes GNOME Builder an IDE into a
library and companion command-line tool.


%package -n %{lib}
Summary:    Library for %{name}

%description -n %{lib}
%{blurb}.

%{summary}.


%package -n %{lib}-devel
Summary:    Development headers for %{lib}

%description -n %{lib}-devel
%{blurb}.

%{summary}.


%package -n %{lib_gtk}
Summary:    GTK library for %{name}

%description -n %{lib_gtk}
%{blurb}.

%{summary}.


%package -n %{lib_gtk}-devel
Summary:    Development headers for %{lib_gtk}

%description -n %{lib_gtk}-devel
%{blurb}.

%{summary}.


%prep
%autosetup -n %{name}-%{commit}


%build
%meson
%meson_build


%install
%meson_install

install -Dpm 0644 data/bash-completion/%{name} '%{buildroot}%{zsh_completions_dir}/_%{name}'


%check
%meson_test

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files
%doc NEWS README.md
%license COPYING
%{_bindir}/%{name}
%{_metainfodir}/app.devsuite.Foundry.metainfo.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/language-defaults
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{bash_completions_dir}/%{name}
%{zsh_completions_dir}/_%{name}

%files -n %{lib}
%{_libdir}/%{lib}-1.so*
%{_libdir}/girepository-1.0/Foundry-1.typelib

%files -n %{lib}-devel
%dir %{_includedir}/%{lib}-1
%{_includedir}/%{lib}-1/%{name}*.h
%dir %{_libdir}/%{lib}-1
%{_libdir}/%{lib}-1/include/%{lib}-config.h
%{_libdir}/pkgconfig/%{lib}-1.pc
%{_datadir}/gir-1.0/Foundry-1.gir

%files -n %{lib_gtk}
%{_libdir}/%{lib_gtk}-1.so*
%{_libdir}/girepository-1.0/FoundryGtk-1.typelib

%files -n %{lib_gtk}-devel
%dir %{_includedir}/%{lib_gtk}-1
%{_includedir}/%{lib_gtk}-1/%{name}*.h
%{_libdir}/pkgconfig/%{lib_gtk}-1.pc
%{_datadir}/gir-1.0/FoundryGtk-1.gir


%changelog
%autochangelog
