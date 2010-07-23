Name:		external-disk
Version:	0.1
Release:	4%{?dist}
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
requires:	bash >= 4.0
requires:	grep

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
install -m 755 src/umount-luks %{buildroot}/usr/local/sbin/

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc src/COPYING
%config /etc/udev/rules.d/75-external-disk.rules
/usr/local/sbin/mount-luks
/usr/local/sbin/umount-luks

%preun
sed -i "/^#EXTERNAL_DISK_BEGIN/,/^#EXTERNAL_DISK_END/d" /etc/fstab


%pre
cat >> /etc/fstab << EOF
#EXTERNAL_DISK_BEGIN
# caution: do not modify the lines between begin and end
# these lines are managed by the "external-disk" rpm

# unencrypted stuff
/dev/portable /media/portable vfat defaults 0 0
/dev/insecure /media/insecure ext3 defaults 0 0
# encrypted stuff
/dev/mapper/secure  /media/secure  ext3 noauto 0 0
/dev/mapper/voyager /media/voyager ext3 noauto 0 0

#EXTERNAL_DISK_END
EOF


%post


%postun


%verifyscript
# need to make this more robust
grep -q EXTERNAL_DISK /etc/fstab || {
  echo "Error: missing entries in /etc/fstab"
  exit 1
} >&2


%changelog
* Fri Jul 23 2010 Paul Morgan <jumanjiman@gmail.com> 0.1-4
- absolute paths in mount-luks and umount-luks
- mount-luks checks that mountpoint exists

* Fri Jul 23 2010 Paul Morgan <jumanjiman@gmail.com> 0.1-3
- quiet grep in umount-luks error check
- fixed logic in mount-luks

* Fri Jul 23 2010 Paul Morgan <jumanjiman@gmail.com> 0.1-2
- cleaned up spec file

* Fri Jul 23 2010 Paul Morgan <jumanjiman@gmail.com> 0.1-1
- added basic error checks to mount-luks
- added umount-luks script

* Fri Jul 23 2010 Paul Morgan <jumanjiman@gmail.com> 0.1-0
- initial packaging
