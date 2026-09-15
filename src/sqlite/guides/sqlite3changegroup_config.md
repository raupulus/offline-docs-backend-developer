---
title: Configure a changegroup object
source_url: https://www.sqlite.org/session/sqlite3changegroup_config.html
source_path: session/sqlite3changegroup_config.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6850
---

[](../session/intro.md)

## Session Module C Interface

## Configure a changegroup object

> int sqlite3changegroup_config(sqlite3_changegroup\*, int, void \*pArg);\

Configure the changegroup object passed as the first argument. At present the only valid value for the second parameter is [SQLITE_CHANGEGROUP_CONFIG_PATCHSET](../session/c_changegroup_config_patchset.md).

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
