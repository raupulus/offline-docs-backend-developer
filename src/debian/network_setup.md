---
title: Network setup
source_url: https://www.debian.org/doc/manuals/debian-reference/_network_setup
source_repo: https://salsa.debian.org/debian/debian-reference.git
source_ref: master
source_commit: b7239e647
source_path: 05_network_setup.rawxml
technology: debian
version: 12 (Bookworm)
license: GPL-2.0-or-later
retrieved_at: '2026-09-15'
order: 60
---

## Network setup

> [!TIP]
> For general guide to the GNU/Linux networking, read the [Linux Network Administrators Guide](http://www.tldp.org/LDP/nag2/).

> [!TIP]
> For modern Debian specific guide to the networking, read [The Debian Administrator's Handbook — Configuring the Network](https://www.debian.org/doc/manuals/debian-handbook/sect.network-config).

> [!WARNING]
> Instead of using the traditional interface naming scheme ("`eth0`", "`eth1`", "`wlan0`", …), the newer [systemd](https://en.wikipedia.org/wiki/Systemd) uses "[Predictable Network Interface Names](https://www.freedesktop.org/wiki/Software/systemd/PredictableNetworkInterfaceNames/)" such as "`enp0s25`".

> [!WARNING]
> This chapter is getting outdated since this is based on Debian 7.0 (`Wheezy`) released in 2013.

> [!TIP]
> Although this document still uses old `ifconfig(8)` with IPv4 for its network configuration examples, Debian is moving to `ip(8)` with IPv4+IPv6 in the `wheezy` release. Patches to update this document are welcomed.

> [!TIP]
> Under [systemd](https://en.wikipedia.org/wiki/Systemd), [networkd](https://en.wikipedia.org/wiki/Systemd#networkd) may be used to manage networks. See `systemd-networkd(8)`.

## The basic network infrastructure

Let's review the basic network infrastructure on the modern Debian system.

| packages | popcon | size | type | description |
|:---|:---|:---|:---|:---|
| `ifupdown` | @-@popcon1@-@ | @-@psize1@-@ | config::ifupdown | standardized tool to bring up and down the network (Debian specific) |
| `ifplugd` | @-@popcon1@-@ | @-@psize1@-@ | , , | manage the wired network automatically |
| `ifupdown-extra` | @-@popcon1@-@ | @-@psize1@-@ | , , | network testing script to enhance "`ifupdown`" package |
| `ifmetric` | @-@popcon1@-@ | @-@psize1@-@ | , , | set routing metrics for a network interface |
| `guessnet` | @-@popcon1@-@ | @-@psize1@-@ | , , | mapping script to enhance "`ifupdown`" package via "`/etc/network/interfaces`" file |
| `ifscheme` | @-@popcon1@-@ | @-@psize1@-@ | , , | mapping scripts to enhance "`ifupdown`" package |
| `network-manager` | @-@popcon1@-@ | @-@psize1@-@ | config::NM | [NetworkManager](https://en.wikipedia.org/wiki/NetworkManager) (daemon): manage the network automatically |
| `network-manager-gnome` | @-@popcon1@-@ | @-@psize1@-@ | , , | [NetworkManager](https://en.wikipedia.org/wiki/NetworkManager) (GNOME frontend) |
| `wicd` | @-@popcon1@-@ | @-@psize1@-@ | config::wicd | wired and wireless network manager (metapackage) |
| `wicd-cli` | @-@popcon1@-@ | @-@psize1@-@ | , , | wired and wireless network manager (command-line client) |
| `wicd-curses` | @-@popcon1@-@ | @-@psize1@-@ | , , | wired and wireless network manager (Curses client) |
| `wicd-daemon` | @-@popcon1@-@ | @-@psize1@-@ | , , | wired and wireless network manager (daemon) |
| `wicd-gtk` | @-@popcon1@-@ | @-@psize1@-@ | , , | wired and wireless network manager (GTK+ client) |
| `iptables` | @-@popcon1@-@ | @-@psize1@-@ | config::Netfilter | administration tools for packet filtering and NAT ([Netfilter](https://en.wikipedia.org/wiki/Netfilter)) |
| `iproute2` | @-@popcon1@-@ | @-@psize1@-@ | config::iproute2 | [iproute2](http://www.linuxfoundation.org/collaborate/workgroups/networking/iproute2), IPv6 and other advanced network configuration: `ip(8)`, `tc(8)`, etc |
| `ifrename` | @-@popcon1@-@ | @-@psize1@-@ | , , | rename network interfaces based on various static criteria: `ifrename(8)` |
| `ethtool` | @-@popcon1@-@ | @-@psize1@-@ | , , | display or change Ethernet device settings |
| `iputils-ping` | @-@popcon1@-@ | @-@psize1@-@ | test::iproute2 | test network reachability of a remote host by [hostname](https://en.wikipedia.org/wiki/Hostname) or [IP address](https://en.wikipedia.org/wiki/IP_address) ([iproute2](http://www.linuxfoundation.org/collaborate/workgroups/networking/iproute2)) |
| `iputils-arping` | @-@popcon1@-@ | @-@psize1@-@ | , , | test network reachability of a remote host specified by the [ARP](https://en.wikipedia.org/wiki/Address_Resolution_Protocol) address |
| `iputils-tracepath` | @-@popcon1@-@ | @-@psize1@-@ | , , | trace the network path to a remote host |
| `net-tools` | @-@popcon1@-@ | @-@psize1@-@ | config::net-tools | NET-3 networking toolkit ([net-tools](http://www.linuxfoundation.org/collaborate/workgroups/networking/net-tools), IPv4 network configuration): `ifconfig(8)` etc. |
| `inetutils-ping` | @-@popcon1@-@ | @-@psize1@-@ | test::net-tools | test network reachability of a remote host by [hostname](https://en.wikipedia.org/wiki/Hostname) or [IP address](https://en.wikipedia.org/wiki/IP_address) (legacy, GNU) |
| `arping` | @-@popcon1@-@ | @-@psize1@-@ | , , | test network reachability of a remote host specified by the [ARP](https://en.wikipedia.org/wiki/Address_Resolution_Protocol) address (legacy) |
| `traceroute` | @-@popcon1@-@ | @-@psize1@-@ | , , | trace the network path to a remote host (legacy, console) |
| `isc-dhcp-client` | @-@popcon1@-@ | @-@psize1@-@ | config::low-level | DHCP client |
| `wpasupplicant` | @-@popcon1@-@ | @-@psize1@-@ | , , | client support for WPA and WPA2 (IEEE 802.11i) |
| `wpagui` | @-@popcon1@-@ | @-@psize1@-@ | , , | Qt GUI client for wpa_supplicant |
| `wireless-tools` | @-@popcon1@-@ | @-@psize1@-@ | , , | tools for manipulating Linux Wireless Extensions |
| `ppp` | @-@popcon1@-@ | @-@psize1@-@ | , , | PPP/PPPoE connection with `chat` |
| `pppoeconf` | @-@popcon1@-@ | @-@psize1@-@ | config::helper | configuration helper for PPPoE connection |
| `pppconfig` | @-@popcon1@-@ | @-@psize1@-@ | , , | configuration helper for PPP connection with `chat` |
| `wvdial` | @-@popcon1@-@ | @-@psize1@-@ | , , | configuration helper for PPP connection with `wvdial` and `ppp` |
| `mtr-tiny` | @-@popcon1@-@ | @-@psize1@-@ | test::low-level | trace the network path to a remote host (curses) |
| `mtr` | @-@popcon1@-@ | @-@psize1@-@ | , , | trace the network path to a remote host (curses and GTK+) |
| `gnome-nettool` | @-@popcon1@-@ | @-@psize1@-@ | , , | tools for common network information operations (GNOME) |
| `nmap` | @-@popcon1@-@ | @-@psize1@-@ | , , | network mapper / port scanner ([Nmap](https://en.wikipedia.org/wiki/Nmap), console) |
| `zenmap` | @-@popcon1@-@ | @-@psize1@-@ | , , | network mapper / port scanner (GTK+) |
| `tcpdump` | @-@popcon1@-@ | @-@psize1@-@ | , , | network traffic analyzer ([Tcpdump](https://en.wikipedia.org/wiki/Tcpdump), console) |
| `wireshark` | @-@popcon1@-@ | @-@psize1@-@ | , , | network traffic analyzer ([Wireshark](https://en.wikipedia.org/wiki/Wireshark), GTK+) |
| `tshark` | @-@popcon1@-@ | @-@psize1@-@ | , , | network traffic analyzer (console) |
| `tcptrace` | @-@popcon1@-@ | @-@psize1@-@ | , , | produce a summarization of the connections from `tcpdump` output |
| `snort` | @-@popcon1@-@ | @-@psize1@-@ | , , | flexible network intrusion detection system ([Snort](https://en.wikipedia.org/wiki/Snort_(software))) |
| `ntopng` | @-@popcon1@-@ | @-@psize1@-@ | , , | display network usage in web browser |
| `dnsutils` | @-@popcon1@-@ | @-@psize1@-@ | , , | network clients provided with [BIND](https://en.wikipedia.org/wiki/BIND): `nslookup(8)`, `nsupdate(8)`, `dig(8)` |
| `dlint` | @-@popcon1@-@ | @-@psize1@-@ | , , | check [DNS](https://en.wikipedia.org/wiki/Domain_Name_System) zone information using nameserver lookups |
| `dnstracer` | @-@popcon1@-@ | @-@psize1@-@ | , , | trace a chain of [DNS](https://en.wikipedia.org/wiki/Domain_Name_System) servers to the source |

List of network configuration tools

### The hostname resolution

The hostname resolution is currently supported by the [NSS (Name Service Switch)](https://en.wikipedia.org/wiki/Name_Service_Switch) mechanism too. The flow of this resolution is the following.

1.  The "`/etc/nsswitch.conf`" file with stanza like "`hosts: files dns`" dictates the hostname resolution order. (This replaces the old functionality of the "`order`" stanza in "`/etc/host.conf`".)

2.  The `files` method is invoked first. If the hostname is found in the "`/etc/hosts`" file, it returns all valid addresses for it and exits. (The "`/etc/host.conf`" file contains "`multi on`".)

3.  The `dns` method is invoked. If the hostname is found by the query to the [Internet Domain Name System (DNS)](https://en.wikipedia.org/wiki/Domain_Name_System) identified by the "`/etc/resolv.conf`" file, it returns all valid addresses for it and exits.

For example, "`/etc/hosts`" looks like the following.

    127.0.0.1 localhost
    127.0.1.1 <host_name>

    # The following lines are desirable for IPv6 capable hosts
    ::1     ip6-localhost ip6-loopback
    fe00::0 ip6-localnet
    ff00::0 ip6-mcastprefix
    ff02::1 ip6-allnodes
    ff02::2 ip6-allrouters
    ff02::3 ip6-allhosts

Each line starts with a [IP address](https://en.wikipedia.org/wiki/IP_address) and it is followed by the associated [hostname](https://en.wikipedia.org/wiki/Hostname).

The IP address `127.0.1.1` in the second line of this example may not be found on some other Unix-like systems. The [Debian Installer](https://en.wikipedia.org/wiki/Debian-Installer) creates this entry for a system without a permanent IP address as a workaround for some software (e.g., GNOME) as documented in the [bug \#719621](http://bugs.debian.org/719621).

The \<host_name\> matches the hostname defined in the "`/etc/hostname`".

For a system with a permanent IP address, that permanent IP address should be used here instead of `127.0.1.1`.

For a system with a permanent IP address and a [fully qualified domain name (FQDN)](https://en.wikipedia.org/wiki/FQDN) provided by the [Domain Name System (DNS)](https://en.wikipedia.org/wiki/Domain_Name_System), that canonical \<host_name\>.\<domain_name\> should be used instead of just \<host_name\>.

The "`/etc/resolv.conf`" is a static file if the `resolvconf` package is not installed. If installed, it is a symbolic link. Either way, it contains information that initialize the resolver routines. If the DNS is found at IP="`192.168.11.1`", it contains the following.

    nameserver 192.168.11.1

The `resolvconf` package makes this "`/etc/resolv.conf`" into a symbolic link and manages its contents by the hook scripts automatically.

For the PC workstation on the typical adhoc LAN environment, the hostname can be resolved via Multicast DNS (mDNS, [Zeroconf](https://en.wikipedia.org/wiki/Zeroconf)) in addition to the basic `files` and `dns` methods.

- [Avahi](https://en.wikipedia.org/wiki/Avahi_(software)) provides a framework for Multicast DNS Service Discovery on Debian.

- It is equivalent of [Apple Bonjour / Apple Rendezvous](https://en.wikipedia.org/wiki/Bonjour_(software)).

- The `libnss-mdns` plugin package provides host name resolution via mDNS for the GNU Name Service Switch (NSS) functionality of the GNU C Library (glibc).

- The "`/etc/nsswitch.conf`" file should have stanza like "`hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4`".

- Host names ending with the [".local"](https://en.wikipedia.org/wiki/.local) [pseudo-top-level domain](https://en.wikipedia.org/wiki/Pseudo-top-level_domain) (TLD) are resolved.

- The mDNS IPv4 link-local multicast address "`224.0.0.251`" or its IPv6 equivalent "`FF02::FB`" are used to make DNS query for a name ending with "`.local`".

The hostname resolution via deprecated [NETBios over TCP/IP](https://en.wikipedia.org/wiki/NetBIOS_over_TCP/IP) used by the older Windows system can be provided by installing the `winbind` package. The "`/etc/nsswitch.conf`" file should have stanza like "`hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4 wins`" to enable this functionality. (Modern Windows system usually use the `dns` method for the hostname resolution.)

> [!NOTE]
> The [expansion of generic Top-Level Domains (gTLD)](http://newgtlds.icann.org/en/program-status/delegated-strings) in the [Domain Name System](https://en.wikipedia.org/wiki/Domain_Name_System) is underway. Watch out for the [name collision](http://icannwiki.com/Name_Collision) when chosing a domain name used only within LAN.

### The network interface name

The network interface name, e.g. `eth0`, is assigned to each hardware in the Linux kernel through the user space configuration mechanism, `udev` (see [???](#_the_udev_system)), as it is found. The network interface name is referred as **physical interface** in `ifup(8)` and `interfaces(5)`.

In order to ensure each network interface to be named persistently for each reboot using [MAC address](https://en.wikipedia.org/wiki/MAC_address) etc., there is a rules file "`/etc/udev/rules.d/70-persistent-net.rules`". This file is automatically generated by the "`/lib/udev/write_net_rules`" program, probably run by the "`persistent-net-generator.rules`" rules file. You can modify it to change naming rule.

> [!CAUTION]
> When editing the "`/etc/udev/rules.d/70-persistent-net.rules`" rules file, you must keep each rule on a single line and the [MAC address](https://en.wikipedia.org/wiki/MAC_address) in lowercase. For example, if you find "FireWire device" and "PCI device" in this file, you probably want to name "PCI device" as `eth0` and configure it as the primary network interface.

### The network address range for the LAN

Let us be reminded of the IPv4 32 bit address ranges in each class reserved for use on the [local area networks (LANs)](https://en.wikipedia.org/wiki/Local_area_network) by [rfc1918](http://tools.ietf.org/html/rfc1918). These addresses are guaranteed not to conflict with any addresses on the Internet proper.

| Class | network addresses           | net mask      | net mask /bits | \# of subnets |
|:------|:----------------------------|:--------------|:---------------|:--------------|
| A     | 10.x.x.x                    | 255.0.0.0     | /8             | 1             |
| B     | 172.16.x.x — 172.31.x.x     | 255.255.0.0   | /16            | 16            |
| C     | 192.168.0.x — 192.168.255.x | 255.255.255.0 | /24            | 256           |

List of network address ranges

> [!NOTE]
> If one of these addresses is assigned to a host, then that host must not access the Internet directly but must access it through a gateway that acts as a proxy for individual services or else does [Network Address Translation (NAT)](https://en.wikipedia.org/wiki/Network_address_translation). The broadband router usually performs NAT for the consumer LAN environment.

### The network device support

Although most hardware devices are supported by the Debian system, there are some network devices which require [DFSG](https://www.debian.org/social_contract#guidelines) non-free firmware to support them. Please see [???](#_hardware_drivers_and_firmware).

## The modern network configuration for desktop

Network interfaces are typically initialized in "`networking.service`" for the `lo` interface and "`NetworkManager.service`" for other interfaces on modern Debian desktop system under `systemd`.

Debian `squeeze` and newer can manage the network connection via management [daemon](https://en.wikipedia.org/wiki/Daemon_(computer_software)) software such as [NetworkManager (NM)](https://en.wikipedia.org/wiki/NetworkManager) (network-manager and associated packages) or [Wicd](https://en.wikipedia.org/wiki/Wicd_(Linux_Network_Manager)) (wicd and associated packages).

- They come with their own [GUI](https://en.wikipedia.org/wiki/Graphical_user_interface) and command-line programs as their user interfaces.

- They come with their own [daemon](https://en.wikipedia.org/wiki/Daemon_(computer_software)) as their backend system.

- They allow easy connection of your system to the Internet.

- They allow easy management of wired and wireless network configuration.

- They allow us to configure network independent of the legacy `ifupdown` package.

> [!NOTE]
> Do not use these automatic network configuration tools for servers. These are aimed primarily for mobile desktop users on laptops.

These modern network configuration tools need to be configured properly to avoid conflicting with the legacy `ifupdown` package and its configuration file "`/etc/network/interfaces`".

> [!NOTE]
> Some features of these automatic network configuration tools may suffer regressions. These are not as robust as the legacy `ifupdown` package. Check [BTS of network-manager](http://bugs.debian.org/cgi-bin/pkgreport.cgi?package=network-manager) and [BTS of wicd](http://bugs.debian.org/cgi-bin/pkgreport.cgi?package=wicd) for current issues and limitations.

### GUI network configuration tools

Official documentations for NM and Wicd on Debian are provided in "`/usr/share/doc/network-manager/README.Debian`" and "`/usr/share/doc/wicd/README.Debian`", respectively.

Essentially, the network configuration for desktop is done as follows.

1.  Make desktop user, e.g. `foo`, belong to group "`netdev`" by the following (Alternatively, do it automatically via [D-bus](https://en.wikipedia.org/wiki/D-Bus) under modern desktop environments such as GNOME and KDE).

        $ sudo adduser foo netdev

2.  Keep configuration of "`/etc/network/interfaces`" as simple as in the following.

        auto lo
        iface lo inet loopback

3.  Restart NM or Wicd by the following.

        $ sudo /etc/init.d/network-manager restart

        $ sudo /etc/init.d/wicd restart

4.  Configure your network via GUI.

> [!NOTE]
> Only interfaces which are **not** listed in "`/etc/network/interfaces`" are managed by NM or Wicd to avoid conflict with `ifupdown`.

> [!TIP]
> If you wish to extend network configuration capabilities of NM, please seek appropriate plug-in modules and supplemental packages such as `network-manager-openconnect`, `network-manager-openvpn-gnome`, `network-manager-pptp-gnome`, `mobile-broadband-provider-info`, `gnome-bluetooth`, etc. The same goes for those of Wicd.

> [!CAUTION]
> These automatic network configuration tools may not be compatible with esoteric configurations of legacy `ifupdown` in "`/etc/network/interfaces`" such as ones in [The basic network configuration with ifupdown (legacy)](#_the_basic_network_configuration_with_ifupdown_legacy) and [The advanced network configuration with ifupdown (legacy)](#_the_advanced_network_configuration_with_ifupdown_legacy). Check [BTS of network-manager](http://bugs.debian.org/cgi-bin/pkgreport.cgi?package=network-manager) and [BTS of wicd](http://bugs.debian.org/cgi-bin/pkgreport.cgi?package=wicd) for current issues and limitations.

## The modern network configuration without GUI

Under [systemd](https://en.wikipedia.org/wiki/Systemd), the network may be configured in `/etc/systemd/network/` instead. See `systemd-resolved(8)`, `resolved.conf(5)`, and `systemd-networkd(8)`.

This allows the modern network configuration without GUI.

A DHCP client configuration can be set up by creating "`/etc/systemd/network/dhcp.network`". E.g.:

    [Match]
    Name=en*

    [Network]
    DHCP=yes

A static network configuration can be set up by creating "`/etc/systemd/network/static.network`". E.g.:

    [Match]
    Name=en*

    [Network]
    Address=192.168.0.15/24
    Gateway=192.168.0.1

## The legacy network connection and configuration

When the method described in [The modern network configuration for desktop](#_the_modern_network_configuration_for_desktop) does not suffice your needs, you should use the legacy network connection and configuration method which combines many simpler tools.

The legacy network connection is specific for each method (see [The network connection method (legacy)](#_the_network_connection_method_legacy)).

There are 2 types of programs for the low level network configuration on Linux (see [Iproute2 commands](#_iproute2_commands)).

- Old [net-tools](http://www.linuxfoundation.org/collaborate/workgroups/networking/net-tools) programs (`ifconfig(8)`, …) are from the Linux NET-3 networking system. Most of these are obsolete now.

- New [Linux iproute2](http://www.linuxfoundation.org/collaborate/workgroups/networking/iproute2) programs (`ip(8)`, …) are the current Linux networking system.

Although these low level networking programs are powerful, they are cumbersome to use. So high level network configuration systems have been created.

The `ifupdown` package is the de facto standard for such high level network configuration system on Debian. It enables you to bring up network simply by doing , e.g., "`ifup eth0`". Its configuration file is the "`/etc/network/interfaces`" file and its typical contents are the following.

    auto lo
    iface lo inet loopback

    auto eth0
    iface eth0 inet dhcp

The `resolvconf` package was created to supplement `ifupdown` system to support smooth reconfiguration of network address resolution by automating rewrite of resolver configuration file "`/etc/resolv.conf`". Now, most Debian network configuration packages are modified to use `resolvconf` package (see "`/usr/share/doc/resolvconf/README.Debian`").

Helper scripts to the `ifupdown` package such as `ifplugd`, `guessnet`, `ifscheme`, etc. are created to automate dynamic configuration of network environment such as one for mobile PC on wired LAN. These are relatively difficult to use but play well with existing `ifupdown` system.

These are explained in detail with examples (see [The basic network configuration with ifupdown (legacy)](#_the_basic_network_configuration_with_ifupdown_legacy) and [The advanced network configuration with ifupdown (legacy)](#_the_advanced_network_configuration_with_ifupdown_legacy)).

## The network connection method (legacy)

> [!CAUTION]
> The connection test methods described in this section are meant for testing purposes. It is not meant to be used directly for the daily network connection. You are advised to use NM, Wicd, or the `ifupdown` package instead (see [The modern network configuration for desktop](#_the_modern_network_configuration_for_desktop) and [The basic network configuration with ifupdown (legacy)](#_the_basic_network_configuration_with_ifupdown_legacy)).

The typical network connection method and connection path for a PC can be summarized as the following.

| PC | connection method | connection path |
|:---|:---|:---|
| Serial port (`ppp0`) | PPP | ⇔ [modem](https://en.wikipedia.org/wiki/Modem) ⇔ POTS ⇔ dial-up access point ⇔ ISP |
| Ethernet port (`eth0`) | PPPoE/DHCP/Static | ⇔ BB-modem ⇔ BB service ⇔ BB access point ⇔ ISP |
| Ethernet port (`eth0`) | DHCP/Static | ⇔ LAN ⇔ BB-router with [network address translation (NAT)](https://en.wikipedia.org/wiki/Network_address_translation) (⇔ BB-modem …) |

List of network connection methods and connection paths

Here is the summary of configuration scripts for each connection method.

| connection method | configuration | backend package(s) |
|:---|:---|:---|
| PPP | `pppconfig` to create deterministic chat | `pppconfig`, `ppp` |
| PPP (alternative) | `wvdialconf` to create heuristic chat | `ppp`, `wvdial` |
| PPPoE | `pppoeconf` to create deterministic chat | `pppoeconf`, `ppp` |
| DHCP | described in "`/etc/dhcp/dhclient.conf`" | `isc-dhcp-client` |
| static IP (IPv4) | described in "`/etc/network/interfaces`" | `iproute` or `net-tools` (obsolete) |
| static IP (IPv6) | described in "`/etc/network/interfaces`" | `iproute` |

List of network connection configurations

The network connection acronyms mean the following.

| acronym | meaning |
|:---|:---|
| [POTS](https://en.wikipedia.org/wiki/Plain_old_telephone_service) | plain old telephone service |
| BB | [broadband](https://en.wikipedia.org/wiki/Broadband) |
| BB-service | e.g., the digital subscriber line (DSL), the cable TV, or the fiber to the premises (FTTP) |
| BB-modem | e.g., [the DSL modem](https://en.wikipedia.org/wiki/DSL_modem), [the cable modem](https://en.wikipedia.org/wiki/Cable_modem), or [the optical network terminal (ONT)](https://en.wikipedia.org/wiki/FTTP) |
| [LAN](https://en.wikipedia.org/wiki/Local_area_network) | local area network |
| [WAN](https://en.wikipedia.org/wiki/Wide_area_network) | wide area network |
| [DHCP](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol) | dynamic host configuration protocol |
| [PPP](https://en.wikipedia.org/wiki/Point-to-Point_Protocol) | point-to-point protocol |
| [PPPoE](https://en.wikipedia.org/wiki/Point-to-Point_Protocol_over_Ethernet) | point-to-point protocol over Ethernet |
| [ISP](https://en.wikipedia.org/wiki/ISP) | Internet service provider |

List of network connection acronyms

> [!NOTE]
> The WAN connection services via cable TV are generally served by DHCP or PPPoE. The ones by ADSL and FTTP are generally served by PPPoE. You have to consult your ISP for exact configuration requirements of the WAN connection.

> [!NOTE]
> When BB-router is used to create home LAN environment, PCs on LAN are connected to the WAN via BB-router with [network address translation (NAT)](https://en.wikipedia.org/wiki/Network_address_translation). For such case, PC's network interfaces on the LAN are served by static IP or DHCP from the BB-router. BB-router must be configured to connect the WAN following the instruction by your ISP.

### The DHCP connection with the Ethernet

The typical modern home and small business network, i.e. LAN, are connected to the WAN (Internet) using some consumer grade broadband router. The LAN behind this router is usually served by the [dynamic host configuration protocol (DHCP)](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol) server running on the router.

Just install the `isc-dhcp-client` package for the Ethernet served by the [dynamic host configuration protocol (DHCP)](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol).

See `dhclient.conf(5)`.

### The static IP connection with the Ethernet

No special action is needed for the Ethernet served by the static IP.

### The PPP connection with pppconfig

The configuration script `pppconfig` configures the [PPP](https://en.wikipedia.org/wiki/Point-to-Point_Protocol) connection interactively just by selecting the following.

- The telephone number

- The ISP user name

- The ISP password

- The port speed

- The modem communication port

- The authentication method

| file | function |
|:---|:---|
| `/etc/ppp/peers/<isp_name>` | The `pppconfig` generated configuration file for `pppd` specific to \<isp_name\> |
| `/etc/chatscripts/<isp_name>` | The `pppconfig` generated configuration file for `chat` specific to \<isp_name\> |
| `/etc/ppp/options` | The general execution parameter for `pppd` |
| `/etc/ppp/pap-secret` | Authentication data for the [PAP](https://en.wikipedia.org/wiki/Password_authentication_protocol) (security risk) |
| `/etc/ppp/chap-secret` | Authentication data for the [CHAP](https://en.wikipedia.org/wiki/Challenge-handshake_authentication_protocol) (more secure) |

List of configuration files for the [PPP](https://en.wikipedia.org/wiki/Point-to-Point_Protocol) connection with pppconfig

> [!CAUTION]
> The "\<isp_name\>" value of "`provider`" is assumed if `pon` and `poff` commands are invoked without arguments.

You can test configuration using low level network configuration tools as the following.

    $ sudo pon <isp_name>
    ...
    $ sudo poff <isp_name>

See "`/usr/share/doc/ppp/README.Debian.gz`".

### The alternative PPP connection with wvdialconf

A different approach to using `pppd(8)` is to run it from `wvdial(1)` which comes in the `wvdial` package. Instead of `pppd` running `chat(8)` to dial in and negotiate the connection, `wvdial` does the dialing and initial negotiating and then starts `pppd` to do the rest.

The configuration script `wvdialconf` configures the PPP connection interactively just by selecting the following.

- The telephone number

- The ISP user name

- The ISP password

`wvdial` succeeds in making the connection in most cases and maintains authentication data list automatically.

| file | function |
|:---|:---|
| `/etc/ppp/peers/wvdial` | The `wvdialconf` generated configuration file for `pppd` specific to `wvdial` |
| `/etc/wvdial.conf` | The `wvdialconf` generated configuration file |
| `/etc/ppp/options` | The general execution parameter for `pppd` |
| `/etc/ppp/pap-secret` | Authentication data for the [PAP](https://en.wikipedia.org/wiki/Password_authentication_protocol) (security risk) |
| `/etc/ppp/chap-secret` | Authentication data for the [CHAP](https://en.wikipedia.org/wiki/Challenge-handshake_authentication_protocol) (more secure) |

List of configuration files for the PPP connection with wvdialconf

You can test configuration using low level network configuration tools as the following.

    $ sudo wvdial
    ...
    $ sudo killall wvdial

See `wvdial(1)` and `wvdial.conf(5)`.

### The PPPoE connection with pppoeconf

When your ISP serves you with PPPoE connection and you decide to connect your PC directly to the WAN, the network of your PC must be configured with the PPPoE. The PPPoE stand for PPP over Ethernet. The configuration script `pppoeconf` configures the PPPoE connection interactively.

The configuration files are the following.

| file | function |
|:---|:---|
| `/etc/ppp/peers/dsl-provider` | The `pppoeconf` generated configuration file for `pppd` specific to `pppoe` |
| `/etc/ppp/options` | The general execution parameter for `pppd` |
| `/etc/ppp/pap-secret` | Authentication data for the [PAP](https://en.wikipedia.org/wiki/Password_authentication_protocol) (security risk) |
| `/etc/ppp/chap-secret` | Authentication data for the [CHAP](https://en.wikipedia.org/wiki/Challenge-handshake_authentication_protocol) (more secure) |

List of configuration files for the PPPoE connection with pppoeconf

You can test configuration using low level network configuration tools as the following.

    $ sudo /sbin/ifconfig eth0 up
    $ sudo pon dsl-provider
    ...
    $ sudo poff dsl-provider
    $ sudo /sbin/ifconfig eth0 down

See "`/usr/share/doc/pppoeconf/README.Debian`".

## The basic network configuration with ifupdown (legacy)

The traditional [TCP/IP network](https://en.wikipedia.org/wiki/Internet_Protocol_Suite) setup on the Debian system uses `ifupdown` package as a high level tool. There are 2 typical cases.

- For **dynamic IP** system such as mobile PCs, you should setup TCP/IP network **with** the `resolvconf` package and enable you to switch your network configuration easily (see [The network interface served by the DHCP](#_the_network_interface_served_by_the_dhcp)).

- For **static IP** system such as servers, you should setup TCP/IP network **without** the `resolvconf` package and keep your system simple (see [The network interface with the static IP](#_the_network_interface_with_the_static_ip)).

These traditional setup methods are quite useful if you wish to set up advanced configuration; find details in the following.

The `ifupdown` package provides the standardized framework for the high level network configuration in the Debian system. In this section, we learn the basic network configuration with `ifupdown` with simplified introduction and many typical examples.

### The command syntax simplified

The `ifupdown` package contains 2 commands: `ifup(8)` and `ifdown(8)`. They offer high level network configuration dictated by the configuration file "/etc/network/interfaces".

| command | action |
|:---|:---|
| `ifup eth0` | bring up a network interface `eth0` with the configuration `eth0` if "`iface eth0`" stanza exists |
| `ifdown eth0` | bring down a network interface `eth0` with the configuration `eth0` if "`iface eth0`" stanza exists |

List of basic network configuration commands with ifupdown

> [!WARNING]
> Do not use low level configuration tools such as `ifconfig(8)` and `ip(8)` commands to configure an interface in **up** state.

> [!NOTE]
> There is no command `ifupdown`.

### The basic syntax of "/etc/network/interfaces"

The key syntax of "`/etc/network/interfaces`" as explained in `interfaces(5)` can be summarized as the following.

| stanza | meaning |
|:---|:---|
| "`auto <interface_name>`" | start interface \<interface_name\> upon start of the system |
| "`allow-auto <interface_name>`" | , , |
| "`allow-hotplug <interface_name>`" | start interface \<interface_name\> when the kernel detects a hotplug event from the interface |
| Lines started with "`iface <config_name> …`" | define the network configuration \<config_name\> |
| Lines started with "`mapping <interface_name_glob>`" | define mapping value of \<config_name\> for the matching \<interface_name\> |
| A line starting with a hash "`#`" | ignore as comments (end-of-line comments are **not** supported) |
| A line ending with a backslash "`\`" | extend the configuration to the next line |

List of stanzas in "`/etc/network/interfaces`" {#list-of-stanzas-in-eni}

Lines started with **`iface`** stanza has the following syntax.

    iface <config_name> <address_family> <method_name>
     <option1> <value1>
     <option2> <value2>
     ...

For the basic configuration, the **`mapping`** stanza is not used and you use the network interface name as the network configuration name (See [The mapping stanza](#_the_mapping_stanza)).

> [!WARNING]
> Do not define duplicates of the "`iface`" stanza for a network interface in "`/etc/network/interfaces`".

### The loopback network interface

The following configuration entry in the "`/etc/network/interfaces`" file brings up the loopback network interface `lo` upon booting the system (via **`auto`** stanza).

    auto lo
    iface lo inet loopback

This one always exists in the "`/etc/network/interfaces`" file.

### The network interface served by the DHCP

After preparing the system by [The DHCP connection with the Ethernet](#_the_dhcp_connection_with_the_ethernet), the network interface served by the DHCP is configured by creating the configuration entry in the "`/etc/network/interfaces`" file as the following.

    allow-hotplug eth0
    iface eth0 inet dhcp

When the Linux kernel detects the physical interface `eth0`, the **`allow-hotplug`** stanza causes `ifup` to bring up the interface and the **`iface`** stanza causes `ifup` to use DHCP to configure the interface.

### The network interface with the static IP

The network interface served by the static IP is configured by creating the configuration entry in the "`/etc/network/interfaces`" file as the following.

    allow-hotplug eth0
    iface eth0 inet static
     address 192.168.11.100
     netmask 255.255.255.0
     gateway 192.168.11.1
     dns-domain example.com
     dns-nameservers 192.168.11.1

When the Linux kernel detects the physical interface `eth0`, the **`allow-hotplug`** stanza causes `ifup` to bring up the interface and the **`iface`** stanza causes `ifup` to use the static IP to configure the interface.

Here, I assumed the following.

- IP address range of the LAN network: `192.168.11.0` - `192.168.11.255`

- IP address of the gateway: `192.168.11.1`

- IP address of the PC: `192.168.11.100`

- The `resolvconf` package: installed

- The domain name: "`example.com`"

- IP address of the DNS server: `192.168.11.1`

When the `resolvconf` package is not installed, DNS related configuration needs to be done manually by editing the "`/etc/resolv.conf`" as the following.

    nameserver 192.168.11.1
    domain example.com

> [!CAUTION]
> The IP addresses used in the above example are not meant to be copied literally. You have to adjust IP numbers to your actual network configuration.

### The basics of wireless LAN interface

The [wireless LAN (WLAN for short)](https://en.wikipedia.org/wiki/Wireless_LAN) provides the fast wireless connectivity through the spread-spectrum communication of unlicensed radio bands based on the set of standards called [IEEE 802.11](https://en.wikipedia.org/wiki/IEEE_802.11).

The WLAN interfaces are almost like normal Ethernet interfaces but require some network ID and encryption key data to be provided when they are initialized. Their high level network tools are exactly the same as that of Ethernet interfaces except interface names are a bit different like `eth1`, `wlan0`, `ath0`, `wifi0`, … depending on the kernel drivers used.

> [!TIP]
> The `wmaster0` device is the master device which is an internal device used only by [SoftMAC](https://en.wikipedia.org/wiki/SoftMAC) with new [mac80211 API of Linux](http://linuxwireless.org/).

Here are some keywords to remember for the WLAN.

| acronym | full word | meaning |
|:---|:---|:---|
| NWID | Network ID | 16 bit network ID used by pre-802.11 [WaveLAN](https://en.wikipedia.org/wiki/WaveLAN) network (very deprecated) |
| (E)SSID | (Extended) [Service Set Identifier](https://en.wikipedia.org/wiki/Service_set_identifier) | network name of the [Wireless Access Points (APs)](https://en.wikipedia.org/wiki/Wireless_access_point) interconnected to form an integrated [802.11 wireless LAN](https://en.wikipedia.org/wiki/IEEE_802.11), Domain ID |
| WEP, (WEP2) | [Wired Equivalent Privacy](https://en.wikipedia.org/wiki/Wired_Equivalent_Privacy) | 1st generation 64-bit (128-bit) wireless encryption standard with 40-bit key (deprecated) |
| WPA | [Wi-Fi Protected Access](https://en.wikipedia.org/wiki/Wi-Fi_Protected_Access) | 2nd generation wireless encryption standard (most of 802.11i), compatible with WEP |
| WPA2 | [Wi-Fi Protected Access 2](https://en.wikipedia.org/wiki/IEEE_802.11i) | 3rd generation wireless encryption standard (full 802.11i), non-compatible with WEP |

List of acronyms for WLAN

The actual choice of protocol is usually limited by the wireless router you deploy.

### The wireless LAN interface with WPA/WPA2

You need to install the `wpasupplicant` package to support the WLAN with the new WPA/WPA2.

In case of the [DHCP](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol) served IP on WLAN connection, the "`/etc/network/interfaces`" file entry should be as the following.

    allow-hotplug ath0
    iface ath0 inet dhcp
     wpa-ssid homezone
     # hexadecimal psk is encoded from a plaintext passphrase
     wpa-psk 000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f

See "`/usr/share/doc/wpasupplicant/README.modes.gz`".

### The wireless LAN interface with WEP

You need to install the `wireless-tools` package to support the WLAN with the old WEP. (Your consumer grade router may still be using this insecure infrastructure but this is better than nothing.)

> [!CAUTION]
> Please note that your network traffic on WLAN with WEP may be sniffed by others.

In case of the [DHCP](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol) served IP on WLAN connection, the "`/etc/network/interfaces`" file entry should be as the following.

    allow-hotplug eth0
    iface eth0 inet dhcp
     wireless-essid Home
     wireless-key1 0123-4567-89ab-cdef
     wireless-key2 12345678
     wireless-key3 s:password
     wireless-defaultkey 2
     wireless-keymode open

See "`/usr/share/doc/wireless-tools/README.Debian`".

### The PPP connection

You need to configure the PPP connection first as described before (see [The PPP connection with pppconfig](#_the_ppp_connection_with_pppconfig)). Then, add the "`/etc/network/interfaces`" file entry for the primary PPP device `ppp0` as the following.

    iface ppp0 inet ppp
     provider <isp_name>

### The alternative PPP connection

You need to configure the alternative PPP connection with `wvdial` first as described before (see [The alternative PPP connection with wvdialconf](#_the_alternative_ppp_connection_with_wvdialconf)). Then, add the "`/etc/network/interfaces`" file entry for the primary PPP device `ppp0` as the following.

    iface ppp0 inet wvdial

### The PPPoE connection

For PC connected directly to the WAN served by the PPPoE, you need to configure system with the PPPoE connection as described before (see [The PPPoE connection with pppoeconf](#_the_pppoe_connection_with_pppoeconf)). Then, add the "`/etc/network/interfaces`" file entry for the primary PPPoE device `eth0` as the following.

    allow-hotplug eth0
    iface eth0 inet manual
     pre-up /sbin/ifconfig eth0 up
     up ifup ppp0=dsl
     down ifdown ppp0=dsl
     post-down /sbin/ifconfig eth0 down
    # The following is used internally only
    iface dsl inet ppp
     provider dsl-provider

### The network configuration state of ifupdown

The "`/etc/network/run/ifstate`" file stores the **intended** network configuration states for all the currently active network interfaces managed by the `ifupdown` package. Unfortunately, even if the `ifupdown` system fails to bring up the interface as intended, the "`/etc/network/run/ifstate`" file lists it active.

Unless the output of the `ifconfig(8)` command for an interface does not have a line like following example, it can not be used as a part of [IPV4 network](https://en.wikipedia.org/wiki/IPv4).

      inet addr:192.168.11.2  Bcast:192.168.11.255  Mask:255.255.255.0

> [!NOTE]
> For the Ethernet device connected to the PPPoE, the output of the `ifconfig(8)` command lacks a line which looks like above example.

### The basic network reconfiguration

When you try to reconfigure the interface, e.g. `eth0`, you must disable it first with the "**`sudo ifdown eth0`**" command. This removes the entry of `eth0` from the "`/etc/network/run/ifstate`" file. (This may result in some error message if `eth0` is not active or it is configured improperly previously. So far, it seems to be safe to do this for the simple single user work station at any time.)

You are now free to rewrite the "`/etc/network/interfaces`" contents as needed to reconfigure the network interface, `eth0`.

Then, you can reactivate `eth0` with the "**`sudo ifup eth0`**" command.

> [!TIP]
> You can (re)initialize the network interface simply by "**`sudo ifdown eth0;sudo ifup eth0`**".

### The ifupdown-extra package

The `ifupdown-extra` package provides easy network connection tests for use with the `ifupdown` package.

- The `network-test(1)` command can be used from the shell.

- The automatic scripts are run for each `ifup` command execution.

The `network-test` command frees you from the execution of cumbersome low level commands to analyze the network problem.

The automatic scripts are installed in "`/etc/network/*/`" and perform the following.

- Check the network cable connection

- Check duplicate use of IP address

- Setup system's static routes based on the "`/etc/network/routes`" definition

- Check if network gateway is reachable

- Record results in the "`/var/log/syslog`" file

This syslog record is quite useful for administration of the network problem on the remote system.

> [!TIP]
> The automatic behavior of the `ifupdown-extra` package is configurable with the "`/etc/default/network-test`". Some of these automatic checks slow down the system boot-up a little bit since it takes some time to listen for [ARP](https://en.wikipedia.org/wiki/Address_Resolution_Protocol) replies.

## The advanced network configuration with ifupdown (legacy)

The functionality of the `ifupdown` package can be improved beyond what was described in [The basic network configuration with ifupdown (legacy)](#_the_basic_network_configuration_with_ifupdown_legacy) with the advanced knowledge.

The functionalities described here are completely optional. I, being lazy and minimalist, rarely bother to use these.

> [!CAUTION]
> If you could not set up network connection by information in [The basic network configuration with ifupdown (legacy)](#_the_basic_network_configuration_with_ifupdown_legacy), you make situation worse by using information below.

### The ifplugd package

The `ifplugd` package is an older automatic network configuration tool which can manage only Ethernet connections. This solves unplugged/replugged Ethernet cable issues for mobile PC etc. If you have [NetworkManager](https://en.wikipedia.org/wiki/NetworkManager) or [Wicd](https://en.wikipedia.org/wiki/Wicd_(Linux_Network_Manager)) (see [The modern network configuration for desktop](#_the_modern_network_configuration_for_desktop)) installed, you do not need this package.

This package runs a [daemon](https://en.wikipedia.org/wiki/Daemon_(computer_software)) and replaces **auto** or **allow-hotplug** functionalities (see [List of stanzas in ""](#list-of-stanzas-in-eni)) and starts interfaces upon their connection to the network.

Here is how to use the `ifplugd` package for the internal Ethernet port, e.g. `eth0`.

1.  Remove stanza in "`/etc/network/interfaces`": "`auto eth0`" or "`allow-hotplug eth0`".

2.  Keep stanza in "`/etc/network/interfaces`": "`iface eth0 inet …`" and "`mapping …`".

3.  Install the `ifplugd` package.

4.  Run "`sudo dpkg-reconfigure ifplugd`".

5.  Put `eth0` as the "static interfaces to be watched by ifplugd".

Now, the network reconfiguration works as you desire.

- Upon power-on or upon hardware discovery, the interface is not brought up by itself.

  - Quick boot process without the long DHCP timeout.

  - No funny activated interface without proper IPv4 address (see [The network configuration state of ifupdown](#_the_network_configuration_state_of_ifupdown)).

- Upon finding the Ethernet cable, the interface is brought up.

- Upon some time after unplugging the Ethernet cable, the interface is brought down automatically.

- Upon plugging in another Ethernet cable, the interface is brought up under the new network environment.

> [!TIP]
> The arguments for the `ifplugd(8)` command can set its behaviors such as the delay for reconfiguring interfaces.

### The ifmetric package

The `ifmetric` package enables us to manipulate metrics of routes a posteriori even for DHCP.

The following sets the `eth0` interface to be preferred over the `wlan0` interface.

1.  Install the `ifmetric` package.

2.  Add an option line with "`metric 0`" just below the "`iface eth0 inet dhcp`" line in "`/etc/network/interfaces`".

3.  Add an option line with "`metric 1`" just below the "`iface wlan0 inet dhcp`" line in "`/etc/network/interfaces`".

The metric 0 means the highest priority route and is the default one. The larger metric value means lower priority routes. The IP address of the active interface with the lowest metric value becomes the originating one. See `ifmetric(8)`.

### The virtual interface

A single physical Ethernet interface can be configured as multiple virtual interfaces with different IP addresses. Usually the purpose is to connect an interface to several IP subnetworks. For example, IP address based virtual web hosting by a single network interface is one such application.

For example, let's suppose the following.

- A single Ethernet interface on your host is connected to a Ethernet hub (not to the broadband router).

- The Ethernet hub is connected to both the Internet and LAN network.

- The LAN network uses subnet `192.168.0.x/24`.

- Your host uses DHCP served IP address with the physical interface `eth0` for the Internet.

- Your host uses `192.168.0.1` with the virtual interface `eth0:0` for the LAN.

The following stanzas in "`/etc/network/interfaces`" configure your network.

    iface eth0 inet dhcp
     metric 0
    iface eth0:0 inet static
     address 192.168.0.1
     netmask 255.255.255.0
     network 192.168.0.0
     metric 1

> [!CAUTION]
> Although this configuration example with [network address translation (NAT)](https://en.wikipedia.org/wiki/Network_address_translation) using [netfilter/iptables](https://en.wikipedia.org/wiki/Netfilter) (see [Netfilter infrastructure](#_netfilter_infrastructure)) can provide cheap router for the LAN with only single interface, there is no real firewall capability with such set up. You should use 2 physical interfaces with NAT to secure the local network from the Internet.

### The advanced command syntax

The `ifupdown` package offers advanced network configuration using the **network configuration** name and the **network interface** name. I use a terminology being slightly different from the one used in `ifup(8)` and `interfaces(5)`.

| manpage terminology | my terminology | examples in the following text | description |
|:---|:---|:---|:---|
| **physical interface** name | **network interface** name | `lo`, `eth0`, `<interface_name>` | name given by the Linux kernel (using `udev` mechanism) |
| **logical interface** name | **network configuration** name | `config1`, `config2`, `<config_name>` | name token following **`iface`** in the "`/etc/network/interfaces`" |

List of terminology for network devices

Basic network configuration commands in [The command syntax simplified](#_the_command_syntax_simplified) require the **network configuration** name token of the **`iface`** stanza to match the **network interface** name in the "`/etc/network/interfaces`".

Advanced network configuration commands enables separation of the **network configuration** name and the **network interface** name in the "`/etc/network/interfaces`" as the following.

| command | action |
|:---|:---|
| `ifup eth0=config1` | bring up a network interface `eth0` with the configuration `config1` |
| `ifdown eth0=config1` | bring down a network interface `eth0` with the configuration `config1` |
| `ifup eth0` | bring up a network interface `eth0` with the configuration selected by **`mapping`** stanza |
| `ifdown eth0` | bring down a network interface `eth0` with the configuration selected by **`mapping`** stanza |

List of advanced network configuration commands with ifupdown

### The mapping stanza

We skipped explaining the **`mapping`** stanza in the "`/etc/network/interfaces`" in [The basic syntax of "/etc/network/interfaces"](#_the_basic_syntax_of_etc_network_interfaces) to avoid complication. This stanza has the following syntax.

    mapping <interface_name_glob>
     script <script_name>
     map <script_input1>
     map <script_input2>
     map ...

This provides advanced features to the "`/etc/network/interfaces`" file by automating the choice of the configuration with the mapping script specified by `<script_name>`.

Let's follow the execution of the following.

    $ sudo ifup eth0

When the "`<interface_name_glob>`" matches "`eth0`", this execution produces the execution of the following command to configure `eth0` automatically.

    $ sudo ifup eth0=$(echo -e '<script_input1> \n <script_input2> \n ...' | <script_name> eth0)

Here, script input lines with "`map`" are optional and can be repeated.

> [!NOTE]
> The glob for **`mapping`** stanza works like shell filename glob (see [???](#_shell_glob)).

### The manually switchable network configuration

Here is how to switch manually among several network configurations without rewriting the "`/etc/network/interfaces`" file as in [The basic network reconfiguration](#_the_basic_network_reconfiguration) .

For all the network configuration you need to access, you create a separate stanza in "`/etc/network/interfaces`" file as the following.

    auto lo
    iface lo inet loopback

    iface config1 inet dhcp

    iface config2 inet static
     address 192.168.11.100
     netmask 255.255.255.0
     gateway 192.168.11.1
     dns-domain example.com
     dns-nameservers 192.168.11.1

    iface pppoe inet manual
     pre-up /sbin/ifconfig eth0 up
     up ifup ppp0=dsl
     down ifdown ppp0=dsl
     post-down /sbin/ifconfig eth0 down

    # The following is used internally only
    iface dsl inet ppp
     provider dsl-provider

    iface pots inet ppp
     provider provider

Please note the **network configuration name** which is the token after **`iface`** does not use the token for the **network interface name**. Also, there are no **`auto`** stanza nor **`allow-hotplug`** stanza to start the network interface `eth0` automatically upon events.

Now you are ready to switch the network configuration.

Let's move your PC to a LAN served by the DHCP. You bring up the **network interface** (the physical interface) `eth0` by assigning the **network configuration** name (the logical interface name) `config1` to it by the following.

    $ sudo ifup eth0=config1
    Password:
    ...

The interface `eth0` is up, configured by DHCP and connected to LAN.

    $ sudo ifdown eth0=config1
    ...

The interface `eth0` is down and disconnected from LAN.

Let's move your PC to a LAN served by the static IP. You bring up the **network interface** `eth0` by assigning the **network configuration** name `config2` to it by the following.

    $ sudo ifup eth0=config2
    ...

The interface `eth0` is up, configured with static IP and connected to LAN. The additional parameters given as `dns-*` configures "`/etc/resolv.conf`" contents. This "`/etc/resolv.conf`" is better manged if the `resolvconf` package is installed.

    $ sudo ifdown eth0=config2
    ...

The interface `eth0` is down and disconnected from LAN, again.

Let's move your PC to a port on BB-modem connected to the PPPoE served service. You bring up the **network interface** `eth0` by assigning the **network configuration** name `pppoe` to it by the following.

    $ sudo ifup eth0=pppoe
    ...

The interface `eth0` is up, configured with PPPoE connection directly to the ISP.

    $ sudo ifdown eth0=pppoe
    ...

The interface `eth0` is down and disconnected, again.

Let's move your PC to a location without LAN or BB-modem but with POTS and modem. You bring up the **network interface** `ppp0` by assigning the **network configuration** name `pots` to it by the following.

    $ sudo ifup ppp0=pots
    ...

The interface `ppp0` is up and connected to the Internet with PPP.

    $ sudo ifdown ppp0=pots
    ...

The interface `ppp0` is down and disconnected from the Internet.

You should check the "`/etc/network/run/ifstate`" file for the current network configuration state of the `ifupdown` system.

> [!WARNING]
> You may need to adjust numbers at the end of `eth*`, `ppp*`, etc. if you have multiple network interfaces.

### Scripting with the ifupdown system

The `ifupdown` system automatically runs scripts installed in "`/etc/network/*/`" while exporting environment variables to scripts.

| environment variable | value passed |
|:---|:---|
| "`$IFACE`" | physical name (interface name) of the interface being processed |
| "`$LOGICAL`" | logical name (configuration name) of the interface being processed |
| "`$ADDRFAM`" | \<address_family\> of the interface |
| "`$METHOD`" | \<method_name\> of the interface (e.g., "static") |
| "`$MODE`" | "start" if run from `ifup`, "stop" if run from `ifdown` |
| "`$PHASE`" | as per "`$MODE`", but with finer granularity, distinguishing the `pre-up`, `post-up`, `pre-down` and `post-down` phases |
| "`$VERBOSITY`" | indicates whether "`--verbose`" was used; set to 1 if so, 0 if not |
| "`$PATH`" | command search path: "`/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin`" |
| "`$IF_<OPTION>`" | value for the corresponding option under the **`iface`** stanza |

List of environment variables passed by the ifupdown system

Here, each environment variable, "`$IF_<OPTION>`", is created from the name for the corresponding option such as \<option1\> and \<option2\> by prepending "`$IF_`", converting the case to the upper case, replacing hyphens to underscores, and discarding non-alphanumeric characters.

> [!TIP]
> See [The basic syntax of "/etc/network/interfaces"](#_the_basic_syntax_of_etc_network_interfaces) for \<address_family\>, \<method_name\>, \<option1\> and \<option2\>.

The `ifupdown-extra` package (see [The ifupdown-extra package](#_the_ifupdown_extra_package)) uses these environment variables to extend the functionality of the `ifupdown` package. The `ifmetric` package (see [The ifmetric package](#_the_ifmetric_package)) installs the "`/etc/network/if-up.d/ifmetric`" script which sets the metric via the "`$IF_METRIC`" variable. The `guessnet` package (see [Mapping with guessnet](#_mapping_with_guessnet)), which provides simple and powerful framework for the auto-selection of the network configuration via the mapping mechanism, also uses these.

> [!NOTE]
> For more specific examples of custom network configuration scripts using these environment variables, you should check example scripts in "`/usr/share/doc/ifupdown/examples/*`" and scripts used in `ifscheme` and `ifupdown-scripts-zg2` packages. These additional scripts have some overlaps of functionalities with basic `ifupdown-extra` and `guessnet` packages. If you install these additional scripts, you should customize these scripts to avoid interferences.

### Mapping with guessnet

Instead of manually choosing configuration as described in [The manually switchable network configuration](#_the_manually_switchable_network_configuration), you can use the mapping mechanism described in [The mapping stanza](#_the_mapping_stanza) to select network configuration automatically with custom scripts.

The `guessnet-ifupdown(8)` command provided by the `guessnet` package is designed to be used as a mapping script and provides powerful framework to enhance the `ifupdown` system.

- You list test condition as the value for **`guessnet`** options for each network configuration under **`iface`** stanza.

- Mapping choses the **`iface`** with first non-ERROR result as the network configuration.

This dual usage of the "`/etc/network/interfaces`" file by the mapping script, `guessnet-ifupdown`, and the original network configuration infrastructure, `ifupdown`, does not cause negative impacts since **`guessnet`** options only export extra environment variables to scripts run by the `ifupdown` system. See details in `guessnet-ifupdown(8)`.

> [!NOTE]
> When multiple **`guessnet`** option lines are required in "`/etc/network/interfaces`", use option lines started with **`guessnet1`**, **`guessnet2`**, and so on, since the `ifupdown` package does not allow starting strings of option lines to be repeated.

## The low level network configuration

### Iproute2 commands

[Iproute2](http://www.linuxfoundation.org/collaborate/workgroups/networking/iproute2) commands offer complete low-level network configuration capabilities. Here is a translation table from obsolete [net-tools](http://www.linuxfoundation.org/collaborate/workgroups/networking/net-tools) commands to new [iproute2](http://www.linuxfoundation.org/collaborate/workgroups/networking/iproute2) etc. commands.

| obsolete net-tools | new iproute2 etc. | manipulation |
|:---|:---|:---|
| `ifconfig(8)` | `ip addr` | protocol (IP or IPv6) address on a device |
| `route(8)` | `ip route` | routing table entry |
| `arp(8)` | `ip neigh` | ARP or NDISC cache entry |
| `ipmaddr` | `ip maddr` | multicast address |
| `iptunnel` | `ip tunnel` | tunnel over IP |
| `nameif(8)` | `ifrename(8)` | name network interfaces based on MAC addresses |
| `mii-tool(8)` | `ethtool(8)` | Ethernet device settings |

Translation table from obsolete `net-tools` commands to new `iproute2` commands

See `ip(8)` and [IPROUTE2 Utility Suite Howto](http://www.policyrouting.org/iproute2.doc.html).

### Safe low level network operations

You may use low level network commands as follows safely since they do not change network configuration.

| command | description |
|:---|:---|
| `ifconfig` | display the link and address status of active interfaces |
| `ip addr show` | display the link and address status of active interfaces |
| `route -n` | display all the routing table in numerical addresses |
| `ip route show` | display all the routing table in numerical addresses |
| `arp` | display the current content of the [ARP](https://en.wikipedia.org/wiki/Address_Resolution_Protocol) cache tables |
| `ip neigh` | display the current content of the [ARP](https://en.wikipedia.org/wiki/Address_Resolution_Protocol) cache tables |
| `plog` | display ppp daemon log |
| `ping yahoo.com` | check the Internet connection to "`yahoo.com`" |
| `whois yahoo.com` | check who registered "`yahoo.com`" in the domains database |
| `traceroute yahoo.com` | trace the Internet connection to "`yahoo.com`" |
| `tracepath yahoo.com` | trace the Internet connection to "`yahoo.com`" |
| `mtr yahoo.com` | trace the Internet connection to "`yahoo.com`" (repeatedly) |
| `dig [@dns-server.com] example.com [{a|mx|any}]` | check [DNS](https://en.wikipedia.org/wiki/Domain_Name_System) records of "`example.com`" by "`dns-server.com`" for a "`a`", "`mx`", or "`any`" record |
| `iptables -L -n` | check packet filter |
| `netstat -a` | find all open ports |
| `netstat -l --inet` | find listening ports |
| `netstat -ln --tcp` | find listening TCP ports (numeric) |
| `dlint example.com` | check DNS zone information of "`example.com`" |

List of low level network commands

> [!TIP]
> Some of these low level network configuration tools reside in "`/sbin/`". You may need to issue full command path such as "`/sbin/ifconfig`" or add "`/sbin`" to the "`$PATH`" list in your "`~/.bashrc`".

## Network optimization

Generic network optimization is beyond the scope of this documentation. I touch only subjects pertinent to the consumer grade connection.

| packages | popcon | size | description |
|:---|:---|:---|:---|
| `iftop` | @-@popcon1@-@ | @-@psize1@-@ | display bandwidth usage information on an network interface |
| `iperf` | @-@popcon1@-@ | @-@psize1@-@ | Internet Protocol bandwidth measuring tool |
| `ifstat` | @-@popcon1@-@ | @-@psize1@-@ | InterFace STATistics Monitoring |
| `bmon` | @-@popcon1@-@ | @-@psize1@-@ | portable bandwidth monitor and rate estimator |
| `ethstatus` | @-@popcon1@-@ | @-@psize1@-@ | script that quickly measures network device throughput |
| `bing` | @-@popcon1@-@ | @-@psize1@-@ | empirical stochastic bandwidth tester |
| `bwm-ng` | @-@popcon1@-@ | @-@psize1@-@ | small and simple console-based bandwidth monitor |
| `ethstats` | @-@popcon1@-@ | @-@psize1@-@ | console-based Ethernet statistics monitor |
| `ipfm` | @-@popcon1@-@ | @-@psize1@-@ | bandwidth analysis tool |

List of network optimization tools

### Finding optimal MTU

The [Maximum Transmission Unit (MTU)](https://en.wikipedia.org/wiki/Maximum_transmission_unit) value can be determined experimentally with `ping(8)` with "`-M do`" option which sends ICMP packets with data size starting from 1500 (with offset of 28 bytes for the IP+ICMP header) and finding the largest size without IP fragmentation.

For example, try the following

    $ ping -c 1 -s $((1500-28)) -M do www.debian.org
    PING www.debian.org (194.109.137.218) 1472(1500) bytes of data.
    From 192.168.11.2 icmp_seq=1 Frag needed and DF set (mtu = 1454)

    --- www.debian.org ping statistics ---
    0 packets transmitted, 0 received, +1 errors

Try 1454 instead of 1500

You see `ping(8)` succeed with 1454.

This process is [Path MTU (PMTU) discovery](https://en.wikipedia.org/wiki/Path_MTU_discovery) ([RFC1191](http://tools.ietf.org/html/rfc1191)) and the `tracepath(8)` command can automate this.

> [!TIP]
> The above example with PMTU value of 1454 is for my previous FTTP provider which used [Asynchronous Transfer Mode](https://en.wikipedia.org/wiki/Asynchronous_Transfer_Mode) (ATM) as its backbone network and served its clients with the [PPPoE](https://en.wikipedia.org/wiki/Point-to-Point_Protocol_over_Ethernet). The actual PMTU value depends on your environment, e.g., 1500 for the my new FTTP provider.

| network environment | MTU | rationale |
|:---|:---|:---|
| Dial-up link (IP: PPP) | 576 | standard |
| Ethernet link (IP: DHCP or fixed) | 1500 | standard and default |
| Ethernet link (IP: PPPoE) | 1492 (=1500-8) | 2 bytes for PPP header and 6 bytes for PPPoE header |
| Ethernet link (ISP's backbone: ATM, IP: DHCP or fixed) | 1462 (=48\*31-18-8) | author's speculation: 18 bytes for Ethernet header, 8 bytes for SAR trailer |
| Ethernet link (ISP's backbone: ATM, IP: PPPoE) | 1454 (=48\*31-8-18-8) | see "[Optimal MTU configuration for PPPoE ADSL Connections](http://www.mynetwatchman.com/kb/ADSL/pppoemtu.htm)" for rationale |

Basic guide lines of the optimal MTU value

In addtion to these basic guide lines, you should know the following.

- Any use of tunneling methods ([VPN](https://en.wikipedia.org/wiki/Virtual_private_network) etc.) may reduce optimal MTU further by their overheads.

- The MTU value should not exceed the experimentally determined PMTU value.

- The bigger MTU value is generally better when other limitations are met.

### Setting MTU

Here are examples for setting the MTU value from its default 1500 to 1454.

For the DHCP (see [The network interface served by the DHCP](#_the_network_interface_served_by_the_dhcp)), you can replace pertinent **`iface`** stanza lines in the "`/etc/network/interfaces`" with the following.

    iface eth0 inet dhcp
     pre-up /sbin/ifconfig $IFACE mtu 1454

For the static IP (see [The network interface with the static IP](#_the_network_interface_with_the_static_ip)), you can replace pertinent **`iface`** stanza lines in the "`/etc/network/interfaces`" with the following.

    iface eth0 inet static
     address 192.168.11.100
     netmask 255.255.255.0
     gateway 192.168.11.1
     mtu 1454
     dns-domain example.com
     dns-nameservers 192.168.11.1

For the direct PPPoE (see [The PPPoE connection with pppoeconf](#_the_pppoe_connection_with_pppoeconf)), you can replace pertinent "`mtu`" line in the "`/etc/ppp/peers/dsl-provider`" with the following.

    mtu 1454

The [maximum segment size](https://en.wikipedia.org/wiki/Maximum_segment_size) (MSS) is used as an alternative measure of packet size. The relationship between MSS and MTU are the following.

- MSS = MTU - 40 for IPv4

- MSS = MTU - 60 for IPv6

> [!NOTE]
> The `iptables(8)` (see [Netfilter infrastructure](#_netfilter_infrastructure)) based optimization can clamp packet size by the MSS and is useful for the router. See "TCPMSS" in `iptables(8)`.

### WAN TCP optimization

The TCP throughput can be maximized by adjusting TCP buffer size parameters as described in "[TCP Tuning Guide](http://dsd.lbl.gov/TCP-tuning/)" and "[TCP tuning](https://en.wikipedia.org/wiki/TCP_tuning)" for the modern high-bandwidth and high-latency WAN. So far, the current Debian default settings serve well even for my LAN connected by the fast 1G bps FTTP service.

## Netfilter infrastructure

[Netfilter](https://en.wikipedia.org/wiki/Netfilter) provides infrastructure for [stateful firewall](https://en.wikipedia.org/wiki/Stateful_firewall) and [network address translation (NAT)](https://en.wikipedia.org/wiki/Network_address_translation) with [Linux kernel](https://en.wikipedia.org/wiki/Linux_kernel) modules (see [???](#_the_kernel_module_initialization)).

| packages | popcon | size | description |
|:---|:---|:---|:---|
| `iptables` | @-@popcon1@-@ | @-@psize1@-@ | administration tools for [netfilter](https://en.wikipedia.org/wiki/Netfilter) (`iptables(8)` for IPv4, `ip6tables(8)` for IPv6) |
| `arptables` | @-@popcon1@-@ | @-@psize1@-@ | administration tools for [netfilter](https://en.wikipedia.org/wiki/Netfilter) (`arptables(8)` for ARP) |
| `ebtables` | @-@popcon1@-@ | @-@psize1@-@ | administration tools for [netfilter](https://en.wikipedia.org/wiki/Netfilter) (`ebtables(8)` for Ethernet bridging) |
| `iptstate` | @-@popcon1@-@ | @-@psize1@-@ | continuously monitor [netfilter](https://en.wikipedia.org/wiki/Netfilter) state (similar to `top(1)`) |
| `shorewall-init` | @-@popcon1@-@ | @-@psize1@-@ | [Shoreline Firewall](https://en.wikipedia.org/wiki/Shorewall) initialization |
| `shorewall` | @-@popcon1@-@ | @-@psize1@-@ | [Shoreline Firewall](https://en.wikipedia.org/wiki/Shorewall), [netfilter](https://en.wikipedia.org/wiki/Netfilter) configuration file generator |
| `shorewall-lite` | @-@popcon1@-@ | @-@psize1@-@ | [Shoreline Firewall](https://en.wikipedia.org/wiki/Shorewall), [netfilter](https://en.wikipedia.org/wiki/Netfilter) configuration file generator (light version) |
| `shorewall6` | @-@popcon1@-@ | @-@psize1@-@ | [Shoreline Firewall](https://en.wikipedia.org/wiki/Shorewall), [netfilter](https://en.wikipedia.org/wiki/Netfilter) configuration file generator (IPv6 version) |
| `shorewall6-lite` | @-@popcon1@-@ | @-@psize1@-@ | [Shoreline Firewall](https://en.wikipedia.org/wiki/Shorewall), [netfilter](https://en.wikipedia.org/wiki/Netfilter) configuration file generator (IPv6, light version) |

List of firewall tools

Main user space program of [netfilter](https://en.wikipedia.org/wiki/Netfilter) is `iptables(8)`. You can manually configure [netfilter](https://en.wikipedia.org/wiki/Netfilter) interactively from shell, save its state with `iptables-save(8)`, and restore it via init script with `iptables-restore(8)` upon system reboot.

Configuration helper scripts such as [shorewall](https://en.wikipedia.org/wiki/Shorewall) ease this process.

See documentations at <http://www.netfilter.org/documentation/> (or in "`/usr/share/doc/iptables/html/`").

- [Linux Networking-concepts HOWTO](http://www.netfilter.org/documentation/HOWTO/networking-concepts-HOWTO.html)

- [Linux 2.4 Packet Filtering HOWTO](http://www.netfilter.org/documentation/HOWTO/packet-filtering-HOWTO.html)

- [Linux 2.4 NAT HOWTO](http://www.netfilter.org/documentation/HOWTO/NAT-HOWTO.html)

> [!TIP]
> Although these were written for Linux **2.4**, both `iptables(8)` command and netfilter kernel function apply for Linux **2.6** and **3.x** kernel series.
