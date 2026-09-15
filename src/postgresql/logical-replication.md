---
title: Logical Replication
source_url: https://www.postgresql.org/docs/17/logical-replication.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: logical-replication.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 860
---

## Logical Replication

Logical replication is a method of replicating data objects and their changes, based upon their replication identity (usually a primary key). We use the term logical in contrast to physical replication, which uses exact block addresses and byte-by-byte replication. PostgreSQL supports both mechanisms concurrently, see [???](#high-availability). Logical replication allows fine-grained control over both data replication and security.

Logical replication uses a publish and subscribe model with one or more subscribers subscribing to one or more publications on a publisher node. Subscribers pull data from the publications they subscribe to and may subsequently re-publish data to allow cascading replication or more complex configurations.

Logical replication of a table typically starts with taking a snapshot of the data on the publisher database and copying that to the subscriber. Once that is done, the changes on the publisher are sent to the subscriber as they occur in real-time. The subscriber applies the data in the same order as the publisher so that transactional consistency is guaranteed for publications within a single subscription. This method of data replication is sometimes referred to as transactional replication.

The typical use-cases for logical replication are:

- Sending incremental changes in a single database or a subset of a database to subscribers as they occur.

- Firing triggers for individual changes as they arrive on the subscriber.

- Consolidating multiple databases into a single one (for example for analytical purposes).

- Replicating between different major versions of PostgreSQL.

- Replicating between PostgreSQL instances on different platforms (for example Linux to Windows).

- Giving access to replicated data to different groups of users.

- Sharing a subset of the database between multiple databases.

The subscriber database behaves in the same way as any other PostgreSQL instance and can be used as a publisher for other databases by defining its own publications. When the subscriber is treated as read-only by an application, there will be no conflicts from a single subscription. On the other hand, if there are other writes done either by an application or by other subscribers to the same set of tables, conflicts can arise.

## Publication

A publication can be defined on any physical replication primary. The node where a publication is defined is referred to as publisher. A publication is a set of changes generated from a table or a group of tables, and might also be described as a change set or replication set. Each publication exists in only one database.

Publications are different from schemas and do not affect how the table is accessed. Each table can be added to multiple publications if needed. Publications may currently only contain tables and all tables in schema. Objects must be added explicitly, except when a publication is created for `ALL TABLES`.

Publications can choose to limit the changes they produce to any combination of `INSERT`, `UPDATE`, `DELETE`, and `TRUNCATE`, similar to how triggers are fired by particular event types. By default, all operation types are replicated. These publication specifications apply only for DML operations; they do not affect the initial data synchronization copy. (Row filters have no effect for `TRUNCATE`. See [Row Filters](#logical-replication-row-filter)).

A published table must have a replica identity configured in order to be able to replicate `UPDATE` and `DELETE` operations, so that appropriate rows to update or delete can be identified on the subscriber side. By default, this is the primary key, if there is one. Another unique index (with certain additional requirements) can also be set to be the replica identity. If the table does not have any suitable key, then it can be set to replica identity `FULL`, which means the entire row becomes the key. When replica identity `FULL` is specified, indexes can be used on the subscriber side for searching the rows. Candidate indexes must be btree or hash, non-partial, and the leftmost index field must be a column (not an expression) that references the published table column. These restrictions on the non-unique index properties adhere to some of the restrictions that are enforced for primary keys. If there are no such suitable indexes, the search on the subscriber side can be very inefficient, therefore replica identity `FULL` should only be used as a fallback if no other solution is possible. If a replica identity other than `FULL` is set on the publisher side, a replica identity comprising the same or fewer columns must also be set on the subscriber side. See [???](#sql-altertable-replica-identity) for details on how to set the replica identity. If a table without a replica identity is added to a publication that replicates `UPDATE` or `DELETE` operations then subsequent `UPDATE` or `DELETE` operations will cause an error on the publisher. `INSERT` operations can proceed regardless of any replica identity.

Every publication can have multiple subscribers.

A publication is created using the [`CREATE PUBLICATION`](#sql-createpublication) command and may later be altered or dropped using corresponding commands.

The individual tables can be added and removed dynamically using [`ALTER PUBLICATION`](#sql-alterpublication). Both the `ADD TABLE` and `DROP TABLE` operations are transactional; so the table will start or stop replicating at the correct snapshot once the transaction has committed.

## Subscription

A subscription is the downstream side of logical replication. The node where a subscription is defined is referred to as the subscriber. A subscription defines the connection to another database and the set of publications (one or more) to which it wants to subscribe.

The subscriber database behaves in the same way as any other PostgreSQL instance and can be used as a publisher for other databases by defining its own publications.

A subscriber node may have multiple subscriptions if desired. It is possible to define multiple subscriptions between a single publisher-subscriber pair, in which case care must be taken to ensure that the subscribed publication objects don't overlap.

Each subscription will receive changes via one replication slot (see [???](#streaming-replication-slots)). Additional replication slots may be required for the initial data synchronization of pre-existing table data and those will be dropped at the end of data synchronization.

A logical replication subscription can be a standby for synchronous replication (see [???](#synchronous-replication)). The standby name is by default the subscription name. An alternative name can be specified as `application_name` in the connection information of the subscription.

Subscriptions are dumped by `pg_dump` if the current user is a superuser. Otherwise a warning is written and subscriptions are skipped, because non-superusers cannot read all subscription information from the pg_subscription catalog.

The subscription is added using [`CREATE SUBSCRIPTION`](#sql-createsubscription) and can be stopped/resumed at any time using the [`ALTER SUBSCRIPTION`](#sql-altersubscription) command and removed using [`DROP SUBSCRIPTION`](#sql-dropsubscription).

When a subscription is dropped and recreated, the synchronization information is lost. This means that the data has to be resynchronized afterwards.

The schema definitions are not replicated, and the published tables must exist on the subscriber. Only regular tables may be the target of replication. For example, you can't replicate to a view.

The tables are matched between the publisher and the subscriber using the fully qualified table name. Replication to differently-named tables on the subscriber is not supported.

Columns of a table are also matched by name. The order of columns in the subscriber table does not need to match that of the publisher. The data types of the columns do not need to match, as long as the text representation of the data can be converted to the target type. For example, you can replicate from a column of type `integer` to a column of type `bigint`. The target table can also have additional columns not provided by the published table. Any such columns will be filled with the default value as specified in the definition of the target table. However, logical replication in binary format is more restrictive. See the [`binary`](#sql-createsubscription-params-with-binary) option of `CREATE SUBSCRIPTION` for details.

### Replication Slot Management

As mentioned earlier, each (active) subscription receives changes from a replication slot on the remote (publishing) side.

Additional table synchronization slots are normally transient, created internally to perform initial table synchronization and dropped automatically when they are no longer needed. These table synchronization slots have generated names: “`pg_%u_sync_%u_%llu`” (parameters: Subscription `oid`, Table `relid`, system identifier `sysid`)

Normally, the remote replication slot is created automatically when the subscription is created using [ `CREATE SUBSCRIPTION`](#sql-createsubscription) and it is dropped automatically when the subscription is dropped using [`DROP SUBSCRIPTION`](#sql-dropsubscription). In some situations, however, it can be useful or necessary to manipulate the subscription and the underlying replication slot separately. Here are some scenarios:

- When creating a subscription, the replication slot already exists. In that case, the subscription can be created using the `create_slot = false` option to associate with the existing slot.

- When creating a subscription, the remote host is not reachable or in an unclear state. In that case, the subscription can be created using the `connect = false` option. The remote host will then not be contacted at all. This is what pg_dump uses. The remote replication slot will then have to be created manually before the subscription can be activated.

- When dropping a subscription, the replication slot should be kept. This could be useful when the subscriber database is being moved to a different host and will be activated from there. In that case, disassociate the slot from the subscription using [`ALTER SUBSCRIPTION`](#sql-altersubscription) before attempting to drop the subscription.

- When dropping a subscription, the remote host is not reachable. In that case, disassociate the slot from the subscription using `ALTER SUBSCRIPTION` before attempting to drop the subscription. If the remote database instance no longer exists, no further action is then necessary. If, however, the remote database instance is just unreachable, the replication slot (and any still remaining table synchronization slots) should then be dropped manually; otherwise it/they would continue to reserve WAL and might eventually cause the disk to fill up. Such cases should be carefully investigated.

### Examples: Set Up Logical Replication

Create some test tables on the publisher.

    test_pub=# CREATE TABLE t1(a int, b text, PRIMARY KEY(a));
    CREATE TABLE
    test_pub=# CREATE TABLE t2(c int, d text, PRIMARY KEY(c));
    CREATE TABLE
    test_pub=# CREATE TABLE t3(e int, f text, PRIMARY KEY(e));
    CREATE TABLE

Create the same tables on the subscriber.

    test_sub=# CREATE TABLE t1(a int, b text, PRIMARY KEY(a));
    CREATE TABLE
    test_sub=# CREATE TABLE t2(c int, d text, PRIMARY KEY(c));
    CREATE TABLE
    test_sub=# CREATE TABLE t3(e int, f text, PRIMARY KEY(e));
    CREATE TABLE

Insert data to the tables at the publisher side.

    test_pub=# INSERT INTO t1 VALUES (1, 'one'), (2, 'two'), (3, 'three');
    INSERT 0 3
    test_pub=# INSERT INTO t2 VALUES (1, 'A'), (2, 'B'), (3, 'C');
    INSERT 0 3
    test_pub=# INSERT INTO t3 VALUES (1, 'i'), (2, 'ii'), (3, 'iii');
    INSERT 0 3

Create publications for the tables. The publications `pub2` and `pub3a` disallow some [`publish`](#sql-createpublication-params-with-publish) operations. The publication `pub3b` has a row filter (see [Row Filters](#logical-replication-row-filter)).

    test_pub=# CREATE PUBLICATION pub1 FOR TABLE t1;
    CREATE PUBLICATION
    test_pub=# CREATE PUBLICATION pub2 FOR TABLE t2 WITH (publish = 'truncate');
    CREATE PUBLICATION
    test_pub=# CREATE PUBLICATION pub3a FOR TABLE t3 WITH (publish = 'truncate');
    CREATE PUBLICATION
    test_pub=# CREATE PUBLICATION pub3b FOR TABLE t3 WHERE (e > 5);
    CREATE PUBLICATION

Create subscriptions for the publications. The subscription `sub3` subscribes to both `pub3a` and `pub3b`. All subscriptions will copy initial data by default.

    test_sub=# CREATE SUBSCRIPTION sub1
    test_sub-# CONNECTION 'host=localhost dbname=test_pub application_name=sub1'
    test_sub-# PUBLICATION pub1;
    CREATE SUBSCRIPTION
    test_sub=# CREATE SUBSCRIPTION sub2
    test_sub-# CONNECTION 'host=localhost dbname=test_pub application_name=sub2'
    test_sub-# PUBLICATION pub2;
    CREATE SUBSCRIPTION
    test_sub=# CREATE SUBSCRIPTION sub3
    test_sub-# CONNECTION 'host=localhost dbname=test_pub application_name=sub3'
    test_sub-# PUBLICATION pub3a, pub3b;
    CREATE SUBSCRIPTION

Observe that initial table data is copied, regardless of the `publish` operation of the publication.

    test_sub=# SELECT * FROM t1;
     a |   b
    ---+-------
     1 | one
     2 | two
     3 | three
    (3 rows)

    test_sub=# SELECT * FROM t2;
     c | d
    ---+---
     1 | A
     2 | B
     3 | C
    (3 rows)

Furthermore, because the initial data copy ignores the `publish` operation, and because publication `pub3a` has no row filter, it means the copied table `t3` contains all rows even when they do not match the row filter of publication `pub3b`.

    test_sub=# SELECT * FROM t3;
     e |  f
    ---+-----
     1 | i
     2 | ii
     3 | iii
    (3 rows)

Insert more data to the tables at the publisher side.

    test_pub=# INSERT INTO t1 VALUES (4, 'four'), (5, 'five'), (6, 'six');
    INSERT 0 3
    test_pub=# INSERT INTO t2 VALUES (4, 'D'), (5, 'E'), (6, 'F');
    INSERT 0 3
    test_pub=# INSERT INTO t3 VALUES (4, 'iv'), (5, 'v'), (6, 'vi');
    INSERT 0 3

Now the publisher side data looks like:

    test_pub=# SELECT * FROM t1;
     a |   b
    ---+-------
     1 | one
     2 | two
     3 | three
     4 | four
     5 | five
     6 | six
    (6 rows)

    test_pub=# SELECT * FROM t2;
     c | d
    ---+---
     1 | A
     2 | B
     3 | C
     4 | D
     5 | E
     6 | F
    (6 rows)

    test_pub=# SELECT * FROM t3;
     e |  f
    ---+-----
     1 | i
     2 | ii
     3 | iii
     4 | iv
     5 | v
     6 | vi
    (6 rows)

Observe that during normal replication the appropriate `publish` operations are used. This means publications `pub2` and `pub3a` will not replicate the `INSERT`. Also, publication `pub3b` will only replicate data that matches the row filter of `pub3b`. Now the subscriber side data looks like:

    test_sub=# SELECT * FROM t1;
     a |   b
    ---+-------
     1 | one
     2 | two
     3 | three
     4 | four
     5 | five
     6 | six
    (6 rows)

    test_sub=# SELECT * FROM t2;
     c | d
    ---+---
     1 | A
     2 | B
     3 | C
    (3 rows)

    test_sub=# SELECT * FROM t3;
     e |  f
    ---+-----
     1 | i
     2 | ii
     3 | iii
     6 | vi
    (4 rows)

### Examples: Deferred Replication Slot Creation

There are some cases (e.g. [Replication Slot Management](#logical-replication-subscription-slot)) where, if the remote replication slot was not created automatically, the user must create it manually before the subscription can be activated. The steps to create the slot and activate the subscription are shown in the following examples. These examples specify the standard logical decoding output plugin (`pgoutput`), which is what the built-in logical replication uses.

First, create a publication for the examples to use.

    test_pub=# CREATE PUBLICATION pub1 FOR ALL TABLES;
    CREATE PUBLICATION

Example 1: Where the subscription says `connect = false`

- Create the subscription.

      test_sub=# CREATE SUBSCRIPTION sub1
      test_sub-# CONNECTION 'host=localhost dbname=test_pub'
      test_sub-# PUBLICATION pub1
      test_sub-# WITH (connect=false);
      WARNING:  subscription was created, but is not connected
      HINT:  To initiate replication, you must manually create the replication slot, enable the subscription, and refresh the subscription.
      CREATE SUBSCRIPTION

- On the publisher, manually create a slot. Because the name was not specified during `CREATE SUBSCRIPTION`, the name of the slot to create is same as the subscription name, e.g. "sub1".

      test_pub=# SELECT * FROM pg_create_logical_replication_slot('sub1', 'pgoutput');
       slot_name |    lsn
      -----------+-----------
       sub1      | 0/19404D0
      (1 row)

- On the subscriber, complete the activation of the subscription. After this the tables of `pub1` will start replicating.

      test_sub=# ALTER SUBSCRIPTION sub1 ENABLE;
      ALTER SUBSCRIPTION
      test_sub=# ALTER SUBSCRIPTION sub1 REFRESH PUBLICATION;
      ALTER SUBSCRIPTION

Example 2: Where the subscription says `connect = false`, but also specifies the [`slot_name`](#sql-createsubscription-params-with-slot-name) option.

- Create the subscription.

      test_sub=# CREATE SUBSCRIPTION sub1
      test_sub-# CONNECTION 'host=localhost dbname=test_pub'
      test_sub-# PUBLICATION pub1
      test_sub-# WITH (connect=false, slot_name='myslot');
      WARNING:  subscription was created, but is not connected
      HINT:  To initiate replication, you must manually create the replication slot, enable the subscription, and refresh the subscription.
      CREATE SUBSCRIPTION

- On the publisher, manually create a slot using the same name that was specified during `CREATE SUBSCRIPTION`, e.g. "myslot".

      test_pub=# SELECT * FROM pg_create_logical_replication_slot('myslot', 'pgoutput');
       slot_name |    lsn
      -----------+-----------
       myslot    | 0/19059A0
      (1 row)

- On the subscriber, the remaining subscription activation steps are the same as before.

      test_sub=# ALTER SUBSCRIPTION sub1 ENABLE;
      ALTER SUBSCRIPTION
      test_sub=# ALTER SUBSCRIPTION sub1 REFRESH PUBLICATION;
      ALTER SUBSCRIPTION

Example 3: Where the subscription specifies `slot_name = NONE`

- Create the subscription. When `slot_name = NONE` then `enabled = false`, and `create_slot = false` are also needed.

      test_sub=# CREATE SUBSCRIPTION sub1
      test_sub-# CONNECTION 'host=localhost dbname=test_pub'
      test_sub-# PUBLICATION pub1
      test_sub-# WITH (slot_name=NONE, enabled=false, create_slot=false);
      CREATE SUBSCRIPTION

- On the publisher, manually create a slot using any name, e.g. "myslot".

      test_pub=# SELECT * FROM pg_create_logical_replication_slot('myslot', 'pgoutput');
       slot_name |    lsn
      -----------+-----------
       myslot    | 0/1905930
      (1 row)

- On the subscriber, associate the subscription with the slot name just created.

      test_sub=# ALTER SUBSCRIPTION sub1 SET (slot_name='myslot');
      ALTER SUBSCRIPTION

- The remaining subscription activation steps are same as before.

      test_sub=# ALTER SUBSCRIPTION sub1 ENABLE;
      ALTER SUBSCRIPTION
      test_sub=# ALTER SUBSCRIPTION sub1 REFRESH PUBLICATION;
      ALTER SUBSCRIPTION

## Logical Replication Failover

To allow subscriber nodes to continue replicating data from the publisher node even when the publisher node goes down, there must be a physical standby corresponding to the publisher node. The logical slots on the primary server corresponding to the subscriptions can be synchronized to the standby server by specifying `failover = true` when creating subscriptions. See [???](#logicaldecoding-replication-slots-synchronization) for details. Enabling the [`failover`](#sql-createsubscription-params-with-failover) parameter ensures a seamless transition of those subscriptions after the standby is promoted. They can continue subscribing to publications on the new primary server.

Because the slot synchronization logic copies asynchronously, it is necessary to confirm that replication slots have been synced to the standby server before the failover happens. To ensure a successful failover, the standby server must be ahead of the subscriber. This can be achieved by configuring [`synchronized_standby_slots`](#guc-synchronized-standby-slots).

To confirm that the standby server is indeed ready for failover for a given subscriber, follow these steps to verify that all the logical replication slots required by that subscriber have been synchronized to the standby server:

1.  On the subscriber node, use the following SQL to identify which replication slots should be synced to the standby that we plan to promote. This query will return the relevant replication slots associated with the failover-enabled subscriptions.

        test_sub=# SELECT
                       array_agg(quote_literal(s.subslotname)) AS slots
                   FROM  pg_subscription s
                   WHERE s.subfailover AND
                         s.subslotname IS NOT NULL;
         slots
        -------
         {'sub1','sub2','sub3'}
        (1 row)

2.  On the subscriber node, use the following SQL to identify which table synchronization slots should be synced to the standby that we plan to promote. This query needs to be run on each database that includes the failover-enabled subscription(s). Note that the table sync slot should be synced to the standby server only if the table copy is finished (See [???](#catalog-pg-subscription-rel)). We don't need to ensure that the table sync slots are synced in other scenarios as they will either be dropped or re-created on the new primary server in those cases.

        test_sub=# SELECT
                       array_agg(quote_literal(slot_name)) AS slots
                   FROM
                   (
                       SELECT CONCAT('pg_', srsubid, '_sync_', srrelid, '_', ctl.system_identifier) AS slot_name
                       FROM pg_control_system() ctl, pg_subscription_rel r, pg_subscription s
                       WHERE r.srsubstate = 'f' AND s.oid = r.srsubid AND s.subfailover
                   );
         slots
        -------
         {'pg_16394_sync_16385_7394666715149055164'}
        (1 row)

3.  Check that the logical replication slots identified above exist on the standby server and are ready for failover.

        test_standby=# SELECT slot_name, (synced AND NOT temporary AND invalidation_reason IS NULL) AS failover_ready
                       FROM pg_replication_slots
                       WHERE slot_name IN
                           ('sub1','sub2','sub3', 'pg_16394_sync_16385_7394666715149055164');
          slot_name                                 | failover_ready
        --------------------------------------------+----------------
          sub1                                      | t
          sub2                                      | t
          sub3                                      | t
          pg_16394_sync_16385_7394666715149055164   | t
        (4 rows)

If all the slots are present on the standby server and the result (`failover_ready`) of the above SQL query is true, then existing subscriptions can continue subscribing to publications on the new primary server.

The first two steps in the above procedure are meant for a PostgreSQL subscriber. It is recommended to run these steps on each subscriber node, that will be served by the designated standby after failover, to obtain the complete list of replication slots. This list can then be verified in Step 3 to ensure failover readiness. Non-PostgreSQL subscribers, on the other hand, may use their own methods to identify the replication slots used by their respective subscriptions.

In some cases, such as during a planned failover, it is necessary to confirm that all subscribers, whether PostgreSQL or non-PostgreSQL, will be able to continue replication after failover to a given standby server. In such cases, use the following SQL, instead of performing the first two steps above, to identify which replication slots on the primary need to be synced to the standby that is intended for promotion. This query returns the relevant replication slots associated with all the failover-enabled subscriptions.

    /* primary # */ SELECT array_agg(quote_literal(r.slot_name)) AS slots
                   FROM pg_replication_slots r
                   WHERE r.failover AND NOT r.temporary;
     slots
    -------
     {'sub1','sub2','sub3', 'pg_16394_sync_16385_7394666715149055164'}
    (1 row)

## Row Filters

By default, all data from all published tables will be replicated to the appropriate subscribers. The replicated data can be reduced by using a row filter. A user might choose to use row filters for behavioral, security or performance reasons. If a published table sets a row filter, a row is replicated only if its data satisfies the row filter expression. This allows a set of tables to be partially replicated. The row filter is defined per table. Use a `WHERE` clause after the table name for each published table that requires data to be filtered out. The `WHERE` clause must be enclosed by parentheses. See [???](#sql-createpublication) for details.

### Row Filter Rules

Row filters are applied *before* publishing the changes. If the row filter evaluates to `false` or `NULL` then the row is not replicated. The `WHERE` clause expression is evaluated with the same role used for the replication connection (i.e. the role specified in the [`CONNECTION`](#sql-createsubscription-params-connection) clause of the [???](#sql-createsubscription)). Row filters have no effect for `TRUNCATE` command.

### Expression Restrictions

The `WHERE` clause allows only simple expressions. It cannot contain user-defined functions, operators, types, and collations, system column references or non-immutable built-in functions.

If a publication publishes `UPDATE` or `DELETE` operations, the row filter `WHERE` clause must contain only columns that are covered by the replica identity (see [???](#sql-altertable-replica-identity)). If a publication publishes only `INSERT` operations, the row filter `WHERE` clause can use any column.

### UPDATE Transformations

Whenever an `UPDATE` is processed, the row filter expression is evaluated for both the old and new row (i.e. using the data before and after the update). If both evaluations are `true`, it replicates the `UPDATE` change. If both evaluations are `false`, it doesn't replicate the change. If only one of the old/new rows matches the row filter expression, the `UPDATE` is transformed to `INSERT` or `DELETE`, to avoid any data inconsistency. The row on the subscriber should reflect what is defined by the row filter expression on the publisher.

If the old row satisfies the row filter expression (it was sent to the subscriber) but the new row doesn't, then, from a data consistency perspective the old row should be removed from the subscriber. So the `UPDATE` is transformed into a `DELETE`.

If the old row doesn't satisfy the row filter expression (it wasn't sent to the subscriber) but the new row does, then, from a data consistency perspective the new row should be added to the subscriber. So the `UPDATE` is transformed into an `INSERT`.

[ Transformation Summary](#logical-replication-row-filter-transformations-summary) summarizes the applied transformations.

| Old row  | New row  | Transformation  |
|----------|----------|-----------------|
| no match | no match | don't replicate |
| no match | match    | `INSERT`        |
| match    | no match | `DELETE`        |
| match    | match    | `UPDATE`        |

`UPDATE` Transformation Summary {#logical-replication-row-filter-transformations-summary}

### Partitioned Tables

If the publication contains a partitioned table, the publication parameter [`publish_via_partition_root`](#sql-createpublication-params-with-publish-via-partition-root) determines which row filter is used. If `publish_via_partition_root` is `true`, the *root partitioned table's* row filter is used. Otherwise, if `publish_via_partition_root` is `false` (default), each *partition's* row filter is used.

### Initial Data Synchronization

If the subscription requires copying pre-existing table data and a publication contains `WHERE` clauses, only data that satisfies the row filter expressions is copied to the subscriber.

If the subscription has several publications in which a table has been published with different `WHERE` clauses, rows that satisfy *any* of the expressions will be copied. See [Combining Multiple Row Filters](#logical-replication-row-filter-combining) for details.

> [!WARNING]
> Because initial data synchronization does not take into account the [`publish`](#sql-createpublication-params-with-publish) parameter when copying existing table data, some rows may be copied that would not be replicated using DML. Refer to [Initial Snapshot](#logical-replication-snapshot), and see [Examples: Set Up Logical Replication](#logical-replication-subscription-examples) for examples.

> [!NOTE]
> If the subscriber is in a release prior to 15, copying pre-existing data doesn't use row filters even if they are defined in the publication. This is because old releases can only copy the entire table data.

### Combining Multiple Row Filters

If the subscription has several publications in which the same table has been published with different row filters (for the same [`publish`](#sql-createpublication-params-with-publish) operation), those expressions get ORed together, so that rows satisfying *any* of the expressions will be replicated. This means all the other row filters for the same table become redundant if:

- One of the publications has no row filter.

- One of the publications was created using [`FOR ALL TABLES`](#sql-createpublication-params-for-all-tables). This clause does not allow row filters.

- One of the publications was created using [`FOR TABLES IN SCHEMA`](#sql-createpublication-params-for-tables-in-schema) and the table belongs to the referred schema. This clause does not allow row filters.

### Examples

Create some tables to be used in the following examples.

    test_pub=# CREATE TABLE t1(a int, b int, c text, PRIMARY KEY(a,c));
    CREATE TABLE
    test_pub=# CREATE TABLE t2(d int, e int, f int, PRIMARY KEY(d));
    CREATE TABLE
    test_pub=# CREATE TABLE t3(g int, h int, i int, PRIMARY KEY(g));
    CREATE TABLE

Create some publications. Publication `p1` has one table (`t1`) and that table has a row filter. Publication `p2` has two tables. Table `t1` has no row filter, and table `t2` has a row filter. Publication `p3` has two tables, and both of them have a row filter.

    test_pub=# CREATE PUBLICATION p1 FOR TABLE t1 WHERE (a > 5 AND c = 'NSW');
    CREATE PUBLICATION
    test_pub=# CREATE PUBLICATION p2 FOR TABLE t1, t2 WHERE (e = 99);
    CREATE PUBLICATION
    test_pub=# CREATE PUBLICATION p3 FOR TABLE t2 WHERE (d = 10), t3 WHERE (g = 10);
    CREATE PUBLICATION

`psql` can be used to show the row filter expressions (if defined) for each publication.

    test_pub=# \dRp+
                                   Publication p1
      Owner   | All tables | Inserts | Updates | Deletes | Truncates | Via root
    ----------+------------+---------+---------+---------+-----------+----------
     postgres | f          | t       | t       | t       | t         | f
    Tables:
        "public.t1" WHERE ((a > 5) AND (c = 'NSW'::text))

                                   Publication p2
      Owner   | All tables | Inserts | Updates | Deletes | Truncates | Via root
    ----------+------------+---------+---------+---------+-----------+----------
     postgres | f          | t       | t       | t       | t         | f
    Tables:
        "public.t1"
        "public.t2" WHERE (e = 99)

                                   Publication p3
      Owner   | All tables | Inserts | Updates | Deletes | Truncates | Via root
    ----------+------------+---------+---------+---------+-----------+----------
     postgres | f          | t       | t       | t       | t         | f
    Tables:
        "public.t2" WHERE (d = 10)
        "public.t3" WHERE (g = 10)

`psql` can be used to show the row filter expressions (if defined) for each table. See that table `t1` is a member of two publications, but has a row filter only in `p1`. See that table `t2` is a member of two publications, and has a different row filter in each of them.

    test_pub=# \d t1
                     Table "public.t1"
     Column |  Type   | Collation | Nullable | Default
    --------+---------+-----------+----------+---------
     a      | integer |           | not null |
     b      | integer |           |          |
     c      | text    |           | not null |
    Indexes:
        "t1_pkey" PRIMARY KEY, btree (a, c)
    Publications:
        "p1" WHERE ((a > 5) AND (c = 'NSW'::text))
        "p2"

    test_pub=# \d t2
                     Table "public.t2"
     Column |  Type   | Collation | Nullable | Default
    --------+---------+-----------+----------+---------
     d      | integer |           | not null |
     e      | integer |           |          |
     f      | integer |           |          |
    Indexes:
        "t2_pkey" PRIMARY KEY, btree (d)
    Publications:
        "p2" WHERE (e = 99)
        "p3" WHERE (d = 10)

    test_pub=# \d t3
                     Table "public.t3"
     Column |  Type   | Collation | Nullable | Default
    --------+---------+-----------+----------+---------
     g      | integer |           | not null |
     h      | integer |           |          |
     i      | integer |           |          |
    Indexes:
        "t3_pkey" PRIMARY KEY, btree (g)
    Publications:
        "p3" WHERE (g = 10)

On the subscriber node, create a table `t1` with the same definition as the one on the publisher, and also create the subscription `s1` that subscribes to the publication `p1`.

    test_sub=# CREATE TABLE t1(a int, b int, c text, PRIMARY KEY(a,c));
    CREATE TABLE
    test_sub=# CREATE SUBSCRIPTION s1
    test_sub-# CONNECTION 'host=localhost dbname=test_pub application_name=s1'
    test_sub-# PUBLICATION p1;
    CREATE SUBSCRIPTION

Insert some rows. Only the rows satisfying the `t1 WHERE` clause of publication `p1` are replicated.

    test_pub=# INSERT INTO t1 VALUES (2, 102, 'NSW');
    INSERT 0 1
    test_pub=# INSERT INTO t1 VALUES (3, 103, 'QLD');
    INSERT 0 1
    test_pub=# INSERT INTO t1 VALUES (4, 104, 'VIC');
    INSERT 0 1
    test_pub=# INSERT INTO t1 VALUES (5, 105, 'ACT');
    INSERT 0 1
    test_pub=# INSERT INTO t1 VALUES (6, 106, 'NSW');
    INSERT 0 1
    test_pub=# INSERT INTO t1 VALUES (7, 107, 'NT');
    INSERT 0 1
    test_pub=# INSERT INTO t1 VALUES (8, 108, 'QLD');
    INSERT 0 1
    test_pub=# INSERT INTO t1 VALUES (9, 109, 'NSW');
    INSERT 0 1

    test_pub=# SELECT * FROM t1;
     a |  b  |  c
    ---+-----+-----
     2 | 102 | NSW
     3 | 103 | QLD
     4 | 104 | VIC
     5 | 105 | ACT
     6 | 106 | NSW
     7 | 107 | NT
     8 | 108 | QLD
     9 | 109 | NSW
    (8 rows)

    test_sub=# SELECT * FROM t1;
     a |  b  |  c
    ---+-----+-----
     6 | 106 | NSW
     9 | 109 | NSW
    (2 rows)

Update some data, where the old and new row values both satisfy the `t1 WHERE` clause of publication `p1`. The `UPDATE` replicates the change as normal.

    test_pub=# UPDATE t1 SET b = 999 WHERE a = 6;
    UPDATE 1

    test_pub=# SELECT * FROM t1;
     a |  b  |  c
    ---+-----+-----
     2 | 102 | NSW
     3 | 103 | QLD
     4 | 104 | VIC
     5 | 105 | ACT
     7 | 107 | NT
     8 | 108 | QLD
     9 | 109 | NSW
     6 | 999 | NSW
    (8 rows)

    test_sub=# SELECT * FROM t1;
     a |  b  |  c
    ---+-----+-----
     9 | 109 | NSW
     6 | 999 | NSW
    (2 rows)

Update some data, where the old row values did not satisfy the `t1 WHERE` clause of publication `p1`, but the new row values do satisfy it. The `UPDATE` is transformed into an `INSERT` and the change is replicated. See the new row on the subscriber.

    test_pub=# UPDATE t1 SET a = 555 WHERE a = 2;
    UPDATE 1

    test_pub=# SELECT * FROM t1;
      a  |  b  |  c
    -----+-----+-----
       3 | 103 | QLD
       4 | 104 | VIC
       5 | 105 | ACT
       7 | 107 | NT
       8 | 108 | QLD
       9 | 109 | NSW
       6 | 999 | NSW
     555 | 102 | NSW
    (8 rows)

    test_sub=# SELECT * FROM t1;
      a  |  b  |  c
    -----+-----+-----
       9 | 109 | NSW
       6 | 999 | NSW
     555 | 102 | NSW
    (3 rows)

Update some data, where the old row values satisfied the `t1 WHERE` clause of publication `p1`, but the new row values do not satisfy it. The `UPDATE` is transformed into a `DELETE` and the change is replicated. See that the row is removed from the subscriber.

    test_pub=# UPDATE t1 SET c = 'VIC' WHERE a = 9;
    UPDATE 1

    test_pub=# SELECT * FROM t1;
      a  |  b  |  c
    -----+-----+-----
       3 | 103 | QLD
       4 | 104 | VIC
       5 | 105 | ACT
       7 | 107 | NT
       8 | 108 | QLD
       6 | 999 | NSW
     555 | 102 | NSW
       9 | 109 | VIC
    (8 rows)

    test_sub=# SELECT * FROM t1;
      a  |  b  |  c
    -----+-----+-----
       6 | 999 | NSW
     555 | 102 | NSW
    (2 rows)

The following examples show how the publication parameter [`publish_via_partition_root`](#sql-createpublication-params-with-publish-via-partition-root) determines whether the row filter of the parent or child table will be used in the case of partitioned tables.

Create a partitioned table on the publisher.

    test_pub=# CREATE TABLE parent(a int PRIMARY KEY) PARTITION BY RANGE(a);
    CREATE TABLE
    test_pub=# CREATE TABLE child PARTITION OF parent DEFAULT;
    CREATE TABLE

Create the same tables on the subscriber.

    test_sub=# CREATE TABLE parent(a int PRIMARY KEY) PARTITION BY RANGE(a);
    CREATE TABLE
    test_sub=# CREATE TABLE child PARTITION OF parent DEFAULT;
    CREATE TABLE

Create a publication `p4`, and then subscribe to it. The publication parameter `publish_via_partition_root` is set as true. There are row filters defined on both the partitioned table (`parent`), and on the partition (`child`).

    test_pub=# CREATE PUBLICATION p4 FOR TABLE parent WHERE (a < 5), child WHERE (a >= 5)
    test_pub-# WITH (publish_via_partition_root=true);
    CREATE PUBLICATION

    test_sub=# CREATE SUBSCRIPTION s4
    test_sub-# CONNECTION 'host=localhost dbname=test_pub application_name=s4'
    test_sub-# PUBLICATION p4;
    CREATE SUBSCRIPTION

Insert some values directly into the `parent` and `child` tables. They replicate using the row filter of `parent` (because `publish_via_partition_root` is true).

    test_pub=# INSERT INTO parent VALUES (2), (4), (6);
    INSERT 0 3
    test_pub=# INSERT INTO child VALUES (3), (5), (7);
    INSERT 0 3

    test_pub=# SELECT * FROM parent ORDER BY a;
     a
    ---
     2
     3
     4
     5
     6
     7
    (6 rows)

    test_sub=# SELECT * FROM parent ORDER BY a;
     a
    ---
     2
     3
     4
    (3 rows)

Repeat the same test, but with a different value for `publish_via_partition_root`. The publication parameter `publish_via_partition_root` is set as false. A row filter is defined on the partition (`child`).

    test_pub=# DROP PUBLICATION p4;
    DROP PUBLICATION
    test_pub=# CREATE PUBLICATION p4 FOR TABLE parent, child WHERE (a >= 5)
    test_pub-# WITH (publish_via_partition_root=false);
    CREATE PUBLICATION

    test_sub=# ALTER SUBSCRIPTION s4 REFRESH PUBLICATION;
    ALTER SUBSCRIPTION

Do the inserts on the publisher same as before. They replicate using the row filter of `child` (because `publish_via_partition_root` is false).

    test_pub=# TRUNCATE parent;
    TRUNCATE TABLE
    test_pub=# INSERT INTO parent VALUES (2), (4), (6);
    INSERT 0 3
    test_pub=# INSERT INTO child VALUES (3), (5), (7);
    INSERT 0 3

    test_pub=# SELECT * FROM parent ORDER BY a;
     a
    ---
     2
     3
     4
     5
     6
     7
    (6 rows)

    test_sub=# SELECT * FROM child ORDER BY a;
     a
    ---
     5
     6
     7
    (3 rows)

## Column Lists

Each publication can optionally specify which columns of each table are replicated to subscribers. The table on the subscriber side must have at least all the columns that are published. If no column list is specified, then all columns on the publisher are replicated. See [???](#sql-createpublication) for details on the syntax.

The choice of columns can be based on behavioral or performance reasons. However, do not rely on this feature for security: a malicious subscriber is able to obtain data from columns that are not specifically published. If security is a consideration, protections can be applied at the publisher side.

If no column list is specified, any columns added to the table later are automatically replicated. This means that having a column list which names all columns is not the same as having no column list at all.

A column list can contain only simple column references. The order of columns in the list is not preserved.

Specifying a column list when the publication also publishes [`FOR TABLES IN SCHEMA`](#sql-createpublication-params-for-tables-in-schema) is not supported.

For partitioned tables, the publication parameter [`publish_via_partition_root`](#sql-createpublication-params-with-publish-via-partition-root) determines which column list is used. If `publish_via_partition_root` is `true`, the root partitioned table's column list is used. Otherwise, if `publish_via_partition_root` is `false` (the default), each partition's column list is used.

If a publication publishes `UPDATE` or `DELETE` operations, any column list must include the table's replica identity columns (see [???](#sql-altertable-replica-identity)). If a publication publishes only `INSERT` operations, then the column list may omit replica identity columns.

Column lists have no effect for the `TRUNCATE` command.

During initial data synchronization, only the published columns are copied. However, if the subscriber is from a release prior to 15, then all the columns in the table are copied during initial data synchronization, ignoring any column lists.

> [!WARNING]
> There's currently no support for subscriptions comprising several publications where the same table has been published with different column lists. [???](#sql-createsubscription) disallows creating such subscriptions, but it is still possible to get into that situation by adding or altering column lists on the publication side after a subscription has been created.
>
> This means changing the column lists of tables on publications that are already subscribed could lead to errors being thrown on the subscriber side.
>
> If a subscription is affected by this problem, the only way to resume replication is to adjust one of the column lists on the publication side so that they all match; and then either recreate the subscription, or use [ `ALTER SUBSCRIPTION ... DROP PUBLICATION`](#sql-altersubscription-params-setadddrop-publication) to remove one of the offending publications and add it again.

### Examples

Create a table `t1` to be used in the following example.

    test_pub=# CREATE TABLE t1(id int, a text, b text, c text, d text, e text, PRIMARY KEY(id));
    CREATE TABLE

Create a publication `p1`. A column list is defined for table `t1` to reduce the number of columns that will be replicated. Notice that the order of column names in the column list does not matter.

    test_pub=# CREATE PUBLICATION p1 FOR TABLE t1 (id, b, a, d);
    CREATE PUBLICATION

`psql` can be used to show the column lists (if defined) for each publication.

    test_pub=# \dRp+
                                   Publication p1
      Owner   | All tables | Inserts | Updates | Deletes | Truncates | Via root
    ----------+------------+---------+---------+---------+-----------+----------
     postgres | f          | t       | t       | t       | t         | f
    Tables:
        "public.t1" (id, a, b, d)

`psql` can be used to show the column lists (if defined) for each table.

    test_pub=# \d t1
                     Table "public.t1"
     Column |  Type   | Collation | Nullable | Default
    --------+---------+-----------+----------+---------
     id     | integer |           | not null |
     a      | text    |           |          |
     b      | text    |           |          |
     c      | text    |           |          |
     d      | text    |           |          |
     e      | text    |           |          |
    Indexes:
        "t1_pkey" PRIMARY KEY, btree (id)
    Publications:
        "p1" (id, a, b, d)

On the subscriber node, create a table `t1` which now only needs a subset of the columns that were on the publisher table `t1`, and also create the subscription `s1` that subscribes to the publication `p1`.

    test_sub=# CREATE TABLE t1(id int, b text, a text, d text, PRIMARY KEY(id));
    CREATE TABLE
    test_sub=# CREATE SUBSCRIPTION s1
    test_sub-# CONNECTION 'host=localhost dbname=test_pub application_name=s1'
    test_sub-# PUBLICATION p1;
    CREATE SUBSCRIPTION

On the publisher node, insert some rows to table `t1`.

    test_pub=# INSERT INTO t1 VALUES(1, 'a-1', 'b-1', 'c-1', 'd-1', 'e-1');
    INSERT 0 1
    test_pub=# INSERT INTO t1 VALUES(2, 'a-2', 'b-2', 'c-2', 'd-2', 'e-2');
    INSERT 0 1
    test_pub=# INSERT INTO t1 VALUES(3, 'a-3', 'b-3', 'c-3', 'd-3', 'e-3');
    INSERT 0 1
    test_pub=# SELECT * FROM t1 ORDER BY id;
     id |  a  |  b  |  c  |  d  |  e
    ----+-----+-----+-----+-----+-----
      1 | a-1 | b-1 | c-1 | d-1 | e-1
      2 | a-2 | b-2 | c-2 | d-2 | e-2
      3 | a-3 | b-3 | c-3 | d-3 | e-3
    (3 rows)

Only data from the column list of publication `p1` is replicated.

    test_sub=# SELECT * FROM t1 ORDER BY id;
     id |  b  |  a  |  d
    ----+-----+-----+-----
      1 | b-1 | a-1 | d-1
      2 | b-2 | a-2 | d-2
      3 | b-3 | a-3 | d-3
    (3 rows)

## Conflicts

Logical replication behaves similarly to normal DML operations in that the data will be updated even if it was changed locally on the subscriber node. If incoming data violates any constraints the replication will stop. This is referred to as a conflict. When replicating `UPDATE` or `DELETE` operations, missing data will not produce a conflict and such operations will simply be skipped.

Logical replication operations are performed with the privileges of the role which owns the subscription. Permissions failures on target tables will cause replication conflicts, as will enabled [row-level security](#ddl-rowsecurity) on target tables that the subscription owner is subject to, without regard to whether any policy would ordinarily reject the `INSERT`, `UPDATE`, `DELETE` or `TRUNCATE` which is being replicated. This restriction on row-level security may be lifted in a future version of PostgreSQL.

A conflict will produce an error and will stop the replication; it must be resolved manually by the user. Details about the conflict can be found in the subscriber's server log.

The resolution can be done either by changing data or permissions on the subscriber so that it does not conflict with the incoming change or by skipping the transaction that conflicts with the existing data. When a conflict produces an error, the replication won't proceed, and the logical replication worker will emit the following kind of message to the subscriber's server log:

    ERROR:  duplicate key value violates unique constraint "test_pkey"
    DETAIL:  Key (c)=(1) already exists.
    CONTEXT:  processing remote data for replication origin "pg_16395" during "INSERT" for replication target relation "public.test" in transaction 725 finished at 0/14C0378

The LSN of the transaction that contains the change violating the constraint and the replication origin name can be found from the server log (LSN 0/14C0378 and replication origin `pg_16395` in the above case). The transaction that produced the conflict can be skipped by using [`ALTER SUBSCRIPTION ... SKIP`](#sql-altersubscription-params-skip) with the finish LSN (i.e., LSN 0/14C0378). The finish LSN could be an LSN at which the transaction is committed or prepared on the publisher. Alternatively, the transaction can also be skipped by calling the [ `pg_replication_origin_advance()`](#pg-replication-origin-advance) function. Before using this function, the subscription needs to be disabled temporarily either by [ `ALTER SUBSCRIPTION ... DISABLE`](#sql-altersubscription-params-disable) or, the subscription can be used with the [`disable_on_error`](#sql-createsubscription-params-with-disable-on-error) option. Then, you can use `pg_replication_origin_advance()` function with the `node_name` (i.e., `pg_16395`) and the next LSN of the finish LSN (i.e., 0/14C0379). The current position of origins can be seen in the [ pg_replication_origin_status](#view-pg-replication-origin-status) system view. Please note that skipping the whole transaction includes skipping changes that might not violate any constraint. This can easily make the subscriber inconsistent.

When the [`streaming`](#sql-createsubscription-params-with-streaming) mode is `parallel`, the finish LSN of failed transactions may not be logged. In that case, it may be necessary to change the streaming mode to `on` or `off` and cause the same conflicts again so the finish LSN of the failed transaction will be written to the server log. For the usage of finish LSN, please refer to [`ALTER SUBSCRIPTION ... SKIP`](#sql-altersubscription).

## Restrictions

Logical replication currently has the following restrictions or missing functionality. These might be addressed in future releases.

- The database schema and DDL commands are not replicated. The initial schema can be copied by hand using `pg_dump --schema-only`. Subsequent schema changes would need to be kept in sync manually. (Note, however, that there is no need for the schemas to be absolutely the same on both sides.) Logical replication is robust when schema definitions change in a live database: When the schema is changed on the publisher and replicated data starts arriving at the subscriber but does not fit into the table schema, replication will error until the schema is updated. In many cases, intermittent errors can be avoided by applying additive schema changes to the subscriber first.

- Sequence data is not replicated. The data in serial or identity columns backed by sequences will of course be replicated as part of the table, but the sequence itself would still show the start value on the subscriber. If the subscriber is used as a read-only database, then this should typically not be a problem. If, however, some kind of switchover or failover to the subscriber database is intended, then the sequences would need to be updated to the latest values, either by copying the current data from the publisher (perhaps using `pg_dump`) or by determining a sufficiently high value from the tables themselves.

- Replication of `TRUNCATE` commands is supported, but some care must be taken when truncating groups of tables connected by foreign keys. When replicating a truncate action, the subscriber will truncate the same group of tables that was truncated on the publisher, either explicitly specified or implicitly collected via `CASCADE`, minus tables that are not part of the subscription. This will work correctly if all affected tables are part of the same subscription. But if some tables to be truncated on the subscriber have foreign-key links to tables that are not part of the same (or any) subscription, then the application of the truncate action on the subscriber will fail.

- Large objects (see [???](#largeobjects)) are not replicated. There is no workaround for that, other than storing data in normal tables.

- Replication is only supported by tables, including partitioned tables. Attempts to replicate other types of relations, such as views, materialized views, or foreign tables, will result in an error.

- When replicating between partitioned tables, the actual replication originates, by default, from the leaf partitions on the publisher, so partitions on the publisher must also exist on the subscriber as valid target tables. (They could either be leaf partitions themselves, or they could be further subpartitioned, or they could even be independent tables.) Publications can also specify that changes are to be replicated using the identity and schema of the partitioned root table instead of that of the individual leaf partitions in which the changes actually originate (see [`publish_via_partition_root`](#sql-createpublication-params-with-publish-via-partition-root) parameter of `CREATE PUBLICATION`).

- When using [`REPLICA IDENTITY FULL`](#sql-altertable-replica-identity-full) on published tables, it is important to note that the `UPDATE` and `DELETE` operations cannot be applied to subscribers if the tables include attributes with datatypes (such as point or box) that do not have a default operator class for B-tree or Hash. However, this limitation can be overcome by ensuring that the table has a primary key or replica identity defined for it.

## Architecture

Logical replication starts by copying a snapshot of the data on the publisher database. Once that is done, changes on the publisher are sent to the subscriber as they occur in real time. The subscriber applies data in the order in which commits were made on the publisher so that transactional consistency is guaranteed for the publications within any single subscription.

Logical replication is built with an architecture similar to physical streaming replication (see [???](#streaming-replication)). It is implemented by `walsender` and `apply` processes. The walsender process starts logical decoding (described in [???](#logicaldecoding)) of the WAL and loads the standard logical decoding output plugin (`pgoutput`). The plugin transforms the changes read from WAL to the logical replication protocol (see [???](#protocol-logical-replication)) and filters the data according to the publication specification. The data is then continuously transferred using the streaming replication protocol to the apply worker, which maps the data to local tables and applies the individual changes as they are received, in correct transactional order.

The apply process on the subscriber database always runs with [`session_replication_role`](#guc-session-replication-role) set to `replica`. This means that, by default, triggers and rules will not fire on a subscriber. Users can optionally choose to enable triggers and rules on a table using the [`ALTER TABLE`](#sql-altertable) command and the `ENABLE TRIGGER` and `ENABLE RULE` clauses.

The logical replication apply process currently only fires row triggers, not statement triggers. The initial table synchronization, however, is implemented like a `COPY` command and thus fires both row and statement triggers for `INSERT`.

### Initial Snapshot

The initial data in existing subscribed tables is snapshotted and copied in a parallel instance of a special kind of apply process. This process will create its own replication slot and copy the existing data. As soon as the copy is finished the table contents will become visible to other backends. Once existing data is copied, the worker enters synchronization mode, which ensures that the table is brought up to a synchronized state with the main apply process by streaming any changes that happened during the initial data copy using standard logical replication. During this synchronization phase, the changes are applied and committed in the same order as they happened on the publisher. Once synchronization is done, control of the replication of the table is given back to the main apply process where replication continues as normal.

> [!NOTE]
> The publication [`publish`](#sql-createpublication-params-with-publish) parameter only affects what DML operations will be replicated. The initial data synchronization does not take this parameter into account when copying the existing table data.

## Monitoring

Because logical replication is based on a similar architecture as [physical streaming replication](#streaming-replication), the monitoring on a publication node is similar to monitoring of a physical replication primary (see [???](#streaming-replication-monitoring)).

The monitoring information about subscription is visible in [ pg_stat_subscription](#monitoring-pg-stat-subscription). This view contains one row for every subscription worker. A subscription can have zero or more active subscription workers depending on its state.

Normally, there is a single apply process running for an enabled subscription. A disabled subscription or a crashed subscription will have zero rows in this view. If the initial data synchronization of any table is in progress, there will be additional workers for the tables being synchronized. Moreover, if the [`streaming`](#sql-createsubscription-params-with-streaming) transaction is applied in parallel, there may be additional parallel apply workers.

## Security

The role used for the replication connection must have the `REPLICATION` attribute (or be a superuser). If the role lacks `SUPERUSER` and `BYPASSRLS`, publisher row security policies can execute. If the role does not trust all table owners, include `options=-crow_security=off` in the connection string; if a table owner then adds a row security policy, that setting will cause replication to halt rather than execute the policy. Access for the role must be configured in `pg_hba.conf` and it must have the `LOGIN` attribute.

The name of the output plugin used by the replication connection must be included in the server's [???](#guc-output-plugin-libraries). (For subscriptions, the plugin name that is used is `pgoutput`.) Superusers may modify the trusted list per-connection, by including `options=-coutput_plugin_libraries=...` in the connection string.

In order to be able to copy the initial table data, the role used for the replication connection must have the `SELECT` privilege on a published table (or be a superuser).

To create a publication, the user must have the `CREATE` privilege in the database.

To add tables to a publication, the user must have ownership rights on the table. To add all tables in schema to a publication, the user must be a superuser. To create a publication that publishes all tables or all tables in schema automatically, the user must be a superuser.

There are currently no privileges on publications. Any subscription (that is able to connect) can access any publication. Thus, if you intend to hide some information from particular subscribers, such as by using row filters or column lists, or by not adding the whole table to the publication, be aware that other publications in the same database could expose the same information. Publication privileges might be added to PostgreSQL in the future to allow for finer-grained access control.

To create a subscription, the user must have the privileges of the `pg_create_subscription` role, as well as `CREATE` privileges on the database.

The subscription apply process will, at a session level, run with the privileges of the subscription owner. However, when performing an insert, update, delete, or truncate operation on a particular table, it will switch roles to the table owner and perform the operation with the table owner's privileges. This means that the subscription owner needs to be able to `SET ROLE` to each role that owns a replicated table.

If the subscription has been configured with `run_as_owner = true`, then no user switching will occur. Instead, all operations will be performed with the permissions of the subscription owner. In this case, the subscription owner only needs privileges to `SELECT`, `INSERT`, `UPDATE`, and `DELETE` from the target table, and does not need privileges to `SET ROLE` to the table owner. However, this also means that any user who owns a table into which replication is happening can execute arbitrary code with the privileges of the subscription owner. For example, they could do this by simply attaching a trigger to one of the tables which they own. Because it is usually undesirable to allow one role to freely assume the privileges of another, this option should be avoided unless user security within the database is of no concern.

On the publisher, privileges are only checked once at the start of a replication connection and are not re-checked as each change record is read.

On the subscriber, the subscription owner's privileges are re-checked for each transaction when applied. If a worker is in the process of applying a transaction when the ownership of the subscription is changed by a concurrent transaction, the application of the current transaction will continue under the old owner's privileges.

## Configuration Settings

Logical replication requires several configuration options to be set. Most options are relevant only on one side of the replication. However, `max_replication_slots` is used on both the publisher and the subscriber, but it has a different meaning for each.

### Publishers

[`wal_level`](#guc-wal-level) must be set to `logical`.

[`max_replication_slots`](#guc-max-replication-slots) must be set to at least the number of subscriptions expected to connect, plus some reserve for table synchronization.

[`max_wal_senders`](#guc-max-wal-senders) should be set to at least the same as `max_replication_slots`, plus the number of physical replicas that are connected at the same time.

Logical replication walsender is also affected by [`wal_sender_timeout`](#guc-wal-sender-timeout).

### Subscribers

[`max_replication_slots`](#guc-max-replication-slots-subscriber) must be set to at least the number of subscriptions that will be added to the subscriber, plus some reserve for table synchronization.

[`max_logical_replication_workers`](#guc-max-logical-replication-workers) must be set to at least the number of subscriptions (for leader apply workers), plus some reserve for the table synchronization workers and parallel apply workers.

[`max_worker_processes`](#guc-max-worker-processes) may need to be adjusted to accommodate for replication workers, at least ([`max_logical_replication_workers`](#guc-max-logical-replication-workers) + `1`). Note, some extensions and parallel queries also take worker slots from `max_worker_processes`.

[`max_sync_workers_per_subscription`](#guc-max-sync-workers-per-subscription) controls the amount of parallelism of the initial data copy during the subscription initialization or when new tables are added.

[`max_parallel_apply_workers_per_subscription`](#guc-max-parallel-apply-workers-per-subscription) controls the amount of parallelism for streaming of in-progress transactions with subscription parameter `streaming = parallel`.

Logical replication workers are also affected by [`wal_receiver_timeout`](#guc-wal-receiver-timeout), [`wal_receiver_status_interval`](#guc-wal-receiver-status-interval) and [`wal_retrieve_retry_interval`](#guc-wal-retrieve-retry-interval).

## Quick Setup

First set the configuration options in `postgresql.conf`:

    wal_level = logical

The other required settings have default values that are sufficient for a basic setup.

`pg_hba.conf` needs to be adjusted to allow replication (the values here depend on your actual network configuration and user you want to use for connecting):

    host     all     repuser     0.0.0.0/0     md5

Then on the publisher database:

    CREATE PUBLICATION mypub FOR TABLE users, departments;

And on the subscriber database:

    CREATE SUBSCRIPTION mysub CONNECTION 'dbname=foo host=bar user=repuser' PUBLICATION mypub;

The above will start the replication process, which synchronizes the initial table contents of the tables `users` and `departments` and then starts replicating incremental changes to those tables.
