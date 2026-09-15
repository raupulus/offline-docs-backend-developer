---
title: SQLite Runtime Status
source_url: https://www.sqlite.org/c3ref/status.html
source_path: c3ref/status.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1870
---

> \
> int sqlite3_status(int op, int \*pCurrent, int \*pHighwater, int resetFlag);\
> int sqlite3_status64(\
>   int op,\
>   sqlite3_int64 \*pCurrent,\
>   sqlite3_int64 \*pHighwater,\
>   int resetFlag\
> );\

These interfaces are used to retrieve runtime status information about the performance of SQLite, and optionally to reset various highwater marks. The first argument is an integer code for the specific parameter to measure. Recognized integer codes are of the form [SQLITE_STATUS\_...](../c3ref/c_status_malloc_count.md). The current value of the parameter is returned into \*pCurrent. The highest recorded value is returned in \*pHighwater. If the resetFlag is true, then the highest record value is reset after \*pHighwater is written. Some parameters do not record the highest value. For those parameters nothing is written into \*pHighwater and the resetFlag is ignored. Other parameters record only the highwater mark and not the current value. For these latter parameters nothing is written into \*pCurrent.

The sqlite3_status() and sqlite3_status64() routines return SQLITE_OK on success and a non-zero [error code](../rescode.md) on failure.

If either the current value or the highwater mark is too large to be represented by a 32-bit integer, then the values returned by sqlite3_status() are undefined.

See also: [sqlite3_db_status()](../c3ref/db_status.md)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
