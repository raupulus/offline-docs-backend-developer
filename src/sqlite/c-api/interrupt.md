---
title: Interrupt A Long-Running Query
source_url: https://www.sqlite.org/c3ref/interrupt.html
source_path: c3ref/interrupt.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1390
---

> \
> void sqlite3_interrupt(sqlite3\*);\
> int sqlite3_is_interrupted(sqlite3\*);\

This function causes any pending database operation to abort and return at its earliest opportunity. This routine is typically called in response to a user action such as pressing "Cancel" or Ctrl-C where the user wants a long query operation to halt immediately.

It is safe to call this routine from a thread different from the thread that is currently running the database operation. But it is not safe to call this routine with a [database connection](../c3ref/sqlite3.md) that is closed or might close before sqlite3_interrupt() returns.

If an SQL operation is very nearly finished at the time when sqlite3_interrupt() is called, then it might not have an opportunity to be interrupted and might continue to completion.

An SQL operation that is interrupted will return [SQLITE_INTERRUPT](../rescode.md#interrupt). If the interrupted SQL operation is an INSERT, UPDATE, or DELETE that is inside an explicit transaction, then the entire transaction will be rolled back automatically.

The sqlite3_interrupt(D) call is in effect until all currently running SQL statements on [database connection](../c3ref/sqlite3.md) D complete. Any new SQL statements that are started after the sqlite3_interrupt() call and before the running statement count reaches zero are interrupted as if they had been running prior to the sqlite3_interrupt() call. New SQL statements that are started after the running statement count reaches zero are not effected by the sqlite3_interrupt(). A call to sqlite3_interrupt(D) that occurs when there are no running SQL statements is a no-op and has no effect on SQL statements that are started after the sqlite3_interrupt() call returns.

The [sqlite3_is_interrupted(D)](../c3ref/interrupt.md) interface can be used to determine whether or not an interrupt is currently in effect for [database connection](../c3ref/sqlite3.md) D. It returns 1 if an interrupt is currently in effect, or 0 otherwise.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
