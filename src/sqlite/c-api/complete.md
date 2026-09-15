---
title: Determine If An SQL Statement Is Complete
source_url: https://www.sqlite.org/c3ref/complete.html
source_path: c3ref/complete.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 930
---

> \
> int sqlite3_complete(const char \*sql);\
> int sqlite3_complete16(const void \*sql);\

These routines are useful during command-line input to determine if the currently entered text seems to form a complete SQL statement or if additional input is needed before sending the text into SQLite for parsing. These routines return 1 if the input string appears to be a complete SQL statement. A statement is judged to be complete if it ends with a semicolon token and is not a prefix of a well-formed CREATE TRIGGER statement. Semicolons that are embedded within string literals or quoted identifier names or comments are not independent tokens (they are part of the token in which they are embedded) and thus do not count as a statement terminator. Whitespace and comments that follow the final semicolon are ignored.

These routines return 0 if the statement is incomplete. If a memory allocation fails, then SQLITE_NOMEM is returned.

These routines do not parse the SQL statements and thus will not detect syntactically incorrect SQL.

If SQLite has not been initialized using [sqlite3_initialize()](../c3ref/initialize.md) prior to invoking sqlite3_complete16() then sqlite3_initialize() is invoked automatically by sqlite3_complete16(). If that initialization fails, then the return value from sqlite3_complete16() will be non-zero regardless of whether or not the input SQL is complete.

The input to [sqlite3_complete()](../c3ref/complete.md) must be a zero-terminated UTF-8 string.

The input to [sqlite3_complete16()](../c3ref/complete.md) must be a zero-terminated UTF-16 string in native byte order.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
