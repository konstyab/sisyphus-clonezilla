Name: clonezilla
Version: 3.21.13
Release: alt1
BuildArch: noarch

Summary: Clonezilla is a partition and disk imaging/cloning program similar to True Image or Norton Ghost

License: GPLv2
Group: System/Configuration/Hardware
Url: http://clonezilla.org/

Packager: Sample Maintainer <samplemaintainer@altlinux.org>
%filter_from_requires /^\/.*/d
%filter_from_requires /^sysvinit.*/d
%filter_from_requires /^systemd.*/d
#BuildPreReq:
Source: %name-%version.tar
Requires: bash perl-base drbl partimage psmisc udpcast partclone ntfs-3g

%description
Clonezilla is a partition and disk imaging/cloning program similar
to True Image or Norton Ghost. It helps you to do system deployment,
bare metal backup and recovery. Two types of Clonezilla are available,
Clonezilla live and Clonezilla SE (server edition). Clonezilla live
is suitable for single machine backup and restore. While Clonezilla
SE is for massive deployment, it can clone many (40 plus!) computers
simultaneously. Clonezilla saves and restores only used blocks in the
hard disk. This increases the clone efficiency. With some high-end
hardware in a 42-node cluster, a multicast restoring at rate 8 GB/min
was reported


%prep
%setup

%build

%make_build

%install
%makeinstall_std



%find_lang %name
chmod +x %buildroot/usr/sbin/ocs-install-grub

%files -f %name.lang
%_bindir/*
/etc/drbl/*
/usr/sbin/*
/usr/share/clonezilla
/usr/share/drbl/*



%changelog
* Sun Dec 04 2016 Sample Maintainer <samplemaintainer@altlinux.org> 3.21.13-alt1
- initial build

