---
title: CHECKPOINT
description: force a write-ahead log checkpoint
source_url: https://www.postgresql.org/docs/17/sql-checkpoint.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: ref/checkpoint.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
section: ref
order: 1700
---

CHECKPOINT

CHECKPOINT

7

SQL - Language Statements

CHECKPOINT

force a write-ahead log checkpoint

CHECKPOINT

## Description

A checkpoint is a point in the write-ahead log sequence at which all data files have been updated to reflect the information in the log. All data files will be flushed to disk. Refer to [???](#wal-configuration) for more details about what happens during a checkpoint.

The `CHECKPOINT` command forces an immediate checkpoint when the command is issued, without waiting for a regular checkpoint scheduled by the system (controlled by the settings in [???](#runtime-config-wal-checkpoints)). `CHECKPOINT` is not intended for use during normal operation.

If executed during recovery, the `CHECKPOINT` command will force a restartpoint (see [???](#wal-configuration)) rather than writing a new checkpoint.

Only superusers or users with the privileges of the [`pg_checkpoint`](#predefined-roles-table) role can call `CHECKPOINT`.

## Compatibility

The `CHECKPOINT` command is a PostgreSQL language extension.
