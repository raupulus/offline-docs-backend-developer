---
title: Preface
source_url: https://www.debian.org/doc/manuals/debian-reference/_preface
source_repo: https://salsa.debian.org/debian/debian-reference.git
source_ref: master
source_commit: b7239e647
source_path: 00_preface.rawxml
technology: debian
version: 12 (Bookworm)
license: GPL-2.0-or-later
retrieved_at: '2026-09-15'
order: 10
---

## Preface

This [Debian Reference (version @-@dr-version@-@)](https://www.debian.org/doc/manuals/debian-reference/) (@-@build-date@-@) is intended to provide a broad overview of the Debian system administration as a post-installation user guide.

The target reader is someone who is willing to learn shell scripts but who is not ready to read all the C sources to figure out how the [GNU](https://en.wikipedia.org/wiki/GNU)/[Linux](https://en.wikipedia.org/wiki/Linux) system works.

For installation instructions, see:

- [Debian GNU/Linux Installation Guide for current stable system](https://www.debian.org/releases/stable/installmanual)

- [Debian GNU/Linux Installation Guide for current testing system](https://www.debian.org/releases/testing/installmanual)

## Disclaimer

All warranties are disclaimed. All trademarks are property of their respective trademark owners.

The Debian system itself is a moving target. This makes its documentation difficult to be current and correct. Although the current unstable version of the Debian system was used as the basis for writing this, some contents may be already outdated by the time you read this.

Please treat this document as the secondary reference. This document does not replace any authoritative guides. The author and contributors do not take responsibility for consequences of errors, omissions or ambiguity in this document.

## What is Debian

The [Debian Project](https://www.debian.org) is an association of individuals who have made common cause to create a free operating system. It's distribution is characterized by the following.

- Commitment to the software freedom: [Debian Social Contract and Debian Free Software Guidelines (DFSG)](https://www.debian.org/social_contract)

- Internet based distributed unpaid volunteer effort: <https://www.debian.org>

- Large number of pre-compiled high quality software packages

- Focus on stability and security with easy access to the security updates

- Focus on smooth upgrade to the latest software packages in the `unstable` and `testing` archives

- Large number of supported hardware architectures

Free Software pieces in Debian come from [GNU](https://en.wikipedia.org/wiki/GNU), [Linux](https://en.wikipedia.org/wiki/Linux), [BSD](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution), [X](https://en.wikipedia.org/wiki/X_Window_System), [ISC](https://en.wikipedia.org/wiki/Internet_Systems_Consortium), [Apache](https://en.wikipedia.org/wiki/Apache_Software_Foundation), [Ghostscript](https://en.wikipedia.org/wiki/Ghostscript), [Common Unix Printing System ](https://en.wikipedia.org/wiki/Common_Unix_Printing_System), [Samba](https://en.wikipedia.org/wiki/Samba_(software)), [GNOME](https://en.wikipedia.org/wiki/GNOME), [KDE](https://en.wikipedia.org/wiki/KDE), [Mozilla](https://en.wikipedia.org/wiki/Mozilla), [LibreOffice](https://en.wikipedia.org/wiki/LibreOffice), [Vim](https://en.wikipedia.org/wiki/Vim_(text_editor)), [TeX](https://en.wikipedia.org/wiki/TeX), [LaTeX](https://en.wikipedia.org/wiki/LaTeX), [DocBook](https://en.wikipedia.org/wiki/DocBook), [Perl](https://en.wikipedia.org/wiki/Perl), [Python](https://en.wikipedia.org/wiki/Python_(programming_language)), [Tcl](https://en.wikipedia.org/wiki/Tcl), [Java](https://en.wikipedia.org/wiki/Java_(programming_language)), [Ruby](https://en.wikipedia.org/wiki/Ruby_(programming_language)), [PHP](https://en.wikipedia.org/wiki/PHP), [Berkeley DB](https://en.wikipedia.org/wiki/Berkeley_DB), [MariaDB](https://en.wikipedia.org/wiki/MariaDB), [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL), [SQLite](https://en.wikipedia.org/wiki/Sqlite), [Exim](https://en.wikipedia.org/wiki/Exim), [Postfix](https://en.wikipedia.org/wiki/Postfix_(software)), [Mutt](https://en.wikipedia.org/wiki/Mutt_(e-mail_client)), [FreeBSD](https://en.wikipedia.org/wiki/FreeBSD), [OpenBSD](https://en.wikipedia.org/wiki/OpenBSD), [Plan 9](https://en.wikipedia.org/wiki/Plan_9_from_Bell_Labs) and many more independent free software projects. Debian integrates this diversity of Free Software into one system.

## About this document

## Guiding rules

Following guiding rules are followed while compiling this document.

- Provide overview and skip corner cases. (**Big Picture**)

- Keep It Short and Simple. (**KISS**)

- Do not reinvent the wheel. (Use pointers to **the existing references**)

- Focus on non-GUI tools and consoles. (Use **shell examples**)

- Be objective. (Use [popcon](http://popcon.debian.org/) etc.)

> [!TIP]
> I tried to elucidate hierarchical aspects and lower levels of the system.

## Prerequisites

> [!WARNING]
> You are expected to make good efforts to seek answers by yourself beyond this documentation. This document only gives efficient starting points.

You must seek solution by yourself from primary sources.

- [The Debian Administrator's Handbook](https://www.debian.org/doc/manuals/debian-handbook/)

- The Debian site at <https://www.debian.org> for the general information

- The documentation under the "`/usr/share/doc/<package_name>`" directory

- The Unix style **manpage**: "`dpkg -L <package_name> |grep '/man/man.*/'`"

- The GNU style **info page**: "`dpkg -L <package_name> |grep '/info/'`"

- The bug report: [http://bugs.debian.org/\<package_name\>](https://bugs.debian.org/)

- The Debian Wiki at <https://wiki.debian.org/> for the moving and specific topics

- The HOWTOs from The Linux Documentation Project (TLDP) at <http://tldp.org/>

- The Single UNIX Specification from the Open Group's The UNIX System Home Page at <http://www.unix.org/>

- The free encyclopedia from Wikipedia at <https://www.wikipedia.org/>

> [!NOTE]
> For detailed documentation, you may need to install the corresponding documentation package named with "`-doc`" as its suffix.

## Conventions

This document provides information through the following simplified presentation style with `bash(1)` shell command examples.

    # <command in root account>
    $ <command in user account>

These shell prompts distinguish account used and correspond to set environment variables as: "`PS1='\$'`" and "`PS2=' '`". These values are chosen for the sake of readability of this document and are not typical on actual installed system.

> [!NOTE]
> See the meaning of the "`$PS1`" and "`$PS2`" environment variables in `bash(1)`.

**Action** required by the system administrator is written in the imperative sentence, e.g. "Type Enter-key after typing each command string to the shell."

The **description** column and similar ones in the table may contain a **noun phrase** following [the package short description convention](https://www.debian.org/doc/manuals/developers-reference/best-pkging-practices#bpp-desc-basics) which drops leading articles such as "a" and "the". They may alternatively contain an infinitive phrase as a **noun phrase** without leading "to" following the short command description convention in manpages. These may look funny to some people but are my intentional choices of style to keep this documentation as simple as possible. These **Noun phrases** do not capitalize their starting nor end with periods following these short description convention.

> [!NOTE]
> Proper nouns including command names keeps their case irrespective of their location.

A **command snippet** quoted in a text paragraph is referred by the typewriter font between double quotation marks, such as "`aptitude safe-upgrade`".

A **text data** from a configuration file quoted in a text paragraph is referred by the typewriter font between double quotation marks, such as "`deb-src`".

A **command** is referred by its name in the typewriter font optionally followed by its manpage section number in parenthesis, such as `bash(1)`. You are encouraged to obtain information by typing the following.

    $ man 1 bash

A **manpage** is referred by its name in the typewriter font followed by its manpage section number in parenthesis, such as `sources.list(5)`. You are encouraged to obtain information by typing the following.

    $ man 5 sources.list

An **info page** is referred by its command snippet in the typewriter font between double quotation marks, such as "`info make`". You are encouraged to obtain information by typing the following.

    $ info make

A **filename** is referred by the typewriter font between double quotation marks, such as "`/etc/passwd`". For configuration files, you are encouraged to obtain information by typing the following.

    $ sensible-pager "/etc/passwd"

A **directory name** is referred by the typewriter font between double quotation marks, such as "`/etc/apt/`". You are encouraged to explore its contents by typing the following.

    $ mc "/etc/apt/"

A **package name** is referred by its name in the typewriter font, such as `vim`. You are encouraged to obtain information by typing the following.

    $ dpkg -L vim
    $ apt-cache show vim
    $ aptitude show vim

A **documentation** may indicate its location by the filename in the typewriter font between double quotation marks, such as "`/usr/share/doc/base-passwd/users-and-groups.txt.gz`" and "`/usr/share/doc/base-passwd/users-and-groups.html`"; or by its [URL](https://en.wikipedia.org/wiki/Uniform_Resource_Locator), such as <https://www.debian.org>. You are encouraged to read the documentation by typing the following.

    $ zcat "/usr/share/doc/base-passwd/users-and-groups.txt.gz" | sensible-pager
    $ sensible-browser "/usr/share/doc/base-passwd/users-and-groups.html"
    $ sensible-browser "https://www.debian.org"

An **environment variable** is referred by its name with leading "`$`" in the typewriter font between double quotation marks, such as "`$TERM`". You are encouraged to obtain its current value by typing the following.

    $ echo "$TERM"

## The popcon

The [popcon](http://popcon.debian.org/) data is presented as the objective measure for the popularity of each package. It was downloaded on @-@pop-date@-@ and contains the total submission of @-@pop-submissions@-@ reports over @-@pop-packages@-@ binary packages and @-@pop-architectures@-@ architectures.

> [!NOTE]
> Please note that the `@-@arch@-@` `unstable` archive contains only @-@all-packages@-@ packages currently. The popcon data contains reports from many old system installations.

The popcon number preceded with "V:" for "votes" is calculated by "1000 \* (the popcon submissions for the package executed recently on the PC)/(the total popcon submissions)".

The popcon number preceded with "I:" for "installs" is calculated by "1000 \* (the popcon submissions for the package installed on the PC)/(the total popcon submissions)".

> [!NOTE]
> The popcon figures should not be considered as absolute measures of the importance of packages. There are many factors which can skew statistics. For example, some system participating popcon may have mounted directories such as "`/bin`" with "`noatime`" option for system performance improvement and effectively disabled "vote" from such system.

## The package size

The package size data is also presented as the objective measure for each package. It is based on the "`Installed-Size:`" reported by "`apt-cache show`" or "`aptitude show`" command (currently on `@-@arch@-@` architecture for the `unstable` release). The reported size is in KiB ([Kibibyte](https://en.wikipedia.org/wiki/Kibibyte) = unit for 1024 bytes).

> [!NOTE]
> A package with a small numerical package size may indicate that the package in the `unstable` release is a dummy package which installs other packages with significant contents by the dependency. The dummy package enables a smooth transition or split of the package.

> [!NOTE]
> A package size followed by "(\*)" indicates that the package in the `unstable` release is missing and the package size for the `experimental` release is used instead.

## Bug reports on this document

Please file bug reports on the `debian-reference` package using `reportbug(1)` if you find any issues on this document. Please include correction suggestion by "`diff -u`" to the plain text version or to the source.

## Reminders for new users

Here are some reminders for new users:

- Backup your data

- Secure your password and security keys

- [KISS (keep it simple stupid)](https://en.wikipedia.org/wiki/KISS_principle)

  - Don't over-engineer your system

- Read your log files

  - The **FIRST** error is the one that counts

- [RTFM (read the fine manual)](https://en.wikipedia.org/wiki/RTFM)

- Search the Internet before asking questions

- Don't be root when you don't have to be

- Don't mess with the package management system

- Don't type anything you don't understand

- Don't change the file permissions (before the full security review)

- Don't leave your root shell until you **TEST** your changes

- Always have an alternative boot media (USB memory stick, CD, …)

## Some quotes for new users

Here are some interesting quotes from the Debian mailing list which may help enlighten new users.

- "This is Unix. It gives you enough rope to hang yourself." --- Miquel van Smoorenburg `<miquels at cistron.nl>`

- "Unix IS user friendly… It's just selective about who its friends are." --- Tollef Fog Heen `<tollef at add.no>`

Wikipedia has article "[Unix philosophy](https://en.wikipedia.org/wiki/Unix_philosophy)" which lists interesting quotes.
