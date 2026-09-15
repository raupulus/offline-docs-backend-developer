---
title: Register A Callback To Handle SQLITE_BUSY Errors
source_url: https://www.sqlite.org/c3ref/busy_handler.html
source_path: c3ref/busy_handler.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 380
---

> \
> int sqlite3_busy_handler(sqlite3\*,int(\*)(void\*,int),void\*);\

The sqlite3_busy_handler(D,X,P) routine sets a callback function X that might be invoked with argument P whenever an attempt is made to access a database table associated with [database connection](../c3ref/sqlite3.md) D when another thread or process has the table locked. The sqlite3_busy_handler() interface is used to implement [sqlite3_busy_timeout()](../c3ref/busy_timeout.md) and [PRAGMA busy_timeout](../pragma.md#pragma_busy_timeout).

If the busy callback is NULL, then [SQLITE_BUSY](../rescode.md#busy) is returned immediately upon encountering the lock. If the busy callback is not NULL, then the callback might be invoked with two arguments.

The first argument to the busy handler is a copy of the void\* pointer which is the third argument to sqlite3_busy_handler(). The second argument to the busy handler callback is the number of times that the busy handler has been invoked previously for the same locking event. If the busy callback returns 0, then no additional attempts are made to access the database and [SQLITE_BUSY](../rescode.md#busy) is returned to the application. If the callback returns non-zero, then another attempt is made to access the database and the cycle repeats.

The presence of a busy handler does not guarantee that it will be invoked when there is lock contention. If SQLite determines that invoking the busy handler could result in a deadlock, it will go ahead and return [SQLITE_BUSY](../rescode.md#busy) to the application instead of invoking the busy handler. Consider a scenario where one process is holding a read lock that it is trying to promote to a reserved lock and a second process is holding a reserved lock that it is trying to promote to an exclusive lock. The first process cannot proceed because it is blocked by the second and the second process cannot proceed because it is blocked by the first. If both processes invoke the busy handlers, neither will make any progress. Therefore, SQLite returns [SQLITE_BUSY](../rescode.md#busy) for the first process, hoping that this will induce the first process to release its read lock and allow the second process to proceed.

The default busy callback is NULL.

There can only be a single busy handler defined for each [database connection](../c3ref/sqlite3.md). Setting a new busy handler clears any previously set handler. Note that calling [sqlite3_busy_timeout()](../c3ref/busy_timeout.md) or evaluating [PRAGMA busy_timeout=N](../pragma.md#pragma_busy_timeout) will change the busy handler and thus clear any previously set busy handler.

The busy callback should not take any actions which modify the database connection that invoked the busy handler. In other words, the busy handler is not reentrant. Any such actions result in undefined behavior.

A busy handler must not close the database connection or [prepared statement](../c3ref/stmt.md) that invoked the busy handler.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
