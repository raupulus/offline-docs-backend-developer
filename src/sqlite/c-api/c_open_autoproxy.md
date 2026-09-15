---
title: Flags For File Open Operations
source_url: https://www.sqlite.org/c3ref/c_open_autoproxy.html
source_path: c3ref/c_open_autoproxy.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 620
---

> \
> \#define SQLITE_OPEN_READONLY         0x00000001  /\* Ok for sqlite3_open_v2() \*/\
> \#define SQLITE_OPEN_READWRITE        0x00000002  /\* Ok for sqlite3_open_v2() \*/\
> \#define SQLITE_OPEN_CREATE           0x00000004  /\* Ok for sqlite3_open_v2() \*/\
> \#define SQLITE_OPEN_DELETEONCLOSE    0x00000008  /\* VFS only \*/\
> \#define SQLITE_OPEN_EXCLUSIVE        0x00000010  /\* VFS only \*/\
> \#define SQLITE_OPEN_AUTOPROXY        0x00000020  /\* VFS only \*/\
> \#define SQLITE_OPEN_URI              0x00000040  /\* Ok for sqlite3_open_v2() \*/\
> \#define SQLITE_OPEN_MEMORY           0x00000080  /\* Ok for sqlite3_open_v2() \*/\
> \#define SQLITE_OPEN_MAIN_DB          0x00000100  /\* VFS only \*/\
> \#define SQLITE_OPEN_TEMP_DB          0x00000200  /\* VFS only \*/\
> \#define SQLITE_OPEN_TRANSIENT_DB     0x00000400  /\* VFS only \*/\
> \#define SQLITE_OPEN_MAIN_JOURNAL     0x00000800  /\* VFS only \*/\
> \#define SQLITE_OPEN_TEMP_JOURNAL     0x00001000  /\* VFS only \*/\
> \#define SQLITE_OPEN_SUBJOURNAL       0x00002000  /\* VFS only \*/\
> \#define SQLITE_OPEN_SUPER_JOURNAL    0x00004000  /\* VFS only \*/\
> \#define SQLITE_OPEN_NOMUTEX          0x00008000  /\* Ok for sqlite3_open_v2() \*/\
> \#define SQLITE_OPEN_FULLMUTEX        0x00010000  /\* Ok for sqlite3_open_v2() \*/\
> \#define SQLITE_OPEN_SHAREDCACHE      0x00020000  /\* Ok for sqlite3_open_v2() \*/\
> \#define SQLITE_OPEN_PRIVATECACHE     0x00040000  /\* Ok for sqlite3_open_v2() \*/\
> \#define SQLITE_OPEN_WAL              0x00080000  /\* VFS only \*/\
> \#define SQLITE_OPEN_NOFOLLOW         0x01000000  /\* Ok for sqlite3_open_v2() \*/\
> \#define SQLITE_OPEN_EXRESCODE        0x02000000  /\* Extended result codes \*/\

These bit values are intended for use in the 3rd parameter to the [sqlite3_open_v2()](../c3ref/open.md) interface and in the 4th parameter to the [sqlite3_vfs.xOpen](../c3ref/vfs.md#sqlite3vfsxopen) method.

Only those flags marked as "Ok for sqlite3_open_v2()" may be used as the third argument to the [sqlite3_open_v2()](../c3ref/open.md) interface. The other flags have historically been ignored by sqlite3_open_v2(), though future versions of SQLite might change so that an error is raised if any of the disallowed bits are passed into sqlite3_open_v2(). Applications should not depend on the historical behavior.

Note in particular that passing the SQLITE_OPEN_EXCLUSIVE flag into [sqlite3_open_v2()](../c3ref/open.md) does \*not\* cause the underlying database file to be opened using O_EXCL. Passing SQLITE_OPEN_EXCLUSIVE into [sqlite3_open_v2()](../c3ref/open.md) has historically been a no-op and might become an error in future versions of SQLite.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
