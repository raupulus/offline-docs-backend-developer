---
title: DROP ROLE
description: remove a database role
source_url: https://www.postgresql.org/docs/17/sql-droprole.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_role.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2500
---

DROP ROLE

DROP ROLE

7

SQL - Language Statements

DROP ROLE

remove a database role

DROP ROLE \[ IF EXISTS \]

name

\[, ...\]

## Description

`DROP ROLE` removes the specified role(s). To drop a superuser role, you must be a superuser yourself; to drop non-superuser roles, you must have `CREATEROLE` privilege and have been granted `ADMIN OPTION` on the role.

A role cannot be removed if it is still referenced in any database of the cluster; an error will be raised if so. Before dropping the role, you must drop all the objects it owns (or reassign their ownership) and revoke any privileges the role has been granted on other objects. The [`REASSIGN OWNED`](#sql-reassign-owned) and [`DROP OWNED`](#sql-drop-owned) commands can be useful for this purpose; see [???](#role-removal) for more discussion.

However, it is not necessary to remove role memberships involving the role; `DROP ROLE` automatically revokes any memberships of the target role in other roles, and of other roles in the target role. The other roles are not dropped nor otherwise affected.

## Parameters

`IF EXISTS`  
Do not throw an error if the role does not exist. A notice is issued in this case.

\<name\>  
The name of the role to remove.

## Notes

PostgreSQL includes a program [???](#app-dropuser) that has the same functionality as this command (in fact, it calls this command) but can be run from the command shell.

## Examples

To drop a role:

    DROP ROLE jonathan;

## Compatibility

The SQL standard defines `DROP ROLE`, but it allows only one role to be dropped at a time, and it specifies different privilege requirements than PostgreSQL uses.

## See Also
