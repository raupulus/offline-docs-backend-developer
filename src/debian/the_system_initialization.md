---
title: The system initialization
source_url: https://www.debian.org/doc/manuals/debian-reference/_the_system_initialization
source_repo: https://salsa.debian.org/debian/debian-reference.git
source_ref: master
source_commit: b7239e647
source_path: 03_the_system_initialization.rawxml
technology: debian
version: 12 (Bookworm)
license: GPL-2.0-or-later
retrieved_at: '2026-09-15'
order: 40
---

## The system initialization

It is wise for you as the system administrator to know roughly how the Debian system is started and configured. Although the exact details are in the source files of the packages installed and their documentations, it is a bit overwhelming for most of us.

I did my best to provide a quick overview of the key points of the Debian system and their configuration for your reference, based on the current and previous knowledge of mine and others. Since the Debian system is a moving target, the situation over the system may have been changed. Before making any changes to the system, you should refer to the latest documentation for each package.

> [!TIP]
> `bootup(7)` describes the system bootup process based on `systemd` . (Recent Debian)

> [!TIP]
> `boot(7)` describes the system bootup process based on UNIX System V Release 4. (Older Debian)

## An overview of the boot strap process

The computer system undergoes several phases of [boot strap processes](https://en.wikipedia.org/wiki/Booting) from the power-on event until it offers the fully functional operating system (OS) to the user.

For simplicity, I limit discussion to the typical PC platform with the default installation.

The typical boot strap process is like a four-stage rocket. Each stage rocket hands over the system control to the next stage one.

- [Stage 1: the BIOS](#_stage_1_the_bios)

- [Stage 2: the boot loader](#_stage_2_the_boot_loader)

- [Stage 3: the mini-Debian system](#_stage_3_the_mini_debian_system)

- [Stage 4: the normal Debian system](#_stage_4_the_normal_debian_system)

Of course, these can be configured differently. For example, if you compiled your own kernel, you may be skipping the step with the mini-Debian system. So please do not assume this is the case for your system until you check it yourself.

> [!NOTE]
> For non-legacy PC platform such as the SUN or the Macintosh system, the BIOS on ROM and the partition on the disk may be quite different ([???](#_disk_partition_configuration)). Please seek the platform specific documentations elsewhere for such a case.

### Stage 1: the BIOS

The [BIOS](https://en.wikipedia.org/wiki/BIOS) is the 1st stage of the boot process which is started by the power-on event. The [BIOS](https://en.wikipedia.org/wiki/BIOS) residing on the [read only memory (ROM)](https://en.wikipedia.org/wiki/Read-only_memory) is executed from the particular memory address to which the program counter of CPU is initialized by the power-on event.

This BIOS performs the basic initialization of the hardware ([POST: power on self test](https://en.wikipedia.org/wiki/Power-on_self-test)) and hands the system control to the next step which you provide. The BIOS is usually provided with the hardware.

The BIOS startup screen usually indicates what key(s) to press to enter the BIOS setup screen to configure the BIOS behavior. Popular keys used are F1, F2, F10, Esc, Ins, and Del. If your BIOS startup screen is hidden by a nice graphics screen, you may press some keys such as Esc to disable this. These keys are highly dependent on the hardware.

The hardware location and the priority of the code started by the BIOS can be selected from the BIOS setup screen. Typically, the first few sectors of the first found selected device (hard disk, floppy disk, CD-ROM, …) are loaded to the memory and this initial code is executed. This initial code can be any one of the following.

- The boot loader code

- The kernel code of the stepping stone OS such as [FreeDOS](http://www.freedos.org/)

- The kernel code of the target OS if it fits in this small space

Typically, the system is booted from the specified partition of the primary hard disk partition. First 2 sectors of the hard disk on legacy PC contain the [master boot record (MBR)](https://en.wikipedia.org/wiki/Master_boot_record). The disk partition information including the boot selection is recorded at the end of this MBR. The first boot loader code executed from the BIOS occupies the rest of this MBR.

### Stage 2: the boot loader

The [boot loader](https://en.wikipedia.org/wiki/Boot_loader) is the 2nd stage of the boot process which is started by the BIOS. It loads the system kernel image and the [initrd](https://en.wikipedia.org/wiki/Initrd) image to the memory and hands control over to them. This initrd image is the root filesystem image and its support depends on the bootloader used.

The Debian system normally uses the Linux kernel as the default system kernel. The initrd image for the current 2.6/3.x Linux kernel is technically the [initramfs](https://wiki.debian.org/initramfs) (initial RAM filesystem) image. The basic initrd image is a compressed cpio archive of files in the root filesystem. The kernel can update microcode very early during boot before loading this basic initrd image. This is facilitated by the combined initrd image which is microcode binary blob in uncompressed cpio format followed by the basic initrd image.

> [!TIP]
> You can inspect the content of the initrd image file using `lsinitramfs(8)` and `unmkinitramfs(8)` from the `initramfs-tools-core` package. See more on <https://wiki.debian.org/initramfs>.

The default install of the Debian system places first-stage GRUB boot loader code into the [MBR](https://en.wikipedia.org/wiki/Master_boot_record) for the PC platform. There are many boot loaders and configuration options available.

| package | popcon | size | initrd | bootloader | description |
|:---|:---|:---|:---|:---|:---|
| grub-legacy | @-@popcon1@-@ | @-@psize1@-@ | Supported | [GRUB Legacy](https://en.wikipedia.org/wiki/GNU_GRUB) | This is smart enough to understand disk partitions and filesystems such as vfat, ext3, …. |
| grub-pc | @-@popcon1@-@ | @-@psize1@-@ | Supported | [GRUB 2](https://en.wikipedia.org/wiki/GNU_GRUB) | This is smart enough to understand disk partitions and filesystems such as vfat, ext4, …. (default) |
| grub-rescue-pc | @-@popcon1@-@ | @-@psize1@-@ | Supported | [GRUB 2](https://en.wikipedia.org/wiki/GNU_GRUB) | This is GRUB 2 bootable rescue images (CD and floppy) (PC/BIOS version) |
| lilo | @-@popcon1@-@ | @-@psize1@-@ | Supported | [Lilo](https://en.wikipedia.org/wiki/LILO_(boot_loader)) | This relies on the sector locations of data on the hard disk. (Old) |
| syslinux | @-@popcon1@-@ | @-@psize1@-@ | Supported | [Isolinux](https://en.wikipedia.org/wiki/SYSLINUX) | This understands the ISO9660 filesystem. This is used by the boot CD. |
| syslinux | @-@popcon1@-@ | @-@psize1@-@ | Supported | [Syslinux](https://en.wikipedia.org/wiki/SYSLINUX) | This understands the [MSDOS filesystem (FAT)](https://en.wikipedia.org/wiki/File_Allocation_Table). This is used by the boot floppy. |
| loadlin | @-@popcon1@-@ | @-@psize1@-@ | Supported | [Loadlin](https://en.wikipedia.org/wiki/Loadlin) | New system is started from the FreeDOS/MSDOS system. |
| mbr | @-@popcon1@-@ | @-@psize1@-@ | Not supported | [MBR by Neil Turton](http://www.chiark.greenend.org.uk/~neilt/) | This is free software which substitutes MSDOS [MBR](https://en.wikipedia.org/wiki/Master_boot_record). This only understands disk partitions. |

List of boot loaders

> [!WARNING]
> Do not play with boot loaders without having bootable rescue media (USB memory stick, CD or floppy) created from images in the `grub-rescue-pc` package. It makes you boot your system even without functioning bootloader on the hard disk.

For GRUB Legacy, the menu configuration file is located at "`/boot/grub/menu.lst`". For example, it has entries as the following.

    title           Debian GNU/Linux
    root            (hd0,2)
    kernel          /vmlinuz root=/dev/hda3 ro
    initrd          /initrd.img

For GRUB 2, the menu configuration file is located at "`/boot/grub/grub.cfg`". It is automatically generated by "`/usr/sbin/update-grub`" using templates from "`/etc/grub.d/*`" and settings from "`/etc/default/grub`". For example, it has entries as the following.

    menuentry "Debian GNU/Linux" {
            set root=(hd0,3)
            linux /vmlinuz root=/dev/hda3
            initrd /initrd.img
    }

For these examples, these GRUB parameters mean the following.

| GRUB parameter | meaning |
|:---|:---|
| `root` | use 3rd partition on the primary disk by setting it as "`(hd0,2)`" in GRUB legacy or as "`(hd0,3)`" in GRUB 2 |
| `kernel` | use kernel located at "`/vmlinuz`" with kernel parameter: "`root=/dev/hda3 ro`" |
| `initrd` | use [initrd/initramfs](https://en.wikipedia.org/wiki/Initrd) image located at "`/initrd.img`" |

The meaning of GRUB parameters

> [!NOTE]
> The value of the partition number used by GRUB legacy program is one less than normal one used by Linux kernel and utility tools. GRUB 2 program fixes this problem.

> [!TIP]
> [UUID](https://en.wikipedia.org/wiki/Universally_Unique_Identifier) (see [???](#_accessing_partition_using_uuid)) may be used to identify a block special device instead of its file name such as "`/dev/hda3`", e.g."`root=UUID=81b289d5-4341-4003-9602-e254a17ac232 ro`".

> [!TIP]
> If [GRUB](https://en.wikipedia.org/wiki/GNU_GRUB) is used, the kernel boot parameter is set in `/boot/grub/grub.cfg`. On Debian system, you should not edit `/boot/grub/grub.cfg` directly. You should edit the `GRUB_CMDLINE_LINUX_DEFAULT` value in `/etc/default/grub` and run `update-grub(8)` to update `/boot/grub/grub.cfg`.

> [!TIP]
> You can start a boot loader from another boot loader using techniques called [chain loading](https://en.wikipedia.org/wiki/Chain_loading).

See "`info grub`" and `grub-install(8)`.

### Stage 3: the mini-Debian system

The mini-Debian system is the 3rd stage of the boot process which is started by the boot loader. It runs the system kernel with its root filesystem on the memory. This is an optional preparatory stage of the boot process.

> [!NOTE]
> The term "the mini-Debian system" is coined by the author to describe this 3rd stage boot process for this document. This system is commonly referred as the [initrd](https://en.wikipedia.org/wiki/Initrd) or initramfs system. Similar system on the memory is used by [the Debian Installer](https://www.debian.org/devel/debian-installer/).

The "`/init`" program is executed as the first program in this root filesystem on the memory. It is a program which initializes the kernel in user space and hands control over to the next stage. This mini-Debian system offers flexibility to the boot process such as adding kernel modules before the main boot process or mounting the root filesystem as an encrypted one.

- The "`/init`" program is a shell script program if initramfs was created by `initramfs-tools`.

  - You can interrupt this part of the boot process to gain root shell by providing "`break=init`" etc. to the kernel boot parameter. See the "`/init`" script for more break conditions. This shell environment is sophisticated enough to make a good inspection of your machine's hardware.

  - Commands available in this mini-Debian system are stripped down ones and mainly provided by a GNU tool called `busybox(1)`.

- The "`/init`" program is a binary `systemd` program if initramfs was created by `dracut`.

  - Commands available in this mini-Debian system are stripped down `systemd(1)` environment.

> [!CAUTION]
> You need to use "`-n`" option for `mount` command when you are on the readonly root filesystem.

### Stage 4: the normal Debian system

The normal Debian system is the 4th stage of the boot process which is started by the mini-Debian system. The system kernel for the mini-Debian system continues to run in this environment. The root filesystem is switched from the one on the memory to the one on the real hard disk filesystem.

The [init](https://en.wikipedia.org/wiki/Init) program is executed as the first program with PID=1 to perform the main boot process of starting many programs. The default file path for the init program is "`/sbin/init`" but it can be changed by the kernel boot parameter as "`init=/path/to/init_program`".

The default init program has been changing:

- Debian before `squeeze` uses the simple [SysV](https://en.wikipedia.org/wiki/UNIX_System_V)-style init.

- Debian `wheezy` improves the SysV-style init by ordering the boot sequence with LSB header and starting boot scripts in parallel.

- Debian `jessie` switches its default init to the [systemd](https://en.wikipedia.org/wiki/Systemd) for the event-driven and parallel initialization.

> [!TIP]
> The actual init command on your system can be verified by the "`ps --pid 1 -f`" command.

> [!TIP]
> "`/sbin/init`" is symlinked to "`/lib/systemd/systemd`" after Debian `jessie`.

| package | popcon | size | description |
|:---|:---|:---|:---|
| `systemd` | @-@popcon1@-@ | @-@psize1@-@ | event-based `init(8)` daemon for concurrency (alternative to `sysvinit`) |
| `systemd-sysv` | @-@popcon1@-@ | @-@psize1@-@ | the manual pages and links needed for `systemd` to replace `sysvinit` |
| `systemd-cron` | @-@popcon1@-@ | @-@psize1@-@ | `systemd` units to provide `cron` daemon and `anacron` functionality |
| `init-system-helpers` | @-@popcon1@-@ | @-@psize1@-@ | helper tools for switching between `sysvinit` and `systemd` |
| `initscripts` | @-@popcon1@-@ | @-@psize1@-@ | scripts for initializing and shutting down the system |
| `sysvinit-core` | @-@popcon1@-@ | @-@psize1@-@ | System-V-like `init(8)` utilities |
| `sysv-rc` | @-@popcon1@-@ | @-@psize1@-@ | System-V-like runlevel change mechanism |
| `sysvinit-utils` | @-@popcon1@-@ | @-@psize1@-@ | System-V-like utilities (`startpar(8)`, `bootlogd(8)`, …) |
| `lsb-base` | @-@popcon1@-@ | @-@psize1@-@ | [Linux Standard Base](https://en.wikipedia.org/wiki/Linux_Standard_Base) 3.2 init script functionality |
| `insserv` | @-@popcon1@-@ | @-@psize1@-@ | tool to organize boot sequence using LSB init.d script dependencies |
| `uswsusp` | @-@popcon1@-@ | @-@psize1@-@ | tools to use userspace software suspend provided by Linux |
| `kexec-tools` | @-@popcon1@-@ | @-@psize1@-@ | kexec tool for `kexec(8)` reboots (warm reboot) |
| `systemd-bootchart` | @-@popcon1@-@ | @-@psize1@-@ | boot process performance analyser |
| `bootchart2` | @-@popcon1@-@ | @-@psize1@-@ | boot process performance analyser |
| `pybootchartgui` | @-@popcon1@-@ | @-@psize1@-@ | boot process performance analyser (visualisation) |
| `mingetty` | @-@popcon1@-@ | @-@psize1@-@ | console-only `getty(8)` |
| `mgetty` | @-@popcon1@-@ | @-@psize1@-@ | smart modem `getty(8)` replacement |

List of boot utilities for the Debian system

> [!TIP]
> See [Debian wiki: BootProcessSpeedup](https://wiki.debian.org/BootProcessSpeedup) for the latest tips to speed up the boot process.

## Systemd init

This section describes how system is started by the `systemd(1)` program with `PID=1` (i.e., init process).

The `systemd` init process spawns processes in parallel based on the unit configuration files (see `systemd.unit(5)`) which are written in declarative style instead of SysV-like procedural style. These are loaded from a set of paths (see `systemd-system.conf(5)`) as follows:

- "`/lib/systemd/system`": OS default configuration files

- "`/etc/systemd/system`": system administrator configuration files which override the OS default configuration files

- "`/run/systemd/system`": run-time generated configuration files which override the installed configuration files

Their inter-dependencies are specified by the directives "`Wants=`", "`Requires=`", "`Before=`", "`After=`", … (see "MAPPING OF UNIT PROPERTIES TO THEIR INVERSES" in `systemd.unit(5)`). The resource controls are also defined (see `systemd.resource-control(5)`).

The suffix of the unit configuration file encodes their types as:

- **\*.service** describes the process controlled and supervised by `systemd`. See `systemd.service(5)`.

- **\*.device** describes the device exposed in the `sysfs(5)` as `udev(7)` device tree. See `systemd.device(5)`.

- **\*.mount** describes the file system mount point controlled and supervised by `systemd`. See `systemd.mount(5)`.

- **\*.automount** describes the file system auto mount point controlled and supervised by `systemd`. See `systemd.automount(5)`.

- **\*.swap** describes the swap device or file controlled and supervised by `systemd`. See `systemd.swap(5)`.

- **\*.path** describes the path monitored by `systemd` for path-based activation. See `systemd.path(5)`.

- **\*.socket** describes the socket controlled and supervised by `systemd` for socket-based activation. See `systemd.socket(5)`.

- **\*.timer** describes the timer controlled and supervised by `systemd` for timer-based activation. See `systemd.timer(5)`.

- **\*.slice** manages resources with the `cgroups(7)`. See `systemd.slice(5)`.

- **\*.scope** is created programmatically using the bus interfaces of `systemd` to manages a set of system processes. See `systemd.scope(5)`.

- **\*.target** groups other unit configuration files to create the synchronization point during start-up. See `systemd.target(5)`.

Upon system start up (i.e., init), the `systemd` process tries to start the "`/lib/systemd/system/default.target` (normally symlinked to "`graphical.target`"). First, some special target units (see `systemd.special(7)`) such as "`local-fs.target`", "`swap.target`" and "`cryptsetup.target`" are pulled in to mount the filesystems. Then, other target units are also pulled in by the target unit dependencies. For details, read `bootup(7)`.

`systemd` offers backward compatibility features. SysV-style boot scripts in "`/etc/init.d/rc[0123456S].d/[KS]<name>`" are still parsed and `telinit(8)` is translated into systemd unit activation requests.

> [!CAUTION]
> Emulated runlevel 2 to 4 are all symlinked to the same "`multi-user.target`".

### The hostname

The kernel maintains the system **hostname**. The system unit started by `systemd-hostnamed.service` sets the system hostname at boot time to the name stored in "`/etc/hostname`". This file should contain **only** the system hostname, not a fully qualified domain name.

To print out the current hostname run `hostname(1)` without an argument.

### The filesystem

The mount options of normal disk and network filesystems are set in "`/etc/fstab`". See `fstab(5)` and [???](#_optimization_of_filesystem_by_mount_options).

The configuration of the encrypted filesystem is set in "`/etc/crypttab`". See `crypttab(5)`

The configuration of software RAID with `mdadm(8)` is set in "`/etc/mdadm/mdadm.conf`". See `mdadm.conf(5)`.

> [!WARNING]
> After mounting all the filesystems, temporary files in "`/tmp`", "`/var/lock`", and "`/var/run`" are cleaned for each boot up.

### Network interface initialization

Network interfaces are typically initialized in "`networking.service`" for the `lo` interface and "`NetworkManager.service`" for other interfaces on modern Debian desktop system under `systemd`.

See [???](#_network_setup) for how to configure them.

### The kernel message

The kernel error message displayed to the console can be configured by setting its threshold level.

    # dmesg -n3

| error level value | error level name | meaning                          |
|:------------------|:-----------------|:---------------------------------|
| 0                 | KERN_EMERG       | system is unusable               |
| 1                 | KERN_ALERT       | action must be taken immediately |
| 2                 | KERN_CRIT        | critical conditions              |
| 3                 | KERN_ERR         | error conditions                 |
| 4                 | KERN_WARNING     | warning conditions               |
| 5                 | KERN_NOTICE      | normal but significant condition |
| 6                 | KERN_INFO        | informational                    |
| 7                 | KERN_DEBUG       | debug-level messages             |

List of kernel error levels

### The system message

Under `systemd`, both kernel and system messages are logged by the journal service `systemd-journald.service` (a.k.a `journald`) either into a persistent binary data below "`/var/log/journal`" or into a volatile binary data below "`/run/log/journal/`". These binary log data are accessed by the `journalctl(1)` command.

Under `systemd`, the system logging utility `rsyslogd(8)` changes its behavior to read the volatile binary log data (instead of pre-systemd default "`/dev/log`") and to create traditional permanent ASCII system log data.

The system message can be customized by "`/etc/default/rsyslog`" and "`/etc/rsyslog.conf`" for both the log file and on-screen display. See `rsyslogd(8)` and `rsyslog.conf(5)`. See also [???](#_log_analyzer).

### System management under systemd

The `systemd` offers not only init system but also generic system management functionalities such as journal logging, login management, time management, network management. etc..

The `systemd(1)` is managed by several commands:

- the `systemctl(1)` command controls the `systemd` system and service manager (CLI),

- the `systemsdm(1)` command controls the `systemd` system and service manager (GUI),

- the `journalctl(1)` command queries the `systemd` journal,

- the `loginctl(1)` command controls the `systemd` login manager, and

- the `systemd-analyze(1)` analyzes system boot-up performance.

Here are a list of typical `systemd` management command snippets. For the exact meanings, please read the pertinent manpages.

| Operation | Type | Command snippets |
|:---|:---|:---|
| GUI for service manager | GUI | "`systemadm`" (`systemd-ui` package) |
| List all target unit configuration | Unit | "`systemctl list-units --type=target`" |
| List all service unit configuration | Unit | "`systemctl list-units --type=service`" |
| List all unit configuration types | Unit | "`systemctl list-units --type=help`" |
| List all socket units in memory | Unit | "`systemctl list-sockets`" |
| List all timer units in memory | Unit | "`systemctl list-timers`" |
| Start "`$unit`" | Unit | "`systemctl start $unit`" |
| Stop "`$unit`" | Unit | "`systemctl stop $unit`" |
| Reload service-specific configuration | Unit | "`systemctl reload $unit`" |
| Stop and start all "`$unit`" | Unit | "`systemctl restart $unit`" |
| Start "`$unit`" and stop all others | Unit | "`systemctl isolate $unit`" |
| Switch to "`graphical`" (GUI system) | Unit | "`systemctl isolate graphical`" |
| Switch to "`multi-user`" (CLI system) | Unit | "`systemctl isolate multi-user`" |
| Switch to "`rescue`" (single user CLI system) | Unit | "`systemctl isolate rescue`" |
| Send kill signal to "`$unit`" | Unit | "`systemctl kill $unit`" |
| Check if "`$unit`" service is active | Unit | "`systemctl is-active $unit`" |
| Check if "`$unit`" service is failed | Unit | "`systemctl is-failed $unit`" |
| Check status of "`$unit|$PID|device`" | Unit | "`systemctl status $unit|$PID|$device`" |
| Show properties of "`$unit|$job`" | Unit | "`systemctl show $unit|$job`" |
| Reset failed "`$unit`" | Unit | "`systemctl reset-failed $unit"` |
| List dependency of all unit services | Unit | "`systemctl list-dependencies --all`" |
| List unit files installed on the system | Unit file | "`systemctl list-unit-files`" |
| Enable "`$unit`" (add symlink) | Unit file | "`systemctl enable $unit`" |
| Disable "`$unit`" (remove symlink) | Unit file | "`systemctl disable $unit`" |
| Unmask "`$unit`" (remove symlink to "`/dev/null`") | Unit file | "`systemctl unmask $unit`" |
| Mask "`$unit`" (add symlink to "`/dev/null`") | Unit file | "`systemctl mask $unit`" |
| Get default-target setting | Unit file | "`systemctl get-default`" |
| Set default-target to "`graphical`" (GUI system) | Unit file | "`systemctl set-default graphical`" |
| Set default-target to "`multi-user`" (CLI system) | Unit file | "`systemctl set-default multi-user`" |
| Show job environment | Environment | "`systemctl show-environment`" |
| Set job environment "`variable`" to "`value`" | Environment | "`systemctl set-environment variable=value`" |
| Unset job environment "`variable`" | Environment | "`systemctl unset-environment variable`" |
| Reload all unit files and daemons | Lifecycle | "`systemctl daemon-reload`" |
| Shut down the system | System | "`systemctl poweroff`" |
| Shut down and reboot the system | System | "`systemctl reboot`" |
| Suspend the system | System | "`systemctl suspend`" |
| Hibernate the system | System | "`systemctl hibernate`" |
| View job log of "`$unit`" | Journal | "`journalctl -u $unit`" |
| View job log of "`$unit`" ("`tail -f`" style) | Journal | "`journalctl -u $unit -f`" |
| Show time spent for each initialization steps | Analyze | "`systemd-analyze time`" |
| List of all units by the time to initialize | Analyze | "`systemd-analyze blame`" |
| Load and detect errors in "`$unit`" file | Analyze | "`systemd-analyze verify $unit`" |
| Track boot process by the `cgroups(7)` | Cgroup | "`systemd-cgls`" |
| Track boot process by the `cgroups(7)` | Cgroup | "`ps xawf -eo pid,user,cgroup,args`" |
| Track boot process by the `cgroups(7)` | Cgroup | Read [sysfs](https://en.wikipedia.org/wiki/Sysfs) under "`/sys/fs/cgroup/systemd/`" |

List of typical `systemd` management command snippets

Here, "`$unit`" in the above examples may be a single unit name (suffix such as `.service` and `.target` are optional) or, in many cases, multiple unit specifications (shell-style globs "`*`", "`?`", "`[]`" using `fnmatch(3)` which will be matched against the primary names of all units currently in memory).

System state changing commands in the above examples are typically preceded by the "`sudo`" to attain the required administrative privilege.

The output of the "`systemctl status $unit|$PID|$device`" uses color of the dot ("●") to summarize the unit state at a glance.

- White "●" indicates an "inactive" or "deactivating" state.

- Red "●" indicates a "failed" or "error" state.

- Green "●" indicates an "active", "reloading" or "activating" state.

### Customizing systemd

With default installation, many network services (see [???](#_network_applications)) are started as daemon processes after `network.target` at boot time by `systemd`. The "`sshd`" is no exception. Let's change this to on-demand start of "`sshd`" as a customization example.

First, disable system installed service unit.

     $ sudo systemctl stop sshd.service
     $ sudo systemctl mask sshd.service

The on-demand socket activation system of the classic Unix services was through the `indetd` superserver. Under `systemd`, the equivalent can be enabled by adding **\*.socket** and **\*.service** unit configuration files.

`sshd.socket` for specifying a socket to listen on

    [Unit]
    Description=SSH Socket for Per-Connection Servers

    [Socket]
    ListenStream=22
    Accept=yes

    [Install]
    WantedBy=sockets.target

`sshd@.service` as the matching service file of `sshd.socket`

    [Unit]
    Description=SSH Per-Connection Server

    [Service]
    ExecStart=-/usr/sbin/sshd -i
    StandardInput=socket

Then reload.

     $ sudo systemctl daemon-reload

## The udev system

For Linux kernel 2.6 and newer, [the udev system](https://en.wikipedia.org/wiki/Udev) provides mechanism for the automatic hardware discovery and initialization (see `udev(7)`). Upon discovery of each device by the kernel, the udev system starts a user process which uses information from the [sysfs](https://en.wikipedia.org/wiki/Sysfs) filesystem (see [???](#_procfs_and_sysfs)), loads required kernel modules supporting it using the `modprobe(8)` program (see [The kernel module initialization](#_the_kernel_module_initialization)), and creates corresponding device nodes.

> [!TIP]
> If "`/lib/modules/<kernel-version>/modules.dep`" was not generated properly by `depmod(8)` for some reason, modules may not be loaded as expected by the udev system. Execute "`depmod -a`" to fix it.

The name of device nodes can be configured by udev rule files in "`/etc/udev/rules.d/`". Current default rules tend to create dynamically generated names resulting non-static device names except for cd and network devices. By adding your custom rules similar to what cd and network devices do, you can generate static device names for other devices such as USB memory sticks, too. See "[Writing udev rules](http://www.reactivated.net/writing_udev_rules.html)" or "`/usr/share/doc/udev/writing_udev_rules/index.html`".

Since the udev system is somewhat a moving target, I leave details to other documentations and describe the minimum information here.

> [!TIP]
> For mounting rules in "`/etc/fstab`", device nodes do not need to be static ones. You can use [UUID](https://en.wikipedia.org/wiki/Universally_Unique_Identifier) to mount devices instead of device names such as "`/dev/sda`". See [???](#_accessing_partition_using_uuid).

### The kernel module initialization

The `modprobe(8)` program enables us to configure running Linux kernel from user process by adding and removing kernel modules. The udev system (see [The udev system](#_the_udev_system)) automates its invocation to help the kernel module initialization.

There are non-hardware modules and special hardware driver modules as the following which need to be pre-loaded by listing them in the "`/etc/modules`" file (see `modules(5)`).

- [TUN/TAP](https://en.wikipedia.org/wiki/TUN/TAP) modules providing virtual Point-to-Point network device (TUN) and virtual Ethernet network device (TAP),

- [netfilter](https://en.wikipedia.org/wiki/Netfilter) modules providing netfilter firewall capabilities (`iptables(8)`, [???](#_netfilter_infrastructure)), and

- [watchdog timer](https://en.wikipedia.org/wiki/Watchdog_timer) driver modules.

The configuration files for the `modprobe(8)` program are located under the "`/etc/modprobes.d/`" directory as explained in `modprobe.conf(5)`. (If you want to avoid some kernel modules to be auto-loaded, consider to blacklist them in the "`/etc/modprobes.d/blacklist`" file.)

The "`/lib/modules/<version>/modules.dep`" file generated by the `depmod(8)` program describes module dependencies used by the `modprobe(8)` program.

> [!NOTE]
> If you experience module loading issues with boot time module loading or with `modprobe(8)`, "`depmod -a`" may resolve these issues by reconstructing "`modules.dep`".

The `modinfo(8)` program shows information about a Linux kernel module.

The `lsmod(8)` program nicely formats the contents of the "`/proc/modules`", showing what kernel modules are currently loaded.

> [!TIP]
> You can identify exact hardware on your system. See [???](#_hardware_identification).

> [!TIP]
> You may configure hardware at boot time to activate expected hardware features. See [???](#_hardware_configuration).

> [!TIP]
> You can probably add support for your special device by recompiling the kernel. See [???](#_the_kernel).
