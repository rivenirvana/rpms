%bcond check 0

%global debug_package %{nil}

%global gomodulesmode GO111MODULE=on
%global goipath github.com/jesseduffield/lazygit
Version:        0.58.1
%global commit  19605ad47699888da471ddf17bd2ae6dbb1abf3a

%gometa -L -f

%global golicenses  LICENSE
%global godocs      README.md CONTRIBUTING.md CODE-OF-CONDUCT.md VISION.md docs

Name:           lazygit
Release:        4%{?dist}
Summary:        Simple terminal UI for git commands

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

BuildRequires:  golang >= 1.25

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
LDFLAGS=%{shrink:"-X main.version=%{version}
                  -X main.commit=%{commit}
                  -X main.date=%{lua: print(os.date("%Y%m%d"))}
                  -X main.buildSource=copr"}

%gobuild -o %{gobuilddir}/%{name} %{goipath}

%install
install -Dpm 0755 %{gobuilddir}/%{name} %{buildroot}%{_bindir}/%{name}

%if %{with check}
%check
%gocheck
%endif

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/%{name}

%changelog
%autochangelog
