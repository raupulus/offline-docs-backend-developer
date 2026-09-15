---
title: recovery.conf file merged into postgresql.conf
source_url: https://www.postgresql.org/docs/17/recovery-config.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: appendix-obsolete-recovery-config.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 80
---

## `recovery.conf` file merged into `postgresql.conf`

recovery.conf

PostgreSQL 11 and below used a configuration file named `recovery.conf` <span class="indexterm"></span> to manage replicas and standbys. Support for this file was removed in PostgreSQL 12. See [the release notes for PostgreSQL 12](#release-prior) for details on this change.

On PostgreSQL 12 and above, [archive recovery, streaming replication, and PITR](#continuous-archiving) are configured using [normal server configuration parameters](#runtime-config-replication-standby). These are set in `postgresql.conf` or via [ALTER SYSTEM](#sql-altersystem) like any other parameter.

The server will not start if a `recovery.conf` exists.

PostgreSQL 15 and below had a setting `promote_trigger_file`, or `trigger_file` before 12. Use `pg_ctl promote` or call `pg_promote()` to promote a standby instead.

The `standby_mode` <span class="indexterm"></span> setting has been removed. A `standby.signal` file in the data directory is used instead. See [???](#standby-server-operation) for details.
