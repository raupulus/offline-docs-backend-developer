---
title: Evaluate An SQL Statement
source_url: https://www.sqlite.org/c3ref/step.html
source_path: c3ref/step.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1880
---

> \
> int sqlite3_step(sqlite3_stmt\*);\

After a [prepared statement](../c3ref/stmt.md) has been prepared using any of [sqlite3_prepare_v2()](../c3ref/prepare.md), [sqlite3_prepare_v3()](../c3ref/prepare.md), [sqlite3_prepare16_v2()](../c3ref/prepare.md), or [sqlite3_prepare16_v3()](../c3ref/prepare.md) or one of the legacy interfaces [sqlite3_prepare()](../c3ref/prepare.md) or [sqlite3_prepare16()](../c3ref/prepare.md), this function must be called one or more times to evaluate the statement.

The details of the behavior of the sqlite3_step() interface depend on whether the statement was prepared using the newer "vX" interfaces [sqlite3_prepare_v3()](../c3ref/prepare.md), [sqlite3_prepare_v2()](../c3ref/prepare.md), [sqlite3_prepare16_v3()](../c3ref/prepare.md), [sqlite3_prepare16_v2()](../c3ref/prepare.md) or the older legacy interfaces [sqlite3_prepare()](../c3ref/prepare.md) and [sqlite3_prepare16()](../c3ref/prepare.md). The use of the new "vX" interface is recommended for new applications but the legacy interface will continue to be supported.

In the legacy interface, the return value will be either [SQLITE_BUSY](../rescode.md#busy), [SQLITE_DONE](../rescode.md#done), [SQLITE_ROW](../rescode.md#row), [SQLITE_ERROR](../rescode.md#error), or [SQLITE_MISUSE](../rescode.md#misuse). With the "v2" interface, any of the other [result codes](../rescode.md) or [extended result codes](../rescode.md#extrc) might be returned as well.

[SQLITE_BUSY](../rescode.md#busy) means that the database engine was unable to acquire the database locks it needs to do its job. If the statement is a [COMMIT](../lang_transaction.md) or occurs outside of an explicit transaction, then you can retry the statement. If the statement is not a [COMMIT](../lang_transaction.md) and occurs within an explicit transaction then you should rollback the transaction before continuing.

[SQLITE_DONE](../rescode.md#done) means that the statement has finished executing successfully. sqlite3_step() should not be called again on this virtual machine without first calling [sqlite3_reset()](../c3ref/reset.md) to reset the virtual machine back to its initial state.

If the SQL statement being executed returns any data, then [SQLITE_ROW](../rescode.md#row) is returned each time a new row of data is ready for processing by the caller. The values may be accessed using the [column access functions](../c3ref/column_blob.md). sqlite3_step() is called again to retrieve the next row of data.

[SQLITE_ERROR](../rescode.md#error) means that a run-time error (such as a constraint violation) has occurred. sqlite3_step() should not be called again on the VM. More information may be found by calling [sqlite3_errmsg()](../c3ref/errcode.md). With the legacy interface, a more specific error code (for example, [SQLITE_INTERRUPT](../rescode.md#interrupt), [SQLITE_SCHEMA](../rescode.md#schema), [SQLITE_CORRUPT](../rescode.md#corrupt), and so forth) can be obtained by calling [sqlite3_reset()](../c3ref/reset.md) on the [prepared statement](../c3ref/stmt.md). In the "v2" interface, the more specific error code is returned directly by sqlite3_step().

[SQLITE_MISUSE](../rescode.md#misuse) means that the this routine was called inappropriately. Perhaps it was called on a [prepared statement](../c3ref/stmt.md) that has already been [finalized](../c3ref/finalize.md) or on one that had previously returned [SQLITE_ERROR](../rescode.md#error) or [SQLITE_DONE](../rescode.md#done). Or it could be the case that the same database connection is being used by two or more threads at the same moment in time.

For all versions of SQLite up to and including 3.6.23.1, a call to [sqlite3_reset()](../c3ref/reset.md) was required after sqlite3_step() returned anything other than [SQLITE_ROW](../rescode.md#row) before any subsequent invocation of sqlite3_step(). Failure to reset the prepared statement using [sqlite3_reset()](../c3ref/reset.md) would result in an [SQLITE_MISUSE](../rescode.md#misuse) return from sqlite3_step(). But after [version 3.6.23.1](../releaselog/3_6_23_1.md) (2010-03-26), sqlite3_step() began calling [sqlite3_reset()](../c3ref/reset.md) automatically in this circumstance rather than returning [SQLITE_MISUSE](../rescode.md#misuse). This is not considered a compatibility break because any application that ever receives an SQLITE_MISUSE error is broken by definition. The [SQLITE_OMIT_AUTORESET](../compile.md#omit_autoreset) compile-time option can be used to restore the legacy behavior.

**Goofy Interface Alert:** In the legacy interface, the sqlite3_step() API always returns a generic error code, [SQLITE_ERROR](../rescode.md#error), following any error other than [SQLITE_BUSY](../rescode.md#busy) and [SQLITE_MISUSE](../rescode.md#misuse). You must call [sqlite3_reset()](../c3ref/reset.md) or [sqlite3_finalize()](../c3ref/finalize.md) in order to find one of the specific [error codes](../rescode.md) that better describes the error. We admit that this is a goofy design. The problem has been fixed with the "v2" interface. If you prepare all of your SQL statements using [sqlite3_prepare_v3()](../c3ref/prepare.md) or [sqlite3_prepare_v2()](../c3ref/prepare.md) or [sqlite3_prepare16_v2()](../c3ref/prepare.md) or [sqlite3_prepare16_v3()](../c3ref/prepare.md) instead of the legacy [sqlite3_prepare()](../c3ref/prepare.md) and [sqlite3_prepare16()](../c3ref/prepare.md) interfaces, then the more specific [error codes](../rescode.md) are returned directly by sqlite3_step(). The use of the "vX" interfaces is recommended.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
