---
title: Synchronization Type Flags
source_url: https://www.sqlite.org/c3ref/c_sync_dataonly.html
source_path: c3ref/c_sync_dataonly.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 740
---

> \
> \#define SQLITE_SYNC_NORMAL        0x00002\
> \#define SQLITE_SYNC_FULL          0x00003\
> \#define SQLITE_SYNC_DATAONLY      0x00010\

When SQLite invokes the xSync() method of an [sqlite3_io_methods](../c3ref/io_methods.md) object it uses a combination of these integer values as the second argument.

When the SQLITE_SYNC_DATAONLY flag is used, it means that the sync operation only needs to flush data to mass storage. Inode information need not be flushed. If the lower four bits of the flag equal SQLITE_SYNC_NORMAL, that means to use normal fsync() semantics. If the lower four bits equal SQLITE_SYNC_FULL, that means to use Mac OS X style fullsync instead of fsync().

Do not confuse the SQLITE_SYNC_NORMAL and SQLITE_SYNC_FULL flags with the [PRAGMA synchronous](../pragma.md#pragma_synchronous)=NORMAL and [PRAGMA synchronous](../pragma.md#pragma_synchronous)=FULL settings. The [synchronous pragma](../pragma.md#pragma_synchronous) determines when calls to the xSync VFS method occur and applies uniformly across all platforms. The SQLITE_SYNC_NORMAL and SQLITE_SYNC_FULL flags determine how energetic or rigorous or forceful the sync operations are and only make a difference on Mac OSX for the default SQLite code. (Third-party VFS implementations might also make the distinction between SQLITE_SYNC_NORMAL and SQLITE_SYNC_FULL, but among the operating systems natively supported by SQLite, only Mac OSX cares about the difference.)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
