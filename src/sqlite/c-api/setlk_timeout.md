---
title: Set the Setlk Timeout
source_url: https://www.sqlite.org/c3ref/setlk_timeout.html
source_path: c3ref/setlk_timeout.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1770
---

> \
> int sqlite3_setlk_timeout(sqlite3\*, int ms, int flags);\

This routine is only useful in SQLITE_ENABLE_SETLK_TIMEOUT builds. If the VFS supports blocking locks, it sets the timeout in ms used by eligible locks taken on wal mode databases by the specified database handle. In non-SQLITE_ENABLE_SETLK_TIMEOUT builds, or if the VFS does not support blocking locks, this function is a no-op.

Passing 0 to this function disables blocking locks altogether. Passing -1 to this function requests that the VFS blocks for a long time - indefinitely if possible. The results of passing any other negative value are undefined.

Internally, each SQLite database handle stores two timeout values - the busy-timeout (used for rollback mode databases, or if the VFS does not support blocking locks) and the setlk-timeout (used for blocking locks on wal-mode databases). The sqlite3_busy_timeout() method sets both values, this function sets only the setlk-timeout value. Therefore, to configure separate busy-timeout and setlk-timeout values for a single database handle, call sqlite3_busy_timeout() followed by this function.

Whenever the number of connections to a wal mode database falls from 1 to 0, the last connection takes an exclusive lock on the database, then checkpoints and deletes the wal file. While it is doing this, any new connection that tries to read from the database fails with an SQLITE_BUSY error. Or, if the SQLITE_SETLK_BLOCK_ON_CONNECT flag is passed to this API, the new connection blocks until the exclusive lock has been released.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
