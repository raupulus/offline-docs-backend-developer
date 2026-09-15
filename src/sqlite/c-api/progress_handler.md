---
title: Query Progress Callbacks
source_url: https://www.sqlite.org/c3ref/progress_handler.html
source_path: c3ref/progress_handler.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1660
---

> \
> void sqlite3_progress_handler(sqlite3\*, int, int(\*)(void\*), void\*);\

The sqlite3_progress_handler(D,N,X,P) interface causes the callback function X to be invoked periodically during long running calls to [sqlite3_step()](../c3ref/step.md) and [sqlite3_prepare()](../c3ref/prepare.md) and similar for database connection D. An example use for this interface is to keep a GUI updated during a large query.

The parameter P is passed through as the only parameter to the callback function X. The parameter N is the approximate number of [virtual machine instructions](../opcode.md) that are evaluated between successive invocations of the callback X. If N is less than one then the progress handler is disabled.

Only a single progress handler may be defined at one time per [database connection](../c3ref/sqlite3.md); setting a new progress handler cancels the old one. Setting parameter X to NULL disables the progress handler. The progress handler is also disabled by setting N to a value less than 1.

If the progress callback returns non-zero, the operation is interrupted. This feature can be used to implement a "Cancel" button on a GUI progress dialog box.

The progress handler callback must not do anything that will modify the database connection that invoked the progress handler. Note that [sqlite3_prepare_v2()](../c3ref/prepare.md) and [sqlite3_step()](../c3ref/step.md) both modify their database connections for the meaning of "modify" in this paragraph.

The progress handler callback would originally only be invoked from the bytecode engine. It still might be invoked during [sqlite3_prepare()](../c3ref/prepare.md) and similar because those routines might force a reparse of the schema which involves running the bytecode engine. However, beginning with SQLite version 3.41.0, the progress handler callback might also be invoked directly from [sqlite3_prepare()](../c3ref/prepare.md) while analyzing and generating code for complex queries.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
