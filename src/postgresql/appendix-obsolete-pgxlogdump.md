---
title: pg_xlogdump renamed to pg_waldump
source_url: https://www.postgresql.org/docs/17/pgxlogdump.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: appendix-obsolete-pgxlogdump.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 70
---

## `pg_xlogdump` renamed to `pg_waldump`

pg_xlogdump

pg_waldump

PostgreSQL 9.6 and below provided a command named `pg_xlogdump` <span class="indexterm"></span> to read write-ahead-log (WAL) files. This command was renamed to `pg_waldump`, see [???](#pgwaldump) for documentation of `pg_waldump` and see [the release notes for PostgreSQL 10](#release-prior) for details on this change.
