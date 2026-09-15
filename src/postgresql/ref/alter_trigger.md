---
title: ALTER TRIGGER
description: change the definition of a trigger
source_url: https://www.postgresql.org/docs/17/sql-altertrigger.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/alter_trigger.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 1580
---

ALTER TRIGGER

ALTER TRIGGER

7

SQL - Language Statements

ALTER TRIGGER

change the definition of a trigger

ALTER TRIGGER

name

ON

table_name

RENAME TO

new_name

ALTER TRIGGER

name

ON

table_name

\[ NO \] DEPENDS ON EXTENSION

extension_name

## Description

`ALTER TRIGGER` changes properties of an existing trigger.

The `RENAME` clause changes the name of the given trigger without otherwise changing the trigger definition. If the table that the trigger is on is a partitioned table, then corresponding clone triggers in the partitions are renamed too.

The `DEPENDS ON EXTENSION` clause marks the trigger as dependent on an extension, such that if the extension is dropped, the trigger will automatically be dropped as well.

You must own the table on which the trigger acts to be allowed to change its properties.

## Parameters

\<name\>  
The name of an existing trigger to alter.

\<table_name\>  
The name of the table on which this trigger acts.

\<new_name\>  
The new name for the trigger.

\<extension_name\>  
The name of the extension that the trigger is to depend on (or no longer dependent on, if `NO` is specified). A trigger that's marked as dependent on an extension is automatically dropped when the extension is dropped.

## Notes

The ability to temporarily enable or disable a trigger is provided by [`ALTER TABLE`](#sql-altertable), not by `ALTER TRIGGER`, because `ALTER TRIGGER` has no convenient way to express the option of enabling or disabling all of a table's triggers at once.

## Examples

To rename an existing trigger:

    ALTER TRIGGER emp_stamp ON emp RENAME TO emp_track_chgs;

To mark a trigger as being dependent on an extension:

    ALTER TRIGGER emp_stamp ON emp DEPENDS ON EXTENSION emplib;

## Compatibility

`ALTER TRIGGER` is a PostgreSQL extension of the SQL standard.

## See Also
