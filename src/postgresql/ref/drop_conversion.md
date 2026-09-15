---
title: DROP CONVERSION
description: remove a conversion
source_url: https://www.postgresql.org/docs/17/sql-dropconversion.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_conversion.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2310
---

DROP CONVERSION

DROP CONVERSION

7

SQL - Language Statements

DROP CONVERSION

remove a conversion

DROP CONVERSION \[ IF EXISTS \]

name

\[ CASCADE \| RESTRICT \]

## Description

`DROP CONVERSION` removes a previously defined conversion. To be able to drop a conversion, you must own the conversion.

## Parameters

`IF EXISTS`  
Do not throw an error if the conversion does not exist. A notice is issued in this case.

\<name\>  
The name of the conversion. The conversion name can be schema-qualified.

`CASCADE`; `RESTRICT`  
These key words do not have any effect, since there are no dependencies on conversions.

## Examples

To drop the conversion named `myname`:

    DROP CONVERSION myname;

## Compatibility

There is no `DROP CONVERSION` statement in the SQL standard, but a `DROP TRANSLATION` statement that goes along with the `CREATE TRANSLATION` statement that is similar to the `CREATE CONVERSION` statement in PostgreSQL.

## See Also
