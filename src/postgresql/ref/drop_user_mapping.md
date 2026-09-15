---
title: DROP USER MAPPING
description: remove a user mapping for a foreign server
source_url: https://www.postgresql.org/docs/17/sql-dropusermapping.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/drop_user_mapping.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2680
---

DROP USER MAPPING

DROP USER MAPPING

7

SQL - Language Statements

DROP USER MAPPING

remove a user mapping for a foreign server

DROP USER MAPPING \[ IF EXISTS \] FOR {

user_name

\| USER \| CURRENT_ROLE \| CURRENT_USER \| PUBLIC } SERVER

server_name

## Description

`DROP USER MAPPING` removes an existing user mapping from foreign server.

The owner of a foreign server can drop user mappings for that server for any user. Also, a user can drop a user mapping for their own user name if `USAGE` privilege on the server has been granted to the user.

## Parameters

`IF EXISTS`  
Do not throw an error if the user mapping does not exist. A notice is issued in this case.

\<user_name\>  
User name of the mapping. `CURRENT_ROLE`, `CURRENT_USER`, and `USER` match the name of the current user. `PUBLIC` is used to match all present and future user names in the system.

\<server_name\>  
Server name of the user mapping.

## Examples

Drop a user mapping `bob`, server `foo` if it exists:

    DROP USER MAPPING IF EXISTS FOR bob SERVER foo;

## Compatibility

`DROP USER MAPPING` conforms to ISO/IEC 9075-9 (SQL/MED). The `IF EXISTS` clause is a PostgreSQL extension.

## See Also
