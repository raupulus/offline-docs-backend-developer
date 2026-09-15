---
title: ALTER LARGE OBJECT
description: change the definition of a large object
source_url: https://www.postgresql.org/docs/17/sql-alterlargeobject.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/alter_large_object.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 1390
---

ALTER LARGE OBJECT

ALTER LARGE OBJECT

7

SQL - Language Statements

ALTER LARGE OBJECT

change the definition of a large object

ALTER LARGE OBJECT

large_object_oid

OWNER TO {

new_owner

\| CURRENT_ROLE \| CURRENT_USER \| SESSION_USER }

## Description

`ALTER LARGE OBJECT` changes the definition of a large object.

You must own the large object to use `ALTER LARGE OBJECT`. To alter the owner, you must also be able to `SET ROLE` to the new owning role. (However, a superuser can alter any large object anyway.) Currently, the only functionality is to assign a new owner, so both restrictions always apply.

## Parameters

\<large_object_oid\>  
OID of the large object to be altered

\<new_owner\>  
The new owner of the large object

## Compatibility

There is no `ALTER LARGE OBJECT` statement in the SQL standard.

## See Also
