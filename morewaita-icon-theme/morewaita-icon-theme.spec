%global debug_package %{nil}

%define __reponame MoreWaita
%define __lowername %(echo %{__reponame} | tr '[:upper:]' '[:lower:]')

%define __urlver 49
%define _disable_source_fetch 0

Name:           %{__lowername}-icon-theme
Version:        %__urlver
Release:        1%{?dist}
Summary:        Adwaita-style extra icons theme for GNOME Shell

License:        GPL-3.0-or-later
URL:            https://github.com/somepaulo/%{__reponame}
Source0:        %{url}/archive/refs/tags/v%{__urlver}.tar.gz

Requires:       adwaita-icon-theme

%description
An expanded Adwaita-styled companion icon theme with extra icons for popular
apps and MIME types to complement Gnome Shell's original icons.

%prep
%autosetup -n %{__reponame}-%{__urlver}

%build
rm -rf _dev/

%install
install -d %{buildroot}%{_datadir}/icons/%{__reponame}
cp -r * %{buildroot}%{_datadir}/icons/%{__reponame}/

%files
%{_datadir}/icons/%{__reponame}/
