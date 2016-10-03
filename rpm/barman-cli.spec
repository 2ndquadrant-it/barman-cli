%if 0%{?rhel} == 7
  %global pybasever 2.7
%else
  %if 0%{?fedora}>=21
    %global pybasever 2.7
  %else
    %global pybasever 2.6
  %endif
%endif

%if 0%{?rhel} == 5
%global with_python26 1
%endif

%if 0%{?with_python26}
%global __python_ver python26
%global __python %{_bindir}/python%{pybasever}
%global __os_install_post %{__multiple_python_os_install_post}
%else
%global __python_ver python
%endif

%global main_version 1.2
# comment out the next line if not a pre-release (use '#%%global ...')
#%%global extra_version a1
# Usually 1 - unique sequence for all pre-release version
%global package_release 1

%{!?pybasever: %define pybasever %(%{__python} -c "import sys;print(sys.version[0:3])")}
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Summary:	Client Utilities for Barman, Backup and Recovery Manager for PostgreSQL
Name:		barman-cli
Version:	%{main_version}
Release:	%{?extra_version:0.}%{package_release}%{?extra_version:.%{extra_version}}%{?dist}
License:	GPLv3
Group:		Applications/Databases
Url:		http://www.pgbarman.org/
Source0:	%{name}-%{version}%{?extra_version:%{extra_version}}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot-%(%{__id_u} -n)
BuildArch:	noarch
Vendor:		2ndQuadrant Italia Srl <info@2ndquadrant.it>
Requires:	python-abi = %{pybasever}, %{__python_ver}-argparse

%description
Client utilities for the integration of Barman in
PostgreSQL clusters.

Barman (Backup and Recovery Manager) is an open-source
administration tool for disaster recovery of PostgreSQL
servers written in Python.
It allows your organisation to perform remote backups of
multiple servers in business critical environments to
reduce risk and help DBAs during the recovery phase.

Barman is distributed under GNU GPL 3 and maintained
by 2ndQuadrant.

%prep
%setup -n %{name}-%{version}%{?extra_version:%{extra_version}} -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{python_sitelib}/barman_cli-%{version}%{?extra_version:%{extra_version}}-py%{pybasever}.egg-info
%{_bindir}/barman-wal-restore
%doc %{_mandir}/man1/barman-wal-restore.1.gz

%changelog
* Mon Oct  3 2016 - Marco Nenciarini <marco.nenciarini@2ndquadrant.it> 1.2-1
- New release 1.2-1
* Wed Sep 16 2016 - Francesco Canovai <francesco.canovai@2ndquadrant.it> 1.1-2
- Fixed dependency on python-argparse
* Wed Sep 14 2016 - Marco Nenciarini <marco.nenciarini@2ndquadrant.it> 1.1-1
- New release 1.1-1
