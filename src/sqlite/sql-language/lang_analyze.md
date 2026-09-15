---
title: ANALYZE
source_url: https://www.sqlite.org/lang_analyze.html
source_path: lang_analyze.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: sql-language
order: 3150
---

# 1. Overview

**[analyze-stmt:](syntax/analyze-stmt.md)** hide

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSJmb250LXNpemU6aW5pdGlhbDsiIGNsYXNzPSJwaWtjaHIiIHZpZXdib3g9IjAgMCA2NTQuNTU3IDE0MC40IiBkYXRhLXBpa2Noci1kYXRlPSIyMDI1MDMxOTE2MTk0MyI+CjxjaXJjbGUgY3g9IjUuNzYiIGN5PSIxNy4yOCIgcj0iMy42IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyI+PC9jaXJjbGU+Cjxwb2x5Z29uIHBvaW50cz0iMzIuNCwxNy4yOCAyMC44OCwyMS42IDIwLjg4LDEyLjk2IiBzdHlsZT0iZmlsbDpyZ2IoMCwwLDApIj48L3BvbHlnb24+CjxwYXRoIGQ9Ik05LjM2LDE3LjI4TDI2LjY0LDE3LjI4IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHBhdGggZD0iTTQ3LjUyLDMyLjRMMTExLjk3NCwzMi40QTE1LjEyIDE1LjEyIDAgMCAwIDEyNy4wOTQgMTcuMjhBMTUuMTIgMTUuMTIgMCAwIDAgMTExLjk3NCAyLjE2TDQ3LjUyLDIuMTZBMTUuMTIgMTUuMTIgMCAwIDAgMzIuNCAxNy4yOEExNS4xMiAxNS4xMiAwIDAgMCA0Ny41MiAzMi40WiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+Cjx0ZXh0IHg9Ijc5Ljc0NzIiIHk9IjE3LjI4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSJyZ2IoMCwwLDApIiBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCI+QU5BTFlaRTwvdGV4dD4KPHBvbHlnb24gcG9pbnRzPSIxNTAuMTM0LDE3LjI4IDEzOC42MTQsMjEuNiAxMzguNjE0LDEyLjk2IiBzdHlsZT0iZmlsbDpyZ2IoMCwwLDApIj48L3BvbHlnb24+CjxwYXRoIGQ9Ik0xMjcuMDk0LDE3LjI4TDE0NC4zNzQsMTcuMjgiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cG9seWdvbiBwb2ludHM9IjE4OC4xNzQsMTIzLjEyIDE3Ni42NTQsMTI3LjQ0IDE3Ni42NTQsMTE4LjgiIHN0eWxlPSJmaWxsOnJnYigwLDAsMCkiPjwvcG9seWdvbj4KPHBhdGggZD0iTTE1MC4xMzQsMTcuMjggTCAxNTcuNjM0LDE3LjI4IFEgMTY1LjEzNCwxNy4yOCAxNjUuMTM0LDMyLjI4IEwgMTY1LjEzNCwxMDguMTIgUSAxNjUuMTM0LDEyMy4xMiAxNzMuNzc0LDEyMy4xMiBMIDE4Mi40MTQsMTIzLjEyIiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHBhdGggZD0iTTIwMy4yOTQsMTM4LjI0TDI5OS42NTksMTM4LjI0QTE1LjEyIDE1LjEyIDAgMCAwIDMxNC43NzkgMTIzLjEyQTE1LjEyIDE1LjEyIDAgMCAwIDI5OS42NTkgMTA4TDIwMy4yOTQsMTA4QTE1LjEyIDE1LjEyIDAgMCAwIDE4OC4xNzQgMTIzLjEyQTE1LjEyIDE1LjEyIDAgMCAwIDIwMy4yOTQgMTM4LjI0WiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+Cjx0ZXh0IHg9IjI1MS40NzciIHk9IjEyMy4xMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0icmdiKDAsMCwwKSIgZG9taW5hbnQtYmFzZWxpbmU9ImNlbnRyYWwiPnNjaGVtYS1uYW1lPC90ZXh0Pgo8cG9seWdvbiBwb2ludHM9IjMzNy44MTksMTIzLjEyIDMyNi4yOTksMTI3LjQ0IDMyNi4yOTksMTE4LjgiIHN0eWxlPSJmaWxsOnJnYigwLDAsMCkiPjwvcG9seWdvbj4KPHBhdGggZD0iTTMxNC43NzksMTIzLjEyTDMzMi4wNTksMTIzLjEyIiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHBhdGggZD0iTTM1Mi45MzksMTM4LjI0QTE1LjEyIDE1LjEyIDAgMCAwIDM2OC4wNTkgMTIzLjEyQTE1LjEyIDE1LjEyIDAgMCAwIDM1Mi45MzkgMTA4QTE1LjEyIDE1LjEyIDAgMCAwIDMzNy44MTkgMTIzLjEyQTE1LjEyIDE1LjEyIDAgMCAwIDM1Mi45MzkgMTM4LjI0WiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+Cjx0ZXh0IHg9IjM1Mi45MzkiIHk9IjEyMy4xMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9InJnYigwLDAsMCkiIGRvbWluYW50LWJhc2VsaW5lPSJjZW50cmFsIj4uPC90ZXh0Pgo8cG9seWdvbiBwb2ludHM9IjM5MS4wOTksMTIzLjEyIDM3OS41NzksMTI3LjQ0IDM3OS41NzksMTE4LjgiIHN0eWxlPSJmaWxsOnJnYigwLDAsMCkiPjwvcG9seWdvbj4KPHBhdGggZD0iTTM2OC4wNTksMTIzLjEyTDM4NS4zMzksMTIzLjEyIiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHBhdGggZD0iTTQwNi4yMTksMTM4LjI0TDU1Ni4wMzcsMTM4LjI0QTE1LjEyIDE1LjEyIDAgMCAwIDU3MS4xNTcgMTIzLjEyQTE1LjEyIDE1LjEyIDAgMCAwIDU1Ni4wMzcgMTA4TDQwNi4yMTksMTA4QTE1LjEyIDE1LjEyIDAgMCAwIDM5MS4wOTkgMTIzLjEyQTE1LjEyIDE1LjEyIDAgMCAwIDQwNi4yMTkgMTM4LjI0WiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+Cjx0ZXh0IHg9IjQ4MS4xMjgiIHk9IjEyMy4xMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0icmdiKDAsMCwwKSIgZG9taW5hbnQtYmFzZWxpbmU9ImNlbnRyYWwiPnRhYmxlLW9yLWluZGV4LW5hbWU8L3RleHQ+Cjxwb2x5Z29uIHBvaW50cz0iNTk0LjE5NywxMjMuMTIgNTgyLjY3NywxMjcuNDQgNTgyLjY3NywxMTguOCIgc3R5bGU9ImZpbGw6cmdiKDAsMCwwKSI+PC9wb2x5Z29uPgo8cGF0aCBkPSJNNTcxLjE1NywxMjMuMTJMNTg4LjQzNywxMjMuMTIiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cG9seWdvbiBwb2ludHM9IjY0NS4xOTcsMTcuMjggNjMzLjY3NywyMS42IDYzMy42NzcsMTIuOTYiIHN0eWxlPSJmaWxsOnJnYigwLDAsMCkiPjwvcG9seWdvbj4KPHBhdGggZD0iTTU5NC4xOTcsMTIzLjEyIEwgNjAxLjY5NywxMjMuMTIgUSA2MDkuMTk3LDEyMy4xMiA2MDkuMTk3LDEwOC4xMiBMIDYwOS4xOTcsMzIuMjggUSA2MDkuMTk3LDE3LjI4IDYyNC4xOTcsMTcuMjggTCA2MjQuNDM3LDE3LjI4IEwgNjM5LjQzNywxNy4yOCIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+CjxjaXJjbGUgY3g9IjY0OC43OTciIGN5PSIxNy4yOCIgcj0iMy42IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyI+PC9jaXJjbGU+Cjxwb2x5Z29uIHBvaW50cz0iMzk3LjY2NiwxNy4yOCAzODYuMTQ2LDIxLjYgMzg2LjE0NiwxMi45NiIgc3R5bGU9ImZpbGw6cmdiKDAsMCwwKSI+PC9wb2x5Z29uPgo8cGF0aCBkPSJNMTUwLjEzNCwxNy4yOEwzOTEuOTA2LDE3LjI4IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHBhdGggZD0iTTM5Ny42NjYsMTcuMjhMNjMzLjY3NywxNy4yOCIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+Cjxwb2x5Z29uIHBvaW50cz0iMTg4LjE3NCw0Ny41MiAxNzYuNjU0LDUxLjg0IDE3Ni42NTQsNDMuMiIgc3R5bGU9ImZpbGw6cmdiKDAsMCwwKSI+PC9wb2x5Z29uPgo8cGF0aCBkPSJNMTUwLjEzNCwxNy4yOCBMIDE1Ny42MzQsMTcuMjggUSAxNjUuMTM0LDE3LjI4IDE2NS4xMzQsMzIuMjggTCAxNjUuMTM0LDMyLjUyIFEgMTY1LjEzNCw0Ny41MiAxNzMuNzc0LDQ3LjUyIEwgMTgyLjQxNCw0Ny41MiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+CjxwYXRoIGQ9Ik0yMDMuMjk0LDYyLjY0TDI5OS42NTksNjIuNjRBMTUuMTIgMTUuMTIgMCAwIDAgMzE0Ljc3OSA0Ny41MkwzMTQuNzc5LDQ3LjUyQTE1LjEyIDE1LjEyIDAgMCAwIDI5OS42NTkgMzIuNEwyMDMuMjk0LDMyLjRBMTUuMTIgMTUuMTIgMCAwIDAgMTg4LjE3NCA0Ny41MkwxODguMTc0LDQ3LjUyQTE1LjEyIDE1LjEyIDAgMCAwIDIwMy4yOTQgNjIuNjRaIiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHRleHQgeD0iMjUxLjQ3NyIgeT0iNDcuNTIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9InJnYigwLDAsMCkiIGRvbWluYW50LWJhc2VsaW5lPSJjZW50cmFsIj5zY2hlbWEtbmFtZTwvdGV4dD4KPHBvbHlnb24gcG9pbnRzPSI1OTQuMTk3LDQ3LjUyIDU4Mi42NzcsNTEuODQgNTgyLjY3Nyw0My4yIiBzdHlsZT0iZmlsbDpyZ2IoMCwwLDApIj48L3BvbHlnb24+CjxwYXRoIGQ9Ik0zMTQuNzc5LDQ3LjUyTDU4OC40MzcsNDcuNTIiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8cGF0aCBkPSJNNTk0LjE5Nyw0Ny41MiBMIDYwMS42OTcsNDcuNTIgUSA2MDkuMTk3LDQ3LjUyIDYwOS4xOTcsNDAuMDIgTCA2MDkuMTk3LDMyLjUyIiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoyLjE2O3N0cm9rZTpyZ2IoMCwwLDApOyIgLz4KPHBvbHlnb24gcG9pbnRzPSIxODguMTc0LDg1LjMyIDE3Ni42NTQsODkuNjQgMTc2LjY1NCw4MSIgc3R5bGU9ImZpbGw6cmdiKDAsMCwwKSI+PC9wb2x5Z29uPgo8cGF0aCBkPSJNMTUwLjEzNCwxNy4yOCBMIDE1Ny42MzQsMTcuMjggUSAxNjUuMTM0LDE3LjI4IDE2NS4xMzQsMzIuMjggTCAxNjUuMTM0LDcwLjMyIFEgMTY1LjEzNCw4NS4zMiAxNzMuNzc0LDg1LjMyIEwgMTgyLjQxNCw4NS4zMiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+CjxwYXRoIGQ9Ik0yMDMuMjk0LDEwMC40NEwzNTMuMTEyLDEwMC40NEExNS4xMiAxNS4xMiAwIDAgMCAzNjguMjMyIDg1LjMyQTE1LjEyIDE1LjEyIDAgMCAwIDM1My4xMTIgNzAuMkwyMDMuMjk0LDcwLjJBMTUuMTIgMTUuMTIgMCAwIDAgMTg4LjE3NCA4NS4zMkExNS4xMiAxNS4xMiAwIDAgMCAyMDMuMjk0IDEwMC40NFoiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8dGV4dCB4PSIyNzguMjAzIiB5PSI4NS4zMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0icmdiKDAsMCwwKSIgZG9taW5hbnQtYmFzZWxpbmU9ImNlbnRyYWwiPmluZGV4LW9yLXRhYmxlLW5hbWU8L3RleHQ+Cjxwb2x5Z29uIHBvaW50cz0iNTk0LjE5Nyw4NS4zMiA1ODIuNjc3LDg5LjY0IDU4Mi42NzcsODEiIHN0eWxlPSJmaWxsOnJnYigwLDAsMCkiPjwvcG9seWdvbj4KPHBhdGggZD0iTTM2OC4yMzIsODUuMzJMNTg4LjQzNyw4NS4zMiIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6Mi4xNjtzdHJva2U6cmdiKDAsMCwwKTsiIC8+CjxwYXRoIGQ9Ik01OTQuMTk3LDg1LjMyIEwgNjAxLjY5Nyw4NS4zMiBRIDYwOS4xOTcsODUuMzIgNjA5LjE5Nyw3Ny44MiBMIDYwOS4xOTcsNzAuMzIiIHN0eWxlPSJmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjIuMTY7c3Ryb2tlOnJnYigwLDAsMCk7IiAvPgo8L3N2Zz4=" class="pikchr" />

The ANALYZE command gathers statistics about tables and indices and stores the collected information in [internal tables](fileformat2.md#intschema) of the database where the query optimizer can access the information and use it to help make better query planning choices. If no arguments are given, the main database and all attached databases are analyzed. If a schema name is given as the argument, then all tables and indices in that one database are analyzed. If the argument is a table name, then only that table and the indices associated with that table are analyzed. If the argument is an index name, then only that one index is analyzed.

<span id="req"></span>

# 2. Recommended usage patterns

The use of ANALYZE is never required. However, if an application makes complex queries that have many possible query plans, the query planner will be better able to pick the best plan if ANALYZE has been run. This can result in significant performance improvements for some queries.

Two recommended approaches for when and how to run ANALYZE are described in the next subsections, in order of preference. <span id="pragopt"></span>

## 2.1. Periodically run "PRAGMA optimize"

The [PRAGMA optimize](pragma.md#pragma_optimize) command will automatically run ANALYZE when needed. Suggested use:

1.  Applications with short-lived database connections should run "PRAGMA optimize;" once, just prior to closing each database connection.

2.  Applications that use long-lived database connections should run "PRAGMA optimize=0x10002;" when the connection is first opened, and then also run "PRAGMA optimize;" periodically, perhaps once per day, or more if the database is evolving rapidly.

3.  All applications should run "PRAGMA optimize;" after a schema change, especially after one or more [CREATE INDEX](lang_createindex.md) statements.

The [PRAGMA optimize](pragma.md#pragma_optimize) command is usually a no-op but it will occasionally run one or more ANALYZE subcommands on individual tables of the database if doing so will be useful to the query planner. Since SQLite version 3.46.0 (2024-05-23), the "PRAGMA optimize" command automatically limits the scope of ANALYZE subcommands so that the overall "PRAGMA optimize" command completes quickly even on enormous databases. There is no need to use [PRAGMA analysis_limit](pragma.md#pragma_analysis_limit). This is the recommended way of running ANALYZE moving forward.

The [PRAGMA optimize](pragma.md#pragma_optimize) command will normally only consider running ANALYZE on tables that have been previously queried by the same database connection or that do not have entries in the [sqlite_stat1](fileformat2.md#stat1tab) table. However, if the 0x10000 bit is added to the argument, PRAGMA optimize will examine all tables to see if they can benefit from ANALYZE, not just those that have been recently queried. There is no query history when a database connection first opens, and that is why adding the 0x10000 bit is recommended when running PRAGMA optimize on a fresh database connection.

See the [Automatically Running ANALYZE](lang_analyze.md#autoanalyze) and [Approximate ANALYZE For Large Databases](lang_analyze.md#approx) sections below for additional information. <span id="statanal"></span>

## 2.2. Fixed results of ANALYZE

Running ANALYZE can cause SQLite to choose different query plans for subsequent queries. This is almost always a positive thing, as the query plans chosen after ANALYZE will in nearly every case be better than the query plans picked before ANALYZE. That is the whole point of ANALYZE. But there can be no proof of running ANALYZE will always be beneficial. One can construct pathological cases where running ANALYZE could make some subsequent queries run slower.

Some developers prefer that once the design of an application is frozen, SQLite will always pick the same query plans as it did during development and testing. Then if millions of copies of the application are shipped to customers, the developers are assured that all of those millions of copies are running the same query plans regardless of what data the individual customers insert into their particular databases. This can help in reproducing complaints of performance problems coming back from the field.

To achieve this objection, never run a full ANALYZE nor the "PRAGMA optimize" command in the application. Rather, only run ANALYZE during development, manually using the [command-line interface](cli.md) or similar, on a test database that is similar in size and content to live databases. Then capture the result of this one-time ANALYZE using a script like the following:

.mode list\
SELECT \
  'ANALYZE sqlite_schema;' \|\|\
  'DELETE FROM sqlite_stat1;' \|\|\
  'INSERT INTO sqlite_stat1(tbl,idx,stat)VALUES' \|\|\
  (SELECT group_concat(format('(%Q,%Q,%Q)',tbl,idx,stat),',')\
    FROM sqlite_stat1) \|\|\
  ';ANALYZE sqlite_schema;';\

When creating a new instance of the database in deployed instances of the application, or perhaps every time the application is started up in the case of long-running applications, run the commands generated by script above. This will populate the [sqlite_stat1](fileformat2.md#stat1tab) table exactly as it was during development and testing and ensure that the query plans selected in the field are same as those selected during testing in the lab. Maybe copy/paste the string generated by the script above into a static string constant named "zStat1Init" and then invoke:

sqlite3_exec(db, zStat1Init, 0, 0, 0);\

Perhaps also add "BEGIN;" at the start of the string constant and "COMMIT;" at the end, depending on the context in which the script is run.

See the [query planner stability guarantee](queryplanner-ng.md#qpstab) for addition information.

# 3. Details

The default implementation stores all statistics in a single table named "[sqlite_stat1](fileformat2.md#stat1tab)". If SQLite is compiled with the [SQLITE_ENABLE_STAT4](compile.md#enable_stat4) option, then additional histogram data is collected and stored in [sqlite_stat4](fileformat2.md#stat4tab). Older versions of SQLite would make use of the [sqlite_stat2](fileformat2.md#stat2tab) table or [sqlite_stat3](fileformat2.md#stat3tab) table when compiled with [SQLITE_ENABLE_STAT2](compile.md#enable_stat2) or [SQLITE_ENABLE_STAT3](compile.md#enable_stat3), but all recent versions of SQLite ignore the sqlite_stat2 and sqlite_stat3 tables. Future enhancements may create additional [internal tables](fileformat2.md#intschema) with the same name pattern except with final digit larger than "4". All of these tables are collectively referred to as "statistics tables".

The content of the statistics tables can be queried using [SELECT](lang_select.md) and can be changed using the [DELETE](lang_delete.md), [INSERT](lang_insert.md), and [UPDATE](lang_update.md) commands. The [DROP TABLE](lang_droptable.md) command works on statistics tables as of SQLite version 3.7.9. (2011-11-01) The [ALTER TABLE](lang_altertable.md) command does not work on statistics tables. Appropriate care should be used when changing the content of the statistics tables as invalid content can cause SQLite to select inefficient query plans. Generally speaking, one should not modify the content of the statistics tables by any mechanism other than invoking the ANALYZE command. See "[Manual Control Of Query Plans Using SQLITE_STAT Tables](optoverview.md#manctrl)" for further information.

Statistics gathered by ANALYZE are <u>not</u> updated as the content of the database changes. If the content of the database changes significantly, or if the database schema changes, then one should consider rerunning the ANALYZE command in order to update the statistics.

The query planner loads the content of the statistics tables into memory when the schema is read. Hence, when an application changes the statistics tables directly, SQLite will not immediately notice the changes. An application can force the query planner to reread the statistics tables by running **ANALYZE sqlite_schema**.

<span id="autoanalyze"></span>

# 4. Automatically Running ANALYZE

The [PRAGMA optimize](pragma.md#pragma_optimize) command will automatically run ANALYZE on individual tables on an as-needed basis. The recommended practice is for applications to invoke the [PRAGMA optimize](pragma.md#pragma_optimize) statement just before closing each database connection. Or, if the application keeps a single database connection open for a long time, then it should run "PRAGMA optimize=0x10002" when the connection is first opened and run "PRAGMA optimize;" periodically thereafter, perhaps once per day or even once per hour.

Each SQLite [database connection](c3ref/sqlite3.md) records cases when the query planner would benefit from having accurate results of ANALYZE at hand. These records are held in memory and accumulate over the life of a database connection. The [PRAGMA optimize](pragma.md#pragma_optimize) command looks at those records and runs ANALYZE on only those tables for which new or updated ANALYZE data seems likely to be useful. In most cases [PRAGMA optimize](pragma.md#pragma_optimize) will not run ANALYZE, but it will occasionally do so either for tables that have never before been analyzed, or for tables that have grown significantly since they were last analyzed.

Since the actions of [PRAGMA optimize](pragma.md#pragma_optimize) are determined to some extent by prior queries that have been evaluated on the same database connection, it is recommended that [PRAGMA optimize](pragma.md#pragma_optimize) be deferred until the database connection is closing and has thus had an opportunity to accumulate as much usage information as possible. It is also reasonable to set a timer to run [PRAGMA optimize](pragma.md#pragma_optimize) every few hours, or every few days, for database connections that stay open for a long time. When running [PRAGMA optimize](pragma.md#pragma_optimize) immediately after a database connection is opened, one can add the 0x10000 bit to the bitmask argument (thus making the command read "PRAGMA optimize=0x10002") which causes all tables to be examined, even tables that have not been queried during the current connection.

The [PRAGMA optimize](pragma.md#pragma_optimize) command was first introduced with SQLite 3.18.0 (2017-03-28) and is a no-op for all prior releases of SQLite. The [PRAGMA optimize](pragma.md#pragma_optimize) command was significantly enhanced in SQLite 3.46.0 (2024-05-23) and the advice given in this documentation is based on those enhancements. Applications that use earlier versions of SQLite should consult the corresponding documentation for better advice on the best ways to use PRAGMA optimize.

<span id="approx"></span>

# 5. Approximate ANALYZE For Large Databases

By default, ANALYZE does a full scan of every index. This can be slow for large databases. So beginning with SQLite version 3.32.0 (2020-05-22), the [PRAGMA analysis_limit](pragma.md#pragma_analysis_limit) command can be used to limit the amount of scanning performed by ANALYZE, and thus help ANALYZE to run faster, even on very large database files. We call this running an "approximate ANALYZE".

The recommended usage pattern for the [analysis_limit](pragma.md#pragma_analysis_limit) pragma is like this:

PRAGMA analysis_limit=1000;\

This pragma tells the ANALYZE command to start a full scan of the index as it normally would. But when the number of rows visited reaches 1000 (or whatever other limit is specified by the pragma), the ANALYZE command will begin taking actions to stop the scan. If the left-most column of the index has changed at least once during the previous 1000 steps, then the analysis stops immediately. But if the left-most column has always been the same, then ANALYZE skips ahead to the first entry with a different left-most column and reads an additional 1000 rows before terminating.

The details of the effects of the analysis limit described in the previous paragraph are subject to change in future versions of SQLite. But the core idea will remain the same. An analysis limit of N will strive to limit the number of rows visited in each index to approximately N.

Values of N between 100 and 1000 are recommended. Or, to disable the analysis limit, causing ANALYZE to do a complete scan of each index, set the analysis limit to 0. The default value for the analysis limit is 0 for backwards compatibility.

The values placed in the sqlite_stat1 table by an approximate ANALYZE are not exactly the same as what would be computed by an unrestricted analysis. But they are usually close enough. The index statistics in the sqlite_stat1 table are approximations in any case, so the fact that the results of an approximate ANALYZE are slightly different from a traditional full scan ANALYZE has little practical impact. It is possible to construct a pathological case where an approximate ANALYZE is noticeably inferior to a full-scan ANALYZE, but such cases are rare in real-world problems.

A good rule of thumb seems to be to always set "PRAGMA analysis_limit=N" for N between 100 and 1000 prior to running either "ANALYZE". It used to be that this was also recommended prior to running "[PRAGMA optimize](pragma.md#pragma_optimize)", but since version 3.46.0 (2024-05-23) that happens automatically. The results are not quite as precise when using PRAGMA analysis_limit, but they are precise enough, and the fact that the results are computed so much faster means that developers are more likely to compute them. An approximate ANALYZE is better than not running ANALYZE at all.

## 5.1. Limitations of approximate ANALYZE

The content in the sqlite_stat4 table cannot be computed with anything less than a full scan. Hence, if a non-zero analysis limit is specified, the sqlite_stat4 table is not computed.
