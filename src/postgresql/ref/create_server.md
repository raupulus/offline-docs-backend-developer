---
title: CREATE SERVER
description: define a new foreign server
source_url: https://www.postgresql.org/docs/17/sql-createserver.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/create_server.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2040
---

CREATE SERVER

CREATE SERVER

7

SQL - Language Statements

CREATE SERVER

define a new foreign server

CREATE SERVER \[ IF NOT EXISTS \]

server_name

\[ TYPE '

server_type

' \] \[ VERSION '

server_version

' \] FOREIGN DATA WRAPPER

fdw_name

\[ OPTIONS (

option

'

value

' \[, ... \] ) \]

## Description

`CREATE SERVER` defines a new foreign server. The user who defines the server becomes its owner.

A foreign server typically encapsulates connection information that a foreign-data wrapper uses to access an external data resource. Additional user-specific connection information may be specified by means of user mappings.

The server name must be unique within the database.

Creating a server requires `USAGE` privilege on the foreign-data wrapper being used.

## Parameters

`IF NOT EXISTS`  
Do not throw an error if a server with the same name already exists. A notice is issued in this case. Note that there is no guarantee that the existing server is anything like the one that would have been created.

\<server_name\>  
The name of the foreign server to be created.

\<server_type\>  
Optional server type, potentially useful to foreign-data wrappers.

\<server_version\>  
Optional server version, potentially useful to foreign-data wrappers.

\<fdw_name\>  
The name of the foreign-data wrapper that manages the server.

`OPTIONS ( option 'value' [, ... ] )`  
This clause specifies the options for the server. The options typically define the connection details of the server, but the actual names and values are dependent on the server's foreign-data wrapper.

## Notes

When using the [???](#dblink) module, a foreign server's name can be used as an argument of the [???](#contrib-dblink-connect) function to indicate the connection parameters. It is necessary to have the `USAGE` privilege on the foreign server to be able to use it in this way.

If the foreign server supports sort pushdown, it is necessary for it to have the same sort ordering as the local server.

## Examples

Create a server `myserver` that uses the foreign-data wrapper `postgres_fdw`:

    CREATE SERVER myserver FOREIGN DATA WRAPPER postgres_fdw OPTIONS (host 'foo', dbname 'foodb', port '5432');

See [???](#postgres-fdw) for more details.

## Compatibility

`CREATE SERVER` conforms to ISO/IEC 9075-9 (SQL/MED).

## See Also
