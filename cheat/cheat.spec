%global commit 7908a678dfb1dd52baabeeff6f567d6d586293fb
%global shortc %(c=%{commit}; echo ${c:0:7})

%global sheets_url    https://github.com/cheat/cheatsheets
%global sheets_commit 36bdb99dcfadde210503d8c2dcf94b34ee950e1d
%global sheets_shortc %(c=%{sheets_commit}; echo ${c:0:7})

# https://github.com/cheat/cheat
%global goipath     github.com/cheat/cheat
Version:            4.4.2
%global tag         4.4.2

%gometa

%global common_description %{expand:
Cheat allows you to create and view interactive cheatsheets on the command-
line. It was designed to help remind *nix system administrators of options for
commands that they use frequently, but not frequently enough to remember.}

%global golicenses  LICENSE.txt
%global godocs      README.md CONTRIBUTING.md cmd/cheat/docopt.txt

Name:           cheat
Release:        12%{?dist}
Summary:        Help for various commands and their use cases

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        %{sheets_url}/archive/%{sheets_commit}.tar.gz
Source2:        cheat-config-FEDORA.yml

BuildRequires:  golang(github.com/alecthomas/chroma/v2/quick)
BuildRequires:  golang(github.com/davecgh/go-spew/spew)
BuildRequires:  golang(github.com/docopt/docopt-go)
BuildRequires:  golang(github.com/go-git/go-git/v5)
BuildRequires:  golang(github.com/mattn/go-isatty)
BuildRequires:  golang(github.com/mgutz/ansi)
BuildRequires:  golang(github.com/mitchellh/go-homedir)
BuildRequires:  golang(gopkg.in/yaml.v3)

Recommends:     cheat-community-cheatsheets

%description
%{common_description}

# We wont use full versioned dependency because rpmdiff then complains about
# difference between noarch subpackages on different architectures
%package bash-completion
Summary: Bash completion support for %{name}
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
Requires: bash bash-completion

%description bash-completion
Files needed to support bash completion.

%package fish-completion
Summary: Fish completion support for %{name}
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
Requires: fish

%description fish-completion
Files needed to support fish completion.

%package zsh-completion
Summary: Zsh completion support for %{name}
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
Requires: zsh

%description zsh-completion
Files needed to support zsh completion.

%package community-cheatsheets
Summary:   Cheatsheets created by comunity for %{name}
URL:       %{sheets_url}
License:   CC0
BuildArch: noarch
Requires:  %{name} = %{version}-%{release}
Supplements:  cheat

%description community-cheatsheets
Cheatsheets for various programs created and maintained by the
community.

%gopkg

%prep
%goprep
tar -xf %{SOURCE1}

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
mkdir -m 0755 -p %{buildroot}%{_datadir}/bash-completion/completions
mkdir -m 0755 -p %{buildroot}%{_datadir}/fish/vendor_completions.d
mkdir -m 0755 -p %{buildroot}%{_datadir}/zsh/site-functions/

install -m 0644 -p scripts/cheat.bash %{buildroot}%{_datadir}/bash-completion/completions/cheat
install -m 0644 -p scripts/cheat.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/cheat.fish
install -m 0644 -p scripts/cheat.zsh %{buildroot}%{_datadir}/zsh/site-functions/_cheat

install -m 0755 -vd %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/cheat %{buildroot}%{_bindir}/

# Install cheatsheets
mkdir -m 0755 -p %{buildroot}%{_datadir}/cheat

for sheet in cheatsheets-%{sheets_commit}/* ; do
  if [[ -d "$sheet" ]]; then
    mkdir -m 0755 -p %{buildroot}%{_datadir}/cheat/"$sheet"
    for new_sheet in "cheatsheets-%{sheets_commit}/$sheet/"* ; do
      install -m 0644 -p $new_sheet "%{buildroot}%{_datadir}/cheat/$sheet/"
    done
  else
    install -m 0644 -p $sheet %{buildroot}%{_datadir}/cheat/
  fi
done

mkdir -m 0755 -p %{buildroot}%{_sysconfdir}/cheat
install -m 0644 -p %{SOURCE2} %{buildroot}%{_sysconfdir}/cheat/conf.yml

%check
%gocheck

%files
%license LICENSE.txt
%doc README.md CONTRIBUTING.md cmd/cheat/docopt.txt
%config(noreplace) %{_sysconfdir}/cheat/conf.yml
%{_bindir}/cheat

%files community-cheatsheets
%license cheatsheets-%{sheets_commit}/.github/LICENSE.txt
%{_datadir}/cheat/

%files bash-completion
%{_datadir}/bash-completion/completions/cheat

%files fish-completion
%{_datadir}/fish/vendor_completions.d/cheat.fish

%files zsh-completion
%{_datadir}/zsh/site-functions/_cheat

%gopkgfiles

%changelog
%autochangelog
