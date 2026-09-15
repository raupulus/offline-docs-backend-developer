---
title: Fundamental Datatypes
source_url: https://www.sqlite.org/c3ref/c_blob.html
source_path: c3ref/c_blob.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 450
---

> \
> \#define SQLITE_INTEGER  1\
> \#define SQLITE_FLOAT    2\
> \#define SQLITE_BLOB     4\
> \#define SQLITE_NULL     5\
> \#ifdef SQLITE_TEXT\
> \# undef SQLITE_TEXT\
> \#else\
> \# define SQLITE_TEXT     3\
> \#endif\
> \#define SQLITE3_TEXT     3\

Every value in SQLite has one of five fundamental datatypes:

- 64-bit signed integer
- 64-bit IEEE floating point number
- string
- BLOB
- NULL

These constants are codes for each of those types.

Note that the SQLITE_TEXT constant was also used in SQLite version 2 for a completely different meaning. Software that links against both SQLite version 2 and SQLite version 3 should use SQLITE3_TEXT, not SQLITE_TEXT.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
