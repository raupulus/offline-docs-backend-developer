---
title: Deprecated Tracing And Profiling Functions
source_url: https://www.sqlite.org/c3ref/profile.html
source_path: c3ref/profile.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1650
---

> \
> void \*sqlite3_trace(sqlite3\*,\
>    void(\*xTrace)(void\*,const char\*), void\*);\
> void \*sqlite3_profile(sqlite3\*,\
>    void(\*xProfile)(void\*,const char\*,sqlite3_uint64), void\*);\

These routines are deprecated. Use the [sqlite3_trace_v2()](../c3ref/trace_v2.md) interface instead of the routines described here.

These routines register callback functions that can be used for tracing and profiling the execution of SQL statements.

The callback function registered by sqlite3_trace() is invoked at various times when an SQL statement is being run by [sqlite3_step()](../c3ref/step.md). The sqlite3_trace() callback is invoked with a UTF-8 rendering of the SQL statement text as the statement first begins executing. Additional sqlite3_trace() callbacks might occur as each triggered subprogram is entered. The callbacks for triggers contain a UTF-8 SQL comment that identifies the trigger.

The [SQLITE_TRACE_SIZE_LIMIT](../compile.md#trace_size_limit) compile-time option can be used to limit the length of [bound parameter](../lang_expr.md#varparam) expansion in the output of sqlite3_trace().

The callback function registered by sqlite3_profile() is invoked as each SQL statement finishes. The profile callback contains the original statement text and an estimate of wall-clock time of how long that statement took to run. The profile callback time is in units of nanoseconds, however the current implementation is only capable of millisecond resolution so the six least significant digits in the time are meaningless. Future versions of SQLite might provide greater resolution on the profiler callback. Invoking either [sqlite3_trace()](../c3ref/profile.md) or [sqlite3_trace_v2()](../c3ref/trace_v2.md) will cancel the profile callback.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
