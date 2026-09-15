---
title: Features Of SQLite
source_url: https://www.sqlite.org/features.html
source_path: features.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 2840
---

# Features Of SQLite

- [Transactions](transactional.md) are atomic, consistent, isolated, and durable (ACID) even after system crashes and power failures.
- [Zero-configuration](zeroconf.md) - no setup or administration needed.
- [Full-featured SQL](fullsql.md) implementation with advanced capabilities like [partial indexes](partialindex.md), [indexes on expressions](expridx.md), [JSON](json1.md), [common table expressions](lang_with.md), and [window functions](windowfunctions.md). ([Omitted features](omitted.md))
- A complete database is stored in a [single cross-platform disk file](onefile.md). Great for use as an [application file format](appfileformat.md).
- Supports terabyte-sized databases and gigabyte-sized strings and blobs. (See [limits.html](limits.md).)
- Small code [footprint](footprint.md): less than 900KiB fully configured or much less with optional features omitted.
- Simple, easy to use [API](cintro.md).
- Fast: In some cases, SQLite is [faster than direct filesystem I/O](fasterthanfs.md)
- Written in ANSI-C. [TCL bindings](tclsqlite.md) included. Bindings for dozens of other languages available separately.
- Well-commented source code with [100% branch test coverage](testing.md#coverage).
- Available as a [single ANSI-C source-code file](amalgamation.md) that is [easy to compile](howtocompile.md) and hence is easy to add into a larger project.
- [Self-contained](selfcontained.md): no external dependencies.
- Cross-platform: Android, \*BSD, iOS, Linux, Mac, Solaris, VxWorks, and Windows (Win32, WinCE, WinRT) are supported out of the box. Easy to port to other systems.
- Sources are in the [public domain](copyright.md). Use for any purpose.
- Comes with a standalone [command-line interface](cli.md) (CLI) client that can be used to administer SQLite databases.

## Suggested Uses For SQLite:

- **Database For The Internet Of Things.** SQLite is a popular choice for the database engine in cellphones, PDAs, MP3 players, set-top boxes, and other electronic gadgets. SQLite has a small code footprint, makes efficient use of memory, disk space, and disk bandwidth, is highly reliable, and requires no maintenance from a Database Administrator.

- **Application File Format.** Rather than using fopen() to write XML, JSON, CSV, or some proprietary format into disk files used by your application, use an SQLite database. You'll avoid having to write and troubleshoot a parser, your data will be more easily accessible and cross-platform, and your updates will be transactional. ([more...](appfileformat.md))

- **Website Database.** Because it requires no configuration and stores information in ordinary disk files, SQLite is a popular choice as the database to back small to medium-sized websites.

- **Stand-in For An Enterprise RDBMS.** SQLite is often used as a surrogate for an enterprise RDBMS for demonstration purposes or for testing. SQLite is fast and requires no setup, which takes a lot of the hassle out of testing and which makes demos perky and easy to launch.

- [More suggestions...](./whentouse.md)
