---
title: Options for sqlite3changegroup_config().
source_url: https://www.sqlite.org/session/c_changegroup_config_patchset.html
source_path: session/c_changegroup_config_patchset.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6600
---

[](../session/intro.md)

## Session Module C Interface

## Options for sqlite3changegroup_config().

> \#define SQLITE_CHANGEGROUP_CONFIG_PATCHSET 1\

The following values may be passed as the 2nd parameter to sqlite3changegroup_config().

SQLITE_CHANGEGROUP_CONFIG_PATCHSET

A changegroup object generates either a changeset or patchset. Usually, this is determined by whether the first call to sqlite3changegroup_add() is passed a changeset or a patchset. Or, if the first changes are added to the changegroup object using the sqlite3changegroup_change_xxx() APIs, then this option may be used to configure whether the changegroup object generates a changeset or patchset.

When this option is invoked, parameter pArg must point to a value of type int. If the changegroup currently contains zero changes, and the value of the int variable is zero or greater than zero, then the changegroup is configured to generate a changeset or patchset, respectively. It is a no-op, not an error, if the changegroup is not configured because it has already started accumulating changes.

Before returning, the int variable is set to 0 if the changegroup is configured to generate a changeset, or 1 if it is configured to generate a patchset.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
