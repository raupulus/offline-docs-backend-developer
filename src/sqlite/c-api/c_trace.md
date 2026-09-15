---
title: SQL Trace Event Codes
source_url: https://www.sqlite.org/c3ref/c_trace.html
source_path: c3ref/c_trace.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 760
---

> \
> \#define SQLITE_TRACE_STMT       0x01\
> \#define SQLITE_TRACE_PROFILE    0x02\
> \#define SQLITE_TRACE_ROW        0x04\
> \#define SQLITE_TRACE_CLOSE      0x08\

These constants identify classes of events that can be monitored using the [sqlite3_trace_v2()](../c3ref/trace_v2.md) tracing logic. The M argument to [sqlite3_trace_v2(D,M,X,P)](../c3ref/trace_v2.md) is an OR-ed combination of one or more of the following constants. The first argument to the trace callback is one of the following constants.

New tracing constants may be added in future releases.

A trace callback has four arguments: xCallback(T,C,P,X). The T argument is one of the integer type codes above. The C argument is a copy of the context pointer passed in as the fourth argument to [sqlite3_trace_v2()](../c3ref/trace_v2.md). The P and X arguments are pointers whose meanings depend on T.

SQLITE_TRACE_STMT  
An SQLITE_TRACE_STMT callback is invoked when a prepared statement first begins running and possibly at other times during the execution of the prepared statement, such as at the start of each trigger subprogram. The P argument is a pointer to the [prepared statement](../c3ref/stmt.md). The X argument is a pointer to a string which is the unexpanded SQL text of the prepared statement or an SQL comment that indicates the invocation of a trigger. The callback can compute the same text that would have been returned by the legacy [sqlite3_trace()](../c3ref/profile.md) interface by using the X argument when X begins with "--" and invoking [sqlite3_expanded_sql(P)](../c3ref/expanded_sql.md) otherwise.

<span id="sqlitetraceprofile"></span>

SQLITE_TRACE_PROFILE  
An SQLITE_TRACE_PROFILE callback provides approximately the same information as is provided by the [sqlite3_profile()](../c3ref/profile.md) callback. The P argument is a pointer to the [prepared statement](../c3ref/stmt.md) and the X argument points to a 64-bit integer which is approximately the number of nanoseconds that the prepared statement took to run. The SQLITE_TRACE_PROFILE callback is invoked when the statement finishes.

<span id="sqlitetracerow"></span>

SQLITE_TRACE_ROW  
An SQLITE_TRACE_ROW callback is invoked whenever a prepared statement generates a single row of result. The P argument is a pointer to the [prepared statement](../c3ref/stmt.md) and the X argument is unused.

<span id="sqlitetraceclose"></span>

SQLITE_TRACE_CLOSE  
An SQLITE_TRACE_CLOSE callback is invoked when a database connection closes. The P argument is a pointer to the [database connection](../c3ref/sqlite3.md) object and the X argument is unused.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
