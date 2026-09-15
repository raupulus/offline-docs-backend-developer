---
title: Finish adding one-at-at-time changes to a changegroup
source_url: https://www.sqlite.org/session/sqlite3changegroup_change_finish.html
source_path: session/sqlite3changegroup_change_finish.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6810
---

[](../session/intro.md)

## Session Module C Interface

## Finish adding one-at-at-time changes to a changegroup

> int sqlite3changegroup_change_finish(\
>   sqlite3_changegroup\*, \
>   int bDiscard, \
>   char \*\*pzErr\
> );\

This function may only be called following a successful call to sqlite3changegroup_change_begin(). Otherwise, it is an SQLITE_MISUSE error.

If parameter bDiscard is non-zero, then the current change is simply discarded. In this case this function is always successful and SQLITE_OK returned.

If parameter bDiscard is zero, then an attempt is made to add the current change to the changegroup. Assuming the changegroup is configured to produce a changeset (not a patchset), this requires that:

\* If the change is an INSERT or DELETE, then a value must be specified for all columns of the new.\* or old.\* record, respectively.

\* If the change is an UPDATE record, then values must be provided for the PRIMARY KEY columns of the old.\* record, but must not be provided for PRIMARY KEY columns of the new.\* record.

\* If the change is an UPDATE record, then for each non-PRIMARY KEY column in the old.\* record for which a value has been provided, a value must also be provided for the same column in the new.\* record. Similarly, for each non-PK column in the old.\* record for which a value is not provided, a value must not be provided for the same column in the new.\* record.

\* All values specified for PRIMARY KEY columns must be non-NULL.

Otherwise, it is an error.

If the changegroup already contains a change for the same row (identified by PRIMARY KEY columns), then the current change is combined with the existing change in the same way as for sqlite3changegroup_add().

For a patchset, all of the above rules apply except that it doesn't matter whether or not values are provided for the non-PK old.\* record columns for an UPDATE or DELETE change. This means that code used to produce a changeset using the sqlite3changegroup_change_xxx() APIs may also be used to produce patchsets.

If the call is successful, SQLITE_OK is returned. Otherwise, if an error occurs, an SQLite error code is returned. If an error is returned and parameter pzErr is not NULL, then (\*pzErr) may be set to point to a buffer containing a nul-terminated, utf-8 encoded, English language error message. It is the responsibility of the caller to eventually free any such error message buffer using sqlite3_free().

See also lists of [Objects](../session/objlist.md), [Constants](../session/constlist.md), and [Functions](../session/funclist.md).
