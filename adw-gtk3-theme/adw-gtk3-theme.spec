%global commit  be2889526d08116f90678f4c6d8c229c4390d0b9
%global shortc  %(c=%{commit}; echo ${c:0:7})

%global sass_v  1.97.3

Name:           adw-gtk3-theme
Version:        6.4
Release:        2.%{shortc}%{?dist}
Summary:        The theme from libadwaita ported to GTK-3
BuildArch:      noarch

License:        LGPL-2.1-only
URL:            https://github.com/lassekongo83/adw-gtk3
Source0:        %{url}/archive/%{commit}.tar.gz
Source1:        https://github.com/sass/dart-sass/releases/download/%{sass_v}/dart-sass-%{sass_v}-linux-x64.tar.gz

BuildRequires:  meson

%description
%{summary}.

%prep
%autosetup -n adw-gtk3-%{commit} -a 1

%build
PATH="$(pwd)/dart-sass:$PATH"
%meson --prefix=%{buildroot}%{_prefix}
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_datadir}/themes/adw-gtk3/
%{_datadir}/themes/adw-gtk3-dark/

%changelog
%autochangelog
