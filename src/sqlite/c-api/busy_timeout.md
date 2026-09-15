---
title: Set A Busy Timeout
source_url: https://www.sqlite.org/c3ref/busy_timeout.html
source_path: c3ref/busy_timeout.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 390
---

> \
> int sqlite3_busy_timeout(sqlite3\*, int ms);\

This routine sets a [busy handler](../c3ref/busy_handler.md) that sleeps for a specified amount of time when a table is locked. The handler will sleep multiple times until at least "ms" milliseconds of sleeping have accumulated. After at least "ms" milliseconds of sleeping, the handler returns 0 which causes [sqlite3_step()](../c3ref/step.md) to return [SQLITE_BUSY](../rescode.md#busy).

Calling this routine with an argument less than or equal to zero turns off all busy handlers.

There can only be a single busy handler for a particular [database connection](../c3ref/sqlite3.md) at any given moment. If another busy handler was defined (using [sqlite3_busy_handler()](../c3ref/busy_handler.md)) prior to calling this routine, that other busy handler is cleared.

See also: [PRAGMA busy_timeout](../pragma.md#pragma_busy_timeout)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
