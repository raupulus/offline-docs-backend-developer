---
title: SQL Trace Hook
source_url: https://www.sqlite.org/c3ref/trace_v2.html
source_path: c3ref/trace_v2.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 2110
---

> \
> int sqlite3_trace_v2(\
>   sqlite3\*,\
>   unsigned uMask,\
>   int(\*xCallback)(unsigned,void\*,void\*,void\*),\
>   void \*pCtx\
> );\

The sqlite3_trace_v2(D,M,X,P) interface registers a trace callback function X against [database connection](../c3ref/sqlite3.md) D, using property mask M and context pointer P. If the X callback is NULL or if the M mask is zero, then tracing is disabled. The M argument should be the bitwise OR-ed combination of zero or more [SQLITE_TRACE](../c3ref/c_trace.md) constants.

Each call to either sqlite3_trace(D,X,P) or sqlite3_trace_v2(D,M,X,P) overrides (cancels) all prior calls to sqlite3_trace(D,X,P) or sqlite3_trace_v2(D,M,X,P) for the [database connection](../c3ref/sqlite3.md) D. Each database connection may have at most one trace callback.

The X callback is invoked whenever any of the events identified by mask M occur. The integer return value from the callback is currently ignored, though this may change in future releases. Callback implementations should return zero to ensure future compatibility.

A trace callback is invoked with four arguments: callback(T,C,P,X). The T argument is one of the [SQLITE_TRACE](../c3ref/c_trace.md) constants to indicate why the callback was invoked. The C argument is a copy of the context pointer. The P and X arguments are pointers whose meanings depend on T.

The sqlite3_trace_v2() interface is intended to replace the legacy interfaces [sqlite3_trace()](../c3ref/profile.md) and [sqlite3_profile()](../c3ref/profile.md), both of which are deprecated.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
