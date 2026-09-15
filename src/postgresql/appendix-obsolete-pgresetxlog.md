---
title: pg_resetxlog renamed to pg_resetwal
source_url: https://www.postgresql.org/docs/17/app-pgresetxlog.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: appendix-obsolete-pgresetxlog.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 60
---

## `pg_resetxlog` renamed to `pg_resetwal`

pg_resetxlog

pg_resetwal

PostgreSQL 9.6 and below provided a command named `pg_resetxlog` <span class="indexterm"></span> to reset the write-ahead-log (WAL) files. This command was renamed to `pg_resetwal`, see [???](#app-pgresetwal) for documentation of `pg_resetwal` and see [the release notes for PostgreSQL 10](#release-prior) for details on this change.
