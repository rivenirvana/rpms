%global         debug_package   %{nil}

%global         jdk_ver         21
%global         gradle_ver      9.3.0

Name:           ghidra
Version:        12.0.1
Release:        1%{?dist}
Summary:        ghidra - Software reverse engineering (SRE) suite of tools

License:        Apache 2.0
URL:            https://ghidra-sre.org/
Source0:        https://github.com/NationalSecurityAgency/ghidra/archive/Ghidra_%{version}_build.tar.gz
Source1:        https://downloads.gradle.org/distributions/gradle-%{gradle_ver}-bin.zip
Source2:        ghidra.desktop

Requires:       (java-%{jdk_ver}-openjdk or temurin-%{jdk_ver}-jdk)
BuildRequires:  java-%{jdk_ver}-openjdk-devel
BuildRequires:  java-%{jdk_ver}-openjdk-headless
BuildRequires:  gcc gcc-c++
BuildRequires:  bison flex
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
BuildRequires:  python3-pip

%description
Ghidra is a software reverse engineering (SRE) framework developed
by NSA's Research Directorate for NSA's cybersecurity mission. It
helps analyze malicious code and malware like viruses, and can give
cybersecurity professionals a better understanding of potential
vulnerabilities in their networks and systems.

%package server
Summary:        Ghidra Server
Requires:       %{name}%{?_isa} = %{version}

%description server
Ghidra Server

%package docs
Summary:        Ghidra Documentation
Requires:       %{name}%{?_isa} = %{version}

%description docs
Ghidra Documentation

%prep
%autosetup -n ghidra-Ghidra_%{version}_build -a 1

JAVA_HOME=%{_jvmdir}/jre-%{jdk_ver}-openjdk \
    gradle-%{gradle_ver}/bin/gradle -I gradle/support/fetchDependencies.gradle

%build
JAVA_HOME=%{_jvmdir}/jre-%{jdk_ver}-openjdk \
    gradle-%{gradle_ver}/bin/gradle buildGhidra

%install
mkdir -p %{buildroot}%{_libdir}/%{name}/ %{buildroot}%{_bindir}/

unzip build/dist/ghidra_%{version}_DEV_%{lua: print(os.date("%Y%m%d"))}_linux*.zip
cp -r ghidra_%{version}_DEV/* %{buildroot}%{_libdir}/%{name}

ln -s %{_libdir}/%{name}/ghidraRun %{buildroot}%{_bindir}/%{name}

ln -s %{_libdir}/%{name}/server/ghidraSvr %{buildroot}%{_bindir}/%{name}-server
ln -s %{_libdir}/%{name}/server/svrAdmin %{buildroot}%{_bindir}/%{name}-server-admin
ln -s %{_libdir}/%{name}/server/svrInstall %{buildroot}%{_bindir}/%{name}-server-install
ln -s %{_libdir}/%{name}/server/svrUninstall %{buildroot}%{_bindir}/%{name}-server-uninstall

install -Dpm 0644 Ghidra/RuntimeScripts/Windows/support/ghidra.ico %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/ghidra.ico

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/ghidra.desktop
%{_datadir}/icons/hicolor/scalable/apps/ghidra.ico
%{_libdir}/%{name}/

%files server
%{_bindir}/%{name}-server
%{_bindir}/%{name}-server-admin
%{_bindir}/%{name}-server-install
%{_bindir}/%{name}-server-uninstall
%{_libdir}/%{name}/server/

%files docs
%{_libdir}/%{name}/docs/

%check

%changelog
%autochangelog
