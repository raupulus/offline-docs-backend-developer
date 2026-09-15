---
title: Determine If An SQL Statement Writes The Database
source_url: https://www.sqlite.org/c3ref/stmt_readonly.html
source_path: c3ref/stmt_readonly.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1930
---

> \
> int sqlite3_stmt_readonly(sqlite3_stmt \*pStmt);\

The sqlite3_stmt_readonly(X) interface returns true (non-zero) if and only if the [prepared statement](../c3ref/stmt.md) X makes no direct changes to the content of the database file.

Note that [application-defined SQL functions](../appfunc.md) or [virtual tables](../vtab.md) might change the database indirectly as a side effect. For example, if an application defines a function "eval()" that calls [sqlite3_exec()](../c3ref/exec.md), then the following SQL statement would change the database file through side-effects:

> \
> SELECT eval('DELETE FROM t1') FROM t2;\

But because the [SELECT](../lang_select.md) statement does not change the database file directly, sqlite3_stmt_readonly() would still return true.

Transaction control statements such as [BEGIN](../lang_transaction.md), [COMMIT](../lang_transaction.md), [ROLLBACK](../lang_transaction.md), [SAVEPOINT](../lang_savepoint.md), and [RELEASE](../lang_savepoint.md) cause sqlite3_stmt_readonly() to return true, since the statements themselves do not actually modify the database but rather they control the timing of when other statements modify the database. The [ATTACH](../lang_attach.md) and [DETACH](../lang_detach.md) statements also cause sqlite3_stmt_readonly() to return true since, while those statements change the configuration of a database connection, they do not make changes to the content of the database files on disk. The sqlite3_stmt_readonly() interface returns true for [BEGIN](../lang_transaction.md) since [BEGIN](../lang_transaction.md) merely sets internal flags, but the [BEGIN IMMEDIATE](../lang_transaction.md) and [BEGIN EXCLUSIVE](../lang_transaction.md) commands do touch the database and so sqlite3_stmt_readonly() returns false for those commands.

This routine returns false if there is any possibility that the statement might change the database file. A false return does not guarantee that the statement will change the database file. For example, an UPDATE statement might have a WHERE clause that makes it a no-op, but the sqlite3_stmt_readonly() result would still be false. Similarly, a CREATE TABLE IF NOT EXISTS statement is a read-only no-op if the table already exists, but sqlite3_stmt_readonly() still returns false for such a statement.

If prepared statement X is an [EXPLAIN](../lang_explain.md) or [EXPLAIN QUERY PLAN](../eqp.md) statement, then sqlite3_stmt_readonly(X) returns the same value as if the EXPLAIN or EXPLAIN QUERY PLAN prefix were omitted.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
