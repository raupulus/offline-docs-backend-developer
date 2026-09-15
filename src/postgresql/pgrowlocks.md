---
title: pgrowlocks — show a table's row locking information
source_url: https://www.postgresql.org/docs/17/pgrowlocks.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: pgrowlocks.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 1040
---

## pgrowlocks show a table's row locking information

pgrowlocks

The `pgrowlocks` module provides a function to show row locking information for a specified table.

By default use is restricted to superusers, roles with privileges of the `pg_stat_scan_tables` role, and users with `SELECT` permissions on the table.

## Overview

pgrowlocks

pgrowlocks(text) returns setof record

The parameter is the name of a table. The result is a set of records, with one row for each locked row within the table. The output columns are shown in [ Output Columns](#pgrowlocks-columns).

| Name | Type | Description |
|----|----|----|
| locked_row | `tid` | Tuple ID (TID) of locked row |
| locker | `xid` | Transaction ID of locker, or multixact ID if multitransaction; see [???](#transaction-id) |
| multi | `boolean` | True if locker is a multitransaction |
| xids | `xid[]` | Transaction IDs of lockers (more than one if multitransaction) |
| modes | `text[]` | Lock mode of lockers (more than one if multitransaction), an array of `For Key Share`, `For Share`, `For No Key Update`, `No Key Update`, `For Update`, `Update`. |
| pids | `integer[]` | Process IDs of locking backends (more than one if multitransaction) |

`pgrowlocks` Output Columns {#pgrowlocks-columns}

`pgrowlocks` takes `AccessShareLock` for the target table and reads each row one by one to collect the row locking information. This is not very speedy for a large table. Note that:

1.  If an `ACCESS EXCLUSIVE` lock is taken on the table, `pgrowlocks` will be blocked.

2.  `pgrowlocks` is not guaranteed to produce a self-consistent snapshot. It is possible that a new row lock is taken, or an old lock is freed, during its execution.

`pgrowlocks` does not show the contents of locked rows. If you want to take a look at the row contents at the same time, you could do something like this:

    SELECT * FROM accounts AS a, pgrowlocks('accounts') AS p
      WHERE p.locked_row = a.ctid;

Be aware however that such a query will be very inefficient.

## Sample Output

    =# SELECT * FROM pgrowlocks('t1');
     locked_row | locker | multi | xids  |     modes      |  pids
    ------------+--------+-------+-------+----------------+--------
     (0,1)      |    609 | f     | {609} | {"For Share"}  | {3161}
     (0,2)      |    609 | f     | {609} | {"For Share"}  | {3161}
     (0,3)      |    607 | f     | {607} | {"For Update"} | {3107}
     (0,4)      |    607 | f     | {607} | {"For Update"} | {3107}
    (4 rows)

## Author

Tatsuo Ishii
