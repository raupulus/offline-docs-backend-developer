---
title: Maximum xShmLock index
source_url: https://www.sqlite.org/c3ref/c_shm_nlock.html
source_path: c3ref/c_shm_nlock.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 700
---

> \
> \#define SQLITE_SHM_NLOCK        8\

The xShmLock method on [sqlite3_io_methods](../c3ref/io_methods.md) may use values between 0 and this upper bound as its "offset" argument. The SQLite core will never attempt to acquire or release a lock outside of this range

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
