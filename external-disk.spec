Name:		external-disk
Version:	0.1
Release:	0%{?dist}
Summary:	Configures /etc/fstab for my portable hard drives

Group:		Admin
License:	GPLv3
URL:		http://github.com/jumanjiman/external-disk
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
buildarch:	noarch

Requires:	udev
Requires:	cryptsetup-luks
Requires:	setup
Requires:	sed

%description


%prep
%setup -q


%build


%install
rm -rf %{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc src/COPYING
%config /etc/udev/rules.d/75-external-disk.rules


%changelog

