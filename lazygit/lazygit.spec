%global goipath github.com/jesseduffield/lazygit
%global commit  b2fd6128f66ae8907f1c9771a3a57f2c22467ac9
Version:    0.47.1
%gometa -L -f

%global golicenses  LICENSE
%global godocs      README.md CONTRIBUTING.md CODE-OF-CONDUCT.md docs

Name:       lazygit
Release:    1%{?dist}
Summary:    A simple terminal UI for git commands

License:    MIT
URL:        %{gourl}
Source0:    %{gosource}

BuildRequires: golang >= 1.22
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
%goprep

%build
echo $LDFLAGS
export LDFLAGS %{shrink:%{expand:
                "-X main.commit=%{commit}
                 -X main.date=%(echo %{release} | sed -E 's/.*\.([0-9]{8})git.*/\1/')
                 -X main.version=%{version}
                 -X main.buildSource=copr"
}}
echo $LDFLAGS

%gobuild -o %{gobuilddir}/%{name} %{goipath}
go-md2man -in README.md -out %{name}.1

%install
%gopkginstall
install -Dpm 0755 %{gobuilddir}/%{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%check
%gocheck

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
