---
title: Obtain A Composite Changeset From A Changegroup
source_url: https://www.sqlite.org/session/sqlite3changegroup_output.html
source_path: session/sqlite3changegroup_output.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6880
---

[](../session/intro.md)

## Session Module C Interface

## Obtain A Composite Changeset From A Changegroup

> int sqlite3changegroup_output(\
>   sqlite3_changegroup\*,\
>   int \*pnData,                    /\* OUT: Size of output buffer in bytes \*/\
>   void \*\*ppData                   /\* OUT: Pointer to output buffer \*/\
> );\

Obtain a buffer containing a changeset (or patchset) representing the current contents of the changegroup. If the inputs to the changegroup were themselves changesets, the output is a changeset. Or, if the inputs were patchsets, the output is also a patchset.

As with the output of the sqlite3session_changeset() and sqlite3session_patchset() functions, all changes related to a single table are grouped together in the output of this function. Tables appear in the same order as for the very first changeset added to the changegroup. If the second or subsequent changesets added to the changegroup contain changes for tables that do not appear in the first changeset, they are appended onto the end of the output changeset, again in the order in which they are first encountered.

If an error occurs, an SQLite error code is returned and the output variables (\*pnData) and (\*ppData) are set to 0. Otherwise, SQLITE_OK is returned and the output variables are set to the size of and a pointer to the output buffer, respectively. In this case it is the responsibility of the caller to eventually free the buffer using a call to sqlite3_free().

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
