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

BuildRequires:  nodejs-npm
BuildRequires:  ttfautohint

%description
Iosevkat is an open-source, sans-serif + slab-serif, monospace + quasi‑proportional typeface family, designed for writing code, using in terminals, and preparing technical documents.

This is a custom build specifically for the kitty terminal.

%prep
%autosetup -n %{source_name}-%{version}
cp "%{SOURCE1}" ./

# Iosevkat — Monospace, Default
%package -n iosevkat-fonts
Summary:        Monospace, Default
%description -n iosevkat-fonts
Iosevkat Monospace, Default

%package -n iosevkat-term-fonts
Summary:        Monospace, Default
%description -n iosevkat-term-fonts
Iosevkat Monospace, Default

%package -n iosevkat-fixed-fonts
Summary:        Monospace, Default
%description -n iosevkat-fixed-fonts
Iosevkat Monospace, Default

%build
npm install
npm run build -- ttf::Iosevkat
npm run build -- ttf::IosevkatTerm
npm run build -- ttf::IosevkatFixed

%clean
%{__rm} -rf %{buildroot}

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/Iosevkat/TTF/*.ttf      -t %{buildroot}%{_datadir}/fonts/iosevkat-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/IosevkatTerm/TTF/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevkat-term-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/IosevkatFixed/TTF/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevkat-fixed-fonts

# Iosevkat — Monospace, Default
%files -n iosevkat-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevkat-fonts

%files -n iosevkat-term-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevkat-term-fonts

%files -n iosevkat-fixed-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevkat-fixed-fonts

%changelog
%autochangelog
