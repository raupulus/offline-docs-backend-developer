---
title: pg_buffercache — inspect PostgreSQL buffer cache state
source_url: https://www.postgresql.org/docs/17/pgbuffercache.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: pgbuffercache.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 1000
---

## pg_buffercache inspect PostgreSQL buffer cache state

pg_buffercache

The `pg_buffercache` module provides a means for examining what's happening in the shared buffer cache in real time. It also offers a low-level way to evict data from it, for testing purposes.

pg_buffercache_pages

pg_buffercache_summary

pg_buffercache_evict

This module provides the `pg_buffercache_pages()` function (wrapped in the pg_buffercache view), the `pg_buffercache_summary()` function, the `pg_buffercache_usage_counts()` function and the `pg_buffercache_evict()` function.

The `pg_buffercache_pages()` function returns a set of records, each row describing the state of one shared buffer entry. The pg_buffercache view wraps the function for convenient use.

The `pg_buffercache_summary()` function returns a single row summarizing the state of the shared buffer cache.

The `pg_buffercache_usage_counts()` function returns a set of records, each row describing the number of buffers with a given usage count.

By default, use of the above functions is restricted to superusers and roles with privileges of the `pg_monitor` role. Access may be granted to others using `GRANT`.

The `pg_buffercache_evict()` function allows a block to be evicted from the buffer pool given a buffer identifier. Use of this function is restricted to superusers only.

## The pg_buffercache View

The definitions of the columns exposed by the view are shown in [ Columns](#pgbuffercache-columns).

<table id="pgbuffercache-columns">
<caption>pg_buffercache Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">bufferid <code>integer</code></p>
<p>ID, in the range 1..<code>shared_buffers</code></p></td>
</tr>
<tr>
<td><p role="column_definition">relfilenode <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.relfilenode)</p>
<p>Filenode number of the relation</p></td>
</tr>
<tr>
<td><p role="column_definition">reltablespace <code>oid</code> (references <a href="#catalog-pg-tablespace">pg_tablespace</a>.oid)</p>
<p>Tablespace OID of the relation</p></td>
</tr>
<tr>
<td><p role="column_definition">reldatabase <code>oid</code> (references <a href="#catalog-pg-database">pg_database</a>.oid)</p>
<p>Database OID of the relation</p></td>
</tr>
<tr>
<td><p role="column_definition">relforknumber <code>smallint</code></p>
<p>Fork number within the relation; see <code>common/relpath.h</code></p></td>
</tr>
<tr>
<td><p role="column_definition">relblocknumber <code>bigint</code></p>
<p>Page number within the relation</p></td>
</tr>
<tr>
<td><p role="column_definition">isdirty <code>boolean</code></p>
<p>Is the page dirty?</p></td>
</tr>
<tr>
<td><p role="column_definition">usagecount <code>smallint</code></p>
<p>Clock-sweep access count</p></td>
</tr>
<tr>
<td><p role="column_definition">pinning_backends <code>integer</code></p>
<p>Number of backends pinning this buffer</p></td>
</tr>
</tbody>
</table>

There is one row for each buffer in the shared cache. Unused buffers are shown with all fields null except bufferid. Shared system catalogs are shown as belonging to database zero.

Because the cache is shared by all the databases, there will normally be pages from relations not belonging to the current database. This means that there may not be matching join rows in pg_class for some rows, or that there could even be incorrect joins. If you are trying to join against pg_class, it's a good idea to restrict the join to rows having reldatabase equal to the current database's OID or zero.

Since buffer manager locks are not taken to copy the buffer state data that the view will display, accessing pg_buffercache view has less impact on normal buffer activity but it doesn't provide a consistent set of results across all buffers. However, we ensure that the information of each buffer is self-consistent.

## The `pg_buffercache_summary()` Function

The definitions of the columns exposed by the function are shown in [ Output Columns](#pgbuffercache-summary-columns).

<table id="pgbuffercache-summary-columns">
<caption><code>pg_buffercache_summary()</code> Output Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">buffers_used <code>int4</code></p>
<p>Number of used shared buffers</p></td>
</tr>
<tr>
<td><p role="column_definition">buffers_unused <code>int4</code></p>
<p>Number of unused shared buffers</p></td>
</tr>
<tr>
<td><p role="column_definition">buffers_dirty <code>int4</code></p>
<p>Number of dirty shared buffers</p></td>
</tr>
<tr>
<td><p role="column_definition">buffers_pinned <code>int4</code></p>
<p>Number of pinned shared buffers</p></td>
</tr>
<tr>
<td><p role="column_definition">usagecount_avg <code>float8</code></p>
<p>Average usage count of used shared buffers</p></td>
</tr>
</tbody>
</table>

The `pg_buffercache_summary()` function returns a single row summarizing the state of all shared buffers. Similar and more detailed information is provided by the pg_buffercache view, but `pg_buffercache_summary()` is significantly cheaper.

Like the pg_buffercache view, `pg_buffercache_summary()` does not acquire buffer manager locks. Therefore concurrent activity can lead to minor inaccuracies in the result.

## The `pg_buffercache_usage_counts()` Function

The definitions of the columns exposed by the function are shown in [ Output Columns](#pgbuffercache_usage_counts-columns).

<table id="pgbuffercache_usage_counts-columns">
<caption><code>pg_buffercache_usage_counts()</code> Output Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">usage_count <code>int4</code></p>
<p>A possible buffer usage count</p></td>
</tr>
<tr>
<td><p role="column_definition">buffers <code>int4</code></p>
<p>Number of buffers with the usage count</p></td>
</tr>
<tr>
<td><p role="column_definition">dirty <code>int4</code></p>
<p>Number of dirty buffers with the usage count</p></td>
</tr>
<tr>
<td><p role="column_definition">pinned <code>int4</code></p>
<p>Number of pinned buffers with the usage count</p></td>
</tr>
</tbody>
</table>

The `pg_buffercache_usage_counts()` function returns a set of rows summarizing the states of all shared buffers, aggregated over the possible usage count values. Similar and more detailed information is provided by the pg_buffercache view, but `pg_buffercache_usage_counts()` is significantly cheaper.

Like the pg_buffercache view, `pg_buffercache_usage_counts()` does not acquire buffer manager locks. Therefore concurrent activity can lead to minor inaccuracies in the result.

## The `pg_buffercache_evict()` Function

The `pg_buffercache_evict()` function takes a buffer identifier, as shown in the bufferid column of the pg_buffercache view. It returns true on success, and false if the buffer wasn't valid, if it couldn't be evicted because it was pinned, or if it became dirty again after an attempt to write it out. The result is immediately out of date upon return, as the buffer might become valid again at any time due to concurrent activity. The function is intended for developer testing only.

## Sample Output

    regression=# SELECT n.nspname, c.relname, count(*) AS buffers
                 FROM pg_buffercache b JOIN pg_class c
                 ON b.relfilenode = pg_relation_filenode(c.oid) AND
                    b.reldatabase IN (0, (SELECT oid FROM pg_database
                                          WHERE datname = current_database()))
                 JOIN pg_namespace n ON n.oid = c.relnamespace
                 GROUP BY n.nspname, c.relname
                 ORDER BY 3 DESC
                 LIMIT 10;

      nspname   |        relname         | buffers
    ------------+------------------------+---------
     public     | delete_test_table      |     593
     public     | delete_test_table_pkey |     494
     pg_catalog | pg_attribute           |     472
     public     | quad_poly_tbl          |     353
     public     | tenk2                  |     349
     public     | tenk1                  |     349
     public     | gin_test_idx           |     306
     pg_catalog | pg_largeobject         |     206
     public     | gin_test_tbl           |     188
     public     | spgist_text_tbl        |     182
    (10 rows)

    regression=# SELECT * FROM pg_buffercache_summary();
     buffers_used | buffers_unused | buffers_dirty | buffers_pinned | usagecount_avg
    --------------+----------------+---------------+----------------+----------------
              248 |        2096904 |            39 |              0 |       3.141129
    (1 row)

    regression=# SELECT * FROM pg_buffercache_usage_counts();
     usage_count | buffers | dirty | pinned
    -------------+---------+-------+--------
               0 |   14650 |     0 |      0
               1 |    1436 |   671 |      0
               2 |     102 |    88 |      0
               3 |      23 |    21 |      0
               4 |       9 |     7 |      0
               5 |     164 |   106 |      0
    (6 rows)

## Authors

Mark Kirkwood <markir@paradise.net.nz>

Design suggestions: Neil Conway <neilc@samurai.com>

Debugging advice: Tom Lane <tgl@sss.pgh.pa.us>
