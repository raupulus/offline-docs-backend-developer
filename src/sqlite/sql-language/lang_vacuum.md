---
title: VACUUM
source_url: https://www.sqlite.org/lang_vacuum.html
source_path: lang_vacuum.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: sql-language
order: 3470
---

# 1. Syntax

**[vacuum-stmt:](syntax/vacuum-stmt.md)** hide

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSJmb250LXNpemU6aW5pdGlhbDsiIGNsYXNzPSJwaWtjaHIiIHZpZXdib3g9IjAgMCA1OTkuNjY5IDY0LjgiIGRhdGEtcGlrY2hyLWRhdGU9IjIwMjUwMzE5MTYxOTQzIj4KPGNpcmNsZSBjeD0iNS43NiIgY3k9IjE3LjI4IiByPSIzLjYiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7Ij48L2NpcmNsZT4KPHBvbHlnb24gcG9pbnRzPSIzMi40LDE3LjI4IDIwLjg4LDIxLjYgMjAuODgsMTIuOTYiIHN0eWxlPSJmaWxsOnJnYigwLDAsMCkiPjwvcG9seWdvbj4KPHBhdGggZD0iTTkuMzYsMTcuMjhMMjYuNjQsMTcuMjgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cGF0aCBkPSJNNDcuNTIsMzIuNEwxMDguODY0LDMyLjRBMTUuMTIgMTUuMTIgMCAwIDAgMTIzLjk4NCAxNy4yOEExNS4xMiAxNS4xMiAwIDAgMCAxMDguODY0IDIuMTZMNDcuNTIsMi4xNkExNS4xMiAxNS4xMiAwIDAgMCAzMi40IDE3LjI4QTE1LjEyIDE1LjEyIDAgMCAwIDQ3LjUyIDMyLjRaIiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHRleHQgeD0iNzguMTkyIiB5PSIxNy4yOCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0icmdiKDAsMCwwKSIgZG9taW5hbnQtYmFzZWxpbmU9ImNlbnRyYWwiPlZBQ1VVTTwvdGV4dD4KPHBvbHlnb24gcG9pbnRzPSIxNjUuNTA0LDQ3LjUyIDE1My45ODQsNTEuODQgMTUzLjk4NCw0My4yIiBzdHlsZT0iZmlsbDpyZ2IoMCwwLDApIj48L3BvbHlnb24+CjxwYXRoIGQ9Ik0xMjMuOTg0LDE3LjI4IEwgMTMxLjQ4NCwxNy4yOCBRIDEzOC45ODQsMTcuMjggMTM4Ljk4NCwzMi4yOCBMIDEzOC45ODQsMzIuNTIgUSAxMzguOTg0LDQ3LjUyIDE0OS4zNjQsNDcuNTIgTCAxNTkuNzQ0LDQ3LjUyIiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHBhdGggZD0iTTE4MC42MjQsNjIuNjRMMjc2Ljk4OSw2Mi42NEExNS4xMiAxNS4xMiAwIDAgMCAyOTIuMTA5IDQ3LjUyTDI5Mi4xMDksNDcuNTJBMTUuMTIgMTUuMTIgMCAwIDAgMjc2Ljk4OSAzMi40TDE4MC42MjQsMzIuNEExNS4xMiAxNS4xMiAwIDAgMCAxNjUuNTA0IDQ3LjUyTDE2NS41MDQsNDcuNTJBMTUuMTIgMTUuMTIgMCAwIDAgMTgwLjYyNCA2Mi42NFoiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8dGV4dCB4PSIyMjguODA2IiB5PSI0Ny41MiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0icmdiKDAsMCwwKSIgZG9taW5hbnQtYmFzZWxpbmU9ImNlbnRyYWwiPnNjaGVtYS1uYW1lPC90ZXh0Pgo8cG9seWdvbiBwb2ludHM9IjMzMy42MjksMTcuMjggMzIyLjEwOSwyMS42IDMyMi4xMDksMTIuOTYiIHN0eWxlPSJmaWxsOnJnYigwLDAsMCkiPjwvcG9seWdvbj4KPHBhdGggZD0iTTI5Mi4xMDksNDcuNTIgTCAyOTkuNjA5LDQ3LjUyIFEgMzA3LjEwOSw0Ny41MiAzMDcuMTA5LDMyLjUyIEwgMzA3LjEwOSwzMi4yOCBRIDMwNy4xMDksMTcuMjggMzE3LjQ4OSwxNy4yOCBMIDMyNy44NjksMTcuMjgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cG9seWdvbiBwb2ludHM9IjM3NS4xNDksNDcuNTIgMzYzLjYyOSw1MS44NCAzNjMuNjI5LDQzLjIiIHN0eWxlPSJmaWxsOnJnYigwLDAsMCkiPjwvcG9seWdvbj4KPHBhdGggZD0iTTMzMy42MjksMTcuMjggTCAzNDEuMTI5LDE3LjI4IFEgMzQ4LjYyOSwxNy4yOCAzNDguNjI5LDMyLjI4IEwgMzQ4LjYyOSwzMi41MiBRIDM0OC42MjksNDcuNTIgMzU5LjAwOSw0Ny41MiBMIDM2OS4zODksNDcuNTIiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cGF0aCBkPSJNMzkwLjI2OSw2Mi42NEw0MTcuMDUzLDYyLjY0QTE1LjEyIDE1LjEyIDAgMCAwIDQzMi4xNzMgNDcuNTJMNDMyLjE3Myw0Ny41MkExNS4xMiAxNS4xMiAwIDAgMCA0MTcuMDUzIDMyLjRMMzkwLjI2OSwzMi40QTE1LjEyIDE1LjEyIDAgMCAwIDM3NS4xNDkgNDcuNTJMMzc1LjE0OSw0Ny41MkExNS4xMiAxNS4xMiAwIDAgMCAzOTAuMjY5IDYyLjY0WiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+Cjx0ZXh0IHg9IjQwMy42NjEiIHk9IjQ3LjUyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSJyZ2IoMCwwLDApIiBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCI+SU5UTzwvdGV4dD4KPHBvbHlnb24gcG9pbnRzPSI0NTUuMjEzLDQ3LjUyIDQ0My42OTMsNTEuODQgNDQzLjY5Myw0My4yIiBzdHlsZT0iZmlsbDpyZ2IoMCwwLDApIj48L3BvbHlnb24+CjxwYXRoIGQ9Ik00MzIuMTczLDQ3LjUyTDQ0OS40NTMsNDcuNTIiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cGF0aCBkPSJNNDcwLjMzMyw2Mi42NEw1MjQuMTg5LDYyLjY0QTE1LjEyIDE1LjEyIDAgMCAwIDUzOS4zMDkgNDcuNTJMNTM5LjMwOSw0Ny41MkExNS4xMiAxNS4xMiAwIDAgMCA1MjQuMTg5IDMyLjRMNDcwLjMzMywzMi40QTE1LjEyIDE1LjEyIDAgMCAwIDQ1NS4yMTMgNDcuNTJMNDU1LjIxMyw0Ny41MkExNS4xMiAxNS4xMiAwIDAgMCA0NzAuMzMzIDYyLjY0WiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+Cjx0ZXh0IHg9IjQ5Ny4yNjEiIHk9IjQ3LjUyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSJyZ2IoMCwwLDApIiBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCI+ZmlsZW5hbWU8L3RleHQ+Cjxwb2x5Z29uIHBvaW50cz0iNTkwLjMwOSwxNy4yOCA1NzguNzg5LDIxLjYgNTc4Ljc4OSwxMi45NiIgc3R5bGU9ImZpbGw6cmdiKDAsMCwwKSI+PC9wb2x5Z29uPgo8cGF0aCBkPSJNNTM5LjMwOSw0Ny41MiBMIDU0Ni44MDksNDcuNTIgUSA1NTQuMzA5LDQ3LjUyIDU1NC4zMDksMzIuNTIgTCA1NTQuMzA5LDMyLjI4IFEgNTU0LjMwOSwxNy4yOCA1NjkuMzA5LDE3LjI4IEwgNTY5LjU0OSwxNy4yOCBMIDU4NC41NDksMTcuMjgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8Y2lyY2xlIGN4PSI1OTMuOTA5IiBjeT0iMTcuMjgiIHI9IjMuNiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiPjwvY2lyY2xlPgo8cGF0aCBkPSJNMTIzLjk4NCwxNy4yOEw1NzguNzg5LDE3LjI4IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPC9zdmc+" class="pikchr" />

# 2. Description

The VACUUM command rebuilds the database file, repacking it into a minimal amount of disk space. There are several reasons an application might do this:

- Unless SQLite is running in "auto_vacuum=FULL" mode, when a large amount of data is deleted from the database file it leaves behind empty space, or "free" database pages. This means the database file might be larger than strictly necessary. Running VACUUM to rebuild the database reclaims this space and reduces the size of the database file.

- Frequent inserts, updates, and deletes can cause the database file to become fragmented - where data for a single table or index is scattered around the database file. Running VACUUM ensures that each table and index is largely stored contiguously within the database file. In some cases, VACUUM may also reduce the number of partially filled pages in the database, reducing the size of the database file further.

- When content is deleted from an SQLite database, the content is not usually erased but rather the space used to hold the content is marked as being available for reuse. This can allow deleted content to be recovered by a hacker or by forensic analysis. Running VACUUM will clean the database of all traces of deleted content, thus preventing an adversary from recovering deleted content. Using VACUUM in this way is an alternative to setting [PRAGMA secure_delete=ON](pragma.md#pragma_secure_delete).

- Normally, the database [page_size](pragma.md#pragma_page_size) and whether or not the database supports [auto_vacuum](pragma.md#pragma_auto_vacuum) must be configured before the database file is actually created. However, when not in [write-ahead log](wal.md) mode, the [page_size](pragma.md#pragma_page_size) and/or [auto_vacuum](pragma.md#pragma_auto_vacuum) properties of an existing database may be changed by using the [page_size](pragma.md#pragma_page_size) and/or [pragma auto_vacuum](pragma.md#pragma_auto_vacuum) pragmas and then immediately VACUUMing the database. When in [write-ahead log](wal.md) mode, only the [auto_vacuum](pragma.md#pragma_auto_vacuum) support property can be changed using VACUUM.

By default, VACUUM operates on the main database. [Attached databases](lang_attach.md) can be vacuumed by appending the appropriate <span class="yyterm">schema-name</span> to the VACUUM statement.

**Compatibility Warning:** The ability to vacuum attached databases was added in [version 3.15.0](releaselog/3_15_0.md) (2016-10-14). Prior to that, a <span class="yyterm">schema-name</span> added to the VACUUM statement would be silently ignored and the "main" schema would be vacuumed.

<span id="vacuuminto"></span>

## 2.1. VACUUM with an INTO clause

If the INTO clause is included, then the original database file is unchanged and a new database is created in a file named by the argument to the INTO clause. The argument is a scalar [expression](lang_expr.md), such as a text literal. The new database will contain the same logical content as the original database, fully vacuumed.

The VACUUM command with an INTO clause is an alternative to the [backup API](backup.md) for generating backup copies of a live database. The advantage of using VACUUM INTO is that the resulting backup database is minimal in size and hence the amount of filesystem I/O may be reduced. Also, all deleted content is purged from the backup, leaving behind no forensic traces. On the other hand, the [backup API](backup.md) uses fewer CPU cycles and can be executed incrementally.

The filename in the INTO clause can be an arbitrary SQL expression that evaluates to a string. The file named by the INTO clause must not previously exist, or else it must be an empty file, or the VACUUM INTO command will fail with an error.

The argument to INTO can be a [URI filename](uri.md) if URI filenames are enabled. URL filenames are enabled if any of the following are true:

- The SQLite library was compiled with [-DSQLITE_USE_URI=1](compile.md#use_uri).
- The [sqlite3_config](c3ref/config.md)([SQLITE_CONFIG_URI](c3ref/c_config_covering_index_scan.md#sqliteconfiguri),1) interfaces was invoked at start-time.
- The [database connection](c3ref/sqlite3.md) that is running the VACUUM INTO statement was originally opened using the [SQLITE_OPEN_URI](c3ref/c_open_autoproxy.md) flag.

The VACUUM INTO command is transactional in the sense that the generated output database is a consistent snapshot of the original database. However, if the VACUUM INTO command is interrupted by an unplanned shutdown or power loss, then the generated output database might be incomplete and corrupt.

However, if the [PRAGMA synchronous](pragma.md#pragma_synchronous) setting of the original database is NORMAL or FULL, then SQLite invokes fsync() or FileFlushBuffers() to sync the output database to disk after it has been written. This means that in these cases, a power failure or unplanned shutdown that occurs after the VACUUM INTO command has completed should not corrupt the database (assuming the OS, file-system and hardware are functioning correctly). <span id="howvacuumworks"></span>

# 3. How VACUUM works

The VACUUM command works by copying the contents of the database into a temporary database file and then overwriting the original with the contents of the temporary file. When overwriting the original, a rollback journal or [write-ahead log](wal.md) WAL file is used just as it would be for any other database transaction. This means that when VACUUMing a database, as much as twice the size of the original database file is required in free disk space.

The VACUUM INTO command works the same way except that it uses the file named on the INTO clause in place of the temporary database and omits the step of copying the vacuumed database back over top of the original database.

The VACUUM command may change the [ROWIDs](lang_createtable.md#rowid) of entries in any tables that do not have an explicit [INTEGER PRIMARY KEY](lang_createtable.md#rowid).

A VACUUM will fail if there is an open transaction on the database connection that is attempting to run the VACUUM. Unfinalized SQL statements typically hold a read transaction open, so the VACUUM might fail if there are unfinalized SQL statements on the same connection. VACUUM (but not VACUUM INTO) is a write operation and so if another database connection is holding a lock that prevents writes, then the VACUUM will fail.

An alternative to using the VACUUM command to reclaim space after data has been deleted is auto-vacuum mode, enabled using the [auto_vacuum](pragma.md#pragma_auto_vacuum) pragma. When [auto_vacuum](pragma.md#pragma_auto_vacuum) is enabled for a database free pages may be reclaimed after deleting data, causing the file to shrink, without rebuilding the entire database using VACUUM. However, using [auto_vacuum](pragma.md#pragma_auto_vacuum) can lead to extra database file fragmentation. And [auto_vacuum](pragma.md#pragma_auto_vacuum) does not compact partially filled pages of the database as VACUUM does.
