---
title: DROP INDEX
description: remove an index
source_url: https://www.postgresql.org/docs/17/sql-dropindex.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_index.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2400
---

DROP INDEX

DROP INDEX

7

SQL - Language Statements

DROP INDEX

remove an index

DROP INDEX \[ CONCURRENTLY \] \[ IF EXISTS \]

name

\[, ...\] \[ CASCADE \| RESTRICT \]

## Description

`DROP INDEX` drops an existing index from the database system. To execute this command you must be the owner of the index.

## Parameters

`CONCURRENTLY`  
Drop the index without locking out concurrent selects, inserts, updates, and deletes on the index's table. A normal `DROP INDEX` acquires an `ACCESS EXCLUSIVE` lock on the table, blocking other accesses until the index drop can be completed. With this option, the command instead waits until conflicting transactions have completed.

There are several caveats to be aware of when using this option. Only one index name can be specified, and the `CASCADE` option is not supported. (Thus, an index that supports a `UNIQUE` or `PRIMARY KEY` constraint cannot be dropped this way.) Also, regular `DROP INDEX` commands can be performed within a transaction block, but `DROP INDEX CONCURRENTLY` cannot. Lastly, indexes on partitioned tables cannot be dropped using this option.

For temporary tables, `DROP INDEX` is always non-concurrent, as no other session can access them, and non-concurrent index drop is cheaper.

`IF EXISTS`  
Do not throw an error if the index does not exist. A notice is issued in this case.

\<name\>  
The name (optionally schema-qualified) of an index to remove.

`CASCADE`  
Automatically drop objects that depend on the index, and in turn all objects that depend on those objects (see [???](#ddl-depend)).

`RESTRICT`  
Refuse to drop the index if any objects depend on it. This is the default.

## Examples

This command will remove the index `title_idx`:

    DROP INDEX title_idx;

## Compatibility

`DROP INDEX` is a PostgreSQL language extension. There are no provisions for indexes in the SQL standard.

## See Also
