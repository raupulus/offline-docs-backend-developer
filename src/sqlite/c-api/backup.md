---
title: Online Backup Object
source_url: https://www.sqlite.org/c3ref/backup.html
source_path: c3ref/backup.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 250
---

> \
> typedef struct sqlite3_backup sqlite3_backup;\

The sqlite3_backup object records state information about an ongoing online backup operation. The sqlite3_backup object is created by a call to [sqlite3_backup_init()](../c3ref/backup_finish.md#sqlite3backupinit) and is destroyed by a call to [sqlite3_backup_finish()](../c3ref/backup_finish.md#sqlite3backupfinish).

See Also: [Using the SQLite Online Backup API](../backup.md)

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
