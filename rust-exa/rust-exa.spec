# Generated by rust2rpm 17
%bcond_without check
%global __cargo_skip_build 0
%global __cargo_is_lib() false

%global crate exa

Name:           rust-%{crate}
Version:        0.10.1
Release:        1%{?dist}
Summary:        Modern replacement for ls

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/exa
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
exa  is a modern replacement for the command-line program ls that ships
with Unix and Linux operating systems, with more features and better defaults.
It uses colours to distinguish file types and metadata.
It knows about symlinks, extended attributes, and Git. And it’s small, fast,
and just one single binary.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENCE
%doc README.md
%{_bindir}/exa
%{_mandir}/man1/exa.1*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/exa.bash
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/exa.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_exa

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 contrib/man/exa.1
install -Dpm0644 -T contrib/completions.bash \
  %{buildroot}%{_datadir}/bash-completion/completions/exa.bash
install -Dpm0644 -T contrib/completions.fish \
  %{buildroot}%{_datadir}/fish/vendor_completions.d/exa.fish
install -Dpm0644 -T contrib/completions.zsh \
  %{buildroot}%{_datadir}/zsh/site-functions/_exa

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Mon Jul 12 01:16:57 PST 2021 rivenirvana <acverain@up.edu.ph> - 0.10.1-1
- Initial package
