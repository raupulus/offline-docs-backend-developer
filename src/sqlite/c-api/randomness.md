---
title: Pseudo-Random Number Generator
source_url: https://www.sqlite.org/c3ref/randomness.html
source_path: c3ref/randomness.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1670
---

> \
> void sqlite3_randomness(int N, void \*P);\

SQLite contains a high-quality pseudo-random number generator (PRNG) used to select random [ROWIDs](../lang_createtable.md#rowid) when inserting new records into a table that already uses the largest possible [ROWID](../lang_createtable.md#rowid). The PRNG is also used for the built-in random() and randomblob() SQL functions. This interface allows applications to access the same PRNG for other purposes.

A call to this routine stores N bytes of randomness into buffer P. The P parameter can be a NULL pointer.

If this routine has not been previously called or if the previous call had N less than one or a NULL pointer for P, then the PRNG is seeded using randomness obtained from the xRandomness method of the default [sqlite3_vfs](../c3ref/vfs.md) object. If the previous call to this routine had an N of 1 or more and a non-NULL P then the pseudo-randomness is generated internally and without recourse to the [sqlite3_vfs](../c3ref/vfs.md) xRandomness method.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
