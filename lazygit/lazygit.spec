%global debug_package %{nil}

%bcond bundled 1
%if %{with bundled}
%global gomodulesmode GO111MODULE=on
%endif

%global commit  4ba85608c8f3f25051994d3a7dd45647f58b119c
%global goipath github.com/jesseduffield/lazygit
%gometa -L -f

Name:       lazygit
Version:    0.41.0
Release:    2%{?dist}
Summary:    Simple terminal UI for git commands

License:    MIT
URL:        %{gourl}
Source:     %{gosource}

BuildRequires: golang >= 1.21
BuildRequires: go-md2man

%description
A simple terminal UI for git commands, written in Go with the gocui library.

Rant time: You've heard it before, git is powerful, but what good is that
power when everything is so damn hard to do? Interactive rebasing requires you
to edit a goddamn TODO file in your editor? Are you kidding me? To stage part
of a file you need to use a command line program to step through each hunk and
if a hunk can't be split down any further but contains code you don't want to
stage, you have to edit an arcane patch file by hand? Are you KIDDING me?!
Sometimes you get asked to stash your changes when switching branches only to
realise that after you switch and unstash that there weren't even any
conflicts and it would have been fine to just checkout the branch directly?
YOU HAVE GOT TO BE KIDDING ME!

If you're a mere mortal like me and you're tired of hearing how powerful git
is when in your daily life it's a powerful pain in your ass, lazygit might be
for you.


%prep
%autosetup -p1 -n %{name}-%{commit}
%if %{without bundled}
%generate_buildrequires
export GOPATH=$(pwd):%{gopath}
%go_generate_buildrequires
%endif


%build
%if %{without bundled}
export GOPATH=$(pwd):%{gopath}
%endif
%gobuild -o %{gobuilddir}/bin/%{name} %{goipath}
go-md2man -in README.md -out %{name}.1


%install
install -Dm 0755 %{gobuilddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm 0644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1


%check
export %{gomodulesmode}
%if %{without bundled}
export GOPATH=$(pwd):%{gopath}
%endif
%gocheck


%files
%license LICENSE
%doc README.md CONTRIBUTING.md CODE-OF-CONDUCT.md docs
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
%autochangelog
