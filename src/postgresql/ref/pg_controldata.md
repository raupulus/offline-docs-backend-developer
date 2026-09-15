---
title: pg_controldata
description: display control information of a PostgreSQL database cluster
source_url: https://www.postgresql.org/docs/17/app-pgcontroldata.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/pg_controldata.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 2920
---

pg_controldata

pg_controldata

1

Application

pg_controldata

display control information of a

PostgreSQL

database cluster

pg_controldata

option

-D

--pgdata

datadir

## Description

`pg_controldata` prints information initialized during `initdb`, such as the catalog version. It also shows information about write-ahead logging and checkpoint processing. This information is cluster-wide, and not specific to any one database.

This utility can only be run by the user who initialized the cluster because it requires read access to the data directory. You can specify the data directory on the command line, or use the environment variable `PGDATA`. This utility supports the options `-V` and `--version`, which print the pg_controldata version and exit. It also supports options `-?` and `--help`, which output the supported arguments.

## Environment

`PGDATA`  
Default data directory location

`PG_COLOR`  
Specifies whether to use color in diagnostic messages. Possible values are `always`, `auto` and `never`.
