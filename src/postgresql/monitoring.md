---
title: Monitoring Database Activity
source_url: https://www.postgresql.org/docs/17/monitoring.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: monitoring.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 910
---

## Monitoring Database Activity

monitoring

database activity

database activity

monitoring

A database administrator frequently wonders, “What is the system doing right now?” This chapter discusses how to find that out.

Several tools are available for monitoring database activity and analyzing performance. Most of this chapter is devoted to describing PostgreSQL's cumulative statistics system, but one should not neglect regular Unix monitoring programs such as `ps`, `top`, `iostat`, and `vmstat`. Also, once one has identified a poorly-performing query, further investigation might be needed using PostgreSQL's [`EXPLAIN`](#sql-explain) command. [???](#using-explain) discusses `EXPLAIN` and other methods for understanding the behavior of an individual query.

## Standard Unix Tools

ps

to monitor activity

On most Unix platforms, PostgreSQL modifies its command title as reported by `ps`, so that individual server processes can readily be identified. A sample display is

    $ ps auxww | grep ^postgres
    postgres  15551  0.0  0.1  57536  7132 pts/0    S    18:02   0:00 postgres -i
    postgres  15554  0.0  0.0  57536  1184 ?        Ss   18:02   0:00 postgres: background writer
    postgres  15555  0.0  0.0  57536   916 ?        Ss   18:02   0:00 postgres: checkpointer
    postgres  15556  0.0  0.0  57536   916 ?        Ss   18:02   0:00 postgres: walwriter
    postgres  15557  0.0  0.0  58504  2244 ?        Ss   18:02   0:00 postgres: autovacuum launcher
    postgres  15582  0.0  0.0  58772  3080 ?        Ss   18:04   0:00 postgres: joe runbug 127.0.0.1 idle
    postgres  15606  0.0  0.0  58772  3052 ?        Ss   18:07   0:00 postgres: tgl regression [local] SELECT waiting
    postgres  15610  0.0  0.0  58772  3056 ?        Ss   18:07   0:00 postgres: tgl regression [local] idle in transaction

(The appropriate invocation of `ps` varies across different platforms, as do the details of what is shown. This example is from a recent Linux system.) The first process listed here is the primary server process. The command arguments shown for it are the same ones used when it was launched. The next four processes are background worker processes automatically launched by the primary process. (The “autovacuum launcher” process will not be present if you have set the system not to run autovacuum.) Each of the remaining processes is a server process handling one client connection. Each such process sets its command line display in the form

    postgres: user database host activity

The user, database, and (client) host items remain the same for the life of the client connection, but the activity indicator changes. The activity can be `idle` (i.e., waiting for a client command), `idle in transaction` (waiting for client inside a `BEGIN` block), or a command type name such as `SELECT`. Also, `waiting` is appended if the server process is presently waiting on a lock held by another session. In the above example we can infer that process 15606 is waiting for process 15610 to complete its transaction and thereby release some lock. (Process 15610 must be the blocker, because there is no other active session. In more complicated cases it would be necessary to look into the [pg_locks](#view-pg-locks) system view to determine who is blocking whom.)

If [???](#guc-cluster-name) has been configured the cluster name will also be shown in `ps` output:

    $ psql -c 'SHOW cluster_name'
     cluster_name
    --------------
     server1
    (1 row)

    $ ps aux|grep server1
    postgres   27093  0.0  0.0  30096  2752 ?        Ss   11:34   0:00 postgres: server1: background writer
    ...

If you have turned off [???](#guc-update-process-title) then the activity indicator is not updated; the process title is set only once when a new process is launched. On some platforms this saves a measurable amount of per-command overhead; on others it's insignificant.

> [!TIP]
> Solaris requires special handling. You must use `/usr/ucb/ps`, rather than `/bin/ps`. You also must use two `w` flags, not just one. In addition, your original invocation of the `postgres` command must have a shorter `ps` status display than that provided by each server process. If you fail to do all three things, the `ps` output for each server process will be the original `postgres` command line.

## The Cumulative Statistics System

statistics

PostgreSQL's cumulative statistics system supports collection and reporting of information about server activity. Presently, accesses to tables and indexes in both disk-block and individual-row terms are counted. The total number of rows in each table, and information about vacuum and analyze actions for each table are also counted. If enabled, calls to user-defined functions and the total time spent in each one are counted as well.

PostgreSQL also supports reporting dynamic information about exactly what is going on in the system right now, such as the exact command currently being executed by other server processes, and which other connections exist in the system. This facility is independent of the cumulative statistics system.

### Statistics Collection Configuration

Since collection of statistics adds some overhead to query execution, the system can be configured to collect or not collect information. This is controlled by configuration parameters that are normally set in `postgresql.conf`. (See [???](#runtime-config) for details about setting configuration parameters.)

The parameter [???](#guc-track-activities) enables monitoring of the current command being executed by any server process.

The parameter [???](#guc-track-counts) controls whether cumulative statistics are collected about table and index accesses.

The parameter [???](#guc-track-functions) enables tracking of usage of user-defined functions.

The parameter [???](#guc-track-io-timing) enables monitoring of block read, write, extend, and fsync times.

The parameter [???](#guc-track-wal-io-timing) enables monitoring of WAL write and fsync times.

Normally these parameters are set in `postgresql.conf` so that they apply to all server processes, but it is possible to turn them on or off in individual sessions using the [???](#sql-set) command. (To prevent ordinary users from hiding their activity from the administrator, only superusers are allowed to change these parameters with `SET`.)

Cumulative statistics are collected in shared memory. Every PostgreSQL process collects statistics locally, then updates the shared data at appropriate intervals. When a server, including a physical replica, shuts down cleanly, a permanent copy of the statistics data is stored in the `pg_stat` subdirectory, so that statistics can be retained across server restarts. In contrast, when starting from an unclean shutdown (e.g., after an immediate shutdown, a server crash, starting from a base backup, and point-in-time recovery), all statistics counters are reset.

### Viewing Statistics

Several predefined views, listed in [Dynamic Statistics Views](#monitoring-stats-dynamic-views-table), are available to show the current state of the system. There are also several other views, listed in [Collected Statistics Views](#monitoring-stats-views-table), available to show the accumulated statistics. Alternatively, one can build custom views using the underlying cumulative statistics functions, as discussed in [Statistics Functions](#monitoring-stats-functions).

When using the cumulative statistics views and functions to monitor collected data, it is important to realize that the information does not update instantaneously. Each individual server process flushes out accumulated statistics to shared memory just before going idle, but not more frequently than once per `PGSTAT_MIN_INTERVAL` milliseconds (1 second unless altered while building the server); so a query or transaction still in progress does not affect the displayed totals and the displayed information lags behind actual activity. However, current-query information collected by `track_activities` is always up-to-date.

Another important point is that when a server process is asked to display any of the accumulated statistics, accessed values are cached until the end of its current transaction in the default configuration. So the statistics will show static information as long as you continue the current transaction. Similarly, information about the current queries of all sessions is collected when any such information is first requested within a transaction, and the same information will be displayed throughout the transaction. This is a feature, not a bug, because it allows you to perform several queries on the statistics and correlate the results without worrying that the numbers are changing underneath you. When analyzing statistics interactively, or with expensive queries, the time delta between accesses to individual statistics can lead to significant skew in the cached statistics. To minimize skew, `stats_fetch_consistency` can be set to `snapshot`, at the price of increased memory usage for caching not-needed statistics data. Conversely, if it's known that statistics are only accessed once, caching accessed statistics is unnecessary and can be avoided by setting `stats_fetch_consistency` to `none`. You can invoke `pg_stat_clear_snapshot()` to discard the current transaction's statistics snapshot or cached values (if any). The next use of statistical information will (when in snapshot mode) cause a new snapshot to be built or (when in cache mode) accessed statistics to be cached.

A transaction can also see its own statistics (not yet flushed out to the shared memory statistics) in the views pg_stat_xact_all_tables, pg_stat_xact_sys_tables, pg_stat_xact_user_tables, and pg_stat_xact_user_functions. These numbers do not act as stated above; instead they update continuously throughout the transaction.

Some of the information in the dynamic statistics views shown in [Dynamic Statistics Views](#monitoring-stats-dynamic-views-table) is security restricted. Ordinary users can only see all the information about their own sessions (sessions belonging to a role that they are a member of). In rows about other sessions, many columns will be null. Note, however, that the existence of a session and its general properties such as its sessions user and database are visible to all users. Superusers and roles with privileges of built-in role `pg_read_all_stats` (see also [???](#predefined-roles)) can see all the information about all sessions.

| View Name | Description |
|----|----|
| pg_stat_activity <span class="indexterm"></span> | One row per server process, showing information related to the current activity of that process, such as state and current query. See [ pg_stat_activity](#monitoring-pg-stat-activity-view) for details. |
| pg_stat_replication<span class="indexterm"></span> | One row per WAL sender process, showing statistics about replication to that sender's connected standby server. See [ pg_stat_replication](#monitoring-pg-stat-replication-view) for details. |
| pg_stat_wal_receiver<span class="indexterm"></span> | Only one row, showing statistics about the WAL receiver from that receiver's connected server. See [ pg_stat_wal_receiver](#monitoring-pg-stat-wal-receiver-view) for details. |
| pg_stat_recovery_prefetch<span class="indexterm"></span> | Only one row, showing statistics about blocks prefetched during recovery. See [ pg_stat_recovery_prefetch](#monitoring-pg-stat-recovery-prefetch) for details. |
| pg_stat_subscription<span class="indexterm"></span> | At least one row per subscription, showing information about the subscription workers. See [ pg_stat_subscription](#monitoring-pg-stat-subscription) for details. |
| pg_stat_ssl<span class="indexterm"></span> | One row per connection (regular and replication), showing information about SSL used on this connection. See [ pg_stat_ssl](#monitoring-pg-stat-ssl-view) for details. |
| pg_stat_gssapi<span class="indexterm"></span> | One row per connection (regular and replication), showing information about GSSAPI authentication and encryption used on this connection. See [ pg_stat_gssapi](#monitoring-pg-stat-gssapi-view) for details. |
| pg_stat_progress_analyze<span class="indexterm"></span> | One row for each backend (including autovacuum worker processes) running `ANALYZE`, showing current progress. See [ANALYZE Progress Reporting](#analyze-progress-reporting). |
| pg_stat_progress_create_index<span class="indexterm"></span> | One row for each backend running `CREATE INDEX` or `REINDEX`, showing current progress. See [CREATE INDEX Progress Reporting](#create-index-progress-reporting). |
| pg_stat_progress_vacuum<span class="indexterm"></span> | One row for each backend (including autovacuum worker processes) running `VACUUM`, showing current progress. See [VACUUM Progress Reporting](#vacuum-progress-reporting). |
| pg_stat_progress_cluster<span class="indexterm"></span> | One row for each backend running `CLUSTER` or `VACUUM FULL`, showing current progress. See [CLUSTER Progress Reporting](#cluster-progress-reporting). |
| pg_stat_progress_basebackup<span class="indexterm"></span> | One row for each WAL sender process streaming a base backup, showing current progress. See [Base Backup Progress Reporting](#basebackup-progress-reporting). |
| pg_stat_progress_copy<span class="indexterm"></span> | One row for each backend running `COPY`, showing current progress. See [COPY Progress Reporting](#copy-progress-reporting). |

Dynamic Statistics Views {#monitoring-stats-dynamic-views-table}

| View Name | Description |
|----|----|
| pg_stat_archiver<span class="indexterm"></span> | One row only, showing statistics about the WAL archiver process's activity. See [ pg_stat_archiver](#monitoring-pg-stat-archiver-view) for details. |
| pg_stat_bgwriter<span class="indexterm"></span> | One row only, showing statistics about the background writer process's activity. See [ pg_stat_bgwriter](#monitoring-pg-stat-bgwriter-view) for details. |
| pg_stat_checkpointer<span class="indexterm"></span> | One row only, showing statistics about the checkpointer process's activity. See [ pg_stat_checkpointer](#monitoring-pg-stat-checkpointer-view) for details. |
| pg_stat_database<span class="indexterm"></span> | One row per database, showing database-wide statistics. See [ pg_stat_database](#monitoring-pg-stat-database-view) for details. |
| pg_stat_database_conflicts<span class="indexterm"></span> | One row per database, showing database-wide statistics about query cancels due to conflict with recovery on standby servers. See [ pg_stat_database_conflicts](#monitoring-pg-stat-database-conflicts-view) for details. |
| pg_stat_io<span class="indexterm"></span> | One row for each combination of backend type, context, and target object containing cluster-wide I/O statistics. See [ pg_stat_io](#monitoring-pg-stat-io-view) for details. |
| pg_stat_replication_slots<span class="indexterm"></span> | One row per replication slot, showing statistics about the replication slot's usage. See [ pg_stat_replication_slots](#monitoring-pg-stat-replication-slots-view) for details. |
| pg_stat_slru<span class="indexterm"></span> | One row per SLRU, showing statistics of operations. See [ pg_stat_slru](#monitoring-pg-stat-slru-view) for details. |
| pg_stat_subscription_stats<span class="indexterm"></span> | One row per subscription, showing statistics about errors. See [ pg_stat_subscription_stats](#monitoring-pg-stat-subscription-stats) for details. |
| pg_stat_wal<span class="indexterm"></span> | One row only, showing statistics about WAL activity. See [ pg_stat_wal](#monitoring-pg-stat-wal-view) for details. |
| pg_stat_all_tables<span class="indexterm"></span> | One row for each table in the current database, showing statistics about accesses to that specific table. See [ pg_stat_all_tables](#monitoring-pg-stat-all-tables-view) for details. |
| pg_stat_sys_tables<span class="indexterm"></span> | Same as pg_stat_all_tables, except that only system tables are shown. |
| pg_stat_user_tables<span class="indexterm"></span> | Same as pg_stat_all_tables, except that only user tables are shown. |
| pg_stat_xact_all_tables<span class="indexterm"></span> | Similar to pg_stat_all_tables, but counts actions taken so far within the current transaction (which are *not* yet included in pg_stat_all_tables and related views). The columns for numbers of live and dead rows and vacuum and analyze actions are not present in this view. |
| pg_stat_xact_sys_tables<span class="indexterm"></span> | Same as pg_stat_xact_all_tables, except that only system tables are shown. |
| pg_stat_xact_user_tables<span class="indexterm"></span> | Same as pg_stat_xact_all_tables, except that only user tables are shown. |
| pg_stat_all_indexes<span class="indexterm"></span> | One row for each index in the current database, showing statistics about accesses to that specific index. See [ pg_stat_all_indexes](#monitoring-pg-stat-all-indexes-view) for details. |
| pg_stat_sys_indexes<span class="indexterm"></span> | Same as pg_stat_all_indexes, except that only indexes on system tables are shown. |
| pg_stat_user_indexes<span class="indexterm"></span> | Same as pg_stat_all_indexes, except that only indexes on user tables are shown. |
| pg_stat_user_functions<span class="indexterm"></span> | One row for each tracked function, showing statistics about executions of that function. See [ pg_stat_user_functions](#monitoring-pg-stat-user-functions-view) for details. |
| pg_stat_xact_user_functions<span class="indexterm"></span> | Similar to pg_stat_user_functions, but counts only calls during the current transaction (which are *not* yet included in pg_stat_user_functions). |
| pg_statio_all_tables<span class="indexterm"></span> | One row for each table in the current database, showing statistics about I/O on that specific table. See [ pg_statio_all_tables](#monitoring-pg-statio-all-tables-view) for details. |
| pg_statio_sys_tables<span class="indexterm"></span> | Same as pg_statio_all_tables, except that only system tables are shown. |
| pg_statio_user_tables<span class="indexterm"></span> | Same as pg_statio_all_tables, except that only user tables are shown. |
| pg_statio_all_indexes<span class="indexterm"></span> | One row for each index in the current database, showing statistics about I/O on that specific index. See [ pg_statio_all_indexes](#monitoring-pg-statio-all-indexes-view) for details. |
| pg_statio_sys_indexes<span class="indexterm"></span> | Same as pg_statio_all_indexes, except that only indexes on system tables are shown. |
| pg_statio_user_indexes<span class="indexterm"></span> | Same as pg_statio_all_indexes, except that only indexes on user tables are shown. |
| pg_statio_all_sequences<span class="indexterm"></span> | One row for each sequence in the current database, showing statistics about I/O on that specific sequence. See [ pg_statio_all_sequences](#monitoring-pg-statio-all-sequences-view) for details. |
| pg_statio_sys_sequences<span class="indexterm"></span> | Same as pg_statio_all_sequences, except that only system sequences are shown. (Presently, no system sequences are defined, so this view is always empty.) |
| pg_statio_user_sequences<span class="indexterm"></span> | Same as pg_statio_all_sequences, except that only user sequences are shown. |

Collected Statistics Views {#monitoring-stats-views-table}

The per-index statistics are particularly useful to determine which indexes are being used and how effective they are.

The pg_stat_io and pg_statio\_ set of views are useful for determining the effectiveness of the buffer cache. They can be used to calculate a cache hit ratio. Note that while PostgreSQL's I/O statistics capture most instances in which the kernel was invoked in order to perform I/O, they do not differentiate between data which had to be fetched from disk and that which already resided in the kernel page cache. Users are advised to use the PostgreSQL statistics views in combination with operating system utilities for a more complete picture of their database's I/O performance.

### pg_stat_activity

pg_stat_activity

The pg_stat_activity view will have one row per server process, showing information related to the current activity of that process.

<table id="pg-stat-activity-view">
<caption>pg_stat_activity View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">datid <code>oid</code></p>
<p>OID of the database this backend is connected to</p></td>
</tr>
<tr>
<td><p role="column_definition">datname <code>name</code></p>
<p>Name of the database this backend is connected to</p></td>
</tr>
<tr>
<td><p role="column_definition">pid <code>integer</code></p>
<p>Process ID of this backend</p></td>
</tr>
<tr>
<td><p role="column_definition">leader_pid <code>integer</code></p>
<p>Process ID of the parallel group leader if this process is a parallel query worker, or process ID of the leader apply worker if this process is a parallel apply worker. <code>NULL</code> indicates that this process is a parallel group leader or leader apply worker, or does not participate in any parallel operation.</p></td>
</tr>
<tr>
<td><p role="column_definition">usesysid <code>oid</code></p>
<p>OID of the user logged into this backend</p></td>
</tr>
<tr>
<td><p role="column_definition">usename <code>name</code></p>
<p>Name of the user logged into this backend</p></td>
</tr>
<tr>
<td><p role="column_definition">application_name <code>text</code></p>
<p>Name of the application that is connected to this backend</p></td>
</tr>
<tr>
<td><p role="column_definition">client_addr <code>inet</code></p>
<p>IP address of the client connected to this backend. If this field is null, it indicates either that the client is connected via a Unix socket on the server machine or that this is an internal process such as autovacuum.</p></td>
</tr>
<tr>
<td><p role="column_definition">client_hostname <code>text</code></p>
<p>Host name of the connected client, as reported by a reverse DNS lookup of client_addr. This field will only be non-null for IP connections, and only when <a href="#guc-log-hostname">???</a> is enabled.</p></td>
</tr>
<tr>
<td><p role="column_definition">client_port <code>integer</code></p>
<p>TCP port number that the client is using for communication with this backend, or <code>-1</code> if a Unix socket is used. If this field is null, it indicates that this is an internal server process.</p></td>
</tr>
<tr>
<td><p role="column_definition">backend_start <code>timestamp with time zone</code></p>
<p>Time when this process was started. For client backends, this is the time the client connected to the server.</p></td>
</tr>
<tr>
<td><p role="column_definition">xact_start <code>timestamp with time zone</code></p>
<p>Time when this process' current transaction was started, or null if no transaction is active. If the current query is the first of its transaction, this column is equal to the query_start column.</p></td>
</tr>
<tr>
<td><p role="column_definition">query_start <code>timestamp with time zone</code></p>
<p>Time when the currently active query was started, or if state is not <code>active</code>, when the last query was started</p></td>
</tr>
<tr>
<td><p role="column_definition">state_change <code>timestamp with time zone</code></p>
<p>Time when the state was last changed</p></td>
</tr>
<tr>
<td><p role="column_definition">wait_event_type <code>text</code></p>
<p>The type of event for which the backend is waiting, if any; otherwise NULL. See <a href="#wait-event-table">Wait Event Types</a>.</p></td>
</tr>
<tr>
<td><p role="column_definition">wait_event <code>text</code></p>
<p>Wait event name if backend is currently waiting, otherwise NULL. See <a href="#wait-event-activity-table">???</a> through <a href="#wait-event-timeout-table">???</a>.</p></td>
</tr>
<tr>
<td><p role="column_definition">state <code>text</code></p>
<p>Current overall state of this backend. Possible values are:</p>
<ul>
<li><p><code>active</code>: The backend is executing a query.</p></li>
<li><p><code>idle</code>: The backend is waiting for a new client command.</p></li>
<li><p><code>idle in transaction</code>: The backend is in a transaction, but is not currently executing a query.</p></li>
<li><p><code>idle in transaction (aborted)</code>: This state is similar to <code>idle in transaction</code>, except one of the statements in the transaction caused an error.</p></li>
<li><p><code>fastpath function call</code>: The backend is executing a fast-path function.</p></li>
<li><p><code>disabled</code>: This state is reported if <a href="#guc-track-activities">???</a> is disabled in this backend.</p></li>
</ul></td>
</tr>
<tr>
<td><p role="column_definition">backend_xid <code>xid</code></p>
<p>Top-level transaction identifier of this backend, if any; see <a href="#transaction-id">???</a>.</p></td>
</tr>
<tr>
<td><p role="column_definition">backend_xmin <code>xid</code></p>
<p>The current backend's <code>xmin</code> horizon.</p></td>
</tr>
<tr>
<td><p role="column_definition">query_id <code>bigint</code></p>
<p>Identifier of this backend's most recent query. If state is <code>active</code> this field shows the identifier of the currently executing query. In all other states, it shows the identifier of last query that was executed. Query identifiers are not computed by default so this field will be null unless <a href="#guc-compute-query-id">???</a> parameter is enabled or a third-party module that computes query identifiers is configured.</p></td>
</tr>
<tr>
<td><p role="column_definition">query <code>text</code></p>
<p>Text of this backend's most recent query. If state is <code>active</code> this field shows the currently executing query. In all other states, it shows the last query that was executed. By default the query text is truncated at 1024 bytes; this value can be changed via the parameter <a href="#guc-track-activity-query-size">???</a>.</p></td>
</tr>
<tr>
<td><p role="column_definition">backend_type <code>text</code></p>
<p>Type of current backend. Possible types are <code>autovacuum launcher</code>, <code>autovacuum worker</code>, <code>logical replication launcher</code>, <code>logical replication worker</code>, <code>parallel worker</code>, <code>background writer</code>, <code>client backend</code>, <code>checkpointer</code>, <code>archiver</code>, <code>standalone backend</code>, <code>startup</code>, <code>walreceiver</code>, <code>walsender</code>, <code>walwriter</code> and <code>walsummarizer</code>. In addition, background workers registered by extensions may have additional types.</p></td>
</tr>
</tbody>
</table>

> [!NOTE]
> The wait_event and state columns are independent. If a backend is in the `active` state, it may or may not be `waiting` on some event. If the state is `active` and wait_event is non-null, it means that a query is being executed, but is being blocked somewhere in the system.

| Wait Event Type | Description |
|----|----|
| `Activity` | The server process is idle. This event type indicates a process waiting for activity in its main processing loop. `wait_event` will identify the specific wait point; see [???](#wait-event-activity-table). |
| `BufferPin` | The server process is waiting for exclusive access to a data buffer. Buffer pin waits can be protracted if another process holds an open cursor that last read data from the buffer in question. See [???](#wait-event-bufferpin-table). |
| `Client` | The server process is waiting for activity on a socket connected to a user application. Thus, the server expects something to happen that is independent of its internal processes. `wait_event` will identify the specific wait point; see [???](#wait-event-client-table). |
| `Extension` | The server process is waiting for some condition defined by an extension module. See [???](#wait-event-extension-table). |
| `InjectionPoint` | The server process is waiting for an injection point to reach an outcome defined in a test. See [???](#xfunc-addin-injection-points) for more details. This type has no predefined wait points. |
| `IO` | The server process is waiting for an I/O operation to complete. `wait_event` will identify the specific wait point; see [???](#wait-event-io-table). |
| `IPC` | The server process is waiting for some interaction with another server process. `wait_event` will identify the specific wait point; see [???](#wait-event-ipc-table). |
| `Lock` | The server process is waiting for a heavyweight lock. Heavyweight locks, also known as lock manager locks or simply locks, primarily protect SQL-visible objects such as tables. However, they are also used to ensure mutual exclusion for certain internal operations such as relation extension. `wait_event` will identify the type of lock awaited; see [???](#wait-event-lock-table). |
| `LWLock` | The server process is waiting for a lightweight lock. Most such locks protect a particular data structure in shared memory. `wait_event` will contain a name identifying the purpose of the lightweight lock. (Some locks have specific names; others are part of a group of locks each with a similar purpose.) See [???](#wait-event-lwlock-table). |
| `Timeout` | The server process is waiting for a timeout to expire. `wait_event` will identify the specific wait point; see [???](#wait-event-timeout-table). |

Wait Event Types {#wait-event-table}

Here are examples of how wait events can be viewed:

    SELECT pid, wait_event_type, wait_event FROM pg_stat_activity WHERE wait_event is NOT NULL;
     pid  | wait_event_type | wait_event
    ------+-----------------+------------
     2540 | Lock            | relation
     6644 | LWLock          | ProcArray
    (2 rows)

    SELECT a.pid, a.wait_event, w.description
      FROM pg_stat_activity a JOIN
           pg_wait_events w ON (a.wait_event_type = w.type AND
                                a.wait_event = w.name)
      WHERE a.wait_event is NOT NULL and a.state = 'active';
    -[ RECORD 1 ]------------------------------------------------------​------------
    pid         | 686674
    wait_event  | WALInitSync
    description | Waiting for a newly initialized WAL file to reach durable storage

> [!NOTE]
> Extensions can add `Extension`, `InjectionPoint`, and `LWLock` events to the lists shown in [???](#wait-event-extension-table) and [???](#wait-event-lwlock-table). In some cases, the name of an `LWLock` assigned by an extension will not be available in all server processes. It might be reported as just “`extension`” rather than the extension-assigned name.

### pg_stat_replication

pg_stat_replication

The pg_stat_replication view will contain one row per WAL sender process, showing statistics about replication to that sender's connected standby server. Only directly connected standbys are listed; no information is available about downstream standby servers.

<table id="pg-stat-replication-view">
<caption>pg_stat_replication View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">pid <code>integer</code></p>
<p>Process ID of a WAL sender process</p></td>
</tr>
<tr>
<td><p role="column_definition">usesysid <code>oid</code></p>
<p>OID of the user logged into this WAL sender process</p></td>
</tr>
<tr>
<td><p role="column_definition">usename <code>name</code></p>
<p>Name of the user logged into this WAL sender process</p></td>
</tr>
<tr>
<td><p role="column_definition">application_name <code>text</code></p>
<p>Name of the application that is connected to this WAL sender</p></td>
</tr>
<tr>
<td><p role="column_definition">client_addr <code>inet</code></p>
<p>IP address of the client connected to this WAL sender. If this field is null, it indicates that the client is connected via a Unix socket on the server machine.</p></td>
</tr>
<tr>
<td><p role="column_definition">client_hostname <code>text</code></p>
<p>Host name of the connected client, as reported by a reverse DNS lookup of client_addr. This field will only be non-null for IP connections, and only when <a href="#guc-log-hostname">???</a> is enabled.</p></td>
</tr>
<tr>
<td><p role="column_definition">client_port <code>integer</code></p>
<p>TCP port number that the client is using for communication with this WAL sender, or <code>-1</code> if a Unix socket is used</p></td>
</tr>
<tr>
<td><p role="column_definition">backend_start <code>timestamp with time zone</code></p>
<p>Time when this process was started, i.e., when the client connected to this WAL sender</p></td>
</tr>
<tr>
<td><p role="column_definition">backend_xmin <code>xid</code></p>
<p>This standby's <code>xmin</code> horizon reported by <a href="#guc-hot-standby-feedback">???</a>.</p></td>
</tr>
<tr>
<td><p role="column_definition">state <code>text</code></p>
<p>Current WAL sender state. Possible values are:</p>
<ul>
<li><p><code>startup</code>: This WAL sender is starting up.</p></li>
<li><p><code>catchup</code>: This WAL sender's connected standby is catching up with the primary.</p></li>
<li><p><code>streaming</code>: This WAL sender is streaming changes after its connected standby server has caught up with the primary.</p></li>
<li><p><code>backup</code>: This WAL sender is sending a backup.</p></li>
<li><p><code>stopping</code>: This WAL sender is stopping.</p></li>
</ul></td>
</tr>
<tr>
<td><p role="column_definition">sent_lsn <code>pg_lsn</code></p>
<p>Last write-ahead log location sent on this connection</p></td>
</tr>
<tr>
<td><p role="column_definition">write_lsn <code>pg_lsn</code></p>
<p>Last write-ahead log location written to disk by this standby server</p></td>
</tr>
<tr>
<td><p role="column_definition">flush_lsn <code>pg_lsn</code></p>
<p>Last write-ahead log location flushed to disk by this standby server</p></td>
</tr>
<tr>
<td><p role="column_definition">replay_lsn <code>pg_lsn</code></p>
<p>Last write-ahead log location replayed into the database on this standby server</p></td>
</tr>
<tr>
<td><p role="column_definition">write_lag <code>interval</code></p>
<p>Time elapsed between flushing recent WAL locally and receiving notification that this standby server has written it (but not yet flushed it or applied it). This can be used to gauge the delay that <code>synchronous_commit</code> level <code>remote_write</code> incurred while committing if this server was configured as a synchronous standby.</p></td>
</tr>
<tr>
<td><p role="column_definition">flush_lag <code>interval</code></p>
<p>Time elapsed between flushing recent WAL locally and receiving notification that this standby server has written and flushed it (but not yet applied it). This can be used to gauge the delay that <code>synchronous_commit</code> level <code>on</code> incurred while committing if this server was configured as a synchronous standby.</p></td>
</tr>
<tr>
<td><p role="column_definition">replay_lag <code>interval</code></p>
<p>Time elapsed between flushing recent WAL locally and receiving notification that this standby server has written, flushed and applied it. This can be used to gauge the delay that <code>synchronous_commit</code> level <code>remote_apply</code> incurred while committing if this server was configured as a synchronous standby.</p></td>
</tr>
<tr>
<td><p role="column_definition">sync_priority <code>integer</code></p>
<p>Priority of this standby server for being chosen as the synchronous standby in a priority-based synchronous replication. This has no effect in a quorum-based synchronous replication.</p></td>
</tr>
<tr>
<td><p role="column_definition">sync_state <code>text</code></p>
<p>Synchronous state of this standby server. Possible values are:</p>
<ul>
<li><p><code>async</code>: This standby server is asynchronous.</p></li>
<li><p><code>potential</code>: This standby server is now asynchronous, but can potentially become synchronous if one of current synchronous ones fails.</p></li>
<li><p><code>sync</code>: This standby server is synchronous.</p></li>
<li><p><code>quorum</code>: This standby server is considered as a candidate for quorum standbys.</p></li>
</ul></td>
</tr>
<tr>
<td><p role="column_definition">reply_time <code>timestamp with time zone</code></p>
<p>Send time of last reply message received from standby server</p></td>
</tr>
</tbody>
</table>

The lag times reported in the pg_stat_replication view are measurements of the time taken for recent WAL to be written, flushed and replayed and for the sender to know about it. These times represent the commit delay that was (or would have been) introduced by each synchronous commit level, if the remote server was configured as a synchronous standby. For an asynchronous standby, the replay_lag column approximates the delay before recent transactions became visible to queries. If the standby server has entirely caught up with the sending server and there is no more WAL activity, the most recently measured lag times will continue to be displayed for a short time and then show NULL.

Lag times work automatically for physical replication. Logical decoding plugins may optionally emit tracking messages; if they do not, the tracking mechanism will simply display NULL lag.

> [!NOTE]
> The reported lag times are not predictions of how long it will take for the standby to catch up with the sending server assuming the current rate of replay. Such a system would show similar times while new WAL is being generated, but would differ when the sender becomes idle. In particular, when the standby has caught up completely, pg_stat_replication shows the time taken to write, flush and replay the most recent reported WAL location rather than zero as some users might expect. This is consistent with the goal of measuring synchronous commit and transaction visibility delays for recent write transactions. To reduce confusion for users expecting a different model of lag, the lag columns revert to NULL after a short time on a fully replayed idle system. Monitoring systems should choose whether to represent this as missing data, zero or continue to display the last known value.

### pg_stat_replication_slots

pg_stat_replication_slots

The pg_stat_replication_slots view will contain one row per logical replication slot, showing statistics about its usage.

<table id="pg-stat-replication-slots-view">
<caption>pg_stat_replication_slots View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">slot_name <code>text</code></p>
<p>A unique, cluster-wide identifier for the replication slot</p></td>
</tr>
<tr>
<td><p role="column_definition">spill_txns <code>bigint</code></p>
<p>Number of transactions spilled to disk once the memory used by logical decoding to decode changes from WAL has exceeded <code>logical_decoding_work_mem</code>. The counter gets incremented for both top-level transactions and subtransactions.</p></td>
</tr>
<tr>
<td><p role="column_definition">spill_count <code>bigint</code></p>
<p>Number of times transactions were spilled to disk while decoding changes from WAL for this slot. This counter is incremented each time a transaction is spilled, and the same transaction may be spilled multiple times.</p></td>
</tr>
<tr>
<td><p role="column_definition">spill_bytes <code>bigint</code></p>
<p>Amount of decoded transaction data spilled to disk while performing decoding of changes from WAL for this slot. This and other spill counters can be used to gauge the I/O which occurred during logical decoding and allow tuning <code>logical_decoding_work_mem</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">stream_txns <code>bigint</code></p>
<p>Number of in-progress transactions streamed to the decoding output plugin after the memory used by logical decoding to decode changes from WAL for this slot has exceeded <code>logical_decoding_work_mem</code>. Streaming only works with top-level transactions (subtransactions can't be streamed independently), so the counter is not incremented for subtransactions.</p></td>
</tr>
<tr>
<td><p role="column_definition">stream_count<code>bigint</code></p>
<p>Number of times in-progress transactions were streamed to the decoding output plugin while decoding changes from WAL for this slot. This counter is incremented each time a transaction is streamed, and the same transaction may be streamed multiple times.</p></td>
</tr>
<tr>
<td><p role="column_definition">stream_bytes<code>bigint</code></p>
<p>Amount of transaction data decoded for streaming in-progress transactions to the decoding output plugin while decoding changes from WAL for this slot. This and other streaming counters for this slot can be used to tune <code>logical_decoding_work_mem</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">total_txns <code>bigint</code></p>
<p>Number of decoded transactions sent to the decoding output plugin for this slot. This counts top-level transactions only, and is not incremented for subtransactions. Note that this includes the transactions that are streamed and/or spilled.</p></td>
</tr>
<tr>
<td><p role="column_definition">total_bytes<code>bigint</code></p>
<p>Amount of transaction data decoded for sending transactions to the decoding output plugin while decoding changes from WAL for this slot. Note that this includes data that is streamed and/or spilled.</p></td>
</tr>
<tr>
<td><p role="column_definition">stats_reset <code>timestamp with time zone</code></p>
<p>Time at which these statistics were last reset</p></td>
</tr>
</tbody>
</table>

### pg_stat_wal_receiver

pg_stat_wal_receiver

The pg_stat_wal_receiver view will contain only one row, showing statistics about the WAL receiver from that receiver's connected server.

<table id="pg-stat-wal-receiver-view">
<caption>pg_stat_wal_receiver View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">pid <code>integer</code></p>
<p>Process ID of the WAL receiver process</p></td>
</tr>
<tr>
<td><p role="column_definition">status <code>text</code></p>
<p>Activity status of the WAL receiver process</p></td>
</tr>
<tr>
<td><p role="column_definition">receive_start_lsn <code>pg_lsn</code></p>
<p>First write-ahead log location used when WAL receiver is started</p></td>
</tr>
<tr>
<td><p role="column_definition">receive_start_tli <code>integer</code></p>
<p>First timeline number used when WAL receiver is started</p></td>
</tr>
<tr>
<td><p role="column_definition">written_lsn <code>pg_lsn</code></p>
<p>Last write-ahead log location already received and written to disk, but not flushed. This should not be used for data integrity checks.</p></td>
</tr>
<tr>
<td><p role="column_definition">flushed_lsn <code>pg_lsn</code></p>
<p>Last write-ahead log location already received and flushed to disk, the initial value of this field being the first log location used when WAL receiver is started</p></td>
</tr>
<tr>
<td><p role="column_definition">received_tli <code>integer</code></p>
<p>Timeline number of last write-ahead log location received and flushed to disk, the initial value of this field being the timeline number of the first log location used when WAL receiver is started</p></td>
</tr>
<tr>
<td><p role="column_definition">last_msg_send_time <code>timestamp with time zone</code></p>
<p>Send time of last message received from origin WAL sender</p></td>
</tr>
<tr>
<td><p role="column_definition">last_msg_receipt_time <code>timestamp with time zone</code></p>
<p>Receipt time of last message received from origin WAL sender</p></td>
</tr>
<tr>
<td><p role="column_definition">latest_end_lsn <code>pg_lsn</code></p>
<p>Last write-ahead log location reported to origin WAL sender</p></td>
</tr>
<tr>
<td><p role="column_definition">latest_end_time <code>timestamp with time zone</code></p>
<p>Time of last write-ahead log location reported to origin WAL sender</p></td>
</tr>
<tr>
<td><p role="column_definition">slot_name <code>text</code></p>
<p>Replication slot name used by this WAL receiver</p></td>
</tr>
<tr>
<td><p role="column_definition">sender_host <code>text</code></p>
<p>Host of the PostgreSQL instance this WAL receiver is connected to. This can be a host name, an IP address, or a directory path if the connection is via Unix socket. (The path case can be distinguished because it will always be an absolute path, beginning with <code>/</code>.)</p></td>
</tr>
<tr>
<td><p role="column_definition">sender_port <code>integer</code></p>
<p>Port number of the PostgreSQL instance this WAL receiver is connected to.</p></td>
</tr>
<tr>
<td><p role="column_definition">conninfo <code>text</code></p>
<p>Connection string used by this WAL receiver, with security-sensitive fields obfuscated.</p></td>
</tr>
</tbody>
</table>

### pg_stat_recovery_prefetch

pg_stat_recovery_prefetch

The pg_stat_recovery_prefetch view will contain only one row. The columns wal_distance, block_distance and io_depth show current values, and the other columns show cumulative counters that can be reset with the `pg_stat_reset_shared` function.

<table id="pg-stat-recovery-prefetch-view">
<caption>pg_stat_recovery_prefetch View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">stats_reset <code>timestamp with time zone</code></p>
<p>Time at which these statistics were last reset</p></td>
</tr>
<tr>
<td><p role="column_definition">prefetch <code>bigint</code></p>
<p>Number of blocks prefetched because they were not in the buffer pool</p></td>
</tr>
<tr>
<td><p role="column_definition">hit <code>bigint</code></p>
<p>Number of blocks not prefetched because they were already in the buffer pool</p></td>
</tr>
<tr>
<td><p role="column_definition">skip_init <code>bigint</code></p>
<p>Number of blocks not prefetched because they would be zero-initialized</p></td>
</tr>
<tr>
<td><p role="column_definition">skip_new <code>bigint</code></p>
<p>Number of blocks not prefetched because they didn't exist yet</p></td>
</tr>
<tr>
<td><p role="column_definition">skip_fpw <code>bigint</code></p>
<p>Number of blocks not prefetched because a full page image was included in the WAL</p></td>
</tr>
<tr>
<td><p role="column_definition">skip_rep <code>bigint</code></p>
<p>Number of blocks not prefetched because they were already recently prefetched</p></td>
</tr>
<tr>
<td><p role="column_definition">wal_distance <code>int</code></p>
<p>How many bytes ahead the prefetcher is looking</p></td>
</tr>
<tr>
<td><p role="column_definition">block_distance <code>int</code></p>
<p>How many blocks ahead the prefetcher is looking</p></td>
</tr>
<tr>
<td><p role="column_definition">io_depth <code>int</code></p>
<p>How many prefetches have been initiated but are not yet known to have completed</p></td>
</tr>
</tbody>
</table>

### pg_stat_subscription

pg_stat_subscription

<table id="pg-stat-subscription">
<caption>pg_stat_subscription View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">subid <code>oid</code></p>
<p>OID of the subscription</p></td>
</tr>
<tr>
<td><p role="column_definition">subname <code>name</code></p>
<p>Name of the subscription</p></td>
</tr>
<tr>
<td><p role="column_definition">worker_type <code>text</code></p>
<p>Type of the subscription worker process. Possible types are <code>apply</code>, <code>parallel apply</code>, and <code>table synchronization</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">pid <code>integer</code></p>
<p>Process ID of the subscription worker process</p></td>
</tr>
<tr>
<td><p role="column_definition">leader_pid <code>integer</code></p>
<p>Process ID of the leader apply worker if this process is a parallel apply worker; NULL if this process is a leader apply worker or a table synchronization worker</p></td>
</tr>
<tr>
<td><p role="column_definition">relid <code>oid</code></p>
<p>OID of the relation that the worker is synchronizing; NULL for the leader apply worker and parallel apply workers</p></td>
</tr>
<tr>
<td><p role="column_definition">received_lsn <code>pg_lsn</code></p>
<p>Last write-ahead log location received, the initial value of this field being 0; NULL for parallel apply workers</p></td>
</tr>
<tr>
<td><p role="column_definition">last_msg_send_time <code>timestamp with time zone</code></p>
<p>Send time of last message received from origin WAL sender; NULL for parallel apply workers</p></td>
</tr>
<tr>
<td><p role="column_definition">last_msg_receipt_time <code>timestamp with time zone</code></p>
<p>Receipt time of last message received from origin WAL sender; NULL for parallel apply workers</p></td>
</tr>
<tr>
<td><p role="column_definition">latest_end_lsn <code>pg_lsn</code></p>
<p>Last write-ahead log location reported to origin WAL sender; NULL for parallel apply workers</p></td>
</tr>
<tr>
<td><p role="column_definition">latest_end_time <code>timestamp with time zone</code></p>
<p>Time of last write-ahead log location reported to origin WAL sender; NULL for parallel apply workers</p></td>
</tr>
</tbody>
</table>

### pg_stat_subscription_stats

pg_stat_subscription_stats

The pg_stat_subscription_stats view will contain one row per subscription.

<table id="pg-stat-subscription-stats">
<caption>pg_stat_subscription_stats View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">subid <code>oid</code></p>
<p>OID of the subscription</p></td>
</tr>
<tr>
<td><p role="column_definition">subname <code>name</code></p>
<p>Name of the subscription</p></td>
</tr>
<tr>
<td><p role="column_definition">apply_error_count <code>bigint</code></p>
<p>Number of times an error occurred while applying changes</p></td>
</tr>
<tr>
<td><p role="column_definition">sync_error_count <code>bigint</code></p>
<p>Number of times an error occurred during the initial table synchronization</p></td>
</tr>
<tr>
<td><p role="column_definition">stats_reset <code>timestamp with time zone</code></p>
<p>Time at which these statistics were last reset</p></td>
</tr>
</tbody>
</table>

### pg_stat_ssl

pg_stat_ssl

The pg_stat_ssl view will contain one row per backend or WAL sender process, showing statistics about SSL usage on this connection. It can be joined to pg_stat_activity or pg_stat_replication on the pid column to get more details about the connection.

<table id="pg-stat-ssl-view">
<caption>pg_stat_ssl View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">pid <code>integer</code></p>
<p>Process ID of a backend or WAL sender process</p></td>
</tr>
<tr>
<td><p role="column_definition">ssl <code>boolean</code></p>
<p>True if SSL is used on this connection</p></td>
</tr>
<tr>
<td><p role="column_definition">version <code>text</code></p>
<p>Version of SSL in use, or NULL if SSL is not in use on this connection</p></td>
</tr>
<tr>
<td><p role="column_definition">cipher <code>text</code></p>
<p>Name of SSL cipher in use, or NULL if SSL is not in use on this connection</p></td>
</tr>
<tr>
<td><p role="column_definition">bits <code>integer</code></p>
<p>Number of bits in the encryption algorithm used, or NULL if SSL is not used on this connection</p></td>
</tr>
<tr>
<td><p role="column_definition">client_dn <code>text</code></p>
<p>Distinguished Name (DN) field from the client certificate used, or NULL if no client certificate was supplied or if SSL is not in use on this connection. This field is truncated if the DN field is longer than <code>NAMEDATALEN</code> (64 characters in a standard build).</p></td>
</tr>
<tr>
<td><p role="column_definition">client_serial <code>numeric</code></p>
<p>Serial number of the client certificate, or NULL if no client certificate was supplied or if SSL is not in use on this connection. The combination of certificate serial number and certificate issuer uniquely identifies a certificate (unless the issuer erroneously reuses serial numbers).</p></td>
</tr>
<tr>
<td><p role="column_definition">issuer_dn <code>text</code></p>
<p>DN of the issuer of the client certificate, or NULL if no client certificate was supplied or if SSL is not in use on this connection. This field is truncated like client_dn.</p></td>
</tr>
</tbody>
</table>

### pg_stat_gssapi

pg_stat_gssapi

The pg_stat_gssapi view will contain one row per backend, showing information about GSSAPI usage on this connection. It can be joined to pg_stat_activity or pg_stat_replication on the pid column to get more details about the connection.

<table id="pg-stat-gssapi-view">
<caption>pg_stat_gssapi View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">pid <code>integer</code></p>
<p>Process ID of a backend</p></td>
</tr>
<tr>
<td><p role="column_definition">gss_authenticated <code>boolean</code></p>
<p>True if GSSAPI authentication was used for this connection</p></td>
</tr>
<tr>
<td><p role="column_definition">principal <code>text</code></p>
<p>Principal used to authenticate this connection, or NULL if GSSAPI was not used to authenticate this connection. This field is truncated if the principal is longer than <code>NAMEDATALEN</code> (64 characters in a standard build).</p></td>
</tr>
<tr>
<td><p role="column_definition">encrypted <code>boolean</code></p>
<p>True if GSSAPI encryption is in use on this connection</p></td>
</tr>
<tr>
<td><p role="column_definition">credentials_delegated <code>boolean</code></p>
<p>True if GSSAPI credentials were delegated on this connection.</p></td>
</tr>
</tbody>
</table>

### pg_stat_archiver

pg_stat_archiver

The pg_stat_archiver view will always have a single row, containing data about the archiver process of the cluster.

<table id="pg-stat-archiver-view">
<caption>pg_stat_archiver View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">archived_count <code>bigint</code></p>
<p>Number of WAL files that have been successfully archived</p></td>
</tr>
<tr>
<td><p role="column_definition">last_archived_wal <code>text</code></p>
<p>Name of the WAL file most recently successfully archived</p></td>
</tr>
<tr>
<td><p role="column_definition">last_archived_time <code>timestamp with time zone</code></p>
<p>Time of the most recent successful archive operation</p></td>
</tr>
<tr>
<td><p role="column_definition">failed_count <code>bigint</code></p>
<p>Number of failed attempts for archiving WAL files</p></td>
</tr>
<tr>
<td><p role="column_definition">last_failed_wal <code>text</code></p>
<p>Name of the WAL file of the most recent failed archival operation</p></td>
</tr>
<tr>
<td><p role="column_definition">last_failed_time <code>timestamp with time zone</code></p>
<p>Time of the most recent failed archival operation</p></td>
</tr>
<tr>
<td><p role="column_definition">stats_reset <code>timestamp with time zone</code></p>
<p>Time at which these statistics were last reset</p></td>
</tr>
</tbody>
</table>

Normally, WAL files are archived in order, oldest to newest, but that is not guaranteed, and does not hold under special circumstances like when promoting a standby or after crash recovery. Therefore it is not safe to assume that all files older than last_archived_wal have also been successfully archived.

### pg_stat_io

pg_stat_io

The pg_stat_io view will contain one row for each combination of backend type, target I/O object, and I/O context, showing cluster-wide I/O statistics. Combinations which do not make sense are omitted.

Currently, I/O on relations (e.g. tables, indexes) is tracked. However, relation I/O which bypasses shared buffers (e.g. when moving a table from one tablespace to another) is currently not tracked.

<table id="pg-stat-io-view">
<caption>pg_stat_io View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">backend_type <code>text</code></p>
<p>Type of backend (e.g. background worker, autovacuum worker). See <a href="#monitoring-pg-stat-activity-view"> pg_stat_activity</a> for more information on <code>backend_type</code>s. Some <code>backend_type</code>s do not accumulate I/O operation statistics and will not be included in the view.</p></td>
</tr>
<tr>
<td><p role="column_definition">object <code>text</code></p>
<p>Target object of an I/O operation. Possible values are:</p>
<ul>
<li><p><code>relation</code>: Permanent relations.</p></li>
<li><p><code>temp relation</code>: Temporary relations.</p></li>
</ul></td>
</tr>
<tr>
<td><p role="column_definition">context <code>text</code></p>
<p>The context of an I/O operation. Possible values are:</p>
<ul>
<li><p><code>normal</code>: The default or standard <code>context</code> for a type of I/O operation. For example, by default, relation data is read into and written out from shared buffers. Thus, reads and writes of relation data to and from shared buffers are tracked in <code>context</code> <code>normal</code>.</p></li>
<li><p><code>vacuum</code>: I/O operations performed outside of shared buffers while vacuuming and analyzing permanent relations. Temporary table vacuums use the same local buffer pool as other temporary table I/O operations and are tracked in <code>context</code> <code>normal</code>.</p></li>
<li><p><code>bulkread</code>: Certain large read I/O operations done outside of shared buffers, for example, a sequential scan of a large table.</p></li>
<li><p><code>bulkwrite</code>: Certain large write I/O operations done outside of shared buffers, such as <code>COPY</code>.</p></li>
</ul></td>
</tr>
<tr>
<td><p role="column_definition">reads <code>bigint</code></p>
<p>Number of read operations, each of the size specified in <code>op_bytes</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">read_time <code>double precision</code></p>
<p>Time spent in read operations in milliseconds (if <a href="#guc-track-io-timing">???</a> is enabled, otherwise zero)</p></td>
</tr>
<tr>
<td><p role="column_definition">writes <code>bigint</code></p>
<p>Number of write operations, each of the size specified in <code>op_bytes</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">write_time <code>double precision</code></p>
<p>Time spent in write operations in milliseconds (if <a href="#guc-track-io-timing">???</a> is enabled, otherwise zero)</p></td>
</tr>
<tr>
<td><p role="column_definition">writebacks <code>bigint</code></p>
<p>Number of units of size <code>op_bytes</code> which the process requested the kernel write out to permanent storage.</p></td>
</tr>
<tr>
<td><p role="column_definition">writeback_time <code>double precision</code></p>
<p>Time spent in writeback operations in milliseconds (if <a href="#guc-track-io-timing">???</a> is enabled, otherwise zero). This includes the time spent queueing write-out requests and, potentially, the time spent to write out the dirty data.</p></td>
</tr>
<tr>
<td><p role="column_definition">extends <code>bigint</code></p>
<p>Number of relation extend operations, each of the size specified in <code>op_bytes</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">extend_time <code>double precision</code></p>
<p>Time spent in extend operations in milliseconds (if <a href="#guc-track-io-timing">???</a> is enabled, otherwise zero)</p></td>
</tr>
<tr>
<td><p role="column_definition">op_bytes <code>bigint</code></p>
<p>The number of bytes per unit of I/O read, written, or extended.</p>
<p>Relation data reads, writes, and extends are done in <code>block_size</code> units, derived from the build-time parameter <code>BLCKSZ</code>, which is <code>8192</code> by default.</p></td>
</tr>
<tr>
<td><p role="column_definition">hits <code>bigint</code></p>
<p>The number of times a desired block was found in a shared buffer.</p></td>
</tr>
<tr>
<td><p role="column_definition">evictions <code>bigint</code></p>
<p>Number of times a block has been written out from a shared or local buffer in order to make it available for another use.</p>
<p>In <code>context</code> <code>normal</code>, this counts the number of times a block was evicted from a buffer and replaced with another block. In <code>context</code>s <code>bulkwrite</code>, <code>bulkread</code>, and <code>vacuum</code>, this counts the number of times a block was evicted from shared buffers in order to add the shared buffer to a separate, size-limited ring buffer for use in a bulk I/O operation.</p></td>
</tr>
<tr>
<td><p role="column_definition">reuses <code>bigint</code></p>
<p>The number of times an existing buffer in a size-limited ring buffer outside of shared buffers was reused as part of an I/O operation in the <code>bulkread</code>, <code>bulkwrite</code>, or <code>vacuum</code> <code>context</code>s.</p></td>
</tr>
<tr>
<td><p role="column_definition">fsyncs <code>bigint</code></p>
<p>Number of <code>fsync</code> calls. These are only tracked in <code>context</code> <code>normal</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">fsync_time <code>double precision</code></p>
<p>Time spent in fsync operations in milliseconds (if <a href="#guc-track-io-timing">???</a> is enabled, otherwise zero)</p></td>
</tr>
<tr>
<td><p role="column_definition">stats_reset <code>timestamp with time zone</code></p>
<p>Time at which these statistics were last reset.</p></td>
</tr>
</tbody>
</table>

Some backend types never perform I/O operations on some I/O objects and/or in some I/O contexts. These rows are omitted from the view. For example, the checkpointer does not checkpoint temporary tables, so there will be no rows for `backend_type` `checkpointer` and `object` `temp relation`.

In addition, some I/O operations will never be performed either by certain backend types or on certain I/O objects and/or in certain I/O contexts. These cells will be NULL. For example, temporary tables are not `fsync`ed, so `fsyncs` will be NULL for `object` `temp relation`. Also, the background writer does not perform reads, so `reads` will be NULL in rows for `backend_type` `background writer`.

pg_stat_io can be used to inform database tuning. For example:

- A high `evictions` count can indicate that shared buffers should be increased.

- Client backends rely on the checkpointer to ensure data is persisted to permanent storage. Large numbers of `fsyncs` by `client backend`s could indicate a misconfiguration of shared buffers or of the checkpointer. More information on configuring the checkpointer can be found in [???](#wal-configuration).

- Normally, client backends should be able to rely on auxiliary processes like the checkpointer and the background writer to write out dirty data as much as possible. Large numbers of writes by client backends could indicate a misconfiguration of shared buffers or of the checkpointer. More information on configuring the checkpointer can be found in [???](#wal-configuration).

> [!NOTE]
> Columns tracking I/O time will only be non-zero when [???](#guc-track-io-timing) is enabled. The user should be careful when referencing these columns in combination with their corresponding I/O operations in case `track_io_timing` was not enabled for the entire time since the last stats reset.

### pg_stat_bgwriter

pg_stat_bgwriter

The pg_stat_bgwriter view will always have a single row, containing data about the background writer of the cluster.

<table id="pg-stat-bgwriter-view">
<caption>pg_stat_bgwriter View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">buffers_clean <code>bigint</code></p>
<p>Number of buffers written by the background writer</p></td>
</tr>
<tr>
<td><p role="column_definition">maxwritten_clean <code>bigint</code></p>
<p>Number of times the background writer stopped a cleaning scan because it had written too many buffers</p></td>
</tr>
<tr>
<td><p role="column_definition">buffers_alloc <code>bigint</code></p>
<p>Number of buffers allocated</p></td>
</tr>
<tr>
<td><p role="column_definition">stats_reset <code>timestamp with time zone</code></p>
<p>Time at which these statistics were last reset</p></td>
</tr>
</tbody>
</table>

### pg_stat_checkpointer

pg_stat_checkpointer

The pg_stat_checkpointer view will always have a single row, containing data about the checkpointer process of the cluster.

<table id="pg-stat-checkpointer-view">
<caption>pg_stat_checkpointer View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">num_timed <code>bigint</code></p>
<p>Number of scheduled checkpoints due to timeout. Note that checkpoints may be skipped if the server has been idle since the last one, and this value counts both completed and skipped checkpoints</p></td>
</tr>
<tr>
<td><p role="column_definition">num_requested <code>bigint</code></p>
<p>Number of requested checkpoints that have been performed</p></td>
</tr>
<tr>
<td><p role="column_definition">restartpoints_timed <code>bigint</code></p>
<p>Number of scheduled restartpoints due to timeout or after a failed attempt to perform it</p></td>
</tr>
<tr>
<td><p role="column_definition">restartpoints_req <code>bigint</code></p>
<p>Number of requested restartpoints</p></td>
</tr>
<tr>
<td><p role="column_definition">restartpoints_done <code>bigint</code></p>
<p>Number of restartpoints that have been performed</p></td>
</tr>
<tr>
<td><p role="column_definition">write_time <code>double precision</code></p>
<p>Total amount of time that has been spent in the portion of processing checkpoints and restartpoints where files are written to disk, in milliseconds</p></td>
</tr>
<tr>
<td><p role="column_definition">sync_time <code>double precision</code></p>
<p>Total amount of time that has been spent in the portion of processing checkpoints and restartpoints where files are synchronized to disk, in milliseconds</p></td>
</tr>
<tr>
<td><p role="column_definition">buffers_written <code>bigint</code></p>
<p>Number of buffers written during checkpoints and restartpoints</p></td>
</tr>
<tr>
<td><p role="column_definition">stats_reset <code>timestamp with time zone</code></p>
<p>Time at which these statistics were last reset</p></td>
</tr>
</tbody>
</table>

### pg_stat_wal

pg_stat_wal

The pg_stat_wal view will always have a single row, containing data about WAL activity of the cluster.

<table id="pg-stat-wal-view">
<caption>pg_stat_wal View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">wal_records <code>bigint</code></p>
<p>Total number of WAL records generated</p></td>
</tr>
<tr>
<td><p role="column_definition">wal_fpi <code>bigint</code></p>
<p>Total number of WAL full page images generated</p></td>
</tr>
<tr>
<td><p role="column_definition">wal_bytes <code>numeric</code></p>
<p>Total amount of WAL generated in bytes</p></td>
</tr>
<tr>
<td><p role="column_definition">wal_buffers_full <code>bigint</code></p>
<p>Number of times WAL data was written to disk because WAL buffers became full</p></td>
</tr>
<tr>
<td><p role="column_definition">wal_write <code>bigint</code></p>
<p>Number of times WAL buffers were written out to disk via <code>XLogWrite</code> request. See <a href="#wal-configuration">???</a> for more information about the internal WAL function <code>XLogWrite</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">wal_sync <code>bigint</code></p>
<p>Number of times WAL files were synced to disk via <code>issue_xlog_fsync</code> request (if <a href="#guc-fsync">???</a> is <code>on</code> and <a href="#guc-wal-sync-method">???</a> is either <code>fdatasync</code>, <code>fsync</code> or <code>fsync_writethrough</code>, otherwise zero). See <a href="#wal-configuration">???</a> for more information about the internal WAL function <code>issue_xlog_fsync</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">wal_write_time <code>double precision</code></p>
<p>Total amount of time spent writing WAL buffers to disk via <code>XLogWrite</code> request, in milliseconds (if <a href="#guc-track-wal-io-timing">???</a> is enabled, otherwise zero). This includes the sync time when <code>wal_sync_method</code> is either <code>open_datasync</code> or <code>open_sync</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">wal_sync_time <code>double precision</code></p>
<p>Total amount of time spent syncing WAL files to disk via <code>issue_xlog_fsync</code> request, in milliseconds (if <code>track_wal_io_timing</code> is enabled, <code>fsync</code> is <code>on</code>, and <code>wal_sync_method</code> is either <code>fdatasync</code>, <code>fsync</code> or <code>fsync_writethrough</code>, otherwise zero).</p></td>
</tr>
<tr>
<td><p role="column_definition">stats_reset <code>timestamp with time zone</code></p>
<p>Time at which these statistics were last reset</p></td>
</tr>
</tbody>
</table>

### pg_stat_database

pg_stat_database

The pg_stat_database view will contain one row for each database in the cluster, plus one for shared objects, showing database-wide statistics.

<table id="pg-stat-database-view">
<caption>pg_stat_database View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">datid <code>oid</code></p>
<p>OID of this database, or 0 for objects belonging to a shared relation</p></td>
</tr>
<tr>
<td><p role="column_definition">datname <code>name</code></p>
<p>Name of this database, or <code>NULL</code> for shared objects.</p></td>
</tr>
<tr>
<td><p role="column_definition">numbackends <code>integer</code></p>
<p>Number of backends currently connected to this database, or <code>NULL</code> for shared objects. This is the only column in this view that returns a value reflecting current state; all other columns return the accumulated values since the last reset.</p></td>
</tr>
<tr>
<td><p role="column_definition">xact_commit <code>bigint</code></p>
<p>Number of transactions in this database that have been committed</p></td>
</tr>
<tr>
<td><p role="column_definition">xact_rollback <code>bigint</code></p>
<p>Number of transactions in this database that have been rolled back</p></td>
</tr>
<tr>
<td><p role="column_definition">blks_read <code>bigint</code></p>
<p>Number of disk blocks read in this database</p></td>
</tr>
<tr>
<td><p role="column_definition">blks_hit <code>bigint</code></p>
<p>Number of times disk blocks were found already in the buffer cache, so that a read was not necessary (this only includes hits in the PostgreSQL buffer cache, not the operating system's file system cache)</p></td>
</tr>
<tr>
<td><p role="column_definition">tup_returned <code>bigint</code></p>
<p>Number of live rows fetched by sequential scans and index entries returned by index scans in this database</p></td>
</tr>
<tr>
<td><p role="column_definition">tup_fetched <code>bigint</code></p>
<p>Number of live rows fetched by index scans in this database</p></td>
</tr>
<tr>
<td><p role="column_definition">tup_inserted <code>bigint</code></p>
<p>Number of rows inserted by queries in this database</p></td>
</tr>
<tr>
<td><p role="column_definition">tup_updated <code>bigint</code></p>
<p>Number of rows updated by queries in this database</p></td>
</tr>
<tr>
<td><p role="column_definition">tup_deleted <code>bigint</code></p>
<p>Number of rows deleted by queries in this database</p></td>
</tr>
<tr>
<td><p role="column_definition">conflicts <code>bigint</code></p>
<p>Number of queries canceled due to conflicts with recovery in this database. (Conflicts occur only on standby servers; see <a href="#monitoring-pg-stat-database-conflicts-view"> pg_stat_database_conflicts</a> for details.)</p></td>
</tr>
<tr>
<td><p role="column_definition">temp_files <code>bigint</code></p>
<p>Number of temporary files created by queries in this database. All temporary files are counted, regardless of why the temporary file was created (e.g., sorting or hashing), and regardless of the <a href="#guc-log-temp-files">???</a> setting.</p></td>
</tr>
<tr>
<td><p role="column_definition">temp_bytes <code>bigint</code></p>
<p>Total amount of data written to temporary files by queries in this database. All temporary files are counted, regardless of why the temporary file was created, and regardless of the <a href="#guc-log-temp-files">???</a> setting.</p></td>
</tr>
<tr>
<td><p role="column_definition">deadlocks <code>bigint</code></p>
<p>Number of deadlocks detected in this database</p></td>
</tr>
<tr>
<td><p role="column_definition">checksum_failures <code>bigint</code></p>
<p>Number of data page checksum failures detected in this database (or on a shared object), or NULL if data checksums are not enabled.</p></td>
</tr>
<tr>
<td><p role="column_definition">checksum_last_failure <code>timestamp with time zone</code></p>
<p>Time at which the last data page checksum failure was detected in this database (or on a shared object), or NULL if data checksums are not enabled.</p></td>
</tr>
<tr>
<td><p role="column_definition">blk_read_time <code>double precision</code></p>
<p>Time spent reading data file blocks by backends in this database, in milliseconds (if <a href="#guc-track-io-timing">???</a> is enabled, otherwise zero)</p></td>
</tr>
<tr>
<td><p role="column_definition">blk_write_time <code>double precision</code></p>
<p>Time spent writing data file blocks by backends in this database, in milliseconds (if <a href="#guc-track-io-timing">???</a> is enabled, otherwise zero)</p></td>
</tr>
<tr>
<td><p role="column_definition">session_time <code>double precision</code></p>
<p>Time spent by database sessions in this database, in milliseconds (note that statistics are only updated when the state of a session changes, so if sessions have been idle for a long time, this idle time won't be included)</p></td>
</tr>
<tr>
<td><p role="column_definition">active_time <code>double precision</code></p>
<p>Time spent executing SQL statements in this database, in milliseconds (this corresponds to the states <code>active</code> and <code>fastpath function call</code> in <a href="#monitoring-pg-stat-activity-view"> pg_stat_activity</a>)</p></td>
</tr>
<tr>
<td><p role="column_definition">idle_in_transaction_time <code>double precision</code></p>
<p>Time spent idling while in a transaction in this database, in milliseconds (this corresponds to the states <code>idle in transaction</code> and <code>idle in transaction (aborted)</code> in <a href="#monitoring-pg-stat-activity-view"> pg_stat_activity</a>)</p></td>
</tr>
<tr>
<td><p role="column_definition">sessions <code>bigint</code></p>
<p>Total number of sessions established to this database</p></td>
</tr>
<tr>
<td><p role="column_definition">sessions_abandoned <code>bigint</code></p>
<p>Number of database sessions to this database that were terminated because connection to the client was lost</p></td>
</tr>
<tr>
<td><p role="column_definition">sessions_fatal <code>bigint</code></p>
<p>Number of database sessions to this database that were terminated by fatal errors</p></td>
</tr>
<tr>
<td><p role="column_definition">sessions_killed <code>bigint</code></p>
<p>Number of database sessions to this database that were terminated by operator intervention</p></td>
</tr>
<tr>
<td><p role="column_definition">stats_reset <code>timestamp with time zone</code></p>
<p>Time at which these statistics were last reset</p></td>
</tr>
</tbody>
</table>

### pg_stat_database_conflicts

pg_stat_database_conflicts

The pg_stat_database_conflicts view will contain one row per database, showing database-wide statistics about query cancels occurring due to conflicts with recovery on standby servers. This view will only contain information on standby servers, since conflicts do not occur on primary servers.

<table id="pg-stat-database-conflicts-view">
<caption>pg_stat_database_conflicts View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">datid <code>oid</code></p>
<p>OID of a database</p></td>
</tr>
<tr>
<td><p role="column_definition">datname <code>name</code></p>
<p>Name of this database</p></td>
</tr>
<tr>
<td><p role="column_definition">confl_tablespace <code>bigint</code></p>
<p>Number of queries in this database that have been canceled due to dropped tablespaces</p></td>
</tr>
<tr>
<td><p role="column_definition">confl_lock <code>bigint</code></p>
<p>Number of queries in this database that have been canceled due to lock timeouts</p></td>
</tr>
<tr>
<td><p role="column_definition">confl_snapshot <code>bigint</code></p>
<p>Number of queries in this database that have been canceled due to old snapshots</p></td>
</tr>
<tr>
<td><p role="column_definition">confl_bufferpin <code>bigint</code></p>
<p>Number of queries in this database that have been canceled due to pinned buffers</p></td>
</tr>
<tr>
<td><p role="column_definition">confl_deadlock <code>bigint</code></p>
<p>Number of queries in this database that have been canceled due to deadlocks</p></td>
</tr>
<tr>
<td><p role="column_definition">confl_active_logicalslot <code>bigint</code></p>
<p>Number of uses of logical slots in this database that have been canceled due to old snapshots or too low a <a href="#guc-wal-level">???</a> on the primary</p></td>
</tr>
</tbody>
</table>

### pg_stat_all_tables

pg_stat_all_tables

The pg_stat_all_tables view will contain one row for each table in the current database (including TOAST tables), showing statistics about accesses to that specific table. The pg_stat_user_tables and pg_stat_sys_tables views contain the same information, but filtered to only show user and system tables respectively.

<table id="pg-stat-all-tables-view">
<caption>pg_stat_all_tables View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">relid <code>oid</code></p>
<p>OID of a table</p></td>
</tr>
<tr>
<td><p role="column_definition">schemaname <code>name</code></p>
<p>Name of the schema that this table is in</p></td>
</tr>
<tr>
<td><p role="column_definition">relname <code>name</code></p>
<p>Name of this table</p></td>
</tr>
<tr>
<td><p role="column_definition">seq_scan <code>bigint</code></p>
<p>Number of sequential scans initiated on this table</p></td>
</tr>
<tr>
<td><p role="column_definition">last_seq_scan <code>timestamp with time zone</code></p>
<p>The time of the last sequential scan on this table, based on the most recent transaction stop time</p></td>
</tr>
<tr>
<td><p role="column_definition">seq_tup_read <code>bigint</code></p>
<p>Number of live rows fetched by sequential scans</p></td>
</tr>
<tr>
<td><p role="column_definition">idx_scan <code>bigint</code></p>
<p>Number of index scans initiated on this table</p></td>
</tr>
<tr>
<td><p role="column_definition">last_idx_scan <code>timestamp with time zone</code></p>
<p>The time of the last index scan on this table, based on the most recent transaction stop time</p></td>
</tr>
<tr>
<td><p role="column_definition">idx_tup_fetch <code>bigint</code></p>
<p>Number of live rows fetched by index scans</p></td>
</tr>
<tr>
<td><p role="column_definition">n_tup_ins <code>bigint</code></p>
<p>Total number of rows inserted</p></td>
</tr>
<tr>
<td><p role="column_definition">n_tup_upd <code>bigint</code></p>
<p>Total number of rows updated. (This includes row updates counted in n_tup_hot_upd and n_tup_newpage_upd, and remaining non-HOT updates.)</p></td>
</tr>
<tr>
<td><p role="column_definition">n_tup_del <code>bigint</code></p>
<p>Total number of rows deleted</p></td>
</tr>
<tr>
<td><p role="column_definition">n_tup_hot_upd <code>bigint</code></p>
<p>Number of rows <a href="#storage-hot">HOT updated</a>. These are updates where no successor versions are required in indexes.</p></td>
</tr>
<tr>
<td><p role="column_definition">n_tup_newpage_upd <code>bigint</code></p>
<p>Number of rows updated where the successor version goes onto a <em>new</em> heap page, leaving behind an original version with a <a href="#storage-tuple-layout">t_ctid field</a> that points to a different heap page. These are always non-HOT updates.</p></td>
</tr>
<tr>
<td><p role="column_definition">n_live_tup <code>bigint</code></p>
<p>Estimated number of live rows</p></td>
</tr>
<tr>
<td><p role="column_definition">n_dead_tup <code>bigint</code></p>
<p>Estimated number of dead rows</p></td>
</tr>
<tr>
<td><p role="column_definition">n_mod_since_analyze <code>bigint</code></p>
<p>Estimated number of rows modified since this table was last analyzed</p></td>
</tr>
<tr>
<td><p role="column_definition">n_ins_since_vacuum <code>bigint</code></p>
<p>Estimated number of rows inserted since this table was last vacuumed</p></td>
</tr>
<tr>
<td><p role="column_definition">last_vacuum <code>timestamp with time zone</code></p>
<p>Last time at which this table was manually vacuumed (not counting <code>VACUUM FULL</code>)</p></td>
</tr>
<tr>
<td><p role="column_definition">last_autovacuum <code>timestamp with time zone</code></p>
<p>Last time at which this table was vacuumed by the autovacuum daemon</p></td>
</tr>
<tr>
<td><p role="column_definition">last_analyze <code>timestamp with time zone</code></p>
<p>Last time at which this table was manually analyzed</p></td>
</tr>
<tr>
<td><p role="column_definition">last_autoanalyze <code>timestamp with time zone</code></p>
<p>Last time at which this table was analyzed by the autovacuum daemon</p></td>
</tr>
<tr>
<td><p role="column_definition">vacuum_count <code>bigint</code></p>
<p>Number of times this table has been manually vacuumed (not counting <code>VACUUM FULL</code>)</p></td>
</tr>
<tr>
<td><p role="column_definition">autovacuum_count <code>bigint</code></p>
<p>Number of times this table has been vacuumed by the autovacuum daemon</p></td>
</tr>
<tr>
<td><p role="column_definition">analyze_count <code>bigint</code></p>
<p>Number of times this table has been manually analyzed</p></td>
</tr>
<tr>
<td><p role="column_definition">autoanalyze_count <code>bigint</code></p>
<p>Number of times this table has been analyzed by the autovacuum daemon</p></td>
</tr>
</tbody>
</table>

### pg_stat_all_indexes

pg_stat_all_indexes

The pg_stat_all_indexes view will contain one row for each index in the current database, showing statistics about accesses to that specific index. The pg_stat_user_indexes and pg_stat_sys_indexes views contain the same information, but filtered to only show user and system indexes respectively.

<table id="pg-stat-all-indexes-view">
<caption>pg_stat_all_indexes View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">relid <code>oid</code></p>
<p>OID of the table for this index</p></td>
</tr>
<tr>
<td><p role="column_definition">indexrelid <code>oid</code></p>
<p>OID of this index</p></td>
</tr>
<tr>
<td><p role="column_definition">schemaname <code>name</code></p>
<p>Name of the schema this index is in</p></td>
</tr>
<tr>
<td><p role="column_definition">relname <code>name</code></p>
<p>Name of the table for this index</p></td>
</tr>
<tr>
<td><p role="column_definition">indexrelname <code>name</code></p>
<p>Name of this index</p></td>
</tr>
<tr>
<td><p role="column_definition">idx_scan <code>bigint</code></p>
<p>Number of index scans initiated on this index</p></td>
</tr>
<tr>
<td><p role="column_definition">last_idx_scan <code>timestamp with time zone</code></p>
<p>The time of the last scan on this index, based on the most recent transaction stop time</p></td>
</tr>
<tr>
<td><p role="column_definition">idx_tup_read <code>bigint</code></p>
<p>Number of index entries returned by scans on this index</p></td>
</tr>
<tr>
<td><p role="column_definition">idx_tup_fetch <code>bigint</code></p>
<p>Number of live table rows fetched by simple index scans using this index</p></td>
</tr>
</tbody>
</table>

Indexes can be used by simple index scans, “bitmap” index scans, and the optimizer. In a bitmap scan the output of several indexes can be combined via AND or OR rules, so it is difficult to associate individual heap row fetches with specific indexes when a bitmap scan is used. Therefore, a bitmap scan increments the pg_stat_all_indexes.idx_tup_read count(s) for the index(es) it uses, and it increments the pg_stat_all_tables.idx_tup_fetch count for the table, but it does not affect pg_stat_all_indexes.idx_tup_fetch. The optimizer also accesses indexes to check for supplied constants whose values are outside the recorded range of the optimizer statistics because the optimizer statistics might be stale.

> [!NOTE]
> The idx_tup_read and idx_tup_fetch counts can be different even without any use of bitmap scans, because idx_tup_read counts index entries retrieved from the index while idx_tup_fetch counts live rows fetched from the table. The latter will be less if any dead or not-yet-committed rows are fetched using the index, or if any heap fetches are avoided by means of an index-only scan.

> [!NOTE]
> Queries that use certain SQL constructs to search for rows matching any value out of a list or array of multiple scalar values (see [???](#functions-comparisons)) perform multiple “primitive” index scans (up to one primitive scan per scalar value) during query execution. Each internal primitive index scan increments pg_stat_all_indexes.idx_scan, so it's possible for the count of index scans to significantly exceed the total number of index scan executor node executions.

### pg_statio_all_tables

pg_statio_all_tables

The pg_statio_all_tables view will contain one row for each table in the current database (including TOAST tables), showing statistics about I/O on that specific table. The pg_statio_user_tables and pg_statio_sys_tables views contain the same information, but filtered to only show user and system tables respectively.

<table id="pg-statio-all-tables-view">
<caption>pg_statio_all_tables View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">relid <code>oid</code></p>
<p>OID of a table</p></td>
</tr>
<tr>
<td><p role="column_definition">schemaname <code>name</code></p>
<p>Name of the schema that this table is in</p></td>
</tr>
<tr>
<td><p role="column_definition">relname <code>name</code></p>
<p>Name of this table</p></td>
</tr>
<tr>
<td><p role="column_definition">heap_blks_read <code>bigint</code></p>
<p>Number of disk blocks read from this table</p></td>
</tr>
<tr>
<td><p role="column_definition">heap_blks_hit <code>bigint</code></p>
<p>Number of buffer hits in this table</p></td>
</tr>
<tr>
<td><p role="column_definition">idx_blks_read <code>bigint</code></p>
<p>Number of disk blocks read from all indexes on this table</p></td>
</tr>
<tr>
<td><p role="column_definition">idx_blks_hit <code>bigint</code></p>
<p>Number of buffer hits in all indexes on this table</p></td>
</tr>
<tr>
<td><p role="column_definition">toast_blks_read <code>bigint</code></p>
<p>Number of disk blocks read from this table's TOAST table (if any)</p></td>
</tr>
<tr>
<td><p role="column_definition">toast_blks_hit <code>bigint</code></p>
<p>Number of buffer hits in this table's TOAST table (if any)</p></td>
</tr>
<tr>
<td><p role="column_definition">tidx_blks_read <code>bigint</code></p>
<p>Number of disk blocks read from this table's TOAST table indexes (if any)</p></td>
</tr>
<tr>
<td><p role="column_definition">tidx_blks_hit <code>bigint</code></p>
<p>Number of buffer hits in this table's TOAST table indexes (if any)</p></td>
</tr>
</tbody>
</table>

### pg_statio_all_indexes

pg_statio_all_indexes

The pg_statio_all_indexes view will contain one row for each index in the current database, showing statistics about I/O on that specific index. The pg_statio_user_indexes and pg_statio_sys_indexes views contain the same information, but filtered to only show user and system indexes respectively.

<table id="pg-statio-all-indexes-view">
<caption>pg_statio_all_indexes View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">relid <code>oid</code></p>
<p>OID of the table for this index</p></td>
</tr>
<tr>
<td><p role="column_definition">indexrelid <code>oid</code></p>
<p>OID of this index</p></td>
</tr>
<tr>
<td><p role="column_definition">schemaname <code>name</code></p>
<p>Name of the schema this index is in</p></td>
</tr>
<tr>
<td><p role="column_definition">relname <code>name</code></p>
<p>Name of the table for this index</p></td>
</tr>
<tr>
<td><p role="column_definition">indexrelname <code>name</code></p>
<p>Name of this index</p></td>
</tr>
<tr>
<td><p role="column_definition">idx_blks_read <code>bigint</code></p>
<p>Number of disk blocks read from this index</p></td>
</tr>
<tr>
<td><p role="column_definition">idx_blks_hit <code>bigint</code></p>
<p>Number of buffer hits in this index</p></td>
</tr>
</tbody>
</table>

### pg_statio_all_sequences

pg_statio_all_sequences

The pg_statio_all_sequences view will contain one row for each sequence in the current database, showing statistics about I/O on that specific sequence.

<table id="pg-statio-all-sequences-view">
<caption>pg_statio_all_sequences View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">relid <code>oid</code></p>
<p>OID of a sequence</p></td>
</tr>
<tr>
<td><p role="column_definition">schemaname <code>name</code></p>
<p>Name of the schema this sequence is in</p></td>
</tr>
<tr>
<td><p role="column_definition">relname <code>name</code></p>
<p>Name of this sequence</p></td>
</tr>
<tr>
<td><p role="column_definition">blks_read <code>bigint</code></p>
<p>Number of disk blocks read from this sequence</p></td>
</tr>
<tr>
<td><p role="column_definition">blks_hit <code>bigint</code></p>
<p>Number of buffer hits in this sequence</p></td>
</tr>
</tbody>
</table>

### pg_stat_user_functions

pg_stat_user_functions

The pg_stat_user_functions view will contain one row for each tracked function, showing statistics about executions of that function. The [???](#guc-track-functions) parameter controls exactly which functions are tracked.

<table id="pg-stat-user-functions-view">
<caption>pg_stat_user_functions View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">funcid <code>oid</code></p>
<p>OID of a function</p></td>
</tr>
<tr>
<td><p role="column_definition">schemaname <code>name</code></p>
<p>Name of the schema this function is in</p></td>
</tr>
<tr>
<td><p role="column_definition">funcname <code>name</code></p>
<p>Name of this function</p></td>
</tr>
<tr>
<td><p role="column_definition">calls <code>bigint</code></p>
<p>Number of times this function has been called</p></td>
</tr>
<tr>
<td><p role="column_definition">total_time <code>double precision</code></p>
<p>Total time spent in this function and all other functions called by it, in milliseconds</p></td>
</tr>
<tr>
<td><p role="column_definition">self_time <code>double precision</code></p>
<p>Total time spent in this function itself, not including other functions called by it, in milliseconds</p></td>
</tr>
</tbody>
</table>

### pg_stat_slru

SLRU

pg_stat_slru

PostgreSQL accesses certain on-disk information via `SLRU` (simple least-recently-used) caches. The pg_stat_slru view will contain one row for each tracked SLRU cache, showing statistics about access to cached pages.

For each `SLRU` cache that's part of the core server, there is a configuration parameter that controls its size, with the suffix `_buffers` appended.

<table id="pg-stat-slru-view">
<caption>pg_stat_slru View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">name <code>text</code></p>
<p>Name of the SLRU</p></td>
</tr>
<tr>
<td><p role="column_definition">blks_zeroed <code>bigint</code></p>
<p>Number of blocks zeroed during initializations</p></td>
</tr>
<tr>
<td><p role="column_definition">blks_hit <code>bigint</code></p>
<p>Number of times disk blocks were found already in the SLRU, so that a read was not necessary (this only includes hits in the SLRU, not the operating system's file system cache)</p></td>
</tr>
<tr>
<td><p role="column_definition">blks_read <code>bigint</code></p>
<p>Number of disk blocks read for this SLRU</p></td>
</tr>
<tr>
<td><p role="column_definition">blks_written <code>bigint</code></p>
<p>Number of disk blocks written for this SLRU</p></td>
</tr>
<tr>
<td><p role="column_definition">blks_exists <code>bigint</code></p>
<p>Number of blocks checked for existence for this SLRU</p></td>
</tr>
<tr>
<td><p role="column_definition">flushes <code>bigint</code></p>
<p>Number of flushes of dirty data for this SLRU</p></td>
</tr>
<tr>
<td><p role="column_definition">truncates <code>bigint</code></p>
<p>Number of truncates for this SLRU</p></td>
</tr>
<tr>
<td><p role="column_definition">stats_reset <code>timestamp with time zone</code></p>
<p>Time at which these statistics were last reset</p></td>
</tr>
</tbody>
</table>

### Statistics Functions

Other ways of looking at the statistics can be set up by writing queries that use the same underlying statistics access functions used by the standard views shown above. For details such as the functions' names, consult the definitions of the standard views. (For example, in psql you could issue `\d+ pg_stat_activity`.) The access functions for per-database statistics take a database OID as an argument to identify which database to report on. The per-table and per-index functions take a table or index OID. The functions for per-function statistics take a function OID. Note that only tables, indexes, and functions in the current database can be seen with these functions.

Additional functions related to the cumulative statistics system are listed in [Additional Statistics Functions](#monitoring-stats-funcs-table).

<table id="monitoring-stats-funcs-table">
<caption>Additional Statistics Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><code>pg_backend_pid</code> () integer</p>
<p>Returns the process ID of the server process attached to the current session.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_get_activity</code> ( <code>integer</code> ) setof record</p>
<p>Returns a record of information about the backend with the specified process ID, or one record for each active backend in the system if <code>NULL</code> is specified. The fields returned are a subset of those in the pg_stat_activity view.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_get_snapshot_timestamp</code> () timestamp with time zone</p>
<p>Returns the timestamp of the current statistics snapshot, or NULL if no statistics snapshot has been taken. A snapshot is taken the first time cumulative statistics are accessed in a transaction if <code>stats_fetch_consistency</code> is set to <code>snapshot</code></p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_get_xact_blocks_fetched</code> ( <code>oid</code> ) bigint</p>
<p>Returns the number of block read requests for table or index, in the current transaction. This number minus <code>pg_stat_get_xact_blocks_hit</code> gives the number of kernel <code>read()</code> calls; the number of actual physical reads is usually lower due to kernel-level buffering.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_get_xact_blocks_hit</code> ( <code>oid</code> ) bigint</p>
<p>Returns the number of block read requests for table or index, in the current transaction, found in cache (not triggering kernel <code>read()</code> calls).</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_clear_snapshot</code> () void</p>
<p>Discards the current statistics snapshot or cached information.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_reset</code> () void</p>
<p>Resets all statistics counters for the current database to zero.</p>
<p>This function is restricted to superusers by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_reset_shared</code> ( [ <code>target</code> <code>text</code> <code>DEFAULT</code> <code>NULL</code> ] ) void</p>
<p>Resets some cluster-wide statistics counters to zero, depending on the argument. <code>target</code> can be:</p>
<ul>
<li><p><code>archiver</code>: Reset all the counters shown in the pg_stat_archiver view.</p></li>
<li><p><code>bgwriter</code>: Reset all the counters shown in the pg_stat_bgwriter view.</p></li>
<li><p><code>checkpointer</code>: Reset all the counters shown in the pg_stat_checkpointer view.</p></li>
<li><p><code>io</code>: Reset all the counters shown in the pg_stat_io view.</p></li>
<li><p><code>recovery_prefetch</code>: Reset all the counters shown in the pg_stat_recovery_prefetch view.</p></li>
<li><p><code>slru</code>: Reset all the counters shown in the pg_stat_slru view.</p></li>
<li><p><code>wal</code>: Reset all the counters shown in the pg_stat_wal view.</p></li>
<li><p><code>NULL</code> or not specified: All the counters from the views listed above are reset.</p></li>
</ul>
<p>This function is restricted to superusers by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_reset_single_table_counters</code> ( <code>oid</code> ) void</p>
<p>Resets statistics for a single table or index in the current database or shared across all databases in the cluster to zero.</p>
<p>This function is restricted to superusers by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_reset_single_function_counters</code> ( <code>oid</code> ) void</p>
<p>Resets statistics for a single function in the current database to zero.</p>
<p>This function is restricted to superusers by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_reset_slru</code> ( [ <code>target</code> <code>text</code> <code>DEFAULT</code> <code>NULL</code> ] ) void</p>
<p>Resets statistics to zero for a single SLRU cache, or for all SLRUs in the cluster. If <code>target</code> is <code>NULL</code> or is not specified, all the counters shown in the pg_stat_slru view for all SLRU caches are reset. The argument can be one of <code>commit_timestamp</code>, <code>multixact_member</code>, <code>multixact_offset</code>, <code>notify</code>, <code>serializable</code>, <code>subtransaction</code>, or <code>transaction</code> to reset the counters for only that entry. If the argument is <code>other</code> (or indeed, any unrecognized name), then the counters for all other SLRU caches, such as extension-defined caches, are reset.</p>
<p>This function is restricted to superusers by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_reset_replication_slot</code> ( <code>text</code> ) void</p>
<p>Resets statistics of the replication slot defined by the argument. If the argument is <code>NULL</code>, resets statistics for all the replication slots.</p>
<p>This function is restricted to superusers by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_reset_subscription_stats</code> ( <code>oid</code> ) void</p>
<p>Resets statistics for a single subscription shown in the pg_stat_subscription_stats view to zero. If the argument is <code>NULL</code>, reset statistics for all subscriptions.</p>
<p>This function is restricted to superusers by default, but other users can be granted EXECUTE to run the function.</p></td>
</tr>
</tbody>
</table>

> [!WARNING]
> Using `pg_stat_reset()` also resets counters that autovacuum uses to determine when to trigger a vacuum or an analyze. Resetting these counters can cause autovacuum to not perform necessary work, which can cause problems such as table bloat or out-dated table statistics. A database-wide `ANALYZE` is recommended after the statistics have been reset.

`pg_stat_get_activity`, the underlying function of the pg_stat_activity view, returns a set of records containing all the available information about each backend process. Sometimes it may be more convenient to obtain just a subset of this information. In such cases, another set of per-backend statistics access functions can be used; these are shown in [Per-Backend Statistics Functions](#monitoring-stats-backend-funcs-table). These access functions use the session's backend ID number, which is a small integer (\>= 0) that is distinct from the backend ID of any concurrent session, although a session's ID can be recycled as soon as it exits. The backend ID is used, among other things, to identify the session's temporary schema if it has one. The function `pg_stat_get_backend_idset` provides a convenient way to list all the active backends' ID numbers for invoking these functions. For example, to show the PIDs and current queries of all backends:

    SELECT pg_stat_get_backend_pid(backendid) AS pid,
           pg_stat_get_backend_activity(backendid) AS query
    FROM pg_stat_get_backend_idset() AS backendid;

<table id="monitoring-stats-backend-funcs-table">
<caption>Per-Backend Statistics Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_get_backend_activity</code> ( <code>integer</code> ) text</p>
<p>Returns the text of this backend's most recent query.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_get_backend_activity_start</code> ( <code>integer</code> ) timestamp with time zone</p>
<p>Returns the time when the backend's most recent query was started.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_get_backend_client_addr</code> ( <code>integer</code> ) inet</p>
<p>Returns the IP address of the client connected to this backend.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_get_backend_client_port</code> ( <code>integer</code> ) integer</p>
<p>Returns the TCP port number that the client is using for communication.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_get_backend_dbid</code> ( <code>integer</code> ) oid</p>
<p>Returns the OID of the database this backend is connected to.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_get_backend_idset</code> () setof integer</p>
<p>Returns the set of currently active backend ID numbers.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_get_backend_pid</code> ( <code>integer</code> ) integer</p>
<p>Returns the process ID of this backend.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_get_backend_start</code> ( <code>integer</code> ) timestamp with time zone</p>
<p>Returns the time when this process was started.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_get_backend_subxact</code> ( <code>integer</code> ) record</p>
<p>Returns a record of information about the subtransactions of the backend with the specified ID. The fields returned are <code>subxact_count</code>, which is the number of subtransactions in the backend's subtransaction cache, and <code>subxact_overflowed</code>, which indicates whether the backend's subtransaction cache is overflowed or not.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_get_backend_userid</code> ( <code>integer</code> ) oid</p>
<p>Returns the OID of the user logged into this backend.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_get_backend_wait_event</code> ( <code>integer</code> ) text</p>
<p>Returns the wait event name if this backend is currently waiting, otherwise NULL. See <a href="#wait-event-activity-table">???</a> through <a href="#wait-event-timeout-table">???</a>.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_get_backend_wait_event_type</code> ( <code>integer</code> ) text</p>
<p>Returns the wait event type name if this backend is currently waiting, otherwise NULL. See <a href="#wait-event-table">Wait Event Types</a> for details.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>pg_stat_get_backend_xact_start</code> ( <code>integer</code> ) timestamp with time zone</p>
<p>Returns the time when the backend's current transaction was started.</p></td>
</tr>
</tbody>
</table>

## Viewing Locks

lock

monitoring

Another useful tool for monitoring database activity is the pg_locks system table. It allows the database administrator to view information about the outstanding locks in the lock manager. For example, this capability can be used to:

- View all the locks currently outstanding, all the locks on relations in a particular database, all the locks on a particular relation, or all the locks held by a particular PostgreSQL session.

- Determine the relation in the current database with the most ungranted locks (which might be a source of contention among database clients).

- Determine the effect of lock contention on overall database performance, as well as the extent to which contention varies with overall database traffic.

Details of the pg_locks view appear in [???](#view-pg-locks). For more information on locking and managing concurrency with PostgreSQL, refer to [???](#mvcc).

## Progress Reporting

PostgreSQL has the ability to report the progress of certain commands during command execution. Currently, the only commands which support progress reporting are `ANALYZE`, `CLUSTER`, `CREATE INDEX`, `VACUUM`, `COPY`, and [???](#protocol-replication-base-backup) (i.e., replication command that [???](#app-pgbasebackup) issues to take a base backup). This may be expanded in the future.

### ANALYZE Progress Reporting

pg_stat_progress_analyze

Whenever `ANALYZE` is running, the pg_stat_progress_analyze view will contain a row for each backend that is currently running that command. The tables below describe the information that will be reported and provide information about how to interpret it.

<table id="pg-stat-progress-analyze-view">
<caption>pg_stat_progress_analyze View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">pid <code>integer</code></p>
<p>Process ID of backend.</p></td>
</tr>
<tr>
<td><p role="column_definition">datid <code>oid</code></p>
<p>OID of the database to which this backend is connected.</p></td>
</tr>
<tr>
<td><p role="column_definition">datname <code>name</code></p>
<p>Name of the database to which this backend is connected.</p></td>
</tr>
<tr>
<td><p role="column_definition">relid <code>oid</code></p>
<p>OID of the table being analyzed.</p></td>
</tr>
<tr>
<td><p role="column_definition">phase <code>text</code></p>
<p>Current processing phase. See <a href="#analyze-phases">ANALYZE Phases</a>.</p></td>
</tr>
<tr>
<td><p role="column_definition">sample_blks_total <code>bigint</code></p>
<p>Total number of heap blocks that will be sampled.</p></td>
</tr>
<tr>
<td><p role="column_definition">sample_blks_scanned <code>bigint</code></p>
<p>Number of heap blocks scanned.</p></td>
</tr>
<tr>
<td><p role="column_definition">ext_stats_total <code>bigint</code></p>
<p>Number of extended statistics.</p></td>
</tr>
<tr>
<td><p role="column_definition">ext_stats_computed <code>bigint</code></p>
<p>Number of extended statistics computed. This counter only advances when the phase is <code>computing extended statistics</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">child_tables_total <code>bigint</code></p>
<p>Number of child tables.</p></td>
</tr>
<tr>
<td><p role="column_definition">child_tables_done <code>bigint</code></p>
<p>Number of child tables scanned. This counter only advances when the phase is <code>acquiring inherited sample rows</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">current_child_table_relid <code>oid</code></p>
<p>OID of the child table currently being scanned. This field is only valid when the phase is <code>acquiring inherited sample rows</code>.</p></td>
</tr>
</tbody>
</table>

| Phase | Description |
|----|----|
| `initializing` | The command is preparing to begin scanning the heap. This phase is expected to be very brief. |
| `acquiring sample rows` | The command is currently scanning the table given by relid to obtain sample rows. |
| `acquiring inherited sample rows` | The command is currently scanning child tables to obtain sample rows. Columns child_tables_total, child_tables_done, and current_child_table_relid contain the progress information for this phase. |
| `computing statistics` | The command is computing statistics from the sample rows obtained during the table scan. |
| `computing extended statistics` | The command is computing extended statistics from the sample rows obtained during the table scan. |
| `finalizing analyze` | The command is updating pg_class. When this phase is completed, `ANALYZE` will end. |

ANALYZE Phases {#analyze-phases}

> [!NOTE]
> Note that when `ANALYZE` is run on a partitioned table, all of its partitions are also recursively analyzed. In that case, `ANALYZE` progress is reported first for the parent table, whereby its inheritance statistics are collected, followed by that for each partition.

### CLUSTER Progress Reporting

pg_stat_progress_cluster

Whenever `CLUSTER` or `VACUUM FULL` is running, the pg_stat_progress_cluster view will contain a row for each backend that is currently running either command. The tables below describe the information that will be reported and provide information about how to interpret it.

<table id="pg-stat-progress-cluster-view">
<caption>pg_stat_progress_cluster View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">pid <code>integer</code></p>
<p>Process ID of backend.</p></td>
</tr>
<tr>
<td><p role="column_definition">datid <code>oid</code></p>
<p>OID of the database to which this backend is connected.</p></td>
</tr>
<tr>
<td><p role="column_definition">datname <code>name</code></p>
<p>Name of the database to which this backend is connected.</p></td>
</tr>
<tr>
<td><p role="column_definition">relid <code>oid</code></p>
<p>OID of the table being clustered.</p></td>
</tr>
<tr>
<td><p role="column_definition">command <code>text</code></p>
<p>The command that is running. Either <code>CLUSTER</code> or <code>VACUUM FULL</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">phase <code>text</code></p>
<p>Current processing phase. See <a href="#cluster-phases">CLUSTER and VACUUM FULL Phases</a>.</p></td>
</tr>
<tr>
<td><p role="column_definition">cluster_index_relid <code>oid</code></p>
<p>If the table is being scanned using an index, this is the OID of the index being used; otherwise, it is zero.</p></td>
</tr>
<tr>
<td><p role="column_definition">heap_tuples_scanned <code>bigint</code></p>
<p>Number of heap tuples scanned. This counter only advances when the phase is <code>seq scanning heap</code>, <code>index scanning heap</code> or <code>writing new heap</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">heap_tuples_written <code>bigint</code></p>
<p>Number of heap tuples written. This counter only advances when the phase is <code>seq scanning heap</code>, <code>index scanning heap</code> or <code>writing new heap</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">heap_blks_total <code>bigint</code></p>
<p>Total number of heap blocks in the table. This number is reported as of the beginning of <code>seq scanning heap</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">heap_blks_scanned <code>bigint</code></p>
<p>Number of heap blocks scanned. This counter only advances when the phase is <code>seq scanning heap</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">index_rebuild_count <code>bigint</code></p>
<p>Number of indexes rebuilt. This counter only advances when the phase is <code>rebuilding index</code>.</p></td>
</tr>
</tbody>
</table>

| Phase | Description |
|----|----|
| `initializing` | The command is preparing to begin scanning the heap. This phase is expected to be very brief. |
| `seq scanning heap` | The command is currently scanning the table using a sequential scan. |
| `index scanning heap` | `CLUSTER` is currently scanning the table using an index scan. |
| `sorting tuples` | `CLUSTER` is currently sorting tuples. |
| `writing new heap` | `CLUSTER` is currently writing the new heap. |
| `swapping relation files` | The command is currently swapping newly-built files into place. |
| `rebuilding index` | The command is currently rebuilding an index. |
| `performing final cleanup` | The command is performing final cleanup. When this phase is completed, `CLUSTER` or `VACUUM FULL` will end. |

CLUSTER and VACUUM FULL Phases {#cluster-phases}

### COPY Progress Reporting

pg_stat_progress_copy

Whenever `COPY` is running, the pg_stat_progress_copy view will contain one row for each backend that is currently running a `COPY` command. The table below describes the information that will be reported and provides information about how to interpret it.

<table id="pg-stat-progress-copy-view">
<caption>pg_stat_progress_copy View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">pid <code>integer</code></p>
<p>Process ID of backend.</p></td>
</tr>
<tr>
<td><p role="column_definition">datid <code>oid</code></p>
<p>OID of the database to which this backend is connected.</p></td>
</tr>
<tr>
<td><p role="column_definition">datname <code>name</code></p>
<p>Name of the database to which this backend is connected.</p></td>
</tr>
<tr>
<td><p role="column_definition">relid <code>oid</code></p>
<p>OID of the table on which the <code>COPY</code> command is executed. It is set to <code>0</code> if copying from a <code>SELECT</code> query.</p></td>
</tr>
<tr>
<td><p role="column_definition">command <code>text</code></p>
<p>The command that is running: <code>COPY FROM</code>, or <code>COPY TO</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">type <code>text</code></p>
<p>The I/O type that the data is read from or written to: <code>FILE</code>, <code>PROGRAM</code>, <code>PIPE</code> (for <code>COPY FROM STDIN</code> and <code>COPY TO STDOUT</code>), or <code>CALLBACK</code> (used for example during the initial table synchronization in logical replication).</p></td>
</tr>
<tr>
<td><p role="column_definition">bytes_processed <code>bigint</code></p>
<p>Number of bytes already processed by <code>COPY</code> command.</p></td>
</tr>
<tr>
<td><p role="column_definition">bytes_total <code>bigint</code></p>
<p>Size of source file for <code>COPY FROM</code> command in bytes. It is set to <code>0</code> if not available.</p></td>
</tr>
<tr>
<td><p role="column_definition">tuples_processed <code>bigint</code></p>
<p>Number of tuples already processed by <code>COPY</code> command.</p></td>
</tr>
<tr>
<td><p role="column_definition">tuples_excluded <code>bigint</code></p>
<p>Number of tuples not processed because they were excluded by the <code>WHERE</code> clause of the <code>COPY</code> command.</p></td>
</tr>
<tr>
<td><p role="column_definition">tuples_skipped <code>bigint</code></p>
<p>Number of tuples skipped because they contain malformed data. This counter only advances when a value other than <code>stop</code> is specified to the <code>ON_ERROR</code> option.</p></td>
</tr>
</tbody>
</table>

### CREATE INDEX Progress Reporting

pg_stat_progress_create_index

Whenever `CREATE INDEX` or `REINDEX` is running, the pg_stat_progress_create_index view will contain one row for each backend that is currently creating indexes. The tables below describe the information that will be reported and provide information about how to interpret it.

<table id="pg-stat-progress-create-index-view">
<caption>pg_stat_progress_create_index View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">pid <code>integer</code></p>
<p>Process ID of the backend creating indexes.</p></td>
</tr>
<tr>
<td><p role="column_definition">datid <code>oid</code></p>
<p>OID of the database to which this backend is connected.</p></td>
</tr>
<tr>
<td><p role="column_definition">datname <code>name</code></p>
<p>Name of the database to which this backend is connected.</p></td>
</tr>
<tr>
<td><p role="column_definition">relid <code>oid</code></p>
<p>OID of the table on which the index is being created.</p></td>
</tr>
<tr>
<td><p role="column_definition">index_relid <code>oid</code></p>
<p>OID of the index being created or reindexed. During a non-concurrent <code>CREATE INDEX</code>, this is 0.</p></td>
</tr>
<tr>
<td><p role="column_definition">command <code>text</code></p>
<p>Specific command type: <code>CREATE INDEX</code>, <code>CREATE INDEX CONCURRENTLY</code>, <code>REINDEX</code>, or <code>REINDEX CONCURRENTLY</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">phase <code>text</code></p>
<p>Current processing phase of index creation. See <a href="#create-index-phases">CREATE INDEX Phases</a>.</p></td>
</tr>
<tr>
<td><p role="column_definition">lockers_total <code>bigint</code></p>
<p>Total number of lockers to wait for, when applicable.</p></td>
</tr>
<tr>
<td><p role="column_definition">lockers_done <code>bigint</code></p>
<p>Number of lockers already waited for.</p></td>
</tr>
<tr>
<td><p role="column_definition">current_locker_pid <code>bigint</code></p>
<p>Process ID of the locker currently being waited for.</p></td>
</tr>
<tr>
<td><p role="column_definition">blocks_total <code>bigint</code></p>
<p>Total number of blocks to be processed in the current phase.</p></td>
</tr>
<tr>
<td><p role="column_definition">blocks_done <code>bigint</code></p>
<p>Number of blocks already processed in the current phase.</p></td>
</tr>
<tr>
<td><p role="column_definition">tuples_total <code>bigint</code></p>
<p>Total number of tuples to be processed in the current phase.</p></td>
</tr>
<tr>
<td><p role="column_definition">tuples_done <code>bigint</code></p>
<p>Number of tuples already processed in the current phase.</p></td>
</tr>
<tr>
<td><p role="column_definition">partitions_total <code>bigint</code></p>
<p>Total number of partitions on which the index is to be created or attached, including both direct and indirect partitions. <code>0</code> during a <code>REINDEX</code>, or when the index is not partitioned.</p></td>
</tr>
<tr>
<td><p role="column_definition">partitions_done <code>bigint</code></p>
<p>Number of partitions on which the index has already been created or attached, including both direct and indirect partitions. <code>0</code> during a <code>REINDEX</code>, or when the index is not partitioned.</p></td>
</tr>
</tbody>
</table>

| Phase | Description |
|----|----|
| `initializing` | `CREATE INDEX` or `REINDEX` is preparing to create the index. This phase is expected to be very brief. |
| `waiting for writers before build` | `CREATE INDEX CONCURRENTLY` or `REINDEX CONCURRENTLY` is waiting for transactions with write locks that can potentially see the table to finish. This phase is skipped when not in concurrent mode. Columns lockers_total, lockers_done and current_locker_pid contain the progress information for this phase. |
| `building index` | The index is being built by the access method-specific code. In this phase, access methods that support progress reporting fill in their own progress data, and the subphase is indicated in this column. Typically, blocks_total and blocks_done will contain progress data, as well as potentially tuples_total and tuples_done. |
| `waiting for writers before validation` | `CREATE INDEX CONCURRENTLY` or `REINDEX CONCURRENTLY` is waiting for transactions with write locks that can potentially write into the table to finish. This phase is skipped when not in concurrent mode. Columns lockers_total, lockers_done and current_locker_pid contain the progress information for this phase. |
| `index validation: scanning index` | `CREATE INDEX CONCURRENTLY` is scanning the index searching for tuples that need to be validated. This phase is skipped when not in concurrent mode. Columns blocks_total (set to the total size of the index) and blocks_done contain the progress information for this phase. |
| `index validation: sorting tuples` | `CREATE INDEX CONCURRENTLY` is sorting the output of the index scanning phase. |
| `index validation: scanning table` | `CREATE INDEX CONCURRENTLY` is scanning the table to validate the index tuples collected in the previous two phases. This phase is skipped when not in concurrent mode. Columns blocks_total (set to the total size of the table) and blocks_done contain the progress information for this phase. |
| `waiting for old snapshots` | `CREATE INDEX CONCURRENTLY` or `REINDEX CONCURRENTLY` is waiting for transactions that can potentially see the table to release their snapshots. This phase is skipped when not in concurrent mode. Columns lockers_total, lockers_done and current_locker_pid contain the progress information for this phase. |
| `waiting for readers before marking dead` | `REINDEX CONCURRENTLY` is waiting for transactions with read locks on the table to finish, before marking the old index dead. This phase is skipped when not in concurrent mode. Columns lockers_total, lockers_done and current_locker_pid contain the progress information for this phase. |
| `waiting for readers before dropping` | `REINDEX CONCURRENTLY` is waiting for transactions with read locks on the table to finish, before dropping the old index. This phase is skipped when not in concurrent mode. Columns lockers_total, lockers_done and current_locker_pid contain the progress information for this phase. |

CREATE INDEX Phases {#create-index-phases}

### VACUUM Progress Reporting

pg_stat_progress_vacuum

Whenever `VACUUM` is running, the pg_stat_progress_vacuum view will contain one row for each backend (including autovacuum worker processes) that is currently vacuuming. The tables below describe the information that will be reported and provide information about how to interpret it. Progress for `VACUUM FULL` commands is reported via pg_stat_progress_cluster because both `VACUUM FULL` and `CLUSTER` rewrite the table, while regular `VACUUM` only modifies it in place. See [CLUSTER Progress Reporting](#cluster-progress-reporting).

<table id="pg-stat-progress-vacuum-view">
<caption>pg_stat_progress_vacuum View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">pid <code>integer</code></p>
<p>Process ID of backend.</p></td>
</tr>
<tr>
<td><p role="column_definition">datid <code>oid</code></p>
<p>OID of the database to which this backend is connected.</p></td>
</tr>
<tr>
<td><p role="column_definition">datname <code>name</code></p>
<p>Name of the database to which this backend is connected.</p></td>
</tr>
<tr>
<td><p role="column_definition">relid <code>oid</code></p>
<p>OID of the table being vacuumed.</p></td>
</tr>
<tr>
<td><p role="column_definition">phase <code>text</code></p>
<p>Current processing phase of vacuum. See <a href="#vacuum-phases">VACUUM Phases</a>.</p></td>
</tr>
<tr>
<td><p role="column_definition">heap_blks_total <code>bigint</code></p>
<p>Total number of heap blocks in the table. This number is reported as of the beginning of the scan; blocks added later will not be (and need not be) visited by this <code>VACUUM</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">heap_blks_scanned <code>bigint</code></p>
<p>Number of heap blocks scanned. Because the <a href="#storage-vm">visibility map</a> is used to optimize scans, some blocks will be skipped without inspection; skipped blocks are included in this total, so that this number will eventually become equal to heap_blks_total when the vacuum is complete. This counter only advances when the phase is <code>scanning heap</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">heap_blks_vacuumed <code>bigint</code></p>
<p>Number of heap blocks vacuumed. Unless the table has no indexes, this counter only advances when the phase is <code>vacuuming heap</code>. Blocks that contain no dead tuples are skipped, so the counter may sometimes skip forward in large increments.</p></td>
</tr>
<tr>
<td><p role="column_definition">index_vacuum_count <code>bigint</code></p>
<p>Number of completed index vacuum cycles.</p></td>
</tr>
<tr>
<td><p role="column_definition">max_dead_tuple_bytes <code>bigint</code></p>
<p>Amount of dead tuple data that we can store before needing to perform an index vacuum cycle, based on <a href="#guc-maintenance-work-mem">???</a>.</p></td>
</tr>
<tr>
<td><p role="column_definition">dead_tuple_bytes <code>bigint</code></p>
<p>Amount of dead tuple data collected since the last index vacuum cycle.</p></td>
</tr>
<tr>
<td><p role="column_definition">num_dead_item_ids <code>bigint</code></p>
<p>Number of dead item identifiers collected since the last index vacuum cycle.</p></td>
</tr>
<tr>
<td><p role="column_definition">indexes_total <code>bigint</code></p>
<p>Total number of indexes that will be vacuumed or cleaned up. This number is reported at the beginning of the <code>vacuuming indexes</code> phase or the <code>cleaning up indexes</code> phase.</p></td>
</tr>
<tr>
<td><p role="column_definition">indexes_processed <code>bigint</code></p>
<p>Number of indexes processed. This counter only advances when the phase is <code>vacuuming indexes</code> or <code>cleaning up indexes</code>.</p></td>
</tr>
</tbody>
</table>

| Phase | Description |
|----|----|
| `initializing` | `VACUUM` is preparing to begin scanning the heap. This phase is expected to be very brief. |
| `scanning heap` | `VACUUM` is currently scanning the heap. It will prune and defragment each page if required, and possibly perform freezing activity. The heap_blks_scanned column can be used to monitor the progress of the scan. |
| `vacuuming indexes` | `VACUUM` is currently vacuuming the indexes. If a table has any indexes, this will happen at least once per vacuum, after the heap has been completely scanned. It may happen multiple times per vacuum if [???](#guc-maintenance-work-mem) (or, in the case of autovacuum, [???](#guc-autovacuum-work-mem) if set) is insufficient to store the number of dead tuples found. |
| `vacuuming heap` | `VACUUM` is currently vacuuming the heap. Vacuuming the heap is distinct from scanning the heap, and occurs after each instance of vacuuming indexes. If heap_blks_scanned is less than heap_blks_total, the system will return to scanning the heap after this phase is completed; otherwise, it will begin cleaning up indexes after this phase is completed. |
| `cleaning up indexes` | `VACUUM` is currently cleaning up indexes. This occurs after the heap has been completely scanned and all vacuuming of the indexes and the heap has been completed. |
| `truncating heap` | `VACUUM` is currently truncating the heap so as to return empty pages at the end of the relation to the operating system. This occurs after cleaning up indexes. |
| `performing final cleanup` | `VACUUM` is performing final cleanup. During this phase, `VACUUM` will vacuum the free space map, update statistics in `pg_class`, and report statistics to the cumulative statistics system. When this phase is completed, `VACUUM` will end. |

VACUUM Phases {#vacuum-phases}

### Base Backup Progress Reporting

pg_stat_progress_basebackup

Whenever an application like pg_basebackup is taking a base backup, the pg_stat_progress_basebackup view will contain a row for each WAL sender process that is currently running the `BASE_BACKUP` replication command and streaming the backup. The tables below describe the information that will be reported and provide information about how to interpret it.

<table id="pg-stat-progress-basebackup-view">
<caption>pg_stat_progress_basebackup View</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">pid <code>integer</code></p>
<p>Process ID of a WAL sender process.</p></td>
</tr>
<tr>
<td><p role="column_definition">phase <code>text</code></p>
<p>Current processing phase. See <a href="#basebackup-phases">Base Backup Phases</a>.</p></td>
</tr>
<tr>
<td><p role="column_definition">backup_total <code>bigint</code></p>
<p>Total amount of data that will be streamed. This is estimated and reported as of the beginning of <code>streaming database files</code> phase. Note that this is only an approximation since the database may change during <code>streaming database files</code> phase and WAL log may be included in the backup later. This is always the same value as backup_streamed once the amount of data streamed exceeds the estimated total size. If the estimation is disabled in pg_basebackup (i.e., <code>--no-estimate-size</code> option is specified), this is <code>NULL</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">backup_streamed <code>bigint</code></p>
<p>Amount of data streamed. This counter only advances when the phase is <code>streaming database files</code> or <code>transferring wal files</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">tablespaces_total <code>bigint</code></p>
<p>Total number of tablespaces that will be streamed.</p></td>
</tr>
<tr>
<td><p role="column_definition">tablespaces_streamed <code>bigint</code></p>
<p>Number of tablespaces streamed. This counter only advances when the phase is <code>streaming database files</code>.</p></td>
</tr>
</tbody>
</table>

| Phase | Description |
|----|----|
| `initializing` | The WAL sender process is preparing to begin the backup. This phase is expected to be very brief. |
| `waiting for checkpoint to finish` | The WAL sender process is currently performing `pg_backup_start` to prepare to take a base backup, and waiting for the start-of-backup checkpoint to finish. |
| `estimating backup size` | The WAL sender process is currently estimating the total amount of database files that will be streamed as a base backup. |
| `streaming database files` | The WAL sender process is currently streaming database files as a base backup. |
| `waiting for wal archiving to finish` | The WAL sender process is currently performing `pg_backup_stop` to finish the backup, and waiting for all the WAL files required for the base backup to be successfully archived. If either `--wal-method=none` or `--wal-method=stream` is specified in pg_basebackup, the backup will end when this phase is completed. |
| `transferring wal files` | The WAL sender process is currently transferring all WAL logs generated during the backup. This phase occurs after `waiting for wal archiving to finish` phase if `--wal-method=fetch` is specified in pg_basebackup. The backup will end when this phase is completed. |

Base Backup Phases {#basebackup-phases}

## Dynamic Tracing

DTrace

PostgreSQL provides facilities to support dynamic tracing of the database server. This allows an external utility to be called at specific points in the code and thereby trace execution.

A number of probes or trace points are already inserted into the source code. These probes are intended to be used by database developers and administrators. By default the probes are not compiled into PostgreSQL; the user needs to explicitly tell the configure script to make the probes available.

Currently, the [DTrace](https://en.wikipedia.org/wiki/DTrace) utility is supported, which, at the time of this writing, is available on Solaris, macOS, FreeBSD, NetBSD, and Oracle Linux. The [SystemTap](https://sourceware.org/systemtap/) project for Linux provides a DTrace equivalent and can also be used. Supporting other dynamic tracing utilities is theoretically possible by changing the definitions for the macros in `src/include/utils/probes.h`.

### Compiling for Dynamic Tracing

By default, probes are not available, so you will need to explicitly tell the configure script to make the probes available in PostgreSQL. To include DTrace support specify `--enable-dtrace` to configure. See [???](#configure-options-devel) for further information.

### Built-in Probes

A number of standard probes are provided in the source code, as shown in [Built-in DTrace Probes](#dtrace-probe-point-table); [Defined Types Used in Probe Parameters](#typedefs-table) shows the types used in the probes. More probes can certainly be added to enhance PostgreSQL's observability.

| Name | Parameters | Description |
|----|----|----|
| `transaction-start` | `(LocalTransactionId)` | Probe that fires at the start of a new transaction. arg0 is the transaction ID. |
| `transaction-commit` | `(LocalTransactionId)` | Probe that fires when a transaction completes successfully. arg0 is the transaction ID. |
| `transaction-abort` | `(LocalTransactionId)` | Probe that fires when a transaction completes unsuccessfully. arg0 is the transaction ID. |
| `query-start` | `(const char *)` | Probe that fires when the processing of a query is started. arg0 is the query string. |
| `query-done` | `(const char *)` | Probe that fires when the processing of a query is complete. arg0 is the query string. |
| `query-parse-start` | `(const char *)` | Probe that fires when the parsing of a query is started. arg0 is the query string. |
| `query-parse-done` | `(const char *)` | Probe that fires when the parsing of a query is complete. arg0 is the query string. |
| `query-rewrite-start` | `(const char *)` | Probe that fires when the rewriting of a query is started. arg0 is the query string. |
| `query-rewrite-done` | `(const char *)` | Probe that fires when the rewriting of a query is complete. arg0 is the query string. |
| `query-plan-start` | `()` | Probe that fires when the planning of a query is started. |
| `query-plan-done` | `()` | Probe that fires when the planning of a query is complete. |
| `query-execute-start` | `()` | Probe that fires when the execution of a query is started. |
| `query-execute-done` | `()` | Probe that fires when the execution of a query is complete. |
| `statement-status` | `(const char *)` | Probe that fires anytime the server process updates its pg_stat_activity.status. arg0 is the new status string. |
| `checkpoint-start` | `(int)` | Probe that fires when a checkpoint is started. arg0 holds the bitwise flags used to distinguish different checkpoint types, such as shutdown, immediate or force. |
| `checkpoint-done` | `(int, int, int, int, int)` | Probe that fires when a checkpoint is complete. (The probes listed next fire in sequence during checkpoint processing.) arg0 is the number of buffers written. arg1 is the total number of buffers. arg2, arg3 and arg4 contain the number of WAL files added, removed and recycled respectively. |
| `clog-checkpoint-start` | `(bool)` | Probe that fires when the CLOG portion of a checkpoint is started. arg0 is true for normal checkpoint, false for shutdown checkpoint. |
| `clog-checkpoint-done` | `(bool)` | Probe that fires when the CLOG portion of a checkpoint is complete. arg0 has the same meaning as for `clog-checkpoint-start`. |
| `subtrans-checkpoint-start` | `(bool)` | Probe that fires when the SUBTRANS portion of a checkpoint is started. arg0 is true for normal checkpoint, false for shutdown checkpoint. |
| `subtrans-checkpoint-done` | `(bool)` | Probe that fires when the SUBTRANS portion of a checkpoint is complete. arg0 has the same meaning as for `subtrans-checkpoint-start`. |
| `multixact-checkpoint-start` | `(bool)` | Probe that fires when the MultiXact portion of a checkpoint is started. arg0 is true for normal checkpoint, false for shutdown checkpoint. |
| `multixact-checkpoint-done` | `(bool)` | Probe that fires when the MultiXact portion of a checkpoint is complete. arg0 has the same meaning as for `multixact-checkpoint-start`. |
| `buffer-checkpoint-start` | `(int)` | Probe that fires when the buffer-writing portion of a checkpoint is started. arg0 holds the bitwise flags used to distinguish different checkpoint types, such as shutdown, immediate or force. |
| `buffer-sync-start` | `(int, int)` | Probe that fires when we begin to write dirty buffers during checkpoint (after identifying which buffers must be written). arg0 is the total number of buffers. arg1 is the number that are currently dirty and need to be written. |
| `buffer-sync-written` | `(int)` | Probe that fires after each buffer is written during checkpoint. arg0 is the ID number of the buffer. |
| `buffer-sync-done` | `(int, int, int)` | Probe that fires when all dirty buffers have been written. arg0 is the total number of buffers. arg1 is the number of buffers actually written by the checkpoint process. arg2 is the number that were expected to be written (arg1 of `buffer-sync-start`); any difference reflects other processes flushing buffers during the checkpoint. |
| `buffer-checkpoint-sync-start` | `()` | Probe that fires after dirty buffers have been written to the kernel, and before starting to issue fsync requests. |
| `buffer-checkpoint-done` | `()` | Probe that fires when syncing of buffers to disk is complete. |
| `twophase-checkpoint-start` | `()` | Probe that fires when the two-phase portion of a checkpoint is started. |
| `twophase-checkpoint-done` | `()` | Probe that fires when the two-phase portion of a checkpoint is complete. |
| `buffer-extend-start` | `(ForkNumber, BlockNumber, Oid, Oid, Oid, int, unsigned int)` | Probe that fires when a relation extension starts. arg0 contains the fork to be extended. arg1, arg2, and arg3 contain the tablespace, database, and relation OIDs identifying the relation. arg4 is the ID of the backend which created the temporary relation for a local buffer, or `INVALID_PROC_NUMBER` (-1) for a shared buffer. arg5 is the number of blocks the caller would like to extend by. |
| `buffer-extend-done` | `(ForkNumber, BlockNumber, Oid, Oid, Oid, int, unsigned int, BlockNumber)` | Probe that fires when a relation extension is complete. arg0 contains the fork to be extended. arg1, arg2, and arg3 contain the tablespace, database, and relation OIDs identifying the relation. arg4 is the ID of the backend which created the temporary relation for a local buffer, or `INVALID_PROC_NUMBER` (-1) for a shared buffer. arg5 is the number of blocks the relation was extended by, this can be less than the number in the `buffer-extend-start` due to resource constraints. arg6 contains the BlockNumber of the first new block. |
| `buffer-read-start` | `(ForkNumber, BlockNumber, Oid, Oid, Oid, int)` | Probe that fires when a buffer read is started. arg0 and arg1 contain the fork and block numbers of the page. arg2, arg3, and arg4 contain the tablespace, database, and relation OIDs identifying the relation. arg5 is the ID of the backend which created the temporary relation for a local buffer, or `INVALID_PROC_NUMBER` (-1) for a shared buffer. |
| `buffer-read-done` | `(ForkNumber, BlockNumber, Oid, Oid, Oid, int, bool)` | Probe that fires when a buffer read is complete. arg0 and arg1 contain the fork and block numbers of the page. arg2, arg3, and arg4 contain the tablespace, database, and relation OIDs identifying the relation. arg5 is the ID of the backend which created the temporary relation for a local buffer, or `INVALID_PROC_NUMBER` (-1) for a shared buffer. arg6 is true if the buffer was found in the pool, false if not. |
| `buffer-flush-start` | `(ForkNumber, BlockNumber, Oid, Oid, Oid)` | Probe that fires before issuing any write request for a shared buffer. arg0 and arg1 contain the fork and block numbers of the page. arg2, arg3, and arg4 contain the tablespace, database, and relation OIDs identifying the relation. |
| `buffer-flush-done` | `(ForkNumber, BlockNumber, Oid, Oid, Oid)` | Probe that fires when a write request is complete. (Note that this just reflects the time to pass the data to the kernel; it's typically not actually been written to disk yet.) The arguments are the same as for `buffer-flush-start`. |
| `wal-buffer-write-dirty-start` | `()` | Probe that fires when a server process begins to write a dirty WAL buffer because no more WAL buffer space is available. (If this happens often, it implies that [???](#guc-wal-buffers) is too small.) |
| `wal-buffer-write-dirty-done` | `()` | Probe that fires when a dirty WAL buffer write is complete. |
| `wal-insert` | `(unsigned char, unsigned char)` | Probe that fires when a WAL record is inserted. arg0 is the resource manager (rmid) for the record. arg1 contains the info flags. |
| `wal-switch` | `()` | Probe that fires when a WAL segment switch is requested. |
| `smgr-md-read-start` | `(ForkNumber, BlockNumber, Oid, Oid, Oid, int)` | Probe that fires when beginning to read a block from a relation. arg0 and arg1 contain the fork and block numbers of the page. arg2, arg3, and arg4 contain the tablespace, database, and relation OIDs identifying the relation. arg5 is the ID of the backend which created the temporary relation for a local buffer, or `INVALID_PROC_NUMBER` (-1) for a shared buffer. |
| `smgr-md-read-done` | `(ForkNumber, BlockNumber, Oid, Oid, Oid, int, int, int)` | Probe that fires when a block read is complete. arg0 and arg1 contain the fork and block numbers of the page. arg2, arg3, and arg4 contain the tablespace, database, and relation OIDs identifying the relation. arg5 is the ID of the backend which created the temporary relation for a local buffer, or `INVALID_PROC_NUMBER` (-1) for a shared buffer. arg6 is the number of bytes actually read, while arg7 is the number requested (if these are different it indicates a short read). |
| `smgr-md-write-start` | `(ForkNumber, BlockNumber, Oid, Oid, Oid, int)` | Probe that fires when beginning to write a block to a relation. arg0 and arg1 contain the fork and block numbers of the page. arg2, arg3, and arg4 contain the tablespace, database, and relation OIDs identifying the relation. arg5 is the ID of the backend which created the temporary relation for a local buffer, or `INVALID_PROC_NUMBER` (-1) for a shared buffer. |
| `smgr-md-write-done` | `(ForkNumber, BlockNumber, Oid, Oid, Oid, int, int, int)` | Probe that fires when a block write is complete. arg0 and arg1 contain the fork and block numbers of the page. arg2, arg3, and arg4 contain the tablespace, database, and relation OIDs identifying the relation. arg5 is the ID of the backend which created the temporary relation for a local buffer, or `INVALID_PROC_NUMBER` (-1) for a shared buffer. arg6 is the number of bytes actually written, while arg7 is the number requested (if these are different it indicates a short write). |
| `sort-start` | `(int, bool, int, int, bool, int)` | Probe that fires when a sort operation is started. arg0 indicates heap, index or datum sort. arg1 is true for unique-value enforcement. arg2 is the number of key columns. arg3 is the number of kilobytes of work memory allowed. arg4 is true if random access to the sort result is required. arg5 indicates serial when `0`, parallel worker when `1`, or parallel leader when `2`. |
| `sort-done` | `(bool, long)` | Probe that fires when a sort is complete. arg0 is true for external sort, false for internal sort. arg1 is the number of disk blocks used for an external sort, or kilobytes of memory used for an internal sort. |
| `lwlock-acquire` | `(char *, LWLockMode)` | Probe that fires when an LWLock has been acquired. arg0 is the LWLock's tranche. arg1 is the requested lock mode, either exclusive or shared. |
| `lwlock-release` | `(char *)` | Probe that fires when an LWLock has been released (but note that any released waiters have not yet been awakened). arg0 is the LWLock's tranche. |
| `lwlock-wait-start` | `(char *, LWLockMode)` | Probe that fires when an LWLock was not immediately available and a server process has begun to wait for the lock to become available. arg0 is the LWLock's tranche. arg1 is the requested lock mode, either exclusive or shared. |
| `lwlock-wait-done` | `(char *, LWLockMode)` | Probe that fires when a server process has been released from its wait for an LWLock (it does not actually have the lock yet). arg0 is the LWLock's tranche. arg1 is the requested lock mode, either exclusive or shared. |
| `lwlock-condacquire` | `(char *, LWLockMode)` | Probe that fires when an LWLock was successfully acquired when the caller specified no waiting. arg0 is the LWLock's tranche. arg1 is the requested lock mode, either exclusive or shared. |
| `lwlock-condacquire-fail` | `(char *, LWLockMode)` | Probe that fires when an LWLock was not successfully acquired when the caller specified no waiting. arg0 is the LWLock's tranche. arg1 is the requested lock mode, either exclusive or shared. |
| `lock-wait-start` | `(unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, LOCKMODE)` | Probe that fires when a request for a heavyweight lock (lmgr lock) has begun to wait because the lock is not available. arg0 through arg3 are the tag fields identifying the object being locked. arg4 indicates the type of object being locked. arg5 indicates the lock type being requested. |
| `lock-wait-done` | `(unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, LOCKMODE)` | Probe that fires when a request for a heavyweight lock (lmgr lock) has finished waiting (i.e., has acquired the lock). The arguments are the same as for `lock-wait-start`. |
| `deadlock-found` | `()` | Probe that fires when a deadlock is found by the deadlock detector. |

Built-in DTrace Probes {#dtrace-probe-point-table}

| Type                 | Definition      |
|----------------------|-----------------|
| `LocalTransactionId` | `unsigned int`  |
| `LWLockMode`         | `int`           |
| `LOCKMODE`           | `int`           |
| `BlockNumber`        | `unsigned int`  |
| `Oid`                | `unsigned int`  |
| `ForkNumber`         | `int`           |
| `bool`               | `unsigned char` |

Defined Types Used in Probe Parameters {#typedefs-table}

### Using Probes

The example below shows a DTrace script for analyzing transaction counts in the system, as an alternative to snapshotting pg_stat_database before and after a performance test:

    #!/usr/sbin/dtrace -qs

    postgresql$1:::transaction-start
    {
          @start["Start"] = count();
          self->ts  = timestamp;
    }

    postgresql$1:::transaction-abort
    {
          @abort["Abort"] = count();
    }

    postgresql$1:::transaction-commit
    /self->ts/
    {
          @commit["Commit"] = count();
          @time["Total time (ns)"] = sum(timestamp - self->ts);
          self->ts=0;
    }

When executed, the example D script gives output such as:

    # ./txn_count.d `pgrep -n postgres` or ./txn_count.d <PID>
    ^C

    Start                                          71
    Commit                                         70
    Total time (ns)                        2312105013

> [!NOTE]
> SystemTap uses a different notation for trace scripts than DTrace does, even though the underlying trace points are compatible. One point worth noting is that at this writing, SystemTap scripts must reference probe names using double underscores in place of hyphens. This is expected to be fixed in future SystemTap releases.

You should remember that DTrace scripts need to be carefully written and debugged, otherwise the trace information collected might be meaningless. In most cases where problems are found it is the instrumentation that is at fault, not the underlying system. When discussing information found using dynamic tracing, be sure to enclose the script used to allow that too to be checked and discussed.

### Defining New Probes

New probes can be defined within the code wherever the developer desires, though this will require a recompilation. Below are the steps for inserting new probes:

1.  Decide on probe names and data to be made available through the probes

2.  Add the probe definitions to `src/backend/utils/probes.d`

3.  Include `pg_trace.h` if it is not already present in the module(s) containing the probe points, and insert `TRACE_POSTGRESQL` probe macros at the desired locations in the source code

4.  Recompile and verify that the new probes are available

Example:

Here is an example of how you would add a probe to trace all new transactions by transaction ID.

1.  Decide that the probe will be named `transaction-start` and requires a parameter of type `LocalTransactionId`

2.  Add the probe definition to `src/backend/utils/probes.d`:

        probe transaction__start(LocalTransactionId);

    Note the use of the double underline in the probe name. In a DTrace script using the probe, the double underline needs to be replaced with a hyphen, so `transaction-start` is the name to document for users.

3.  At compile time, `transaction__start` is converted to a macro called `TRACE_POSTGRESQL_TRANSACTION_START` (notice the underscores are single here), which is available by including `pg_trace.h`. Add the macro call to the appropriate location in the source code. In this case, it looks like the following:

        TRACE_POSTGRESQL_TRANSACTION_START(vxid.localTransactionId);

4.  After recompiling and running the new binary, check that your newly added probe is available by executing the following DTrace command. You should see similar output:

        # dtrace -ln transaction-start
           ID    PROVIDER          MODULE           FUNCTION NAME
        18705 postgresql49878     postgres     StartTransactionCommand transaction-start
        18755 postgresql49877     postgres     StartTransactionCommand transaction-start
        18805 postgresql49876     postgres     StartTransactionCommand transaction-start
        18855 postgresql49875     postgres     StartTransactionCommand transaction-start
        18986 postgresql49873     postgres     StartTransactionCommand transaction-start

There are a few things to be careful about when adding trace macros to the C code:

- You should take care that the data types specified for a probe's parameters match the data types of the variables used in the macro. Otherwise, you will get compilation errors.

- On most platforms, if PostgreSQL is built with `--enable-dtrace`, the arguments to a trace macro will be evaluated whenever control passes through the macro, *even if no tracing is being done*. This is usually not worth worrying about if you are just reporting the values of a few local variables. But beware of putting expensive function calls into the arguments. If you need to do that, consider protecting the macro with a check to see if the trace is actually enabled:

      if (TRACE_POSTGRESQL_TRANSACTION_START_ENABLED())
          TRACE_POSTGRESQL_TRANSACTION_START(some_function(...));

  Each trace macro has a corresponding `ENABLED` macro.

## Monitoring Disk Usage

This section discusses how to monitor the disk usage of a PostgreSQL database system.

### Determining Disk Usage

disk usage

Each table has a primary heap disk file where most of the data is stored. If the table has any columns with potentially-wide values, there also might be a TOAST file associated with the table, which is used to store values too wide to fit comfortably in the main table (see [???](#storage-toast)). There will be one valid index on the TOAST table, if present. There also might be indexes associated with the base table. Each table and index is stored in a separate disk file possibly more than one file, if the file would exceed one gigabyte. Naming conventions for these files are described in [???](#storage-file-layout).

You can monitor disk space in three ways: using the SQL functions listed in [???](#functions-admin-dbsize), using the [???](#oid2name) module, or using manual inspection of the system catalogs. The SQL functions are the easiest to use and are generally recommended. The remainder of this section shows how to do it by inspection of the system catalogs.

Using psql on a recently vacuumed or analyzed database, you can issue queries to see the disk usage of any table:

    SELECT pg_relation_filepath(oid), relpages FROM pg_class WHERE relname = 'customer';

     pg_relation_filepath | relpages
    ----------------------+----------
     base/16384/16806     |       60
    (1 row)

Each page is typically 8 kilobytes. (Remember, relpages is only updated by `VACUUM`, `ANALYZE`, and a few DDL commands such as `CREATE INDEX`.) The file path name is of interest if you want to examine the table's disk file directly.

To show the space used by TOAST tables, use a query like the following:

    SELECT relname, relpages
    FROM pg_class,
         (SELECT reltoastrelid
          FROM pg_class
          WHERE relname = 'customer') AS ss
    WHERE oid = ss.reltoastrelid OR
          oid = (SELECT indexrelid
                 FROM pg_index
                 WHERE indrelid = ss.reltoastrelid)
    ORDER BY relname;

           relname        | relpages
    ----------------------+----------
     pg_toast_16806       |        0
     pg_toast_16806_index |        1

You can easily display index sizes, too:

    SELECT c2.relname, c2.relpages
    FROM pg_class c, pg_class c2, pg_index i
    WHERE c.relname = 'customer' AND
          c.oid = i.indrelid AND
          c2.oid = i.indexrelid
    ORDER BY c2.relname;

          relname      | relpages
    -------------------+----------
     customer_id_index |       26

It is easy to find your largest tables and indexes using this information:

    SELECT relname, relpages
    FROM pg_class
    ORDER BY relpages DESC;

           relname        | relpages
    ----------------------+----------
     bigtable             |     3290
     customer             |     3144

### Disk Full Failure

The most important disk monitoring task of a database administrator is to make sure the disk doesn't become full. A filled data disk will not result in data corruption, but it might prevent useful activity from occurring. If the disk holding the WAL files grows full, database server panic and consequent shutdown might occur.

If you cannot free up additional space on the disk by deleting other things, you can move some of the database files to other file systems by making use of tablespaces. See [???](#manage-ag-tablespaces) for more information about that.

> [!TIP]
> Some file systems perform badly when they are almost full, so do not wait until the disk is completely full to take action.

If your system supports per-user disk quotas, then the database will naturally be subject to whatever quota is placed on the user the server runs as. Exceeding the quota will have the same bad effects as running out of disk space entirely.
