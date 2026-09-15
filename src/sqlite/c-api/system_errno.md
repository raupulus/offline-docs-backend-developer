---
title: Low-level system error code
source_url: https://www.sqlite.org/c3ref/system_errno.html
source_path: c3ref/system_errno.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2050
---

> \
> int sqlite3_system_errno(sqlite3\*);\

Attempt to return the underlying operating system error code or error number that caused the most recent I/O error or failure to open a file. The return value is OS-dependent. For example, on unix systems, after [sqlite3_open_v2()](../c3ref/open.md) returns [SQLITE_CANTOPEN](../rescode.md#cantopen), this interface could be called to get back the underlying "errno" that caused the problem, such as ENOSPC, EAUTH, EISDIR, and so forth.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
