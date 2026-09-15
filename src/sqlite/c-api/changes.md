---
title: Count The Number Of Rows Modified
source_url: https://www.sqlite.org/c3ref/changes.html
source_path: c3ref/changes.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 820
---

> \
> int sqlite3_changes(sqlite3\*);\
> sqlite3_int64 sqlite3_changes64(sqlite3\*);\

These functions return the number of rows modified, inserted or deleted by the most recently completed INSERT, UPDATE or DELETE statement on the database connection specified by the only parameter. The two functions are identical except for the type of the return value and that if the number of rows modified by the most recent INSERT, UPDATE, or DELETE is greater than the maximum value supported by type "int", then the return value of sqlite3_changes() is undefined. Executing any other type of SQL statement does not modify the value returned by these functions. For the purposes of this interface, a CREATE TABLE AS SELECT statement does not count as an INSERT, UPDATE or DELETE statement and hence the rows added to the new table by the CREATE TABLE AS SELECT statement are not counted.

Only changes made directly by the INSERT, UPDATE or DELETE statement are considered - auxiliary changes caused by [triggers](../lang_createtrigger.md), [foreign key actions](../foreignkeys.md#fk_actions) or [REPLACE](../lang_replace.md) constraint resolution are not counted.

Changes to a view that are intercepted by [INSTEAD OF triggers](../lang_createtrigger.md#instead_of_trigger) are not counted. The value returned by sqlite3_changes() immediately after an INSERT, UPDATE or DELETE statement run on a view is always zero. Only changes made to real tables are counted.

Things are more complicated if the sqlite3_changes() function is executed while a trigger program is running. This may happen if the program uses the [changes() SQL function](../lang_corefunc.md#changes), or if some other callback function invokes sqlite3_changes() directly. Essentially:

- Before entering a trigger program the value returned by sqlite3_changes() function is saved. After the trigger program has finished, the original value is restored.
- Within a trigger program each INSERT, UPDATE and DELETE statement sets the value returned by sqlite3_changes() upon completion as normal. Of course, this value will not include any changes performed by sub-triggers, as the sqlite3_changes() value will be saved and restored after each sub-trigger has run.

This means that if the changes() SQL function (or similar) is used by the first INSERT, UPDATE or DELETE statement within a trigger, it returns the value as set when the calling statement began executing. If it is used by the second or subsequent such statement within a trigger program, the value returned reflects the number of rows modified by the previous INSERT, UPDATE or DELETE statement within the same trigger.

If a separate thread makes changes on the same database connection while [sqlite3_changes()](../c3ref/changes.md) is running then the value returned is unpredictable and not meaningful.

See also:

- the [sqlite3_total_changes()](../c3ref/total_changes.md) interface
- the [count_changes pragma](../pragma.md#pragma_count_changes)
- the [changes() SQL function](../lang_corefunc.md#changes)
- the [data_version pragma](../pragma.md#pragma_data_version)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
