---
title: DROP SEQUENCE
description: remove a sequence
source_url: https://www.postgresql.org/docs/17/sql-dropsequence.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_sequence.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2540
---

DROP SEQUENCE

DROP SEQUENCE

7

SQL - Language Statements

DROP SEQUENCE

remove a sequence

DROP SEQUENCE \[ IF EXISTS \]

name

\[, ...\] \[ CASCADE \| RESTRICT \]

## Description

`DROP SEQUENCE` removes sequence number generators. A sequence can only be dropped by its owner or a superuser.

## Parameters

`IF EXISTS`  
Do not throw an error if the sequence does not exist. A notice is issued in this case.

\<name\>  
The name (optionally schema-qualified) of a sequence.

`CASCADE`  
Automatically drop objects that depend on the sequence, and in turn all objects that depend on those objects (see [???](#ddl-depend)).

`RESTRICT`  
Refuse to drop the sequence if any objects depend on it. This is the default.

## Examples

To remove the sequence `serial`:

    DROP SEQUENCE serial;

## Compatibility

`DROP SEQUENCE` conforms to the SQL standard, except that the standard only allows one sequence to be dropped per command, and apart from the `IF EXISTS` option, which is a PostgreSQL extension.

## See Also
