---
title: Flags for the xShmLock VFS method
source_url: https://www.sqlite.org/c3ref/c_shm_exclusive.html
source_path: c3ref/c_shm_exclusive.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 690
---

> \
> \#define SQLITE_SHM_UNLOCK       1\
> \#define SQLITE_SHM_LOCK         2\
> \#define SQLITE_SHM_SHARED       4\
> \#define SQLITE_SHM_EXCLUSIVE    8\

These integer constants define the various locking operations allowed by the xShmLock method of [sqlite3_io_methods](../c3ref/io_methods.md). The following are the only legal combinations of flags to the xShmLock method:

- SQLITE_SHM_LOCK \| SQLITE_SHM_SHARED
- SQLITE_SHM_LOCK \| SQLITE_SHM_EXCLUSIVE
- SQLITE_SHM_UNLOCK \| SQLITE_SHM_SHARED
- SQLITE_SHM_UNLOCK \| SQLITE_SHM_EXCLUSIVE

When unlocking, the same SHARED or EXCLUSIVE flag must be supplied as was given on the corresponding lock.

The xShmLock method can transition between unlocked and SHARED or between unlocked and EXCLUSIVE. It cannot transition between SHARED and EXCLUSIVE.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
