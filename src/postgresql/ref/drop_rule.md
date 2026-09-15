---
title: DROP RULE
description: remove a rewrite rule
source_url: https://www.postgresql.org/docs/17/sql-droprule.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_rule.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2520
---

DROP RULE

DROP RULE

7

SQL - Language Statements

DROP RULE

remove a rewrite rule

DROP RULE \[ IF EXISTS \]

name

ON

table_name

\[ CASCADE \| RESTRICT \]

## Description

`DROP RULE` drops a rewrite rule.

## Parameters

`IF EXISTS`  
Do not throw an error if the rule does not exist. A notice is issued in this case.

\<name\>  
The name of the rule to drop.

\<table_name\>  
The name (optionally schema-qualified) of the table or view that the rule applies to.

`CASCADE`  
Automatically drop objects that depend on the rule, and in turn all objects that depend on those objects (see [???](#ddl-depend)).

`RESTRICT`  
Refuse to drop the rule if any objects depend on it. This is the default.

## Examples

To drop the rewrite rule `newrule`:

    DROP RULE newrule ON mytable;

## Compatibility

`DROP RULE` is a PostgreSQL language extension, as is the entire query rewrite system.

## See Also
