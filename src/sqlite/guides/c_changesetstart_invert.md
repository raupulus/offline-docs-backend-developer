---
title: Flags for sqlite3changeset_start_v2
source_url: https://www.sqlite.org/session/c_changesetstart_invert.html
source_path: session/c_changesetstart_invert.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6640
---

[](../session/intro.md)

## Session Module C Interface

## Flags for sqlite3changeset_start_v2

> \#define SQLITE_CHANGESETSTART_INVERT        0x0002\

The following flags may passed via the 4th parameter to [sqlite3changeset_start_v2](../session/sqlite3changeset_start.md) and [sqlite3changeset_start_v2_strm](../session/sqlite3changegroup_add_strm.md):

SQLITE_CHANGESETSTART_INVERT

Invert the changeset while iterating through it. This is equivalent to inverting a changeset using sqlite3changeset_invert() before applying it. It is an error to specify this flag with a patchset.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
