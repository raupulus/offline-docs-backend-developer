---
title: The X Window System
source_url: https://www.debian.org/doc/manuals/debian-reference/_the_x_window_system
source_repo: https://salsa.debian.org/debian/debian-reference.git
source_ref: master
source_commit: b7239e647
source_path: 07_the_x_window_system.rawxml
technology: debian
version: 12 (Bookworm)
license: GPL-2.0-or-later
retrieved_at: '2026-09-15'
order: 80
---

## The X Window System

> [!WARNING]
> This chapter is getting outdated since this is based on Debian 7.0 (`Wheezy`) released in 2013.

The [X Window System](https://en.wikipedia.org/wiki/X_Window_System) on the Debian system is based on the source from [X.Org](http://www.x.org/).

## Key packages

There are a few (meta)packages provided to ease installation.

| (meta)package | popcon | size | description |
|:---|:---|:---|:---|
| `xorg` | @-@popcon1@-@ | @-@psize1@-@ | X libraries, an X server, a set of fonts, and a group of basic X clients and utilities (metapackage) |
| `xserver-xorg` | @-@popcon1@-@ | @-@psize1@-@ | full suite of the X server and its configuration |
| `xbase-clients` | @-@popcon1@-@ | @-@psize1@-@ | miscellaneous assortment of X clients (metapackage) |
| `x11-common` | @-@popcon1@-@ | @-@psize1@-@ | filesystem infrastructure for the X Window System |
| `xorg-docs` | @-@popcon1@-@ | @-@psize1@-@ | miscellaneous documentation for the X.Org software suite |
| `menu` | @-@popcon1@-@ | @-@psize1@-@ | generate the Debian menu for all menu-aware applications |
| `menu-xdg` | @-@popcon1@-@ | @-@psize1@-@ | convert the Debian menu structure to the [freedesktop.org](https://en.wikipedia.org/wiki/Freedesktop.org) xdg menu structure |
| `xdg-utils` | @-@popcon1@-@ | @-@psize1@-@ | utilities to integrate desktop environment provided by the [freedesktop.org](https://en.wikipedia.org/wiki/Freedesktop.org) |
| `task-gnome-desktop` | @-@popcon1@-@ | @-@psize1@-@ | standard [GNOME](https://en.wikipedia.org/wiki/GNOME) desktop environment (metapackage) |
| `task-kde-desktop` | @-@popcon1@-@ | @-@psize1@-@ | core [KDE](https://en.wikipedia.org/wiki/KDE) desktop environment (metapackage) |
| `task-xfce-desktop` | @-@popcon1@-@ | @-@psize1@-@ | [Xfce](https://en.wikipedia.org/wiki/Xfce) lightweight desktop environment (metapackage) |
| `task-lxde-desktop` | @-@popcon1@-@ | @-@psize1@-@ | [LXDE](https://en.wikipedia.org/wiki/LXDE) lightweight desktop environment (metapackage) |
| `fluxbox` | @-@popcon1@-@ | @-@psize1@-@ | [Fluxbox](https://en.wikipedia.org/wiki/Fluxbox): package for highly configurable and low resource [X window manager](https://en.wikipedia.org/wiki/X_window_manager) |

List of key (meta)packages for X Window

For the basics of X, refer to `X(7)` and [the LDP XWindow-User-HOWTO](http://www.tldp.org/HOWTO/XWindow-User-HOWTO.html).

## Setting up desktop environment

A [desktop environment](https://en.wikipedia.org/wiki/Desktop_environment) is usually a combination of a [X window manager](https://en.wikipedia.org/wiki/X_window_manager), a file manager, and a suite of compatible utility programs.

You can setup a full [desktop environment](https://en.wikipedia.org/wiki/Desktop_environment) such as [GNOME](https://en.wikipedia.org/wiki/GNOME), [KDE](https://en.wikipedia.org/wiki/KDE), [Xfce](https://en.wikipedia.org/wiki/Xfce), or [LXDE](https://en.wikipedia.org/wiki/LXDE), from the `aptitude` under the task menu.

> [!TIP]
> Task menu may be out of sync with the latest package transition state under Debian `unstable`/`testing` environment. In such situation, you need to deselect some (meta)packages listed under `aptitude(8)` task menu to avoid package conflicts. When deselecting (meta)packages, you must select certain packages providing their dependencies manually to avoid them deleted automatically.

You may alternatively setup a simple environment manually just with a [X window manager](https://en.wikipedia.org/wiki/X_window_manager) such as [Fluxbox](https://en.wikipedia.org/wiki/Fluxbox).

See [Window Managers for X](http://www.xwinman.org) for the guide to the X window manager and the desktop environment.

### Debian menu

[Debian menu system](https://www.debian.org/doc/packaging-manuals/menu.html/) provides a general interface for both text- and X-oriented programs with `update-menus(1)` from the `menu` package. Each package installs its menu data in the "`/usr/share/menu/`" directory. See "`/usr/share/menu/README`".

### Freedesktop.org menu

Each package which is compliant to Freedesktop.org's xdg menu system installs its menu data provided by "`*.desktop`" under "`/usr/share/applications/`". Modern desktop environments which are compliant to Freedesktop.org standard use these data to generate their menu using the `xdg-utils` package. See "`/usr/share/doc/xdg-utils/README`".

### Debian menu from Freedesktop.org menu

In order to access the traditional Debian menu from the [Freedesktop.org menu](http://www.freedesktop.org/wiki/Specifications/menu-spec/) compliant window manager environment such as GNOME and KDE, you must install the `menu-xdg` package.

## The server/client relationship

The X Window System is activated as a combination of the server and client programs. The meaning for the words **server** and **client** with respect to the words **local** and **remote** requires attention here.

| type | description |
|:---|:---|
| **X server** | a program run on a **local host** connected to the user's display and input devices. |
| **X client** | a program run on a **remote host** that processes data and talks to the X server. |
| **application server** | a program run on a **remote host** that processes data and talks to the application clients. |
| **application client** | a program run on a **local host** connected to the user's display and input devices. |

List of server/client terminology

Modern X servers have [the MIT Shared Memory Extension](https://en.wikipedia.org/wiki/MIT-SHM) and communicate with their local X clients using the local shared memory. This bypasses the network transparent Xlib interprocess communication channel and gains performance for large images.

## The X server

See `xorg(1)` for X server information.

### The (re)configuration of the X server

The following (re)configures an X server.

    # dpkg-reconfigure --priority=low x11-common

> [!NOTE]
> Recent Linux kernels have good graphics and input device supports with [DRM](https://en.wikipedia.org/wiki/Direct_Rendering_Manager), [KMS](https://wiki.debian.org/KernelModesetting), and [udev](https://en.wikipedia.org/wiki/Udev). X server is rewritten to use them. So "`/etc/X11/xorg.conf`" is usually not present on your system. These parameters are configured by the kernel. See "`fb/modedb.txt`" in the Linux kernel documentation.

For the large high resolution CRT monitor, it is a good idea to set the refresh rate as high as your monitor can handle (85 Hz is great, 75 Hz is OK) to reduce flicker. For the LCD monitor, slower standard refresh rate (60Hz) is usually fine due to its slow response.

> [!NOTE]
> Be careful not to use too high refresh rate which may cause fatal hardware failure of your monitor system.

### The connection methods to the X server

There are several ways of getting the "X server" (**display** side) to accept connections from an "X client" (**application** side).

| package | popcon | size | user | encryption | method | pertinent use |
|:---|:---|:---|:---|:---|:---|:---|
| `xbase-clients` | @-@popcon1@-@ | @-@psize1@-@ | unchecked | no | `xhost` command | deprecated |
| `xbase-clients` | @-@popcon1@-@ | @-@psize1@-@ | checked | no | `xauth` command | local connection via pipe |
| `openssh-client` | @-@popcon1@-@ | @-@psize1@-@ | checked | yes | `ssh -X` command | remote network connection |
| `gdm3` | @-@popcon1@-@ | @-@psize1@-@ | checked | no (XDMCP) | GNOME display manager | local connection via pipe |
| `sddm` | @-@popcon1@-@ | @-@psize1@-@ | checked | no (XDMCP) | KDE display manager | local connection via pipe |
| `xdm` | @-@popcon1@-@ | @-@psize1@-@ | checked | no (XDMCP) | X display manager | local connection via pipe |
| `wdm` | @-@popcon1@-@ | @-@psize1@-@ | checked | no (XDMCP) | WindowMaker display manager | local connection via pipe |
| `ldm` | @-@popcon1@-@ | @-@psize1@-@ | checked | yes | LTSP display manager | remote SSH network connection (thin client) |

List of connection methods to the X server

> [!WARNING]
> Do not use remote [TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)/[IP](https://en.wikipedia.org/wiki/Internet_Protocol) connection over **unsecured** network for X connection unless you have very good reason such as use of encryption. A remote TCP/IP socket connection without encryption is prone to the **eavesdropping attack** and is disabled by default on the Debian system. Use "`ssh -X`".

> [!WARNING]
> Do not use [XDMCP connection](https://en.wikipedia.org/wiki/X_display_manager) over **unsecured** network either. It sends data via [UDP](https://en.wikipedia.org/wiki/User_Datagram_Protocol)/[IP](https://en.wikipedia.org/wiki/Internet_Protocol) without encryption and is prone to the **eavesdropping attack**.

> [!TIP]
> LTSP stands for [Linux Terminal Server Project](https://en.wikipedia.org/wiki/Linux_Terminal_Server_Project).

## Starting the X Window System

The X Window System is usually started as an [X session](https://en.wikipedia.org/wiki/X_session_manager) which is the combination of an X server and connecting X clients. For the normal desktop system, both of them are executed on a workstation.

The [X session](https://en.wikipedia.org/wiki/X_session_manager) is started by one of the following.

- `startx` command started from the command line

- One of the [X display manager](https://en.wikipedia.org/wiki/X_display_manager) daemon programs `*dm` started by `systemd` based on the dependency of "`graphical.target`".

> [!TIP]
> The start up script for the display manager daemons checks the content of the "`/etc/X11/default-display-manager`" file before actually executing themselves. This ensures to have only one [X display manager](https://en.wikipedia.org/wiki/X_display_manager) daemon program activated.

> [!TIP]
> See [???](#_specific_locale_only_under_x_window) for initial environment variables of the X display manager.

Essentially, all these programs execute the "`/etc/X11/Xsession`" script. Then the "`/etc/X11/Xsession`" script performs `run-parts(8)` like action to execute scripts in the "`/etc/X11/Xsession.d/`" directory. This is essentially an execution of the first program which is found in the following order by the `exec` builtin command.

1.  The script specified as the argument of "`/etc/X11/Xsession`" by the X display manager, if it is defined.

2.  The "`~/.xsession`" or "`~/.Xsession`" script, if it is defined.

3.  The "`/usr/bin/x-session-manager`" command, if it is defined.

4.  The "`/usr/bin/x-window-manager`" command, if it is defined.

5.  The "`/usr/bin/x-terminal-emulator`" command, if it is defined.

This process is affected by the content of "`/etc/X11/Xsession.options`". The exact programs to which these "`/usr/bin/x-*`" commands point, are determined by the Debian alternatives system and changed by "`update-alternatives --config x-session-manager`", etc.

See `Xsession(5)` for details.

### Starting X session with gdm3

`gdm3(1)` lets you select the session type (or desktop environment: [Setting up desktop environment](#_setting_up_desktop_environment)), and language (or locale: [???](#_the_locale)) of the X session from its menu. It keeps the selected default value in "`~/.dmrc`" as the following.

    [Desktop]
    Session=default
    Language=ja_JP.UTF-8

### Customizing the X session (classic method)

On a system where "`/etc/X11/Xsession.options`" contains a line "`allow-user-xsession`" without preceding "`#`" characters, any user who defines "`~/.xsession`" or "`~/.Xsession`" is able to customize the action of "`/etc/X11/Xsession`" by completely overriding the system code. The last command in the "`~/.xsession`" file should use form of "`exec some-window/session-manager`" to start your favorite X window/session managers.

If this feature is used, the selection of the display (or login) manager (DM), session manager or window manager (WM) by the system utility is ignored.

### Customizing the X session (new method)

Here are new methods to customize the X session without completely overriding the system code as above.

- The display manager `gdm3` can select a specific session and set it as the argument of "`/etc/X11/Xsession`".

  - "`/etc/profile`", "`~/.profile`", "`/etc/xprofile`", and "`~/.xprofile`" files are executed as a part of `gdm3` start up process.

- The "`~/.xsessionrc`" file is executed as a part of start up process. (desktop independent)

  - "`#allow-user-xsession`" in "`/etc/X11/Xsession.options`" does not restrict execution of the "`~/.xsessionrc`" file.

- The "`~/.gnomerc`" file is executed as a part of start up process. (GNOME desktop only)

The selection of the display (or login) manager (DM), session manager or window manager (WM) by the system utility is respected.

These configuration files should not have "`exec …`" nor "`exit`" in them.

### Connecting a remote X client via SSH

The use of "`ssh -X`" enables a secure connection from a local X server to a remote application server.

Set "`X11Forwarding`" entries to "`yes`" in "`/etc/ssh/sshd_config`" of the remote host, if you want to avoid "`-X`" command-line option.

Start the X server on the local host.

Open an `xterm` in the local host.

Run `ssh(1)` to establish a connection with the remote site as the following.

    localname @ localhost $ ssh -q -X loginname@remotehost.domain
    Password:

Run an X application command, e.g. "`gimp`", on the remote site as the following.

    loginname @ remotehost $ gimp &

This method can display the output from a remote X client as if it were locally connected through a local UNIX domain socket.

### Secure X terminal via the Internet

Secure X terminal via the Internet, which displays remotely run entire X desktop environment, can easily achieved by using specialized package such as `ldm`. Your local machine becomes a secure thin client to the remote application server connected via SSH.

## Fonts in the X Window

[Fontconfig 2.0](https://en.wikipedia.org/wiki/Fontconfig) was created to provide a distribution independent library for configuring and customizing font access in 2002. Debian after `squeeze` uses [Fontconfig 2.0](https://en.wikipedia.org/wiki/Fontconfig) for its font configuration.

Font supports on X Window System can be summarized as follows.

- Legacy X server side font support system

  - The original core X11 font system provides backward compatibility for older version of X client applications.

  - The original core X11 fonts are installed on the X server.

- Modern X client side font support system

  - The modern X system supports all fonts listed below ([Basic fonts](#_basic_fonts), [Additional fonts](#_additional_fonts), and [CJK fonts](#_cjk_fonts)) with advanced features such as anti-aliasing.

  - [Xft](https://en.wikipedia.org/wiki/Xft) 2.0 connects modern X applications such as ones from [GNOME](https://en.wikipedia.org/wiki/GNOME), [KDE](https://en.wikipedia.org/wiki/KDE), and [LibreOffice](https://en.wikipedia.org/wiki/LibreOffice) with [FreeType](http://freetype.sourceforge.net/index.html) 2.0 library.

  - [FreeType](http://freetype.sourceforge.net/index.html) 2.0 provides font rasterization library.

  - [Fontconfig](https://en.wikipedia.org/wiki/Fontconfig) provides resolution of the font specification for [Xft](https://en.wikipedia.org/wiki/Xft) 2.0. See `fonts.conf(5)` for its configuration.

  - All modern X applications using [Xft](https://en.wikipedia.org/wiki/Xft) 2.0 can talk to modern X server using the [X Rendering Extension](https://en.wikipedia.org/wiki/XRender).

  - The [X Rendering Extension](https://en.wikipedia.org/wiki/XRender) moves font access and glyph image generation from the X server to the X client.

| package | popcon | size | description |
|:---|:---|:---|:---|
| `xfonts-utils` | @-@popcon1@-@ | @-@psize1@-@ | X Window System font utility programs |
| `libxft2` | @-@popcon1@-@ | @-@psize1@-@ | Xft, a library that connects X applications with the FreeType font rasterization library |
| `libfreetype6` | @-@popcon1@-@ | @-@psize1@-@ | [FreeType](http://freetype.sourceforge.net/index.html) 2.0 font rasterization library |
| `fontconfig` | @-@popcon1@-@ | @-@psize1@-@ | [Fontconfig](https://en.wikipedia.org/wiki/Fontconfig), a generic font configuration library — support binaries |
| `fontconfig-config` | @-@popcon1@-@ | @-@psize1@-@ | [Fontconfig](https://en.wikipedia.org/wiki/Fontconfig), a generic font configuration library — configuration data |

Table of packages to support X Window font systems

You can check font configuration information by the following.

- "`xset q`" for core X11 font path

- "`fc-match`" for fontconfig font default

- "`fc-list`" for available fontconfig fonts

> [!TIP]
> "[The Penguin and Unicode](http://unifont.org/iuc27/html/ICUPresentation.html)" is a good overview of modern X Window System. Other documentations at <http://unifont.org/> should provide good information on Unicode fonts, Unicode-enabled software, internationalization, and Unicode usability issues on [free/libre/open source (FLOSS)](https://en.wikipedia.org/wiki/Free_and_open_source_software) operating systems.

### Basic fonts

There are 2 major types of [computer fonts](https://en.wikipedia.org/wiki/Computer_font).

- Bitmap fonts (good for low resolution rasterization)

- Outline/stroke fonts (good for high resolution rasterization)

While scaling of bitmap fonts causes jugged image, scaling of outline/stroke fonts produces smooth image.

Bitmap fonts on the Debian system are usually provided by compressed [X11 pcf bitmap font files](http://fontforge.sourceforge.net/pcf-format.html) having their file extension "`.pcf.gz`".

Outline fonts on the Debian system are provided by the following.

- [PostScript](https://en.wikipedia.org/wiki/PostScript) Type 1 font files having their file extension "`.pfb`" (binary font file) and "`.afm`" (font metrics file).

- [TrueType](https://en.wikipedia.org/wiki/TrueType) (or [OpenType](https://en.wikipedia.org/wiki/OpenType)) font files usually having their file extension "`.ttf`".

> [!TIP]
> [OpenType](https://en.wikipedia.org/wiki/OpenType) is intended to supersede both [TrueType](https://en.wikipedia.org/wiki/TrueType) and [PostScript](https://en.wikipedia.org/wiki/PostScript) Type 1.

| font package | popcon | size | sans-serif font | serif font | monospace font | source of font |
|:---|:---|:---|:---|:---|:---|:---|
| PostScript | N/A | N/A | [Helvetica](https://en.wikipedia.org/wiki/Helvetica) | [Times](https://en.wikipedia.org/wiki/Times_New_Roman) | [Courier](https://en.wikipedia.org/wiki/Courier_(typeface)) | Adobe |
| gsfonts | @-@popcon1@-@ | @-@psize1@-@ | Nimbus Sans L | Nimbus Roman No9 L | Nimbus Mono L | [URW](http://www.math.utah.edu/~beebe/fonts/urw.html) (Adobe compatible size) |
| gsfonts-x11 | @-@popcon1@-@ | @-@psize1@-@ | Nimbus Sans L | Nimbus Roman No9 L | Nimbus Mono L | X font support with PostScript Type 1 fonts. |
| t1-cyrillic | @-@popcon1@-@ | @-@psize1@-@ | Free Helvetian | Free Times | Free Courier | URW extended (Adobe compatible size) |
| lmodern | @-@popcon1@-@ | @-@psize1@-@ | LMSans\* | LMRoman\* | LMTypewriter\* | scalable PostScript and OpenType fonts based on Computer Modern (from TeX) |

Table of corresponding [PostScript](https://en.wikipedia.org/wiki/PostScript) Type 1 fonts

| font package | popcon | size | sans-serif font | serif font | monospace font | source of font |
|:---|:---|:---|:---|:---|:---|:---|
| ttf-mscorefonts-installer | @-@popcon1@-@ | @-@psize1@-@ | [Arial](https://en.wikipedia.org/wiki/Arial) | [Times New Roman](https://en.wikipedia.org/wiki/Times_New_Roman) | [Courier New](https://en.wikipedia.org/wiki/Courier_(typeface)) | Microsoft (Adobe compatible size) (This installs non-free data) |
| fonts-liberation | @-@popcon1@-@ | @-@psize1@-@ | Liberation Sans | Liberation Serif | Liberation Mono | [Liberation Fonts project](https://en.wikipedia.org/wiki/Liberation_fonts) (Microsoft compatible size) |
| fonts-freefont-ttf | @-@popcon1@-@ | @-@psize1@-@ | FreeSans | FreeSerif | FreeMono | [GNU freefont](http://savannah.gnu.org/projects/freefont/) (Microsoft compatible size) |
| fonts-dejavu | @-@popcon1@-@ | @-@psize1@-@ | DejaVu Sans | DejaVu Serif | DejaVu Sans Mono | [DejaVu](http://dejavu-fonts.org), [Bitstream Vera](http://www.gnome.org/fonts/) with Unicode coverage |
| fonts-dejavu-core | @-@popcon1@-@ | @-@psize1@-@ | DejaVu Sans | DejaVu Serif | DejaVu Sans Mono | [DejaVu](http://dejavu-fonts.org), [Bitstream Vera](http://www.gnome.org/fonts/) with Unicode coverage (sans, sans-bold, serif, serif-bold, mono, mono-bold) |
| fonts-dejavu-extra | @-@popcon1@-@ | @-@psize1@-@ | N/A | N/A | N/A | [DejaVu](http://dejavu-fonts.org), [Bitstream Vera](http://www.gnome.org/fonts/) with Unicode coverage (oblique, italic, bold-oblique, bold-italic, condensed) |
| ttf-unifont | @-@popcon1@-@ | @-@psize1@-@ | N/A | N/A | unifont | [GNU Unifont](http://Unifoundry.com), with all printable character code in Unicode 5.1 Basic Multilingual Plane (BMP) |

Table of corresponding [TrueType](https://en.wikipedia.org/wiki/TrueType) fonts

> [!TIP]
> [DejaVu](http://dejavu-fonts.org) fonts are based on and superset of [Bitstream Vera](http://www.gnome.org/fonts/) fonts.

### Additional fonts

`aptitude(8)` helps you find additional fonts easily.

- The short package list under "Tasks" → "Localization"

- The filtered flat package list of font data with regex on debtag: "`~Gmade-of::data:font`"

- The filtered flat package list of the BDF (bitmap) font packages with regex on package name: "`~nxfonts-`"

- The filtered flat package list of the TrueType (outline) font packages with regex on package name: "`~nttf-|~nfonts-`"

Since **Free** fonts are sometimes limited, installing or sharing some commercial TrueType fonts is an option for a Debian users. In order to make this process easy for the user, some convenience packages have been created.

- `mathematica-fonts`

- `fonts-mscorefonts-installer`

You'll have a really good selection of TrueType fonts at the expense of contaminating your **Free** system with non-Free fonts.

### CJK fonts

Here are some key points focused on fonts of [CJK characters](https://en.wikipedia.org/wiki/CJK_characters).

| font type  | Japanese font name | Chinese font name | Korean font name     |
|:-----------|:-------------------|:------------------|:---------------------|
| sans-serif | gothic, ゴチック   | hei, gothic       | dodum, gulim, gothic |
| serif      | mincho, 明朝       | song, ming        | batang               |

Table of key words used in CJK font names to indicate font types

Font name such as "VL PGothic" with "P" is a proportional font which corresponds to the fixed width "VL Gothic" font.

For example, [Shift_JIS](https://en.wikipedia.org/wiki/Shift_JIS) code table comprises 7070 characters. They can be grouped as the following.

- JIS X 0201 single-byte characters (191 characters, a.k.a. half-width characters)

- JIS X 0208 double-byte characters (6879 characters, a.k.a. full-width characters)

Double-byte characters occupy double width on console terminals which uses CJK fixed width fonts. In order to cope with such situation, [Hanzi Bitmap Font (HBF) File](http://www.ibiblio.org/pub/packages/ccic/software/info/HBF-1.1/) with file extension "`.hbf`" may be deployed for fonts containing single-byte and double-byte characters.

In order to save space for [TrueType](https://en.wikipedia.org/wiki/TrueType) font files, [TrueType](https://en.wikipedia.org/wiki/TrueType) font collection file with file extension "`.ttc`" may be used.

In order to cover complicated code space of characters, CID keyed [PostScript](https://en.wikipedia.org/wiki/PostScript) Type 1 font is used with CMap files starting themselves with "`%!PS-Adobe-3.0 Resource-CMap`". This is rarely used for normal X display but used for PDF rendering etc. (see [X utility applications](#_x_utility_applications)).

> [!TIP]
> The multiple [glyphs](https://en.wikipedia.org/wiki/Glyph) are expected for some [Unicode](https://en.wikipedia.org/wiki/Unicode) code points due to [Han unification](https://en.wikipedia.org/wiki/Han_unification). One of the most annoying ones are "U+3001 IDEOGRAPHIC COMMA" and "U+3002 IDEOGRAPHIC FULL STOP" whose character positions differ among CJK countries. Configuring priority of Japanese centric fonts over Chinese ones using "`~/.fonts.conf`" should give peace of minds to Japanese.

## X applications

### X office applications

Here is a list of basic office applications (LO is LibreOffice).

| package | popcon | package size | type | description |
|:---|:---|:---|:---|:---|
| `libreoffice-writer` | @-@popcon1@-@ | @-@psize1@-@ | LO | word processor |
| `libreoffice-calc` | @-@popcon1@-@ | @-@psize1@-@ | LO | spreadsheet |
| `libreoffice-impress` | @-@popcon1@-@ | @-@psize1@-@ | LO | presentation |
| `libreoffice-base` | @-@popcon1@-@ | @-@psize1@-@ | LO | database management |
| `libreoffice-draw` | @-@popcon1@-@ | @-@psize1@-@ | LO | vector graphics editor (draw) |
| `libreoffice-math` | @-@popcon1@-@ | @-@psize1@-@ | LO | mathematical equation/formula editor |
| `abiword` | @-@popcon1@-@ | @-@psize1@-@ | GNOME | word processor |
| `gnumeric` | @-@popcon1@-@ | @-@psize1@-@ | GNOME | spreadsheet |
| `gimp` | @-@popcon1@-@ | @-@psize1@-@ | GTK | bitmap graphics editor (paint) |
| `inkscape` | @-@popcon1@-@ | @-@psize1@-@ | GNOME | vector graphics editor (draw) |
| `dia` | @-@popcon1@-@ | @-@psize1@-@ | GTK | flowchart and diagram editor |
| `planner` | @-@popcon1@-@ | @-@psize1@-@ | GNOME | project management |
| `calligrawords` | @-@popcon1@-@ | @-@psize1@-@ | KDE | word processor |
| `calligrasheets` | @-@popcon1@-@ | @-@psize1@-@ | KDE | spreadsheet |
| `calligrastage` | @-@popcon1@-@ | @-@psize1@-@ | KDE | presentation |
| `calligraplan` | @-@popcon1@-@ | @-@psize1@-@ | KDE | project management |
| `kexi` | @-@popcon1@-@ | @-@psize1@-@ | KDE | database management |
| `karbon` | @-@popcon1@-@ | @-@psize1@-@ | KDE | vector graphics editor (draw) |

List of basic X office applications

### X utility applications

Here is a list of basic utility applications which caught my eyes.

| package | popcon | package size | type | description |
|:---|:---|:---|:---|:---|
| `evince` | @-@popcon1@-@ | @-@psize1@-@ | GNOME | document(pdf) viewer |
| `okular` | @-@popcon1@-@ | @-@psize1@-@ | KDE | document(pdf) viewer |
| `calibre` | @-@popcon1@-@ | @-@psize1@-@ | KDE | e-book converter and library management |
| `fbreader` | @-@popcon1@-@ | @-@psize1@-@ | GTK | e-book reader |
| `evolution` | @-@popcon1@-@ | @-@psize1@-@ | GNOME | Personal information Management (groupware and email) |
| `kontact` | @-@popcon1@-@ | @-@psize1@-@ | KDE | Personal information Management (groupware and email) |
| `scribus` | @-@popcon1@-@ | @-@psize1@-@ | KDE | desktop page layout editor |
| `glabels` | @-@popcon1@-@ | @-@psize1@-@ | GNOME | label editor |
| `gnucash` | @-@popcon1@-@ | @-@psize1@-@ | GNOME | personal accounting |
| `homebank` | @-@popcon1@-@ | @-@psize1@-@ | GTK | personal accounting |
| `kmymoney` | @-@popcon1@-@ | @-@psize1@-@ | KDE | personal accounting |
| `shotwell` | @-@popcon1@-@ | @-@psize1@-@ | GTK | digital photo organizer |
| `xsane` | @-@popcon1@-@ | @-@psize1@-@ | GTK | scanner frontend |

List of basic X utility applications

> [!CAUTION]
> The `poppler-data` package (previously non-free, see [???](#_ghostscript)) needs to be installed for `evince` and `okular` to display CJK PDF documents using Cmap data ([CJK fonts](#_cjk_fonts)).

> [!NOTE]
> Installing softwares such as `scribus` (KDE) on GNOME desktop environment are quite acceptable since corresponding functionality is not available under GNOME desktop environment. But installing too many packages with duplicated functionalities clutter your menu.

## The X trivia

### Clipboard

The X selection using 3 mouse buttons is the native clipboard feature of X (see [???](#_unix_style_mouse_operations)).

> [!TIP]
> Shift-Insert can work as the equivalent of the middle-mouse-button click.

| package | popcon | package size | type | description |
|:---|:---|:---|:---|:---|
| `xsel` | @-@popcon1@-@ | @-@psize1@-@ | X | command line interface to X selections |
| `xclip` | @-@popcon1@-@ | @-@psize1@-@ | X | command line interface to X selections |

List of basic X selection programs

The modern Desktop Environments (GNOME, KDE, …) offer different clipboard system for the cut, copy, and paste using the left mouse button and keys (CTRL-X, CRTL-C, and CTRL-V).

### Keymaps and pointer button mappings in X

`xmodmap(1)` is a utility for modifying keymaps and pointer button mappings in the X Window System. To get the **keycode**, run `xev(1)` in the X and press keys. To get the meaning of **keysym**, look into the MACRO definition in "`/usr/include/X11/keysymdef.h`" file (`x11proto-core-dev` package). All "`#define`" statements in this file are named as "`XK_`" prepended to **keysym** names.

### Classic X clients

Most traditional X client programs, such as `xterm(1)`, can be started with a set of standard command line options to specify geometry, font, and display.

They also use the X resource database to configure their appearance. The system-wide defaults of X resources are stored in "`/etc/X11/Xresources/*`" and application defaults of them are stored in "`/etc/X11/app-defaults/*`". Use these settings as the starting points.

The "`~/.Xresources`" file is used to store user resource specifications. This file is automatically merged into the default X resources upon login. To make changes to these settings and make them effective immediately, merge them into the database using the following command.

    $ xrdb -merge ~/.Xresources

See `x(7)` and `xrdb(1)`.

### The X terminal emulator — xterm

Learn everything about `xterm(1)` at <http://dickey.his.com/xterm/xterm.faq.html>.

### Running X clients as root

> [!WARNING]
> Never start the X display/session manager under the root account by typing in `root` to the prompt of the display manager such as `gdm3` because it is considered unsafe (insecure), even when you plan to perform administrative activities. The entire X architecture is considered insecure if run as root. You must always use the lowest privilege level possible, like a regular user account.

Easy ways to run a particular X client, e.g. "`foo`" as root is to use `sudo(8)` etc. as the following.

    $ sudo foo &

    $ sudo -s
    # foo &

    $ ssh -X root@localhost
    # foo &

> [!CAUTION]
> Use of `ssh(1)` just for this purpose as above is waste of resource.

In order for the X client to connect to the X server, please note the following.

- Values of the old user's "`$XAUTHORITY`" and "`$DISPLAY`" environment variables must be copied to the new user's ones.

- The file pointed by value of the "`$XAUTHORITY`" environment variable must be readable by the new user.
