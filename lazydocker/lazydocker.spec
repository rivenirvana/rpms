%bcond check 0

%global debug_package %{nil}

%global gomodulesmode GO111MODULE=on
%global goipath github.com/jesseduffield/lazydocker
Version:        0.24.4
%global commit  577797d9ed11463f220c0c5d0acb86b521c1d21d

%gometa -L -f

%global golicenses  LICENSE
%global godocs      README.md CONTRIBUTING.md CODE-OF-CONDUCT.md docs

Name:           lazydocker
Release:        2%{?dist}
Summary:        The lazier way to manage everything docker

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

BuildRequires:  golang >= 1.22

%description
A simple terminal UI for both docker and docker-compose, written in Go with the
gocui library.

Memorising docker commands is hard. Memorising aliases is slightly less hard.
Keeping track of your containers across multiple terminal windows is near
impossible. What if you had all the information you needed in one terminal
window with every common command living one keypress away (and the ability to
add custom commands as well). Lazydocker's goal is to make that dream a reality.

%prep
%goprep

%build
export LDFLAGS="-X main.version=%{version} \
                -X main.commit=%{commit} \
                -X main.date=%{lua: print(os.date("%Y%m%d"))} \
                -X main.buildSource=copr"

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
