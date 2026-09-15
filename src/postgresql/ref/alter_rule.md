---
title: ALTER RULE
description: change the definition of a rule
source_url: https://www.postgresql.org/docs/17/sql-alterrule.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/alter_rule.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 1490
---

ALTER RULE

ALTER RULE

7

SQL - Language Statements

ALTER RULE

change the definition of a rule

ALTER RULE

name

ON

table_name

RENAME TO

new_name

## Description

`ALTER RULE` changes properties of an existing rule. Currently, the only available action is to change the rule's name.

To use `ALTER RULE`, you must own the table or view that the rule applies to.

## Parameters

\<name\>  
The name of an existing rule to alter.

\<table_name\>  
The name (optionally schema-qualified) of the table or view that the rule applies to.

\<new_name\>  
The new name for the rule.

## Examples

To rename an existing rule:

    ALTER RULE notify_all ON emp RENAME TO notify_me;

## Compatibility

`ALTER RULE` is a PostgreSQL language extension, as is the entire query rewrite system.

## See Also
