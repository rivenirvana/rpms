%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevkat
Version:        34.1.0
Release:        1%{?dist}
Summary:        Slender typeface for code, from code.

License:        SIL Open Font License Version 1.1
URL:            https://github.com/be5invis/Iosevka
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        private-build-plans.toml

BuildArch:      noarch

%if 0%{?fedora} > 43
BuildRequires:  nodejs22-npm-bin
%else
BuildRequires:  nodejs-npm
%endif
BuildRequires:  ttfautohint

%description
Iosevkat is an open-source, sans-serif + slab-serif, monospace + quasi‑proportional typeface family, designed for writing code, using in terminals, and preparing technical documents.

This is a custom build specifically for the kitty terminal.

%prep
%autosetup -n %{source_name}-%{version}
cp "%{SOURCE1}" ./

%package -n iosevkat-term-fonts
Summary:        Monospace, Default
%description -n iosevkat-term-fonts
Iosevkat Monospace, Default

%build
npm install
npm run build -- ttf::IosevkatTerm

%clean
%{__rm} -rf %{buildroot}

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/IosevkatTerm/TTF/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevkat-term-fonts

%files -n iosevkat-term-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevkat-term-fonts

%changelog
%autochangelog
