---
title: pg_receivexlog renamed to pg_receivewal
source_url: https://www.postgresql.org/docs/17/app-pgreceivexlog.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: appendix-obsolete-pgreceivexlog.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 50
---

## `pg_receivexlog` renamed to `pg_receivewal`

pg_receivexlog

pg_receivewal

PostgreSQL 9.6 and below provided a command named `pg_receivexlog` <span class="indexterm"></span> to fetch write-ahead-log (WAL) files. This command was renamed to `pg_receivewal`, see [???](#app-pgreceivewal) for documentation of `pg_receivewal` and see [the release notes for PostgreSQL 10](#release-prior) for details on this change.
