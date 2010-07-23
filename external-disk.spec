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
Adds entries to /etc/fstab and provides convenience scripts
specific to my personal external hard drives.


%prep
%setup -q


%build
# nothing to build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc/udev/rules.d/
mkdir -p %{buildroot}/usr/local/sbin/
install -m 644 src/75-external-disk.rules %{buildroot}/etc/udev/rules.d/
install -m 755 src/mount-luks %{buildroot}/usr/local/sbin/

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc src/COPYING
%config /etc/udev/rules.d/75-external-disk.rules
/usr/local/sbin/mount-luks


%changelog

