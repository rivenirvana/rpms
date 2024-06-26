# Generated by rust2rpm 26
%bcond_without check
%bcond_without bundled

%global crate eza

Name:           rust-eza
Version:        0.18.19
Release:        %autorelease
Summary:        Modern replacement for ls

License:        MIT
URL:            https://crates.io/crates/eza
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          eza-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * drop feature for statically linking with OpenSSL
# * drop unused, benchmark-only criterion dev-dependency
# * drop features that are specific to NixOS packaging
# * exclude files that are only useful for upstream development
Patch:          eza-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A modern replacement for ls.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# (MIT OR Apache-2.0) AND BSD-3-Clause AND GPL-2.0-only WITH GCC-exception-2.0 AND MIT
# Apache-2.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License:        MIT AND Apache-2.0 AND BSD-3-Clause AND GPL-2.0-only WITH GCC-exception-2.0 AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown

# exa is unmaintained upstream and was retired - development continued as eza
Obsoletes:      exa < 0.10.1-13

# exa was retired in Fedora 39 - remove Provides and Obsoletes in Fedora 41
Provides:       exa = %{version}-%{release}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENCE
%license LICENSE.dependencies
%doc CHANGELOG.md
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc INSTALL.md
%doc README.md
%doc SECURITY.md
%{_mandir}/man{1,5}/*.{1,5}*
%{_bindir}/eza
%{_bindir}/exa
%{bash_completions_dir}/eza
%{fish_completions_dir}/eza.fish
%{zsh_completions_dir}/_eza

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENCE
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/CODE_OF_CONDUCT.md
%doc %{crate_instdir}/CONTRIBUTING.md
%doc %{crate_instdir}/INSTALL.md
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/SECURITY.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+git-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+git-devel %{_description}

This package contains library source intended for building other packages which
use the "git" feature of the "%{crate}" crate.

%files       -n %{name}+git-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+git2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+git2-devel %{_description}

This package contains library source intended for building other packages which
use the "git2" feature of the "%{crate}" crate.

%files       -n %{name}+git2-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
sed -i -e 's/offline = true/offline = false/'            \
    -e '/\[source.local-registry\]/d'                    \
    -e '/directory = "\/usr\/share\/cargo\/registry"/d'  \
    -e '/\[source.crates-io\]/d'                         \
    -e '/registry = "https:\/\/crates.io"/d'             \
    -e '/replace-with = "local-registry"/d'              .cargo/config

%if %{without bundled}
%generate_buildrequires
%endif
%cargo_generate_buildrequires

%build
%cargo_build
# Refer to /usr/lib/rpm/macros.d/macros.cargo for macros modified. Only removed --offline flag.
# cargo_license_summary
%{__cargo} tree                                                     \
    -Z avoid-dev-deps                                               \
    --workspace                                                     \
    --edges no-build,no-dev,no-proc-macro                           \
    --no-dedupe                                                     \
    --target all                                                    \
    %{__cargo_parse_opts %{-n} %{-a} %{-f:-f%{-f*}}}                \
    --prefix none                                                   \
    --format "# {l}"                                                \
    | sed -e "s: / :/:g" -e "s:/: OR :g"                            \
    | sort -u
# cargo_license
%{__cargo} tree                                                     \
    -Z avoid-dev-deps                                               \
    --workspace                                                     \
    --edges no-build,no-dev,no-proc-macro                           \
    --no-dedupe                                                     \
    --target all                                                    \
    %{__cargo_parse_opts %{-n} %{-a} %{-f:-f%{-f*}}}                \
    --prefix none                                                   \
    --format "{l}: {p}"                                             \
    | sed -e "s: ($(pwd)[^)]*)::g" -e "s: / :/:g" -e "s:/: OR :g"   \
    | sort -u                                                       > LICENSE.dependencies

%install
%cargo_install
# create compatibility symlink for exa
ln -s eza %{buildroot}/%{_bindir}/exa
# install shell completions
install -Dpm 0644 completions/bash/eza -t %{buildroot}/%{bash_completions_dir}/
install -Dpm 0644 completions/fish/eza.fish -t %{buildroot}/%{fish_completions_dir}/
install -Dpm 0644 completions/zsh/_eza -t %{buildroot}/%{zsh_completions_dir}/
# install manpages
install -Dpm 0644 man/eza.1.md                    -t %{buildroot}/%{_mandir}/man1/
install -Dpm 0644 man/eza_colors-explanation.5.md -t %{buildroot}/%{_mandir}/man5/
install -Dpm 0644 man/eza_colors.5.md             -t %{buildroot}/%{_mandir}/man5/

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
