---
title: Pragma statements supported by SQLite
source_url: https://www.sqlite.org/pragma.html
source_path: pragma.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: tools-extensions
order: 3720
---

# PRAGMA Statements

The PRAGMA statement is an SQL extension specific to SQLite and used to modify the operation of the SQLite library or to query the SQLite library for internal (non-table) data. The PRAGMA statement is issued using the same interface as other SQLite commands (e.g. [SELECT](lang_select.md), [INSERT](lang_insert.md)) but is different in the following important respects:

- The pragma command is specific to SQLite and is not compatible with any other SQL database engine.
- Specific pragma statements may be removed and others added in future releases of SQLite. There is no guarantee of backwards compatibility.
- No error messages are generated if an unknown pragma is issued. Unknown pragmas are simply ignored. This means if there is a typo in a pragma statement the library does not inform the user of the fact.
- Some pragmas take effect during the SQL compilation stage, not the execution stage. This means if using the C-language [sqlite3_prepare()](c3ref/prepare.md), [sqlite3_step()](c3ref/step.md), [sqlite3_finalize()](c3ref/finalize.md) API (or similar in a wrapper interface), the pragma may run during the [sqlite3_prepare()](c3ref/prepare.md) call, not during the [sqlite3_step()](c3ref/step.md) call as normal SQL statements do. Or the pragma might run during sqlite3_step() just like normal SQL statements. Whether or not the pragma runs during sqlite3_prepare() or sqlite3_step() depends on the pragma and on the specific release of SQLite.
- The [EXPLAIN](lang_explain.md) and [EXPLAIN QUERY PLAN](eqp.md) prefixes to SQL statements only affect the behavior of the statement during [sqlite3_step()](c3ref/step.md). That means that PRAGMA statements that take effect during [sqlite3_prepare()](c3ref/prepare.md) will behave the same way regardless of whether or not they are prefaced by "EXPLAIN".

The C-language API for SQLite provides the [SQLITE_FCNTL_PRAGMA](c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntlpragma) [file control](c3ref/file_control.md) which gives [VFS](vfs.md) implementations the opportunity to add new PRAGMA statements or to override the meaning of built-in PRAGMA statements.

------------------------------------------------------------------------

<span id="syntax"></span>

## PRAGMA command syntax

**[pragma-stmt:](syntax/pragma-stmt.md)** hide

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSJmb250LXNpemU6aW5pdGlhbDsiIGNsYXNzPSJwaWtjaHIiIHZpZXdib3g9IjAgMCA4MjQuMzUyIDk5LjU3NiIgZGF0YS1waWtjaHItZGF0ZT0iMjAyNTAzMTkxNjE5NDMiPgo8Y2lyY2xlIGN4PSI1Ljc2IiBjeT0iMTcuMjgiIHI9IjMuNiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiPjwvY2lyY2xlPgo8cG9seWdvbiBwb2ludHM9IjMyLjQsMTcuMjggMjAuODgsMjEuNiAyMC44OCwxMi45NiIgc3R5bGU9ImZpbGw6cmdiKDAsMCwwKSI+PC9wb2x5Z29uPgo8cGF0aCBkPSJNOS4zNiwxNy4yOEwyNi42NCwxNy4yOCIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+CjxwYXRoIGQ9Ik00Ny41MiwzMi40TDEwNC4zNzEsMzIuNEExNS4xMiAxNS4xMiAwIDAgMCAxMTkuNDkxIDE3LjI4QTE1LjEyIDE1LjEyIDAgMCAwIDEwNC4zNzEgMi4xNkw0Ny41MiwyLjE2QTE1LjEyIDE1LjEyIDAgMCAwIDMyLjQgMTcuMjhBMTUuMTIgMTUuMTIgMCAwIDAgNDcuNTIgMzIuNFoiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8dGV4dCB4PSI3NS45NDU2IiB5PSIxNy4yOCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0icmdiKDAsMCwwKSIgZG9taW5hbnQtYmFzZWxpbmU9ImNlbnRyYWwiPlBSQUdNQTwvdGV4dD4KPHBvbHlnb24gcG9pbnRzPSIxNTUuNDkxLDE3LjI4IDE0My45NzEsMjEuNiAxNDMuOTcxLDEyLjk2IiBzdHlsZT0iZmlsbDpyZ2IoMCwwLDApIj48L3BvbHlnb24+CjxwYXRoIGQ9Ik0xMTkuNDkxLDE3LjI4TDE0OS43MzEsMTcuMjgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cGF0aCBkPSJNMTcwLjYxMSwzMi40TDI2Ni45NzYsMzIuNEExNS4xMiAxNS4xMiAwIDAgMCAyODIuMDk2IDE3LjI4QTE1LjEyIDE1LjEyIDAgMCAwIDI2Ni45NzYgMi4xNkwxNzAuNjExLDIuMTZBMTUuMTIgMTUuMTIgMCAwIDAgMTU1LjQ5MSAxNy4yOEExNS4xMiAxNS4xMiAwIDAgMCAxNzAuNjExIDMyLjRaIiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHRleHQgeD0iMjE4Ljc5NCIgeT0iMTcuMjgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9InJnYigwLDAsMCkiIGRvbWluYW50LWJhc2VsaW5lPSJjZW50cmFsIj5zY2hlbWEtbmFtZTwvdGV4dD4KPHBvbHlnb24gcG9pbnRzPSIzMDUuMTM2LDE3LjI4IDI5My42MTYsMjEuNiAyOTMuNjE2LDEyLjk2IiBzdHlsZT0iZmlsbDpyZ2IoMCwwLDApIj48L3BvbHlnb24+CjxwYXRoIGQ9Ik0yODIuMDk2LDE3LjI4TDI5OS4zNzYsMTcuMjgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cGF0aCBkPSJNMzIwLjI1NiwzMi40QTE1LjEyIDE1LjEyIDAgMCAwIDMzNS4zNzYgMTcuMjhBMTUuMTIgMTUuMTIgMCAwIDAgMzIwLjI1NiAyLjE2QTE1LjEyIDE1LjEyIDAgMCAwIDMwNS4xMzYgMTcuMjhBMTUuMTIgMTUuMTIgMCAwIDAgMzIwLjI1NiAzMi40WiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+Cjx0ZXh0IHg9IjMyMC4yNTYiIHk9IjE3LjI4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0icmdiKDAsMCwwKSIgZG9taW5hbnQtYmFzZWxpbmU9ImNlbnRyYWwiPi48L3RleHQ+Cjxwb2x5Z29uIHBvaW50cz0iMzcxLjM3NiwxNy4yOCAzNTkuODU2LDIxLjYgMzU5Ljg1NiwxMi45NiIgc3R5bGU9ImZpbGw6cmdiKDAsMCwwKSI+PC9wb2x5Z29uPgo8cGF0aCBkPSJNMzM1LjM3NiwxNy4yOEwzNjUuNjE2LDE3LjI4IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHBhdGggZD0iTTM4Ni40OTYsMzIuNEw0ODMuNjY3LDMyLjRBMTUuMTIgMTUuMTIgMCAwIDAgNDk4Ljc4NyAxNy4yOEExNS4xMiAxNS4xMiAwIDAgMCA0ODMuNjY3IDIuMTZMMzg2LjQ5NiwyLjE2QTE1LjEyIDE1LjEyIDAgMCAwIDM3MS4zNzYgMTcuMjhBMTUuMTIgMTUuMTIgMCAwIDAgMzg2LjQ5NiAzMi40WiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+Cjx0ZXh0IHg9IjQzNS4wODIiIHk9IjE3LjI4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSJyZ2IoMCwwLDApIiBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCI+cHJhZ21hLW5hbWU8L3RleHQ+Cjxwb2x5Z29uIHBvaW50cz0iNTQwLjMwNyw4Mi4yOTYgNTI4Ljc4Nyw4Ni42MTYgNTI4Ljc4Nyw3Ny45NzYiIHN0eWxlPSJmaWxsOnJnYigwLDAsMCkiPjwvcG9seWdvbj4KPHBhdGggZD0iTTQ5OC43ODcsMTcuMjggTCA1MDYuMjg3LDE3LjI4IFEgNTEzLjc4NywxNy4yOCA1MTMuNzg3LDMyLjI4IEwgNTEzLjc4Nyw2Ny4yOTYgUSA1MTMuNzg3LDgyLjI5NiA1MjQuMTY3LDgyLjI5NiBMIDUzNC41NDcsODIuMjk2IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHBhdGggZD0iTTU1NS40MjcsOTcuNDE2QTE1LjEyIDE1LjEyIDAgMCAwIDU3MC41NDcgODIuMjk2QTE1LjEyIDE1LjEyIDAgMCAwIDU1NS40MjcgNjcuMTc2QTE1LjEyIDE1LjEyIDAgMCAwIDU0MC4zMDcgODIuMjk2QTE1LjEyIDE1LjEyIDAgMCAwIDU1NS40MjcgOTcuNDE2WiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+Cjx0ZXh0IHg9IjU1NS40MjciIHk9IjgyLjI5NiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9InJnYigwLDAsMCkiIGRvbWluYW50LWJhc2VsaW5lPSJjZW50cmFsIj4oPC90ZXh0Pgo8cG9seWdvbiBwb2ludHM9IjU5My41ODcsODIuMjk2IDU4Mi4wNjcsODYuNjE2IDU4Mi4wNjcsNzcuOTc2IiBzdHlsZT0iZmlsbDpyZ2IoMCwwLDApIj48L3BvbHlnb24+CjxwYXRoIGQ9Ik01NzAuNTQ3LDgyLjI5Nkw1ODcuODI3LDgyLjI5NiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+CjxwYXRoIGQ9Ik01OTMuNTg3LDk3LjQxNkw3MjAuMTkyLDk3LjQxNkw3MjAuMTkyLDY3LjE3Nkw1OTMuNTg3LDY3LjE3NloiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8dGV4dCB4PSI2NTYuODkiIHk9IjgyLjI5NiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0icmdiKDAsMCwwKSIgZG9taW5hbnQtYmFzZWxpbmU9ImNlbnRyYWwiPnByYWdtYS12YWx1ZTwvdGV4dD4KPHBvbHlnb24gcG9pbnRzPSI3NDMuMjMyLDgyLjI5NiA3MzEuNzEyLDg2LjYxNiA3MzEuNzEyLDc3Ljk3NiIgc3R5bGU9ImZpbGw6cmdiKDAsMCwwKSI+PC9wb2x5Z29uPgo8cGF0aCBkPSJNNzIwLjE5Miw4Mi4yOTZMNzM3LjQ3Miw4Mi4yOTYiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cGF0aCBkPSJNNzU4LjM1Miw5Ny40MTZBMTUuMTIgMTUuMTIgMCAwIDAgNzczLjQ3MiA4Mi4yOTZBMTUuMTIgMTUuMTIgMCAwIDAgNzU4LjM1MiA2Ny4xNzZBMTUuMTIgMTUuMTIgMCAwIDAgNzQzLjIzMiA4Mi4yOTZBMTUuMTIgMTUuMTIgMCAwIDAgNzU4LjM1MiA5Ny40MTZaIiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHRleHQgeD0iNzU4LjM1MiIgeT0iODIuMjk2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0icmdiKDAsMCwwKSIgZG9taW5hbnQtYmFzZWxpbmU9ImNlbnRyYWwiPik8L3RleHQ+Cjxwb2x5Z29uIHBvaW50cz0iODE0Ljk5MiwxNy4yOCA4MDMuNDcyLDIxLjYgODAzLjQ3MiwxMi45NiIgc3R5bGU9ImZpbGw6cmdiKDAsMCwwKSI+PC9wb2x5Z29uPgo8cGF0aCBkPSJNNzczLjQ3Miw4Mi4yOTYgTCA3ODAuOTcyLDgyLjI5NiBRIDc4OC40NzIsODIuMjk2IDc4OC40NzIsNjcuMjk2IEwgNzg4LjQ3MiwzMi4yOCBRIDc4OC40NzIsMTcuMjggNzk4Ljg1MiwxNy4yOCBMIDgwOS4yMzIsMTcuMjgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8Y2lyY2xlIGN4PSI4MTguNTkyIiBjeT0iMTcuMjgiIHI9IjMuNiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiPjwvY2lyY2xlPgo8cG9seWdvbiBwb2ludHM9IjU0MC4zMDcsNDQuNDk2IDUyOC43ODcsNDguODE2IDUyOC43ODcsNDAuMTc2IiBzdHlsZT0iZmlsbDpyZ2IoMCwwLDApIj48L3BvbHlnb24+CjxwYXRoIGQ9Ik00OTguNzg3LDE3LjI4IEwgNTA2LjI4NywxNy4yOCBRIDUxMy43ODcsMTcuMjggNTEzLjc4NywzMC44ODggUSA1MTMuNzg3LDQ0LjQ5NiA1MjQuMTY3LDQ0LjQ5NiBMIDUzNC41NDcsNDQuNDk2IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHBhdGggZD0iTTU1NS40MjcsNTkuNjE2QTE1LjEyIDE1LjEyIDAgMCAwIDU3MC41NDcgNDQuNDk2TDU3MC41NDcsNDQuNDk2QTE1LjEyIDE1LjEyIDAgMCAwIDU1NS40MjcgMjkuMzc2QTE1LjEyIDE1LjEyIDAgMCAwIDU0MC4zMDcgNDQuNDk2TDU0MC4zMDcsNDQuNDk2QTE1LjEyIDE1LjEyIDAgMCAwIDU1NS40MjcgNTkuNjE2WiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+Cjx0ZXh0IHg9IjU1NS40MjciIHk9IjQ0LjQ5NiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9InJnYigwLDAsMCkiIGRvbWluYW50LWJhc2VsaW5lPSJjZW50cmFsIj49PC90ZXh0Pgo8cG9seWdvbiBwb2ludHM9IjU5My41ODcsNDQuNDk2IDU4Mi4wNjcsNDguODE2IDU4Mi4wNjcsNDAuMTc2IiBzdHlsZT0iZmlsbDpyZ2IoMCwwLDApIj48L3BvbHlnb24+CjxwYXRoIGQ9Ik01NzAuNTQ3LDQ0LjQ5Nkw1ODcuODI3LDQ0LjQ5NiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+CjxwYXRoIGQ9Ik01OTMuNTg3LDU5LjYxNkw3MjAuMTkyLDU5LjYxNkw3MjAuMTkyLDI5LjM3Nkw1OTMuNTg3LDI5LjM3NloiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8dGV4dCB4PSI2NTYuODkiIHk9IjQ0LjQ5NiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0icmdiKDAsMCwwKSIgZG9taW5hbnQtYmFzZWxpbmU9ImNlbnRyYWwiPnByYWdtYS12YWx1ZTwvdGV4dD4KPHBvbHlnb24gcG9pbnRzPSI3NzMuNDcyLDQ0LjQ5NiA3NjEuOTUyLDQ4LjgxNiA3NjEuOTUyLDQwLjE3NiIgc3R5bGU9ImZpbGw6cmdiKDAsMCwwKSI+PC9wb2x5Z29uPgo8cGF0aCBkPSJNNzIwLjE5Miw0NC40OTZMNzY3LjcxMiw0NC40OTYiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cGF0aCBkPSJNNzczLjQ3Miw0NC40OTYgTCA3ODAuOTcyLDQ0LjQ5NiBRIDc4OC40NzIsNDQuNDk2IDc4OC40NzIsMzYuOTk2IEwgNzg4LjQ3MiwyOS40OTYiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cG9seWdvbiBwb2ludHM9IjY1Ni44OSwxNy4yOCA2NDUuMzcsMjEuNiA2NDUuMzcsMTIuOTYiIHN0eWxlPSJmaWxsOnJnYigwLDAsMCkiPjwvcG9seWdvbj4KPHBhdGggZD0iTTQ5OC43ODcsMTcuMjhMNjUxLjEzLDE3LjI4IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHBhdGggZD0iTTY1Ni44OSwxNy4yOEw4MDMuNDcyLDE3LjI4IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHBvbHlnb24gcG9pbnRzPSIyMTguNzk0LDQ0LjQ5NiAyMDcuMjc0LDQ4LjgxNiAyMDcuMjc0LDQwLjE3NiIgc3R5bGU9ImZpbGw6cmdiKDAsMCwwKSI+PC9wb2x5Z29uPgo8cGF0aCBkPSJNMTE5LjQ5MSwxNy4yOCBMIDEyNi45OTEsMTcuMjggUSAxMzQuNDkxLDE3LjI4IDEzNC40OTEsMzAuODg4IFEgMTM0LjQ5MSw0NC40OTYgMTQ5LjQ5MSw0NC40OTYgTCAxOTguMDM0LDQ0LjQ5NiBMIDIxMy4wMzQsNDQuNDk2IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHBhdGggZD0iTTIxOC43OTQsNDQuNDk2IEwgMzM1LjM3Niw0NC40OTYgUSAzNTAuMzc2LDQ0LjQ5NiAzNTAuMzc2LDMwLjg4OCBRIDM1MC4zNzYsMTcuMjggMzU3Ljg3NiwxNy4yOCBMIDM2NS4zNzYsMTcuMjgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8L3N2Zz4=" class="pikchr" />

**[pragma-value:](syntax/pragma-value.md)** hide

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSJmb250LXNpemU6aW5pdGlhbDsiIGNsYXNzPSJwaWtjaHIiIHZpZXdib3g9IjAgMCAyNjQuNDk5IDExMC4xNiIgZGF0YS1waWtjaHItZGF0ZT0iMjAyNTAzMTkxNjE5NDMiPgo8Y2lyY2xlIGN4PSI1Ljc2IiBjeT0iMTcuMjgiIHI9IjMuNiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiPjwvY2lyY2xlPgo8cG9seWdvbiBwb2ludHM9IjYzLjM2LDE3LjI4IDUxLjg0LDIxLjYgNTEuODQsMTIuOTYiIHN0eWxlPSJmaWxsOnJnYigwLDAsMCkiPjwvcG9seWdvbj4KPHBhdGggZD0iTTkuMzYsMTcuMjhMNTcuNiwxNy4yOCIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+CjxwYXRoIGQ9Ik02My4zNiwzMi40TDIwMS4xMzksMzIuNEwyMDEuMTM5LDIuMTZMNjMuMzYsMi4xNloiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8dGV4dCB4PSIxMzIuMjUiIHk9IjE3LjI4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSJyZ2IoMCwwLDApIiBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCI+c2lnbmVkLW51bWJlcjwvdGV4dD4KPHBvbHlnb24gcG9pbnRzPSIyNTUuMTM5LDE3LjI4IDI0My42MTksMjEuNiAyNDMuNjE5LDEyLjk2IiBzdHlsZT0iZmlsbDpyZ2IoMCwwLDApIj48L3BvbHlnb24+CjxwYXRoIGQ9Ik0yMDEuMTM5LDE3LjI4TDI0OS4zNzksMTcuMjgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8Y2lyY2xlIGN4PSIyNTguNzM5IiBjeT0iMTcuMjgiIHI9IjMuNiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiPjwvY2lyY2xlPgo8cGF0aCBkPSJNNzguNDgsNzAuMkwxMDUuNjEsNzAuMkExNS4xMiAxNS4xMiAwIDAgMCAxMjAuNzMgNTUuMDhMMTIwLjczLDU1LjA4QTE1LjEyIDE1LjEyIDAgMCAwIDEwNS42MSAzOS45Nkw3OC40OCwzOS45NkExNS4xMiAxNS4xMiAwIDAgMCA2My4zNiA1NS4wOEw2My4zNiw1NS4wOEExNS4xMiAxNS4xMiAwIDAgMCA3OC40OCA3MC4yWiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+Cjx0ZXh0IHg9IjkyLjA0NDgiIHk9IjU1LjA4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSJyZ2IoMCwwLDApIiBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCI+bmFtZTwvdGV4dD4KPHBhdGggZD0iTTc4LjQ4LDEwOEwxNzEuNzM0LDEwOEExNS4xMiAxNS4xMiAwIDAgMCAxODYuODU0IDkyLjg4QTE1LjEyIDE1LjEyIDAgMCAwIDE3MS43MzQgNzcuNzZMNzguNDgsNzcuNzZBMTUuMTIgMTUuMTIgMCAwIDAgNjMuMzYgOTIuODhBMTUuMTIgMTUuMTIgMCAwIDAgNzguNDggMTA4WiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+Cjx0ZXh0IHg9IjEyNS4xMDciIHk9IjkyLjg4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSJyZ2IoMCwwLDApIiBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCI+c2lnbmVkLWxpdGVyYWw8L3RleHQ+Cjxwb2x5Z29uIHBvaW50cz0iNjMuMzYsOTIuODggNTEuODQsOTcuMiA1MS44NCw4OC41NiIgc3R5bGU9ImZpbGw6cmdiKDAsMCwwKSI+PC9wb2x5Z29uPgo8cGF0aCBkPSJNMjEuODQsMTcuMjggTCAyOS4zNCwxNy4yOCBRIDM2Ljg0LDE3LjI4IDM2Ljg0LDMyLjI4IEwgMzYuODQsNzcuODggUSAzNi44NCw5Mi44OCA0Ny4yMiw5Mi44OCBMIDU3LjYsOTIuODgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cG9seWdvbiBwb2ludHM9IjIwMS4xMzksOTIuODggMTg5LjYxOSw5Ny4yIDE4OS42MTksODguNTYiIHN0eWxlPSJmaWxsOnJnYigwLDAsMCkiPjwvcG9seWdvbj4KPHBhdGggZD0iTTE4Ni44NTQsOTIuODhMMTk1LjM3OSw5Mi44OCIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+CjxwYXRoIGQ9Ik0yMDEuMTM5LDkyLjg4IEwgMjA4LjYzOSw5Mi44OCBRIDIxNi4xMzksOTIuODggMjE2LjEzOSw3Ny44OCBMIDIxNi4xMzksMzIuMjggUSAyMTYuMTM5LDE3LjI4IDIyMy42MzksMTcuMjggTCAyMzEuMTM5LDE3LjI4IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHBvbHlnb24gcG9pbnRzPSIyMDEuMTM5LDU1LjA4IDE4OS42MTksNTkuNCAxODkuNjE5LDUwLjc2IiBzdHlsZT0iZmlsbDpyZ2IoMCwwLDApIj48L3BvbHlnb24+CjxwYXRoIGQ9Ik0xMjAuNzMsNTUuMDhMMTk1LjM3OSw1NS4wOCIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+CjxwYXRoIGQ9Ik0yMDEuMTM5LDU1LjA4IEwgMjA4LjYzOSw1NS4wOCBRIDIxNi4xMzksNTUuMDggMjE2LjEzOSw0Ny41OCBMIDIxNi4xMzksNDAuMDgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cG9seWdvbiBwb2ludHM9IjYzLjM2LDU1LjA4IDUxLjg0LDU5LjQgNTEuODQsNTAuNzYiIHN0eWxlPSJmaWxsOnJnYigwLDAsMCkiPjwvcG9seWdvbj4KPHBhdGggZD0iTTM2Ljg0LDM5Ljk2IEwgMzYuODQsNDcuNTIgUSAzNi44NCw1NS4wOCA0Ny4yMiw1NS4wOCBMIDU3LjYsNTUuMDgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8L3N2Zz4=" class="pikchr" />

**[signed-number:](syntax/signed-number.md)** show

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSJmb250LXNpemU6aW5pdGlhbDsiIGNsYXNzPSJwaWtjaHIiIHZpZXdib3g9IjAgMCAyOTIuMDEzIDk5LjU3NiIgZGF0YS1waWtjaHItZGF0ZT0iMjAyNTAzMTkxNjE5NDMiPgo8Y2lyY2xlIGN4PSI1Ljc2IiBjeT0iMTcuMjgiIHI9IjMuNiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiPjwvY2lyY2xlPgo8cG9seWdvbiBwb2ludHM9IjUwLjg4LDQ0LjQ5NiAzOS4zNiw0OC44MTYgMzkuMzYsNDAuMTc2IiBzdHlsZT0iZmlsbDpyZ2IoMCwwLDApIj48L3BvbHlnb24+CjxwYXRoIGQ9Ik05LjM2LDE3LjI4IEwgMTYuODYsMTcuMjggUSAyNC4zNiwxNy4yOCAyNC4zNiwzMC44ODggUSAyNC4zNiw0NC40OTYgMzQuNzQsNDQuNDk2IEwgNDUuMTIsNDQuNDk2IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHBhdGggZD0iTTY2LDU5LjYxNkExNS4xMiAxNS4xMiAwIDAgMCA4MS4xMiA0NC40OTZMODEuMTIsNDQuNDk2QTE1LjEyIDE1LjEyIDAgMCAwIDY2IDI5LjM3NkExNS4xMiAxNS4xMiAwIDAgMCA1MC44OCA0NC40OTZMNTAuODgsNDQuNDk2QTE1LjEyIDE1LjEyIDAgMCAwIDY2IDU5LjYxNloiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8dGV4dCB4PSI2NiIgeT0iNDQuNDk2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0icmdiKDAsMCwwKSIgZG9taW5hbnQtYmFzZWxpbmU9ImNlbnRyYWwiPis8L3RleHQ+Cjxwb2x5Z29uIHBvaW50cz0iMTIyLjY0LDE3LjI4IDExMS4xMiwyMS42IDExMS4xMiwxMi45NiIgc3R5bGU9ImZpbGw6cmdiKDAsMCwwKSI+PC9wb2x5Z29uPgo8cGF0aCBkPSJNODEuMTIsNDQuNDk2IEwgODguNjIsNDQuNDk2IFEgOTYuMTIsNDQuNDk2IDk2LjEyLDMwLjg4OCBRIDk2LjEyLDE3LjI4IDEwNi41LDE3LjI4IEwgMTE2Ljg4LDE3LjI4IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHBhdGggZD0iTTEzNy43NiwzMi40TDI0NC40OTMsMzIuNEExNS4xMiAxNS4xMiAwIDAgMCAyNTkuNjEzIDE3LjI4QTE1LjEyIDE1LjEyIDAgMCAwIDI0NC40OTMgMi4xNkwxMzcuNzYsMi4xNkExNS4xMiAxNS4xMiAwIDAgMCAxMjIuNjQgMTcuMjhBMTUuMTIgMTUuMTIgMCAwIDAgMTM3Ljc2IDMyLjRaIiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHRleHQgeD0iMTkxLjEyNiIgeT0iMTcuMjgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9InJnYigwLDAsMCkiIGRvbWluYW50LWJhc2VsaW5lPSJjZW50cmFsIj5udW1lcmljLWxpdGVyYWw8L3RleHQ+Cjxwb2x5Z29uIHBvaW50cz0iMjgyLjY1MywxNy4yOCAyNzEuMTMzLDIxLjYgMjcxLjEzMywxMi45NiIgc3R5bGU9ImZpbGw6cmdiKDAsMCwwKSI+PC9wb2x5Z29uPgo8cGF0aCBkPSJNMjU5LjYxMywxNy4yOEwyNzYuODkzLDE3LjI4IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPGNpcmNsZSBjeD0iMjg2LjI1MyIgY3k9IjE3LjI4IiByPSIzLjYiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7Ij48L2NpcmNsZT4KPHBvbHlnb24gcG9pbnRzPSI1MC44OCw4Mi4yOTYgMzkuMzYsODYuNjE2IDM5LjM2LDc3Ljk3NiIgc3R5bGU9ImZpbGw6cmdiKDAsMCwwKSI+PC9wb2x5Z29uPgo8cGF0aCBkPSJNOS4zNiwxNy4yOCBMIDE2Ljg2LDE3LjI4IFEgMjQuMzYsMTcuMjggMjQuMzYsMzIuMjggTCAyNC4zNiw2Ny4yOTYgUSAyNC4zNiw4Mi4yOTYgMzQuNzQsODIuMjk2IEwgNDUuMTIsODIuMjk2IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHBhdGggZD0iTTY2LDk3LjQxNkExNS4xMiAxNS4xMiAwIDAgMCA4MS4xMiA4Mi4yOTZMODEuMTIsODIuMjk2QTE1LjEyIDE1LjEyIDAgMCAwIDY2IDY3LjE3NkExNS4xMiAxNS4xMiAwIDAgMCA1MC44OCA4Mi4yOTZMNTAuODgsODIuMjk2QTE1LjEyIDE1LjEyIDAgMCAwIDY2IDk3LjQxNloiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8dGV4dCB4PSI2NiIgeT0iODIuMjk2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0icmdiKDAsMCwwKSIgZG9taW5hbnQtYmFzZWxpbmU9ImNlbnRyYWwiPi08L3RleHQ+CjxwYXRoIGQ9Ik04MS4xMiw4Mi4yOTYgTCA4OC42Miw4Mi4yOTYgUSA5Ni4xMiw4Mi4yOTYgOTYuMTIsNjcuMjk2IEwgOTYuMTIsNDQuMzc2IEwgOTYuMTIsMjkuMzc2IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHBvbHlnb24gcG9pbnRzPSI2NiwxNy4yOCA1NC40OCwyMS42IDU0LjQ4LDEyLjk2IiBzdHlsZT0iZmlsbDpyZ2IoMCwwLDApIj48L3BvbHlnb24+CjxwYXRoIGQ9Ik05LjM2LDE3LjI4TDYwLjI0LDE3LjI4IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHBhdGggZD0iTTY2LDE3LjI4TDExMS4xMiwxNy4yOCIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+Cjwvc3ZnPg==" class="pikchr" />

A pragma can take either zero or one argument. The argument may be either in parentheses or it may be separated from the pragma name by an equal sign. The two syntaxes yield identical results. In many pragmas, the argument is a boolean. The boolean can be one of:

**1 yes true on\
0 no false off**

Keyword arguments can optionally appear in quotes. (Example: `'yes' [FALSE]`.) Some pragmas take a string literal as their argument. When a pragma takes a keyword argument, it will usually also take a numeric equivalent as well. For example, "0" and "no" mean the same thing, as does "1" and "yes". When querying the value of a setting, many pragmas return the number rather than the keyword.

A pragma may have an optional <span class="yyterm">schema-name</span> before the pragma name. The <span class="yyterm">schema-name</span> is the name of an [ATTACH](lang_attach.md)-ed database or "main" or "temp" for the main and the TEMP databases. If the optional schema name is omitted, "main" is assumed. In some pragmas, the schema name is meaningless and is simply ignored. In the documentation below, pragmas for which the schema name is meaningful are shown with a "*schema.*" prefix.

------------------------------------------------------------------------

<span id="pragfunc"></span>

## PRAGMA functions

PRAGMAs that return results and that have no side-effects can be accessed from ordinary [SELECT](lang_select.md) statements as [table-valued functions](vtab.md#tabfunc2). For each participating PRAGMA, the corresponding table-valued function has the same name as the PRAGMA with a 7-character "pragma\_" prefix. The PRAGMA argument and schema, if any, are passed as arguments to the table-valued function, with the schema as an optional, last argument.

For example, information about the columns in an index can be read using the [index_info pragma](pragma.md#pragma_index_info) as follows:

> \
> PRAGMA index_info('idx52');\

Or, the same content can be read using:

> \
> SELECT \* FROM pragma_index_info('idx52');\

The advantage of the table-valued function format is that the query can return just a subset of the PRAGMA columns, can include a WHERE clause, can use aggregate functions, and the table-valued function can be just one of several data sources in a join. For example, to get a list of all indexed columns in a schema, one could query:

> \
> SELECT DISTINCT m.name \|\| '.' \|\| ii.name AS 'indexed-columns'\
>   FROM sqlite_schema AS m,\
>        pragma_index_list(m.name) AS il,\
>        pragma_index_info(il.name) AS ii\
>  WHERE m.type='table'\
>  ORDER BY 1;\

Additional notes:

- Table-valued functions exist only for built-in PRAGMAs, not for PRAGMAs defined using the [SQLITE_FCNTL_PRAGMA](c3ref/c_fcntl_begin_atomic_write.md#sqlitefcntlpragma) file control.

- Table-valued functions exist only for PRAGMAs that return results and that have no side-effects.

- This feature could be used to implement [information schema](https://en.wikipedia.org/wiki/Information_schema) by first creating a separate schema using

  > \
  > [ATTACH](lang_attach.md) ':memory:' AS 'information_schema';\

  Then creating [VIEWs](lang_createview.md) in that schema that implement the official information schema tables using table-valued PRAGMA functions.

- The table-valued functions for PRAGMA feature was added in SQLite version 3.16.0 (2017-01-02). Prior versions of SQLite cannot use this feature.

------------------------------------------------------------------------

<span id="toc"></span>

## List Of PRAGMAs

- [analysis_limit](pragma.md#pragma_analysis_limit)
- [application_id](pragma.md#pragma_application_id)
- [auto_vacuum](pragma.md#pragma_auto_vacuum)
- [automatic_index](pragma.md#pragma_automatic_index)
- [busy_timeout](pragma.md#pragma_busy_timeout)
- [cache_size](pragma.md#pragma_cache_size)
- [cache_spill](pragma.md#pragma_cache_spill)
- [~~case_sensitive_like¹~~](pragma.md#pragma_case_sensitive_like)
- [cell_size_check](pragma.md#pragma_cell_size_check)
- [checkpoint_fullfsync](pragma.md#pragma_checkpoint_fullfsync)
- [collation_list](pragma.md#pragma_collation_list)
- [compile_options](pragma.md#pragma_compile_options)
- [~~count_changes¹~~](pragma.md#pragma_count_changes)
- [~~data_store_directory¹~~](pragma.md#pragma_data_store_directory)
- [data_version](pragma.md#pragma_data_version)
- [database_list](pragma.md#pragma_database_list)
- [~~default_cache_size¹~~](pragma.md#pragma_default_cache_size)
- [defer_foreign_keys](pragma.md#pragma_defer_foreign_keys)
- [~~empty_result_callbacks¹~~](pragma.md#pragma_empty_result_callbacks)
- [encoding](pragma.md#pragma_encoding)
- [foreign_key_check](pragma.md#pragma_foreign_key_check)
- [foreign_key_list](pragma.md#pragma_foreign_key_list)
- [foreign_keys](pragma.md#pragma_foreign_keys)
- [freelist_count](pragma.md#pragma_freelist_count)
- [~~full_column_names¹~~](pragma.md#pragma_full_column_names)
- [fullfsync](pragma.md#pragma_fullfsync)
- [function_list](pragma.md#pragma_function_list)
- [hard_heap_limit](pragma.md#pragma_hard_heap_limit)
- [ignore_check_constraints](pragma.md#pragma_ignore_check_constraints)
- [incremental_vacuum](pragma.md#pragma_incremental_vacuum)
- [index_info](pragma.md#pragma_index_info)
- [index_list](pragma.md#pragma_index_list)
- [index_xinfo](pragma.md#pragma_index_xinfo)
- [integrity_check](pragma.md#pragma_integrity_check)
- [journal_mode](pragma.md#pragma_journal_mode)
- [journal_size_limit](pragma.md#pragma_journal_size_limit)
- [legacy_alter_table](pragma.md#pragma_legacy_alter_table)
- [legacy_file_format](pragma.md#pragma_legacy_file_format)
- [locking_mode](pragma.md#pragma_locking_mode)
- [max_page_count](pragma.md#pragma_max_page_count)
- [mmap_size](pragma.md#pragma_mmap_size)
- [module_list](pragma.md#pragma_module_list)
- [optimize](pragma.md#pragma_optimize)
- [page_count](pragma.md#pragma_page_count)
- [page_size](pragma.md#pragma_page_size)
- [parser_trace²](pragma.md#pragma_parser_trace)
- [pragma_list](pragma.md#pragma_pragma_list)
- [query_only](pragma.md#pragma_query_only)
- [quick_check](pragma.md#pragma_quick_check)
- [read_uncommitted](pragma.md#pragma_read_uncommitted)
- [recursive_triggers](pragma.md#pragma_recursive_triggers)
- [reverse_unordered_selects](pragma.md#pragma_reverse_unordered_selects)
- [schema_version³](pragma.md#pragma_schema_version)
- [secure_delete](pragma.md#pragma_secure_delete)
- [~~short_column_names¹~~](pragma.md#pragma_short_column_names)
- [shrink_memory](pragma.md#pragma_shrink_memory)
- [soft_heap_limit](pragma.md#pragma_soft_heap_limit)
- [stats³](pragma.md#pragma_stats)
- [synchronous](pragma.md#pragma_synchronous)
- [table_info](pragma.md#pragma_table_info)
- [table_list](pragma.md#pragma_table_list)
- [table_xinfo](pragma.md#pragma_table_xinfo)
- [temp_store](pragma.md#pragma_temp_store)
- [~~temp_store_directory¹~~](pragma.md#pragma_temp_store_directory)
- [threads](pragma.md#pragma_threads)
- [trusted_schema](pragma.md#pragma_trusted_schema)
- [user_version](pragma.md#pragma_user_version)
- [vdbe_addoptrace²](pragma.md#pragma_vdbe_addoptrace)
- [vdbe_debug²](pragma.md#pragma_vdbe_debug)
- [vdbe_listing²](pragma.md#pragma_vdbe_listing)
- [vdbe_trace²](pragma.md#pragma_vdbe_trace)
- [wal_autocheckpoint](pragma.md#pragma_wal_autocheckpoint)
- [wal_checkpoint](pragma.md#pragma_wal_checkpoint)
- [writable_schema³](pragma.md#pragma_writable_schema)

Notes:

1.  Pragmas whose names are ~~struck through~~ are deprecated. Do not use them. They exist for historical compatibility.
2.  These pragmas are only available in builds using non-standard compile-time options.
3.  These pragmas are used for testing SQLite and are not recommended for use in application programs.

<span id="pragma_analysis_limit"></span> PRAGMA analysis_limit

------------------------------------------------------------------------

**PRAGMA analysis_limit;\
PRAGMA analysis_limit =** *N***;**

Query or change a limit on the [approximate ANALYZE](lang_analyze.md#approx) setting. This is the approximate number of rows examined in each index by the [ANALYZE](lang_analyze.md) command. If the argument *N* is omitted, then the analysis limit is unchanged. If the limit is zero, then the analysis limit is disabled and the ANALYZE command will examine all rows of each index. If N is greater than zero, then the analysis limit is set to N and subsequent ANALYZE commands will stop analyzing each index after it has examined approximately N rows. If N is a negative number or something other than an integer value, then the pragma behaves as if the N argument was omitted. In all cases, the value returned is the new analysis limit used for subsequent ANALYZE commands.

This pragma can be used to help the ANALYZE command run faster on large databases. The results of analysis are not as good when only part of each index is examined, but the results are usually good enough. Setting N to 100 or 1000 allows the ANALYZE command to run quickly, even on enormous database files.

This pragma was added in SQLite version 3.32.0 (2020-05-22). The current implementation only uses the lower 31 bits of the N value - higher order bits are silently ignored. Future versions of SQLite might begin using higher order bits.

Beginning with SQLite version 3.46.0 (2024-05-23), the recommended way of running [ANALYZE](lang_analyze.md) is with the [PRAGMA optimize](pragma.md#pragma_optimize) command. The [PRAGMA optimize](pragma.md#pragma_optimize) will automatically set a reasonable, temporary analysis limit that ensures that the [PRAGMA optimize](pragma.md#pragma_optimize) command will finish quickly even on enormous databases. Applications that use the [PRAGMA optimize](pragma.md#pragma_optimize) instead of running [ANALYZE](lang_analyze.md) directly do not need to set an analysis limit. <span id="pragma_application_id"></span> PRAGMA application_id

------------------------------------------------------------------------

**PRAGMA** *schema.***application_id;\
PRAGMA** *schema.***application_id =** *integer* **;**

The application_id PRAGMA is used to query or set the 32-bit signed big-endian "Application ID" integer located at offset 68 into the [database header](fileformat2.md#database_header). Applications that use SQLite as their [application file-format](appfileformat.md) should set the Application ID integer to a unique integer so that utilities such as [file(1)](http://www.darwinsys.com/file/) can determine the specific file type rather than just reporting "SQLite3 Database". A list of assigned application IDs can be seen by consulting the [magic.txt](https://sqlite.org/src/artifact?ci=trunk&filename=magic.txt) file in the SQLite source repository.

See also the [user_version pragma](pragma.md#pragma_user_version). <span id="pragma_auto_vacuum"></span> PRAGMA auto_vacuum

------------------------------------------------------------------------

**PRAGMA** *schema.***auto_vacuum;\
PRAGMA** *schema.***auto_vacuum =** *0 \| NONE \| 1 \| FULL \| 2 \| INCREMENTAL***;**

Query or set the auto-vacuum status in the database.

The default setting for auto-vacuum is 0 or "none", unless the [SQLITE_DEFAULT_AUTOVACUUM](compile.md#default_autovacuum) compile-time option is used. The "none" setting means that auto-vacuum is disabled. When auto-vacuum is disabled and data is deleted from a database, the database file remains the same size. Unused database file pages are added to a "[freelist](fileformat2.md#freelist)" and reused for subsequent inserts. So no database file space is lost. However, the database file does not shrink. In this mode the [VACUUM](lang_vacuum.md) command can be used to rebuild the entire database file and thus reclaim unused disk space.

When the auto-vacuum mode is 1 or "full", the freelist pages are moved to the end of the database file and the database file is truncated to remove the freelist pages at every transaction commit. Note, however, that auto-vacuum only truncates the freelist pages from the file. Auto-vacuum does not defragment the database nor repack individual database pages the way that the [VACUUM](lang_vacuum.md) command does. In fact, because it moves pages around within the file, auto-vacuum can actually make fragmentation worse.

Auto-vacuuming is only possible if the database stores some additional information that allows each database page to be traced backwards to its referrer. Therefore, auto-vacuuming must be turned on before any tables are created. It is not possible to enable or disable auto-vacuum after a table has been created.

When the value of auto-vacuum is 2 or "incremental" then the additional information needed to do auto-vacuuming is stored in the database file but auto-vacuuming does not occur automatically at each commit as it does with auto_vacuum=full. In incremental mode, the separate [incremental_vacuum](pragma.md#pragma_incremental_vacuum) pragma must be invoked to cause the auto-vacuum to occur.

The database connection can be changed between full and incremental autovacuum mode at any time. However, changing from "none" to "full" or "incremental" can only occur when the database is new (no tables have yet been created) or by running the [VACUUM](lang_vacuum.md) command. To change auto-vacuum modes, first use the auto_vacuum pragma to set the new desired mode, then invoke the [VACUUM](lang_vacuum.md) command to reorganize the entire database file. To change from "full" or "incremental" back to "none" always requires running [VACUUM](lang_vacuum.md) even on an empty database.

When the auto_vacuum pragma is invoked with no arguments, it returns the current auto_vacuum mode.

<span id="pragma_automatic_index"></span> PRAGMA automatic_index

------------------------------------------------------------------------

**PRAGMA automatic_index;\
PRAGMA automatic_index =** *boolean***;**

Query, set, or clear the [automatic indexing](optoverview.md#autoindex) capability.

[Automatic indexing](optoverview.md#autoindex) is enabled by default as of [version 3.7.17](releaselog/3_7_17.md) (2013-05-20), but this might change in future releases of SQLite. <span id="pragma_busy_timeout"></span> PRAGMA busy_timeout

------------------------------------------------------------------------

**PRAGMA busy_timeout;\
PRAGMA busy_timeout =** *milliseconds***;**

Query or change the setting of the [busy timeout](c3ref/busy_timeout.md). This pragma is an alternative to the [sqlite3_busy_timeout()](c3ref/busy_timeout.md) C-language interface which is made available as a pragma for use with language bindings that do not provide direct access to [sqlite3_busy_timeout()](c3ref/busy_timeout.md).

Each database connection can only have a single [busy handler](c3ref/busy_handler.md). This PRAGMA sets the busy handler for the process, possibly overwriting any previously set busy handler. <span id="pragma_cache_size"></span> PRAGMA cache_size

------------------------------------------------------------------------

**PRAGMA** *schema.***cache_size;\
PRAGMA** *schema.***cache_size =** *pages***;\
PRAGMA** *schema.***cache_size = -***kibibytes***;**

Query or change the suggested maximum number of database disk pages that SQLite will hold in memory at once per open database file. Whether or not this suggestion is honored is at the discretion of the [Application Defined Page Cache](c3ref/pcache_methods2.md). The default page cache that is built into SQLite honors the request, however alternative application-defined page cache implementations may choose to interpret the suggested cache size in different ways or to ignore it altogether. The default suggested cache size is -2000, which means the cache size is limited to 2048000 bytes of memory. The default suggested cache size can be altered using the [SQLITE_DEFAULT_CACHE_SIZE](compile.md#default_cache_size) compile-time options. The TEMP database has a default suggested cache size of 0 pages.

If the argument N is positive then the suggested cache size is set to N. If the argument N is negative, then the number of cache pages is adjusted to be a number of pages that would use approximately abs(N\*1024) bytes of memory based on the current page size. SQLite remembers the number of pages in the page cache, not the amount of memory used. So if you set the cache size using a negative number and subsequently change the page size (using the [PRAGMA page_size](pragma.md#pragma_page_size) command) then the maximum amount of cache memory will go up or down in proportion to the change in page size.

*Backwards compatibility note:* The behavior of cache_size with a negative N was different prior to [version 3.7.10](releaselog/3_7_10.md) (2012-01-16). In earlier versions, the number of pages in the cache was set to the absolute value of N.

When you change the cache size using the cache_size pragma, the change only endures for the current session. The cache size reverts to the default value when the database is closed and reopened.

The default page cache implemention does not allocate the full amount of cache memory all at once. Cache memory is allocated in smaller chunks on an as-needed basis. The page_cache setting is a (suggested) upper bound on the amount of memory that the cache can use, not the amount of memory it will use all of the time. This is the behavior of the default page cache implementation, but an [application defined page cache](c3ref/pcache_methods2.md) is free to behave differently if it wants. <span id="pragma_cache_spill"></span> PRAGMA cache_spill

------------------------------------------------------------------------

**PRAGMA cache_spill;\
PRAGMA cache_spill=***boolean***;\
PRAGMA** *schema.***cache_spill=*N*;**

The cache_spill pragma enables or disables the ability of the pager to spill dirty cache pages to the database file in the middle of a transaction. Cache_spill is enabled by default and most applications should leave it that way as cache spilling is usually advantageous. However, a cache spill has the side-effect of acquiring an [EXCLUSIVE lock](lockingv3.md#excl_lock) on the database file. Hence, some applications that have large long-running transactions may want to disable cache spilling in order to prevent the application from acquiring an exclusive lock on the database until the moment that the transaction [COMMIT](lang_transaction.md)s.

The "PRAGMA cache_spill=*N*" form of this pragma sets a minimum cache size threshold required for spilling to occur. The number of pages in cache must exceed both the cache_spill threshold and the maximum cache size set by the [PRAGMA cache_size](pragma.md#pragma_cache_size) statement in order for spilling to occur.

The "PRAGMA cache_spill=*boolean*" form of this pragma applies across all databases attached to the database connection. But the "PRAGMA cache_spill=*N*" form of this statement only applies to the "main" schema or whatever other schema is specified as part of the statement. <span id="pragma_case_sensitive_like"></span> PRAGMA case_sensitive_like

------------------------------------------------------------------------

**PRAGMA case_sensitive_like =** *boolean***;**

The default behavior of the [LIKE](lang_expr.md#like) operator is to ignore case for ASCII characters. Hence, by default **'a' LIKE 'A'** is true. The case_sensitive_like pragma installs a new application-defined LIKE function that is either case sensitive or insensitive depending on the value of the case_sensitive_like pragma. When case_sensitive_like is disabled, the default LIKE behavior is expressed. When case_sensitive_like is enabled, case becomes significant. So, for example, **'a' LIKE 'A'** is false but **'a' LIKE 'a'** is still true.

This pragma uses [sqlite3_create_function()](c3ref/create_function.md) to overload the LIKE and GLOB functions, which may override previous implementations of LIKE and GLOB registered by the application. This pragma only changes the behavior of the SQL [LIKE](lang_expr.md#like) operator. It does not change the behavior of the [sqlite3_strlike()](c3ref/strlike.md) C-language interface, which is always case insensitive.

**WARNING:** If a database uses the LIKE operator anywhere in the schema, such as in a [CHECK constraint](lang_createtable.md#ckconst) or in an [expression index](expridx.md) or in the WHERE clause of a [partial index](partialindex.md), then changing the definition of the LIKE operator using this PRAGMA can cause the database to appear to be corrupt. [PRAGMA integrity_check](pragma.md#pragma_integrity_check) will report errors. The database is not really corrupt in that changing the behavior of LIKE back to the way it was when the schema was defined and the database was populated will clear the problem. If the use of LIKE occurs only in indexes, then the problem can be cleared by running [REINDEX](lang_reindex.md). Nevertheless, the use of the case_sensitive_like pragma is discouraged.

**This pragma is deprecated** and exists for backwards compatibility only. New applications should avoid using this pragma. Older applications should discontinue use of this pragma at the earliest opportunity. This pragma may be omitted from the build when SQLite is compiled using [SQLITE_OMIT_DEPRECATED](compile.md#omit_deprecated).

<span id="pragma_cell_size_check"></span> PRAGMA cell_size_check

------------------------------------------------------------------------

**PRAGMA cell_size_check\
PRAGMA cell_size_check =** *boolean***;**

The cell_size_check pragma enables or disables additional sanity checking on database b-tree pages as they are initially read from disk. With cell size checking enabled, database corruption is detected earlier and is less likely to "spread". However, there is a small performance hit for doing the extra checks and so cell size checking is turned off by default. <span id="pragma_checkpoint_fullfsync"></span> PRAGMA checkpoint_fullfsync

------------------------------------------------------------------------

**PRAGMA checkpoint_fullfsync\
PRAGMA checkpoint_fullfsync =** *boolean***;**

Query or change the fullfsync flag for [checkpoint](wal.md#ckpt) operations. If this flag is set, then the F_FULLFSYNC syncing method is used during checkpoint operations on systems that support F_FULLFSYNC. The default value of the checkpoint_fullfsync flag is off. Only Mac OS-X supports F_FULLFSYNC.

If the [fullfsync](pragma.md#pragma_fullfsync) flag is set, then the F_FULLFSYNC syncing method is used for all sync operations and the checkpoint_fullfsync setting is irrelevant.

<span id="pragma_collation_list"></span> PRAGMA collation_list

------------------------------------------------------------------------

**PRAGMA collation_list;**

Return a list of the collating sequences defined for the current database connection.

<span id="pragma_compile_options"></span> PRAGMA compile_options

------------------------------------------------------------------------

**PRAGMA compile_options;**

This pragma returns the names of [compile-time options](compile.md) used when building SQLite, one option per row. The "SQLITE\_" prefix is omitted from the returned option names. See also the [sqlite3_compileoption_get()](c3ref/compileoption_get.md) C/C++ interface and the [sqlite_compileoption_get()](lang_corefunc.md#sqlite_compileoption_get) SQL functions.

<span id="pragma_count_changes"></span> PRAGMA count_changes

------------------------------------------------------------------------

**PRAGMA count_changes;\
PRAGMA count_changes =** boolean**;**

Query or change the count-changes flag. Normally, when the count-changes flag is not set, [INSERT](lang_insert.md), [UPDATE](lang_update.md) and [DELETE](lang_delete.md) statements return no data. When count-changes is set, each of these commands returns a single row of data consisting of one integer value - the number of rows inserted, modified or deleted by the command. The returned change count does not include any insertions, modifications or deletions performed by triggers, any changes made automatically by [foreign key actions](foreignkeys.md#fk_actions), or updates caused by an [upsert](lang_upsert.md).

Another way to get the row change counts is to use the [sqlite3_changes()](c3ref/changes.md) or [sqlite3_total_changes()](c3ref/total_changes.md) interfaces. There is a subtle difference, though. When an INSERT, UPDATE, or DELETE is run against a view using an [INSTEAD OF trigger](lang_createtrigger.md#instead_of_trigger), the count_changes pragma reports the number of rows in the view that fired the trigger, whereas [sqlite3_changes()](c3ref/changes.md) and [sqlite3_total_changes()](c3ref/total_changes.md) do not.

**This pragma is deprecated** and exists for backwards compatibility only. New applications should avoid using this pragma. Older applications should discontinue use of this pragma at the earliest opportunity. This pragma may be omitted from the build when SQLite is compiled using [SQLITE_OMIT_DEPRECATED](compile.md#omit_deprecated).

<span id="pragma_data_store_directory"></span> PRAGMA data_store_directory

------------------------------------------------------------------------

**PRAGMA data_store_directory;\
PRAGMA data_store_directory = '***directory-name***';**

Query or change the value of the [sqlite3_data_directory](c3ref/data_directory.md) global variable, which windows operating-system interface backends use to determine where to store database files specified using a relative pathname.

Changing the data_store_directory setting is <u>not</u> threadsafe. Never change the data_store_directory setting if another thread within the application is running any SQLite interface at the same time. Doing so results in undefined behavior. Changing the data_store_directory setting writes to the [sqlite3_data_directory](c3ref/data_directory.md) global variable and that global variable is not protected by a mutex.

This facility is provided for WinRT which does not have an OS mechanism for reading or changing the current working directory. The use of this pragma in any other context is discouraged and may be disallowed in future releases.

**This pragma is deprecated** and exists for backwards compatibility only. New applications should avoid using this pragma. Older applications should discontinue use of this pragma at the earliest opportunity. This pragma may be omitted from the build when SQLite is compiled using [SQLITE_OMIT_DEPRECATED](compile.md#omit_deprecated).

<span id="pragma_data_version"></span> PRAGMA data_version

------------------------------------------------------------------------

**PRAGMA** *schema.***data_version;**

The "PRAGMA data_version" command provides an indication that the database file has been modified. Interactive programs that hold database content in memory or that display database content on-screen can use the PRAGMA data_version command to determine if they need to flush and reload their memory or update the screen display.

The integer values returned by two invocations of "PRAGMA data_version" from the same connection will be different if changes were committed to the database by any other connection in the interim. The "PRAGMA data_version" value is unchanged for commits made on the same database connection. The behavior of "PRAGMA data_version" is the same for all database connections, including database connections in separate processes and [shared cache](sharedcache.md) database connections.

The "PRAGMA data_version" value is a local property of each database connection and so values returned by two concurrent invocations of "PRAGMA data_version" on separate database connections are often different even though the underlying database is identical. It is only meaningful to compare the "PRAGMA data_version" values returned by the same database connection at two different points in time. <span id="pragma_database_list"></span> PRAGMA database_list

------------------------------------------------------------------------

**PRAGMA database_list;**

This pragma works like a query to return one row for each database attached to the current database connection. The second column is "main" for the main database file, "temp" for the database file used to store TEMP objects, or the name of the ATTACHed database for other database files. The third column is the name of the database file itself, or an empty string if the database is not associated with a file.

<span id="pragma_default_cache_size"></span> PRAGMA default_cache_size

------------------------------------------------------------------------

**PRAGMA** *schema.***default_cache_size;\
PRAGMA** *schema.***default_cache_size =** *Number-of-pages***;**

This pragma queries or sets the suggested maximum number of pages of disk cache that will be allocated per open database file. The difference between this pragma and [cache_size](pragma.md#pragma_cache_size) is that the value set here persists across database connections. The value of the default cache size is stored in the 4-byte big-endian integer located at offset 48 in the header of the database file.

**This pragma is deprecated** and exists for backwards compatibility only. New applications should avoid using this pragma. Older applications should discontinue use of this pragma at the earliest opportunity. This pragma may be omitted from the build when SQLite is compiled using [SQLITE_OMIT_DEPRECATED](compile.md#omit_deprecated).

<span id="pragma_defer_foreign_keys"></span> PRAGMA defer_foreign_keys

------------------------------------------------------------------------

**PRAGMA defer_foreign_keys\
PRAGMA defer_foreign_keys =** *boolean***;**

When the defer_foreign_keys [PRAGMA](pragma.md#syntax) is on, enforcement of all [foreign key constraints](foreignkeys.md) is delayed until the outermost transaction is committed. The defer_foreign_keys pragma defaults to OFF so that foreign key constraints are only deferred if they are created as "DEFERRABLE INITIALLY DEFERRED". The defer_foreign_keys pragma is automatically switched off at each COMMIT or ROLLBACK. Hence, the defer_foreign_keys pragma must be separately enabled for each transaction. This pragma is only meaningful if foreign key constraints are enabled, of course.

The [sqlite3_db_status](c3ref/db_status.md)(db,[SQLITE_DBSTATUS_DEFERRED_FKS](c3ref/c_dbstatus_options.md#sqlitedbstatusdeferredfks),...) C-language interface can be used during a transaction to determine if there are deferred and unresolved foreign key constraints.

Caution: Setting "defer_foreign_keys=0" resets the internal foreign-key tracking state of the database connection, so that it becomes possible to commit the current transaction even if there are foreign key violations.

<span id="pragma_empty_result_callbacks"></span> PRAGMA empty_result_callbacks

------------------------------------------------------------------------

**PRAGMA empty_result_callbacks;\
PRAGMA empty_result_callbacks =** *boolean***;**

Query or change the empty-result-callbacks flag.

The empty-result-callbacks flag affects the [sqlite3_exec()](c3ref/exec.md) API only. Normally, when the empty-result-callbacks flag is cleared, the callback function supplied to the [sqlite3_exec()](c3ref/exec.md) is not invoked for commands that return zero rows of data. When empty-result-callbacks is set in this situation, the callback function is invoked exactly once, with the third parameter set to 0 (NULL). This is to enable programs that use the [sqlite3_exec()](c3ref/exec.md) API to retrieve column-names even when a query returns no data.

**This pragma is deprecated** and exists for backwards compatibility only. New applications should avoid using this pragma. Older applications should discontinue use of this pragma at the earliest opportunity. This pragma may be omitted from the build when SQLite is compiled using [SQLITE_OMIT_DEPRECATED](compile.md#omit_deprecated).

<span id="pragma_encoding"></span> PRAGMA encoding

------------------------------------------------------------------------

**PRAGMA encoding;\
PRAGMA encoding = 'UTF-8';\
PRAGMA encoding = 'UTF-16';\
PRAGMA encoding = 'UTF-16le';\
PRAGMA encoding = 'UTF-16be';**

In first form, if the main database has already been created, then this pragma returns the text encoding used by the main database, one of 'UTF-8', 'UTF-16le' (little-endian UTF-16 encoding) or 'UTF-16be' (big-endian UTF-16 encoding). If the main database has not already been created, then the value returned is the text encoding that will be used to create the main database, if it is created by this session.

The second through fifth forms of this pragma set the encoding that the main database will be created with if it is created by this session. The string 'UTF-16' is interpreted as "UTF-16 encoding using native machine byte-ordering". It is not possible to change the text encoding of a database after it has been created and any attempt to do so will be silently ignored.

If no encoding is first set with this pragma, then the encoding with which the main database will be created defaults to one determined by the [API used to open the connection](c3ref/open.md).

Once an encoding has been set for a database, it cannot be changed.

Databases created by the [ATTACH](lang_attach.md) command always use the same encoding as the main database. An attempt to [ATTACH](lang_attach.md) a database with a different text encoding from the "main" database will fail.

<span id="pragma_foreign_key_check"></span> PRAGMA foreign_key_check

------------------------------------------------------------------------

**PRAGMA** *schema.***foreign_key_check;\
PRAGMA** *schema.***foreign_key_check(***table-name***);**

The foreign_key_check pragma checks the database, or the table called "*table-name*", for [foreign key constraints](foreignkeys.md) that are violated. The foreign_key_check pragma returns one row output for each foreign key violation. There are four columns in each result row. The first column is the name of the table that contains the REFERENCES clause. The second column is the [rowid](lang_createtable.md#rowid) of the row that contains the invalid REFERENCES clause, or NULL if the child table is a [WITHOUT ROWID](withoutrowid.md) table. The third column is the name of the table that is referred to. The fourth column is the index of the specific foreign key constraint that failed. The fourth column in the output of the foreign_key_check pragma is the same integer as the first column in the output of the [foreign_key_list pragma](pragma.md#pragma_foreign_key_list). When a "*table-name*" is specified, the only foreign key constraints checked are those created by REFERENCES clauses in the CREATE TABLE statement for *table-name*.

<span id="pragma_foreign_key_list"></span> PRAGMA foreign_key_list

------------------------------------------------------------------------

**PRAGMA foreign_key_list(***table-name***);**

This pragma returns one row for each [foreign key constraint](foreignkeys.md) created by a REFERENCES clause in the CREATE TABLE statement of table "*table-name*". <span id="pragma_foreign_keys"></span> PRAGMA foreign_keys

------------------------------------------------------------------------

**PRAGMA foreign_keys;\
PRAGMA foreign_keys =** *boolean***;**

Query, set, or clear the enforcement of [foreign key constraints](foreignkeys.md).

This pragma is a no-op within a transaction; foreign key constraint enforcement may only be enabled or disabled when there is no pending [BEGIN](lang_transaction.md) or [SAVEPOINT](lang_savepoint.md).

Changing the foreign_keys setting affects the execution of all statements prepared using the database connection, including those prepared before the setting was changed. Any existing statements prepared using the legacy [sqlite3_prepare()](c3ref/prepare.md) interface may fail with an [SQLITE_SCHEMA](rescode.md#schema) error after the foreign_keys setting is changed.

As of SQLite [version 3.6.19](releaselog/3_6_19.md), the default setting for foreign key enforcement is OFF. However, that might change in a future release of SQLite. The default setting for foreign key enforcement can be specified at compile-time using the [SQLITE_DEFAULT_FOREIGN_KEYS](compile.md#default_foreign_keys) preprocessor macro. To minimize future problems, applications should set the foreign key enforcement flag as required by the application and not depend on the default setting. <span id="pragma_freelist_count"></span> PRAGMA freelist_count

------------------------------------------------------------------------

**PRAGMA** *schema.***freelist_count;**

Return the number of unused pages in the database file.

<span id="pragma_full_column_names"></span> PRAGMA full_column_names

------------------------------------------------------------------------

**PRAGMA full_column_names;\
PRAGMA full_column_names =** *boolean***;**

Query or change the full_column_names flag. This flag together with the [short_column_names](pragma.md#pragma_short_column_names) flag determine the way SQLite assigns names to result columns of [SELECT](lang_select.md) statements. Result columns are named by applying the following rules in order:

1.  If there is an AS clause on the result, then the name of the column is the right-hand side of the AS clause.

2.  If the result is a general expression, not just the name of a source table column, then the name of the result is a copy of the expression text.

3.  If the [short_column_names](pragma.md#pragma_short_column_names) pragma is ON, then the name of the result is the name of the source table column without the source table name prefix: COLUMN.

4.  If both pragmas [short_column_names](pragma.md#pragma_short_column_names) and [full_column_names](pragma.md#pragma_full_column_names) are OFF then case (2) applies.

5.  The name of the result column is a combination of the source table and source column name: TABLE.COLUMN

**This pragma is deprecated** and exists for backwards compatibility only. New applications should avoid using this pragma. Older applications should discontinue use of this pragma at the earliest opportunity. This pragma may be omitted from the build when SQLite is compiled using [SQLITE_OMIT_DEPRECATED](compile.md#omit_deprecated).

<span id="pragma_fullfsync"></span> PRAGMA fullfsync

------------------------------------------------------------------------

**PRAGMA fullfsync\
PRAGMA fullfsync =** *boolean***;**

Query or change the fullfsync flag. This flag determines whether or not the F_FULLFSYNC syncing method is used on systems that support it. The default value of the fullfsync flag is off. Only Mac OS X supports F_FULLFSYNC.

See also [checkpoint_fullfsync](pragma.md#pragma_checkpoint_fullfsync).

<span id="pragma_function_list"></span> PRAGMA function_list

------------------------------------------------------------------------

**PRAGMA function_list;**

This pragma returns a list of SQL functions known to the database connection. Each row of the result describes a single calling signature for a single SQL function. Some SQL functions will have multiple rows in the result set if they can (for example) be invoked with a varying number of arguments or can accept text in various encodings. <span id="pragma_hard_heap_limit"></span> PRAGMA hard_heap_limit

------------------------------------------------------------------------

**PRAGMA hard_heap_limit\
PRAGMA hard_heap_limit=***N*

This pragma invokes the [sqlite3_hard_heap_limit64()](c3ref/hard_heap_limit64.md) interface with the argument N, if N is specified and N is a positive integer that is less than the current hard heap limit. The hard_heap_limit pragma always returns the same integer that would be returned by the [sqlite3_hard_heap_limit64](c3ref/hard_heap_limit64.md)(-1) C-language function. That is to say, it always returns the value of the hard heap limit that is set after any changes imposed by this PRAGMA.

This pragma can only lower the heap limit, never raise it. The C-language interface [sqlite3_hard_heap_limit64()](c3ref/hard_heap_limit64.md) must be used to raise the heap limit.

See also the [soft_heap_limit pragma](pragma.md#pragma_soft_heap_limit). <span id="pragma_ignore_check_constraints"></span> PRAGMA ignore_check_constraints

------------------------------------------------------------------------

**PRAGMA ignore_check_constraints =** *boolean***;**

This pragma enables or disables the enforcement of CHECK constraints. The default setting is off, meaning that CHECK constraints are enforced by default.

<span id="pragma_incremental_vacuum"></span> PRAGMA incremental_vacuum

------------------------------------------------------------------------

**PRAGMA** *schema.***incremental_vacuum***(N)***;\
PRAGMA** *schema.***incremental_vacuum;**

The incremental_vacuum pragma causes up to *N* pages to be removed from the [freelist](fileformat2.md#freelist). The database file is truncated by the same amount. The incremental_vacuum pragma has no effect if the database is not in [auto_vacuum=incremental](#pragma_auto_vacuum) mode or if there are no pages on the freelist. If there are fewer than *N* pages on the freelist, or if *N* is less than 1, or if the "(*N*)" argument is omitted, then the entire freelist is cleared.

<span id="pragma_index_info"></span> PRAGMA index_info

------------------------------------------------------------------------

**PRAGMA** *schema.***index_info(***index-name***);**

This pragma returns one row for each key column in the named index. A key column is a column that is actually named in the [CREATE INDEX](lang_createindex.md) index statement or [UNIQUE constraint](lang_createtable.md#uniqueconst) or [PRIMARY KEY constraint](lang_createtable.md#primkeyconst) that created the index. Index entries also usually contain auxiliary columns that point back to the table row being indexed. The auxiliary index-columns are not shown by the index_info pragma, but they are listed by the [index_xinfo pragma](pragma.md#pragma_index_xinfo).

Output columns from the index_info pragma are as follows:

1.  The rank of the column within the index. (0 means left-most.)
2.  The rank of the column within the table being indexed. A value of -1 means [rowid](lang_createtable.md#rowid) and a value of -2 means that an [expression](expridx.md) is being used.
3.  The name of the column being indexed. This columns is NULL if the column is the [rowid](lang_createtable.md#rowid) or an [expression](expridx.md).

If there is no index named *index-name* but there is a [WITHOUT ROWID](withoutrowid.md) table with that name, then (as of SQLite [version 3.30.0](releaselog/3_30_0.md) on 2019-10-04) this pragma returns the PRIMARY KEY columns of the WITHOUT ROWID table as they are used in the records of the underlying b-tree, which is to say with duplicate columns removed. <span id="pragma_index_list"></span> PRAGMA index_list

------------------------------------------------------------------------

**PRAGMA** *schema.***index_list(***table-name***);**

This pragma returns one row for each index associated with the given table.

Output columns from the index_list pragma are as follows:

1.  A sequence number assigned to each index for internal tracking purposes.
2.  The name of the index.
3.  "1" if the index is UNIQUE and "0" if not.
4.  "c" if the index was created by a [CREATE INDEX](lang_createindex.md) statement, "u" if the index was created by a [UNIQUE constraint](lang_createtable.md#uniqueconst), or "pk" if the index was created by a [PRIMARY KEY constraint](lang_createtable.md#primkeyconst).
5.  "1" if the index is a [partial index](partialindex.md) and "0" if not.

<span id="pragma_index_xinfo"></span> PRAGMA index_xinfo

------------------------------------------------------------------------

**PRAGMA** *schema.***index_xinfo(***index-name***);**

This pragma returns information about every column in an index. Unlike this [index_info pragma](pragma.md#pragma_index_info), this pragma returns information about every column in the index, not just the key columns. (A key column is a column that is actually named in the [CREATE INDEX](lang_createindex.md) index statement or [UNIQUE constraint](lang_createtable.md#uniqueconst) or [PRIMARY KEY constraint](lang_createtable.md#primkeyconst) that created the index. Auxiliary columns are additional columns needed to locate the table entry that corresponds to each index entry.)

Output columns from the index_xinfo pragma are as follows:

1.  The rank of the column within the index. (0 means left-most. Key columns come before auxiliary columns.)
2.  The rank of the column within the table being indexed, or -1 if the index-column is the [rowid](lang_createtable.md#rowid) of the table being indexed and -2 if the [index is on an expression](expridx.md).
3.  The name of the column being indexed, or NULL if the index-column is the [rowid](lang_createtable.md#rowid) of the table being indexed or an [expression](expridx.md).
4.  1 if the index-column is sorted in reverse (DESC) order by the index and 0 otherwise.
5.  The name for the [collating sequence](datatype3.md#collation) used to compare values in the index-column.
6.  1 if the index-column is a key column and 0 if the index-column is an auxiliary column.

If there is no index named *index-name* but there is a [WITHOUT ROWID](withoutrowid.md) table with that name, then (as of SQLite [version 3.30.0](releaselog/3_30_0.md) on 2019-10-04) this pragma returns the columns of the WITHOUT ROWID table as they are used in the records of the underlying b-tree, which is to say with de-duplicated PRIMARY KEY columns first followed by data columns. <span id="pragma_integrity_check"></span> PRAGMA integrity_check

------------------------------------------------------------------------

**PRAGMA** *schema.***integrity_check;\
PRAGMA** *schema.***integrity_check(***N***)\
PRAGMA** *schema.***integrity_check(***TABLENAME***)**

This pragma does a low-level formatting and consistency check of the database. The integrity_check pragma look for:

- Table or index entries that are out of sequence
- Misformatted records
- Missing pages
- Missing or surplus index entries
- UNIQUE, CHECK, and NOT NULL constraint errors
- Integrity of the freelist
- Sections of the database that are used more than once, or not at all

If the integrity_check pragma finds problems, strings are returned (as multiple rows with a single column per row) which describe the problems. Pragma integrity_check will return at most *N* errors before the analysis quits, with N defaulting to 100. If pragma integrity_check finds no errors, a single row with the value 'ok' is returned.

The usual case is that the entire database file is checked. However, if the argument is *TABLENAME*, then checking is only performed for the the table named and its associated indexes. This is called a "partial integrity check". Because only a subset of the database is checked, errors such as unused sections of the file or duplication use of the same section of the file by two or more tables cannot be detected. The freelist is only verified on a partial integrity check if *TABLENAME* is [sqlite_schema](schematab.md) or one of its aliases. Support for partial integrity checks was added with version 3.33.0 (2020-08-14).

PRAGMA integrity_check does not find [FOREIGN KEY](foreignkeys.md) errors. Use the [PRAGMA foreign_key_check](pragma.md#pragma_foreign_key_check) command to find errors in FOREIGN KEY constraints.

See also the [PRAGMA quick_check](pragma.md#pragma_quick_check) command which does most of the checking of PRAGMA integrity_check but runs much faster.

<span id="pragma_journal_mode"></span> PRAGMA journal_mode

------------------------------------------------------------------------

**PRAGMA** *schema.***journal_mode;\
PRAGMA** *schema.***journal_mode = *DELETE \| TRUNCATE \| PERSIST \| MEMORY \| WAL \| OFF***

This pragma queries or sets the journal mode for databases associated with the current [database connection](c3ref/sqlite3.md).

The first form of this pragma queries the current journaling mode for *database*. When *database* is omitted, the "main" database is queried.

The second form changes the journaling mode for "*database*" or for all attached databases if "*database*" is omitted. The new journal mode is returned. If the journal mode could not be changed, the original journal mode is returned.

The DELETE journaling mode is the default. In the DELETE mode, the rollback journal is deleted at the conclusion of each transaction. Indeed, the delete operation is the action that causes the transaction to commit. (See the document titled [Atomic Commit In SQLite](atomiccommit.md) for additional detail.)

The TRUNCATE journaling mode commits transactions by truncating the rollback journal to zero-length instead of deleting it. On many systems, truncating a file is much faster than deleting the file since the containing directory does not need to be changed.

The PERSIST journaling mode prevents the rollback journal from being deleted at the end of each transaction. Instead, the header of the journal is overwritten with zeros. This will prevent other database connections from rolling the journal back. The PERSIST journaling mode is useful as an optimization on platforms where deleting or truncating a file is much more expensive than overwriting the first block of a file with zeros. See also: [PRAGMA journal_size_limit](pragma.md#pragma_journal_size_limit) and [SQLITE_DEFAULT_JOURNAL_SIZE_LIMIT](compile.md#default_journal_size_limit).

The MEMORY journaling mode stores the rollback journal in volatile RAM. This saves disk I/O but at the expense of database safety and integrity. If the application using SQLite crashes in the middle of a transaction when the MEMORY journaling mode is set, then the database file will very likely [go corrupt](howtocorrupt.md#cfgerr).

The WAL journaling mode uses a [write-ahead log](wal.md) instead of a rollback journal to implement transactions. The WAL journaling mode is persistent; after being set it stays in effect across multiple database connections and after closing and reopening the database. A database in WAL journaling mode can only be accessed by SQLite [version 3.7.0](releaselog/3_7_0.md) (2010-07-21) or later.

The OFF journaling mode disables the rollback journal completely. No rollback journal is ever created and hence there is never a rollback journal to delete. The OFF journaling mode disables the atomic commit and rollback capabilities of SQLite. The [ROLLBACK](lang_transaction.md) command no longer works; it behaves in an undefined way. Applications must avoid using the [ROLLBACK](lang_transaction.md) command when the journal mode is OFF. If the application crashes in the middle of a transaction when the OFF journaling mode is set, then the database file will very likely [go corrupt](howtocorrupt.md#cfgerr). Without a journal, there is no way for a statement to unwind partially completed operations following a constraint error. This might also leave the database in a corrupted state. For example, if a duplicate entry causes a [CREATE UNIQUE INDEX](lang_createindex.md) statement to fail half-way through, it will leave behind a partially created, and hence corrupt, index. Because OFF journaling mode allows the database file to be corrupted using ordinary SQL, it is disabled when [SQLITE_DBCONFIG_DEFENSIVE](c3ref/c_dbconfig_defensive.md#sqlitedbconfigdefensive) is enabled.

Note that the journal_mode for an [in-memory database](inmemorydb.md) is either MEMORY or OFF and can not be changed to a different value. An attempt to change the journal_mode of an [in-memory database](inmemorydb.md) to any setting other than MEMORY or OFF is ignored. Note also that the journal_mode cannot be changed while a transaction is active.

<span id="pragma_journal_size_limit"></span> PRAGMA journal_size_limit

------------------------------------------------------------------------

**PRAGMA** *schema.***journal_size_limit\
PRAGMA** *schema.***journal_size_limit =** *N* **;**

If a database connection is operating in [exclusive locking mode](pragma.md#pragma_locking_mode) or in [persistent journal mode](pragma.md#pragma_journal_mode) (PRAGMA journal_mode=persist) then after committing a transaction the [rollback journal](lockingv3.md#rollback) file may remain in the file-system. This increases performance for subsequent transactions since overwriting an existing file is faster than append to a file, but it also consumes file-system space. After a large transaction (e.g. a [VACUUM](lang_vacuum.md)), the rollback journal file may consume a very large amount of space.

Similarly, in [WAL mode](wal.md), the write-ahead log file is not truncated following a [checkpoint](wal.md#ckpt). Instead, SQLite reuses the existing file for subsequent WAL entries since overwriting is faster than appending.

The journal_size_limit pragma may be used to limit the size of rollback-journal and WAL files left in the file-system after transactions or checkpoints. Each time a transaction is committed or a WAL file resets, SQLite compares the size of the rollback journal file or WAL file left in the file-system to the size limit set by this pragma and if the journal or WAL file is larger it is truncated to the limit.

The second form of the pragma listed above is used to set a new limit in bytes for the specified database. A negative number implies no limit. To always truncate rollback journals and WAL files to their minimum size, set the journal_size_limit to zero. Both the first and second forms of the pragma listed above return a single result row containing a single integer column - the value of the journal size limit in bytes. The default journal size limit is -1 (no limit). The [SQLITE_DEFAULT_JOURNAL_SIZE_LIMIT](compile.md#default_journal_size_limit) preprocessor macro can be used to change the default journal size limit at compile-time.

This pragma only operates on the single database specified prior to the pragma name (or on the "main" database if no database is specified.) There is no way to change the journal size limit on all attached databases using a single PRAGMA statement. The size limit must be set separately for each attached database. <span id="pragma_legacy_alter_table"></span> PRAGMA legacy_alter_table

------------------------------------------------------------------------

**PRAGMA legacy_alter_table;\
PRAGMA legacy_alter_table = *boolean***

This pragma sets or queries the value of the legacy_alter_table flag. When this flag is on, the [ALTER TABLE RENAME](lang_altertable.md#altertabrename) command (for changing the name of a table) works as it did in SQLite 3.24.0 (2018-06-04) and earlier. More specifically, when this flag is on the [ALTER TABLE RENAME](lang_altertable.md#altertabrename) command only rewrites the initial occurrence of the table name in its [CREATE TABLE](lang_createtable.md) statement and in any associated [CREATE INDEX](lang_createindex.md) and [CREATE TRIGGER](lang_createtrigger.md) statements. Other references to the table are unmodified, including:

- References to the table within the bodies of triggers and views.
- References to the table within CHECK constraints in the original CREATE TABLE statement.
- References to the table within the WHERE clauses of [partial indexes](partialindex.md).

The default setting for this pragma is OFF, which means that all references to the table anywhere in the schema are converted to the new name.

This pragma is provided as a work-around for older programs that contain code that expect the incomplete behavior of [ALTER TABLE RENAME](lang_altertable.md#altertabrename) found in older versions of SQLite. New applications should leave this flag turned off.

For compatibility with older [virtual table](vtab.md) implementations, this flag is turned on temporarily while the [sqlite3_module.xRename](vtab.md#xrename) method is being run. The value of this flag is restored after the [sqlite3_module.xRename](vtab.md#xrename) method finishes.

The legacy alter table behavior can also be toggled on and off using the [SQLITE_DBCONFIG_LEGACY_ALTER_TABLE](c3ref/c_dbconfig_defensive.md#sqlitedbconfiglegacyaltertable) option to the [sqlite3_db_config()](c3ref/db_config.md) interface.

The legacy alter table behavior is a per-connection setting. Turning this features on or off affects all attached database files within the [database connection](c3ref/sqlite3.md). The setting does not persist. Changing this setting in one connection does not affect any other connections. <span id="pragma_legacy_file_format"></span> PRAGMA legacy_file_format

------------------------------------------------------------------------

**PRAGMA legacy_file_format;**

This pragma no longer functions. It has become a no-op. The capabilities formerly provided by PRAGMA legacy_file_format are now available using the [SQLITE_DBCONFIG_LEGACY_FILE_FORMAT](c3ref/c_dbconfig_defensive.md#sqlitedbconfiglegacyfileformat) option to the [sqlite3_db_config()](c3ref/db_config.md) C-language interface.

<span id="pragma_locking_mode"></span> PRAGMA locking_mode

------------------------------------------------------------------------

**PRAGMA** *schema.***locking_mode;\
PRAGMA** *schema.***locking_mode = *NORMAL \| EXCLUSIVE***

This pragma sets or queries the database connection locking-mode. The locking-mode is either NORMAL or EXCLUSIVE.

In NORMAL locking-mode (the default unless overridden at compile-time using [SQLITE_DEFAULT_LOCKING_MODE](compile.md#default_locking_mode)), a database connection unlocks the database file at the conclusion of each read or write transaction. When the locking-mode is set to EXCLUSIVE, the database connection never releases file-locks. The first time the database is read in EXCLUSIVE mode, a shared lock is obtained and held. The first time the database is written, an exclusive lock is obtained and held.

Database locks obtained by a connection in EXCLUSIVE mode may be released either by closing the database connection, or by setting the locking-mode back to NORMAL using this pragma and then accessing the database file (for read or write). Simply setting the locking-mode to NORMAL is not enough - locks are not released until the next time the database file is accessed.

There are three reasons to set the locking-mode to EXCLUSIVE.

1.  The application wants to prevent other processes from accessing the database file.
2.  The number of system calls for filesystem operations is reduced, possibly resulting in a small performance increase.
3.  [WAL](wal.md) databases can be accessed in EXCLUSIVE mode without the use of shared memory. ([Additional information](wal.md#noshm))

When the locking_mode pragma specifies a particular database, for example:

> PRAGMA **main.**locking_mode=EXCLUSIVE;

then the locking mode applies only to the named database. If no database name qualifier precedes the "locking_mode" keyword then the locking mode is applied to all databases, including any new databases added by subsequent [ATTACH](lang_attach.md) commands.

The "temp" database (in which TEMP tables and indices are stored) and [in-memory databases](inmemorydb.md) always uses exclusive locking mode. The locking mode of temp and [in-memory databases](inmemorydb.md) cannot be changed. All other databases use the normal locking mode by default and are affected by this pragma.

If the locking mode is EXCLUSIVE when first entering [WAL journal mode](wal.md), then the locking mode cannot be changed to NORMAL until after exiting WAL journal mode. If the locking mode is NORMAL when first entering WAL journal mode, then the locking mode can be changed between NORMAL and EXCLUSIVE and back again at any time and without needing to exit WAL journal mode.

<span id="pragma_max_page_count"></span> PRAGMA max_page_count

------------------------------------------------------------------------

**PRAGMA** *schema.***max_page_count;\
PRAGMA** *schema.***max_page_count =** *N***;**

Query or set the maximum number of pages in the database file. Both forms of the pragma return the maximum page count. The second form attempts to modify the maximum page count. The maximum page count cannot be reduced below the current database size.

<span id="pragma_mmap_size"></span> PRAGMA mmap_size

------------------------------------------------------------------------

\
**PRAGMA** *schema.***mmap_size;\
PRAGMA** *schema.***mmap_size=***N*

Query or change the maximum number of bytes that are set aside for memory-mapped I/O on a single database. The first form (without an argument) queries the current limit. The second form (with a numeric argument) sets the limit for the specified database, or for all databases if the optional database name is omitted. In the second form, if the database name is omitted, the limit that is set becomes the default limit for all databases that are added to the [database connection](c3ref/sqlite3.md) by subsequent [ATTACH](lang_attach.md) statements.

The argument N is the maximum number of bytes of the database file that will be accessed using memory-mapped I/O. If N is zero then memory mapped I/O is disabled. If N is negative, then the limit reverts to the default value determined by the most recent [sqlite3_config](c3ref/config.md)([SQLITE_CONFIG_MMAP_SIZE](c3ref/c_config_covering_index_scan.md#sqliteconfigmmapsize)), or to the compile time default determined by [SQLITE_DEFAULT_MMAP_SIZE](compile.md#default_mmap_size) if no start-time limit has been set.

The [PRAGMA mmap_size](pragma.md#pragma_mmap_size) statement will never increase the amount of address space used for memory-mapped I/O above the hard limit set by the [SQLITE_MAX_MMAP_SIZE](compile.md#max_mmap_size) compile-time option, nor the hard limit set at startup-time by the second argument to sqlite3_config([SQLITE_CONFIG_MMAP_SIZE](c3ref/c_config_covering_index_scan.md#sqliteconfigmmapsize))

The size of the memory-mapped I/O region cannot be changed while the memory-mapped I/O region is in active use, to avoid unmapping memory out from under running SQL statements. For this reason, the mmap_size pragma may be a no-op if the prior mmap_size is non-zero and there are other SQL statements running concurrently on the same [database connection](c3ref/sqlite3.md).

<span id="pragma_module_list"></span> PRAGMA module_list

------------------------------------------------------------------------

**PRAGMA module_list;**

This pragma returns a list of [virtual table](vtab.md) modules registered with the database connection. <span id="pragma_optimize"></span> PRAGMA optimize

------------------------------------------------------------------------

**PRAGMA optimize;\
PRAGMA optimize(***MASK***);\
PRAGMA** *schema***.optimize;\
PRAGMA** *schema***.optimize(***MASK***);**

Attempt to optimize the database. All schemas are optimized in the first two forms, and only the specified schema is optimized in the latter two.

In most applications, using PRAGMA optimize as follows will help SQLite to achieve the best possible query performance:

1.  Applications with short-lived database connections should run "PRAGMA optimize;" once, just prior to closing each database connection.

2.  Applications that use long-lived database connections should run "PRAGMA optimize=0x10002;" when the connection is first opened, and then also run "PRAGMA optimize;" periodically, perhaps once per day or once per hour.

3.  All applications should run "PRAGMA optimize;" after a schema change, especially after one or more [CREATE INDEX](lang_createindex.md) statements.

This pragma is usually a no-op or nearly so and is very fast. On the occasions where it does need to run ANALYZE on one or more tables, it sets a temporary [analysis limit](pragma.md#pragma_analysis_limit), valid for the duration of this pragma only, that prevents the ANALYZE invocations from running for too long.

Recommended practice is that applications with short-lived database connections should run "PRAGMA optimize" once when the database connection closes. Applications with long-lived database connections should run "PRAGMA optimize=0x10002" when the database connection first opens, then run "PRAGMA optimize" again at periodic intervals - perhaps once per day. All applications should run "PRAGMA optimize" after schema changes, especially [CREATE INDEX](lang_createindex.md).

The details of optimizations performed by this pragma are expected to change and improve over time. Applications should anticipate that this pragma will perform new optimizations in future releases.

The optional MASK argument is a bitmask of optimizations to perform:

0x00001

Debugging mode. Do not actually perform any optimizations but instead return one line of text for each optimization that would have been done. Off by default.

0x00002

Run [ANALYZE](lang_analyze.md) on tables that might benefit. On by default.

0x00010

When running [ANALYZE](lang_analyze.md), set a temporary [PRAGMA analysis_limit](pragma.md#pragma_analysis_limit) to prevent excess run-time. On by default.

0x10000

Check the size of all tables, not just tables that have been recently used, to see if any have grown and shrunk significantly and hence might benefit from being re-analyzed. Off by default.

The default MASK is 0xfffe.

To see all optimizations that would have been done without actually doing them, run "PRAGMA optimize(-1)".

**Determination Of When To Run Analyze**

In the current implementation, a table is analyzed if and only if all of the following are true:

1.  MASK bit 0x02 is set.
2.  The table is an ordinary table, not a view or virtual table.
3.  The table name does not begin with "sqlite\_".
4.  One or more of the following are true:
    1.  The 0x10000 bit of MASK is set
    2.  One or more indexes on the table lack entries in the sqlite_stat1 table.
    3.  The query planner used sqlite_stat1 statistics for one or more indexes of this table at some point during the lifetime of the current database connection.
5.  One or more of the following are true:
    1.  One or more indexes on the table lack entries in the sqlite_stat1 table.
    2.  The number of rows in the table has increased or decreased by 10-fold since the last time ANALYZE was run on the table.

The rules for when tables are analyzed are likely to change in future releases. New MASK values may be added in the future. Future versions of this pragma might accept a string literal argument instead of a bit mask, though the bit mask argument will continue to be supported for backwards compatibility. <span id="pragma_page_count"></span> PRAGMA page_count

------------------------------------------------------------------------

**PRAGMA** *schema.***page_count;**

Return the total number of pages in the database file.

<span id="pragma_page_size"></span> PRAGMA page_size

------------------------------------------------------------------------

**PRAGMA** *schema.***page_size;\
PRAGMA** *schema.***page_size =** *bytes***;**

Query or set the page size of the database. The page size must be a power of two between 512 and 65536 inclusive.

When a new database is created, SQLite assigns a page size to the database based on platform and filesystem. For many years, the default page size was almost always 1024 bytes, but beginning with SQLite [version 3.12.0](releaselog/3_12_0.md) (2016-03-29), the default page size increased to 4096. The default page size is recommended for most applications.

Specifying a new page size does not change the page size immediately. Instead, the new page size is remembered and is used to set the page size when the database is first created, if it does not already exist when the page_size pragma is issued, or at the next [VACUUM](lang_vacuum.md) command that is run on the same database connection while not in [WAL mode](wal.md).

The [SQLITE_DEFAULT_PAGE_SIZE](compile.md#default_page_size) compile-time option can be used to change the default page size assigned to new databases. <span id="pragma_parser_trace"></span> PRAGMA parser_trace

------------------------------------------------------------------------

**PRAGMA parser_trace =** *boolean***;**

If SQLite has been compiled with the [SQLITE_DEBUG](compile.md#debug) compile-time option, then the parser_trace pragma can be used to turn on tracing for the SQL parser used internally by SQLite. This feature is used for debugging SQLite itself.

This pragma is intended for use when debugging SQLite itself. It is only available when the [SQLITE_DEBUG](compile.md#debug) compile-time option is used.

<span id="pragma_pragma_list"></span> PRAGMA pragma_list

------------------------------------------------------------------------

**PRAGMA pragma_list;**

This pragma returns a list of PRAGMA commands known to the database connection. <span id="pragma_query_only"></span> PRAGMA query_only

------------------------------------------------------------------------

**PRAGMA query_only;\
PRAGMA query_only =** *boolean***;**

The query_only pragma prevents data changes on database files when enabled. When this pragma is enabled, any attempt to CREATE, DELETE, DROP, INSERT, or UPDATE will result in an [SQLITE_READONLY](rescode.md#readonly) error. However, the database is not truly read-only. You can still run a [checkpoint](wal.md#ckpt) or a [COMMIT](lang_transaction.md) and the return value of the [sqlite3_db_readonly()](c3ref/db_readonly.md) routine is not affected.

<span id="pragma_quick_check"></span> PRAGMA quick_check

------------------------------------------------------------------------

**PRAGMA** *schema.***quick_check;\
PRAGMA** *schema.***quick_check(***N***)**\
PRAGMA *schema.***quick_check(***TABLENAME***)**

The pragma is like [integrity_check](pragma.md#pragma_integrity_check) except that it does not verify UNIQUE constraints and does not verify that index content matches table content. By skipping UNIQUE and index consistency checks, quick_check is able to run faster. PRAGMA quick_check runs in O(N) time whereas [PRAGMA integrity_check](pragma.md#pragma_integrity_check) requires O(NlogN) time where N is the total number of rows in the database. Otherwise the two pragmas are the same.

<span id="pragma_read_uncommitted"></span> PRAGMA read_uncommitted

------------------------------------------------------------------------

**PRAGMA read_uncommitted;\
PRAGMA read_uncommitted =** *boolean***;**

Query, set, or clear READ UNCOMMITTED isolation. The default isolation level for SQLite is SERIALIZABLE. Any process or thread can select READ UNCOMMITTED isolation, but SERIALIZABLE will still be used except between connections that share a common page and schema cache. Cache sharing is enabled using the [sqlite3_enable_shared_cache()](c3ref/enable_shared_cache.md) API. Cache sharing is disabled by default.

See [SQLite Shared-Cache Mode](sharedcache.md) for additional information.

<span id="pragma_recursive_triggers"></span> PRAGMA recursive_triggers

------------------------------------------------------------------------

**PRAGMA recursive_triggers;\
PRAGMA recursive_triggers =** *boolean***;**

Query, set, or clear the recursive trigger capability.

Changing the recursive_triggers setting affects the execution of all statements prepared using the database connection, including those prepared before the setting was changed. Any existing statements prepared using the legacy [sqlite3_prepare()](c3ref/prepare.md) interface may fail with an [SQLITE_SCHEMA](rescode.md#schema) error after the recursive_triggers setting is changed.

Prior to SQLite [version 3.6.18](releaselog/3_6_18.md) (2009-09-11), recursive triggers were not supported. The behavior of SQLite was always as if this pragma was set to OFF. Support for recursive triggers was added in version 3.6.18 but was initially turned OFF by default, for compatibility. Recursive triggers may be turned on by default in future versions of SQLite.

The depth of recursion for triggers has a hard upper limit set by the [SQLITE_MAX_TRIGGER_DEPTH](limits.md#max_trigger_depth) compile-time option and a run-time limit set by [sqlite3_limit](c3ref/limit.md)(db,[SQLITE_LIMIT_TRIGGER_DEPTH](c3ref/c_limit_attached.md#sqlitelimittriggerdepth),...).

<span id="pragma_reverse_unordered_selects"></span> PRAGMA reverse_unordered_selects

------------------------------------------------------------------------

**PRAGMA reverse_unordered_selects;\
PRAGMA reverse_unordered_selects =** *boolean***;**

When enabled, this PRAGMA causes many [SELECT](lang_select.md) statements without an ORDER BY clause to emit their results in the reverse order from what they normally would. This can help debug applications that are making invalid assumptions about the result order. The reverse_unordered_selects pragma works for most SELECT statements, however the query planner may sometimes choose an algorithm that is not easily reversed, in which case the output will appear in the same order regardless of the reverse_unordered_selects setting.

SQLite makes no guarantees about the order of results if a SELECT omits the ORDER BY clause. Even so, the order of results does not change from one run to the next, and so many applications mistakenly come to depend on the arbitrary output order whatever that order happens to be. However, sometimes new versions of SQLite will contain optimizer enhancements that will cause the output order of queries without ORDER BY clauses to shift. When that happens, applications that depend on a certain output order might malfunction. By running the application multiple times with this pragma both disabled and enabled, cases where the application makes faulty assumptions about output order can be identified and fixed early, reducing problems that might be caused by linking against a different version of SQLite.

<span id="pragma_schema_version"></span> PRAGMA schema_version

------------------------------------------------------------------------

**PRAGMA** *schema.***schema_version;\
PRAGMA** *schema.***schema_version =** *integer* ;

The schema_version pragma will get or set the value of the schema-version integer at offset 40 in the [database header](fileformat2.md#database_header).

SQLite automatically increments the schema-version whenever the schema changes. As each SQL statement runs, the schema version is checked to ensure that the schema has not changed since the SQL statement was [prepared](c3ref/prepare.md). Subverting this mechanism by using "PRAGMA schema_version=N" to change the value of the schema_version may cause SQL statement to run using an obsolete schema, which can lead to incorrect answers and/or [database corruption](howtocorrupt.md#cfgerr). It is always safe to read the schema_version, but changing the schema_version can cause problems. For this reason, attempts to change the value of schema_version are a silent no-op when [defensive mode](c3ref/c_dbconfig_defensive.md#sqlitedbconfigdefensive) is enabled for a database connection.

<span style="background-color: #ffff60;"> **Warning:** Misuse of this pragma can result in [database corruption](howtocorrupt.md#cfgerr). </span>

For the purposes of this pragma, the [VACUUM](lang_vacuum.md) command is considered a schema change, since [VACUUM](lang_vacuum.md) will usually alter the "rootpage" values for entries in the [sqlite_schema table](schematab.md).

See also the [application_id pragma](pragma.md#pragma_application_id) and [user_version pragma](pragma.md#pragma_user_version). <span id="pragma_secure_delete"></span> PRAGMA secure_delete

------------------------------------------------------------------------

**PRAGMA** *schema.***secure_delete;\
PRAGMA** *schema.***secure_delete =** *boolean*\|**FAST**

Query or change the secure-delete setting. When secure_delete is on, SQLite overwrites deleted content with zeros. The default setting for secure_delete is determined by the [SQLITE_SECURE_DELETE](compile.md#secure_delete) compile-time option and is normally off. The off setting for secure_delete improves performance by reducing the number of CPU cycles and the amount of disk I/O. Applications that wish to avoid leaving forensic traces after content is deleted or updated should enable the secure_delete pragma prior to performing the delete or update, or else run [VACUUM](lang_vacuum.md) after the delete or update.

The "fast" setting for secure_delete (added circa 2017-08-01) is an intermediate setting in between "on" and "off". When secure_delete is set to "fast", SQLite will overwrite deleted content with zeros only if doing so does not increase the amount of I/O. In other words, the "fast" setting uses more CPU cycles but does not use more I/O. This has the effect of purging all old content from [b-tree pages](fileformat2.md#btree), but leaving forensic traces on [freelist pages](fileformat2.md#freelist).

When there are [attached databases](lang_attach.md) and no database is specified in the pragma, all databases have their secure-delete setting altered. The secure-delete setting for newly attached databases is the setting of the main database at the time the ATTACH command is evaluated.

When multiple database connections share the same cache, changing the secure-delete flag on one database connection changes it for them all.

**Limitation:** The secure_delete pragma only causes deleted content to be scrubbed from ordinary tables. If [virtual tables](vtab.md) store content in [shadow tables](vtab.md#xshadowname), then deleting content from the virtual table does not necessarily remove forensic traces from the shadow tables. In particular, the [FTS3](fts3.md) and [FTS5](fts5.md) virtual tables that come bundled with SQLite might leave forensic traces in their shadow tables even if the secure_delete pragma is enabled.

<span id="pragma_short_column_names"></span> PRAGMA short_column_names

------------------------------------------------------------------------

**PRAGMA short_column_names;\
PRAGMA short_column_names =** *boolean***;**

Query or change the short-column-names flag. This flag affects the way SQLite names columns of data returned by [SELECT](lang_select.md) statements. See the [full_column_names](pragma.md#pragma_full_column_names) pragma for full details.

**This pragma is deprecated** and exists for backwards compatibility only. New applications should avoid using this pragma. Older applications should discontinue use of this pragma at the earliest opportunity. This pragma may be omitted from the build when SQLite is compiled using [SQLITE_OMIT_DEPRECATED](compile.md#omit_deprecated).

<span id="pragma_shrink_memory"></span> PRAGMA shrink_memory

------------------------------------------------------------------------

**PRAGMA shrink_memory**

This pragma causes the database connection on which it is invoked to free up as much memory as it can, by calling [sqlite3_db_release_memory()](c3ref/db_release_memory.md).

<span id="pragma_soft_heap_limit"></span> PRAGMA soft_heap_limit

------------------------------------------------------------------------

**PRAGMA soft_heap_limit\
PRAGMA soft_heap_limit=***N*

This pragma invokes the [sqlite3_soft_heap_limit64()](c3ref/hard_heap_limit64.md) interface with the argument N, if N is specified and is a non-negative integer. The soft_heap_limit pragma always returns the same integer that would be returned by the [sqlite3_soft_heap_limit64](c3ref/hard_heap_limit64.md)(-1) C-language function.

See also the [hard_heap_limit pragma](pragma.md#pragma_hard_heap_limit). <span id="pragma_stats"></span> PRAGMA stats

------------------------------------------------------------------------

**PRAGMA stats;**

This pragma returns auxiliary information about tables and indices. The returned information is used during testing to help verify that the query planner is operating correctly. The format and meaning of this pragma will likely change from one release to the next. Because of its volatility, the behavior and output format of this pragma are deliberately undocumented.

The intended use of this pragma is only for testing and validation of SQLite. This pragma is subject to change without notice and is not recommended for use by application programs.

<span id="pragma_synchronous"></span> PRAGMA synchronous

------------------------------------------------------------------------

**PRAGMA** *schema.***synchronous;\
PRAGMA** *schema.***synchronous =** *0 \| OFF \| 1 \| NORMAL \| 2 \| FULL \| 3 \| EXTRA***;**

Query or change the setting of the "synchronous" flag. The first (query) form will return the synchronous setting as an integer. The second form changes the synchronous setting. The meanings of the various synchronous settings are as follows:

**EXTRA** (3)  
EXTRA synchronous is like FULL with the addition that the directory containing a [rollback journal](lockingv3.md#rollback) is synced after that journal is unlinked to commit a transaction in DELETE mode. EXTRA provides additional durability if the commit is followed closely by a power loss. Without EXTRA, depending on the underlying filesystem, it is possible that a single transaction that commits right before a power loss might get rolled back upon reboot. The database will not go corrupt. But the last transaction might go missing, thus violating durability, if EXTRA is not set.

EXTRA is no different from FULL in [WAL mode](wal.md).

**FULL** (2)  
When synchronous is FULL (2), the SQLite database engine will use the xSync method of the [VFS](vfs.md) to ensure that all content is safely written to the disk surface prior to continuing. This ensures that an operating system crash or power failure will not corrupt the database.

FULL is the default synchronous mode for a [rollback journal](lockingv3.md#rollback). FULL is atomic, consistent, isolated, and durable (ACID) in [WAL mode](wal.md) and is atomic, consistent, and isolated with a [rollback journal](lockingv3.md#rollback). FULL might also be durable using a rollback journal, depending on the underlying filesystem. FULL is not necessarily durable across a power loss in rollback mode, so if durability is desired, it is best to set the synchronous mode to EXTRA.

**NORMAL** (1)  
When synchronous is NORMAL (1), the SQLite database engine will still sync at the most critical moments, but less often than in FULL mode. There is a very small (though non-zero) chance that a power failure at just the wrong time could corrupt the database in [journal_mode](pragma.md#pragma_journal_mode)=DELETE on an older filesystem. [WAL mode](wal.md) is safe from corruption with synchronous=NORMAL, and probably DELETE mode is safe too on modern filesystems. WAL mode is always consistent with synchronous=NORMAL, but WAL mode does lose durability. A transaction committed in WAL mode with synchronous=NORMAL might roll back following a power loss or system crash. Transactions are durable across application crashes regardless of the synchronous setting or journal mode.

The synchronous=NORMAL setting provides the best balance between performance and safety for most applications running in [WAL mode](wal.md). You lose durability across power lose with synchronous NORMAL in WAL mode, but that is not important for most applications. Transactions are still atomic, consistent, and isolated, which are the most important characteristics in most use cases.

**OFF** (0)  
With synchronous OFF (0), SQLite continues without syncing as soon as it has handed data off to the operating system. If the application running SQLite crashes, the data will be safe, but the database [might become corrupted](howtocorrupt.md#cfgerr) if the operating system crashes or the computer loses power before that data has been written to non-volatile storage. On the other hand, commits can be much faster with synchronous OFF.

Setting synchronous to OFF is a good option when creating a new database from scratch, in a scenario where the process of creating the database can be repeated if a power loss occurs in the middle, and when performance is critical.

Here is the matrix:

 

 Rollback Mode 

 WAL Mode 

 EXTRA 

 ACID 

 ACID 

 FULL 

 Maybe not durable 

 ACID 

 NORMAL 

 Maybe not consistent 

 Maybe not durable 

 OFF 

 Not consistent 

 Not consistent 

In [WAL](wal.md) mode when synchronous is NORMAL (1), the WAL file is synchronized before each [checkpoint](wal.md#ckpt) and the database file is synchronized after each completed [checkpoint](wal.md#ckpt) and the WAL file header is synchronized when a WAL file begins to be reused after a checkpoint, but no sync operations occur during most transactions. With synchronous=FULL in WAL mode, an additional sync operation of the WAL file happens after each transaction commit. The extra WAL sync following each transaction helps ensure that transactions are durable across a power loss. Transactions are consistent with or without the extra syncs provided by synchronous=FULL. If durability is not a concern, then synchronous=NORMAL is normally all one needs in WAL mode.

The TEMP schema always has synchronous=OFF since the content of of TEMP is ephemeral and is not expected to survive a power outage. Attempts to change the synchronous setting for TEMP are silently ignored.

See also the [fullfsync](pragma.md#pragma_fullfsync) and [checkpoint_fullfsync](pragma.md#pragma_checkpoint_fullfsync) pragmas.

<span id="pragma_table_info"></span> PRAGMA table_info

------------------------------------------------------------------------

**PRAGMA** *schema.***table_info(***table-name***);**

This pragma returns one row for each normal column in the named table. Columns in the result set include: "name" (its name); "type" (data type if given, else ''); "notnull" (whether or not the column can be NULL); "dflt_value" (the default value for the column); and "pk" (either zero for columns that are not part of the primary key, or the 1-based index of the column within the primary key).

The "cid" column should not be taken to mean more than "rank within the current result set".

The table named in the table_info pragma can also be a view.

This pragma does not show information about [generated columns](gencol.md) or [hidden columns](vtab.md#hiddencol). Use [PRAGMA table_xinfo](pragma.md#pragma_table_xinfo) to get a more complete list of columns that includes generated and hidden columns. <span id="pragma_table_list"></span> PRAGMA table_list

------------------------------------------------------------------------

**PRAGMA table_list;\
PRAGMA** *schema.***table_list;\
PRAGMA table_list(***table-name***);**

This pragma returns information about the tables and views in the schema, one table per row of output. The table_list pragma first appeared in SQLite version 3.37.0 (2021-11-27). As of its initial release the columns returned by the table_list pragma include those listed below. Future versions of SQLite will probably add additional columns of output.

1.  **schema**: the schema in which the table or view appears (for example "main" or "temp").
2.  **name**: the name of the table or view.
3.  **type**: the type of object - one of "table", "view", "shadow" (for [shadow tables](vtab.md#xshadowname)), or "virtual" for [virtual tables](vtab.md).
4.  **ncol**: the number of columns in the table, including [generated columns](gencol.md) and [hidden columns](vtab.md#hiddencol).
5.  **wr**: 1 if the table is a [WITHOUT ROWID](withoutrowid.md) table or 0 if is not.
6.  **strict**: 1 if the table is a [STRICT table](stricttables.md) or 0 if it is not.
7.  *Additional columns will likely be added in future releases.*

The default behavior is to show all tables in all schemas. If the *schema.* name appears before the pragma, then only tables in that one schema are shown. If a *table-name* argument is supplied, then only information about that one table is returned. <span id="pragma_table_xinfo"></span> PRAGMA table_xinfo

------------------------------------------------------------------------

**PRAGMA** *schema.***table_xinfo(***table-name***);**

This pragma returns one row for each column in the named table, including [generated columns](gencol.md) and [hidden columns](vtab.md#hiddencol). The output has the same columns as for [PRAGMA table_info](pragma.md#pragma_table_info) plus a column, "hidden", whose value signifies a normal column (0), a dynamic or stored generated column (2 or 3), or a hidden column in a virtual table (1). The rows for which this field is non-zero are those omitted for [PRAGMA table_info](pragma.md#pragma_table_info). <span id="pragma_temp_store"></span> PRAGMA temp_store

------------------------------------------------------------------------

**PRAGMA temp_store;\
PRAGMA temp_store =** *0 \| DEFAULT \| 1 \| FILE \| 2 \| MEMORY***;**

Query or change the setting of the "**temp_store**" parameter. When temp_store is DEFAULT (0), the compile-time C preprocessor macro [SQLITE_TEMP_STORE](compile.md#temp_store) is used to determine where temporary tables and indices are stored. When temp_store is MEMORY (2) [temporary tables](inmemorydb.md#temp_db) and indices are kept as if they were in pure [in-memory databases](inmemorydb.md). When temp_store is FILE (1) [temporary tables](inmemorydb.md#temp_db) and indices are stored in a file. The [temp_store_directory](pragma.md#pragma_temp_store_directory) pragma can be used to specify the directory containing temporary files when **FILE** is specified. When the temp_store setting is changed, all existing temporary tables, indices, triggers, and views are immediately deleted.

It is possible for the library compile-time C preprocessor symbol [SQLITE_TEMP_STORE](compile.md#temp_store) to override this pragma setting. The following table summarizes the interaction of the [SQLITE_TEMP_STORE](compile.md#temp_store) preprocessor macro and the temp_store pragma:

> <table data-cellpadding="2" data-border="1">
> <colgroup>
> <col style="width: 33%" />
> <col style="width: 33%" />
> <col style="width: 33%" />
> </colgroup>
> <thead>
> <tr>
> <th style="text-align: center;" data-valign="bottom"><a href="compile.html#temp_store">SQLITE_TEMP_STORE</a></th>
> <th style="text-align: center;" data-valign="bottom">PRAGMA<br />
> temp_store</th>
> <th style="text-align: center;">Storage used for<br />
> TEMP tables and indices</th>
> </tr>
> </thead>
> <tbody>
> <tr>
> <td style="text-align: center;">0</td>
> <td style="text-align: center;"><em>any</em></td>
> <td style="text-align: center;">file</td>
> </tr>
> <tr>
> <td style="text-align: center;">1</td>
> <td style="text-align: center;">0</td>
> <td style="text-align: center;">file</td>
> </tr>
> <tr>
> <td style="text-align: center;">1</td>
> <td style="text-align: center;">1</td>
> <td style="text-align: center;">file</td>
> </tr>
> <tr>
> <td style="text-align: center;">1</td>
> <td style="text-align: center;">2</td>
> <td style="text-align: center;">memory</td>
> </tr>
> <tr>
> <td style="text-align: center;">2</td>
> <td style="text-align: center;">0</td>
> <td style="text-align: center;">memory</td>
> </tr>
> <tr>
> <td style="text-align: center;">2</td>
> <td style="text-align: center;">1</td>
> <td style="text-align: center;">file</td>
> </tr>
> <tr>
> <td style="text-align: center;">2</td>
> <td style="text-align: center;">2</td>
> <td style="text-align: center;">memory</td>
> </tr>
> <tr>
> <td style="text-align: center;">3</td>
> <td style="text-align: center;"><em>any</em></td>
> <td style="text-align: center;">memory</td>
> </tr>
> </tbody>
> </table>

<span id="pragma_temp_store_directory"></span> PRAGMA temp_store_directory

------------------------------------------------------------------------

**PRAGMA temp_store_directory;\
PRAGMA temp_store_directory = '***directory-name***';**

Query or change the value of the [sqlite3_temp_directory](c3ref/temp_directory.md) global variable, which many operating-system interface backends use to determine where to store [temporary tables](inmemorydb.md#temp_db) and indices.

When the temp_store_directory setting is changed, all existing temporary tables, indices, triggers, and viewers in the database connection that issued the pragma are immediately deleted. In practice, temp_store_directory should be set immediately after the first database connection for a process is opened. If the temp_store_directory is changed for one database connection while other database connections are open in the same process, then the behavior is undefined and probably undesirable.

Changing the temp_store_directory setting is <u>not</u> threadsafe. Never change the temp_store_directory setting if another thread within the application is running any SQLite interface at the same time. Doing so results in undefined behavior. Changing the temp_store_directory setting writes to the [sqlite3_temp_directory](c3ref/temp_directory.md) global variable and that global variable is not protected by a mutex.

The value *directory-name* should be enclosed in single quotes. To revert the directory to the default, set the *directory-name* to an empty string, e.g., *PRAGMA temp_store_directory = ''*. An error is raised if *directory-name* is not found or is not writable.

The default directory for temporary files depends on the OS. Some OS interfaces may choose to ignore this variable and place temporary files in some other directory different from the directory specified here. In that sense, this pragma is only advisory.

**This pragma is deprecated** and exists for backwards compatibility only. New applications should avoid using this pragma. Older applications should discontinue use of this pragma at the earliest opportunity. This pragma may be omitted from the build when SQLite is compiled using [SQLITE_OMIT_DEPRECATED](compile.md#omit_deprecated).

<span id="pragma_threads"></span> PRAGMA threads

------------------------------------------------------------------------

**PRAGMA threads;\
PRAGMA threads =** *N***;**

Query or change the value of the [sqlite3_limit](c3ref/limit.md)(db,[SQLITE_LIMIT_WORKER_THREADS](c3ref/c_limit_attached.md#sqlitelimitworkerthreads),...) limit for the current database connection. This limit sets an upper bound on the number of auxiliary threads that a [prepared statement](c3ref/stmt.md) is allowed to launch to assist with a query. The default limit is 0 unless it is changed using the [SQLITE_DEFAULT_WORKER_THREADS](compile.md#default_worker_threads) compile-time option. When the limit is zero, that means no auxiliary threads will be launched.

This pragma is a thin wrapper around the [sqlite3_limit](c3ref/limit.md)(db,[SQLITE_LIMIT_WORKER_THREADS](c3ref/c_limit_attached.md#sqlitelimitworkerthreads),...) interface.

<span id="pragma_trusted_schema"></span> PRAGMA trusted_schema

------------------------------------------------------------------------

**PRAGMA trusted_schema;\
PRAGMA trusted_schema =** *boolean***;**

The trusted_schema setting is a per-connection boolean that determines whether or not SQL functions and virtual tables that have not been security audited are allowed to be run by views, triggers, or in expressions of the schema such as [CHECK constraints](lang_createtable.md#ckconst), [DEFAULT clauses](lang_createtable.md#dfltval), [generated columns](gencol.md), [expression indexes](expridx.md), and/or [partial indexes](partialindex.md). This setting can also be controlled using the [sqlite3_db_config](c3ref/db_config.md)(db,[SQLITE_DBCONFIG_TRUSTED_SCHEMA](c3ref/c_dbconfig_defensive.md#sqlitedbconfigtrustedschema),...) C-language interface.

In order to maintain backwards compatibility, this setting is ON by default. There are advantages to turning it off, and most applications will be unaffected if it is turned off. For that reason, all applications are encouraged to switch this setting off on every database connection as soon as that connection is opened.

The [-DSQLITE_TRUSTED_SCHEMA=0](compile.md#trusted_schema) compile-time option will cause this setting to default to OFF. <span id="pragma_user_version"></span> PRAGMA user_version

------------------------------------------------------------------------

**PRAGMA** *schema.***user_version;\
PRAGMA** *schema.***user_version =** *integer* **;**

The user_version pragma will get or set the value of the user-version integer at offset 60 in the [database header](fileformat2.md#database_header). The user-version is an integer that is available to applications to use however they want. SQLite makes no use of the user-version itself.

See also the [application_id pragma](pragma.md#pragma_application_id) and [schema_version pragma](pragma.md#pragma_schema_version). <span id="pragma_vdbe_addoptrace"></span> PRAGMA vdbe_addoptrace

------------------------------------------------------------------------

**PRAGMA vdbe_addoptrace =** *boolean***;**

If SQLite has been compiled with the [SQLITE_DEBUG](compile.md#debug) compile-time option, then the vdbe_addoptrace pragma can be used to cause complete VDBE opcodes to be displayed as they are created during code generation. This feature is used for debugging SQLite itself. See the [VDBE documentation](vdbe.md#trace) for more information.

This pragma is intended for use when debugging SQLite itself. It is only available when the [SQLITE_DEBUG](compile.md#debug) compile-time option is used.

<span id="pragma_vdbe_debug"></span> PRAGMA vdbe_debug

------------------------------------------------------------------------

**PRAGMA vdbe_debug =** *boolean***;**

If SQLite has been compiled with the [SQLITE_DEBUG](compile.md#debug) compile-time option, then the vdbe_debug pragma is a shorthand for three other debug-only pragmas: vdbe_addoptrace, vdbe_listing, and vdbe_trace. This feature is used for debugging SQLite itself. See the [VDBE documentation](vdbe.md#trace) for more information.

This pragma is intended for use when debugging SQLite itself. It is only available when the [SQLITE_DEBUG](compile.md#debug) compile-time option is used.

<span id="pragma_vdbe_listing"></span> PRAGMA vdbe_listing

------------------------------------------------------------------------

**PRAGMA vdbe_listing =** *boolean***;**

If SQLite has been compiled with the [SQLITE_DEBUG](compile.md#debug) compile-time option, then the vdbe_listing pragma can be used to cause a complete listing of the virtual machine opcodes to appear on standard output as each statement is evaluated. When vdbe_listing is on, the entire content of a program is printed just prior to beginning execution. The statement executes normally after the listing is printed. This feature is used for debugging SQLite itself. See the [VDBE documentation](vdbe.md#trace) for more information.

This pragma is intended for use when debugging SQLite itself. It is only available when the [SQLITE_DEBUG](compile.md#debug) compile-time option is used.

<span id="pragma_vdbe_trace"></span> PRAGMA vdbe_trace

------------------------------------------------------------------------

**PRAGMA vdbe_trace =** *boolean***;**

If SQLite has been compiled with the [SQLITE_DEBUG](compile.md#debug) compile-time option, then the vdbe_trace pragma can be used to cause virtual machine opcodes to be printed on standard output as they are evaluated. This feature is used for debugging SQLite. See the [VDBE documentation](vdbe.md#trace) for more information.

This pragma is intended for use when debugging SQLite itself. It is only available when the [SQLITE_DEBUG](compile.md#debug) compile-time option is used.

<span id="pragma_wal_autocheckpoint"></span> PRAGMA wal_autocheckpoint

------------------------------------------------------------------------

**PRAGMA wal_autocheckpoint;\
PRAGMA wal_autocheckpoint=***N***;**

This pragma queries or sets the [write-ahead log](wal.md) [auto-checkpoint](wal.md#ckpt) interval. When the [write-ahead log](wal.md) is enabled (via the [journal_mode pragma](pragma.md#pragma_journal_mode)) a checkpoint will be run automatically whenever the write-ahead log equals or exceeds *N* pages in length. Setting the auto-checkpoint size to zero or a negative value turns auto-checkpointing off.

This pragma is a wrapper around the [sqlite3_wal_autocheckpoint()](c3ref/wal_autocheckpoint.md) C interface. All automatic checkpoints are [PASSIVE](c3ref/wal_checkpoint_v2.md).

Autocheckpointing is enabled by default with an interval of 1000 or [SQLITE_DEFAULT_WAL_AUTOCHECKPOINT](compile.md#default_wal_autocheckpoint).

<span id="pragma_wal_checkpoint"></span> PRAGMA wal_checkpoint

------------------------------------------------------------------------

**PRAGMA** *schema.***wal_checkpoint;**\
**PRAGMA** *schema.***wal_checkpoint(PASSIVE);**\
**PRAGMA** *schema.***wal_checkpoint(FULL);**\
**PRAGMA** *schema.***wal_checkpoint(RESTART);**\
**PRAGMA** *schema.***wal_checkpoint(TRUNCATE);**\
**PRAGMA** *schema.***wal_checkpoint(NOOP);**

If the [write-ahead log](wal.md) is enabled (via the [journal_mode pragma](pragma.md#pragma_journal_mode)), this pragma causes a [checkpoint](wal.md#ckpt) operation to run on database *database*, or on all attached databases if *database* is omitted. If [write-ahead log](wal.md) mode is disabled, this pragma is a harmless no-op.

Invoking this pragma without an argument is equivalent to calling the [sqlite3_wal_checkpoint()](c3ref/wal_checkpoint.md) C interface.

Invoking this pragma with an argument is equivalent to calling the [sqlite3_wal_checkpoint_v2()](c3ref/wal_checkpoint_v2.md) C interface with a [3rd parameter](c3ref/c_checkpoint_full.md) corresponding to the argument:

PASSIVE  
Checkpoint as many frames as possible without waiting for any database readers or writers to finish. Sync the db file if all frames in the log are checkpointed. This mode is the same as calling the [sqlite3_wal_checkpoint()](c3ref/wal_checkpoint.md) C interface. The [busy-handler callback](c3ref/busy_handler.md) is never invoked in this mode.

FULL  
This mode blocks (invokes the [busy-handler callback](c3ref/busy_handler.md)) until there is no database writer and all readers are reading from the most recent database snapshot. It then checkpoints all frames in the log file and syncs the database file. FULL blocks concurrent writers while it is running, but readers can proceed.

RESTART  
This mode works the same way as FULL with the addition that after checkpointing the log file it blocks (calls the [busy-handler callback](c3ref/busy_handler.md)) until all readers are finished with the log file. This ensures that the next client to write to the database file restarts the log file from the beginning. RESTART blocks concurrent writers while it is running, but allows readers to proceed.

TRUNCATE  
This mode works the same way as RESTART with the addition that the WAL file is truncated to zero bytes upon successful completion.

NOOP  
This mode does not checkpoint any frames. It is used to obtain the returned values only.

The wal_checkpoint pragma returns a single row with three integer columns. The first column is usually 0 but will be 1 if a RESTART or FULL or TRUNCATE checkpoint was blocked from completing, for example because another thread or process was actively using the database. In other words, the first column is 0 if the equivalent call to [sqlite3_wal_checkpoint_v2()](c3ref/wal_checkpoint_v2.md) would have returned [SQLITE_OK](rescode.md#ok) or 1 if the equivalent call would have returned [SQLITE_BUSY](rescode.md#busy). The second column is the number of modified pages that have been written to the write-ahead log file. The third column is the number of pages in the write-ahead log file that have been successfully moved back into the database file at the conclusion of the checkpoint. The second and third column are -1 if there is no write-ahead log, for example if this pragma is invoked on a database connection that is not in [WAL mode](wal.md).

<span id="pragma_writable_schema"></span> PRAGMA writable_schema

------------------------------------------------------------------------

**PRAGMA writable_schema =** *boolean***;**\
**PRAGMA writable_schema = RESET**

When this pragma is on, and the [SQLITE_DBCONFIG_DEFENSIVE](c3ref/c_dbconfig_defensive.md#sqlitedbconfigdefensive) flag is off, then the [sqlite_schema](schematab.md) table can be changed using ordinary [UPDATE](lang_update.md), [INSERT](lang_insert.md), and [DELETE](lang_delete.md) statements. If the argument is "RESET" then schema writing is disabled (as with "PRAGMA writable_schema=OFF") and, in addition, the schema is reloaded. <span style="background-color: #ffff60;">**Warning:** misuse of this pragma can easily result in a [corrupt database file](howtocorrupt.md#cfgerr).</span>

------------------------------------------------------------------------
