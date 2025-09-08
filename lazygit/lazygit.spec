%bcond test 0

%global gomodulesmode GO111MODULE=on
%global goipath github.com/jesseduffield/lazygit
Version:        0.55.0
%global commit  0d5a410114036e2151087e6a8cf5295cca317c16
%gometa -L -f

%global golicenses  LICENSE
%global godocs      README.md CONTRIBUTING.md CODE-OF-CONDUCT.md docs

Name:           lazygit
Release:        1%{?dist}
Summary:        A simple terminal UI for git commands

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

BuildRequires:  git-core
BuildRequires:  golang >= 1.24

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
%goprep

%build
export LDFLAGS=%{shrink:"-X main.commit=%{commit}
                         -X main.version=%{version}
                         -X main.date=%(echo %{release} | sed -E 's/.*\.([0-9]{8})git.*/\1/')
                         -X main.buildSource=copr"}

%gobuild -o %{gobuilddir}/%{name} %{goipath}

%install
install -Dpm 0755 %{gobuilddir}/%{name} %{buildroot}%{_bindir}/%{name}

%check
%if %{with test}
%gocheck
%endif

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/%{name}

%changelog
%autochangelog
