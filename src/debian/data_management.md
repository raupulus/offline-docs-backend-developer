---
title: Data management
source_url: https://www.debian.org/doc/manuals/debian-reference/_data_management
source_repo: https://salsa.debian.org/debian/debian-reference.git
source_ref: master
source_commit: b7239e647
source_path: 10_data_management.rawxml
technology: debian
version: 12 (Bookworm)
license: GPL-2.0-or-later
retrieved_at: '2026-09-15'
order: 110
---

## Data management

Tools and tips for managing binary and text data on the Debian system are described.

## Sharing, copying, and archiving

> [!WARNING]
> The uncoordinated write access to actively accessed devices and files from multiple processes must not be done to avoid the [race condition](https://en.wikipedia.org/wiki/Race_condition). [File locking](https://en.wikipedia.org/wiki/File_locking) mechanisms using `flock(1)` may be used to avoid it.

The security of the data and its controlled sharing have several aspects.

- The creation of data archive

- The remote storage access

- The duplication

- The tracking of the modification history

- The facilitation of data sharing

- The prevention of unauthorized file access

- The detection of unauthorized file modification

These can be realized by using some combination of tools.

- Archive and compression tools

- Copy and synchronization tools

- Network filesystems

- Removable storage media

- The secure shell

- The authentication system

- Version control system tools

- Hash and cryptographic encryption tools

### Archive and compression tools

Here is a summary of archive and compression tools available on the Debian system.

| package | popcon | size | extension | command | comment |
|:---|:---|:---|:---|:---|:---|
| `tar` | @-@popcon1@-@ | @-@psize1@-@ | `.tar` | `tar(1)` | the standard archiver (de facto standard) |
| `cpio` | @-@popcon1@-@ | @-@psize1@-@ | `.cpio` | `cpio(1)` | Unix System V style archiver, use with `find(1)` |
| `binutils` | @-@popcon1@-@ | @-@psize1@-@ | `.ar` | `ar(1)` | archiver for the creation of static libraries |
| `fastjar` | @-@popcon1@-@ | @-@psize1@-@ | `.jar` | `fastjar(1)` | archiver for Java (zip like) |
| `pax` | @-@popcon1@-@ | @-@psize1@-@ | `.pax` | `pax(1)` | new POSIX standard archiver, compromise between `tar` and `cpio` |
| `gzip` | @-@popcon1@-@ | @-@psize1@-@ | `.gz` | `gzip(1)`, `zcat(1)`, … | GNU [LZ77](https://en.wikipedia.org/wiki/LZ77_and_LZ78) compression utility (de facto standard) |
| `bzip2` | @-@popcon1@-@ | @-@psize1@-@ | `.bz2` | `bzip2(1)`, `bzcat(1)`, … | [Burrows-Wheeler block-sorting compression](https://en.wikipedia.org/wiki/Burrows-Wheeler_transform) utility with higher compression ratio than `gzip(1)` (slower than `gzip` with similar syntax) |
| `lzma` | @-@popcon1@-@ | @-@psize1@-@ | `.lzma` | `lzma(1)` | [LZMA](https://en.wikipedia.org/wiki/Lempel-Ziv-Markov_chain_algorithm) compression utility with higher compression ratio than `gzip(1)` (deprecated) |
| `xz-utils` | @-@popcon1@-@ | @-@psize1@-@ | `.xz` | `xz(1)`, `xzdec(1)`, … | [XZ](https://en.wikipedia.org/wiki/Xz) compression utility with higher compression ratio than `bzip2(1)` (slower than `gzip` but faster than `bzip2`; replacement for [LZMA](https://en.wikipedia.org/wiki/Lempel-Ziv-Markov_chain_algorithm) compression utility) |
| `p7zip` | @-@popcon1@-@ | @-@psize1@-@ | `.7z` | `7zr(1)`, `p7zip(1)` | [7-Zip](https://en.wikipedia.org/wiki/7-Zip) file archiver with high compression ratio ([LZMA](https://en.wikipedia.org/wiki/Lempel-Ziv-Markov_chain_algorithm) compression) |
| `p7zip-full` | @-@popcon1@-@ | @-@psize1@-@ | `.7z` | `7z(1)`, `7za(1)` | [7-Zip](https://en.wikipedia.org/wiki/7-Zip) file archiver with high compression ratio ([LZMA](https://en.wikipedia.org/wiki/Lempel-Ziv-Markov_chain_algorithm) compression and others) |
| `lzop` | @-@popcon1@-@ | @-@psize1@-@ | `.lzo` | `lzop(1)` | [LZO](https://en.wikipedia.org/wiki/Lempel-Ziv-Oberhumer) compression utility with higher compression and decompression speed than `gzip(1)` (lower compression ratio than `gzip` with similar syntax) |
| `zip` | @-@popcon1@-@ | @-@psize1@-@ | `.zip` | `zip(1)` | [InfoZIP](https://en.wikipedia.org/wiki/Info-ZIP): DOS archive and compression tool |
| `unzip` | @-@popcon1@-@ | @-@psize1@-@ | `.zip` | `unzip(1)` | [InfoZIP](https://en.wikipedia.org/wiki/Info-ZIP): DOS unarchive and decompression tool |

List of archive and compression tools

> [!WARNING]
> Do not set the "`$TAPE`" variable unless you know what to expect. It changes `tar(1)` behavior.

> [!NOTE]
> The gzipped `tar(1)` archive uses the file extension "`.tgz`" or "`.tar.gz`".

> [!NOTE]
> The xz-compressed `tar(1)` archive uses the file extension "`.txz`" or "`.tar.xz`".

> [!NOTE]
> Popular compression method in [FOSS](https://en.wikipedia.org/wiki/Free_and_open_source_software) tools such as `tar(1)` has been moving as follows: `gzip` → `bzip2` → `xz`

> [!NOTE]
> `cp(1)`, `scp(1)` and `tar(1)` may have some limitation for special files. `cpio(1)` is most versatile.

> [!NOTE]
> `cpio(1)` is designed to be used with `find(1)` and other commands and suitable for creating backup scripts since the file selection part of the script can be tested independently.

> [!NOTE]
> Internal structure of Libreoffice data files are "`.jar`" file which can be opened also by `unzip`.

> [!NOTE]
> The de-facto cross platform archive tool is `zip`. Use it as "`zip -rX`" to attain the maximum compatibility. Use also the "`-s`" option, if the maximum file size matters.

### Copy and synchronization tools

Here is a summary of simple copy and backup tools available on the Debian system.

| package | popcon | size | tool | function |
|:---|:---|:---|:---|:---|
| `coreutils` | @-@popcon1@-@ | @-@psize1@-@ | GNU cp | locally copy files and directories ("-a" for recursive) |
| `openssh-client` | @-@popcon1@-@ | @-@psize1@-@ | scp | remotely copy files and directories (client, "`-r`" for recursive) |
| `openssh-server` | @-@popcon1@-@ | @-@psize1@-@ | sshd | remotely copy files and directories (remote server) |
| `rsync` | @-@popcon1@-@ | @-@psize1@-@ | \- | 1-way remote synchronization and backup |
| `unison` | @-@popcon1@-@ | @-@psize1@-@ | \- | 2-way remote synchronization and backup |

List of copy and synchronization tools

Copying files with `rsync(8)` offers richer features than others.

- delta-transfer algorithm that sends only the differences between the source files and the existing files in the destination

- quick check algorithm (by default) that looks for files that have changed in size or in last-modified time

- "`--exclude`" and "`--exclude-from`" options similar to `tar(1)`

- "a trailing slash on the source directory" syntax that avoids creating an additional directory level at the destination.

> [!TIP]
> Execution of the `bkup` script mentioned in [A copy script for the data backup](#_a_copy_script_for_the_data_backup) with the "`-gl`" option under `cron(8)` should provide very similar functionality as Plan9's `dumpfs` for the static data archive.

> [!TIP]
> Version control system (VCS) tools in [List of version control system tools](#list-of-vcs) can function as the multi-way copy and synchronization tools.

### Idioms for the archive

Here are several ways to archive and unarchive the entire content of the directory "`./source`" using different tools.

GNU `tar(1)`:

    $ tar -cvJf archive.tar.xz ./source
    $ tar -xvJf archive.tar.xz

Alternatively, by the following.

    $ find ./source -xdev -print0 | tar -cvJf archive.tar.xz --null -F -

`cpio(1)`:

    $ find ./source -xdev -print0 | cpio -ov --null > archive.cpio; xz archive.cpio
    $ zcat archive.cpio.xz | cpio -i

### Idioms for the copy

Here are several ways to copy the entire content of the directory "`./source`" using different tools.

- Local copy: "`./source`" directory → "`/dest`" directory

- Remote copy: "`./source`" directory at local host → "`/dest`" directory at "`user@host.dom`" host

`rsync(8)`:

    # cd ./source; rsync -aHAXSv . /dest
    # cd ./source; rsync -aHAXSv . user@host.dom:/dest

You can alternatively use "a trailing slash on the source directory" syntax.

    # rsync -aHAXSv ./source/ /dest
    # rsync -aHAXSv ./source/ user@host.dom:/dest

Alternatively, by the following.

    # cd ./source; find . -print0 | rsync -aHAXSv0 --files-from=- . /dest
    # cd ./source; find . -print0 | rsync -aHAXSv0 --files-from=- . user@host.dom:/dest

GNU `cp(1)` and openSSH `scp(1)`:

    # cd ./source; cp -a . /dest
    # cd ./source; scp -pr . user@host.dom:/dest

GNU `tar(1)`:

    # (cd ./source && tar cf - . ) | (cd /dest && tar xvfp - )
    # (cd ./source && tar cf - . ) | ssh user@host.dom '(cd /dest && tar xvfp - )'

`cpio(1)`:

    # cd ./source; find . -print0 | cpio -pvdm --null --sparse /dest

You can substitute "`.`" with "`foo`" for all examples containing "`.`" to copy files from "`./source/foo`" directory to "`/dest/foo`" directory.

You can substitute "`.`" with the absolute path "`/path/to/source/foo`" for all examples containing "`.`" to drop "`cd ./source;`". These copy files to different locations depending on tools used as follows.

- "`/dest/foo`": `rsync(8)`, GNU `cp(1)`, and `scp(1)`

- "`/dest/path/to/source/foo`": GNU `tar(1)`, and `cpio(1)`

> [!TIP]
> `rsync(8)` and GNU `cp(1)` have option "`-u`" to skip files that are newer on the receiver.

### Idioms for the selection of files

`find(1)` is used to select files for archive and copy commands (see [Idioms for the archive](#_idioms_for_the_archive) and [Idioms for the copy](#_idioms_for_the_copy)) or for `xargs(1)` (see [???](#_repeating_a_command_looping_over_files)). This can be enhanced by using its command arguments.

Basic syntax of `find(1)` can be summarized as the following.

- Its conditional arguments are evaluated from left to right.

- This evaluation stops once its outcome is determined.

- "Logical **OR**" (specified by "`-o`" between conditionals) has lower precedence than "logical **AND**" (specified by "`-a`" or nothing between conditionals).

- "Logical **NOT**" (specified by "`!`" before a conditional) has higher precedence than "logical **AND**".

- "`-prune`" always returns logical **TRUE** and, if it is a directory, searching of file is stopped beyond this point.

- "`-name`" matches the base of the filename with shell glob (see [???](#_shell_glob)) but it also matches its initial "`.`" with metacharacters such as "`*`" and "`?`". (New [POSIX](https://en.wikipedia.org/wiki/POSIX) feature)

- "`-regex`" matches the full path with emacs style **BRE** (see [???](#_regular_expressions)) as default.

- "`-size`" matches the file based on the file size (value precedented with "`+`" for larger, precedented with "`-`" for smaller)

- "`-newer`" matches the file newer than the one specified in its argument.

- "`-print0`" always returns logical **TRUE** and print the full filename ([null terminated](https://en.wikipedia.org/wiki/Null_character)) on the standard output.

`find(1)` is often used with an idiomatic style as the following.

    # find /path/to \
        -xdev -regextype posix-extended \
        -type f -regex ".*\.cpio|.*~" -prune -o \
        -type d -regex ".*/\.git" -prune -o \
        -type f -size +99M -prune -o \
        -type f -newer /path/to/timestamp -print0

This means to do following actions.

1.  Search all files starting from "`/path/to`"

2.  Globally limit its search within its starting filesystem and uses **ERE** (see [???](#_regular_expressions)) instead

3.  Exclude files matching regex of "`.*\.cpio`" or "`.*~`" from search by stop processing

4.  Exclude directories matching regex of "`.*/\.git`" from search by stop processing

5.  Exclude files larger than 99 Megabytes (units of 1048576 bytes) from search by stop processing

6.  Print filenames which satisfy above search conditions and are newer than "`/path/to/timestamp`"

Please note the idiomatic use of "`-prune -o`" to exclude files in the above example.

> [!NOTE]
> For non-Debian [Unix-like](https://en.wikipedia.org/wiki/Unix-like) system, some options may not be supported by `find(1)`. In such a case, please consider to adjust matching methods and replace "`-print0`" with "`-print`". You may need to adjust related commands too.

### Archive media

When choosing [computer data storage media](https://en.wikipedia.org/wiki/Computer_data_storage) for important data archive, you should be careful about their limitations. For small personal data backup, I use CD-R and DVD-R by the brand name company and store in a cool, shaded, dry, clean environment. (Tape archive media seem to be popular for professional use.)

> [!NOTE]
> [A fire-resistant safe](https://en.wikipedia.org/wiki/Safe) are meant for paper documents. Most of the computer data storage media have less temperature tolerance than paper. I usually rely on multiple secure encrypted copies stored in multiple secure locations.

Optimistic storage life of archive media seen on the net (mostly from vendor info).

- 100+ years : Acid free paper with ink

- 100 years : Optical storage (CD/DVD, CD/DVD-R)

- 30 years : Magnetic storage (tape, floppy)

- 20 years : Phase change optical storage (CD-RW)

These do not count on the mechanical failures due to handling etc.

Optimistic write cycle of archive media seen on the net (mostly from vendor info).

- 250,000+ cycles : Harddisk drive

- 10,000+ cycles : Flash memory

- 1,000 cycles : CD/DVD-RW

- 1 cycles : CD/DVD-R, paper

> [!CAUTION]
> Figures of storage life and write cycle here should not be used for decisions on any critical data storage. Please consult the specific product information provided by the manufacture.

> [!TIP]
> Since CD/DVD-R and paper have only 1 write cycle, they inherently prevent accidental data loss by overwriting. This is advantage!

> [!TIP]
> If you need fast and frequent backup of large amount of data, a hard disk on a remote host linked by a fast network connection, may be the only realistic option.

### Removable storage device

Removable storage devices may be any one of the following.

- [USB flash drive](https://en.wikipedia.org/wiki/USB_flash_drive)

- [Hard disk drive](https://en.wikipedia.org/wiki/Hard_disk_drive)

- [Optical disc drive](https://en.wikipedia.org/wiki/Optical_disc_drive)

- Digital camera

- Digital music player

They may be connected via any one of the following.

- [USB](https://en.wikipedia.org/wiki/Universal_Serial_Bus)

- [IEEE 1394 / FireWire](https://en.wikipedia.org/wiki/IEEE_1394)

- [PC Card](https://en.wikipedia.org/wiki/PC_card)

Modern desktop environments such as GNOME and KDE can mount these removable devices automatically without a matching "`/etc/fstab`" entry.

- `udisks` package provides a daemon and associated utilities to mount and unmount these devices.

- [D-bus](https://en.wikipedia.org/wiki/D-Bus) creates events to initiate automatic processes.

- [PolicyKit](https://en.wikipedia.org/wiki/PolicyKit) provides required privileges.

> [!TIP]
> Automounted devices may have the "`uhelper=`" mount option which is used by `umount(8)`.

> [!TIP]
> Automounting under modern desktop environment happens only when those removable media devices are not listed in "`/etc/fstab`".

Mount point under modern desktop environment is chosen as "`/media/<disk_label>`" which can be customized by the following.

- `mlabel(1)` for FAT filesystem

- `genisoimage(1)` with "`-V`" option for ISO9660 filesystem

- `tune2fs(1)` with "`-L`" option for ext2/ext3/ext4 filesystem

> [!TIP]
> The choice of encoding may need to be provided as mount option (see [???](#_filename_encoding)).

> [!TIP]
> The use of the GUI menu to unmount a filesystem may remove its dynamically generated device node such as "`/dev/sdc`". If you wish to keep its device node, unmount it with the `umount(8)` command from the shell prompt.

### Filesystem choice for sharing data

When sharing data with other system via removable storage device, you should format it with common [filesystem](https://en.wikipedia.org/wiki/File_system) supported by both systems. Here is a list of filesystem choices.

| filesystem | description of typical usage scenario |
|:---|:---|
| [FAT12](https://en.wikipedia.org/wiki/File_Allocation_Table) | cross platform sharing of data on the floppy disk (\<32MiB) |
| [FAT16](https://en.wikipedia.org/wiki/File_Allocation_Table) | cross platform sharing of data on the small hard disk like device (\<2GiB) |
| [FAT32](https://en.wikipedia.org/wiki/File_Allocation_Table) | cross platform sharing of data on the large hard disk like device (\<8TiB, supported by newer than MS Windows95 OSR2) |
| [NTFS](https://en.wikipedia.org/wiki/NTFS) | cross platform sharing of data on the large hard disk like device (supported natively on [MS Windows NT](https://en.wikipedia.org/wiki/Windows_NT) and later version, and supported by [NTFS-3G](https://en.wikipedia.org/wiki/NTFS-3G) via [FUSE](https://en.wikipedia.org/wiki/Filesystem_in_Userspace) on Linux) |
| [ISO9660](https://en.wikipedia.org/wiki/ISO_9660) | cross platform sharing of static data on CD-R and DVD+/-R |
| [UDF](https://en.wikipedia.org/wiki/Universal_Disk_Format) | incremental data writing on CD-R and DVD+/-R (new) |
| [MINIX filesystem](https://en.wikipedia.org/wiki/Minix_file_system) | space efficient unix file data storage on the floppy disk |
| [ext2 filesystem](https://en.wikipedia.org/wiki/Ext2) | sharing of data on the hard disk like device with older Linux systems |
| [ext3 filesystem](https://en.wikipedia.org/wiki/Ext3) | sharing of data on the hard disk like device with older Linux systems |
| [ext4 filesystem](https://en.wikipedia.org/wiki/Ext4) | sharing of data on the hard disk like device with current Linux systems |

List of filesystem choices for removable storage devices with typical usage scenarios

> [!TIP]
> See [???](#_removable_disk_encryption_with_dm_crypt_luks) for cross platform sharing of data using device level encryption.

The FAT filesystem is supported by almost all modern operating systems and is quite useful for the data exchange purpose via removable hard disk like media.

When formatting removable hard disk like devices for cross platform sharing of data with the FAT filesystem, the following should be safe choices.

- Partitioning them with `fdisk(8)`, `cfdisk(8)` or `parted(8)` (see [???](#_disk_partition_configuration)) into a single primary partition and to mark it as the following.

  - Type "6" for FAT16 for media smaller than 2GB.

  - Type "c" for FAT32 (LBA) for larger media.

- Formatting the primary partition with `mkfs.vfat(8)` with the following.

  - Just its device name, e.g. "`/dev/sda1`" for FAT16

  - The explicit option and its device name, e.g. "`-F 32 /dev/sda1`" for FAT32

When using the FAT or ISO9660 filesystems for sharing data, the following should be the safe considerations.

- Archiving files into an archive file first using `tar(1)`, or `cpio(1)` to retain the long filename, the symbolic link, the original Unix file permission and the owner information.

- Splitting the archive file into less than 2 GiB chunks with the `split(1)` command to protect it from the file size limitation.

- Encrypting the archive file to secure its contents from the unauthorized access.

> [!NOTE]
> For FAT filesystems by its design, the maximum file size is `(2^32 - 1) bytes = (4GiB - 1 byte)`. For some applications on the older 32 bit OS, the maximum file size was even smaller `(2^31 - 1) bytes = (2GiB - 1 byte)`. Debian does not suffer the latter problem.

> [!NOTE]
> Microsoft itself does not recommend to use FAT for drives or partitions of over 200 MB. Microsoft highlights its short comings such as inefficient disk space usage in their "[Overview of FAT, HPFS, and NTFS File Systems](http://support.microsoft.com/kb/100108/)". Of course, we should normally use the ext4 filesystem for Linux.

> [!TIP]
> For more on filesystems and accessing filesystems, please read "[Filesystems HOWTO](http://tldp.org/HOWTO/Filesystems-HOWTO.html)".

### Sharing data via network

When sharing data with other system via network, you should use common service. Here are some hints.

| network service | description of typical usage scenario |
|:---|:---|
| [SMB/CIFS](https://en.wikipedia.org/wiki/Server_Message_Block) network mounted filesystem with [Samba](https://en.wikipedia.org/wiki/Samba_(software)) | sharing files via "Microsoft Windows Network", see `smb.conf(5)` and [The Official Samba 3.x.x HOWTO and Reference Guide](http://www.samba.org/samba/docs/man/Samba-HOWTO-Collection/) or the `samba-doc` package |
| [NFS](https://en.wikipedia.org/wiki/Network_File_System_(protocol)) network mounted filesystem with the Linux kernel | sharing files via "Unix/Linux Network", see `exports(5)` and [Linux NFS-HOWTO](http://tldp.org/HOWTO/NFS-HOWTO/index.html) |
| [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) service | sharing file between the web server/client |
| [HTTPS](https://en.wikipedia.org/wiki/Https) service | sharing file between the web server/client with encrypted Secure Sockets Layer (SSL) or [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security) (TLS) |
| [FTP](https://en.wikipedia.org/wiki/File_Transfer_Protocol) service | sharing file between the FTP server/client |

List of the network service to chose with the typical usage scenario

Although these filesystems mounted over network and file transfer methods over network are quite convenient for sharing data, these may be insecure. Their network connection must be secured by the following.

- Encrypt it with [SSL/TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security)

- Tunnel it via [SSH](https://en.wikipedia.org/wiki/Secure_Shell)

- Tunnel it via [VPN](https://en.wikipedia.org/wiki/Virtual_private_network)

- Limit it behind the secure firewall

See also [???](#_other_network_application_servers) and [???](#_other_network_application_clients).

## Backup and recovery

We all know that computers fail sometime or human errors cause system and data damages. Backup and recovery operations are the essential part of successful system administration. All possible failure modes hit you some day.

> [!TIP]
> Keep your backup system simple and backup your system often. Having backup data is more important than how technically good your backup method is.

There are 3 key factors which determine actual backup and recovery policy.

1.  Knowing what to backup and recover.

    - Data files directly created by you: data in "`~/`"

    - Data files created by applications used by you: data in "`/var/`" (except "`/var/cache/`", "`/var/run/`", and "`/var/tmp/`")

    - System configuration files: data in "`/etc/`"

    - Local softwares: data in "`/usr/local/`" or "`/opt/`"

    - System installation information: a memo in plain text on key steps (partition, …)

    - Proven set of data: confirmed by experimental recovery operations in advance

2.  Knowing how to backup and recover.

    - Secure storage of data: protection from overwrite and system failure

    - Frequent backup: scheduled backup

    - Redundant backup: data mirroring

    - Fool proof process: easy single command backup

3.  Assessing risks and costs involved.

    - Value of data when lost

    - Required resources for backup: human, hardware, software, …

    - Failure mode and their possibility

> [!NOTE]
> Do not back up the pseudo-filesystem contents found on `/proc`, `/sys`, `/tmp`, and `/run` (see [???](#_procfs_and_sysfs) and [???](#_tmpfs)). Unless you know exactly what you are doing, they are huge useless data.

As for secure storage of data, data should be at least on different disk partitions preferably on different disks and machines to withstand the filesystem corruption. Important data are best stored on a write-once media such as CD/DVD-R to prevent overwrite accidents. (See [???](#_the_binary_data) for how to write to the storage media from the shell commandline. GNOME desktop GUI environment gives you easy access via menu: "Places→CD/DVD Creator".)

> [!NOTE]
> You may wish to stop some application daemons such as MTA (see [???](#_mail_transport_agent_mta)) while backing up data.

> [!NOTE]
> You should pay extra care to the backup and restoration of identity related data files such as "`/etc/ssh/ssh_host_dsa_key`", "`/etc/ssh/ssh_host_rsa_key`", "`~/.gnupg/*`", "`~/.ssh/*`", "`/etc/passwd`", "`/etc/shadow`", "`/etc/fetchmailrc`", "`popularity-contest.conf`", "`/etc/ppp/pap-secrets`", and "`/etc/exim4/passwd.client`". Some of these data can not be regenerated by entering the same input string to the system.

> [!NOTE]
> If you run a cron job as a user process, you must restore files in "`/var/spool/cron/crontabs`" directory and restart `cron(8)`. See [???](#_scheduling_tasks_regularly) for `cron(8)` and `crontab(1)`.

### Backup utility suites

Here is a select list of notable backup utility suites available on the Debian system.

| package | popcon | size | description |
|:---|:---|:---|:---|
| `dump` | @-@popcon1@-@ | @-@psize1@-@ | 4.4 [BSD](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution) `dump(8)` and `restore(8)` for [ext2](https://en.wikipedia.org/wiki/Ext2)/[ext3](https://en.wikipedia.org/wiki/Ext3)/[ext4](https://en.wikipedia.org/wiki/Ext4) filesystems |
| `xfsdump` | @-@popcon1@-@ | @-@psize1@-@ | dump and restore with `xfsdump(8)` and `xfsrestore(8)` for [XFS](https://en.wikipedia.org/wiki/XFS) filesystem on GNU/Linux and [IRIX](https://en.wikipedia.org/wiki/IRIX) |
| `backupninja` | @-@popcon1@-@ | @-@psize1@-@ | lightweight, extensible **meta-backup** system |
| `bacula-common` | @-@popcon1@-@ | @-@psize1@-@ | [Bacula](https://en.wikipedia.org/wiki/Bacula): network backup, recovery and verification - common support files |
| `bacula-client` | @-@popcon1@-@ | @-@psize1@-@ | [Bacula](https://en.wikipedia.org/wiki/Bacula): network backup, recovery and verification - client meta-package |
| `bacula-console` | @-@popcon1@-@ | @-@psize1@-@ | [Bacula](https://en.wikipedia.org/wiki/Bacula): network backup, recovery and verification - text console |
| `bacula-server` | @-@popcon1@-@ | @-@psize1@-@ | [Bacula](https://en.wikipedia.org/wiki/Bacula): network backup, recovery and verification - server meta-package |
| `amanda-common` | @-@popcon1@-@ | @-@psize1@-@ | [Amanda](https://en.wikipedia.org/wiki/Advanced_Maryland_Automatic_Network_Disk_Archiver): Advanced Maryland Automatic Network Disk Archiver (Libs) |
| `amanda-client` | @-@popcon1@-@ | @-@psize1@-@ | [Amanda](https://en.wikipedia.org/wiki/Advanced_Maryland_Automatic_Network_Disk_Archiver): Advanced Maryland Automatic Network Disk Archiver (Client) |
| `amanda-server` | @-@popcon1@-@ | @-@psize1@-@ | [Amanda](https://en.wikipedia.org/wiki/Advanced_Maryland_Automatic_Network_Disk_Archiver): Advanced Maryland Automatic Network Disk Archiver (Server) |
| `backup-manager` | @-@popcon1@-@ | @-@psize1@-@ | command-line backup tool |
| `backup2l` | @-@popcon1@-@ | @-@psize1@-@ | low-maintenance backup/restore tool for mountable media (disk based) |
| `backuppc` | @-@popcon1@-@ | @-@psize1@-@ | [BackupPC](https://en.wikipedia.org/wiki/Backuppc) is a high-performance, enterprise-grade system for backing up PCs (disk based) |
| `duplicity` | @-@popcon1@-@ | @-@psize1@-@ | (remote) incremental backup |
| `flexbackup` | @-@popcon1@-@ | @-@psize1@-@ | (remote) incremental backup |
| `rdiff-backup` | @-@popcon1@-@ | @-@psize1@-@ | (remote) incremental backup |
| `restic` | @-@popcon1@-@ | @-@psize1@-@ | (remote) incremental backup |
| `rsnapshot` | @-@popcon1@-@ | @-@psize1@-@ | (remote) incremental backup |
| `slbackup` | @-@popcon1@-@ | @-@psize1@-@ | (remote) incremental backup |

List of backup suite utilities

Backup tools have their specialized focuses.

- [Mondo Rescue](https://en.wikipedia.org/wiki/Mondo_Rescue) is a backup system to facilitate restoration of complete system quickly from backup CD/DVD etc. without going through normal system installation processes.

- Regular backups of user data can be realized by a simple script ([An example script for the system backup](#_an_example_script_for_the_system_backup)) and `cron(8)`.

- [Bacula](https://en.wikipedia.org/wiki/Bacula), [Amanda](https://en.wikipedia.org/wiki/Advanced_Maryland_Automatic_Network_Disk_Archiver), and [BackupPC](https://en.wikipedia.org/wiki/Backuppc) are full featured backup suite utilities which are focused on regular backups over network.

Basic tools described in [Archive and compression tools](#_archive_and_compression_tools) and [Copy and synchronization tools](#_copy_and_synchronization_tools) can be used to facilitate system backup via custom scripts. Such script can be enhanced by the following.

- The `restic` package enables incremental (remote) backups.

- The `rdiff-backup` package enables incremental (remote) backups.

- The `dump` package helps to archive and restore the whole filesystem incrementally and efficiently.

> [!TIP]
> See files in "`/usr/share/doc/dump/`" and ["Is dump really deprecated?"](http://dump.sourceforge.net/isdumpdeprecated.html) to learn about the `dump` package.

### An example script for the system backup

For a personal Debian desktop system running `unstable` suite, I only need to protect personal and critical data. I reinstall system once a year anyway. Thus I see no reason to backup the whole system or to install a full featured backup utility.

I use a simple script to make a backup archive and burn it into CD/DVD using GUI. Here is an example script for this.

    #!/bin/sh -e
    # Copyright (C) 2007-2008 Osamu Aoki <osamu@debian.org>, Public Domain
    BUUID=1000; USER=osamu # UID and name of a user who accesses backup files
    BUDIR="/var/backups"
    XDIR0=".+/Mail|.+/Desktop"
    XDIR1=".+/\.thumbnails|.+/\.?Trash|.+/\.?[cC]ache|.+/\.gvfs|.+/sessions"
    XDIR2=".+/CVS|.+/\.git|.+/\.svn|.+/Downloads|.+/Archive|.+/Checkout|.+/tmp"
    XSFX=".+\.iso|.+\.tgz|.+\.tar\.gz|.+\.tar\.bz2|.+\.cpio|.+\.tmp|.+\.swp|.+~"
    SIZE="+99M"
    DATE=$(date --utc +"%Y%m%d-%H%M")
    [ -d "$BUDIR" ] || mkdir -p "BUDIR"
    umask 077
    dpkg --get-selections \* > /var/lib/dpkg/dpkg-selections.list
    debconf-get-selections > /var/cache/debconf/debconf-selections

    {
    find /etc /usr/local /opt /var/lib/dpkg/dpkg-selections.list \
         /var/cache/debconf/debconf-selections -xdev -print0
    find /home/$USER /root -xdev -regextype posix-extended \
      -type d -regex "$XDIR0|$XDIR1" -prune -o -type f -regex "$XSFX" -prune -o \
      -type f -size  "$SIZE" -prune -o -print0
    find /home/$USER/Mail/Inbox /home/$USER/Mail/Outbox -print0
    find /home/$USER/Desktop  -xdev -regextype posix-extended \
      -type d -regex "$XDIR2" -prune -o -type f -regex "$XSFX" -prune -o \
      -type f -size  "$SIZE" -prune -o -print0
    } | cpio -ov --null -O $BUDIR/BU$DATE.cpio
    chown $BUUID $BUDIR/BU$DATE.cpio
    touch $BUDIR/backup.stamp

This is meant to be a script example executed from root.

I expect you to change and execute this as follows.

- Edit this script to cover all your important data (see [Idioms for the selection of files](#_idioms_for_the_selection_of_files) and [Backup and recovery](#_backup_and_recovery)).

- Replace "`find … -print0`" with "`find … -newer $BUDIR/backup.stamp -print0`" to make a incremental backup.

- Transfer backup files to the remote host using `scp(1)` or `rsync(1)` or burn them to CD/DVD for extra data security. (I use GNOME desktop GUI for burning CD/DVD. See [???](#_shell_script_example_with_zenity) for extra redundancy.)

Keep it simple!

> [!TIP]
> You can recover debconf configuration data with "`debconf-set-selections debconf-selections`" and dpkg selection data with "`dpkg --set-selection <dpkg-selections.list`".

### A copy script for the data backup

For the set of data under a directory tree, the copy with "`cp -a`" provides the normal backup.

For the set of large non-overwritten static data under a directory tree such as the one under the "`/var/cache/apt/packages/`" directory, hardlinks with "`cp -al`" provide an alternative to the normal backup with efficient use of the disk space.

Here is a copy script, which I named as `bkup`, for the data backup. This script copies all (non-VCS) files under the current directory to the dated directory on the parent directory or on a remote host.

    #!/bin/sh -e
    # Copyright (C) 2007-2008 Osamu Aoki <osamu@debian.org>, Public Domain
    fdot(){ find . -type d \( -iname ".?*" -o -iname "CVS" \) -prune -o -print0;}
    fall(){ find . -print0;}
    mkdircd(){ mkdir -p "$1";chmod 700 "$1";cd "$1">/dev/null;}
    FIND="fdot";OPT="-a";MODE="CPIOP";HOST="localhost";EXTP="$(hostname -f)"
    BKUP="$(basename $(pwd)).bkup";TIME="$(date  +%Y%m%d-%H%M%S)";BU="$BKUP/$TIME"
    while getopts gcCsStrlLaAxe:h:T f; do case $f in
    g)  MODE="GNUCP";; # cp (GNU)
    c)  MODE="CPIOP";; # cpio -p
    C)  MODE="CPIOI";; # cpio -i
    s)  MODE="CPIOSSH";; # cpio/ssh
    t)  MODE="TARSSH";; # tar/ssh
    r)  MODE="RSYNCSSH";; # rsync/ssh
    l)  OPT="-alv";; # hardlink (GNU cp)
    L)  OPT="-av";;  # copy (GNU cp)
    a)  FIND="fall";; # find all
    A)  FIND="fdot";; # find non CVS/ .???/
    x)  set -x;; # trace
    e)  EXTP="${OPTARG}";; # hostname -f
    h)  HOST="${OPTARG}";; # user@remotehost.example.com
    T)  MODE="TEST";; # test find mode
    \?) echo "use -x for trace."
    esac; done
    shift $(expr $OPTIND - 1)
    if [ $# -gt 0 ]; then
      for x in $@; do cp $OPT $x $x.$TIME; done
    elif [ $MODE = GNUCP ]; then
      mkdir -p "../$BU";chmod 700 "../$BU";cp $OPT . "../$BU/"
    elif [ $MODE = CPIOP ]; then
      mkdir -p "../$BU";chmod 700 "../$BU"
      $FIND|cpio --null --sparse -pvd ../$BU
    elif [ $MODE = CPIOI ]; then
      $FIND|cpio -ov --null | ( mkdircd "../$BU"&&cpio -i )
    elif [ $MODE = CPIOSSH ]; then
      $FIND|cpio -ov --null|ssh -C $HOST "( mkdircd \"$EXTP/$BU\"&&cpio -i )"
    elif [ $MODE = TARSSH ]; then
      (tar cvf - . )|ssh -C $HOST "( mkdircd \"$EXTP/$BU\"&& tar xvfp - )"
    elif [ $MODE = RSYNCSSH ]; then
      rsync -aHAXSv ./ "${HOST}:${EXTP}-${BKUP}-${TIME}"
    else
      echo "Any other idea to backup?"
      $FIND |xargs -0 -n 1 echo
    fi

This is meant to be command examples. Please read script and edit it by yourself before using it.

> [!TIP]
> I keep this `bkup` in my "`/usr/local/bin/`" directory. I issue this `bkup` command without any option in the working directory whenever I need a temporary snapshot backup.

> [!TIP]
> For making snapshot history of a source file tree or a configuration file tree, it is easier and space efficient to use `git(7)` (see [Git for recording configuration history](#_git_for_recording_configuration_history)).

## Data security infrastructure

The data security infrastructure is provided by the combination of data encryption tool, message digest tool, and signature tool.

| package | popcon | size | command | description |
|:---|:---|:---|:---|:---|
| `gnupg` | @-@popcon1@-@ | @-@psize1@-@ | `gpg(1)` | [GNU Privacy Guard](https://en.wikipedia.org/wiki/GNU_Privacy_Guard) - OpenPGP encryption and signing tool |
| `gpgv` | @-@popcon1@-@ | @-@psize1@-@ | `gpgv(1)` | GNU Privacy Guard - signature verification tool |
| `paperkey` | @-@popcon1@-@ | @-@psize1@-@ | `paperkey(1)` | extract just the secret information out of OpenPGP secret keys |
| `cryptsetup` | @-@popcon1@-@ | @-@psize1@-@ | `cryptsetup(8)`, … | utilities for [dm-crypto](https://en.wikipedia.org/wiki/Dm-crypt) block device encryption supporting [LUKS](https://en.wikipedia.org/wiki/Linux_Unified_Key_Setup) |
| `ecryptfs-utils` | @-@popcon1@-@ | @-@psize1@-@ | `ecryptfs(7)`, … | utilities for [ecryptfs](http://ecryptfs.sourceforge.net/) stacked filesystem encryption |
| `coreutils` | @-@popcon1@-@ | @-@psize1@-@ | `md5sum(1)` | compute and check MD5 message digest |
| `coreutils` | @-@popcon1@-@ | @-@psize1@-@ | `sha1sum(1)` | compute and check SHA1 message digest |
| `openssl` | @-@popcon1@-@ | @-@psize1@-@ | `openssl(1ssl)` | compute message digest with "`openssl dgst`" (OpenSSL) |

List of data security infrastructure tools

See [???](#_data_encryption_tips) on [dm-crypto](https://en.wikipedia.org/wiki/Dm-crypt) and [ecryptfs](http://ecryptfs.sourceforge.net/) which implement automatic data encryption infrastructure via Linux kernel modules.

### Key management for GnuPG

Here are [GNU Privacy Guard](https://en.wikipedia.org/wiki/GNU_Privacy_Guard) commands for the basic key management.

| command                       | description                             |
|:------------------------------|:----------------------------------------|
| `gpg --gen-key`               | generate a new key                      |
| `gpg --gen-revoke my_user_ID` | generate revoke key for my_user_ID      |
| `gpg --edit-key user_ID`      | edit key interactively, "help" for help |
| `gpg -o file --export`        | export all keys to file                 |
| `gpg --import file`           | import all keys from file               |
| `gpg --send-keys user_ID`     | send key of user_ID to keyserver        |
| `gpg --recv-keys user_ID`     | recv. key of user_ID from keyserver     |
| `gpg --list-keys user_ID`     | list keys of user_ID                    |
| `gpg --list-sigs user_ID`     | list sig. of user_ID                    |
| `gpg --check-sigs user_ID`    | check sig. of user_ID                   |
| `gpg --fingerprint user_ID`   | check fingerprint of user_ID            |
| `gpg --refresh-keys`          | update local keyring                    |

List of GNU Privacy Guard commands for the key management

Here is the meaning of the trust code.

| code | description of trust                         |
|:-----|:---------------------------------------------|
| `-`  | no owner trust assigned / not yet calculated |
| `e`  | trust calculation failed                     |
| `q`  | not enough information for calculation       |
| `n`  | never trust this key                         |
| `m`  | marginally trusted                           |
| `f`  | fully trusted                                |
| `u`  | ultimately trusted                           |

List of the meaning of the trust code

The following uploads my key "`1DD8D791`" to the popular keyserver "`hkp://keys.gnupg.net`".

    $ gpg --keyserver hkp://keys.gnupg.net --send-keys 1DD8D791

A good default keyserver set up in "`~/.gnupg/gpg.conf`" (or old location "`~/.gnupg/options`") contains the following.

    keyserver hkp://keys.gnupg.net

The following obtains unknown keys from the keyserver.

    $ gpg --list-sigs --with-colons | grep '^sig.*\[User ID not found\]' |\
      cut -d ':' -f 5| sort | uniq | xargs gpg --recv-keys

There was a bug in [OpenPGP Public Key Server](http://sourceforge.net/projects/pks/) (pre version 0.9.6) which corrupted key with more than 2 sub-keys. The newer `gnupg` (\>1.2.1-2) package can handle these corrupted subkeys. See `gpg(1)` under "`--repair-pks-subkey-bug`" option.

### Using GnuPG on files

Here are examples for using [GNU Privacy Guard](https://en.wikipedia.org/wiki/GNU_Privacy_Guard) commands on files.

| command | description |
|:---|:---|
| `gpg -a -s file` | sign file into [ASCII](https://en.wikipedia.org/wiki/ASCII) armored file.asc |
| `gpg --armor --sign file` | , , |
| `gpg --clearsign file` | clear-sign message |
| `gpg --clearsign file|mail foo@example.org` | mail a clear-signed message to `foo@example.org` |
| `gpg --clearsign --not-dash-escaped patchfile` | clear-sign patchfile |
| `gpg --verify file` | verify clear-signed file |
| `gpg -o file.sig -b file` | create detached signature |
| `gpg -o file.sig --detach-sig file` | , , |
| `gpg --verify file.sig file` | verify file with file.sig |
| `gpg -o crypt_file.gpg -r name -e file` | public-key encryption intended for name from file to binary crypt_file.gpg |
| `gpg -o crypt_file.gpg --recipient name --encrypt file` | , , |
| `gpg -o crypt_file.asc -a -r name -e file` | public-key encryption intended for name from file to [ASCII](https://en.wikipedia.org/wiki/ASCII) armored crypt_file.asc |
| `gpg -o crypt_file.gpg -c file` | symmetric encryption from file to crypt_file.gpg |
| `gpg -o crypt_file.gpg --symmetric file` | , , |
| `gpg -o crypt_file.asc -a -c file` | symmetric encryption intended for name from file to [ASCII](https://en.wikipedia.org/wiki/ASCII) armored crypt_file.asc |
| `gpg -o file -d crypt_file.gpg -r name` | decryption |
| `gpg -o file --decrypt crypt_file.gpg` | , , |

List of GNU Privacy Guard commands on files

### Using GnuPG with Mutt

Add the following to "`~/.muttrc`" to keep a slow GnuPG from automatically starting, while allowing it to be used by typing "`S`" at the index menu.

    macro index S ":toggle pgp_verify_sig\n"
    set pgp_verify_sig=no

### Using GnuPG with Vim

The `gnupg` plugin let you run GnuPG transparently for files with extension "`.gpg`", "`.asc`", and "`.ppg`".

    # aptitude install vim-scripts vim-addon-manager
    $ vim-addons install gnupg

### The MD5 sum

`md5sum(1)` provides utility to make a digest file using the method in [rfc1321](http://tools.ietf.org/html/rfc1321) and verifying each file with it.

    $ md5sum foo bar >baz.md5
    $ cat baz.md5
    d3b07384d113edec49eaa6238ad5ff00  foo
    c157a79031e1c40f85931829bc5fc552  bar
    $ md5sum -c baz.md5
    foo: OK
    bar: OK

> [!NOTE]
> The computation for the [MD5](https://en.wikipedia.org/wiki/MD5) sum is less CPU intensive than the one for the cryptographic signature by [GNU Privacy Guard (GnuPG)](https://en.wikipedia.org/wiki/GNU_Privacy_Guard). Usually, only the top level digest file is cryptographically signed to ensure data integrity.

## Source code merge tools

There are many merge tools for the source code. Following commands caught my eyes.

| package | popcon | size | command | description |
|:---|:---|:---|:---|:---|
| `diffutils` | @-@popcon1@-@ | @-@psize1@-@ | `diff(1)` | compare files line by line |
| `diffutils` | @-@popcon1@-@ | @-@psize1@-@ | `diff3(1)` | compare and merges three files line by line |
| `vim` | @-@popcon1@-@ | @-@psize1@-@ | `vimdiff(1)` | compare 2 files side by side in vim |
| `patch` | @-@popcon1@-@ | @-@psize1@-@ | `patch(1)` | apply a diff file to an original |
| `dpatch` | @-@popcon1@-@ | @-@psize1@-@ | `dpatch(1)` | manage series of patches for Debian package |
| `diffstat` | @-@popcon1@-@ | @-@psize1@-@ | `diffstat(1)` | produce a histogram of changes by the diff |
| `patchutils` | @-@popcon1@-@ | @-@psize1@-@ | `combinediff(1)` | create a cumulative patch from two incremental patches |
| `patchutils` | @-@popcon1@-@ | @-@psize1@-@ | `dehtmldiff(1)` | extract a diff from an HTML page |
| `patchutils` | @-@popcon1@-@ | @-@psize1@-@ | `filterdiff(1)` | extract or excludes diffs from a diff file |
| `patchutils` | @-@popcon1@-@ | @-@psize1@-@ | `fixcvsdiff(1)` | fix diff files created by CVS that `patch(1)` mis-interprets |
| `patchutils` | @-@popcon1@-@ | @-@psize1@-@ | `flipdiff(1)` | exchange the order of two patches |
| `patchutils` | @-@popcon1@-@ | @-@psize1@-@ | `grepdiff(1)` | show which files are modified by a patch matching a regex |
| `patchutils` | @-@popcon1@-@ | @-@psize1@-@ | `interdiff(1)` | show differences between two unified diff files |
| `patchutils` | @-@popcon1@-@ | @-@psize1@-@ | `lsdiff(1)` | show which files are modified by a patch |
| `patchutils` | @-@popcon1@-@ | @-@psize1@-@ | `recountdiff(1)` | recompute counts and offsets in unified context diffs |
| `patchutils` | @-@popcon1@-@ | @-@psize1@-@ | `rediff(1)` | fix offsets and counts of a hand-edited diff |
| `patchutils` | @-@popcon1@-@ | @-@psize1@-@ | `splitdiff(1)` | separate out incremental patches |
| `patchutils` | @-@popcon1@-@ | @-@psize1@-@ | `unwrapdiff(1)` | demangle patches that have been word-wrapped |
| `wiggle` | @-@popcon1@-@ | @-@psize1@-@ | `wiggle(1)` | apply rejected patches |
| `quilt` | @-@popcon1@-@ | @-@psize1@-@ | `quilt(1)` | manage series of patches |
| `meld` | @-@popcon1@-@ | @-@psize1@-@ | `meld(1)` | compare and merge files (GTK) |
| `dirdiff` | @-@popcon1@-@ | @-@psize1@-@ | `dirdiff(1)` | display differences and merge changes between directory trees |
| `docdiff` | @-@popcon1@-@ | @-@psize1@-@ | `docdiff(1)` | compare two files word by word / char by char |
| `imediff` | @-@popcon1@-@ | @-@psize1@-@ | `imediff(1)` | interactive full screen 2/3-way merge tool |
| `makepatch` | @-@popcon1@-@ | @-@psize1@-@ | `makepatch(1)` | generate extended patch files |
| `makepatch` | @-@popcon1@-@ | @-@psize1@-@ | `applypatch(1)` | apply extended patch files |
| `wdiff` | @-@popcon1@-@ | @-@psize1@-@ | `wdiff(1)` | display word differences between text files |

List of source code merge tools

### Extracting differences for source files

The following procedures extract differences between two source files and create unified diff files "`file.patch0`" or "`file.patch1`" depending on the file location.

    $ diff -u file.old file.new > file.patch0
    $ diff -u old/file new/file > file.patch1

### Merging updates for source files

The diff file (alternatively called patch file) is used to send a program update. The receiving party applies this update to another file by the following.

    $ patch -p0 file < file.patch0
    $ patch -p1 file < file.patch1

### Updating via 3-way-merge

If you have three versions of a source code, you can perform 3-way-merge effectively using `diff3(1)` by the following.

    $ diff3 -m file.mine file.old file.yours > file

## Version control systems

Here is a summary of the [version control systems (VCS)](https://en.wikipedia.org/wiki/Revision_control) on the Debian system.

> [!NOTE]
> If you are new to VCS systems, you should start learning with **Git**, which is growing fast in popularity.

| package | popcon | size | tool | VCS type | comment |
|:---|:---|:---|:---|:---|:---|
| `cssc` | @-@popcon1@-@ | @-@psize1@-@ | [CSSC](http://cssc.sourceforge.net/) | local | clone of the [Unix SCCS](https://en.wikipedia.org/wiki/Source_Code_Control_System) (deprecated) |
| `rcs` | @-@popcon1@-@ | @-@psize1@-@ | [RCS](https://en.wikipedia.org/wiki/Revision_Control_System) | local | "[Unix SCCS](https://en.wikipedia.org/wiki/Source_Code_Control_System) done right" |
| `cvs` | @-@popcon1@-@ | @-@psize1@-@ | [CVS](https://en.wikipedia.org/wiki/Concurrent_Versions_System) | remote | previous standard remote VCS |
| `subversion` | @-@popcon1@-@ | @-@psize1@-@ | [Subversion](https://en.wikipedia.org/wiki/Subversion_(software)) | remote | "CVS done right", the new de facto standard remote VCS |
| `git` | @-@popcon1@-@ | @-@psize1@-@ | [Git](https://en.wikipedia.org/wiki/Git_(software)) | distributed | fast DVCS in C (used by the Linux kernel and others) |
| `mercurial` | @-@popcon1@-@ | @-@psize1@-@ | [Mercurial](https://en.wikipedia.org/wiki/Mercurial_(software)) | distributed | DVCS in Python and some C |
| `bzr` | @-@popcon1@-@ | @-@psize1@-@ | [Bazaar](https://en.wikipedia.org/wiki/Bazaar_(software)) | distributed | DVCS influenced by `tla` written in Python (used by [Ubuntu](http://www.ubuntu.com/)) |
| `darcs` | @-@popcon1@-@ | @-@psize1@-@ | [Darcs](https://en.wikipedia.org/wiki/Darcs) | distributed | DVCS with smart algebra of patches (slow) |
| `tla` | @-@popcon1@-@ | @-@psize1@-@ | [GNU arch](https://en.wikipedia.org/wiki/GNU_arch) | distributed | DVCS mainly by Tom Lord (Historic) |
| `monotone` | @-@popcon1@-@ | @-@psize1@-@ | [Monotone](https://en.wikipedia.org/wiki/Monotone_(software)) | distributed | DVCS in C++ |
| `tkcvs` | @-@popcon1@-@ | @-@psize1@-@ | CVS, … | remote | GUI display of VCS (CVS, Subversion, RCS) repository tree |
| `gitk` | @-@popcon1@-@ | @-@psize1@-@ | Git | distributed | GUI display of VCS (Git) repository tree |

List of version control system tools {#list-of-vcs}

VCS is sometimes known as revision control system (RCS), or software configuration management (SCM).

Distributed VCS such as Git is the tool of choice these days. CVS and Subversion may still be useful to join some existing open source program activities.

Debian provides free Git services via [Debian Salsa service](https://salsa.debian.org/). Its documentation can be found at <https://wiki.debian.org/Salsa> .

> [!CAUTION]
> Debian has closed its old alioth services and the old alioth service data are available at [alioth-archive](https://alioth-archive.debian.org/) as tarballs.

There are few basics for creating a shared access VCS archive.

- Use "`umask 002`" (see [???](#_control_of_permissions_for_newly_created_files_umask))

- Make all VCS archive files belonging to a pertinent group

- Enable set group ID on all VCS archive directories (BSD-like file creation scheme, see [???](#_filesystem_permissions))

- Make user sharing the VCS archive belonging to the group

### Comparison of VCS commands

Here is an oversimplified comparison of native VCS commands to provide the big picture. The typical command sequence may require options and arguments.

| Git | CVS | Subversion | function |
|:---|:---|:---|:---|
| `git init` | `cvs init` | `svn create` | create the (local) repository |
| \- | `cvs login` | \- | login to the remote repository |
| `git clone` | `cvs co` | `svn co` | check out the remote repository as the working tree |
| `git pull` | `cvs up` | `svn up` | update the working tree by merging the remote repository |
| `git add .` | `cvs add` | `svn add` | add file(s) in the working tree to the VCS |
| `git rm` | `cvs rm` | `svn rm` | remove file(s) in working tree from the VCS |
| \- | `cvs ci` | `svn ci` | commit changes to the remote repository |
| `git commit -a` | \- | \- | commit changes to the local repository |
| `git push` | \- | \- | update the remote repository by the local repository |
| `git status` | `cvs status` | `svn status` | display the working tree status from the VCS |
| `git diff` | `cvs diff` | `svn diff` | diff \<reference_repository\> \<working_tree\> |
| `git repack -a -d; git prune` | \- | \- | repack the local repository into single pack |
| `gitk` | `tkcvs` | `tkcvs` | GUI display of VCS repository tree |

Comparison of native VCS commands

> [!CAUTION]
> Invoking a `git` subcommand directly as "`git-xyz`" from the command line has been deprecated since early 2006.

> [!TIP]
> If there is a executable file `git-foo` in the path specified by `$PATH`, entring "`git foo`" without hyphen to the command line invokes this `git-foo`. This is a feature of the `git` command.

> [!TIP]
> GUI tools such as `tkcvs(1)` and `gitk(1)` really help you with tracking revision history of files. The web interface provided by many public archives for browsing their repositories is also quite useful, too.

> [!TIP]
> Git can work directly with different VCS repositories such as ones provided by CVS and Subversion, and provides the local repository for local changes with `git-cvs` and `git-svn` packages. See [git for CVS users](http://www.kernel.org/pub/software/scm/git/docs/gitcvs-migration.html), and [Git for the Subversion repository](#_git_for_the_subversion_repository).

> [!TIP]
> Git has commands which have no equivalents in CVS and Subversion: "fetch", "rebase", "cherry-pick", …

## Git

Git can do everything for both local and remote source code management. This means that you can record the source code changes without needing network connectivity to the remote repository.

### Configuration of Git client

You may wish to set several global configuration in "`~/.gitconfig`" such as your name and email address used by Git by the following.

    $ git config --global user.name "Name Surname"
    $ git config --global user.email yourname@example.com

If you are too used to CVS or Subversion commands, you may wish to set several command aliases by the following.

    $ git config --global alias.ci "commit -a"
    $ git config --global alias.co checkout

You can check your global configuration by the following.

    $ git config --global --list

### Git references

See the following.

- [manpage: git(1)](http://www.kernel.org/pub/software/scm/git/docs/git.html) (`/usr/share/doc/git-doc/git.html`)

- [Git User's Manual](http://www.kernel.org/pub/software/scm/git/docs/user-manual.html) (`/usr/share/doc/git-doc/user-manual.html`)

- [A tutorial introduction to git](http://www.kernel.org/pub/software/scm/git/docs/gittutorial.html) (`/usr/share/doc/git-doc/gittutorial.html`)

- [A tutorial introduction to git: part two](http://www.kernel.org/pub/software/scm/git/docs/gittutorial-2.html) (`/usr/share/doc/git-doc/gittutorial-2.html`)

- [Everyday GIT With 20 Commands Or So](http://www.kernel.org/pub/software/scm/git/docs/everyday.html) (`/usr/share/doc/git-doc/everyday.html`)

- [git for CVS users](http://www.kernel.org/pub/software/scm/git/docs/gitcvs-migration.html) (`/usr/share/doc/git-doc/gitcvs-migration.html`)

  - This also describes how to set up server like CVS and extract old data from CVS into Git.

- [Other git resources available on the web](http://git-scm.com/documentation)

  - [Git - SVN Crash Course](http://git-scm.com/course/svn.html)

  - [Git Magic](http://www-cs-students.stanford.edu/~blynn/gitmagic/) (`/usr/share/doc/gitmagic/html/index.html`)

`git-gui(1)` and `gitk(1)` commands make using Git very easy.

> [!WARNING]
> Do not use the tag string with spaces in it even if some tools such as `gitk(1)` allow you to use it. It may choke some other `git` commands.

### Git commands

Even if your upstream uses different VCS, it may be a good idea to use `git(1)` for local activity since you can manage your local copy of source tree without the network connection to the upstream. Here are some packages and commands used with `git(1)`.

| package | popcon | size | command | description |
|:---|:---|:---|:---|:---|
| `git-doc` | @-@popcon1@-@ | @-@psize1@-@ | N/A | official documentation for Git |
| `gitmagic` | @-@popcon1@-@ | @-@psize1@-@ | N/A | "Git Magic", easier to understand guide for Git |
| `git` | @-@popcon1@-@ | @-@psize1@-@ | `git(7)` | Git, the fast, scalable, distributed revision control system |
| `gitk` | @-@popcon1@-@ | @-@psize1@-@ | `gitk(1)` | GUI Git repository browser with history |
| `git-gui` | @-@popcon1@-@ | @-@psize1@-@ | `git-gui(1)` | GUI for Git (No history) |
| `git-svn` | @-@popcon1@-@ | @-@psize1@-@ | `git-svnimport(1)` | import the data out of Subversion into Git |
| `git-svn` | @-@popcon1@-@ | @-@psize1@-@ | `git-svn(1)` | provide bidirectional operation between the Subversion and Git |
| `git-cvs` | @-@popcon1@-@ | @-@psize1@-@ | `git-cvsimport(1)` | import the data out of CVS into Git |
| `git-cvs` | @-@popcon1@-@ | @-@psize1@-@ | `git-cvsexportcommit(1)` | export a commit to a CVS checkout from Git |
| `git-cvs` | @-@popcon1@-@ | @-@psize1@-@ | `git-cvsserver(1)` | CVS server emulator for Git |
| `git-email` | @-@popcon1@-@ | @-@psize1@-@ | `git-send-email(1)` | send a collection of patches as email from the Git |
| `stgit` | @-@popcon1@-@ | @-@psize1@-@ | `stg(1)` | quilt on top of git (Python) |
| `git-buildpackage` | @-@popcon1@-@ | @-@psize1@-@ | `git-buildpackage(1)` | automate the Debian packaging with the Git |
| `guilt` | @-@popcon1@-@ | @-@psize1@-@ | `guilt(7)` | quilt on top of git (SH/AWK/SED/…) |

List of git related packages and commands

> [!TIP]
> With `git(1)`, you work on a local branch with many commits and use something like "`git rebase -i master`" to reorganize change history later. This enables you to make clean change history. See `git-rebase(1)` and `git-cherry-pick(1)`.

> [!TIP]
> When you want to go back to a clean working directory without loosing the current state of the working directory, you can use "`git stash`". See `git-stash(1)`.

### Git for the Subversion repository

You can check out a Subversion repository at "`svn+ssh://svn.example.org/project/module/trunk`" to a local Git repository at "`./dest`" and commit back to the Subversion repository. E.g.:

    $ git svn clone -s -rHEAD svn+ssh://svn.example.org/project dest
    $ cd dest
    ... make changes
    $ git commit -a
    ... keep working locally with git
    $ git svn dcommit

> [!TIP]
> The use of "`-rHEAD`" enables us to avoid cloning entire historical contents from the Subversion repository.

### Git for recording configuration history

You can manually record chronological history of configuration using [Git](https://en.wikipedia.org/wiki/Git_(software)) tools. Here is a simple example for your practice to record "`/etc/apt/`" contents.

    $ cd /etc/apt/
    $ sudo git init
    $ sudo chmod 700 .git
    $ sudo git add .
    $ sudo git commit -a

Commit configuration with description.

Make modification to the configuration files.

    $ cd /etc/apt/
    $ sudo git commit -a

Commit configuration with description and continue your life.

    $ cd /etc/apt/
    $ sudo gitk --all

You have full configuration history with you.

> [!NOTE]
> `sudo(8)` is needed to work with any file permissions of configuration data. For user configuration data, you may skip `sudo`.

> [!NOTE]
> The "`chmod 700 .git`" command in the above example is needed to protect archive data from unauthorized read access.

> [!TIP]
> For more complete setup for recording configuration history, please look for the `etckeeper` package: [???](#_recording_changes_in_configuration_files).

## CVS

CVS is an **older** version control system before Subversion and Git.

> [!CAUTION]
> Many URLs found in the below examples for CVS don't exist any more.

See the following.

- `cvs(1)`

- "`/usr/share/doc/cvs/html-cvsclient`"

- "`/usr/share/doc/cvs/html-info`"

- "`/usr/share/doc/cvsbook`"

- "`info cvs`"

### Configuration of CVS repository

The following configuration allows commits to the CVS repository only by a member of the "`src`" group, and administration of CVS only by a member of the "`staff`" group, thus reducing the chance of shooting oneself.

    # cd /var/lib; umask 002; mkdir cvs
    # export CVSROOT=/srv/cvs/project
    # cd $CVSROOT
    # chown root:src .
    # chmod 2775 .
    # cvs -d $CVSROOT init
    # cd CVSROOT
    # chown -R root:staff .
    # chmod 2775 .
    # touch val-tags
    # chmod 664 history val-tags
    # chown root:src history val-tags

> [!TIP]
> You may restrict creation of new project by changing the owner of "`$CVSROOT`" directory to "`root:staff`" and its permission to "`3775`".

### Local access to CVS

The default CVS repository is pointed by "`$CVSROOT`". The following sets up "`$CVSROOT`" for the local access.

    $ export CVSROOT=/srv/cvs/project

### Remote access to CVS with pserver

Many public CVS servers provide read-only remote access to them with account name "`anonymous`" via pserver service. For example, Debian web site contents were maintained by [webwml project](http://alioth.debian.org/projects/webwml/) via CVS at Debian alioth service. The following was used to set up "`$CVSROOT`" for the remote access to this old CVS repository.

    $ export CVSROOT=:pserver:anonymous@anonscm.debian.org:/cvs/webwml
    $ cvs login

> [!NOTE]
> Since pserver is prone to eavesdropping attack and insecure, write access is usually disable by server administrators.

### Remote access to CVS with ssh

The following was used to set up "`$CVS_RSH`" and "`$CVSROOT`" for the remote access to the old CVS repository by [webwml project](http://alioth.debian.org/projects/webwml/) with SSH.

    $ export CVS_RSH=ssh
    $ export CVSROOT=:ext:account@cvs.alioth.debian.org:/cvs/webwml

You can also use public key authentication for SSH which eliminates the remote password prompt.

### Importing a new source to CVS

Create a new local source tree location at "`~/path/to/module1`" by the following.

    $ mkdir -p ~/path/to/module1; cd ~/path/to/module1

Populate a new local source tree under "`~/path/to/module1`" with files.

Import it to CVS with the following parameters.

- Module name: "`module1`"

- Vendor tag: "`Main-branch`" (tag for the entire branch)

- Release tag: "`Release-initial`" (tag for a specific release)

<!-- -->

    $ cd ~/path/to/module1
    $ cvs import -m "Start module1" module1 Main-branch Release-initial
    $ rm -Rf . # optional

### File permissions in CVS repository

CVS does not overwrite the current repository file but replaces it with another one. Thus, write permission to the repository directory is critical. For every new module for "`module1`" in repository at "`/srv/cvs/project`", run the following to ensure this condition if needed.

    # cd /srv/cvs/project
    # chown -R root:src module1
    # chmod -R ug+rwX   module1
    # chmod    2775     module1

### Work flow of CVS

Here is an example of typical work flow using CVS.

Check all available modules from CVS project pointed by "`$CVSROOT`" by the following.

    $ cvs rls
    CVSROOT
    module1
    module2
    ...

Checkout "`module1`" to its default directory "`./module1`" by the following.

    $ cd ~/path/to
    $ cvs co module1
    $ cd module1

Make changes to the content as needed.

Check changes by making "`diff -u [repository] [local]`" equivalent by the following.

    $ cvs diff -u

You find that you broke some file "`file_to_undo`" severely but other files are fine.

Overwrite "`file_to_undo`" file with the clean copy from CVS by the following.

    $ cvs up -C file_to_undo

Save the updated local source tree to CVS by the following.

    $ cvs ci -m "Describe change"

Create and add "`file_to_add`" file to CVS by the following.

    $ vi file_to_add
    $ cvs add file_to_add
    $ cvs ci -m "Added file_to_add"

Merge the latest version from CVS by the following.

    $ cvs up -d

Watch out for lines starting with "`C filename`" which indicates conflicting changes.

Look for unmodified code in "`.#filename.version`".

Search for "`<<<<<<<`" and "`>>>>>>>`" in files for conflicting changes.

Edit files to fix conflicts as needed.

Add a release tag "`Release-1`" by the following.

    $ cvs ci -m "last commit for Release-1"
    $ cvs tag Release-1

Edit further.

Remove the release tag "`Release-1`" by the following.

    $ cvs tag -d Release-1

Check in changes to CVS by the following.

    $ cvs ci -m "real last commit for Release-1"

Re-add the release tag "`Release-1`" to updated CVS HEAD of main by the following.

    $ cvs tag Release-1

Create a branch with a sticky branch tag "`Release-initial-bugfixes`" from the original version pointed by the tag "`Release-initial`" and check it out to "`~/path/to/old`" directory by the following.

    $ cvs rtag -b -r Release-initial Release-initial-bugfixes module1
    $ cd ~/path/to
    $ cvs co -r Release-initial-bugfixes -d old module1
    $ cd old

> [!TIP]
> Use "`-D 2005-12-20`" ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date format) instead of "`-r Release-initial`" to specify particular date as the branch point.

Work on this local source tree having the sticky tag "`Release-initial-bugfixes`" which is based on the original version.

Work on this branch by yourself … until someone else joins to this "`Release-initial-bugfixes`" branch.

Sync with files modified by others on this branch while creating new directories as needed by the following.

    $ cvs up -d

Edit files to fix conflicts as needed.

Check in changes to CVS by the following.

    $ cvs ci -m "checked into this branch"

Update the local tree by HEAD of main while removing sticky tag ("`-A`") and without keyword expansion ("`-kk`") by the following.

    $ cvs up -d -kk -A

Update the local tree (content = HEAD of main) by merging from the "`Release-initial-bugfixes`" branch and without keyword expansion by the following.

    $ cvs up -d -kk -j Release-initial-bugfixes

Fix conflicts with editor.

Check in changes to CVS by the following.

    $ cvs ci -m "merged Release-initial-bugfixes"

Make archive by the following.

    $ cd ..
    $ mv old old-module1-bugfixes
    $ tar -cvzf old-module1-bugfixes.tar.gz old-module1-bugfixes
    $ rm -rf old-module1-bugfixes

> [!TIP]
> "`cvs up`" command can take "`-d`" option to create new directories and "`-P`" option to prune empty directories.

> [!TIP]
> You can checkout only a sub directory of "`module1`" by providing its name as "`cvs co module1/subdir`".

| option | meaning                                        |
|:-------|:-----------------------------------------------|
| `-n`   | dry run, no effect                             |
| `-t`   | display messages showing steps of cvs activity |

Notable options for CVS commands (use as first argument(s) to `cvs(1)`)

### Latest files from CVS

To get the latest files from CVS, use "`tomorrow`" by the following.

    $ cvs ex -D tomorrow module_name

### Administration of CVS

Add module alias "`mx`" to a CVS project (local server) by the following.

    $ export CVSROOT=/srv/cvs/project
    $ cvs co CVSROOT/modules
    $ cd CVSROOT
    $ echo "mx -a module1" >>modules
    $ cvs ci -m "Now mx is an alias for module1"
    $ cvs release -d .

Now, you can check out "`module1`" (alias: "`mx`") from CVS to "`new`" directory by the following.

    $ cvs co -d new mx
    $ cd new

> [!NOTE]
> In order to perform above procedure, you should have appropriate file permissions.

### Execution bit for CVS checkout

When you checkout files from CVS, their execution permission bit is retained.

Whenever you see execution permission problems in a checked out file, e.g. "`filename`", change its permission in the corresponding CVS repository by the following to fix it.

    # chmod ugo-x filename

## Subversion

Subversion is an **older** version control system before Git but after CVS. It lacks tagging and branching features found in CVS and Git.

You need to install `subversion`, `libapache2-mod-svn` and `subversion-tools` packages to set up a Subversion server.

### Configuration of Subversion repository

Currently, the `subversion` package does not set up a repository, so one must set it up manually. One possible location for a repository is in "`/srv/svn/project`".

Create a directory by the following.

    # mkdir -p        /srv/svn/project

Create the repository database by the following.

    # svnadmin create /srv/svn/project

### Access to Subversion via Apache2 server

If you only access Subversion repository via Apache2 server, you just need to make the repository only writable by the WWW server by the following.

    # chown -R www-data:www-data /srv/svn/project

Add (or uncomment) the following in "`/etc/apache2/mods-available/dav_svn.conf`" to allow access to the repository via user authentication.

    <Location /project>
      DAV svn
      SVNPath /srv/svn/project
      AuthType Basic
      AuthName "Subversion repository"
      AuthUserFile /etc/subversion/passwd
    <LimitExcept GET PROPFIND OPTIONS REPORT>
        Require valid-user
    </LimitExcept>
    </Location>

Create a user authentication file with the command by the following.

    # htpasswd2 -c /etc/subversion/passwd some-username

Restart Apache2.

Your new Subversion repository is accessible at URL "`http://localhost/project`" and "`http://example.com/project`" from `svn(1)` (assuming your URL of web server is "`http://example.com/`").

### Local access to Subversion by group

The following sets up Subversion repository for the local access by a group, e.g. `project`.

    # chmod  2775     /srv/svn/project
    # chown -R root:src /srv/svn/project
    # chmod -R ug+rwX   /srv/svn/project

Your new Subversion repository is group accessible at URL "`file:///localhost/srv/svn/project`" or "`file:///srv/svn/project`" from `svn(1)` for local users belonging to `project` group. You must run commands, such as `svn`, `svnserve`, `svnlook`, and `svnadmin` under "`umask 002`" to ensure group access.

### Remote access to Subversion via SSH

A group accessible Subversion repository is at URL "`example.com:/srv/svn/project`" for SSH, you can access it from `svn(1)` at URL "`svn+ssh://example.com:/srv/svn/project`".

### Subversion directory structure

Many projects uses directory tree similar to the following for Subversion to compensate its lack of branches and tags.

      ----- module1
        |   |-- branches
        |   |-- tags
        |   |   |-- release-1.0
        |   |   `-- release-2.0
        |   |
        |   `-- trunk
        |       |-- file1
        |       |-- file2
        |       `-- file3
        |
        `-- module2

> [!TIP]
> You must use "`svn copy …`" command to mark branches and tags. This ensures Subversion to record modification history of files properly and saves storage spaces.

### Importing a new source to Subversion

Create a new local source tree location at "`~/path/to/module1`" by the following.

    $ mkdir -p ~/path/to/module1; cd ~/path/to/module1

Populate a new local source tree under "`~/path/to/module1`" with files.

Import it to Subversion with the following parameters.

- Module name: "`module1`"

- Subversion site URL: "`file:///srv/svn/project`"

- Subversion directory: "`module1/trunk`"

- Subversion tag: "`module1/tags/Release-initial`"

<!-- -->

    $ cd ~/path/to/module1
    $ svn import file:///srv/svn/project/module1/trunk -m "Start module1"
    $ svn cp file:///srv/svn/project/module1/trunk file:///srv/svn/project/module1/tags/Release-initial

Alternatively, by the following.

    $ svn import ~/path/to/module1 file:///srv/svn/project/module1/trunk -m "Start module1"
    $ svn cp file:///srv/svn/project/module1/trunk file:///srv/svn/project/module1/tags/Release-initial

> [!TIP]
> You can replace URLs such as "`file:///…`" by any other URL formats such as "`http://…`" and "`svn+ssh://…`".

### Work flow of Subversion

Here is an example of typical work flow using Subversion with its native client.

> [!TIP]
> Client commands offered by the `git-svn` package may offer alternative work flow of Subversion using the `git` command. See [Git for the Subversion repository](#_git_for_the_subversion_repository).

Check all available modules from Subversion project pointed by URL "`file:///srv/svn/project`" by the following.

    $ svn list file:///srv/svn/project
    module1
    module2
    ...

Checkout "`module1/trunk`" to a directory "`module1`" by the following.

    $ cd ~/path/to
    $ svn co file:///srv/svn/project/module1/trunk module1
    $ cd module1

Make changes to the content as needed.

Check changes by making "`diff -u [repository] [local]`" equivalent by the following.

    $ svn diff

You find that you broke some file "`file_to_undo`" severely but other files are fine.

Overwrite "`file_to_undo`" file with the clean copy from Subversion by the following.

    $ svn revert file_to_undo

Save the updated local source tree to Subversion by the following.

    $ svn ci -m "Describe change"

Create and add "`file_to_add`" file to Subversion by the following.

    $ vi file_to_add
    $ svn add file_to_add
    $ svn ci -m "Added file_to_add"

Merge the latest version from Subversion by the following.

    $ svn up

Watch out for lines starting with "`C filename`" which indicates conflicting changes.

Look for unmodified code in, e.g., "`filename.r6`", "`filename.r9`", and "`filename.mine`".

Search for "`<<<<<<<`" and "`>>>>>>>`" in files for conflicting changes.

Edit files to fix conflicts as needed.

Add a release tag "`Release-1`" by the following.

    $ svn ci -m "last commit for Release-1"
    $ svn cp file:///srv/svn/project/module1/trunk file:///srv/svn/project/module1/tags/Release-1

Edit further.

Remove the release tag "`Release-1`" by the following.

    $ svn rm file:///srv/svn/project/module1/tags/Release-1

Check in changes to Subversion by the following.

    $ svn ci -m "real last commit for Release-1"

Re-add the release tag "`Release-1`" from updated Subversion HEAD of trunk by the following.

    $ svn cp file:///srv/svn/project/module1/trunk file:///srv/svn/project/module1/tags/Release-1

Create a branch with a path "`module1/branches/Release-initial-bugfixes`" from the original version pointed by the path "`module1/tags/Release-initial`" and check it out to "`~/path/to/old`" directory by the following.

    $ svn cp file:///srv/svn/project/module1/tags/Release-initial file:///srv/svn/project/module1/branches/Release-initial-bugfixes
    $ cd ~/path/to
    $ svn co file:///srv/svn/project/module1/branches/Release-initial-bugfixes old
    $ cd old

> [!TIP]
> Use "`module1/trunk@{2005-12-20}`" ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date format) instead of "`module1/tags/Release-initial`" to specify particular date as the branch point.

Work on this local source tree pointing to branch "`Release-initial-bugfixes`" which is based on the original version.

Work on this branch by yourself … until someone else joins to this "`Release-initial-bugfixes`" branch.

Sync with files modified by others on this branch by the following.

    $ svn up

Edit files to fix conflicts as needed.

Check in changes to Subversion by the following.

    $ svn ci -m "checked into this branch"

Update the local tree with HEAD of trunk by the following.

    $ svn switch file:///srv/svn/project/module1/trunk

Update the local tree (content = HEAD of trunk) by merging from the "`Release-initial-bugfixes`" branch by the following.

    $ svn merge file:///srv/svn/project/module1/branches/Release-initial-bugfixes

Fix conflicts with editor.

Check in changes to Subversion by the following.

    $ svn ci -m "merged Release-initial-bugfixes"

Make archive by the following.

    $ cd ..
    $ mv old old-module1-bugfixes
    $ tar -cvzf old-module1-bugfixes.tar.gz old-module1-bugfixes
    $ rm -rf old-module1-bugfixes

> [!TIP]
> You can replace URLs such as "`file:///…`" by any other URL formats such as "`http://…`" and "`svn+ssh://…`".

> [!TIP]
> You can checkout only a sub directory of "`module1`" by providing its name as "`svn co file:///srv/svn/project/module1/trunk/subdir module1/subdir`", etc.

| option      | meaning                                 |
|:------------|:----------------------------------------|
| `--dry-run` | dry run, no effect                      |
| `-v`        | display detail messages of svn activity |

Notable options for Subversion commands (use as first argument(s) to `svn(1)`)
