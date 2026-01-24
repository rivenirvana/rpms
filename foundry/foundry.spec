%global commit  9ce615865138c0624ee70dfb0e2de65f066647c5
%global shortc  %(c=%{commit}; echo ${c:0:7})
%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           foundry
Version:        1.1~alpha
Release:        1.g%{shortc}%{?dist}
Summary:        %{blurb}

# foundry: LGPL-2.1-or-later
# bundled eggbitset / timsort: Apache-2.0
License:        LGPL-2.1-or-later AND Apache-2.0

URL:            https://gitlab.gnome.org/GNOME/foundry
Source:         %{url}/-/archive/%{commit}/%{name}-%{commit}.tar.gz

ExcludeArch:    %{ix86}

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  libappstream-glib

BuildRequires:  pkgconfig(editorconfig)
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(jsonrpc-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libcmark)
BuildRequires:  pkgconfig(libdex-1) >= 1.1~alpha
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(libpanel-1)
BuildRequires:  pkgconfig(libpeas-2)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libspelling-1)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  pkgconfig(template-glib-1.0)
BuildRequires:  pkgconfig(vte-2.91-gtk4)
BuildRequires:  pkgconfig(webkitgtk-6.0)
BuildRequires:  pkgconfig(yaml-0.1)

Requires:       libfoundry%{?_isa} = %{version}-%{release}

%global blurb   IDE library and command-line companion tool
%global _description %{expand:
This tool aims to extract much of what makes GNOME Builder an IDE into a
library and companion command-line tool.}

%description %{_description}

%package     -n libfoundry
Summary:        %{blurb} (shared library)

%description -n libfoundry %{_description}
This package contains the shared library.

%package     -n libfoundry-gtk
Summary:        %{blurb} (GTK integration)
Requires:       libfoundry%{?_isa} = %{version}-%{release}

%description -n libfoundry-gtk %{_description}
This package contains the shared library for GTK integration.

%package     -n libfoundry-adw
Summary:        %{blurb} (Adwaita integration)
Requires:       libfoundry%{?_isa} = %{version}-%{release}

%description -n libfoundry-adw %{_description}
This package contains the shared library for Adwaita integration.

%package     -n libfoundry-devel
Summary:        %{blurb} (development files)
Requires:       libfoundry%{?_isa} = %{version}-%{release}

%description -n libfoundry-devel %{_description}
This package contains the development headers for libfoundry.

%package     -n libfoundry-gtk-devel
Summary:        %{blurb} (development files)
Requires:       libfoundry-gtk%{?_isa} = %{version}-%{release}

%description -n libfoundry-gtk-devel %{_description}
This package contains the development headers for libfoundry-gtk.

%package     -n libfoundry-adw-devel
Summary:        %{blurb} (development files)
Requires:       libfoundry-adw%{?_isa} = %{version}-%{release}

%description -n libfoundry-adw-devel %{_description}
This package contains the development headers for libfoundry-adw.

%prep
%autosetup -n %{name}-%{commit}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}
install -Dpm 0644 data/bash-completion/%{name} '%{buildroot}%{zsh_completions_dir}/_%{name}'

%check
%meson_test
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files -f %{name}.lang
%doc NEWS README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_metainfodir}/org.gnome.Foundry.metainfo.xml
%{bash_completions_dir}/%{name}
%{zsh_completions_dir}/_%{name}

%files -n libfoundry
%{_libdir}/libfoundry-1.so*
%{_libdir}/girepository-1.0/Foundry-1.typelib
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/language-defaults
%{_datadir}/glib-2.0/schemas/*.gschema.xml

%files -n libfoundry-gtk
%{_libdir}/libfoundry-gtk-1.so*
%{_libdir}/girepository-1.0/FoundryGtk-1.typelib

%files -n libfoundry-adw
%{_libdir}/libfoundry-adw-1.so*
%{_libdir}/girepository-1.0/FoundryAdw-1.typelib

%files -n libfoundry-devel
%dir %{_includedir}/libfoundry-1
%{_includedir}/libfoundry-1/%{name}*.h
%{_libdir}/libfoundry-1.so
%dir %{_libdir}/libfoundry-1
%dir %{_libdir}/libfoundry-1/include
%{_libdir}/libfoundry-1/include/libfoundry-config.h
%{_libdir}/pkgconfig/libfoundry-1.pc
%{_datadir}/gir-1.0/Foundry-1.gir

%files -n libfoundry-gtk-devel
%dir %{_includedir}/libfoundry-gtk-1
%{_includedir}/libfoundry-gtk-1/%{name}*.h
%{_libdir}/libfoundry-gtk-1.so
%{_libdir}/pkgconfig/libfoundry-gtk-1.pc
%{_datadir}/gir-1.0/FoundryGtk-1.gir

%files -n libfoundry-adw-devel
%dir %{_includedir}/libfoundry-adw-1
%{_includedir}/libfoundry-adw-1/%{name}*.h
%{_libdir}/libfoundry-adw-1.so
%{_libdir}/pkgconfig/libfoundry-adw-1.pc
%{_datadir}/gir-1.0/FoundryAdw-1.gir

%changelog
%autochangelog
