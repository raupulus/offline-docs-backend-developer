---
title: The Schema Table
source_url: https://www.sqlite.org/schematab.html
source_path: schematab.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6550
---

# 1. Introduction

Every SQLite database contains a single "schema table" that stores the schema for that database. The schema for a database is a description of all of the other tables, indexes, triggers, and views that are contained within the database. The schema table looks like this:

> \
> CREATE TABLE sqlite_schema(\
>   type text,\
>   name text,\
>   tbl_name text,\
>   rootpage integer,\
>   sql text\
> );\

The sqlite_schema table contains one row for each table, index, view, and trigger (collectively "objects") in the schema, except there is no entry for the sqlite_schema table itself. See the [schema storage](fileformat2.md#ffschema) subsection of the [file format](fileformat2.md) documentation for additional information on how SQLite uses the sqlite_schema table internally.

# 2. Alternative Names

The schema table can always be referenced using the name "sqlite_schema", especially if qualifed by the schema name like "main.sqlite_schema" or "temp.sqlite_schema". But for historical compatibility, some alternative names are also recognized, including:

1.  sqlite_master
2.  sqlite_temp_schema
3.  sqlite_temp_master

Alternatives (2) and (3) only work for the TEMP database associated with each database connection, but alternative (1) works anywhere. For historical reasons, callbacks from the [sqlite3_set_authorizer()](c3ref/set_authorizer.md) interface always refer to the schema table using names (1) or (3).

# 3. Interpretation Of The Schema Table

The meanings of the fields of the schema table are as follows:

**type**  
The sqlite_schema.type column will be one of the following text strings: 'table', 'index', 'view', or 'trigger' according to the type of object defined. The 'table' string is used for both ordinary and [virtual tables](vtab.md).

**name**\  
The sqlite_schema.name column will hold the name of the object. [UNIQUE](lang_createtable.md#uniqueconst) and [PRIMARY KEY](lang_createtable.md#primkeyconst) constraints on tables cause SQLite to create [internal indexes](fileformat2.md#intschema) with names of the form "sqlite_autoindex_TABLE_N" where TABLE is replaced by the name of the table that contains the constraint and N is an integer beginning with 1 and increasing by one with each constraint seen in the table definition. In a [WITHOUT ROWID](withoutrowid.md) table, there is no sqlite_schema entry for the PRIMARY KEY, but the "sqlite_autoindex_TABLE_N" name is set aside for the PRIMARY KEY as if the sqlite_schema entry did exist. This will affect the numbering of subsequent UNIQUE constraints. The "sqlite_autoindex_TABLE_N" name is never allocated for an [INTEGER PRIMARY KEY](lang_createtable.md#rowid), either in rowid tables or WITHOUT ROWID tables.

**tbl_name**  
The sqlite_schema.tbl_name column holds the name of a table or view that the object is associated with. For a table or view, the tbl_name column is a copy of the name column. For an index, the tbl_name is the name of the table that is indexed. For a trigger, the tbl_name column stores the name of the table or view that causes the trigger to fire.

**rootpage**  
The sqlite_schema.rootpage column stores the page number of the root b-tree page for tables and indexes. For rows that define views, triggers, and virtual tables, the rootpage column is 0 or NULL.

**sql**  
The sqlite_schema.sql column stores SQL text that describes the object. This SQL text is a [CREATE TABLE](lang_createtable.md), [CREATE VIRTUAL TABLE](lang_createvtab.md), [CREATE INDEX](lang_createindex.md), [CREATE VIEW](lang_createview.md), or [CREATE TRIGGER](lang_createtrigger.md) statement that if evaluated against the database file when it is the main database of a [database connection](c3ref/sqlite3.md) would recreate the object. The text is usually a copy of the original statement used to create the object but with normalizations applied so that the text conforms to the following rules:

- The CREATE, TABLE, VIEW, TRIGGER, and INDEX keywords at the beginning of the statement are converted to all upper case letters.
- The TEMP or TEMPORARY keyword is removed if it occurs after the initial CREATE keyword.
- Any database name qualifier that occurs prior to the name of the object being created is removed.
- Leading spaces are removed.
- All spaces following the first two keywords are converted into a single space.

The text in the sqlite_schema.sql column is a copy of the original CREATE statement text that created the object, except normalized as described above and as modified by subsequent [ALTER TABLE](lang_altertable.md) statements. The sqlite_schema.sql is NULL for the [internal indexes](fileformat2.md#intschema) that are automatically created by [UNIQUE](lang_createtable.md#uniqueconst) or [PRIMARY KEY](lang_createtable.md#primkeyconst) constraints.

# 4. Creation and Modification Of The Schema Table

SQLite creates the schema table upon database creation and modifies its content as SQLite users submit DDL statements for execution. There is no need for users to modify it under normal circumstances, and they bear the risk of [database corruption](howtocorrupt.md#cfgerr) if they do modify it.
