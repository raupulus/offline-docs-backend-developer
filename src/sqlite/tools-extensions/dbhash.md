---
title: The dbhash.exe Utility Program
source_url: https://www.sqlite.org/dbhash.html
source_path: dbhash.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: tools-extensions
order: 2650
---

# 1. Overview

The **dbhash** (or **dbhash.exe** on Windows) utility is a command-line program that computes the SHA1 hash of the schema and content for an SQLite database.

Dbhash ignores extraneous formatting details and hashes only the database schema and content. Hence the hash is constant even if the database file is modified by:

- [VACUUM](lang_vacuum.md)
- [PRAGMA page_size](pragma.md#pragma_page_size)
- [PRAGMA journal_mode](pragma.md#pragma_journal_mode)
- [REINDEX](lang_reindex.md)
- [ANALYZE](lang_analyze.md)
- copied via the [backup API](backup.md)
- ... and so forth

The operations above can potentially cause vast changes in the raw database file, and hence cause very different SHA1 hashes at the file level. But since the content represented in the database file is unchanged by these operations, the hash computed by dbhash is also unchanged.

Dbhash can be used to compare two databases to confirm that they are equivalent, even though their representation on disk is quite different. Dbhash might also be used to verify the content of a remote database without having to transmit the entire content of the remote database over a slow link.

# 2. Usage

Dbhash is a command-line utility. To run it, type "dbhash" on a command-line prompt followed by the names of one or more SQLite database files that are to be hashed. The database hashes will be displayed on standard output. For example:

drh@bella:~/sqlite/bld\$ dbhash ~/Fossils/sqlite.fossil\
8d3da9ff87196312aaa33076627ccb7943ef79e3 /home/drh/Fossils/sqlite.fossil\

Dbhash supports command-line options that can restrict the tables of the database file that are hashed, or restrict the hash to only content or only the schema. Run "dbhash --help" for further information.

# 3. Building

To build a copy of the dbhash utility program on unix, get a copy of the canonical SQLite source code and enter:

./configure\
make dbhash\

On Windows, enter:

nmake /f makefile.msc dbhash.exe\

The dbhash program is implemented by a single file of C-code called [dbhash.c](https://sqlite.org/src/artifact?ci=trunk&filename=tool/dbhash.c). To build the dbhash program manually, simply compile the dbhash.c source file and link it against the SQLite library.
