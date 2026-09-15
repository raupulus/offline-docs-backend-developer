---
title: Compile-Time Authorization Callbacks
source_url: https://www.sqlite.org/c3ref/set_authorizer.html
source_path: c3ref/set_authorizer.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1740
---

> \
> int sqlite3_set_authorizer(\
>   sqlite3\*,\
>   int (\*xAuth)(void\*,int,const char\*,const char\*,const char\*,const char\*),\
>   void \*pUserData\
> );\

This routine registers an authorizer callback with a particular [database connection](../c3ref/sqlite3.md), supplied in the first argument. The authorizer callback is invoked as SQL statements are being compiled by [sqlite3_prepare()](../c3ref/prepare.md) or its variants [sqlite3_prepare_v2()](../c3ref/prepare.md), [sqlite3_prepare_v3()](../c3ref/prepare.md), [sqlite3_prepare16()](../c3ref/prepare.md), [sqlite3_prepare16_v2()](../c3ref/prepare.md), and [sqlite3_prepare16_v3()](../c3ref/prepare.md). At various points during the compilation process, as logic is being created to perform various actions, the authorizer callback is invoked to see if those actions are allowed. The authorizer callback should return [SQLITE_OK](../rescode.md#ok) to allow the action, [SQLITE_IGNORE](../c3ref/c_deny.md) to disallow the specific action but allow the SQL statement to continue to be compiled, or [SQLITE_DENY](../c3ref/c_deny.md) to cause the entire SQL statement to be rejected with an error. If the authorizer callback returns any value other than [SQLITE_IGNORE](../c3ref/c_deny.md), [SQLITE_OK](../rescode.md#ok), or [SQLITE_DENY](../c3ref/c_deny.md) then the [sqlite3_prepare_v2()](../c3ref/prepare.md) or equivalent call that triggered the authorizer will fail with an error message.

When the callback returns [SQLITE_OK](../rescode.md#ok), that means the operation requested is ok. When the callback returns [SQLITE_DENY](../c3ref/c_deny.md), the [sqlite3_prepare_v2()](../c3ref/prepare.md) or equivalent call that triggered the authorizer will fail with an error message explaining that access is denied.

The first parameter to the authorizer callback is a copy of the third parameter to the sqlite3_set_authorizer() interface. The second parameter to the callback is an integer [action code](../c3ref/c_alter_table.md) that specifies the particular action to be authorized. The third through sixth parameters to the callback are either NULL pointers or zero-terminated strings that contain additional details about the action to be authorized. Applications must always be prepared to encounter a NULL pointer in any of the third through the sixth parameters of the authorization callback.

If the action code is [SQLITE_READ](../c3ref/c_alter_table.md) and the callback returns [SQLITE_IGNORE](../c3ref/c_deny.md) then the [prepared statement](../c3ref/stmt.md) statement is constructed to substitute a NULL value in place of the table column that would have been read if [SQLITE_OK](../rescode.md#ok) had been returned. The [SQLITE_IGNORE](../c3ref/c_deny.md) return can be used to deny an untrusted user access to individual columns of a table. When a table is referenced by a [SELECT](../lang_select.md) but no column values are extracted from that table (for example in a query like "SELECT count(\*) FROM tab") then the [SQLITE_READ](../c3ref/c_alter_table.md) authorizer callback is invoked once for that table with a column name that is an empty string. If the action code is [SQLITE_DELETE](../c3ref/c_alter_table.md) and the callback returns [SQLITE_IGNORE](../c3ref/c_deny.md) then the [DELETE](../lang_delete.md) operation proceeds but the [truncate optimization](../lang_delete.md#truncateopt) is disabled and all rows are deleted individually.

An authorizer is used when [preparing](../c3ref/prepare.md) SQL statements from an untrusted source, to ensure that the SQL statements do not try to access data they are not allowed to see, or that they do not try to execute malicious statements that damage the database. For example, an application may allow a user to enter arbitrary SQL queries for evaluation by a database. But the application does not want the user to be able to make arbitrary changes to the database. An authorizer could then be put in place while the user-entered SQL is being [prepared](../c3ref/prepare.md) that disallows everything except [SELECT](../lang_select.md) statements.

Applications that need to process SQL from untrusted sources might also consider lowering resource limits using [sqlite3_limit()](../c3ref/limit.md) and limiting database size using the [max_page_count](../pragma.md#pragma_max_page_count) [PRAGMA](../pragma.md#syntax) in addition to using an authorizer.

Only a single authorizer can be in place on a database connection at a time. Each call to sqlite3_set_authorizer overrides the previous call. Disable the authorizer by installing a NULL callback. The authorizer is disabled by default.

The authorizer callback must not do anything that will modify the database connection that invoked the authorizer callback. Note that [sqlite3_prepare_v2()](../c3ref/prepare.md) and [sqlite3_step()](../c3ref/step.md) both modify their database connections for the meaning of "modify" in this paragraph.

When [sqlite3_prepare_v2()](../c3ref/prepare.md) is used to prepare a statement, the statement might be re-prepared during [sqlite3_step()](../c3ref/step.md) due to a schema change. Hence, the application should ensure that the correct authorizer callback remains in place during the [sqlite3_step()](../c3ref/step.md).

Note that the authorizer callback is invoked only during [sqlite3_prepare()](../c3ref/prepare.md) or its variants. Authorization is not performed during statement evaluation in [sqlite3_step()](../c3ref/step.md), unless as stated in the previous paragraph, sqlite3_step() invokes sqlite3_prepare_v2() to reprepare a statement after a schema change.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
