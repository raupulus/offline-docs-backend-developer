---
title: LOAD
description: load a shared library file
source_url: https://www.postgresql.org/docs/17/sql-load.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/load.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2820
---

LOAD

LOAD

7

SQL - Language Statements

LOAD

load a shared library file

LOAD '

filename

'

## Description

This command loads a shared library file into the PostgreSQL server's address space. If the file has been loaded already, the command does nothing. Shared library files that contain C functions are automatically loaded whenever one of their functions is called. Therefore, an explicit `LOAD` is usually only needed to load a library that modifies the server's behavior through “hooks” rather than providing a set of functions.

The library file name is typically given as just a bare file name, which is sought in the server's library search path (set by [???](#guc-dynamic-library-path)). Alternatively it can be given as a full path name. In either case the platform's standard shared library file name extension may be omitted. See [???](#xfunc-c-dynload) for more information on this topic.

\$libdir/plugins

Non-superusers can only apply `LOAD` to library files located in `$libdir/plugins/` the specified \<filename\> must begin with exactly that string. (It is the database administrator's responsibility to ensure that only “safe” libraries are installed there.)

## Compatibility

`LOAD` is a PostgreSQL extension.

## See Also

[???](#sql-createfunction)
