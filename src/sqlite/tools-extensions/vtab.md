---
title: The Virtual Table Mechanism Of SQLite
source_url: https://www.sqlite.org/vtab.html
source_path: vtab.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: tools-extensions
order: 8260
---

# 1. Introduction

A virtual table is an object that is registered with an open SQLite [database connection](c3ref/sqlite3.md). From the perspective of an SQL statement, the virtual table object looks like any other table or view. But behind the scenes, queries and updates on a virtual table invoke callback methods of the virtual table object instead of reading and writing on the database file.

The virtual table mechanism allows an application to publish interfaces that are accessible from SQL statements as if they were tables. SQL statements can do almost anything to a virtual table that they can do to a real table, with the following exceptions:

- One cannot create a trigger on a virtual table.
- One cannot create additional indices on a virtual table. (Virtual tables can have indices but that must be built into the virtual table implementation. Indices cannot be added separately using [CREATE INDEX](lang_createindex.md) statements.)
- One cannot run [ALTER TABLE ... ADD COLUMN](lang_altertable.md) commands against a virtual table.

Individual virtual table implementations might impose additional constraints. For example, some virtual implementations might provide read-only tables. Or some virtual table implementations might allow [INSERT](lang_insert.md) or [DELETE](lang_delete.md) but not [UPDATE](lang_update.md). Or some virtual table implementations might limit the kinds of UPDATEs that can be made.

A virtual table might represent an in-memory data structure. Or it might represent a view of data on disk that is not in the SQLite format. Or the application might compute the content of the virtual table on demand.

Here are some existing and postulated uses for virtual tables:

- A [full-text search](fts3.md) interface
- Spatial indices using [R-Trees](rtree.md)
- Introspect the disk content of an SQLite database file (the [dbstat virtual table](dbstat.md))
- Read and/or write the content of a comma-separated value (CSV) file
- Access the filesystem of the host computer as if it were a database table
- Enabling SQL manipulation of data in statistics packages like R

See the [list of virtual tables](vtablist.md) page for a longer list of actual virtual table implementations.

## 1.1. Usage

A virtual table is created using a [CREATE VIRTUAL TABLE](lang_createvtab.md) statement.

**[create-virtual-table-stmt:](syntax/create-virtual-table-stmt.md)** hide

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSJmb250LXNpemU6aW5pdGlhbDsiIGNsYXNzPSJwaWtjaHIiIHZpZXdib3g9IjAgMCA2MjQuMDk2IDI1OS44NDgiIGRhdGEtcGlrY2hyLWRhdGU9IjIwMjUwMzE5MTYxOTQzIj4KPGNpcmNsZSBjeD0iNS43NiIgY3k9IjE3LjI4IiByPSIzLjYiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7Ij48L2NpcmNsZT4KPHBvbHlnb24gcG9pbnRzPSIzMi40LDE3LjI4IDIwLjg4LDIxLjYgMjAuODgsMTIuOTYiIHN0eWxlPSJmaWxsOnJnYigwLDAsMCkiPjwvcG9seWdvbj4KPHBhdGggZD0iTTkuMzYsMTcuMjhMMjYuNjQsMTcuMjgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cGF0aCBkPSJNNDcuNTIsMzIuNEwxMDAuOTE1LDMyLjRBMTUuMTIgMTUuMTIgMCAwIDAgMTE2LjAzNSAxNy4yOEExNS4xMiAxNS4xMiAwIDAgMCAxMDAuOTE1IDIuMTZMNDcuNTIsMi4xNkExNS4xMiAxNS4xMiAwIDAgMCAzMi40IDE3LjI4QTE1LjEyIDE1LjEyIDAgMCAwIDQ3LjUyIDMyLjRaIiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHRleHQgeD0iNzQuMjE3NiIgeT0iMTcuMjgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9InJnYigwLDAsMCkiIGRvbWluYW50LWJhc2VsaW5lPSJjZW50cmFsIj5DUkVBVEU8L3RleHQ+Cjxwb2x5Z29uIHBvaW50cz0iMTM5LjA3NSwxNy4yOCAxMjcuNTU1LDIxLjYgMTI3LjU1NSwxMi45NiIgc3R5bGU9ImZpbGw6cmdiKDAsMCwwKSI+PC9wb2x5Z29uPgo8cGF0aCBkPSJNMTE2LjAzNSwxNy4yOEwxMzMuMzE1LDE3LjI4IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHBhdGggZD0iTTE1NC4xOTUsMzIuNEwyMTMuNjk2LDMyLjRBMTUuMTIgMTUuMTIgMCAwIDAgMjI4LjgxNiAxNy4yOEExNS4xMiAxNS4xMiAwIDAgMCAyMTMuNjk2IDIuMTZMMTU0LjE5NSwyLjE2QTE1LjEyIDE1LjEyIDAgMCAwIDEzOS4wNzUgMTcuMjhBMTUuMTIgMTUuMTIgMCAwIDAgMTU0LjE5NSAzMi40WiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+Cjx0ZXh0IHg9IjE4My45NDYiIHk9IjE3LjI4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSJyZ2IoMCwwLDApIiBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCI+VklSVFVBTDwvdGV4dD4KPHBvbHlnb24gcG9pbnRzPSIyNTEuODU2LDE3LjI4IDI0MC4zMzYsMjEuNiAyNDAuMzM2LDEyLjk2IiBzdHlsZT0iZmlsbDpyZ2IoMCwwLDApIj48L3BvbHlnb24+CjxwYXRoIGQ9Ik0yMjguODE2LDE3LjI4TDI0Ni4wOTYsMTcuMjgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cGF0aCBkPSJNMjY2Ljk3NiwzMi40TDMwNi4zMTcsMzIuNEExNS4xMiAxNS4xMiAwIDAgMCAzMjEuNDM3IDE3LjI4QTE1LjEyIDE1LjEyIDAgMCAwIDMwNi4zMTcgMi4xNkwyNjYuOTc2LDIuMTZBMTUuMTIgMTUuMTIgMCAwIDAgMjUxLjg1NiAxNy4yOEExNS4xMiAxNS4xMiAwIDAgMCAyNjYuOTc2IDMyLjRaIiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHRleHQgeD0iMjg2LjY0NiIgeT0iMTcuMjgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9InJnYigwLDAsMCkiIGRvbWluYW50LWJhc2VsaW5lPSJjZW50cmFsIj5UQUJMRTwvdGV4dD4KPHBvbHlnb24gcG9pbnRzPSIzNTcuNDM3LDE3LjI4IDM0NS45MTcsMjEuNiAzNDUuOTE3LDEyLjk2IiBzdHlsZT0iZmlsbDpyZ2IoMCwwLDApIj48L3BvbHlnb24+CjxwYXRoIGQ9Ik0zMjEuNDM3LDE3LjI4TDM1MS42NzcsMTcuMjgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cGF0aCBkPSJNMzcyLjU1NywzMi40QTE1LjEyIDE1LjEyIDAgMCAwIDM4Ny42NzcgMTcuMjhBMTUuMTIgMTUuMTIgMCAwIDAgMzcyLjU1NyAyLjE2QTE1LjEyIDE1LjEyIDAgMCAwIDM1Ny40MzcgMTcuMjhBMTUuMTIgMTUuMTIgMCAwIDAgMzcyLjU1NyAzMi40WiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+Cjx0ZXh0IHg9IjM3Mi41NTciIHk9IjE3LjI4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSJyZ2IoMCwwLDApIiBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCI+SUY8L3RleHQ+Cjxwb2x5Z29uIHBvaW50cz0iNDEwLjcxNywxNy4yOCAzOTkuMTk3LDIxLjYgMzk5LjE5NywxMi45NiIgc3R5bGU9ImZpbGw6cmdiKDAsMCwwKSI+PC9wb2x5Z29uPgo8cGF0aCBkPSJNMzg3LjY3NywxNy4yOEw0MDQuOTU3LDE3LjI4IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHBhdGggZD0iTTQyNS44MzcsMzIuNEw0NDUuOTM5LDMyLjRBMTUuMTIgMTUuMTIgMCAwIDAgNDYxLjA1OSAxNy4yOEExNS4xMiAxNS4xMiAwIDAgMCA0NDUuOTM5IDIuMTZMNDI1LjgzNywyLjE2QTE1LjEyIDE1LjEyIDAgMCAwIDQxMC43MTcgMTcuMjhBMTUuMTIgMTUuMTIgMCAwIDAgNDI1LjgzNyAzMi40WiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+Cjx0ZXh0IHg9IjQzNS44ODgiIHk9IjE3LjI4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSJyZ2IoMCwwLDApIiBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCI+Tk9UPC90ZXh0Pgo8cG9seWdvbiBwb2ludHM9IjQ4NC4wOTksMTcuMjggNDcyLjU3OSwyMS42IDQ3Mi41NzksMTIuOTYiIHN0eWxlPSJmaWxsOnJnYigwLDAsMCkiPjwvcG9seWdvbj4KPHBhdGggZD0iTTQ2MS4wNTksMTcuMjhMNDc4LjMzOSwxNy4yOCIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+CjxwYXRoIGQ9Ik00OTkuMjE5LDMyLjRMNTQzLjg1OSwzMi40QTE1LjEyIDE1LjEyIDAgMCAwIDU1OC45NzkgMTcuMjhBMTUuMTIgMTUuMTIgMCAwIDAgNTQzLjg1OSAyLjE2TDQ5OS4yMTksMi4xNkExNS4xMiAxNS4xMiAwIDAgMCA0ODQuMDk5IDE3LjI4QTE1LjEyIDE1LjEyIDAgMCAwIDQ5OS4yMTkgMzIuNFoiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8dGV4dCB4PSI1MjEuNTM5IiB5PSIxNy4yOCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0icmdiKDAsMCwwKSIgZG9taW5hbnQtYmFzZWxpbmU9ImNlbnRyYWwiPkVYSVNUUzwvdGV4dD4KPHBhdGggZD0iTTQ3LjUyLDEwOEwxNDMuODg1LDEwOEExNS4xMiAxNS4xMiAwIDAgMCAxNTkuMDA1IDkyLjg4QTE1LjEyIDE1LjEyIDAgMCAwIDE0My44ODUgNzcuNzZMNDcuNTIsNzcuNzZBMTUuMTIgMTUuMTIgMCAwIDAgMzIuNCA5Mi44OEExNS4xMiAxNS4xMiAwIDAgMCA0Ny41MiAxMDhaIiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHRleHQgeD0iOTUuNzAyNCIgeT0iOTIuODgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9InJnYigwLDAsMCkiIGRvbWluYW50LWJhc2VsaW5lPSJjZW50cmFsIj5zY2hlbWEtbmFtZTwvdGV4dD4KPHBvbHlnb24gcG9pbnRzPSIxODIuMDQ1LDkyLjg4IDE3MC41MjUsOTcuMiAxNzAuNTI1LDg4LjU2IiBzdHlsZT0iZmlsbDpyZ2IoMCwwLDApIj48L3BvbHlnb24+CjxwYXRoIGQ9Ik0xNTkuMDA1LDkyLjg4TDE3Ni4yODUsOTIuODgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cGF0aCBkPSJNMTk3LjE2NSwxMDhBMTUuMTIgMTUuMTIgMCAwIDAgMjEyLjI4NSA5Mi44OEExNS4xMiAxNS4xMiAwIDAgMCAxOTcuMTY1IDc3Ljc2QTE1LjEyIDE1LjEyIDAgMCAwIDE4Mi4wNDUgOTIuODhBMTUuMTIgMTUuMTIgMCAwIDAgMTk3LjE2NSAxMDhaIiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHRleHQgeD0iMTk3LjE2NSIgeT0iOTIuODgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSJyZ2IoMCwwLDApIiBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCI+LjwvdGV4dD4KPHBvbHlnb24gcG9pbnRzPSIyNDguMjg1LDkyLjg4IDIzNi43NjUsOTcuMiAyMzYuNzY1LDg4LjU2IiBzdHlsZT0iZmlsbDpyZ2IoMCwwLDApIj48L3BvbHlnb24+CjxwYXRoIGQ9Ik0yMTIuMjg1LDkyLjg4TDI0Mi41MjUsOTIuODgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cGF0aCBkPSJNMjYzLjQwNSwxMDhMMzM4LjU3MywxMDhBMTUuMTIgMTUuMTIgMCAwIDAgMzUzLjY5MyA5Mi44OEExNS4xMiAxNS4xMiAwIDAgMCAzMzguNTczIDc3Ljc2TDI2My40MDUsNzcuNzZBMTUuMTIgMTUuMTIgMCAwIDAgMjQ4LjI4NSA5Mi44OEExNS4xMiAxNS4xMiAwIDAgMCAyNjMuNDA1IDEwOFoiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8dGV4dCB4PSIzMDAuOTg5IiB5PSI5Mi44OCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0icmdiKDAsMCwwKSIgZG9taW5hbnQtYmFzZWxpbmU9ImNlbnRyYWwiPnRhYmxlLW5hbWU8L3RleHQ+CjxwYXRoIGQ9Ik00Ny41MiwyMTkuODg4TDg2LjUxNTIsMjE5Ljg4OEExNS4xMiAxNS4xMiAwIDAgMCAxMDEuNjM1IDIwNC43NjhBMTUuMTIgMTUuMTIgMCAwIDAgODYuNTE1MiAxODkuNjQ4TDQ3LjUyLDE4OS42NDhBMTUuMTIgMTUuMTIgMCAwIDAgMzIuNCAyMDQuNzY4QTE1LjEyIDE1LjEyIDAgMCAwIDQ3LjUyIDIxOS44ODhaIiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHRleHQgeD0iNjcuMDE3NiIgeT0iMjA0Ljc2OCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0icmdiKDAsMCwwKSIgZG9taW5hbnQtYmFzZWxpbmU9ImNlbnRyYWwiPlVTSU5HPC90ZXh0Pgo8cG9seWdvbiBwb2ludHM9IjEyNC42NzUsMjA0Ljc2OCAxMTMuMTU1LDIwOS4wODggMTEzLjE1NSwyMDAuNDQ4IiBzdHlsZT0iZmlsbDpyZ2IoMCwwLDApIj48L3BvbHlnb24+CjxwYXRoIGQ9Ik0xMDEuNjM1LDIwNC43NjhMMTE4LjkxNSwyMDQuNzY4IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHBhdGggZD0iTTEzOS43OTUsMjE5Ljg4OEwyMzQuNDMyLDIxOS44ODhBMTUuMTIgMTUuMTIgMCAwIDAgMjQ5LjU1MiAyMDQuNzY4QTE1LjEyIDE1LjEyIDAgMCAwIDIzNC40MzIgMTg5LjY0OEwxMzkuNzk1LDE4OS42NDhBMTUuMTIgMTUuMTIgMCAwIDAgMTI0LjY3NSAyMDQuNzY4QTE1LjEyIDE1LjEyIDAgMCAwIDEzOS43OTUgMjE5Ljg4OFoiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8dGV4dCB4PSIxODcuMTE0IiB5PSIyMDQuNzY4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSJyZ2IoMCwwLDApIiBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCI+bW9kdWxlLW5hbWU8L3RleHQ+Cjxwb2x5Z29uIHBvaW50cz0iMjg1LjU1MiwyMDQuNzY4IDI3NC4wMzIsMjA5LjA4OCAyNzQuMDMyLDIwMC40NDgiIHN0eWxlPSJmaWxsOnJnYigwLDAsMCkiPjwvcG9seWdvbj4KPHBhdGggZD0iTTI0OS41NTIsMjA0Ljc2OEwyNzkuNzkyLDIwNC43NjgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cGF0aCBkPSJNMzAwLjY3MiwyMTkuODg4QTE1LjEyIDE1LjEyIDAgMCAwIDMxNS43OTIgMjA0Ljc2OEExNS4xMiAxNS4xMiAwIDAgMCAzMDAuNjcyIDE4OS42NDhBMTUuMTIgMTUuMTIgMCAwIDAgMjg1LjU1MiAyMDQuNzY4QTE1LjEyIDE1LjEyIDAgMCAwIDMwMC42NzIgMjE5Ljg4OFoiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8dGV4dCB4PSIzMDAuNjcyIiB5PSIyMDQuNzY4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0icmdiKDAsMCwwKSIgZG9taW5hbnQtYmFzZWxpbmU9ImNlbnRyYWwiPig8L3RleHQ+Cjxwb2x5Z29uIHBvaW50cz0iMzUxLjc5MiwyMDQuNzY4IDM0MC4yNzIsMjA5LjA4OCAzNDAuMjcyLDIwMC40NDgiIHN0eWxlPSJmaWxsOnJnYigwLDAsMCkiPjwvcG9seWdvbj4KPHBhdGggZD0iTTMxNS43OTIsMjA0Ljc2OEwzNDYuMDMyLDIwNC43NjgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cGF0aCBkPSJNMzY2LjkxMiwyMTkuODg4TDQ5Ny4zNzYsMjE5Ljg4OEExNS4xMiAxNS4xMiAwIDAgMCA1MTIuNDk2IDIwNC43NjhBMTUuMTIgMTUuMTIgMCAwIDAgNDk3LjM3NiAxODkuNjQ4TDM2Ni45MTIsMTg5LjY0OEExNS4xMiAxNS4xMiAwIDAgMCAzNTEuNzkyIDIwNC43NjhBMTUuMTIgMTUuMTIgMCAwIDAgMzY2LjkxMiAyMTkuODg4WiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+Cjx0ZXh0IHg9IjQzMi4xNDQiIHk9IjIwNC43NjgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9InJnYigwLDAsMCkiIGRvbWluYW50LWJhc2VsaW5lPSJjZW50cmFsIj5tb2R1bGUtYXJndW1lbnQ8L3RleHQ+Cjxwb2x5Z29uIHBvaW50cz0iNTQ4LjQ5NiwyMDQuNzY4IDUzNi45NzYsMjA5LjA4OCA1MzYuOTc2LDIwMC40NDgiIHN0eWxlPSJmaWxsOnJnYigwLDAsMCkiPjwvcG9seWdvbj4KPHBhdGggZD0iTTUxMi40OTYsMjA0Ljc2OEw1NDIuNzM2LDIwNC43NjgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cGF0aCBkPSJNNTYzLjYxNiwyMTkuODg4QTE1LjEyIDE1LjEyIDAgMCAwIDU3OC43MzYgMjA0Ljc2OEExNS4xMiAxNS4xMiAwIDAgMCA1NjMuNjE2IDE4OS42NDhBMTUuMTIgMTUuMTIgMCAwIDAgNTQ4LjQ5NiAyMDQuNzY4QTE1LjEyIDE1LjEyIDAgMCAwIDU2My42MTYgMjE5Ljg4OFoiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8dGV4dCB4PSI1NjMuNjE2IiB5PSIyMDQuNzY4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0icmdiKDAsMCwwKSIgZG9taW5hbnQtYmFzZWxpbmU9ImNlbnRyYWwiPik8L3RleHQ+Cjxwb2x5Z29uIHBvaW50cz0iNjE0LjczNiwyMDQuNzY4IDYwMy4yMTYsMjA5LjA4OCA2MDMuMjE2LDIwMC40NDgiIHN0eWxlPSJmaWxsOnJnYigwLDAsMCkiPjwvcG9seWdvbj4KPHBhdGggZD0iTTU3OC43MzYsMjA0Ljc2OEw2MDguOTc2LDIwNC43NjgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8Y2lyY2xlIGN4PSI2MTguMzM2IiBjeT0iMjA0Ljc2OCIgcj0iMy42IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyI+PC9jaXJjbGU+CjxwYXRoIGQ9Ik00MzIuMTQ0LDI1Ny42ODhBMTUuMTIgMTUuMTIgMCAwIDAgNDQ3LjI2NCAyNDIuNTY4QTE1LjEyIDE1LjEyIDAgMCAwIDQzMi4xNDQgMjI3LjQ0OEExNS4xMiAxNS4xMiAwIDAgMCA0MTcuMDI0IDI0Mi41NjhBMTUuMTIgMTUuMTIgMCAwIDAgNDMyLjE0NCAyNTcuNjg4WiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+Cjx0ZXh0IHg9IjQzMi4xNDQiIHk9IjI0Mi41NjgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSJyZ2IoMCwwLDApIiBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCI+LDwvdGV4dD4KPHBvbHlnb24gcG9pbnRzPSI0NDcuMjY0LDI0Mi41NjggNDU4Ljc4NCwyMzguMjQ4IDQ1OC43ODQsMjQ2Ljg4OCIgc3R5bGU9ImZpbGw6cmdiKDAsMCwwKSI+PC9wb2x5Z29uPgo8cGF0aCBkPSJNNTEyLjQ5NiwyMDQuNzY4IEwgNTE5Ljk5NiwyMDQuNzY4IFEgNTI3LjQ5NiwyMDQuNzY4IDUyNy40OTYsMjE5Ljc2OCBMIDUyNy40OTYsMjI3LjU2OCBRIDUyNy40OTYsMjQyLjU2OCA1MTIuNDk2LDI0Mi41NjggTCA0NjguMDI0LDI0Mi41NjggTCA0NTMuMDI0LDI0Mi41NjgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cGF0aCBkPSJNNDE3LjAyNCwyNDIuNTY4IEwgMzQzLjc1MiwyNDIuNTY4IFEgMzI4Ljc1MiwyNDIuNTY4IDMyOC43NTIsMjI3LjU2OCBMIDMyOC43NTIsMjE5Ljc2OCBRIDMyOC43NTIsMjA0Ljc2OCAzMzYuMjUyLDIwNC43NjggTCAzNDMuNzUyLDIwNC43NjgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cG9seWdvbiBwb2ludHM9IjQzMi4xNDQsMTgwLjU3NiA0MjAuNjI0LDE4NC44OTYgNDIwLjYyNCwxNzYuMjU2IiBzdHlsZT0iZmlsbDpyZ2IoMCwwLDApIj48L3BvbHlnb24+CjxwYXRoIGQ9Ik0yNDkuNTUyLDIwNC43NjggTCAyNTcuMDUyLDIwNC43NjggUSAyNjQuNTUyLDIwNC43NjggMjY0LjU1MiwxOTIuNjcyIFEgMjY0LjU1MiwxODAuNTc2IDI3OS41NTIsMTgwLjU3NiBMIDQxMS4zODQsMTgwLjU3NiBMIDQyNi4zODQsMTgwLjU3NiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+CjxwYXRoIGQ9Ik00MzIuMTQ0LDE4MC41NzYgTCA1NzYuNjk2LDE4MC41NzYgUSA1OTEuNjk2LDE4MC41NzYgNTkxLjY5NiwxOTIuNjcyIFEgNTkxLjY5NiwyMDQuNzY4IDU5OS4xOTYsMjA0Ljc2OCBMIDYwNi42OTYsMjA0Ljc2OCIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+Cjxwb2x5Z29uIHBvaW50cz0iMTg3LjExNCwxNTMuMzYgMTk4LjYzNCwxNDkuMDQgMTk4LjYzNCwxNTcuNjgiIHN0eWxlPSJmaWxsOnJnYigwLDAsMCkiPjwvcG9seWdvbj4KPHBhdGggZD0iTTM1My42OTMsOTIuODggTCAzNjEuMTkzLDkyLjg4IFEgMzY4LjY5Myw5Mi44OCAzNjguNjkzLDEwNy44OCBMIDM2OC42OTMsMTM4LjM2IFEgMzY4LjY5MywxNTMuMzYgMzUzLjY5MywxNTMuMzYgTCAyMDcuODc0LDE1My4zNiBMIDE5Mi44NzQsMTUzLjM2IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHBvbHlnb24gcG9pbnRzPSIzMi40LDIwNC43NjggMjAuODgsMjA5LjA4OCAyMC44OCwyMDAuNDQ4IiBzdHlsZT0iZmlsbDpyZ2IoMCwwLDApIj48L3BvbHlnb24+CjxwYXRoIGQ9Ik0xODcuMTE0LDE1My4zNiBMIDIwLjc2LDE1My4zNiBRIDUuNzYsMTUzLjM2IDUuNzYsMTY4LjM2IEwgNS43NiwxODkuNzY4IFEgNS43NiwyMDQuNzY4IDE2LjIsMjA0Ljc2OCBMIDI2LjY0LDIwNC43NjgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cG9seWdvbiBwb2ludHM9IjQyOS45NzksNjIuNjQgNDQxLjQ5OSw1OC4zMiA0NDEuNDk5LDY2Ljk2IiBzdHlsZT0iZmlsbDpyZ2IoMCwwLDApIj48L3BvbHlnb24+CjxwYXRoIGQ9Ik01NTguOTc5LDE3LjI4IEwgNTY2LjQ3OSwxNy4yOCBRIDU3My45NzksMTcuMjggNTczLjk3OSwzMi4yOCBMIDU3My45NzksNDcuNjQgUSA1NzMuOTc5LDYyLjY0IDU1OC45NzksNjIuNjQgTCA0NTAuNzM5LDYyLjY0IEwgNDM1LjczOSw2Mi42NCIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+Cjxwb2x5Z29uIHBvaW50cz0iMzIuNCw5Mi44OCAyMC44OCw5Ny4yIDIwLjg4LDg4LjU2IiBzdHlsZT0iZmlsbDpyZ2IoMCwwLDApIj48L3BvbHlnb24+CjxwYXRoIGQ9Ik00MjkuOTc5LDYyLjY0IEwgMjAuNzYsNjIuNjQgUSA1Ljc2LDYyLjY0IDUuNzYsNzcuNjQgTCA1Ljc2LDc3Ljg4IFEgNS43Niw5Mi44OCAxNi4yLDkyLjg4IEwgMjYuNjQsOTIuODgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cG9seWdvbiBwb2ludHM9IjMzNi40MzcsNDcuMjggMzMyLjExNywzNS43NiAzNDAuNzU3LDM1Ljc2IiBzdHlsZT0iZmlsbDpyZ2IoMCwwLDApIj48L3BvbHlnb24+CjxwYXRoIGQ9Ik0zMjEuNDM3LDE3LjI4IEwgMzI4LjkzNywxNy4yOCBRIDMzNi40MzcsMTcuMjggMzM2LjQzNywyOS40IEwgMzM2LjQzNyw0MS41MiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+CjxwYXRoIGQ9Ik0zMzYuNDM3LDQ3LjI4IEwgMzM2LjQzNyw1NC45NiBRIDMzNi40MzcsNjIuNjQgMzI4LjkzNyw2Mi42NCBMIDMyMS40MzcsNjIuNjQiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cG9seWdvbiBwb2ludHM9Ijk1LjcwMjQsMTIzLjEyIDg0LjE4MjQsMTI3LjQ0IDg0LjE4MjQsMTE4LjgiIHN0eWxlPSJmaWxsOnJnYigwLDAsMCkiPjwvcG9seWdvbj4KPHBhdGggZD0iTTUuNzYsNzcuNzYgTCA1Ljc2LDEwOC4xMiBRIDUuNzYsMTIzLjEyIDIwLjc2LDEyMy4xMiBMIDc0Ljk0MjQsMTIzLjEyIEwgODkuOTQyNCwxMjMuMTIiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cGF0aCBkPSJNOTUuNzAyNCwxMjMuMTIgTCAyMTAuMjQ1LDEyMy4xMiBRIDIyNS4yNDUsMTIzLjEyIDIyNS4yNDUsMTA4LjEyIEwgMjI1LjI0NSwxMDcuODggUSAyMjUuMjQ1LDkyLjg4IDIzMS4wMDUsOTIuODggTCAyMzYuNzY1LDkyLjg4IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPC9zdmc+" class="pikchr" />

The CREATE VIRTUAL TABLE statement creates a new table called <span class="yyterm">table-name</span> derived from the class <span class="yyterm">module-name</span>. The <span class="yyterm">module-name</span> is the name that is registered for the virtual table by the [sqlite3_create_module()](c3ref/create_module.md) interface.

CREATE VIRTUAL TABLE tablename USING modulename;\

One can also provide comma-separated arguments to the module following the module name:

CREATE VIRTUAL TABLE tablename USING modulename(arg1, arg2, ...);\

The format of the arguments to the module is very general. Each <span class="yyterm">module-argument</span> may contain keywords, string literals, identifiers, numbers, and punctuation. Each <span class="yyterm">module-argument</span> is passed as written (as text) into the [constructor method](vtab.md#xcreate) of the virtual table implementation when the virtual table is created and that constructor is responsible for parsing and interpreting the arguments. The argument syntax is sufficiently general that a virtual table implementation can, if it wants to, interpret its arguments as [column definitions](lang_createtable.md#tablecoldef) in an ordinary [CREATE TABLE](lang_createtable.md) statement. The implementation could also impose some other interpretation on the arguments.

Once a virtual table has been created, it can be used like any other table with the exceptions noted above and imposed by specific virtual table implementations. A virtual table is destroyed using the ordinary [DROP TABLE](lang_droptable.md) syntax.

### 1.1.1. Temporary virtual tables

There is no "CREATE TEMP VIRTUAL TABLE" statement. To create a temporary virtual table, add the "temp" schema before the virtual table name.

CREATE VIRTUAL TABLE **temp.**tablename USING module(arg1, ...);\

<span id="epovtab"></span>

### 1.1.2. Eponymous virtual tables

Some virtual tables exist automatically in the "main" schema of every database connection in which their module is registered, even without a [CREATE VIRTUAL TABLE](lang_createvtab.md) statement. Such virtual tables are called "eponymous virtual tables". To use an eponymous virtual table, simply use the module name as if it were a table. Eponymous virtual tables exist in the "main" schema only, so they will not work if prefixed with a different schema name.

An example of an eponymous virtual table is the [dbstat virtual table](dbstat.md). To use the dbstat virtual table as an eponymous virtual table, simply query against the "dbstat" module name, as if it were an ordinary table. (Note that SQLite must be compiled with the [SQLITE_ENABLE_DBSTAT_VTAB](compile.md#enable_dbstat_vtab) option to include the dbstat virtual table in the build.)

SELECT \* FROM dbstat;\

A virtual table is eponymous if its [xCreate](vtab.md#xcreate) method is the exact same function as the [xConnect](vtab.md#xconnect) method, or if the [xCreate](vtab.md#xcreate) method is NULL. The [xCreate](vtab.md#xcreate) method is called when a virtual table is first created using the [CREATE VIRTUAL TABLE](lang_createvtab.md) statement. The [xConnect](vtab.md#xconnect) method is invoked whenever a database connection attaches to or reparses a schema. When these two methods are the same, that indicates that the virtual table has no persistent state that needs to be created and destroyed. <span id="epoonlyvtab"></span>

### 1.1.3. Eponymous-only virtual tables

If the [xCreate](vtab.md#xcreate) method is NULL, then [CREATE VIRTUAL TABLE](lang_createvtab.md) statements are prohibited for that virtual table, and the virtual table is an "eponymous-only virtual table". Eponymous-only virtual tables are useful as [table-valued functions](vtab.md#tabfunc2).

Note that prior to [version 3.9.0](releaselog/3_9_0.md) (2015-10-14), SQLite did not check the xCreate method for NULL before invoking it. So if an eponymous-only virtual table is registered with SQLite [version 3.8.11.1](releaselog/3_8_11_1.md) (2015-07-29) or earlier and a [CREATE VIRTUAL TABLE](lang_createvtab.md) command is attempted against that virtual table module, a jump to a NULL pointer will occur, resulting in a crash.

## 1.2. Implementation

Several new C-level objects are used by the virtual table implementation:

typedef struct sqlite3_vtab sqlite3_vtab;\
typedef struct sqlite3_index_info sqlite3_index_info;\
typedef struct sqlite3_vtab_cursor sqlite3_vtab_cursor;\
typedef struct sqlite3_module sqlite3_module;\

The [sqlite3_module](c3ref/module.md) structure defines a module object used to implement a virtual table. Think of a module as a class from which one can construct multiple virtual tables having similar properties. For example, one might have a module that provides read-only access to comma-separated-value (CSV) files on disk. That one module can then be used to create several virtual tables where each virtual table refers to a different CSV file.

The module structure contains methods that are invoked by SQLite to perform various actions on the virtual table such as creating new instances of a virtual table or destroying old ones, reading and writing data, searching for and deleting, updating, or inserting rows. The module structure is explained in more detail below.

Each virtual table instance is represented by an [sqlite3_vtab](c3ref/vtab.md) structure. The sqlite3_vtab structure looks like this:

struct sqlite3_vtab {\
  const sqlite3_module \*pModule;\
  int nRef;\
  char \*zErrMsg;\
};\

Virtual table implementations will normally subclass this structure to add additional private and implementation-specific fields. The nRef field is used internally by the SQLite core and should not be altered by the virtual table implementation. The virtual table implementation may pass error message text to the core by putting an error message string in zErrMsg. Space to hold this error message string must be obtained from an SQLite memory allocation function such as [sqlite3_mprintf()](c3ref/mprintf.md) or [sqlite3_malloc()](c3ref/free.md). Prior to assigning a new value to zErrMsg, the virtual table implementation must free any preexisting content of zErrMsg using [sqlite3_free()](c3ref/free.md). Failure to do this will result in a memory leak. The SQLite core will free and zero the content of zErrMsg when it delivers the error message text to the client application or when it destroys the virtual table. The virtual table implementation only needs to worry about freeing the zErrMsg content when it overwrites the content with a new, different error message.

The [sqlite3_vtab_cursor](c3ref/vtab_cursor.md) structure represents a pointer to a specific row of a virtual table. This is what an sqlite3_vtab_cursor looks like:

struct sqlite3_vtab_cursor {\
  sqlite3_vtab \*pVtab;\
};\

Once again, practical implementations will likely subclass this structure to add additional private fields.

The [sqlite3_index_info](c3ref/index_info.md) structure is used to pass information into and out of the xBestIndex method of the module that implements a virtual table.

Before a [CREATE VIRTUAL TABLE](lang_createvtab.md) statement can be run, the module specified in that statement must be registered with the database connection. This is accomplished using either of the [sqlite3_create_module()](c3ref/create_module.md) or [sqlite3_create_module_v2()](c3ref/create_module.md) interfaces:

int sqlite3_create_module(\
  sqlite3 \*db,               /\* SQLite connection to register module with \*/\
  const char \*zName,         /\* Name of the module \*/\
  const sqlite3_module \*,    /\* Methods for the module \*/\
  void \*                     /\* Client data for xCreate/xConnect \*/\
);\
int sqlite3_create_module_v2(\
  sqlite3 \*db,               /\* SQLite connection to register module with \*/\
  const char \*zName,         /\* Name of the module \*/\
  const sqlite3_module \*,    /\* Methods for the module \*/\
  void \*,                    /\* Client data for xCreate/xConnect \*/\
  void(\*xDestroy)(void\*)     /\* Client data destructor function \*/\
);\

The [sqlite3_create_module()](c3ref/create_module.md) and [sqlite3_create_module_v2()](c3ref/create_module.md) routines associate a module name with an [sqlite3_module](c3ref/module.md) structure and a separate client data pointer that is specific to each module. The only difference between the two create_module methods is that the \_v2 method includes an extra parameter that specifies a destructor for client data pointer. The module structure is what defines the behavior of a virtual table. The module structure looks like this:

\
struct sqlite3_module {\
  int iVersion;\
  int (\*xCreate)(sqlite3\*, void \*pAux,\
               int argc, char \*const\*argv,\
               sqlite3_vtab \*\*ppVTab,\
               char \*\*pzErr);\
  int (\*xConnect)(sqlite3\*, void \*pAux,\
               int argc, char \*const\*argv,\
               sqlite3_vtab \*\*ppVTab,\
               char \*\*pzErr);\
  int (\*xBestIndex)(sqlite3_vtab \*pVTab, sqlite3_index_info\*);\
  int (\*xDisconnect)(sqlite3_vtab \*pVTab);\
  int (\*xDestroy)(sqlite3_vtab \*pVTab);\
  int (\*xOpen)(sqlite3_vtab \*pVTab, sqlite3_vtab_cursor \*\*ppCursor);\
  int (\*xClose)(sqlite3_vtab_cursor\*);\
  int (\*xFilter)(sqlite3_vtab_cursor\*, int idxNum, const char \*idxStr,\
                int argc, sqlite3_value \*\*argv);\
  int (\*xNext)(sqlite3_vtab_cursor\*);\
  int (\*xEof)(sqlite3_vtab_cursor\*);\
  int (\*xColumn)(sqlite3_vtab_cursor\*, sqlite3_context\*, int);\
  int (\*xRowid)(sqlite3_vtab_cursor\*, sqlite_int64 \*pRowid);\
  int (\*xUpdate)(sqlite3_vtab \*, int, sqlite3_value \*\*, sqlite_int64 \*);\
  int (\*xBegin)(sqlite3_vtab \*pVTab);\
  int (\*xSync)(sqlite3_vtab \*pVTab);\
  int (\*xCommit)(sqlite3_vtab \*pVTab);\
  int (\*xRollback)(sqlite3_vtab \*pVTab);\
  int (\*xFindFunction)(sqlite3_vtab \*pVtab, int nArg, const char \*zName,\
                     void (\*\*pxFunc)(sqlite3_context\*,int,sqlite3_value\*\*),\
                     void \*\*ppArg);\
  int (\*xRename)(sqlite3_vtab \*pVtab, const char \*zNew);\
  /\* The methods above are in version 1 of the sqlite_module object. Those \
  \*\* below are for version 2 and greater. \*/\
  int (\*xSavepoint)(sqlite3_vtab \*pVTab, int);\
  int (\*xRelease)(sqlite3_vtab \*pVTab, int);\
  int (\*xRollbackTo)(sqlite3_vtab \*pVTab, int);\
  /\* The methods above are in versions 1 and 2 of the sqlite_module object.\
  \*\* Those below are for version 3 and greater. \*/\
  int (\*xShadowName)(const char\*);\
  /\* The methods above are in versions 1 through 3 of the sqlite_module object.\
  \*\* Those below are for version 4 and greater. \*/\
  int (\*xIntegrity)(sqlite3_vtab \*pVTab, const char \*zSchema,\
                    const char \*zTabName, int mFlags, char \*\*pzErr);\
};\

The module structure defines all of the methods for each virtual table object. The module structure also contains the iVersion field which defines the particular edition of the module table structure. Currently, iVersion is always 4 or less, but in future releases of SQLite the module structure definition might be extended with additional methods and in that case the maximum iVersion value will be increased.

The rest of the module structure consists of methods used to implement various features of the virtual table. Details on what each of these methods do are provided in the sequel.

## 1.3. Virtual Tables And Shared Cache

Prior to SQLite [version 3.6.17](releaselog/3_6_17.md) (2009-08-10), the virtual table mechanism assumes that each [database connection](c3ref/sqlite3.md) kept its own copy of the database schema. Hence, the virtual table mechanism could not be used in a database that has [shared cache mode](sharedcache.md) enabled. The [sqlite3_create_module()](c3ref/create_module.md) interface would return an error if [shared cache mode](sharedcache.md) is enabled. That restriction was relaxed beginning with SQLite [version 3.6.17](releaselog/3_6_17.md). <span id="customvtab"></span>

## 1.4. Creating New Virtual Table Implementations

Follow these steps to create your own virtual table:

1.  Write all necessary methods.
2.  Create an instance of the [sqlite3_module](c3ref/module.md) structure containing pointers to all the methods from step 1.
3.  Register your [sqlite3_module](c3ref/module.md) structure using one of the [sqlite3_create_module()](c3ref/create_module.md) or [sqlite3_create_module_v2()](c3ref/create_module.md) interfaces.
4.  Run a [CREATE VIRTUAL TABLE](lang_createvtab.md) command that specifies the new module in the USING clause.

The only really hard part is step 1. You might want to start with an existing virtual table implementation and modify it to suit your needs. The [SQLite source tree](https://sqlite.org/src/dir?ci=trunk&type=tree) contains many virtual table implementations that are suitable for copying, including:

- **[templatevtab.c](https://sqlite.org/src/file/ext/misc/templatevtab.c)** → A virtual table created specifically to serve as a template for other custom virtual tables.
- **[series.c](https://sqlite.org/src/file/ext/misc/series.c)** → Implementation of the generate_series() table-valued function.
- **[json.c](https://sqlite.org/src/file/src/json.c)** → Contains the sources for the [json_each()](json1.md#jeach) and [json_tree()](json1.md#jtree) table-valued functions.
- **[csv.c](https://sqlite.org/src/file/ext/misc/csv.c)** → A virtual table that reads CSV files.

There are [many other virtual table implementations](vtablist.md) in the SQLite source tree that can be used as examples. Locate these other virtual table implementations by searching for "sqlite3_create_module".

You might also want to implement your new virtual table as a [loadable extension](loadext.md).

## 1.5. Security Considerations

Custom virtual tables can become security vulnerabilities if not carefully implemented. To help prevent problems, SQLite provides the following additional security features for virtual tables:

1.  The [xConnect](vtab.md#xconnect) and/or [xCreate](vtab.md#xcreate) method can invoke [sqlite3_vtab_config()](c3ref/vtab_config.md) with the [SQLITE_VTAB_DIRECTONLY](c3ref/c_vtab_constraint_support.md#sqlitevtabdirectonly) option to prevent the virtual table from being used from within triggers or views. This is recommended if the capability of using the virtual table from within triggers or views is not needed.

2.  Avoid using [sqlite3_vtab_config()](c3ref/vtab_config.md) with the [SQLITE_VTAB_INNOCUOUS](c3ref/c_vtab_constraint_support.md#sqlitevtabinnocuous) option unless absolutely necessary. Only set SQLITE_VTAB_INNOCUOUS if you are certain that your virtual table has no side effects and its purpose cannot be achieved without that setting.

3.  When the virtual table itself runs SQL statements and those statements depend on arguments to the CREATE VIRTUAL TABLE statement that created the virtual table, use the [sqlite3_prepare_v3()](c3ref/prepare.md) interface with the [SQLITE_PREPARE_FROM_DDL](c3ref/c_prepare_dont_log.md#sqlitepreparefromddl) option to prevent a bypass of the [SQLITE_DBCONFIG_TRUSTED_SCHEMA](c3ref/c_dbconfig_defensive.md#sqlitedbconfigtrustedschema) setting. If you are unsure whether or not an SQL statement depends on the CREATE VIRTUAL TABLE statement, it is usually harmless (depending on the semantics of the virtual table) to include SQLITE_PREPARE_FROM_DDL even if it is not strictly needed, and so the default action should probably be to use SQLITE_PREPARE_FROM_DDL unless you have a specific reason not to.

See also [Security Implications For Custom SQL Functions](./appfunc.md#sec) and [Defense Against The Dark Arts](./security.md).

# 2. Virtual Table Methods

<span id="xcreate"></span>

## 2.1. The xCreate Method

int (\*xCreate)(sqlite3 \*db, void \*pAux,\
             int argc, char \*const\*argv,\
             sqlite3_vtab \*\*ppVTab,\
             char \*\*pzErr);\

The xCreate method is called to create a new instance of a virtual table in response to a [CREATE VIRTUAL TABLE](lang_createvtab.md) statement. If the xCreate method is the same pointer as the [xConnect](vtab.md#xconnect) method, then the virtual table is an [eponymous virtual table](vtab.md#epovtab). If the xCreate method is omitted (if it is a NULL pointer) then the virtual table is an [eponymous-only virtual table](vtab.md#epoonlyvtab).

The db parameter is a pointer to the SQLite [database connection](c3ref/sqlite3.md) that is executing the [CREATE VIRTUAL TABLE](lang_createvtab.md) statement. The pAux argument is the copy of the client data pointer that was the fourth argument to the [sqlite3_create_module()](c3ref/create_module.md) or [sqlite3_create_module_v2()](c3ref/create_module.md) call that registered the [virtual table module](c3ref/module.md). The argv parameter is an array of argc pointers to null terminated strings. The first string, argv\[0\], is the name of the module being invoked. The module name is the name provided as the second argument to [sqlite3_create_module()](c3ref/create_module.md) and as the argument to the USING clause of the [CREATE VIRTUAL TABLE](lang_createvtab.md) statement that is running. The second, argv\[1\], is the name of the database in which the new virtual table is being created. The database name is "main" for the primary database, or "temp" for TEMP database, or the name given at the end of the [ATTACH](lang_attach.md) statement for attached databases. The third element of the array, argv\[2\], is the name of the new virtual table, as specified following the TABLE keyword in the [CREATE VIRTUAL TABLE](lang_createvtab.md) statement. If present, the fourth and subsequent strings in the argv\[\] array report the arguments to the module name in the [CREATE VIRTUAL TABLE](lang_createvtab.md) statement.

The job of this method is to construct the new virtual table object (an [sqlite3_vtab](c3ref/vtab.md) object) and return a pointer to it in \*ppVTab.

As part of the task of creating a new [sqlite3_vtab](c3ref/vtab.md) structure, this method <u>must</u> invoke [sqlite3_declare_vtab()](c3ref/declare_vtab.md) to tell the SQLite core about the columns and datatypes in the virtual table. The [sqlite3_declare_vtab()](c3ref/declare_vtab.md) API has the following prototype:

int sqlite3_declare_vtab(sqlite3 \*db, const char \*zCreateTable)\

The first argument to [sqlite3_declare_vtab()](c3ref/declare_vtab.md) must be the same [database connection](c3ref/sqlite3.md) pointer as the first parameter to this method. The second argument to [sqlite3_declare_vtab()](c3ref/declare_vtab.md) must a zero-terminated UTF-8 string that contains a well-formed [CREATE TABLE](lang_createtable.md) statement that defines the columns in the virtual table and their data types. The name of the table in this CREATE TABLE statement is ignored, as are all constraints. Only the column names and datatypes matter. The CREATE TABLE statement string need not be held in persistent memory. The string can be deallocated and/or reused as soon as the [sqlite3_declare_vtab()](c3ref/declare_vtab.md) routine returns.

The xConnect method can also optionally request special features for the virtual table by making one or more calls to the [sqlite3_vtab_config()](c3ref/vtab_config.md) interface:

int sqlite3_vtab_config(sqlite3 \*db, int op, ...);\

Calls to sqlite3_vtab_config() are optional. But for maximum security, it is recommended that virtual table implementations invoke "[sqlite3_vtab_config](c3ref/vtab_config.md)(db, [SQLITE_VTAB_DIRECTONLY](c3ref/c_vtab_constraint_support.md#sqlitevtabdirectonly))" if the virtual table will not be used from inside of triggers or views.

The xCreate method need not initialize the pModule, nRef, and zErrMsg fields of the [sqlite3_vtab](c3ref/vtab.md) object. The SQLite core will take care of that chore.

The xCreate should return [SQLITE_OK](rescode.md#ok) if it is successful in creating the new virtual table, or [SQLITE_ERROR](rescode.md#error) if it is not successful. If not successful, the [sqlite3_vtab](c3ref/vtab.md) structure must not be allocated. An error message may optionally be returned in \*pzErr if unsuccessful. Space to hold the error message string must be allocated using an SQLite memory allocation function like [sqlite3_malloc()](c3ref/free.md) or [sqlite3_mprintf()](c3ref/mprintf.md) as the SQLite core will attempt to free the space using [sqlite3_free()](c3ref/free.md) after the error has been reported up to the application.

If the xCreate method is omitted (left as a NULL pointer) then the virtual table is an [eponymous-only virtual table](vtab.md#epoonlyvtab). New instances of the virtual table cannot be created using [CREATE VIRTUAL TABLE](lang_createvtab.md) and the virtual table can only be used via its module name. Note that SQLite versions prior to 3.9.0 (2015-10-14) do not understand eponymous-only virtual tables and will segfault if an attempt is made to [CREATE VIRTUAL TABLE](lang_createvtab.md) on an eponymous-only virtual table because the xCreate method was not checked for null.

If the xCreate method is the exact same pointer as the [xConnect](vtab.md#xconnect) method, that indicates that the virtual table does not need to initialize backing store. Such a virtual table can be used as an [eponymous virtual table](vtab.md#epovtab) or as a named virtual table using [CREATE VIRTUAL TABLE](lang_createvtab.md) or both. <span id="hiddencol"></span>

### 2.1.1. Hidden columns in virtual tables

If a column datatype contains the special keyword "HIDDEN" (in any combination of upper and lower case letters) then that keyword is omitted from the column datatype name and the column is marked as a hidden column internally. A hidden column differs from a normal column in three respects:

- Hidden columns are not listed in the dataset returned by "[PRAGMA table_info](pragma.md#pragma_table_info)",
- Hidden columns are not included in the expansion of a "\*" expression in the result set of a [SELECT](lang_select.md), and
- Hidden columns are not included in the implicit column-list used by an [INSERT](lang_insert.md) statement that lacks an explicit column-list.

For example, if the following SQL is passed to [sqlite3_declare_vtab()](c3ref/declare_vtab.md):

CREATE TABLE x(a HIDDEN VARCHAR(12), b INTEGER, c INTEGER Hidden);\

Then the virtual table would be created with two hidden columns, and with datatypes of "VARCHAR(12)" and "INTEGER".

An example use of hidden columns can be seen in the [FTS3](fts3.md) virtual table implementation, where every FTS virtual table contains an [FTS hidden column](fts3.md#hiddencol) that is used to pass information from the virtual table into [FTS auxiliary functions](fts3.md#snippet) and to the [FTS MATCH](fts3.md#full_text_index_queries) operator. <span id="tabfunc2"></span>

### 2.1.2. Table-valued functions

A [virtual table](vtab.md) that contains [hidden columns](vtab.md#hiddencol) can be used like a table-valued function in the FROM clause of a [SELECT](lang_select.md) statement. The arguments to the table-valued function become constraints on the HIDDEN columns of the virtual table.

For example, the "generate_series" extension (located in the [ext/misc/series.c](https://sqlite.org/src/artifact?ci=trunk&filename=ext/misc/series.c) file in the [source tree](https://sqlite.org/src/tree?ci=trunk)) implements an [eponymous virtual table](vtab.md#epovtab) with the following schema:

CREATE TABLE generate_series(\
  value,\
  start HIDDEN,\
  stop HIDDEN,\
  step HIDDEN\
);\

The [sqlite3_module.xBestIndex](vtab.md#xbestindex) method in the implementation of this table checks for equality constraints against the HIDDEN columns, and uses those as input parameters to determine the range of integer "value" outputs to generate. Reasonable defaults are used for any unconstrained columns. For example, to list all integers between 5 and 50:

SELECT value FROM generate_series(5,50);\

The previous query is equivalent to the following:

SELECT value FROM generate_series WHERE start=5 AND stop=50;\

Arguments on the virtual table name are matched to [hidden columns](vtab.md#hiddencol) in order. The number of arguments can be less than the number of hidden columns, in which case the latter hidden columns are unconstrained. However, an error results if there are more arguments than there are hidden columns in the virtual table. <span id="worid"></span>

### 2.1.3.  WITHOUT ROWID Virtual Tables

Beginning with SQLite [version 3.14.0](releaselog/3_14.md) (2016-08-08), the CREATE TABLE statement that is passed into [sqlite3_declare_vtab()](c3ref/declare_vtab.md) may contain a [WITHOUT ROWID](withoutrowid.md) clause. This is useful for cases where the virtual table rows cannot easily be mapped into unique integers. A CREATE TABLE statement that includes WITHOUT ROWID must define one or more columns as the PRIMARY KEY. Every column of the PRIMARY KEY must individually be NOT NULL and all columns for each row must be collectively unique.

Note that SQLite does not enforce the PRIMARY KEY for a WITHOUT ROWID virtual table. Enforcement is the responsibility of the underlying virtual table implementation. But SQLite does assume that the PRIMARY KEY constraint is valid - that the identified columns really are UNIQUE and NOT NULL - and it uses that assumption to optimize queries against the virtual table.

The rowid column is not accessible on a WITHOUT ROWID virtual table (of course).

The [xUpdate](vtab.md#xupdate) method was originally designed around having a [ROWID](lang_createtable.md#rowid) as a single value. The [xUpdate](vtab.md#xupdate) method has been expanded to accommodate an arbitrary PRIMARY KEY in place of the ROWID, but the PRIMARY KEY must still be only one column. For this reason, SQLite will reject any WITHOUT ROWID virtual table that has more than one PRIMARY KEY column and a non-NULL xUpdate method. <span id="xconnect"></span>

## 2.2. The xConnect Method

int (\*xConnect)(sqlite3\*, void \*pAux,\
             int argc, char \*const\*argv,\
             sqlite3_vtab \*\*ppVTab,\
             char \*\*pzErr);\

The xConnect method is very similar to [xCreate](vtab.md#xcreate). It has the same parameters and constructs a new [sqlite3_vtab](c3ref/vtab.md) structure just like xCreate. And it must also call [sqlite3_declare_vtab()](c3ref/declare_vtab.md) like xCreate. It should also make all of the same [sqlite3_vtab_config()](c3ref/vtab_config.md) calls as xCreate.

The difference is that xConnect is called to establish a new connection to an existing virtual table whereas xCreate is called to create a new virtual table from scratch.

The xCreate and xConnect methods are only different when the virtual table has some kind of backing store that must be initialized the first time the virtual table is created. The xCreate method creates and initializes the backing store. The xConnect method just connects to an existing backing store. When xCreate and xConnect are the same, the table is an [eponymous virtual table](vtab.md#epovtab).

As an example, consider a virtual table implementation that provides read-only access to existing comma-separated-value (CSV) files on disk. There is no backing store that needs to be created or initialized for such a virtual table (since the CSV files already exist on disk) so the xCreate and xConnect methods will be identical for that module.

Another example is a virtual table that implements a full-text index. The xCreate method must create and initialize data structures to hold the dictionary and posting lists for that index. The xConnect method, on the other hand, only has to locate and use an existing dictionary and posting lists that were created by a prior xCreate call.

The xConnect method must return [SQLITE_OK](rescode.md#ok) if it is successful in creating the new virtual table, or [SQLITE_ERROR](rescode.md#error) if it is not successful. If not successful, the [sqlite3_vtab](c3ref/vtab.md) structure must not be allocated. An error message may optionally be returned in \*pzErr if unsuccessful. Space to hold the error message string must be allocated using an SQLite memory allocation function like [sqlite3_malloc()](c3ref/free.md) or [sqlite3_mprintf()](c3ref/mprintf.md) as the SQLite core will attempt to free the space using [sqlite3_free()](c3ref/free.md) after the error has been reported up to the application.

The xConnect method is required for every virtual table implementation, though the [xCreate](vtab.md#xcreate) and xConnect pointers of the [sqlite3_module](c3ref/module.md) object may point to the same function if the virtual table does not need to initialize backing store. <span id="xbestindex"></span>

## 2.3. The xBestIndex Method

SQLite uses the xBestIndex method of a virtual table module to determine the best way to access the virtual table. The xBestIndex method has a prototype like this:

int (\*xBestIndex)(sqlite3_vtab \*pVTab, sqlite3_index_info\*);\

The SQLite core communicates with the xBestIndex method by filling in certain fields of the [sqlite3_index_info](c3ref/index_info.md) structure and passing a pointer to that structure into xBestIndex as the second parameter. The xBestIndex method fills out other fields of this structure which forms the reply. The [sqlite3_index_info](c3ref/index_info.md) structure looks like this:

struct sqlite3_index_info {\
  /\* Inputs \*/\
  const int nConstraint;     /\* Number of entries in aConstraint \*/\
  const struct sqlite3_index_constraint {\
     int iColumn;              /\* Column constrained.  -1 for ROWID \*/\
     unsigned char op;         /\* Constraint operator \*/\
     unsigned char usable;     /\* True if this constraint is usable \*/\
     int iTermOffset;          /\* Used internally - xBestIndex should ignore \*/\
  } \*const aConstraint;      /\* Table of WHERE clause constraints \*/\
  const int nOrderBy;        /\* Number of terms in the ORDER BY clause \*/\
  const struct sqlite3_index_orderby {\
     int iColumn;              /\* Column number \*/\
     unsigned char desc;       /\* True for DESC.  False for ASC. \*/\
  } \*const aOrderBy;         /\* The ORDER BY clause \*/\
\
  /\* Outputs \*/\
  struct sqlite3_index_constraint_usage {\
    int argvIndex;           /\* if \>0, constraint is part of argv to xFilter \*/\
    unsigned char omit;      /\* Do not code a test for this constraint \*/\
  } \*const aConstraintUsage;\
  int idxNum;                /\* Number used to identify the index \*/\
  char \*idxStr;              /\* String, possibly obtained from sqlite3_malloc \*/\
  int needToFreeIdxStr;      /\* Free idxStr using sqlite3_free() if true \*/\
  int orderByConsumed;       /\* True if output is already ordered \*/\
  double estimatedCost;      /\* Estimated cost of using this index \*/\
  **/\* Fields below are only available in SQLite 3.8.2 and later \*/**\
  sqlite3_int64 estimatedRows;    /\* Estimated number of rows returned \*/\
  **/\* Fields below are only available in SQLite 3.9.0 and later \*/**\
  int idxFlags;              /\* Mask of SQLITE_INDEX_SCAN\_\* flags \*/\
  **/\* Fields below are only available in SQLite 3.10.0 and later \*/**\
  sqlite3_uint64 colUsed;    /\* Input: Mask of columns used by statement \*/\
};\

Note the warnings on the "estimatedRows", "idxFlags", and "colUsed" fields. These fields were added with SQLite versions 3.8.2, 3.9.0, and 3.10.0, respectively. Any extension that reads or writes these fields must first check that the version of the SQLite library in use is greater than or equal to the appropriate version - perhaps comparing the value returned from [sqlite3_libversion_number()](c3ref/libversion.md) against constants 3008002, 3009000, and/or 3010000. The result of attempting to access these fields in an sqlite3_index_info structure created by an older version of SQLite are undefined.

In addition, there are some defined constants:

\#define SQLITE_INDEX_CONSTRAINT_EQ         2\
\#define SQLITE_INDEX_CONSTRAINT_GT         4\
\#define SQLITE_INDEX_CONSTRAINT_LE         8\
\#define SQLITE_INDEX_CONSTRAINT_LT        16\
\#define SQLITE_INDEX_CONSTRAINT_GE        32\
\#define SQLITE_INDEX_CONSTRAINT_MATCH     64\
\#define SQLITE_INDEX_CONSTRAINT_LIKE      65  /\* 3.10.0 and later \*/\
\#define SQLITE_INDEX_CONSTRAINT_GLOB      66  /\* 3.10.0 and later \*/\
\#define SQLITE_INDEX_CONSTRAINT_REGEXP    67  /\* 3.10.0 and later \*/\
\#define SQLITE_INDEX_CONSTRAINT_NE        68  /\* 3.21.0 and later \*/\
\#define SQLITE_INDEX_CONSTRAINT_ISNOT     69  /\* 3.21.0 and later \*/\
\#define SQLITE_INDEX_CONSTRAINT_ISNOTNULL 70  /\* 3.21.0 and later \*/\
\#define SQLITE_INDEX_CONSTRAINT_ISNULL    71  /\* 3.21.0 and later \*/\
\#define SQLITE_INDEX_CONSTRAINT_IS        72  /\* 3.21.0 and later \*/\
\#define SQLITE_INDEX_CONSTRAINT_LIMIT     73  /\* 3.38.0 and later \*/\
\#define SQLITE_INDEX_CONSTRAINT_OFFSET    74  /\* 3.38.0 and later \*/\
\#define SQLITE_INDEX_CONSTRAINT_FUNCTION 150  /\* 3.25.0 and later \*/\
\#define SQLITE_INDEX_SCAN_UNIQUE           1  /\* Scan visits at most 1 row \*/\

Use the [sqlite3_vtab_collation()](c3ref/vtab_collation.md) interface to find the name of the [collating sequence](datatype3.md#collation) that should be used when evaluating the i-th constraint:

const char \*sqlite3_vtab_collation(sqlite3_index_info\*, int i);\

The SQLite core calls the xBestIndex method when it is compiling a query that involves a virtual table. In other words, SQLite calls this method when it is running [sqlite3_prepare()](c3ref/prepare.md) or the equivalent. By calling this method, the SQLite core is saying to the virtual table that it needs to access some subset of the rows in the virtual table and it wants to know the most efficient way to do that access. The xBestIndex method replies with information that the SQLite core can then use to conduct an efficient search of the virtual table.

While compiling a single SQL query, the SQLite core might call xBestIndex multiple times with different settings in [sqlite3_index_info](c3ref/index_info.md). The SQLite core will then select the combination that appears to give the best performance.

Before calling this method, the SQLite core initializes an instance of the [sqlite3_index_info](c3ref/index_info.md) structure with information about the query that it is currently trying to process. This information derives mainly from the WHERE clause and ORDER BY or GROUP BY clauses of the query, but also from any ON or USING clauses if the query is a join. The information that the SQLite core provides to the xBestIndex method is held in the part of the structure that is marked as "Inputs". The "Outputs" section is initialized to zero.

The information in the [sqlite3_index_info](c3ref/index_info.md) structure is ephemeral and may be overwritten or deallocated as soon as the xBestIndex method returns. If the xBestIndex method needs to remember any part of the [sqlite3_index_info](c3ref/index_info.md) structure, it should make a copy. Care must be take to store the copy in a place where it will be deallocated, such as in the idxStr field with needToFreeIdxStr set to 1.

Note that xBestIndex will always be called before [xFilter](vtab.md#xfilter), since the idxNum and idxStr outputs from xBestIndex are required inputs to xFilter. However, there is no guarantee that xFilter will be called following a successful xBestIndex.

The xBestIndex method is required for every virtual table implementation.

### 2.3.1. Inputs

The main thing that the SQLite core is trying to communicate to the virtual table is the constraints that are available to limit the number of rows that need to be searched. The aConstraint\[\] array contains one entry for each constraint. There will be exactly nConstraint entries in that array.

Each constraint will usually correspond to a term in the WHERE clause or in a USING or ON clause that is of the form

> column OP EXPR

Where "column" is a column in the virtual table, OP is an operator like "=" or "\<", and EXPR is an arbitrary expression. So, for example, if the WHERE clause contained a term like this:

a = 5\

Then one of the constraints would be on the "a" column with operator "=" and an expression of "5". Constraints need not have a literal representation of the WHERE clause. The query optimizer might make transformations to the WHERE clause in order to extract as many constraints as it can. So, for example, if the WHERE clause contained something like this:

x BETWEEN 10 AND 100 AND 999\>y\

The query optimizer might translate this into three separate constraints:

x \>= 10\
x \<= 100\
y \< 999\

For each such constraint, the aConstraint\[\].iColumn field indicates which column appears on the left-hand side of the constraint. The first column of the virtual table is column 0. The rowid of the virtual table is column -1. The aConstraint\[\].op field indicates which operator is used. The SQLITE_INDEX_CONSTRAINT\_\* constants map integer constants into operator values. Columns occur in the order they were defined by the call to [sqlite3_declare_vtab()](c3ref/declare_vtab.md) in the [xCreate](vtab.md#xcreate) or [xConnect](vtab.md#xconnect) method. Hidden columns are counted when determining the column index.

If the [xFindFunction()](vtab.md#xfindfunction) method for the virtual table is defined, and if xFindFunction() sometimes returns [SQLITE_INDEX_CONSTRAINT_FUNCTION](c3ref/c_index_constraint_eq.md) or larger, then the constraints might also be of the form:

> FUNCTION( column, EXPR)

In this case the aConstraint\[\].op value is the same as the value returned by [xFindFunction()](vtab.md#xfindfunction) for FUNCTION.

The aConstraint\[\] array contains information about all constraints that apply to the virtual table. But some of the constraints might not be usable because of the way tables are ordered in a join. The xBestIndex method must therefore only consider constraints that have an aConstraint\[\].usable flag which is true.

In addition to WHERE clause constraints, the SQLite core also tells the xBestIndex method about the ORDER BY clause. (In an aggregate query, the SQLite core might put in GROUP BY clause information in place of the ORDER BY clause information, but this fact should not make any difference to the xBestIndex method.) If all terms of the ORDER BY clause are columns in the virtual table, then nOrderBy will be the number of terms in the ORDER BY clause and the aOrderBy\[\] array will identify the column for each term in the order by clause and whether or not that column is ASC or DESC. <span id="colUsed"></span>

In SQLite [version 3.10.0](releaselog/3_10_0.md) (2016-01-06) and later, the colUsed field is available to indicate which fields of the virtual table are actually used by the statement being prepared. If the lowest bit of colUsed is set, that means that the first column is used. The second lowest bit corresponds to the second column. And so forth. If the most significant bit of colUsed is set, that means that one or more columns other than the first 63 columns are used. If column usage information is needed by the [xFilter](vtab.md#xfilter) method, then the required bits must be encoded into either the output idxNum field or idxStr content.

#### 2.3.1.1. LIKE, GLOB, REGEXP, and MATCH functions

For the LIKE, GLOB, REGEXP, and MATCH operators, the aConstraint\[\].iColumn value is the virtual table column that is the left operand of the operator. However, if these operators are expressed as function calls instead of operators, then the aConstraint\[\].iColumn value references the virtual table column that is the second argument to that function:

> LIKE(*EXPR*, *column*)\
> GLOB(*EXPR*, *column*)\
> REGEXP(*EXPR*, *column*)\
> MATCH(*EXPR*, *column*)\

Hence, as far as the xBestIndex() method is concerned, the following two forms are equivalent:

> *column* LIKE *EXPR*\
> LIKE(*EXPR*,*column*)

This special behavior of looking at the second argument of a function only occurs for the LIKE, GLOB, REGEXP, and MATCH functions. For all other functions, the aConstraint\[\].iColumn value references the first argument of the function.

This special feature of LIKE, GLOB, REGEXP, and MATCH does not apply to the [xFindFunction()](vtab.md#xfindfunction) method, however. The [xFindFunction()](vtab.md#xfindfunction) method always keys off of the left operand of an LIKE, GLOB, REGEXP, or MATCH operator but off of the first argument to function-call equivalents of those operators.

#### 2.3.1.2. LIMIT and OFFSET

When aConstraint\[\].op is one of SQLITE_INDEX_CONSTRAINT_LIMIT or SQLITE_INDEX_CONSTRAINT_OFFSET, that indicates that there is a LIMIT or OFFSET clause on the SQL query statement that is using the virtual table. The LIMIT and OFFSET operators have no left operand, and so when aConstraint\[\].op is one of SQLITE_INDEX_CONSTRAINT_LIMIT or SQLITE_INDEX_CONSTRAINT_OFFSET then the aConstraint\[\].iColumn value is meaningless and should not be used.

#### 2.3.1.3. Right-hand side values of constraints

The [sqlite3_vtab_rhs_value()](c3ref/vtab_rhs_value.md) interface can be used to try to access the right-hand operand of a constraint. However, the value of a right-hand operator might not be known at the time that the xBestIndex method is run, so the sqlite3_vtab_rhs_value() call might not be successful. Usually the right operand of a constraint is only available to xBestIndex if it is coded as a literal value in the input SQL. If the right operand is coded as an expression or a [host parameter](c3ref/bind_blob.md), it probably will not be accessible to xBestIndex. Some operators, such as [SQLITE_INDEX_CONSTRAINT_ISNULL](c3ref/c_index_constraint_eq.md) and [SQLITE_INDEX_CONSTRAINT_ISNOTNULL](c3ref/c_index_constraint_eq.md) have no right-hand operand. The sqlite3_vtab_rhs_value() interface always returns [SQLITE_NOTFOUND](rescode.md#notfound) for such operators.

### 2.3.2. Outputs

Given all of the information above, the job of the xBestIndex method is to figure out the best way to search the virtual table.

The xBestIndex method conveys an indexing strategy to the [xFilter](vtab.md#xfilter) method through the idxNum and idxStr fields. The idxNum value and idxStr string content are arbitrary as far as the SQLite core is concerned and can have any meaning as long as xBestIndex and xFilter agree on what that meaning is. The SQLite core just copies the information from xBestIndex through to the [xFilter](vtab.md#xfilter) method, assuming only that the char sequence referenced via idxStr is NUL terminated.

The idxStr value may be a string obtained from an SQLite memory allocation function such as [sqlite3_mprintf()](c3ref/mprintf.md). If this is the case, then the needToFreeIdxStr flag must be set to true so that the SQLite core will know to call [sqlite3_free()](c3ref/free.md) on that string when it has finished with it, and thus avoid a memory leak. The idxStr value may also be a static constant string, in which case the needToFreeIdxStr boolean should remain false.

The estimatedCost field should be set to the estimated number of disk access operations required to execute this query against the virtual table. The SQLite core will often call xBestIndex multiple times with different constraints, obtain multiple cost estimates, then choose the query plan that gives the lowest estimate. The SQLite core initializes estimatedCost to a very large value prior to invoking xBestIndex, so if xBestIndex determines that the current combination of parameters is undesirable, it can leave the estimatedCost field unchanged to discourage its use.

If the current version of SQLite is 3.8.2 or greater, the estimatedRows field may be set to an estimate of the number of rows returned by the proposed query plan. If this value is not explicitly set, the default estimate of 25 rows is used.

If the current version of SQLite is 3.9.0 or greater, the idxFlags field may be set to SQLITE_INDEX_SCAN_UNIQUE to indicate that the virtual table will return only zero or one rows given the input constraints. Additional bits of the idxFlags field might be understood in later versions of SQLite.

The aConstraintUsage\[\] array contains one element for each of the nConstraint constraints in the inputs section of the [sqlite3_index_info](c3ref/index_info.md) structure. The aConstraintUsage\[\] array is used by xBestIndex to tell the core how it is using the constraints.

The xBestIndex method may set aConstraintUsage\[\].argvIndex entries to values greater than zero. Exactly one entry should be set to 1, another to 2, another to 3, and so forth up to as many or as few as the xBestIndex method wants. The EXPR of the corresponding constraints will then be passed in as the argv\[\] parameters to xFilter.

For example, if the aConstraint\[3\].argvIndex is set to 1, then when xFilter is called, the argv\[0\] passed to xFilter will have the EXPR value of the aConstraint\[3\] constraint.

#### 2.3.2.1. Omit constraint checking in bytecode

By default, the SQLite generates [bytecode](opcode.md) that will double-check all constraints on each row of the virtual table to verify that they are satisfied. If the virtual table can guarantee that a constraint will always be satisfied, it can try to suppress that double-check by setting aConstraintUsage\[\].omit. However, with some exceptions, this is only a hint and there is no guarantee that the redundant check of the constraint will be suppressed. Key points:

- The omit flag is only honored if the argvIndex value for the constraint is greater than 0 and less than or equal to 16. Constraint checking is never suppressed for constraints that do not pass their right operand into the xFilter method. The current implementation is only able to suppress redundant constraint checking for the first 16 values passed to xFilter, though that limitation might be increased in future releases.

- The omit flag is always honored for [SQLITE_INDEX_CONSTRAINT_OFFSET](c3ref/c_index_constraint_eq.md) constraints as long as argvIndex is greater than 0. Setting the omit flag on an SQLITE_INDEX_CONSTRAINT_OFFSET constraint indicates to SQLite that the virtual table will itself suppress the first N rows of output, where N is the right operand of the OFFSET operator. If the virtual table implementation sets omit on an SQLITE_INDEX_CONSTRAINT_OFFSET constraint but then fails to suppress the first N rows of output, an incorrect answer will result from the overall query.

<span id="obc"></span>

#### 2.3.2.2. ORDER BY and orderByConsumed

If the virtual table will output rows in the order specified by the ORDER BY clause, then the orderByConsumed flag may be set to true. If the output is not automatically in the correct order then orderByConsumed must be left in its default false setting. This will indicate to the SQLite core that it will need to do a separate sorting pass over the data after it comes out of the virtual table. Setting orderByConsumed is an optimization. A query will always get the correct answer if orderByConsumed is left at its default value (0). Unnecessary sort operations might be avoided resulting in a faster query if orderByConsumed is set, but setting orderByConsumed incorrectly can result in an incorrect answer. It is suggested that new virtual table implementations leave the orderByConsumed value unset initially, and then after everything else is known to be working correctly, go back and attempt to optimize by setting orderByConsumed where appropriate.

Sometimes the orderByConsumed flag can be safely set even if the outputs from the virtual table are not strictly in the order specified by nOrderBy and aOrderBy. If the [sqlite3_vtab_distinct()](c3ref/vtab_distinct.md) interface returns 1 or 2, that indicates that the ordering can be relaxed. See the documentation on [sqlite3_vtab_distinct()](c3ref/vtab_distinct.md) for further information.

### 2.3.3. Return Value

The xBestIndex method should return SQLITE_OK on success. If any kind of fatal error occurs, an appropriate error code (ex: [SQLITE_NOMEM](rescode.md#nomem)) should be returned instead.

If xBestIndex returns [SQLITE_CONSTRAINT](rescode.md#constraint), that does not indicate an error. Rather, SQLITE_CONSTRAINT indicates that the particular combination of input parameters specified is insufficient for the virtual table to do its job. This is logically the same as setting the estimatedCost to infinity. If every call to xBestIndex for a particular query plan returns SQLITE_CONSTRAINT, that means there is no way for the virtual table to be safely used, and the [sqlite3_prepare()](c3ref/prepare.md) call will fail with a "no query solution" error. <span id="erpotvf"></span>

### 2.3.4. Enforcing Required Parameters On Table-Valued Functions

The SQLITE_CONSTRAINT return from xBestIndex is useful for [table-valued functions](vtab.md#tabfunc2) that have required parameters. If the aConstraint\[\].usable field is false for one of the required parameter, then the xBestIndex method should return SQLITE_CONSTRAINT. If a required field does not appear in the aConstraint\[\] array at all, that means that the corresponding parameter is omitted from the input SQL. In that case, xBestIndex should set an error message in pVTab-\>zErrMsg and return SQLITE_ERROR. To summarize:

1.  The aConstraint\[\].usable value for a required parameter is false → return SQLITE_CONSTRAINT.

2.  A required parameter does not appear anywhere in the aConstraint\[\] array → Set an error message in pVTab-\>zErrMsg and return SQLITE_ERROR

The following example will better illustrate the use of SQLITE_CONSTRAINT as a return value from xBestIndex:

SELECT \* FROM realtab, tablevaluedfunc(realtab.x);\

Assuming that the first hidden column of "tablevaluedfunc" is "param1", the query above is semantically equivalent to this:

SELECT \* FROM realtab, tablevaluedfunc\
 WHERE tablevaluedfunc.param1 = realtab.x;\

The query planner must decide between many possible implementations of this query, but two plans in particular are of note:

1.  Scan all rows of realtab and for each row, find rows in tablevaluedfunc where param1 is equal to realtab.x

2.  Scan all rows of tablevalued func and for each row find rows in realtab where x is equal to tablevaluedfunc.param1.

The xBestIndex method will be invoked once for each of the potential plans above. For plan 1, the aConstraint\[\].usable flag for the SQLITE_CONSTRAINT_EQ constraint on the param1 column will be true because the right-hand side value for the "param1 = ?" constraint will be known, since it is determined by the outer realtab loop. But for plan 2, the aConstraint\[\].usable flag for "param1 = ?" will be false because the right-hand side value is determined by an inner loop and is thus an unknown quantity. Because param1 is a required input to the table-valued functions, the xBestIndex method should return SQLITE_CONSTRAINT when presented with plan 2, indicating that a required input is missing. This forces the query planner to select plan 1. <span id="xdisconnect"></span>

## 2.4. The xDisconnect Method

int (\*xDisconnect)(sqlite3_vtab \*pVTab);\

This method releases a connection to a virtual table. Only the [sqlite3_vtab](c3ref/vtab.md) object is destroyed. The virtual table is not destroyed and any backing store associated with the virtual table persists. This method undoes the work of [xConnect](vtab.md#xconnect).

This method is a destructor for a connection to the virtual table. Contrast this method with [xDestroy](vtab.md#sqlite3_module.xDestroy). The xDestroy is a destructor for the entire virtual table.

The xDisconnect method is required for every virtual table implementation, though it is acceptable for the xDisconnect and [xDestroy](vtab.md#sqlite3_module.xDestroy) methods to be the same function if that makes sense for the particular virtual table. <span id="sqlite3_module.xDestroy"></span>

## 2.5. The xDestroy Method

int (\*xDestroy)(sqlite3_vtab \*pVTab);\

This method releases a connection to a virtual table, just like the [xDisconnect](vtab.md#xdisconnect) method, and it also destroys the underlying table implementation. This method undoes the work of [xCreate](vtab.md#xcreate).

The [xDisconnect](vtab.md#xdisconnect) method is called whenever a database connection that uses a virtual table is closed. The xDestroy method is only called when a [DROP TABLE](lang_droptable.md) statement is executed against the virtual table.

The xDestroy method is required for every virtual table implementation, though it is acceptable for the [xDisconnect](vtab.md#xdisconnect) and xDestroy methods to be the same function if that makes sense for the particular virtual table. <span id="xopen"></span>

## 2.6. The xOpen Method

int (\*xOpen)(sqlite3_vtab \*pVTab, sqlite3_vtab_cursor \*\*ppCursor);\

The xOpen method creates a new cursor used for accessing (read and/or writing) a virtual table. A successful invocation of this method will allocate the memory for the [sqlite3_vtab_cursor](c3ref/vtab_cursor.md) (or a subclass), initialize the new object, and make \*ppCursor point to the new object. The successful call then returns [SQLITE_OK](rescode.md#ok).

For every successful call to this method, the SQLite core will later invoke the [xClose](vtab.md#xclose) method to destroy the allocated cursor.

The xOpen method need not initialize the pVtab field of the [sqlite3_vtab_cursor](c3ref/vtab_cursor.md) structure. The SQLite core will take care of that chore automatically.

A virtual table implementation must be able to support an arbitrary number of simultaneously open cursors.

When initially opened, the cursor is in an undefined state. The SQLite core will invoke the [xFilter](vtab.md#xfilter) method on the cursor prior to any attempt to position or read from the cursor.

The xOpen method is required for every virtual table implementation. <span id="xclose"></span>

## 2.7. The xClose Method

int (\*xClose)(sqlite3_vtab_cursor\*);\

The xClose method closes a cursor previously opened by [xOpen](vtab.md#xopen). The SQLite core will always call xClose once for each cursor opened using xOpen.

This method must release all resources allocated by the corresponding xOpen call. The routine will not be called again even if it returns an error. The SQLite core will not use the [sqlite3_vtab_cursor](c3ref/vtab_cursor.md) again after it has been closed.

The xClose method is required for every virtual table implementation. <span id="xeof"></span>

## 2.8. The xEof Method

int (\*xEof)(sqlite3_vtab_cursor\*);\

The xEof method must return false (zero) if the specified cursor currently points to a valid row of data, or true (non-zero) otherwise. This method is called by the SQL engine immediately after each [xFilter](vtab.md#xfilter) and [xNext](vtab.md#xnext) invocation.

The xEof method is required for every virtual table implementation. <span id="xfilter"></span>

## 2.9. The xFilter Method

int (\*xFilter)(sqlite3_vtab_cursor\*, int idxNum, const char \*idxStr,\
              int argc, sqlite3_value \*\*argv);\

This method begins a search of a virtual table. The first argument is a cursor opened by [xOpen](vtab.md#xopen). The next two arguments define a particular search index previously chosen by [xBestIndex](vtab.md#xbestindex). The specific meanings of idxNum and idxStr are unimportant as long as xFilter and xBestIndex agree on what that meaning is.

The xBestIndex function may have requested the values of certain expressions using the aConstraintUsage\[\].argvIndex values of the [sqlite3_index_info](c3ref/index_info.md) structure. Those values are passed to xFilter using the argc and argv parameters.

If the virtual table contains one or more rows that match the search criteria, then the cursor must be left pointing at the first row. Subsequent calls to [xEof](vtab.md#xeof) must return false (zero). If there are no rows matching, then the cursor must be left in a state that will cause the [xEof](vtab.md#xeof) to return true (non-zero). The SQLite engine will use the [xColumn](vtab.md#xcolumn) and [xRowid](vtab.md#xrowid) methods to access that row content. The [xNext](vtab.md#xnext) method will be used to advance to the next row.

This method must return [SQLITE_OK](rescode.md#ok) if successful, or an sqlite [error code](rescode.md) if an error occurs.

The xFilter method is required for every virtual table implementation. <span id="xnext"></span>

## 2.10. The xNext Method

int (\*xNext)(sqlite3_vtab_cursor\*);\

The xNext method advances a [virtual table cursor](c3ref/vtab_cursor.md) to the next row of a result set initiated by [xFilter](vtab.md#xfilter). If the cursor is already pointing at the last row when this routine is called, then the cursor no longer points to valid data and a subsequent call to the [xEof](vtab.md#xeof) method must return true (non-zero). If the cursor is successfully advanced to another row of content, then subsequent calls to [xEof](vtab.md#xeof) must return false (zero).

This method must return [SQLITE_OK](rescode.md#ok) if successful, or an sqlite [error code](rescode.md) if an error occurs.

The xNext method is required for every virtual table implementation. <span id="xcolumn"></span>

## 2.11. The xColumn Method

int (\*xColumn)(sqlite3_vtab_cursor\*, sqlite3_context\*, int N);\

The SQLite core invokes this method in order to find the value for the N-th column of the current row. N is zero-based so the first column is numbered 0. The xColumn method may return its result back to SQLite using one of the following interfaces:

- [sqlite3_result_blob()](c3ref/result_blob.md)
- [sqlite3_result_blob64()](c3ref/result_blob.md)
- [sqlite3_result_double()](c3ref/result_blob.md)
- [sqlite3_result_int()](c3ref/result_blob.md)
- [sqlite3_result_int64()](c3ref/result_blob.md)
- [sqlite3_result_null()](c3ref/result_blob.md)
- [sqlite3_result_pointer()](c3ref/result_blob.md)
- [sqlite3_result_text()](c3ref/result_blob.md)
- [sqlite3_result_text16()](c3ref/result_blob.md)
- [sqlite3_result_text16le()](c3ref/result_blob.md)
- [sqlite3_result_text16be()](c3ref/result_blob.md)
- [sqlite3_result_text64()](c3ref/result_blob.md)
- [sqlite3_result_value()](c3ref/result_blob.md)
- [sqlite3_result_zeroblob()](c3ref/result_blob.md)
- [sqlite3_result_zeroblob64()](c3ref/result_blob.md)

If the xColumn method implementation calls none of the functions above, then the value of the column defaults to an SQL NULL.

To raise an error, the xColumn method should use one of the result_text() methods to set the error message text, then return an appropriate [error code](rescode.md). The xColumn method must return [SQLITE_OK](rescode.md#ok) on success.

The xColumn method is required for every virtual table implementation. <span id="xrowid"></span>

## 2.12. The xRowid Method

int (\*xRowid)(sqlite3_vtab_cursor \*pCur, sqlite_int64 \*pRowid);\

A successful invocation of this method will cause \*pRowid to be filled with the [rowid](lang_createtable.md#rowid) of row that the [virtual table cursor](c3ref/vtab_cursor.md) pCur is currently pointing at. This method returns [SQLITE_OK](rescode.md#ok) on success. It returns an appropriate [error code](rescode.md) on failure.

The xRowid method is required for every virtual table implementation. <span id="xupdate"></span>

## 2.13. The xUpdate Method

int (\*xUpdate)(\
  sqlite3_vtab \*pVTab,\
  int argc,\
  sqlite3_value \*\*argv,\
  sqlite_int64 \*pRowid\
);\

All changes to a virtual table are made using the xUpdate method. This one method can be used to insert, delete, or update.

The argc parameter specifies the number of entries in the argv array. The value of argc will be 1 for a pure delete operation or N+2 for an insert or replace or update where N is the number of columns in the table. In the previous sentence, N includes any hidden columns.

Every argv entry will have a non-NULL value in C but may contain the SQL value NULL. In other words, it is always true that `argv[i]!=0` for **i** between 0 and `argc-1`. However, it might be the case that `sqlite3_value_type(argv[i])==SQLITE_NULL`.

The argv\[0\] parameter is the [rowid](lang_createtable.md#rowid) of a row in the virtual table to be deleted. If argv\[0\] is an SQL NULL, then no deletion occurs.

The argv\[1\] parameter is the rowid of a new row to be inserted into the virtual table. If argv\[1\] is an SQL NULL, then the implementation must choose a rowid for the newly inserted row. Subsequent argv\[\] entries contain values of the columns of the virtual table, in the order that the columns were declared. The number of columns will match the table declaration that the [xConnect](vtab.md#xconnect) or [xCreate](vtab.md#xcreate) method made using the [sqlite3_declare_vtab()](c3ref/declare_vtab.md) call. All hidden columns are included.

When doing an insert without a rowid (argc\>1, argv\[1\] is an SQL NULL), on a virtual table that uses ROWID (but not on a [WITHOUT ROWID virtual table](vtab.md#worid)), the implementation must set \*pRowid to the rowid of the newly inserted row; this will become the value returned by the [sqlite3_last_insert_rowid()](c3ref/last_insert_rowid.md) function. Setting this value in all the other cases is a harmless no-op; the SQLite engine ignores the \*pRowid return value if argc==1 or argv\[1\] is not an SQL NULL.

Each call to xUpdate will fall into one of cases shown below. Not that references to **argv\[i\]** mean the SQL value held within the argv\[i\] object, not the argv\[i\] object itself.

> **argc = 1\
> argv\[0\] ≠ NULL**  
> DELETE: The single row with rowid or PRIMARY KEY equal to argv\[0\] is deleted. No insert occurs.
>
> **argc \> 1\
> argv\[0\] = NULL**  
> INSERT: A new row is inserted with column values taken from argv\[2\] and following. In a rowid virtual table, if argv\[1\] is an SQL NULL, then a new unique rowid is generated automatically. The argv\[1\] will be NULL for a [WITHOUT ROWID virtual table](vtab.md#worid), in which case the implementation should take the PRIMARY KEY value from the appropriate column in argv\[2\] and following.
>
> **argc \> 1\
> argv\[0\] ≠ NULL\
> argv\[0\] = argv\[1\]**  
> UPDATE: The row with rowid or PRIMARY KEY argv\[0\] is updated with new values in argv\[2\] and following parameters.
>
> **argc \> 1\
> argv\[0\] ≠ NULL\
> argv\[0\] ≠ argv\[1\]**  
> UPDATE with rowid or PRIMARY KEY change: The row with rowid or PRIMARY KEY argv\[0\] is updated with the rowid or PRIMARY KEY in argv\[1\] and new values in argv\[2\] and following parameters. This will occur when an SQL statement updates a rowid, as in the statement:
>
> > [UPDATE](lang_update.md) table SET rowid=rowid+1 WHERE ...;

The xUpdate method must return [SQLITE_OK](rescode.md#ok) if and only if it is successful. If a failure occurs, the xUpdate must return an appropriate [error code](rescode.md). On a failure, the pVTab-\>zErrMsg element may optionally be replaced with error message text stored in memory allocated from SQLite using functions such as [sqlite3_mprintf()](c3ref/mprintf.md) or [sqlite3_malloc()](c3ref/free.md).

If the xUpdate method violates some constraint of the virtual table (including, but not limited to, attempting to store a value of the wrong datatype, attempting to store a value that is too large or too small, or attempting to change a read-only value) then the xUpdate must fail with an appropriate [error code](rescode.md).

If the xUpdate method is performing an UPDATE, then [sqlite3_value_nochange(X)](c3ref/value_blob.md) can be used to discover which columns of the virtual table were actually modified by the UPDATE statement. The [sqlite3_value_nochange(X)](c3ref/value_blob.md) interface returns true for columns that do not change. On every UPDATE, SQLite will first invoke [xColumn](vtab.md#xcolumn) separately for each unchanging column in the table to obtain the value for that column. The [xColumn](vtab.md#xcolumn) method can check to see if the column is unchanged at the SQL level by invoking [sqlite3_vtab_nochange()](c3ref/vtab_nochange.md). If [xColumn](vtab.md#xcolumn) sees that the column is not being modified, it should return without setting a result using one of the [sqlite3_result_xxxxx()](c3ref/result_blob.md) interfaces. Only in that case [sqlite3_value_nochange()](c3ref/value_blob.md) will be true within the xUpdate method. If [xColumn](vtab.md#xcolumn) does invoke one or more [sqlite3_result_xxxxx()](c3ref/result_blob.md) interfaces, then SQLite understands that as a change in the value of the column and the [sqlite3_value_nochange()](c3ref/value_blob.md) call for that column within xUpdate will return false.

There might be one or more [sqlite3_vtab_cursor](c3ref/vtab_cursor.md) objects open and in use on the virtual table instance and perhaps even on the row of the virtual table when the xUpdate method is invoked. The implementation of xUpdate must be prepared for attempts to delete or modify rows of the table out from other existing cursors. If the virtual table cannot accommodate such changes, the xUpdate method must return an [error code](rescode.md).

The xUpdate method is optional. If the xUpdate pointer in the [sqlite3_module](c3ref/module.md) for a virtual table is a NULL pointer, then the virtual table is read-only. <span id="xfindfunction"></span>

## 2.14. The xFindFunction Method

int (\*xFindFunction)(\
  sqlite3_vtab \*pVtab,\
  int nArg,\
  const char \*zName,\
  void (\*\*pxFunc)(sqlite3_context\*,int,sqlite3_value\*\*),\
  void \*\*ppArg\
);\

This method is called during [sqlite3_prepare()](c3ref/prepare.md) to give the virtual table implementation an opportunity to overload functions. This method may be set to NULL in which case no overloading occurs.

When a function uses a column from a virtual table as its first argument, this method is called to see if the virtual table would like to overload the function. The first three parameters are inputs: the virtual table, the number of arguments to the function, and the name of the function. If no overloading is desired, this method returns 0. To overload the function, this method writes the new function implementation into \*pxFunc and writes user data into \*ppArg and returns either 1 or a number between [SQLITE_INDEX_CONSTRAINT_FUNCTION](c3ref/c_index_constraint_eq.md) and 255.

Historically, the return value from xFindFunction() was either zero or one. Zero means that the function is not overloaded and one means that it is overloaded. The ability to return values of [SQLITE_INDEX_CONSTRAINT_FUNCTION](c3ref/c_index_constraint_eq.md) or greater was added in version 3.25.0 (2018-09-15). If xFindFunction returns [SQLITE_INDEX_CONSTRAINT_FUNCTION](c3ref/c_index_constraint_eq.md) or greater, than means that the function takes two arguments and the function can be used as a boolean in the WHERE clause of a query and that the virtual table is able to exploit that function to speed up the query result. When xFindFunction returns [SQLITE_INDEX_CONSTRAINT_FUNCTION](c3ref/c_index_constraint_eq.md) or larger, the value returned becomes the [sqlite3_index_info](c3ref/index_info.md).aConstraint.op value for one of the constraints passed into [xBestIndex()](vtab.md#xbestindex). The first argument to the function is the column identified by aConstraint\[\].iColumn field of the constraint and the second argument to the function is the value that will be passed into [xFilter()](vtab.md#xfilter) (if the aConstraintUsage\[\].argvIndex value is set) or the value returned from [sqlite3_vtab_rhs_value()](c3ref/vtab_rhs_value.md).

The [Geopoly module](geopoly.md) is an example of a virtual table that makes use of [SQLITE_INDEX_CONSTRAINT_FUNCTION](c3ref/c_index_constraint_eq.md) to improve performance. The xFindFunction() method for Geopoly returns SQLITE_INDEX_CONSTRAINT_FUNCTION for the [geopoly_overlap()](geopoly.md#goverlap) SQL function and it returns SQLITE_INDEX_CONSTRAINT_FUNCTION+1 for the [geopoly_within()](geopoly.md#gwithin) SQL function. This permits search optimizations for queries such as:

SELECT \* FROM geopolytab WHERE geopoly_overlap(\_shape, \$query_polygon);\
SELECT \* FROM geopolytab WHERE geopoly_within(\_shape, \$query_polygon);\

Note that infix functions ([LIKE](lang_expr.md#like), [GLOB](lang_expr.md#glob), [REGEXP](lang_expr.md#regexp), and [MATCH](lang_expr.md#match)) reverse the order of their arguments. So "like(A,B)" would normally work the same as "B like A". However, xFindFunction() always looks at the left-most argument, not the first logical argument. Hence, for the form "B like A", SQLite looks at the left operand "B" and if that operand is a virtual table column it invokes the xFindFunction() method on that virtual table. But if the form "like(A,B)" is used instead, then SQLite checks the A term to see if it is column of a virtual table and if so it invokes the xFindFunction() method for the virtual table of column A.

The function pointer returned by this routine must be valid for the lifetime of the [sqlite3_vtab](c3ref/vtab.md) object given in the first parameter. <span id="xBegin"></span>

## 2.15. The xBegin Method

int (\*xBegin)(sqlite3_vtab \*pVTab);\

This method begins a transaction on a virtual table. This method is optional. The xBegin pointer of [sqlite3_module](c3ref/module.md) may be NULL.

This method is always followed by one call to either the [xCommit](vtab.md#xcommit) or [xRollback](vtab.md#xrollback) method. Virtual table transactions do not nest, so the xBegin method will not be invoked more than once on a single virtual table without an intervening call to either [xCommit](vtab.md#xcommit) or [xRollback](vtab.md#xrollback). Multiple calls to other methods can and likely will occur in between the xBegin and the corresponding [xCommit](vtab.md#xcommit) or [xRollback](vtab.md#xrollback). <span id="xsync"></span>

## 2.16. The xSync Method

int (\*xSync)(sqlite3_vtab \*pVTab);\

This method signals the start of a two-phase commit on a virtual table. This method is optional. The xSync pointer of [sqlite3_module](c3ref/module.md) may be NULL.

This method is only invoked after a call to the [xBegin](vtab.md#xBegin) method and prior to an [xCommit](vtab.md#xcommit) or [xRollback](vtab.md#xrollback). In order to implement two-phase commit, the xSync method on all virtual tables is invoked prior to invoking the [xCommit](vtab.md#xcommit) method on any virtual table. If any of the xSync methods fail, the entire transaction is rolled back. <span id="xcommit"></span>

## 2.17. The xCommit Method

int (\*xCommit)(sqlite3_vtab \*pVTab);\

This method causes a virtual table transaction to commit. This method is optional. The xCommit pointer of [sqlite3_module](c3ref/module.md) may be NULL.

A call to this method always follows a prior call to [xBegin](vtab.md#xBegin) and [xSync](vtab.md#xsync). <span id="xrollback"></span>

## 2.18. The xRollback Method

int (\*xRollback)(sqlite3_vtab \*pVTab);\

This method causes a virtual table transaction to rollback. This method is optional. The xRollback pointer of [sqlite3_module](c3ref/module.md) may be NULL.

A call to this method always follows a prior call to [xBegin](vtab.md#xBegin). <span id="xrename"></span>

## 2.19. The xRename Method

int (\*xRename)(sqlite3_vtab \*pVtab, const char \*zNew);\

This method notifies the virtual table implementation that the virtual table will be given a new name. If this method returns [SQLITE_OK](rescode.md#ok) then SQLite renames the table. If this method returns an [error code](rescode.md) then the renaming is prevented.

The xRename method is optional. If omitted, then the virtual table may not be renamed using the ALTER TABLE RENAME command.

The [PRAGMA legacy_alter_table](pragma.md#pragma_legacy_alter_table) setting is enabled prior to invoking this method, and the value for legacy_alter_table is restored after this method finishes. This is necessary for the correct operation of virtual tables that make use of [shadow tables](vtab.md#xshadowname) where the shadow tables must be renamed to match the new virtual table name. If the legacy_alter_format is off, then the xConnect method will be invoked for the virtual table every time the xRename method tries to change the name of the shadow table. <span id="xsavepoint"></span>

## 2.20. The xSavepoint, xRelease, and xRollbackTo Methods

int (\*xSavepoint)(sqlite3_vtab \*pVtab, int);\
int (\*xRelease)(sqlite3_vtab \*pVtab, int);\
int (\*xRollbackTo)(sqlite3_vtab \*pVtab, int);\

These methods provide the virtual table implementation an opportunity to implement nested transactions. They are always optional and will only be called in SQLite [version 3.7.7](releaselog/3_7_7.md) (2011-06-23) and later.

When xSavepoint(X,N) is invoked, that is a signal to the virtual table X that it should save its current state as savepoint N. A subsequent call to xRollbackTo(X,R) means that the state of the virtual table should return to what it was when xSavepoint(X,R) was last called. The call to xRollbackTo(X,R) will invalidate all savepoints with N\>R; none of the invalided savepoints will be rolled back or released without first being reinitialized by a call to xSavepoint(). A call to xRelease(X,M) invalidates all savepoints where N\>=M.

None of the xSavepoint(), xRelease(), or xRollbackTo() methods will ever be called except in between calls to xBegin() and either xCommit() or xRollback().

<span id="xshadowname"></span>

## 2.21. The xShadowName Method

Some virtual table implementations (ex: [FTS3](fts3.md), [FTS5](fts5.md), and [RTREE](rtree.md)) make use of real (non-virtual) database tables to store content. For example, when content is inserted into the FTS3 virtual table, the data is ultimately stored in real tables named "%\_content", "%\_segdir", "%\_segments", "%\_stat", and "%\_docsize" where "%" is the name of the original virtual table. These auxiliary real tables that store content for a virtual table are called "shadow tables". See ([1](fts3.md#*shadowtab)), ([2](fts5.md#fts5shadowtables)), and ([3](rtree.md#xshadow)) for additional information.

The xShadowName method exists to allow SQLite to determine whether a certain real table is in fact a shadow table for a virtual table.

SQLite understands a real table to be a shadow table if all of the following are true:

- The name of the table contains one or more "\_" characters.
- The part of the name prior to the last "\_" exactly matches the name of a virtual table that was created using [CREATE VIRTUAL TABLE](lang_createvtab.md). (Shadow tables are not recognized for [eponymous virtual tables](vtab.md#epovtab) and [table-valued functions](vtab.md#tabfunc2).)
- The virtual table contains an xShadowName method.
- The xShadowName method returns true when its input is the part of the table name past the last "\_" character.

If SQLite recognizes a table as a shadow table, and if the [SQLITE_DBCONFIG_DEFENSIVE](c3ref/c_dbconfig_defensive.md#sqlitedbconfigdefensive) flag is set, then the shadow table is read-only for ordinary SQL statements. The shadow table can still be written, but only by SQL that is invoked from within one of the methods of some virtual table implementation.

The whole point of the xShadowName method is to protect the content of shadow tables from being corrupted by hostile SQL. Every virtual table implementation that uses shadow tables should be able to detect and cope with corrupted shadow table content. However, bugs in a particular virtual table implementation might allow a deliberately corrupted shadow table to cause a crash or other malfunction. The xShadowName mechanism seeks to avoid zero-day exploits by preventing ordinary SQL statements from deliberately corrupting shadow tables.

Shadow tables are read/write by default. Shadow tables only become read-only when the [SQLITE_DBCONFIG_DEFENSIVE](c3ref/c_dbconfig_defensive.md#sqlitedbconfigdefensive) flag is set using [sqlite3_db_config()](c3ref/db_config.md). Shadow tables need to be read/write by default in order to maintain backwards compatibility. For example, the SQL text generated by the [.dump](cli.md#dump) command of the [CLI](cli.md) writes directly into shadow tables. <span id="xintegrity"></span>

## 2.22. The xIntegrity Method

If the iVersion for an sqlite3_module is 4 or more and the xIntegrity method is not NULL, then the [PRAGMA integrity_check](pragma.md#pragma_integrity_check) and [PRAGMA quick_check](pragma.md#pragma_quick_check) commands will invoke xIntegrity as part of its processing. If the xIntegrity method writes an error message string into the fifth parameter, then PRAGMA integrity_check will report that error as part of its output. So, in other words, the xIntegrity method allows the [PRAGMA integrity_check](pragma.md#pragma_integrity_check) command to verify the integrity of content stored in a virtual table.

The xIntegrity method is called with five parameters:

- **pVTab** → A pointer to the [sqlite3_vtab](c3ref/vtab.md) object that is the virtual table being checked.
- **zSchema** → The name of the schema ("main", "temp", etc.) in which the virtual table is defined.
- **zTabName** → The name of the virtual table.
- **mFlags** → A flag to indicate whether this is an "integrity_check" or a "quick_check". Currently, this parameter will always be either 0 or 1, though future versions of SQLite might use other bits of the integer to indicate additional processing options.
- **pzErr** → This parameter points to a "char\*" that is initialized to NULL. The xIntegrity() implementation should make \*pzErr point to an error string obtained from sqlite3_malloc() or equivalent if it finds any problems.

The xIntegrity method should normally return SQLITE_OK - even if it finds problems in the content of the virtual table. Any other error code means that the xIntegrity method itself encountered problems while trying to evaluate the virtual table content. So, for example, if the inverted index for [FTS5](fts5.md) is found to be internally inconsistent, then the xIntegrity method should write an appropriate error message into the pzErr parameter and return SQLITE_OK. But if the xIntegrity method is unable to complete its evaluation of the virtual table content due to running out of memory, then it should return SQLITE_NOMEM.

If an error message is generated, space to hold the error message string should be obtained from [sqlite3_malloc64()](c3ref/free.md) or the equivalent. Ownership of the error message string will pass to the SQLite core when xIntegrity returns. The core will make sure that [sqlite3_free()](c3ref/free.md) is invoked to reclaim the memory when it has finished with the error message. The PRAGMA integrity_check command that invokes the xIntegrity method does not change the returned error message. The xIntegrity method itself should include the name of the virtual table as part of the message. The zSchema and zName parameters are provided to make that easier.

The mFlags parameter is currently a boolean value (either 0 or 1) that indicates if the xIntegrity method was called due to [PRAGMA integrity_check](pragma.md#pragma_integrity_check) (mFlags==0) or due to [PRAGMA quick_check](pragma.md#pragma_quick_check) (mFlags==1). Generally speaking, the xIntegrity method should do whatever validity checking it can accomplish in linear time regardless, but only do checking that requires superlinear time if `(mFlags&1)==0`. Future versions of SQLite might use higher-order bits of the mFlags parameter to indicate additional processing options.

Support for the xIntegrity method was added in SQLite version 3.44.0 (2023-11-01). In that same release, the xIntegrity method was added to many built-in virtual tables, such as [FTS3](fts3.md), [FTS5](fts5.md), and [RTREE](rtree.md) so that the content of those tables will henceforth be automatically checked for consistency when [PRAGMA integrity_check](pragma.md#pragma_integrity_check) is run.
