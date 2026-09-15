---
title: SQLite is a Self Contained System
source_url: https://www.sqlite.org/selfcontained.html
source_path: selfcontained.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6570
---

SQLite is "stand-alone" or "self-contained" in the sense that it has very few dependencies. It runs on any operating system, even stripped-down bare-bones embedded operating systems. SQLite uses no external libraries or interfaces (other than a few standard C-library calls described below). The entire SQLite library is encapsulated in a [single source code file](amalgamation.md) that requires no special facilities or tools to build.

A minimal build of SQLite requires just these routines from the standard C library:

- memcmp()
- memcpy()
- memmove()
- memset()
- strcmp()
- strlen()
- strncmp()

Most builds also use the system memory allocation routines:

- malloc()
- realloc()
- free()

But those routines are optional and can be omitted using a [compile-time option](compile.md#zero_malloc).

Default builds of SQLite contain appropriate [VFS objects](vfs.md) for talking to the underlying operating system, and those VFS objects will contain operating system calls such as open(), read(), write(), fsync(), and so forth. All of these interfaces are readily available on most platforms, and custom VFSes can be designed to run SQLite on even the most austere embedded devices.
