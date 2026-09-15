---
title: Default Roles Renamed to Predefined Roles
source_url: https://www.postgresql.org/docs/17/default-roles.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: appendix-obsolete-default-roles.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 40
---

## Default Roles Renamed to Predefined Roles

default-roles

PostgreSQL 13 and below used the term “Default Roles”. However, as these roles are not able to actually be changed and are installed as part of the system at initialization time, the more appropriate term to use is “Predefined Roles”. See [???](#predefined-roles) for current documentation regarding Predefined Roles, and [the release notes for PostgreSQL 14](#release-prior) for details on this change.
