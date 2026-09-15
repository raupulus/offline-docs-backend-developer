---
title: Appendix
source_url: https://www.debian.org/doc/manuals/debian-reference/_appendix
source_repo: https://salsa.debian.org/debian/debian-reference.git
source_ref: master
source_commit: b7239e647
source_path: 90_appendix.rawxml
technology: debian
version: 12 (Bookworm)
license: GPL-2.0-or-later
retrieved_at: '2026-09-15'
order: 140
---

## Appendix

Here are backgrounds of this document.

## The Debian maze

The Linux system is a very powerful computing platform for a networked computer. However, learning how to use all its capabilities is not easy. Setting up the LPR printer queue with a non-PostScript printer was a good example of stumble points. (There are no issues anymore since newer installations use the new CUPS system.)

There is a complete, detailed map called the "SOURCE CODE". This is very accurate but very hard to understand. There are also references called HOWTO and mini-HOWTO. They are easier to understand but tend to give too much detail and lose the big picture. I sometimes have a problem finding the right section in a long HOWTO when I need a few commands to invoke.

I hope this "Debian Reference (version @-@dr-version@-@)" (@-@build-date@-@) provides a good starting direction for people in the Debian maze.

## Copyright history

The Debian Reference was initiated by me, Osamu Aoki \<osamu at debian dot org\>, as a personal system administration memo. Many contents came from the knowledge I gained from [the debian-user mailing list](http://lists.debian.org/debian-user/) and other Debian resources.

Following a suggestion from Josip Rodin, who was very active with the [Debian Documentation Project (DDP)](https://www.debian.org/doc/ddp), "Debian Reference (version 1, 2001-2007)" was created as a part of DDP documents.

After 6 years, I realized that the original "Debian Reference (version 1)" was outdated and started to rewrite many contents. New "Debian Reference (version 2)" is released in 2008.

The tutorial contents can trace its origin and its inspiration in followings.

- "[Linux User's Guide](http://www.ibiblio.org/pub/Linux/docs/linux-doc-project/users-guide/user-beta-1.pdf.gz)" by Larry Greenfield (December 1996)

  - obsoleted by "Debian Tutorial"

- "[Debian Tutorial](https://www.debian.org/doc/manuals/debian-tutorial/)" by Havoc Pennington. (11 December, 1998)

  - partially written by Oliver Elphick, Ole Tetlie, James Treacy, Craig Sawyer, and Ivan E. Moore II

  - obsoleted by "Debian GNU/Linux: Guide to Installation and Usage"

- "[Debian GNU/Linux: Guide to Installation and Usage](http://archive.debian.net/woody/debian-guide)" by John Goerzen and Ossama Othman (1999)

  - obsoleted by "Debian Reference (version 1)"

The package and archive description can trace some of their origin and their inspiration in following.

- "[Debian FAQ](https://www.debian.org/doc/manuals/debian-faq/)" (March 2002 version, when this was maintained by Josip Rodin)

The other contents can trace some of their origin and their inspiration in following.

- "[Debian Reference](http://packages.debian.org/search?keywords=debian-reference&searchon=sourcenames&exact=1&suite=all&section=all) (version 1)" by Osamu Aoki (2001–2007)

  - obsoleted by the newer "Debian Reference (version 2)" in 2008.

The previous "Debian Reference (version 1)" was created with many contributors.

- the major contents contribution on network configuration topics by Thomas Hood

- significant contents contribution on X and VCS related topics by Brian Nelson

- the help on the build scripts and many content corrections by Jens Seidel

- extensive proofreading by David Sewell

- many contributions by the translators, contributors, and bug reporters

Many manual pages and info pages on the Debian system were used as the primary references to write this document. To the extent Osamu Aoki considered within the [fair use](https://en.wikipedia.org/wiki/Fair_use), many parts of them, especially command definitions, were used as phrase pieces after careful editorial efforts to fit them into the style and the objective of this document.

The gdb debugger description was expanded using [Debian wiki contents on backtrace](http://wiki.debian.org/HowToGetABacktrace) with consent by Ari Pollak, Loïc Minier, and Dafydd Harries.

Contents of the current "Debian Reference (version @-@dr-version@-@)" (@-@build-date@-@) are mostly my own work except as mentioned above. These has been updated by the contributors too.

The author, Osamu Aoki, thanks all those who helped make this document possible.

## Document format

The source of the English original document is currently written in [AsciiDoc](http://packages.debian.org/search?keywords=asciidoc) text files. [AsciiDoc](http://packages.debian.org/search?keywords=asciidoc) is used as convenience only since it is less typing than straight XML and supports table in the very intuitive format. You should think XML and PO files as real source files. Via build script, it is converted to DocBook XML format and automatically generated data are inserted to form a final Docbook XML source. This final Docbook XML source can be converted to HTML, epub, plain text, PostScript, and PDF. (Some formats may be skipped for distribution.)
