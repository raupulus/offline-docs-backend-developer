---
title: Closing A Database Connection
source_url: https://www.sqlite.org/c3ref/close.html
source_path: c3ref/close.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 840
---

> \
> int sqlite3_close(sqlite3\*);\
> int sqlite3_close_v2(sqlite3\*);\

The sqlite3_close() and sqlite3_close_v2() routines are destructors for the [sqlite3](../c3ref/sqlite3.md) object. Calls to sqlite3_close() and sqlite3_close_v2() return [SQLITE_OK](../rescode.md#ok) if the [sqlite3](../c3ref/sqlite3.md) object is successfully destroyed and all associated resources are deallocated.

Ideally, applications should [finalize](../c3ref/finalize.md) all [prepared statements](../c3ref/stmt.md), [close](../c3ref/blob_close.md) all [BLOB handles](../c3ref/blob.md), and [finish](../c3ref/backup_finish.md#sqlite3backupfinish) all [sqlite3_backup](../c3ref/backup.md) objects associated with the [sqlite3](../c3ref/sqlite3.md) object prior to attempting to close the object. If the database connection is associated with unfinalized prepared statements, BLOB handlers, and/or unfinished sqlite3_backup objects then sqlite3_close() will leave the database connection open and return [SQLITE_BUSY](../rescode.md#busy). If sqlite3_close_v2() is called with unfinalized prepared statements, unclosed BLOB handlers, and/or unfinished sqlite3_backups, it returns [SQLITE_OK](../rescode.md#ok) regardless, but instead of deallocating the database connection immediately, it marks the database connection as an unusable "zombie" and makes arrangements to automatically deallocate the database connection after all prepared statements are finalized, all BLOB handles are closed, and all backups have finished. The sqlite3_close_v2() interface is intended for use with host languages that are garbage collected, and where the order in which destructors are called is arbitrary.

If an [sqlite3](../c3ref/sqlite3.md) object is destroyed while a transaction is open, the transaction is automatically rolled back.

The C parameter to [sqlite3_close(C)](../c3ref/close.md) and [sqlite3_close_v2(C)](../c3ref/close.md) must be either a NULL pointer or an [sqlite3](../c3ref/sqlite3.md) object pointer obtained from [sqlite3_open()](../c3ref/open.md), [sqlite3_open16()](../c3ref/open.md), or [sqlite3_open_v2()](../c3ref/open.md), and not previously closed. Calling sqlite3_close() or sqlite3_close_v2() with a NULL pointer argument is a harmless no-op.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
