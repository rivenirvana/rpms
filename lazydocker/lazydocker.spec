%global debug_package %{nil}
%bcond bundled 1
%if %{with bundled}
%global gomodulesmode GO111MODULE=on
%endif

%global commit  de40167712063b02cb74ff3c4137eaf4b421638a
%global goipath github.com/jesseduffield/lazydocker
%gometa -L -f

Name:       lazydocker
Version:    0.23.3
Release:    1%{?dist}
Summary:    Lazier way to manage everything docker

License:    MIT
URL:        %{gourl}
Source0:    %{gosource}

BuildRequires: golang >= 1.21
BuildRequires: go-md2man

%description
A simple terminal UI for both docker and docker-compose, written in Go with the
gocui library.

Memorising docker commands is hard. Memorising aliases is slightly less hard.
Keeping track of your containers across multiple terminal windows is near
impossible. What if you had all the information you needed in one terminal
window with every common command living one keypress away (and the ability to
add custom commands as well). Lazydocker's goal is to make that dream a reality.


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
GO_LDFLAGS="-X main.version=%{version}"
%gobuild -o %{gobuilddir}/bin/%{name} %{goipath}
go-md2man -in README.md -out %{name}.1


%install
install -Dpm 0755 %{gobuilddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1

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