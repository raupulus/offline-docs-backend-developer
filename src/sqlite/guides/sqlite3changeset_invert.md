---
title: Invert A Changeset
source_url: https://www.sqlite.org/session/sqlite3changeset_invert.html
source_path: session/sqlite3changeset_invert.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6950
---

[](../session/intro.md)

## Session Module C Interface

## Invert A Changeset

> int sqlite3changeset_invert(\
>   int nIn, const void \*pIn,       /\* Input changeset \*/\
>   int \*pnOut, void \*\*ppOut        /\* OUT: Inverse of input \*/\
> );\

This function is used to "invert" a changeset object. Applying an inverted changeset to a database reverses the effects of applying the uninverted changeset. Specifically:

- Each DELETE change is changed to an INSERT, and
- Each INSERT change is changed to a DELETE, and
- For each UPDATE change, the old.\* and new.\* values are exchanged.

This function does not change the order in which changes appear within the changeset. It merely reverses the sense of each individual change.

If successful, a pointer to a buffer containing the inverted changeset is stored in \*ppOut, the size of the same buffer is stored in \*pnOut, and SQLITE_OK is returned. If an error occurs, both \*pnOut and \*ppOut are zeroed and an SQLite error code returned.

It is the responsibility of the caller to eventually call sqlite3_free() on the \*ppOut pointer to free the buffer allocation following a successful call to this function.

WARNING/TODO: This function currently assumes that the input is a valid changeset. If it is not, the results are undefined.

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
