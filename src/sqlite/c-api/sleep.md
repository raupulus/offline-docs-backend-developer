---
title: Suspend Execution For A Short Time
source_url: https://www.sqlite.org/c3ref/sleep.html
source_path: c3ref/sleep.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1780
---

> \
> int sqlite3_sleep(int);\

The sqlite3_sleep() function causes the current thread to suspend execution for at least a number of milliseconds specified in its parameter.

If the operating system does not support sleep requests with millisecond time resolution, then the time will be rounded up to the nearest second. The number of milliseconds of sleep actually requested from the operating system is returned.

SQLite implements this interface by calling the xSleep() method of the default [sqlite3_vfs](../c3ref/vfs.md) object. If the xSleep() method of the default VFS is not implemented correctly, or not implemented at all, then the behavior of sqlite3_sleep() may deviate from the description in the previous paragraphs.

If a negative argument is passed to sqlite3_sleep() the results vary by VFS and operating system. Some system treat a negative argument as an instruction to sleep forever. Others understand it to mean do not sleep at all. In SQLite version 3.42.0 and later, a negative argument passed into sqlite3_sleep() is changed to zero before it is relayed down into the xSleep method of the VFS.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
