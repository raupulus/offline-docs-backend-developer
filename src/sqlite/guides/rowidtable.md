---
title: Rowid Tables
source_url: https://www.sqlite.org/rowidtable.html
source_path: rowidtable.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6510
---

# Rowid Tables

## 1.0 Definition

A "rowid table" is any table in an SQLite schema that

- is *not* a [virtual table](vtab.md), and
- is *not* a [WITHOUT ROWID](withoutrowid.md) table.

Most tables in a typical SQLite database schema are rowid tables.

Rowid tables are distinguished by the fact that they all have a unique, non-NULL, signed 64-bit integer [rowid](lang_createtable.md#rowid) that is used as the access key for the data in the underlying [B-tree](fileformat2.md#btree) storage engine.

## 2.0 Quirks

- The [PRIMARY KEY](lang_createtable.md#primkeyconst) of a rowid table (if there is one) is usually not the true primary key for the table, in the sense that it is not the unique key used by the underlying [B-tree](fileformat2.md#btree) storage engine. The exception to this rule is when the rowid table declares an [INTEGER PRIMARY KEY](lang_createtable.md#rowid). In the exception, the INTEGER PRIMARY KEY becomes an alias for the [rowid](lang_createtable.md#rowid).

- The true primary key for a rowid table (the value that is used as the key to look up rows in the underlying [B-tree](fileformat2.md#btree) storage engine) is the [rowid](lang_createtable.md#rowid).

- The PRIMARY KEY constraint for a rowid table (as long as it is not the true primary key or INTEGER PRIMARY KEY) is really the same thing as a [UNIQUE constraint](lang_createtable.md#uniqueconst). Because it is not a true primary key, columns of the PRIMARY KEY are allowed to be NULL, in violation of all SQL standards.

- The [rowid](lang_createtable.md#rowid) of a rowid table can be accessed (or changed) by reading or writing to any of the "rowid" or "oid" or "\_rowid\_" columns. Except, if there are declared columns in the table that use any of those special names, then those names refer to the declared columns, not to the underlying [rowid](lang_createtable.md#rowid).

- Access to records via [rowid](lang_createtable.md#rowid) is highly optimized and very fast.

- If the [rowid](lang_createtable.md#rowid) is not aliased by [INTEGER PRIMARY KEY](lang_createtable.md#rowid) then it is not persistent and might change. In particular the [VACUUM](lang_vacuum.md) command will change rowids for tables that do not declare an INTEGER PRIMARY KEY. Therefore, applications should not normally access the rowid directly, but instead use an INTEGER PRIMARY KEY.

- In the underlying [file format](fileformat2.md), each rowid is stored as a [variable-length integer](fileformat2.md#varint). That means that small non-negative rowid values take up less disk space than large or negative rowid values.

- All of the complications above (and others not mentioned here) arise from the need to preserve backwards compatibility for the hundreds of billions of SQLite database files in circulation. In a perfect world, there would be no such thing as a "rowid" and all tables would following the standard semantics implemented as [WITHOUT ROWID](withoutrowid.md) tables, only without the extra "WITHOUT ROWID" keywords. Unfortunately, life is messy. The designer of SQLite offers his sincere apology for the current mess.
