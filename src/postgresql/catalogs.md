---
title: System Catalogs
source_url: https://www.postgresql.org/docs/17/catalogs.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: catalogs.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 270
---

## System Catalogs

The system catalogs are the place where a relational database management system stores schema metadata, such as information about tables and columns, and internal bookkeeping information. PostgreSQL's system catalogs are regular tables. You can drop and recreate the tables, add columns, insert and update values, and severely mess up your system that way. Normally, one should not change the system catalogs by hand, there are normally SQL commands to do that. (For example, `CREATE DATABASE` inserts a row into the pg_database catalog and actually creates the database on disk.) There are some exceptions for particularly esoteric operations, but many of those have been made available as SQL commands over time, and so the need for direct manipulation of the system catalogs is ever decreasing.

## Overview

[System Catalogs](#catalog-table) lists the system catalogs. More detailed documentation of each catalog follows below.

Most system catalogs are copied from the template database during database creation and are thereafter database-specific. A few catalogs are physically shared across all databases in a cluster; these are noted in the descriptions of the individual catalogs.

| Catalog Name | Purpose |
|----|----|
| [pg_aggregate](#catalog-pg-aggregate) | aggregate functions |
| [pg_am](#catalog-pg-am) | relation access methods |
| [pg_amop](#catalog-pg-amop) | access method operators |
| [pg_amproc](#catalog-pg-amproc) | access method support functions |
| [pg_attrdef](#catalog-pg-attrdef) | column default values |
| [pg_attribute](#catalog-pg-attribute) | table columns (“attributes”) |
| [pg_authid](#catalog-pg-authid) | authorization identifiers (roles) |
| [pg_auth_members](#catalog-pg-auth-members) | authorization identifier membership relationships |
| [pg_cast](#catalog-pg-cast) | casts (data type conversions) |
| [pg_class](#catalog-pg-class) | tables, indexes, sequences, views (“relations”) |
| [pg_collation](#catalog-pg-collation) | collations (locale information) |
| [pg_constraint](#catalog-pg-constraint) | check constraints, unique constraints, primary key constraints, foreign key constraints |
| [pg_conversion](#catalog-pg-conversion) | encoding conversion information |
| [pg_database](#catalog-pg-database) | databases within this database cluster |
| [pg_db_role_setting](#catalog-pg-db-role-setting) | per-role and per-database settings |
| [pg_default_acl](#catalog-pg-default-acl) | default privileges for object types |
| [pg_depend](#catalog-pg-depend) | dependencies between database objects |
| [pg_description](#catalog-pg-description) | descriptions or comments on database objects |
| [pg_enum](#catalog-pg-enum) | enum label and value definitions |
| [pg_event_trigger](#catalog-pg-event-trigger) | event triggers |
| [pg_extension](#catalog-pg-extension) | installed extensions |
| [pg_foreign_data_wrapper](#catalog-pg-foreign-data-wrapper) | foreign-data wrapper definitions |
| [pg_foreign_server](#catalog-pg-foreign-server) | foreign server definitions |
| [pg_foreign_table](#catalog-pg-foreign-table) | additional foreign table information |
| [pg_index](#catalog-pg-index) | additional index information |
| [pg_inherits](#catalog-pg-inherits) | table inheritance hierarchy |
| [pg_init_privs](#catalog-pg-init-privs) | object initial privileges |
| [pg_language](#catalog-pg-language) | languages for writing functions |
| [pg_largeobject](#catalog-pg-largeobject) | data pages for large objects |
| [pg_largeobject_metadata](#catalog-pg-largeobject-metadata) | metadata for large objects |
| [pg_namespace](#catalog-pg-namespace) | schemas |
| [pg_opclass](#catalog-pg-opclass) | access method operator classes |
| [pg_operator](#catalog-pg-operator) | operators |
| [pg_opfamily](#catalog-pg-opfamily) | access method operator families |
| [pg_parameter_acl](#catalog-pg-parameter-acl) | configuration parameters for which privileges have been granted |
| [pg_partitioned_table](#catalog-pg-partitioned-table) | information about partition key of tables |
| [pg_policy](#catalog-pg-policy) | row-security policies |
| [pg_proc](#catalog-pg-proc) | functions and procedures |
| [pg_publication](#catalog-pg-publication) | publications for logical replication |
| [pg_publication_namespace](#catalog-pg-publication-namespace) | schema to publication mapping |
| [pg_publication_rel](#catalog-pg-publication-rel) | relation to publication mapping |
| [pg_range](#catalog-pg-range) | information about range types |
| [pg_replication_origin](#catalog-pg-replication-origin) | registered replication origins |
| [pg_rewrite](#catalog-pg-rewrite) | query rewrite rules |
| [pg_seclabel](#catalog-pg-seclabel) | security labels on database objects |
| [pg_sequence](#catalog-pg-sequence) | information about sequences |
| [pg_shdepend](#catalog-pg-shdepend) | dependencies on shared objects |
| [pg_shdescription](#catalog-pg-shdescription) | comments on shared objects |
| [pg_shseclabel](#catalog-pg-shseclabel) | security labels on shared database objects |
| [pg_statistic](#catalog-pg-statistic) | planner statistics |
| [pg_statistic_ext](#catalog-pg-statistic-ext) | extended planner statistics (definition) |
| [pg_statistic_ext_data](#catalog-pg-statistic-ext-data) | extended planner statistics (built statistics) |
| [pg_subscription](#catalog-pg-subscription) | logical replication subscriptions |
| [pg_subscription_rel](#catalog-pg-subscription-rel) | relation state for subscriptions |
| [pg_tablespace](#catalog-pg-tablespace) | tablespaces within this database cluster |
| [pg_transform](#catalog-pg-transform) | transforms (data type to procedural language conversions) |
| [pg_trigger](#catalog-pg-trigger) | triggers |
| [pg_ts_config](#catalog-pg-ts-config) | text search configurations |
| [pg_ts_config_map](#catalog-pg-ts-config-map) | text search configurations' token mappings |
| [pg_ts_dict](#catalog-pg-ts-dict) | text search dictionaries |
| [pg_ts_parser](#catalog-pg-ts-parser) | text search parsers |
| [pg_ts_template](#catalog-pg-ts-template) | text search templates |
| [pg_type](#catalog-pg-type) | data types |
| [pg_user_mapping](#catalog-pg-user-mapping) | mappings of users to foreign servers |

System Catalogs {#catalog-table}

## pg_aggregate

pg_aggregate

The catalog pg_aggregate stores information about aggregate functions. An aggregate function is a function that operates on a set of values (typically one column from each row that matches a query condition) and returns a single value computed from all these values. Typical aggregate functions are `sum`, `count`, and `max`. Each entry in pg_aggregate is an extension of an entry in [pg_proc](#catalog-pg-proc). The pg_proc entry carries the aggregate's name, input and output data types, and other information that is similar to ordinary functions.

<table>
<caption>pg_aggregate Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">aggfnoid <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>pg_proc OID of the aggregate function</p></td>
</tr>
<tr>
<td><p role="column_definition">aggkind <code>char</code></p>
<p>Aggregate kind: <code>n</code> for “normal” aggregates, <code>o</code> for “ordered-set” aggregates, or <code>h</code> for “hypothetical-set” aggregates</p></td>
</tr>
<tr>
<td><p role="column_definition">aggnumdirectargs <code>int2</code></p>
<p>Number of direct (non-aggregated) arguments of an ordered-set or hypothetical-set aggregate, counting a variadic array as one argument. If equal to pronargs, the aggregate must be variadic and the variadic array describes the aggregated arguments as well as the final direct arguments. Always zero for normal aggregates.</p></td>
</tr>
<tr>
<td><p role="column_definition">aggtransfn <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>Transition function</p></td>
</tr>
<tr>
<td><p role="column_definition">aggfinalfn <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>Final function (zero if none)</p></td>
</tr>
<tr>
<td><p role="column_definition">aggcombinefn <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>Combine function (zero if none)</p></td>
</tr>
<tr>
<td><p role="column_definition">aggserialfn <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>Serialization function (zero if none)</p></td>
</tr>
<tr>
<td><p role="column_definition">aggdeserialfn <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>Deserialization function (zero if none)</p></td>
</tr>
<tr>
<td><p role="column_definition">aggmtransfn <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>Forward transition function for moving-aggregate mode (zero if none)</p></td>
</tr>
<tr>
<td><p role="column_definition">aggminvtransfn <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>Inverse transition function for moving-aggregate mode (zero if none)</p></td>
</tr>
<tr>
<td><p role="column_definition">aggmfinalfn <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>Final function for moving-aggregate mode (zero if none)</p></td>
</tr>
<tr>
<td><p role="column_definition">aggfinalextra <code>bool</code></p>
<p>True to pass extra dummy arguments to aggfinalfn</p></td>
</tr>
<tr>
<td><p role="column_definition">aggmfinalextra <code>bool</code></p>
<p>True to pass extra dummy arguments to aggmfinalfn</p></td>
</tr>
<tr>
<td><p role="column_definition">aggfinalmodify <code>char</code></p>
<p>Whether aggfinalfn modifies the transition state value: <code>r</code> if it is read-only, <code>s</code> if the aggtransfn cannot be applied after the aggfinalfn, or <code>w</code> if it writes on the value</p></td>
</tr>
<tr>
<td><p role="column_definition">aggmfinalmodify <code>char</code></p>
<p>Like aggfinalmodify, but for the aggmfinalfn</p></td>
</tr>
<tr>
<td><p role="column_definition">aggsortop <code>oid</code> (references <a href="#catalog-pg-operator">pg_operator</a>.oid)</p>
<p>Associated sort operator (zero if none)</p></td>
</tr>
<tr>
<td><p role="column_definition">aggtranstype <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>Data type of the aggregate function's internal transition (state) data</p></td>
</tr>
<tr>
<td><p role="column_definition">aggtransspace <code>int4</code></p>
<p>Approximate average size (in bytes) of the transition state data, or zero to use a default estimate</p></td>
</tr>
<tr>
<td><p role="column_definition">aggmtranstype <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>Data type of the aggregate function's internal transition (state) data for moving-aggregate mode (zero if none)</p></td>
</tr>
<tr>
<td><p role="column_definition">aggmtransspace <code>int4</code></p>
<p>Approximate average size (in bytes) of the transition state data for moving-aggregate mode, or zero to use a default estimate</p></td>
</tr>
<tr>
<td><p role="column_definition">agginitval <code>text</code></p>
<p>The initial value of the transition state. This is a text field containing the initial value in its external string representation. If this field is null, the transition state value starts out null.</p></td>
</tr>
<tr>
<td><p role="column_definition">aggminitval <code>text</code></p>
<p>The initial value of the transition state for moving-aggregate mode. This is a text field containing the initial value in its external string representation. If this field is null, the transition state value starts out null.</p></td>
</tr>
</tbody>
</table>

New aggregate functions are registered with the [`CREATE AGGREGATE`](#sql-createaggregate) command. See [???](#xaggr) for more information about writing aggregate functions and the meaning of the transition functions, etc.

## pg_am

pg_am

The catalog pg_am stores information about relation access methods. There is one row for each access method supported by the system. Currently, only tables and indexes have access methods. The requirements for table and index access methods are discussed in detail in [???](#tableam) and [???](#indexam) respectively.

<table>
<caption>pg_am Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">amname <code>name</code></p>
<p>Name of the access method</p></td>
</tr>
<tr>
<td><p role="column_definition">amhandler <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>OID of a handler function that is responsible for supplying information about the access method</p></td>
</tr>
<tr>
<td><p role="column_definition">amtype <code>char</code></p>
<p><code>t</code> = table (including materialized views), <code>i</code> = index.</p></td>
</tr>
</tbody>
</table>

> [!NOTE]
> Before PostgreSQL 9.6, pg_am contained many additional columns representing properties of index access methods. That data is now only directly visible at the C code level. However, `pg_index_column_has_property()` and related functions have been added to allow SQL queries to inspect index access method properties; see [???](#functions-info-catalog-table).

## pg_amop

pg_amop

The catalog pg_amop stores information about operators associated with access method operator families. There is one row for each operator that is a member of an operator family. A family member can be either a search operator or an ordering operator. An operator can appear in more than one family, but cannot appear in more than one search position nor more than one ordering position within a family. (It is allowed, though unlikely, for an operator to be used for both search and ordering purposes.)

<table>
<caption>pg_amop Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">amopfamily <code>oid</code> (references <a href="#catalog-pg-opfamily">pg_opfamily</a>.oid)</p>
<p>The operator family this entry is for</p></td>
</tr>
<tr>
<td><p role="column_definition">amoplefttype <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>Left-hand input data type of operator</p></td>
</tr>
<tr>
<td><p role="column_definition">amoprighttype <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>Right-hand input data type of operator</p></td>
</tr>
<tr>
<td><p role="column_definition">amopstrategy <code>int2</code></p>
<p>Operator strategy number</p></td>
</tr>
<tr>
<td><p role="column_definition">amoppurpose <code>char</code></p>
<p>Operator purpose, either <code>s</code> for search or <code>o</code> for ordering</p></td>
</tr>
<tr>
<td><p role="column_definition">amopopr <code>oid</code> (references <a href="#catalog-pg-operator">pg_operator</a>.oid)</p>
<p>OID of the operator</p></td>
</tr>
<tr>
<td><p role="column_definition">amopmethod <code>oid</code> (references <a href="#catalog-pg-am">pg_am</a>.oid)</p>
<p>Index access method operator family is for</p></td>
</tr>
<tr>
<td><p role="column_definition">amopsortfamily <code>oid</code> (references <a href="#catalog-pg-opfamily">pg_opfamily</a>.oid)</p>
<p>The B-tree operator family this entry sorts according to, if an ordering operator; zero if a search operator</p></td>
</tr>
</tbody>
</table>

A “search” operator entry indicates that an index of this operator family can be searched to find all rows satisfying `WHERE` \<indexed_column\> \<operator\> \<constant\>. Obviously, such an operator must return `boolean`, and its left-hand input type must match the index's column data type.

An “ordering” operator entry indicates that an index of this operator family can be scanned to return rows in the order represented by `ORDER BY` \<indexed_column\> \<operator\> \<constant\>. Such an operator could return any sortable data type, though again its left-hand input type must match the index's column data type. The exact semantics of the `ORDER BY` are specified by the amopsortfamily column, which must reference a B-tree operator family for the operator's result type.

> [!NOTE]
> At present, it's assumed that the sort order for an ordering operator is the default for the referenced operator family, i.e., `ASC NULLS LAST`. This might someday be relaxed by adding additional columns to specify sort options explicitly.

An entry's amopmethod must match the opfmethod of its containing operator family (including amopmethod here is an intentional denormalization of the catalog structure for performance reasons). Also, amoplefttype and amoprighttype must match the oprleft and oprright fields of the referenced [pg_operator](#catalog-pg-operator) entry.

## pg_amproc

pg_amproc

The catalog pg_amproc stores information about support functions associated with access method operator families. There is one row for each support function belonging to an operator family.

<table>
<caption>pg_amproc Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">amprocfamily <code>oid</code> (references <a href="#catalog-pg-opfamily">pg_opfamily</a>.oid)</p>
<p>The operator family this entry is for</p></td>
</tr>
<tr>
<td><p role="column_definition">amproclefttype <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>Left-hand input data type of associated operator</p></td>
</tr>
<tr>
<td><p role="column_definition">amprocrighttype <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>Right-hand input data type of associated operator</p></td>
</tr>
<tr>
<td><p role="column_definition">amprocnum <code>int2</code></p>
<p>Support function number</p></td>
</tr>
<tr>
<td><p role="column_definition">amproc <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>OID of the function</p></td>
</tr>
</tbody>
</table>

The usual interpretation of the amproclefttype and amprocrighttype fields is that they identify the left and right input types of the operator(s) that a particular support function supports. For some access methods these match the input data type(s) of the support function itself, for others not. There is a notion of “default” support functions for an index, which are those with amproclefttype and amprocrighttype both equal to the index operator class's opcintype.

## pg_attrdef

pg_attrdef

The catalog pg_attrdef stores column default values. The main information about columns is stored in [pg_attribute](#catalog-pg-attribute). Only columns for which a default value has been explicitly set will have an entry here.

<table>
<caption>pg_attrdef Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">adrelid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The table this column belongs to</p></td>
</tr>
<tr>
<td><p role="column_definition">adnum <code>int2</code> (references <a href="#catalog-pg-attribute">pg_attribute</a>.attnum)</p>
<p>The number of the column</p></td>
</tr>
<tr>
<td><p role="column_definition">adbin <code>pg_node_tree</code></p>
<p>The column default value, in <code>nodeToString()</code> representation. Use <code>pg_get_expr(adbin, adrelid)</code> to convert it to an SQL expression.</p></td>
</tr>
</tbody>
</table>

## pg_attribute

pg_attribute

The catalog pg_attribute stores information about table columns. There will be exactly one pg_attribute row for every column in every table in the database. (There will also be attribute entries for indexes, and indeed all objects that have [pg_class](#catalog-pg-class) entries.)

The term attribute is equivalent to column and is used for historical reasons.

<table>
<caption>pg_attribute Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">attrelid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The table this column belongs to</p></td>
</tr>
<tr>
<td><p role="column_definition">attname <code>name</code></p>
<p>The column name</p></td>
</tr>
<tr>
<td><p role="column_definition">atttypid <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>The data type of this column (zero for a dropped column)</p></td>
</tr>
<tr>
<td><p role="column_definition">attlen <code>int2</code></p>
<p>A copy of <code>pg_type.typlen</code> of this column's type</p></td>
</tr>
<tr>
<td><p role="column_definition">attnum <code>int2</code></p>
<p>The number of the column. Ordinary columns are numbered from 1 up. System columns, such as ctid, have (arbitrary) negative numbers.</p></td>
</tr>
<tr>
<td><p role="column_definition">attcacheoff <code>int4</code></p>
<p>Always -1 in storage, but when loaded into a row descriptor in memory this might be updated to cache the offset of the attribute within the row</p></td>
</tr>
<tr>
<td><p role="column_definition">atttypmod <code>int4</code></p>
<p>atttypmod records type-specific data supplied at table creation time (for example, the maximum length of a <code>varchar</code> column). It is passed to type-specific input functions and length coercion functions. The value will generally be -1 for types that do not need atttypmod.</p></td>
</tr>
<tr>
<td><p role="column_definition">attndims <code>int2</code></p>
<p>Number of dimensions, if the column is an array type; otherwise 0. (Presently, the number of dimensions of an array is not enforced, so any nonzero value effectively means “it's an array”.)</p></td>
</tr>
<tr>
<td><p role="column_definition">attbyval <code>bool</code></p>
<p>A copy of <code>pg_type.typbyval</code> of this column's type</p></td>
</tr>
<tr>
<td><p role="column_definition">attalign <code>char</code></p>
<p>A copy of <code>pg_type.typalign</code> of this column's type</p></td>
</tr>
<tr>
<td><p role="column_definition">attstorage <code>char</code></p>
<p>Normally a copy of <code>pg_type.typstorage</code> of this column's type. For TOAST-able data types, this can be altered after column creation to control storage policy.</p></td>
</tr>
<tr>
<td><p role="column_definition">attcompression <code>char</code></p>
<p>The current compression method of the column. Typically this is <code>'\0'</code> to specify use of the current default setting (see <a href="#guc-default-toast-compression">???</a>). Otherwise, <code>'p'</code> selects pglz compression, while <code>'l'</code> selects LZ4 compression. However, this field is ignored whenever attstorage does not allow compression.</p></td>
</tr>
<tr>
<td><p role="column_definition">attnotnull <code>bool</code></p>
<p>This represents a not-null constraint.</p></td>
</tr>
<tr>
<td><p role="column_definition">atthasdef <code>bool</code></p>
<p>This column has a default expression or generation expression, in which case there will be a corresponding entry in the <a href="#catalog-pg-attrdef">pg_attrdef</a> catalog that actually defines the expression. (Check attgenerated to determine whether this is a default or a generation expression.)</p></td>
</tr>
<tr>
<td><p role="column_definition">atthasmissing <code>bool</code></p>
<p>This column has a value which is used where the column is entirely missing from the row, as happens when a column is added with a non-volatile <code>DEFAULT</code> value after the row is created. The actual value used is stored in the attmissingval column.</p></td>
</tr>
<tr>
<td><p role="column_definition">attidentity <code>char</code></p>
<p>If a zero byte (<code>''</code>), then not an identity column. Otherwise, <code>a</code> = generated always, <code>d</code> = generated by default.</p></td>
</tr>
<tr>
<td><p role="column_definition">attgenerated <code>char</code></p>
<p>If a zero byte (<code>''</code>), then not a generated column. Otherwise, <code>s</code> = stored. (Other values might be added in the future.)</p></td>
</tr>
<tr>
<td><p role="column_definition">attisdropped <code>bool</code></p>
<p>This column has been dropped and is no longer valid. A dropped column is still physically present in the table, but is ignored by the parser and so cannot be accessed via SQL.</p></td>
</tr>
<tr>
<td><p role="column_definition">attislocal <code>bool</code></p>
<p>This column is defined locally in the relation. Note that a column can be locally defined and inherited simultaneously.</p></td>
</tr>
<tr>
<td><p role="column_definition">attinhcount <code>int2</code></p>
<p>The number of direct ancestors this column has. A column with a nonzero number of ancestors cannot be dropped nor renamed.</p></td>
</tr>
<tr>
<td><p role="column_definition">attcollation <code>oid</code> (references <a href="#catalog-pg-collation">pg_collation</a>.oid)</p>
<p>The defined collation of the column, or zero if the column is not of a collatable data type</p></td>
</tr>
<tr>
<td><p role="column_definition">attstattarget <code>int2</code></p>
<p>attstattarget controls the level of detail of statistics accumulated for this column by <a href="#sql-analyze"><code>ANALYZE</code></a>. A zero value indicates that no statistics should be collected. A null value says to use the system default statistics target. The exact meaning of positive values is data type-dependent. For scalar data types, attstattarget is both the target number of “most common values” to collect, and the target number of histogram bins to create.</p></td>
</tr>
<tr>
<td><p role="column_definition">attacl <code>aclitem[]</code></p>
<p>Column-level access privileges, if any have been granted specifically on this column</p></td>
</tr>
<tr>
<td><p role="column_definition">attoptions <code>text[]</code></p>
<p>Attribute-level options, as “keyword=value” strings</p></td>
</tr>
<tr>
<td><p role="column_definition">attfdwoptions <code>text[]</code></p>
<p>Attribute-level foreign data wrapper options, as “keyword=value” strings</p></td>
</tr>
<tr>
<td><p role="column_definition">attmissingval <code>anyarray</code></p>
<p>This column has a one element array containing the value used when the column is entirely missing from the row, as happens when the column is added with a non-volatile <code>DEFAULT</code> value after the row is created. The value is only used when atthasmissing is true. If there is no value the column is null.</p></td>
</tr>
</tbody>
</table>

In a dropped column's pg_attribute entry, atttypid is reset to zero, but attlen and the other fields copied from [pg_type](#catalog-pg-type) are still valid. This arrangement is needed to cope with the situation where the dropped column's data type was later dropped, and so there is no pg_type row anymore. attlen and the other fields can be used to interpret the contents of a row of the table.

## pg_authid

pg_authid

The catalog pg_authid contains information about database authorization identifiers (roles). A role subsumes the concepts of “users” and “groups”. A user is essentially just a role with the rolcanlogin flag set. Any role (with or without rolcanlogin) can have other roles as members; see [pg_auth_members](#catalog-pg-auth-members).

Since this catalog contains passwords, it must not be publicly readable. [pg_roles](#view-pg-roles) is a publicly readable view on pg_authid that blanks out the password field.

[???](#user-manag) contains detailed information about user and privilege management.

Because user identities are cluster-wide, pg_authid is shared across all databases of a cluster: there is only one copy of pg_authid per cluster, not one per database.

<table>
<caption>pg_authid Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">rolname <code>name</code></p>
<p>Role name</p></td>
</tr>
<tr>
<td><p role="column_definition">rolsuper <code>bool</code></p>
<p>Role has superuser privileges</p></td>
</tr>
<tr>
<td><p role="column_definition">rolinherit <code>bool</code></p>
<p>Role automatically inherits privileges of roles it is a member of</p></td>
</tr>
<tr>
<td><p role="column_definition">rolcreaterole <code>bool</code></p>
<p>Role can create more roles</p></td>
</tr>
<tr>
<td><p role="column_definition">rolcreatedb <code>bool</code></p>
<p>Role can create databases</p></td>
</tr>
<tr>
<td><p role="column_definition">rolcanlogin <code>bool</code></p>
<p>Role can log in. That is, this role can be given as the initial session authorization identifier.</p></td>
</tr>
<tr>
<td><p role="column_definition">rolreplication <code>bool</code></p>
<p>Role is a replication role. A replication role can initiate replication connections and create and drop replication slots.</p></td>
</tr>
<tr>
<td><p role="column_definition">rolbypassrls <code>bool</code></p>
<p>Role bypasses every row-level security policy, see <a href="#ddl-rowsecurity">???</a> for more information.</p></td>
</tr>
<tr>
<td><p role="column_definition">rolconnlimit <code>int4</code></p>
<p>For roles that can log in, this sets maximum number of concurrent connections this role can make. -1 means no limit.</p></td>
</tr>
<tr>
<td><p role="column_definition">rolpassword <code>text</code></p>
<p>Encrypted password; null if none. The format depends on the form of encryption used.</p></td>
</tr>
<tr>
<td><p role="column_definition">rolvaliduntil <code>timestamptz</code></p>
<p>Password expiry time (only used for password authentication); null if no expiration</p></td>
</tr>
</tbody>
</table>

For an MD5 encrypted password, rolpassword column will begin with the string `md5` followed by a 32-character hexadecimal MD5 hash. The MD5 hash will be of the user's password concatenated to their user name. For example, if user `joe` has password `xyzzy`, PostgreSQL will store the md5 hash of `xyzzyjoe`.

If the password is encrypted with SCRAM-SHA-256, it has the format: SCRAM-SHA-256\$\<\<iteration count\>\>:\<\<salt\>\>\$\<\<StoredKey\>\>:\<\<ServerKey\>\> where \<salt\>, \<StoredKey\> and \<ServerKey\> are in Base64 encoded format. This format is the same as that specified by [RFC 5803](https://datatracker.ietf.org/doc/html/rfc5803).

## pg_auth_members

pg_auth_members

The catalog pg_auth_members shows the membership relations between roles. Any non-circular set of relationships is allowed.

Because user identities are cluster-wide, pg_auth_members is shared across all databases of a cluster: there is only one copy of pg_auth_members per cluster, not one per database.

<table>
<caption>pg_auth_members Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">roleid <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>ID of a role that has a member</p></td>
</tr>
<tr>
<td><p role="column_definition">member <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>ID of a role that is a member of roleid</p></td>
</tr>
<tr>
<td><p role="column_definition">grantor <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>ID of the role that granted this membership</p></td>
</tr>
<tr>
<td><p role="column_definition">admin_option <code>bool</code></p>
<p>True if member can grant membership in roleid to others</p></td>
</tr>
<tr>
<td><p role="column_definition">inherit_option <code>bool</code></p>
<p>True if the member automatically inherits the privileges of the granted role</p></td>
</tr>
<tr>
<td><p role="column_definition">set_option <code>bool</code></p>
<p>True if the member can <a href="#sql-set-role"><code>SET ROLE</code></a> to the granted role</p></td>
</tr>
</tbody>
</table>

## pg_cast

pg_cast

The catalog pg_cast stores data type conversion paths, both built-in and user-defined.

It should be noted that pg_cast does not represent every type conversion that the system knows how to perform; only those that cannot be deduced from some generic rule. For example, casting between a domain and its base type is not explicitly represented in pg_cast. Another important exception is that “automatic I/O conversion casts”, those performed using a data type's own I/O functions to convert to or from `text` or other string types, are not explicitly represented in pg_cast.

<table>
<caption>pg_cast Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">castsource <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>OID of the source data type</p></td>
</tr>
<tr>
<td><p role="column_definition">casttarget <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>OID of the target data type</p></td>
</tr>
<tr>
<td><p role="column_definition">castfunc <code>oid</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>The OID of the function to use to perform this cast. Zero is stored if the cast method doesn't require a function.</p></td>
</tr>
<tr>
<td><p role="column_definition">castcontext <code>char</code></p>
<p>Indicates what contexts the cast can be invoked in. <code>e</code> means only as an explicit cast (using <code>CAST</code> or <code>::</code> syntax). <code>a</code> means implicitly in assignment to a target column, as well as explicitly. <code>i</code> means implicitly in expressions, as well as the other cases.</p></td>
</tr>
<tr>
<td><p role="column_definition">castmethod <code>char</code></p>
<p>Indicates how the cast is performed. <code>f</code> means that the function specified in the castfunc field is used. <code>i</code> means that the input/output functions are used. <code>b</code> means that the types are binary-coercible, thus no conversion is required.</p></td>
</tr>
</tbody>
</table>

The cast functions listed in pg_cast must always take the cast source type as their first argument type, and return the cast destination type as their result type. A cast function can have up to three arguments. The second argument, if present, must be type `integer`; it receives the type modifier associated with the destination type, or -1 if there is none. The third argument, if present, must be type `boolean`; it receives `true` if the cast is an explicit cast, `false` otherwise.

It is legitimate to create a pg_cast entry in which the source and target types are the same, if the associated function takes more than one argument. Such entries represent “length coercion functions” that coerce values of the type to be legal for a particular type modifier value.

When a pg_cast entry has different source and target types and a function that takes more than one argument, it represents converting from one type to another and applying a length coercion in a single step. When no such entry is available, coercion to a type that uses a type modifier involves two steps, one to convert between data types and a second to apply the modifier.

## pg_class

pg_class

The catalog pg_class describes tables and other objects that have columns or are otherwise similar to a table. This includes indexes (but see also [pg_index](#catalog-pg-index)), sequences (but see also [pg_sequence](#catalog-pg-sequence)), views, materialized views, composite types, and TOAST tables; see relkind. Below, when we mean all of these kinds of objects we speak of “relations”. Not all of pg_class's columns are meaningful for all relation kinds.

<table>
<caption>pg_class Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">relname <code>name</code></p>
<p>Name of the table, index, view, etc.</p></td>
</tr>
<tr>
<td><p role="column_definition">relnamespace <code>oid</code> (references <a href="#catalog-pg-namespace">pg_namespace</a>.oid)</p>
<p>The OID of the namespace that contains this relation</p></td>
</tr>
<tr>
<td><p role="column_definition">reltype <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>The OID of the data type that corresponds to this table's row type, if any; zero for indexes, sequences, and toast tables, which have no pg_type entry</p></td>
</tr>
<tr>
<td><p role="column_definition">reloftype <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>For typed tables, the OID of the underlying composite type; zero for all other relations</p></td>
</tr>
<tr>
<td><p role="column_definition">relowner <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>Owner of the relation</p></td>
</tr>
<tr>
<td><p role="column_definition">relam <code>oid</code> (references <a href="#catalog-pg-am">pg_am</a>.oid)</p>
<p>The access method used to access this table or index. Not meaningful if the relation is a sequence or has no on-disk file, except for partitioned tables, where, if set, it takes precedence over <code>default_table_access_method</code> when determining the access method to use for partitions created when one is not specified in the creation command.</p></td>
</tr>
<tr>
<td><p role="column_definition">relfilenode <code>oid</code></p>
<p>Name of the on-disk file of this relation; zero means this is a “mapped” relation whose disk file name is determined by low-level state</p></td>
</tr>
<tr>
<td><p role="column_definition">reltablespace <code>oid</code> (references <a href="#catalog-pg-tablespace">pg_tablespace</a>.oid)</p>
<p>The tablespace in which this relation is stored. If zero, the database's default tablespace is implied. Not meaningful if the relation has no on-disk file, except for partitioned tables, where this is the tablespace in which partitions will be created when one is not specified in the creation command.</p></td>
</tr>
<tr>
<td><p role="column_definition">relpages <code>int4</code></p>
<p>Size of the on-disk representation of this table in pages (of size <code>BLCKSZ</code>). This is only an estimate used by the planner. It is updated by <a href="#sql-vacuum"><code>VACUUM</code></a>, <a href="#sql-analyze"><code>ANALYZE</code></a>, and a few DDL commands such as <a href="#sql-createindex"><code>CREATE INDEX</code></a>.</p></td>
</tr>
<tr>
<td><p role="column_definition">reltuples <code>float4</code></p>
<p>Number of live rows in the table. This is only an estimate used by the planner. It is updated by <a href="#sql-vacuum"><code>VACUUM</code></a>, <a href="#sql-analyze"><code>ANALYZE</code></a>, and a few DDL commands such as <a href="#sql-createindex"><code>CREATE INDEX</code></a>. If the table has never yet been vacuumed or analyzed, reltuples contains <code>-1</code> indicating that the row count is unknown.</p></td>
</tr>
<tr>
<td><p role="column_definition">relallvisible <code>int4</code></p>
<p>Number of pages that are marked all-visible in the table's visibility map. This is only an estimate used by the planner. It is updated by <a href="#sql-vacuum"><code>VACUUM</code></a>, <a href="#sql-analyze"><code>ANALYZE</code></a>, and a few DDL commands such as <a href="#sql-createindex"><code>CREATE INDEX</code></a>.</p></td>
</tr>
<tr>
<td><p role="column_definition">reltoastrelid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>OID of the TOAST table associated with this table, zero if none. The TOAST table stores large attributes “out of line” in a secondary table.</p></td>
</tr>
<tr>
<td><p role="column_definition">relhasindex <code>bool</code></p>
<p>True if this is a table and it has (or recently had) any indexes</p></td>
</tr>
<tr>
<td><p role="column_definition">relisshared <code>bool</code></p>
<p>True if this table is shared across all databases in the cluster. Only certain system catalogs (such as <a href="#catalog-pg-database">pg_database</a>) are shared.</p></td>
</tr>
<tr>
<td><p role="column_definition">relpersistence <code>char</code></p>
<p><code>p</code> = permanent table/sequence, <code>u</code> = unlogged table/sequence, <code>t</code> = temporary table/sequence</p></td>
</tr>
<tr>
<td><p role="column_definition">relkind <code>char</code></p>
<p><code>r</code> = ordinary table, <code>i</code> = index, <code>S</code> = sequence, <code>t</code> = TOAST table, <code>v</code> = view, <code>m</code> = materialized view, <code>c</code> = composite type, <code>f</code> = foreign table, <code>p</code> = partitioned table, <code>I</code> = partitioned index</p></td>
</tr>
<tr>
<td><p role="column_definition">relnatts <code>int2</code></p>
<p>Number of user columns in the relation (system columns not counted). There must be this many corresponding entries in <a href="#catalog-pg-attribute">pg_attribute</a>. See also pg_attribute.attnum.</p></td>
</tr>
<tr>
<td><p role="column_definition">relchecks <code>int2</code></p>
<p>Number of <code>CHECK</code> constraints on the table; see <a href="#catalog-pg-constraint">pg_constraint</a> catalog</p></td>
</tr>
<tr>
<td><p role="column_definition">relhasrules <code>bool</code></p>
<p>True if table has (or once had) rules; see <a href="#catalog-pg-rewrite">pg_rewrite</a> catalog</p></td>
</tr>
<tr>
<td><p role="column_definition">relhastriggers <code>bool</code></p>
<p>True if table has (or once had) triggers; see <a href="#catalog-pg-trigger">pg_trigger</a> catalog</p></td>
</tr>
<tr>
<td><p role="column_definition">relhassubclass <code>bool</code></p>
<p>True if table or index has (or once had) any inheritance children or partitions</p></td>
</tr>
<tr>
<td><p role="column_definition">relrowsecurity <code>bool</code></p>
<p>True if table has row-level security enabled; see <a href="#catalog-pg-policy">pg_policy</a> catalog</p></td>
</tr>
<tr>
<td><p role="column_definition">relforcerowsecurity <code>bool</code></p>
<p>True if row-level security (when enabled) will also apply to table owner; see <a href="#catalog-pg-policy">pg_policy</a> catalog</p></td>
</tr>
<tr>
<td><p role="column_definition">relispopulated <code>bool</code></p>
<p>True if relation is populated (this is true for all relations other than some materialized views)</p></td>
</tr>
<tr>
<td><p role="column_definition">relreplident <code>char</code></p>
<p>Columns used to form “replica identity” for rows: <code>d</code> = default (primary key, if any), <code>n</code> = nothing, <code>f</code> = all columns, <code>i</code> = index with indisreplident set (same as nothing if the index used has been dropped)</p></td>
</tr>
<tr>
<td><p role="column_definition">relispartition <code>bool</code></p>
<p>True if table or index is a partition</p></td>
</tr>
<tr>
<td><p role="column_definition">relrewrite <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>For new relations being written during a DDL operation that requires a table rewrite, this contains the OID of the original relation; otherwise zero. That state is only visible internally; this field should never contain anything other than zero for a user-visible relation.</p></td>
</tr>
<tr>
<td><p role="column_definition">relfrozenxid <code>xid</code></p>
<p>All transaction IDs before this one have been replaced with a permanent (“frozen”) transaction ID in this table. This is used to track whether the table needs to be vacuumed in order to prevent transaction ID wraparound or to allow <code>pg_xact</code> to be shrunk. Zero (<code>InvalidTransactionId</code>) if the relation is not a table.</p></td>
</tr>
<tr>
<td><p role="column_definition">relminmxid <code>xid</code></p>
<p>All multixact IDs before this one have been replaced by a transaction ID in this table. This is used to track whether the table needs to be vacuumed in order to prevent multixact ID wraparound or to allow <code>pg_multixact</code> to be shrunk. Zero (<code>InvalidMultiXactId</code>) if the relation is not a table.</p></td>
</tr>
<tr>
<td><p role="column_definition">relacl <code>aclitem[]</code></p>
<p>Access privileges; see <a href="#ddl-priv">???</a> for details</p></td>
</tr>
<tr>
<td><p role="column_definition">reloptions <code>text[]</code></p>
<p>Access-method-specific options, as “keyword=value” strings</p></td>
</tr>
<tr>
<td><p role="column_definition">relpartbound <code>pg_node_tree</code></p>
<p>If table is a partition (see relispartition), internal representation of the partition bound</p></td>
</tr>
</tbody>
</table>

Several of the Boolean flags in pg_class are maintained lazily: they are guaranteed to be true if that's the correct state, but may not be reset to false immediately when the condition is no longer true. For example, relhasindex is set by [`CREATE INDEX`](#sql-createindex), but it is never cleared by [`DROP INDEX`](#sql-dropindex). Instead, [`VACUUM`](#sql-vacuum) clears relhasindex if it finds the table has no indexes. This arrangement avoids race conditions and improves concurrency.

## pg_collation

pg_collation

The catalog pg_collation describes the available collations, which are essentially mappings from an SQL name to operating system locale categories. See [???](#collation) for more information.

<table>
<caption>pg_collation Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">collname <code>name</code></p>
<p>Collation name (unique per namespace and encoding)</p></td>
</tr>
<tr>
<td><p role="column_definition">collnamespace <code>oid</code> (references <a href="#catalog-pg-namespace">pg_namespace</a>.oid)</p>
<p>The OID of the namespace that contains this collation</p></td>
</tr>
<tr>
<td><p role="column_definition">collowner <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>Owner of the collation</p></td>
</tr>
<tr>
<td><p role="column_definition">collprovider <code>char</code></p>
<p>Provider of the collation: <code>d</code> = database default, <code>b</code> = builtin, <code>c</code> = libc, <code>i</code> = icu</p></td>
</tr>
<tr>
<td><p role="column_definition">collisdeterministic <code>bool</code></p>
<p>Is the collation deterministic?</p></td>
</tr>
<tr>
<td><p role="column_definition">collencoding <code>int4</code></p>
<p>Encoding in which the collation is applicable, or -1 if it works for any encoding</p></td>
</tr>
<tr>
<td><p role="column_definition">collcollate <code>text</code></p>
<p><code>LC_COLLATE</code> for this collation object. If the provider is not <code>libc</code>, collcollate is <code>NULL</code> and colllocale is used instead.</p></td>
</tr>
<tr>
<td><p role="column_definition">collctype <code>text</code></p>
<p><code>LC_CTYPE</code> for this collation object. If the provider is not <code>libc</code>, collctype is <code>NULL</code> and colllocale is used instead.</p></td>
</tr>
<tr>
<td><p role="column_definition">colllocale <code>text</code></p>
<p>Collation provider locale name for this collation object. If the provider is <code>libc</code>, colllocale is <code>NULL</code>; collcollate and collctype are used instead.</p></td>
</tr>
<tr>
<td><p role="column_definition">collicurules <code>text</code></p>
<p>ICU collation rules for this collation object</p></td>
</tr>
<tr>
<td><p role="column_definition">collversion <code>text</code></p>
<p>Provider-specific version of the collation. This is recorded when the collation is created and then checked when it is used, to detect changes in the collation definition that could lead to data corruption.</p></td>
</tr>
</tbody>
</table>

Note that the unique key on this catalog is (collname, collencoding, collnamespace) not just (collname, collnamespace). PostgreSQL generally ignores all collations that do not have collencoding equal to either the current database's encoding or -1, and creation of new entries with the same name as an entry with collencoding = -1 is forbidden. Therefore it is sufficient to use a qualified SQL name (\<schema\>.\<name\>) to identify a collation, even though this is not unique according to the catalog definition. The reason for defining the catalog this way is that initdb fills it in at cluster initialization time with entries for all locales available on the system, so it must be able to hold entries for all encodings that might ever be used in the cluster.

In the `template0` database, it could be useful to create collations whose encoding does not match the database encoding, since they could match the encodings of databases later cloned from `template0`. This would currently have to be done manually.

## pg_constraint

pg_constraint

The catalog pg_constraint stores check, primary key, unique, foreign key, and exclusion constraints on tables, as well as not-null constraints on domains. (Column constraints are not treated specially. Every column constraint is equivalent to some table constraint.) Not-null constraints on relations are represented in the [pg_attribute](#catalog-pg-attribute) catalog, not here.

User-defined constraint triggers (created with [ `CREATE CONSTRAINT TRIGGER`](#sql-createtrigger)) also give rise to an entry in this table.

Check constraints on domains are stored here, too.

<table>
<caption>pg_constraint Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">conname <code>name</code></p>
<p>Constraint name (not necessarily unique!)</p></td>
</tr>
<tr>
<td><p role="column_definition">connamespace <code>oid</code> (references <a href="#catalog-pg-namespace">pg_namespace</a>.oid)</p>
<p>The OID of the namespace that contains this constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">contype <code>char</code></p>
<p><code>c</code> = check constraint, <code>f</code> = foreign key constraint, <code>n</code> = not-null constraint (domains only), <code>p</code> = primary key constraint, <code>u</code> = unique constraint, <code>t</code> = constraint trigger, <code>x</code> = exclusion constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">condeferrable <code>bool</code></p>
<p>Is the constraint deferrable?</p></td>
</tr>
<tr>
<td><p role="column_definition">condeferred <code>bool</code></p>
<p>Is the constraint deferred by default?</p></td>
</tr>
<tr>
<td><p role="column_definition">convalidated <code>bool</code></p>
<p>Has the constraint been validated? Currently, can be false only for foreign keys and CHECK constraints</p></td>
</tr>
<tr>
<td><p role="column_definition">conrelid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The table this constraint is on; zero if not a table constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">contypid <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>The domain this constraint is on; zero if not a domain constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">conindid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The index supporting this constraint, if it's a unique, primary key, foreign key, or exclusion constraint; else zero</p></td>
</tr>
<tr>
<td><p role="column_definition">conparentid <code>oid</code> (references <a href="#catalog-pg-constraint">pg_constraint</a>.oid)</p>
<p>The corresponding constraint of the parent partitioned table, if this is a constraint on a partition; else zero</p></td>
</tr>
<tr>
<td><p role="column_definition">confrelid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>If a foreign key, the referenced table; else zero</p></td>
</tr>
<tr>
<td><p role="column_definition">confupdtype <code>char</code></p>
<p>Foreign key update action code: <code>a</code> = no action, <code>r</code> = restrict, <code>c</code> = cascade, <code>n</code> = set null, <code>d</code> = set default</p></td>
</tr>
<tr>
<td><p role="column_definition">confdeltype <code>char</code></p>
<p>Foreign key deletion action code: <code>a</code> = no action, <code>r</code> = restrict, <code>c</code> = cascade, <code>n</code> = set null, <code>d</code> = set default</p></td>
</tr>
<tr>
<td><p role="column_definition">confmatchtype <code>char</code></p>
<p>Foreign key match type: <code>f</code> = full, <code>p</code> = partial, <code>s</code> = simple</p></td>
</tr>
<tr>
<td><p role="column_definition">conislocal <code>bool</code></p>
<p>This constraint is defined locally for the relation. Note that a constraint can be locally defined and inherited simultaneously.</p></td>
</tr>
<tr>
<td><p role="column_definition">coninhcount <code>int2</code></p>
<p>The number of direct inheritance ancestors this constraint has. A constraint with a nonzero number of ancestors cannot be dropped nor renamed.</p></td>
</tr>
<tr>
<td><p role="column_definition">connoinherit <code>bool</code></p>
<p>This constraint is defined locally for the relation. It is a non-inheritable constraint.</p></td>
</tr>
<tr>
<td><p role="column_definition">conkey <code>int2[]</code> (references <a href="#catalog-pg-attribute">pg_attribute</a>.attnum)</p>
<p>If a table constraint (including foreign keys, but not constraint triggers), list of the constrained columns</p></td>
</tr>
<tr>
<td><p role="column_definition">confkey <code>int2[]</code> (references <a href="#catalog-pg-attribute">pg_attribute</a>.attnum)</p>
<p>If a foreign key, list of the referenced columns</p></td>
</tr>
<tr>
<td><p role="column_definition">conpfeqop <code>oid[]</code> (references <a href="#catalog-pg-operator">pg_operator</a>.oid)</p>
<p>If a foreign key, list of the equality operators for PK = FK comparisons</p></td>
</tr>
<tr>
<td><p role="column_definition">conppeqop <code>oid[]</code> (references <a href="#catalog-pg-operator">pg_operator</a>.oid)</p>
<p>If a foreign key, list of the equality operators for PK = PK comparisons</p></td>
</tr>
<tr>
<td><p role="column_definition">conffeqop <code>oid[]</code> (references <a href="#catalog-pg-operator">pg_operator</a>.oid)</p>
<p>If a foreign key, list of the equality operators for FK = FK comparisons</p></td>
</tr>
<tr>
<td><p role="column_definition">confdelsetcols <code>int2[]</code> (references <a href="#catalog-pg-attribute">pg_attribute</a>.attnum)</p>
<p>If a foreign key with a <code>SET NULL</code> or <code>SET DEFAULT</code> delete action, the columns that will be updated. If null, all of the referencing columns will be updated.</p></td>
</tr>
<tr>
<td><p role="column_definition">conexclop <code>oid[]</code> (references <a href="#catalog-pg-operator">pg_operator</a>.oid)</p>
<p>If an exclusion constraint, list of the per-column exclusion operators</p></td>
</tr>
<tr>
<td><p role="column_definition">conbin <code>pg_node_tree</code></p>
<p>If a check constraint, an internal representation of the expression. (It's recommended to use <code>pg_get_constraintdef()</code> to extract the definition of a check constraint.)</p></td>
</tr>
</tbody>
</table>

In the case of an exclusion constraint, conkey is only useful for constraint elements that are simple column references. For other cases, a zero appears in conkey and the associated index must be consulted to discover the expression that is constrained. (conkey thus has the same contents as [pg_index](#catalog-pg-index).indkey for the index.)

> [!NOTE]
> `pg_class.relchecks` needs to agree with the number of check-constraint entries found in this table for each relation.

## pg_conversion

pg_conversion

The catalog pg_conversion describes encoding conversion functions. See [???](#sql-createconversion) for more information.

<table>
<caption>pg_conversion Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">conname <code>name</code></p>
<p>Conversion name (unique within a namespace)</p></td>
</tr>
<tr>
<td><p role="column_definition">connamespace <code>oid</code> (references <a href="#catalog-pg-namespace">pg_namespace</a>.oid)</p>
<p>The OID of the namespace that contains this conversion</p></td>
</tr>
<tr>
<td><p role="column_definition">conowner <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>Owner of the conversion</p></td>
</tr>
<tr>
<td><p role="column_definition">conforencoding <code>int4</code></p>
<p>Source encoding ID (<a href="#pg-encoding-to-char"><code>pg_encoding_to_char()</code></a> can translate this number to the encoding name)</p></td>
</tr>
<tr>
<td><p role="column_definition">contoencoding <code>int4</code></p>
<p>Destination encoding ID (<a href="#pg-encoding-to-char"><code>pg_encoding_to_char()</code></a> can translate this number to the encoding name)</p></td>
</tr>
<tr>
<td><p role="column_definition">conproc <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>Conversion function</p></td>
</tr>
<tr>
<td><p role="column_definition">condefault <code>bool</code></p>
<p>True if this is the default conversion</p></td>
</tr>
</tbody>
</table>

## pg_database

pg_database

The catalog pg_database stores information about the available databases. Databases are created with the [`CREATE DATABASE`](#sql-createdatabase) command. Consult [???](#managing-databases) for details about the meaning of some of the parameters.

Unlike most system catalogs, pg_database is shared across all databases of a cluster: there is only one copy of pg_database per cluster, not one per database.

<table>
<caption>pg_database Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">datname <code>name</code></p>
<p>Database name</p></td>
</tr>
<tr>
<td><p role="column_definition">datdba <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>Owner of the database, usually the user who created it</p></td>
</tr>
<tr>
<td><p role="column_definition">encoding <code>int4</code></p>
<p>Character encoding for this database (<a href="#pg-encoding-to-char"><code>pg_encoding_to_char()</code></a> can translate this number to the encoding name)</p></td>
</tr>
<tr>
<td><p role="column_definition">datlocprovider <code>char</code></p>
<p>Locale provider for this database: <code>b</code> = builtin, <code>c</code> = libc, <code>i</code> = icu</p></td>
</tr>
<tr>
<td><p role="column_definition">datistemplate <code>bool</code></p>
<p>If true, then this database can be cloned by any user with <code>CREATEDB</code> privileges; if false, then only superusers or the owner of the database can clone it.</p></td>
</tr>
<tr>
<td><p role="column_definition">datallowconn <code>bool</code></p>
<p>If false then no one can connect to this database. This is used to protect the <code>template0</code> database from being altered.</p></td>
</tr>
<tr>
<td><p role="column_definition">dathasloginevt <code>bool</code></p>
<p>Indicates that there are login event triggers defined for this database. This flag is used to avoid extra lookups on the pg_event_trigger table during each backend startup. This flag is used internally by PostgreSQL and should not be manually altered or read for monitoring purposes.</p></td>
</tr>
<tr>
<td><p role="column_definition">datconnlimit <code>int4</code></p>
<p>Sets maximum number of concurrent connections that can be made to this database. -1 means no limit, -2 indicates the database is invalid.</p></td>
</tr>
<tr>
<td><p role="column_definition">datfrozenxid <code>xid</code></p>
<p>All transaction IDs before this one have been replaced with a permanent (“frozen”) transaction ID in this database. This is used to track whether the database needs to be vacuumed in order to prevent transaction ID wraparound or to allow <code>pg_xact</code> to be shrunk. It is the minimum of the per-table <a href="#catalog-pg-class">pg_class</a>.relfrozenxid values.</p></td>
</tr>
<tr>
<td><p role="column_definition">datminmxid <code>xid</code></p>
<p>All multixact IDs before this one have been replaced with a transaction ID in this database. This is used to track whether the database needs to be vacuumed in order to prevent multixact ID wraparound or to allow <code>pg_multixact</code> to be shrunk. It is the minimum of the per-table <a href="#catalog-pg-class">pg_class</a>.relminmxid values.</p></td>
</tr>
<tr>
<td><p role="column_definition">dattablespace <code>oid</code> (references <a href="#catalog-pg-tablespace">pg_tablespace</a>.oid)</p>
<p>The default tablespace for the database. Within this database, all tables for which <a href="#catalog-pg-class">pg_class</a>.reltablespace is zero will be stored in this tablespace; in particular, all the non-shared system catalogs will be there.</p></td>
</tr>
<tr>
<td><p role="column_definition">datcollate <code>text</code></p>
<p>LC_COLLATE for this database</p></td>
</tr>
<tr>
<td><p role="column_definition">datctype <code>text</code></p>
<p>LC_CTYPE for this database</p></td>
</tr>
<tr>
<td><p role="column_definition">datlocale <code>text</code></p>
<p>Collation provider locale name for this database. If the provider is <code>libc</code>, datlocale is <code>NULL</code>; datcollate and datctype are used instead.</p></td>
</tr>
<tr>
<td><p role="column_definition">daticurules <code>text</code></p>
<p>ICU collation rules for this database</p></td>
</tr>
<tr>
<td><p role="column_definition">datcollversion <code>text</code></p>
<p>Provider-specific version of the collation. This is recorded when the database is created and then checked when it is used, to detect changes in the collation definition that could lead to data corruption.</p></td>
</tr>
<tr>
<td><p role="column_definition">datacl <code>aclitem[]</code></p>
<p>Access privileges; see <a href="#ddl-priv">???</a> for details</p></td>
</tr>
</tbody>
</table>

## pg_db_role_setting

pg_db_role_setting

The catalog pg_db_role_setting records the default values that have been set for run-time configuration variables, for each role and database combination.

Unlike most system catalogs, pg_db_role_setting is shared across all databases of a cluster: there is only one copy of pg_db_role_setting per cluster, not one per database.

<table>
<caption>pg_db_role_setting Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">setdatabase <code>oid</code> (references <a href="#catalog-pg-database">pg_database</a>.oid)</p>
<p>The OID of the database the setting is applicable to, or zero if not database-specific</p></td>
</tr>
<tr>
<td><p role="column_definition">setrole <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>The OID of the role the setting is applicable to, or zero if not role-specific</p></td>
</tr>
<tr>
<td><p role="column_definition">setconfig <code>text[]</code></p>
<p>Defaults for run-time configuration variables</p></td>
</tr>
</tbody>
</table>

## pg_default_acl

pg_default_acl

The catalog pg_default_acl stores initial privileges to be assigned to newly created objects.

<table>
<caption>pg_default_acl Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">defaclrole <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>The OID of the role associated with this entry</p></td>
</tr>
<tr>
<td><p role="column_definition">defaclnamespace <code>oid</code> (references <a href="#catalog-pg-namespace">pg_namespace</a>.oid)</p>
<p>The OID of the namespace associated with this entry, or zero if none</p></td>
</tr>
<tr>
<td><p role="column_definition">defaclobjtype <code>char</code></p>
<p>Type of object this entry is for: <code>r</code> = relation (table, view), <code>S</code> = sequence, <code>f</code> = function, <code>T</code> = type, <code>n</code> = schema</p></td>
</tr>
<tr>
<td><p role="column_definition">defaclacl <code>aclitem[]</code></p>
<p>Access privileges that this type of object should have on creation</p></td>
</tr>
</tbody>
</table>

A pg_default_acl entry shows the initial privileges to be assigned to an object belonging to the indicated user. There are currently two types of entry: “global” entries with defaclnamespace = zero, and “per-schema” entries that reference a particular schema. If a global entry is present then it *overrides* the normal hard-wired default privileges for the object type. A per-schema entry, if present, represents privileges to be *added to* the global or hard-wired default privileges.

Note that when an ACL entry in another catalog is null, it is taken to represent the hard-wired default privileges for its object, *not* whatever might be in pg_default_acl at the moment. pg_default_acl is only consulted during object creation.

## pg_depend

pg_depend

The catalog pg_depend records the dependency relationships between database objects. This information allows `DROP` commands to find which other objects must be dropped by `DROP CASCADE` or prevent dropping in the `DROP RESTRICT` case.

See also [pg_shdepend](#catalog-pg-shdepend), which performs a similar function for dependencies involving objects that are shared across a database cluster.

<table>
<caption>pg_depend Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">classid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The OID of the system catalog the dependent object is in</p></td>
</tr>
<tr>
<td><p role="column_definition">objid <code>oid</code> (references any OID column)</p>
<p>The OID of the specific dependent object</p></td>
</tr>
<tr>
<td><p role="column_definition">objsubid <code>int4</code></p>
<p>For a table column, this is the column number (the objid and classid refer to the table itself). For all other object types, this column is zero.</p></td>
</tr>
<tr>
<td><p role="column_definition">refclassid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The OID of the system catalog the referenced object is in</p></td>
</tr>
<tr>
<td><p role="column_definition">refobjid <code>oid</code> (references any OID column)</p>
<p>The OID of the specific referenced object</p></td>
</tr>
<tr>
<td><p role="column_definition">refobjsubid <code>int4</code></p>
<p>For a table column, this is the column number (the refobjid and refclassid refer to the table itself). For all other object types, this column is zero.</p></td>
</tr>
<tr>
<td><p role="column_definition">deptype <code>char</code></p>
<p>A code defining the specific semantics of this dependency relationship; see text</p></td>
</tr>
</tbody>
</table>

In all cases, a pg_depend entry indicates that the referenced object cannot be dropped without also dropping the dependent object. However, there are several subflavors identified by deptype:

`DEPENDENCY_NORMAL` (`n`)  
A normal relationship between separately-created objects. The dependent object can be dropped without affecting the referenced object. The referenced object can only be dropped by specifying `CASCADE`, in which case the dependent object is dropped, too. Example: a table column has a normal dependency on its data type.

`DEPENDENCY_AUTO` (`a`)  
The dependent object can be dropped separately from the referenced object, and should be automatically dropped (regardless of `RESTRICT` or `CASCADE` mode) if the referenced object is dropped. Example: a named constraint on a table is made auto-dependent on the table, so that it will go away if the table is dropped.

`DEPENDENCY_INTERNAL` (`i`)  
The dependent object was created as part of creation of the referenced object, and is really just a part of its internal implementation. A direct `DROP` of the dependent object will be disallowed outright (we'll tell the user to issue a `DROP` against the referenced object, instead). A `DROP` of the referenced object will result in automatically dropping the dependent object whether `CASCADE` is specified or not. If the dependent object has to be dropped due to a dependency on some other object being removed, its drop is converted to a drop of the referenced object, so that `NORMAL` and `AUTO` dependencies of the dependent object behave much like they were dependencies of the referenced object. Example: a view's `ON SELECT` rule is made internally dependent on the view, preventing it from being dropped while the view remains. Dependencies of the rule (such as tables it refers to) act as if they were dependencies of the view.

`DEPENDENCY_PARTITION_PRI` (`P`); `DEPENDENCY_PARTITION_SEC` (`S`)  
The dependent object was created as part of creation of the referenced object, and is really just a part of its internal implementation; however, unlike `INTERNAL`, there is more than one such referenced object. The dependent object must not be dropped unless at least one of these referenced objects is dropped; if any one is, the dependent object should be dropped whether or not `CASCADE` is specified. Also unlike `INTERNAL`, a drop of some other object that the dependent object depends on does not result in automatic deletion of any partition-referenced object. Hence, if the drop does not cascade to at least one of these objects via some other path, it will be refused. (In most cases, the dependent object shares all its non-partition dependencies with at least one partition-referenced object, so that this restriction does not result in blocking any cascaded delete.) Primary and secondary partition dependencies behave identically except that the primary dependency is preferred for use in error messages; hence, a partition-dependent object should have one primary partition dependency and one or more secondary partition dependencies. Note that partition dependencies are made in addition to, not instead of, any dependencies the object would normally have. This simplifies `ATTACH/DETACH PARTITION` operations: the partition dependencies need only be added or removed. Example: a child partitioned index is made partition-dependent on both the partition table it is on and the parent partitioned index, so that it goes away if either of those is dropped, but not otherwise. The dependency on the parent index is primary, so that if the user tries to drop the child partitioned index, the error message will suggest dropping the parent index instead (not the table).

`DEPENDENCY_EXTENSION` (`e`)  
The dependent object is a member of the extension that is the referenced object (see [pg_extension](#catalog-pg-extension)). The dependent object can be dropped only via [`DROP EXTENSION`](#sql-dropextension) on the referenced object. Functionally this dependency type acts the same as an `INTERNAL` dependency, but it's kept separate for clarity and to simplify pg_dump.

`DEPENDENCY_AUTO_EXTENSION` (`x`)  
The dependent object is not a member of the extension that is the referenced object (and so it should not be ignored by pg_dump), but it cannot function without the extension and should be auto-dropped if the extension is. The dependent object may be dropped on its own as well. Functionally this dependency type acts the same as an `AUTO` dependency, but it's kept separate for clarity and to simplify pg_dump.

Other dependency flavors might be needed in future.

Note that it's quite possible for two objects to be linked by more than one pg_depend entry. For example, a child partitioned index would have both a partition-type dependency on its associated partition table, and an auto dependency on each column of that table that it indexes. This sort of situation expresses the union of multiple dependency semantics. A dependent object can be dropped without `CASCADE` if any of its dependencies satisfies its condition for automatic dropping. Conversely, all the dependencies' restrictions about which objects must be dropped together must be satisfied.

Most objects created during initdb are considered “pinned”, which means that the system itself depends on them. Therefore, they are never allowed to be dropped. Also, knowing that pinned objects will not be dropped, the dependency mechanism doesn't bother to make pg_depend entries showing dependencies on them. Thus, for example, a table column of type `numeric` notionally has a `NORMAL` dependency on the `numeric` data type, but no such entry actually appears in pg_depend.

## pg_description

pg_description

The catalog pg_description stores optional descriptions (comments) for each database object. Descriptions can be manipulated with the [`COMMENT`](#sql-comment) command and viewed with psql's `\d` commands. Descriptions of many built-in system objects are provided in the initial contents of pg_description.

See also [pg_shdescription](#catalog-pg-shdescription), which performs a similar function for descriptions involving objects that are shared across a database cluster.

<table>
<caption>pg_description Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">objoid <code>oid</code> (references any OID column)</p>
<p>The OID of the object this description pertains to</p></td>
</tr>
<tr>
<td><p role="column_definition">classoid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The OID of the system catalog this object appears in</p></td>
</tr>
<tr>
<td><p role="column_definition">objsubid <code>int4</code></p>
<p>For a comment on a table column, this is the column number (the objoid and classoid refer to the table itself). For all other object types, this column is zero.</p></td>
</tr>
<tr>
<td><p role="column_definition">description <code>text</code></p>
<p>Arbitrary text that serves as the description of this object</p></td>
</tr>
</tbody>
</table>

## pg_enum

pg_enum

The pg_enum catalog contains entries showing the values and labels for each enum type. The internal representation of a given enum value is actually the OID of its associated row in pg_enum.

<table>
<caption>pg_enum Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">enumtypid <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>The OID of the <a href="#catalog-pg-type">pg_type</a> entry owning this enum value</p></td>
</tr>
<tr>
<td><p role="column_definition">enumsortorder <code>float4</code></p>
<p>The sort position of this enum value within its enum type</p></td>
</tr>
<tr>
<td><p role="column_definition">enumlabel <code>name</code></p>
<p>The textual label for this enum value</p></td>
</tr>
</tbody>
</table>

The OIDs for pg_enum rows follow a special rule: even-numbered OIDs are guaranteed to be ordered in the same way as the sort ordering of their enum type. That is, if two even OIDs belong to the same enum type, the smaller OID must have the smaller enumsortorder value. Odd-numbered OID values need bear no relationship to the sort order. This rule allows the enum comparison routines to avoid catalog lookups in many common cases. The routines that create and alter enum types attempt to assign even OIDs to enum values whenever possible.

When an enum type is created, its members are assigned sort-order positions 1..\<n\>. But members added later might be given negative or fractional values of enumsortorder. The only requirement on these values is that they be correctly ordered and unique within each enum type.

## pg_event_trigger

pg_event_trigger

The catalog pg_event_trigger stores event triggers. See [???](#event-triggers) for more information.

<table>
<caption>pg_event_trigger Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">evtname <code>name</code></p>
<p>Trigger name (must be unique)</p></td>
</tr>
<tr>
<td><p role="column_definition">evtevent <code>name</code></p>
<p>Identifies the event for which this trigger fires</p></td>
</tr>
<tr>
<td><p role="column_definition">evtowner <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>Owner of the event trigger</p></td>
</tr>
<tr>
<td><p role="column_definition">evtfoid <code>oid</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>The function to be called</p></td>
</tr>
<tr>
<td><p role="column_definition">evtenabled <code>char</code></p>
<p>Controls in which <a href="#guc-session-replication-role">???</a> modes the event trigger fires. <code>O</code> = trigger fires in “origin” and “local” modes, <code>D</code> = trigger is disabled, <code>R</code> = trigger fires in “replica” mode, <code>A</code> = trigger fires always.</p></td>
</tr>
<tr>
<td><p role="column_definition">evttags <code>text[]</code></p>
<p>Command tags for which this trigger will fire. If NULL, the firing of this trigger is not restricted on the basis of the command tag.</p></td>
</tr>
</tbody>
</table>

## pg_extension

pg_extension

The catalog pg_extension stores information about the installed extensions. See [???](#extend-extensions) for details about extensions.

<table>
<caption>pg_extension Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">extname <code>name</code></p>
<p>Name of the extension</p></td>
</tr>
<tr>
<td><p role="column_definition">extowner <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>Owner of the extension</p></td>
</tr>
<tr>
<td><p role="column_definition">extnamespace <code>oid</code> (references <a href="#catalog-pg-namespace">pg_namespace</a>.oid)</p>
<p>Schema containing the extension's exported objects</p></td>
</tr>
<tr>
<td><p role="column_definition">extrelocatable <code>bool</code></p>
<p>True if extension can be relocated to another schema</p></td>
</tr>
<tr>
<td><p role="column_definition">extversion <code>text</code></p>
<p>Version name for the extension</p></td>
</tr>
<tr>
<td><p role="column_definition">extconfig <code>oid[]</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>Array of <code>regclass</code> OIDs for the extension's configuration table(s), or <code>NULL</code> if none</p></td>
</tr>
<tr>
<td><p role="column_definition">extcondition <code>text[]</code></p>
<p>Array of <code>WHERE</code>-clause filter conditions for the extension's configuration table(s), or <code>NULL</code> if none</p></td>
</tr>
</tbody>
</table>

Note that unlike most catalogs with a “namespace” column, extnamespace is not meant to imply that the extension belongs to that schema. Extension names are never schema-qualified. Rather, extnamespace indicates the schema that contains most or all of the extension's objects. If extrelocatable is true, then this schema must in fact contain all schema-qualifiable objects belonging to the extension.

## pg_foreign_data_wrapper

pg_foreign_data_wrapper

The catalog pg_foreign_data_wrapper stores foreign-data wrapper definitions. A foreign-data wrapper is the mechanism by which external data, residing on foreign servers, is accessed.

<table>
<caption>pg_foreign_data_wrapper Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">fdwname <code>name</code></p>
<p>Name of the foreign-data wrapper</p></td>
</tr>
<tr>
<td><p role="column_definition">fdwowner <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>Owner of the foreign-data wrapper</p></td>
</tr>
<tr>
<td><p role="column_definition">fdwhandler <code>oid</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>References a handler function that is responsible for supplying execution routines for the foreign-data wrapper. Zero if no handler is provided</p></td>
</tr>
<tr>
<td><p role="column_definition">fdwvalidator <code>oid</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>References a validator function that is responsible for checking the validity of the options given to the foreign-data wrapper, as well as options for foreign servers and user mappings using the foreign-data wrapper. Zero if no validator is provided</p></td>
</tr>
<tr>
<td><p role="column_definition">fdwacl <code>aclitem[]</code></p>
<p>Access privileges; see <a href="#ddl-priv">???</a> for details</p></td>
</tr>
<tr>
<td><p role="column_definition">fdwoptions <code>text[]</code></p>
<p>Foreign-data wrapper specific options, as “keyword=value” strings</p></td>
</tr>
</tbody>
</table>

## pg_foreign_server

pg_foreign_server

The catalog pg_foreign_server stores foreign server definitions. A foreign server describes a source of external data, such as a remote server. Foreign servers are accessed via foreign-data wrappers.

<table>
<caption>pg_foreign_server Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">srvname <code>name</code></p>
<p>Name of the foreign server</p></td>
</tr>
<tr>
<td><p role="column_definition">srvowner <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>Owner of the foreign server</p></td>
</tr>
<tr>
<td><p role="column_definition">srvfdw <code>oid</code> (references <a href="#catalog-pg-foreign-data-wrapper">pg_foreign_data_wrapper</a>.oid)</p>
<p>OID of the foreign-data wrapper of this foreign server</p></td>
</tr>
<tr>
<td><p role="column_definition">srvtype <code>text</code></p>
<p>Type of the server (optional)</p></td>
</tr>
<tr>
<td><p role="column_definition">srvversion <code>text</code></p>
<p>Version of the server (optional)</p></td>
</tr>
<tr>
<td><p role="column_definition">srvacl <code>aclitem[]</code></p>
<p>Access privileges; see <a href="#ddl-priv">???</a> for details</p></td>
</tr>
<tr>
<td><p role="column_definition">srvoptions <code>text[]</code></p>
<p>Foreign server specific options, as “keyword=value” strings</p></td>
</tr>
</tbody>
</table>

## pg_foreign_table

pg_foreign_table

The catalog pg_foreign_table contains auxiliary information about foreign tables. A foreign table is primarily represented by a [pg_class](#catalog-pg-class) entry, just like a regular table. Its pg_foreign_table entry contains the information that is pertinent only to foreign tables and not any other kind of relation.

<table>
<caption>pg_foreign_table Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">ftrelid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The OID of the <a href="#catalog-pg-class">pg_class</a> entry for this foreign table</p></td>
</tr>
<tr>
<td><p role="column_definition">ftserver <code>oid</code> (references <a href="#catalog-pg-foreign-server">pg_foreign_server</a>.oid)</p>
<p>OID of the foreign server for this foreign table</p></td>
</tr>
<tr>
<td><p role="column_definition">ftoptions <code>text[]</code></p>
<p>Foreign table options, as “keyword=value” strings</p></td>
</tr>
</tbody>
</table>

## pg_index

pg_index

The catalog pg_index contains part of the information about indexes. The rest is mostly in [pg_class](#catalog-pg-class).

<table>
<caption>pg_index Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">indexrelid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The OID of the <a href="#catalog-pg-class">pg_class</a> entry for this index</p></td>
</tr>
<tr>
<td><p role="column_definition">indrelid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The OID of the <a href="#catalog-pg-class">pg_class</a> entry for the table this index is for</p></td>
</tr>
<tr>
<td><p role="column_definition">indnatts <code>int2</code></p>
<p>The total number of columns in the index (duplicates <code>pg_class.relnatts</code>); this number includes both key and included attributes</p></td>
</tr>
<tr>
<td><p role="column_definition">indnkeyatts <code>int2</code></p>
<p>The number of key columns in the index, not counting any included columns, which are merely stored and do not participate in the index semantics</p></td>
</tr>
<tr>
<td><p role="column_definition">indisunique <code>bool</code></p>
<p>If true, this is a unique index</p></td>
</tr>
<tr>
<td><p role="column_definition">indnullsnotdistinct <code>bool</code></p>
<p>This value is only used for unique indexes. If false, this unique index will consider null values distinct (so the index can contain multiple null values in a column, the default PostgreSQL behavior). If it is true, it will consider null values to be equal (so the index can only contain one null value in a column).</p></td>
</tr>
<tr>
<td><p role="column_definition">indisprimary <code>bool</code></p>
<p>If true, this index represents the primary key of the table (indisunique should always be true when this is true)</p></td>
</tr>
<tr>
<td><p role="column_definition">indisexclusion <code>bool</code></p>
<p>If true, this index supports an exclusion constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">indimmediate <code>bool</code></p>
<p>If true, the uniqueness check is enforced immediately on insertion (irrelevant if indisunique is not true)</p></td>
</tr>
<tr>
<td><p role="column_definition">indisclustered <code>bool</code></p>
<p>If true, the table was last clustered on this index</p></td>
</tr>
<tr>
<td><p role="column_definition">indisvalid <code>bool</code></p>
<p>If true, the index is currently valid for queries. False means the index is possibly incomplete: it must still be modified by <a href="#sql-insert"><code>INSERT</code></a>/<a href="#sql-update"><code>UPDATE</code></a> operations, but it cannot safely be used for queries. If it is unique, the uniqueness property is not guaranteed true either.</p></td>
</tr>
<tr>
<td><p role="column_definition">indcheckxmin <code>bool</code></p>
<p>If true, queries must not use the index until the xmin of this pg_index row is below their <code>TransactionXmin</code> event horizon, because the table may contain broken <a href="#storage-hot">HOT chains</a> with incompatible rows that they can see</p></td>
</tr>
<tr>
<td><p role="column_definition">indisready <code>bool</code></p>
<p>If true, the index is currently ready for inserts. False means the index must be ignored by <a href="#sql-insert"><code>INSERT</code></a>/<a href="#sql-update"><code>UPDATE</code></a> operations.</p></td>
</tr>
<tr>
<td><p role="column_definition">indislive <code>bool</code></p>
<p>If false, the index is in process of being dropped, and should be ignored for all purposes (including HOT-safety decisions)</p></td>
</tr>
<tr>
<td><p role="column_definition">indisreplident <code>bool</code></p>
<p>If true this index has been chosen as “replica identity” using <a href="#sql-altertable-replica-identity"><code>ALTER TABLE ... REPLICA IDENTITY USING INDEX ...</code></a></p></td>
</tr>
<tr>
<td><p role="column_definition">indkey <code>int2vector</code> (references <a href="#catalog-pg-attribute">pg_attribute</a>.attnum)</p>
<p>This is an array of indnatts values that indicate which table columns this index indexes. For example, a value of <code>1 3</code> would mean that the first and the third table columns make up the index entries. Key columns come before non-key (included) columns. A zero in this array indicates that the corresponding index attribute is an expression over the table columns, rather than a simple column reference.</p></td>
</tr>
<tr>
<td><p role="column_definition">indcollation <code>oidvector</code> (references <a href="#catalog-pg-collation">pg_collation</a>.oid)</p>
<p>For each column in the index key (indnkeyatts values), this contains the OID of the collation to use for the index, or zero if the column is not of a collatable data type.</p></td>
</tr>
<tr>
<td><p role="column_definition">indclass <code>oidvector</code> (references <a href="#catalog-pg-opclass">pg_opclass</a>.oid)</p>
<p>For each column in the index key (indnkeyatts values), this contains the OID of the operator class to use. See <a href="#catalog-pg-opclass">pg_opclass</a> for details.</p></td>
</tr>
<tr>
<td><p role="column_definition">indoption <code>int2vector</code></p>
<p>This is an array of indnkeyatts values that store per-column flag bits. The meaning of the bits is defined by the index's access method.</p></td>
</tr>
<tr>
<td><p role="column_definition">indexprs <code>pg_node_tree</code></p>
<p>Expression trees (in <code>nodeToString()</code> representation) for index attributes that are not simple column references. This is a list with one element for each zero entry in indkey. Null if all index attributes are simple references.</p></td>
</tr>
<tr>
<td><p role="column_definition">indpred <code>pg_node_tree</code></p>
<p>Expression tree (in <code>nodeToString()</code> representation) for partial index predicate. Null if not a partial index.</p></td>
</tr>
</tbody>
</table>

## pg_inherits

pg_inherits

The catalog pg_inherits records information about table and index inheritance hierarchies. There is one entry for each direct parent-child table or index relationship in the database. (Indirect inheritance can be determined by following chains of entries.)

<table>
<caption>pg_inherits Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">inhrelid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The OID of the child table or index</p></td>
</tr>
<tr>
<td><p role="column_definition">inhparent <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The OID of the parent table or index</p></td>
</tr>
<tr>
<td><p role="column_definition">inhseqno <code>int4</code></p>
<p>If there is more than one direct parent for a child table (multiple inheritance), this number tells the order in which the inherited columns are to be arranged. The count starts at 1.</p>
<p>Indexes cannot have multiple inheritance, since they can only inherit when using declarative partitioning.</p></td>
</tr>
<tr>
<td><p role="column_definition">inhdetachpending <code>bool</code></p>
<p><code>true</code> for a partition that is in the process of being detached; <code>false</code> otherwise.</p></td>
</tr>
</tbody>
</table>

## pg_init_privs

pg_init_privs

The catalog pg_init_privs records information about the initial privileges of objects in the system. There is one entry for each object in the database which has a non-default (non-NULL) initial set of privileges.

Objects can have initial privileges either by having those privileges set when the system is initialized (by initdb) or when the object is created during a [`CREATE EXTENSION`](#sql-createextension) and the extension script sets initial privileges using the [`GRANT`](#sql-grant) system. Note that the system will automatically handle recording of the privileges during the extension script and that extension authors need only use the `GRANT` and `REVOKE` statements in their script to have the privileges recorded. The `privtype` column indicates if the initial privilege was set by initdb or during a `CREATE EXTENSION` command.

Objects which have initial privileges set by initdb will have entries where `privtype` is `'i'`, while objects which have initial privileges set by `CREATE EXTENSION` will have entries where `privtype` is `'e'`.

<table>
<caption>pg_init_privs Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">objoid <code>oid</code> (references any OID column)</p>
<p>The OID of the specific object</p></td>
</tr>
<tr>
<td><p role="column_definition">classoid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The OID of the system catalog the object is in</p></td>
</tr>
<tr>
<td><p role="column_definition">objsubid <code>int4</code></p>
<p>For a table column, this is the column number (the objoid and classoid refer to the table itself). For all other object types, this column is zero.</p></td>
</tr>
<tr>
<td><p role="column_definition">privtype <code>char</code></p>
<p>A code defining the type of initial privilege of this object; see text</p></td>
</tr>
<tr>
<td><p role="column_definition">initprivs <code>aclitem[]</code></p>
<p>The initial access privileges; see <a href="#ddl-priv">???</a> for details</p></td>
</tr>
</tbody>
</table>

## pg_language

pg_language

The catalog pg_language registers languages in which you can write functions or stored procedures. See [???](#sql-createlanguage) and [???](#xplang) for more information about language handlers.

<table>
<caption>pg_language Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">lanname <code>name</code></p>
<p>Name of the language</p></td>
</tr>
<tr>
<td><p role="column_definition">lanowner <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>Owner of the language</p></td>
</tr>
<tr>
<td><p role="column_definition">lanispl <code>bool</code></p>
<p>This is false for internal languages (such as SQL) and true for user-defined languages. Currently, pg_dump still uses this to determine which languages need to be dumped, but this might be replaced by a different mechanism in the future.</p></td>
</tr>
<tr>
<td><p role="column_definition">lanpltrusted <code>bool</code></p>
<p>True if this is a trusted language, which means that it is believed not to grant access to anything outside the normal SQL execution environment. Only superusers can create functions in untrusted languages.</p></td>
</tr>
<tr>
<td><p role="column_definition">lanplcallfoid <code>oid</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>For noninternal languages this references the language handler, which is a special function that is responsible for executing all functions that are written in the particular language. Zero for internal languages.</p></td>
</tr>
<tr>
<td><p role="column_definition">laninline <code>oid</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>This references a function that is responsible for executing “inline” anonymous code blocks (<a href="#sql-do">???</a> blocks). Zero if inline blocks are not supported.</p></td>
</tr>
<tr>
<td><p role="column_definition">lanvalidator <code>oid</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>This references a language validator function that is responsible for checking the syntax and validity of new functions when they are created. Zero if no validator is provided.</p></td>
</tr>
<tr>
<td><p role="column_definition">lanacl <code>aclitem[]</code></p>
<p>Access privileges; see <a href="#ddl-priv">???</a> for details</p></td>
</tr>
</tbody>
</table>

## pg_largeobject

pg_largeobject

The catalog pg_largeobject holds the data making up “large objects”. A large object is identified by an OID assigned when it is created. Each large object is broken into segments or “pages” small enough to be conveniently stored as rows in pg_largeobject. The amount of data per page is defined to be `LOBLKSIZE` (which is currently `BLCKSZ/4`, or typically 2 kB).

Prior to PostgreSQL 9.0, there was no permission structure associated with large objects. As a result, pg_largeobject was publicly readable and could be used to obtain the OIDs (and contents) of all large objects in the system. This is no longer the case; use [pg_largeobject_metadata](#catalog-pg-largeobject-metadata) to obtain a list of large object OIDs.

<table>
<caption>pg_largeobject Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">loid <code>oid</code> (references <a href="#catalog-pg-largeobject-metadata">pg_largeobject_metadata</a>.oid)</p>
<p>Identifier of the large object that includes this page</p></td>
</tr>
<tr>
<td><p role="column_definition">pageno <code>int4</code></p>
<p>Page number of this page within its large object (counting from zero)</p></td>
</tr>
<tr>
<td><p role="column_definition">data <code>bytea</code></p>
<p>Actual data stored in the large object. This will never be more than <code>LOBLKSIZE</code> bytes and might be less.</p></td>
</tr>
</tbody>
</table>

Each row of pg_largeobject holds data for one page of a large object, beginning at byte offset (`pageno * LOBLKSIZE`) within the object. The implementation allows sparse storage: pages might be missing, and might be shorter than `LOBLKSIZE` bytes even if they are not the last page of the object. Missing regions within a large object read as zeroes.

## pg_largeobject_metadata

pg_largeobject_metadata

The catalog pg_largeobject_metadata holds metadata associated with large objects. The actual large object data is stored in [pg_largeobject](#catalog-pg-largeobject).

<table>
<caption>pg_largeobject_metadata Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">lomowner <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>Owner of the large object</p></td>
</tr>
<tr>
<td><p role="column_definition">lomacl <code>aclitem[]</code></p>
<p>Access privileges; see <a href="#ddl-priv">???</a> for details</p></td>
</tr>
</tbody>
</table>

## pg_namespace

pg_namespace

The catalog pg_namespace stores namespaces. A namespace is the structure underlying SQL schemas: each namespace can have a separate collection of relations, types, etc. without name conflicts.

<table>
<caption>pg_namespace Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">nspname <code>name</code></p>
<p>Name of the namespace</p></td>
</tr>
<tr>
<td><p role="column_definition">nspowner <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>Owner of the namespace</p></td>
</tr>
<tr>
<td><p role="column_definition">nspacl <code>aclitem[]</code></p>
<p>Access privileges; see <a href="#ddl-priv">???</a> for details</p></td>
</tr>
</tbody>
</table>

## pg_opclass

pg_opclass

The catalog pg_opclass defines index access method operator classes. Each operator class defines semantics for index columns of a particular data type and a particular index access method. An operator class essentially specifies that a particular operator family is applicable to a particular indexable column data type. The set of operators from the family that are actually usable with the indexed column are whichever ones accept the column's data type as their left-hand input.

Operator classes are described at length in [???](#xindex).

<table>
<caption>pg_opclass Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">opcmethod <code>oid</code> (references <a href="#catalog-pg-am">pg_am</a>.oid)</p>
<p>Index access method operator class is for</p></td>
</tr>
<tr>
<td><p role="column_definition">opcname <code>name</code></p>
<p>Name of this operator class</p></td>
</tr>
<tr>
<td><p role="column_definition">opcnamespace <code>oid</code> (references <a href="#catalog-pg-namespace">pg_namespace</a>.oid)</p>
<p>Namespace of this operator class</p></td>
</tr>
<tr>
<td><p role="column_definition">opcowner <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>Owner of the operator class</p></td>
</tr>
<tr>
<td><p role="column_definition">opcfamily <code>oid</code> (references <a href="#catalog-pg-opfamily">pg_opfamily</a>.oid)</p>
<p>Operator family containing the operator class</p></td>
</tr>
<tr>
<td><p role="column_definition">opcintype <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>Data type that the operator class indexes</p></td>
</tr>
<tr>
<td><p role="column_definition">opcdefault <code>bool</code></p>
<p>True if this operator class is the default for opcintype</p></td>
</tr>
<tr>
<td><p role="column_definition">opckeytype <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>Type of data stored in index, or zero if same as opcintype</p></td>
</tr>
</tbody>
</table>

An operator class's opcmethod must match the opfmethod of its containing operator family. Also, there must be no more than one pg_opclass row having opcdefault true for any given combination of opcmethod and opcintype.

## pg_operator

pg_operator

The catalog pg_operator stores information about operators. See [???](#sql-createoperator) and [???](#xoper) for more information.

<table>
<caption>pg_operator Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">oprname <code>name</code></p>
<p>Name of the operator</p></td>
</tr>
<tr>
<td><p role="column_definition">oprnamespace <code>oid</code> (references <a href="#catalog-pg-namespace">pg_namespace</a>.oid)</p>
<p>The OID of the namespace that contains this operator</p></td>
</tr>
<tr>
<td><p role="column_definition">oprowner <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>Owner of the operator</p></td>
</tr>
<tr>
<td><p role="column_definition">oprkind <code>char</code></p>
<p><code>b</code> = infix operator (“both”), or <code>l</code> = prefix operator (“left”)</p></td>
</tr>
<tr>
<td><p role="column_definition">oprcanmerge <code>bool</code></p>
<p>This operator supports merge joins</p></td>
</tr>
<tr>
<td><p role="column_definition">oprcanhash <code>bool</code></p>
<p>This operator supports hash joins</p></td>
</tr>
<tr>
<td><p role="column_definition">oprleft <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>Type of the left operand (zero for a prefix operator)</p></td>
</tr>
<tr>
<td><p role="column_definition">oprright <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>Type of the right operand</p></td>
</tr>
<tr>
<td><p role="column_definition">oprresult <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>Type of the result (zero for a not-yet-defined “shell” operator)</p></td>
</tr>
<tr>
<td><p role="column_definition">oprcom <code>oid</code> (references <a href="#catalog-pg-operator">pg_operator</a>.oid)</p>
<p>Commutator of this operator (zero if none)</p></td>
</tr>
<tr>
<td><p role="column_definition">oprnegate <code>oid</code> (references <a href="#catalog-pg-operator">pg_operator</a>.oid)</p>
<p>Negator of this operator (zero if none)</p></td>
</tr>
<tr>
<td><p role="column_definition">oprcode <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>Function that implements this operator (zero for a not-yet-defined “shell” operator)</p></td>
</tr>
<tr>
<td><p role="column_definition">oprrest <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>Restriction selectivity estimation function for this operator (zero if none)</p></td>
</tr>
<tr>
<td><p role="column_definition">oprjoin <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>Join selectivity estimation function for this operator (zero if none)</p></td>
</tr>
</tbody>
</table>

## pg_opfamily

pg_opfamily

The catalog pg_opfamily defines operator families. Each operator family is a collection of operators and associated support routines that implement the semantics specified for a particular index access method. Furthermore, the operators in a family are all “compatible”, in a way that is specified by the access method. The operator family concept allows cross-data-type operators to be used with indexes and to be reasoned about using knowledge of access method semantics.

Operator families are described at length in [???](#xindex).

<table>
<caption>pg_opfamily Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">opfmethod <code>oid</code> (references <a href="#catalog-pg-am">pg_am</a>.oid)</p>
<p>Index access method operator family is for</p></td>
</tr>
<tr>
<td><p role="column_definition">opfname <code>name</code></p>
<p>Name of this operator family</p></td>
</tr>
<tr>
<td><p role="column_definition">opfnamespace <code>oid</code> (references <a href="#catalog-pg-namespace">pg_namespace</a>.oid)</p>
<p>Namespace of this operator family</p></td>
</tr>
<tr>
<td><p role="column_definition">opfowner <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>Owner of the operator family</p></td>
</tr>
</tbody>
</table>

The majority of the information defining an operator family is not in its pg_opfamily row, but in the associated rows in [pg_amop](#catalog-pg-amop), [pg_amproc](#catalog-pg-amproc), and [pg_opclass](#catalog-pg-opclass).

## pg_parameter_acl

pg_parameter_acl

The catalog pg_parameter_acl records configuration parameters for which privileges have been granted to one or more roles. No entry is made for parameters that have default privileges.

Unlike most system catalogs, pg_parameter_acl is shared across all databases of a cluster: there is only one copy of pg_parameter_acl per cluster, not one per database.

<table>
<caption>pg_parameter_acl Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">parname <code>text</code></p>
<p>The name of a configuration parameter for which privileges are granted</p></td>
</tr>
<tr>
<td><p role="column_definition">paracl <code>aclitem[]</code></p>
<p>Access privileges; see <a href="#ddl-priv">???</a> for details</p></td>
</tr>
</tbody>
</table>

## pg_partitioned_table

pg_partitioned_table

The catalog pg_partitioned_table stores information about how tables are partitioned.

<table>
<caption>pg_partitioned_table Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">partrelid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The OID of the <a href="#catalog-pg-class">pg_class</a> entry for this partitioned table</p></td>
</tr>
<tr>
<td><p role="column_definition">partstrat <code>char</code></p>
<p>Partitioning strategy; <code>h</code> = hash partitioned table, <code>l</code> = list partitioned table, <code>r</code> = range partitioned table</p></td>
</tr>
<tr>
<td><p role="column_definition">partnatts <code>int2</code></p>
<p>The number of columns in the partition key</p></td>
</tr>
<tr>
<td><p role="column_definition">partdefid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The OID of the <a href="#catalog-pg-class">pg_class</a> entry for the default partition of this partitioned table, or zero if this partitioned table does not have a default partition</p></td>
</tr>
<tr>
<td><p role="column_definition">partattrs <code>int2vector</code> (references <a href="#catalog-pg-attribute">pg_attribute</a>.attnum)</p>
<p>This is an array of partnatts values that indicate which table columns are part of the partition key. For example, a value of <code>1 3</code> would mean that the first and the third table columns make up the partition key. A zero in this array indicates that the corresponding partition key column is an expression, rather than a simple column reference.</p></td>
</tr>
<tr>
<td><p role="column_definition">partclass <code>oidvector</code> (references <a href="#catalog-pg-opclass">pg_opclass</a>.oid)</p>
<p>For each column in the partition key, this contains the OID of the operator class to use. See <a href="#catalog-pg-opclass">pg_opclass</a> for details.</p></td>
</tr>
<tr>
<td><p role="column_definition">partcollation <code>oidvector</code> (references <a href="#catalog-pg-collation">pg_collation</a>.oid)</p>
<p>For each column in the partition key, this contains the OID of the collation to use for partitioning, or zero if the column is not of a collatable data type.</p></td>
</tr>
<tr>
<td><p role="column_definition">partexprs <code>pg_node_tree</code></p>
<p>Expression trees (in <code>nodeToString()</code> representation) for partition key columns that are not simple column references. This is a list with one element for each zero entry in partattrs. Null if all partition key columns are simple references.</p></td>
</tr>
</tbody>
</table>

## pg_policy

pg_policy

The catalog pg_policy stores row-level security policies for tables. A policy includes the kind of command that it applies to (possibly all commands), the roles that it applies to, the expression to be added as a security-barrier qualification to queries that include the table, and the expression to be added as a `WITH CHECK` option for queries that attempt to add new records to the table.

<table>
<caption>pg_policy Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">polname <code>name</code></p>
<p>The name of the policy</p></td>
</tr>
<tr>
<td><p role="column_definition">polrelid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The table to which the policy applies</p></td>
</tr>
<tr>
<td><p role="column_definition">polcmd <code>char</code></p>
<p>The command type to which the policy is applied: <code>r</code> for <a href="#sql-select">???</a>, <code>a</code> for <a href="#sql-insert">???</a>, <code>w</code> for <a href="#sql-update">???</a>, <code>d</code> for <a href="#sql-delete">???</a>, or <code>*</code> for all</p></td>
</tr>
<tr>
<td><p role="column_definition">polpermissive <code>bool</code></p>
<p>Is the policy permissive or restrictive?</p></td>
</tr>
<tr>
<td><p role="column_definition">polroles <code>oid[]</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>The roles to which the policy is applied; zero means <code>PUBLIC</code> (and normally appears alone in the array)</p></td>
</tr>
<tr>
<td><p role="column_definition">polqual <code>pg_node_tree</code></p>
<p>The expression tree to be added to the security barrier qualifications for queries that use the table</p></td>
</tr>
<tr>
<td><p role="column_definition">polwithcheck <code>pg_node_tree</code></p>
<p>The expression tree to be added to the WITH CHECK qualifications for queries that attempt to add rows to the table</p></td>
</tr>
</tbody>
</table>

> [!NOTE]
> Policies stored in pg_policy are applied only when [pg_class](#catalog-pg-class).relrowsecurity is set for their table.

## pg_proc

pg_proc

The catalog pg_proc stores information about functions, procedures, aggregate functions, and window functions (collectively also known as routines). See [???](#sql-createfunction), [???](#sql-createprocedure), and [???](#xfunc) for more information.

If prokind indicates that the entry is for an aggregate function, there should be a matching row in [pg_aggregate](#catalog-pg-aggregate).

<table>
<caption>pg_proc Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">proname <code>name</code></p>
<p>Name of the function</p></td>
</tr>
<tr>
<td><p role="column_definition">pronamespace <code>oid</code> (references <a href="#catalog-pg-namespace">pg_namespace</a>.oid)</p>
<p>The OID of the namespace that contains this function</p></td>
</tr>
<tr>
<td><p role="column_definition">proowner <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>Owner of the function</p></td>
</tr>
<tr>
<td><p role="column_definition">prolang <code>oid</code> (references <a href="#catalog-pg-language">pg_language</a>.oid)</p>
<p>Implementation language or call interface of this function</p></td>
</tr>
<tr>
<td><p role="column_definition">procost <code>float4</code></p>
<p>Estimated execution cost (in units of <a href="#guc-cpu-operator-cost">???</a>); if proretset, this is cost per row returned</p></td>
</tr>
<tr>
<td><p role="column_definition">prorows <code>float4</code></p>
<p>Estimated number of result rows (zero if not proretset)</p></td>
</tr>
<tr>
<td><p role="column_definition">provariadic <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>Data type of the variadic array parameter's elements, or zero if the function does not have a variadic parameter</p></td>
</tr>
<tr>
<td><p role="column_definition">prosupport <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>Planner support function for this function (see <a href="#xfunc-optimization">???</a>), or zero if none</p></td>
</tr>
<tr>
<td><p role="column_definition">prokind <code>char</code></p>
<p><code>f</code> for a normal function, <code>p</code> for a procedure, <code>a</code> for an aggregate function, or <code>w</code> for a window function</p></td>
</tr>
<tr>
<td><p role="column_definition">prosecdef <code>bool</code></p>
<p>Function is a security definer (i.e., a “setuid” function)</p></td>
</tr>
<tr>
<td><p role="column_definition">proleakproof <code>bool</code></p>
<p>The function has no side effects. No information about the arguments is conveyed except via the return value. Any function that might throw an error depending on the values of its arguments is not leak-proof.</p></td>
</tr>
<tr>
<td><p role="column_definition">proisstrict <code>bool</code></p>
<p>Function returns null if any call argument is null. In that case the function won't actually be called at all. Functions that are not “strict” must be prepared to handle null inputs.</p></td>
</tr>
<tr>
<td><p role="column_definition">proretset <code>bool</code></p>
<p>Function returns a set (i.e., multiple values of the specified data type)</p></td>
</tr>
<tr>
<td><p role="column_definition">provolatile <code>char</code></p>
<p>provolatile tells whether the function's result depends only on its input arguments, or is affected by outside factors. It is <code>i</code> for “immutable” functions, which always deliver the same result for the same inputs. It is <code>s</code> for “stable” functions, whose results (for fixed inputs) do not change within a scan. It is <code>v</code> for “volatile” functions, whose results might change at any time. (Use <code>v</code> also for functions with side-effects, so that calls to them cannot get optimized away.)</p></td>
</tr>
<tr>
<td><p role="column_definition">proparallel <code>char</code></p>
<p>proparallel tells whether the function can be safely run in parallel mode. It is <code>s</code> for functions which are safe to run in parallel mode without restriction. It is <code>r</code> for functions which can be run in parallel mode, but their execution is restricted to the parallel group leader; parallel worker processes cannot invoke these functions. It is <code>u</code> for functions which are unsafe in parallel mode; the presence of such a function forces a serial execution plan.</p></td>
</tr>
<tr>
<td><p role="column_definition">pronargs <code>int2</code></p>
<p>Number of input arguments</p></td>
</tr>
<tr>
<td><p role="column_definition">pronargdefaults <code>int2</code></p>
<p>Number of arguments that have defaults</p></td>
</tr>
<tr>
<td><p role="column_definition">prorettype <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>Data type of the return value</p></td>
</tr>
<tr>
<td><p role="column_definition">proargtypes <code>oidvector</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>An array of the data types of the function arguments. This includes only input arguments (including <code>INOUT</code> and <code>VARIADIC</code> arguments), and thus represents the call signature of the function.</p></td>
</tr>
<tr>
<td><p role="column_definition">proallargtypes <code>oid[]</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>An array of the data types of the function arguments. This includes all arguments (including <code>OUT</code> and <code>INOUT</code> arguments); however, if all the arguments are <code>IN</code> arguments, this field will be null. Note that subscripting is 1-based, whereas for historical reasons proargtypes is subscripted from 0.</p></td>
</tr>
<tr>
<td><p role="column_definition">proargmodes <code>char[]</code></p>
<p>An array of the modes of the function arguments, encoded as <code>i</code> for <code>IN</code> arguments, <code>o</code> for <code>OUT</code> arguments, <code>b</code> for <code>INOUT</code> arguments, <code>v</code> for <code>VARIADIC</code> arguments, <code>t</code> for <code>TABLE</code> arguments. If all the arguments are <code>IN</code> arguments, this field will be null. Note that subscripts correspond to positions of proallargtypes not proargtypes.</p></td>
</tr>
<tr>
<td><p role="column_definition">proargnames <code>text[]</code></p>
<p>An array of the names of the function arguments. Arguments without a name are set to empty strings in the array. If none of the arguments have a name, this field will be null. Note that subscripts correspond to positions of proallargtypes not proargtypes.</p></td>
</tr>
<tr>
<td><p role="column_definition">proargdefaults <code>pg_node_tree</code></p>
<p>Expression trees (in <code>nodeToString()</code> representation) for default values. This is a list with pronargdefaults elements, corresponding to the last &lt;N&gt; <em>input</em> arguments (i.e., the last &lt;N&gt; proargtypes positions). If none of the arguments have defaults, this field will be null.</p></td>
</tr>
<tr>
<td><p role="column_definition">protrftypes <code>oid[]</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>An array of the argument/result data type(s) for which to apply transforms (from the function's <code>TRANSFORM</code> clause). Null if none.</p></td>
</tr>
<tr>
<td><p role="column_definition">prosrc <code>text</code></p>
<p>This tells the function handler how to invoke the function. It might be the actual source code of the function for interpreted languages, a link symbol, a file name, or just about anything else, depending on the implementation language/call convention.</p></td>
</tr>
<tr>
<td><p role="column_definition">probin <code>text</code></p>
<p>Additional information about how to invoke the function. Again, the interpretation is language-specific.</p></td>
</tr>
<tr>
<td><p role="column_definition">prosqlbody <code>pg_node_tree</code></p>
<p>Pre-parsed SQL function body. This is used for SQL-language functions when the body is given in SQL-standard notation rather than as a string literal. It's null in other cases.</p></td>
</tr>
<tr>
<td><p role="column_definition">proconfig <code>text[]</code></p>
<p>Function's local settings for run-time configuration variables</p></td>
</tr>
<tr>
<td><p role="column_definition">proacl <code>aclitem[]</code></p>
<p>Access privileges; see <a href="#ddl-priv">???</a> for details</p></td>
</tr>
</tbody>
</table>

For compiled functions, both built-in and dynamically loaded, prosrc contains the function's C-language name (link symbol). For SQL-language functions, prosrc contains the function's source text if that is specified as a string literal; but if the function body is specified in SQL-standard style, prosrc is unused (typically it's an empty string) and prosqlbody contains the pre-parsed definition. For all other currently-known language types, prosrc contains the function's source text. probin is null except for dynamically-loaded C functions, for which it gives the name of the shared library file containing the function.

## pg_publication

pg_publication

The catalog pg_publication contains all publications created in the database. For more on publications see [???](#logical-replication-publication).

<table>
<caption>pg_publication Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">pubname <code>name</code></p>
<p>Name of the publication</p></td>
</tr>
<tr>
<td><p role="column_definition">pubowner <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>Owner of the publication</p></td>
</tr>
<tr>
<td><p role="column_definition">puballtables <code>bool</code></p>
<p>If true, this publication automatically includes all tables in the database, including any that will be created in the future.</p></td>
</tr>
<tr>
<td><p role="column_definition">pubinsert <code>bool</code></p>
<p>If true, <a href="#sql-insert">???</a> operations are replicated for tables in the publication.</p></td>
</tr>
<tr>
<td><p role="column_definition">pubupdate <code>bool</code></p>
<p>If true, <a href="#sql-update">???</a> operations are replicated for tables in the publication.</p></td>
</tr>
<tr>
<td><p role="column_definition">pubdelete <code>bool</code></p>
<p>If true, <a href="#sql-delete">???</a> operations are replicated for tables in the publication.</p></td>
</tr>
<tr>
<td><p role="column_definition">pubtruncate <code>bool</code></p>
<p>If true, <a href="#sql-truncate">???</a> operations are replicated for tables in the publication.</p></td>
</tr>
<tr>
<td><p role="column_definition">pubviaroot <code>bool</code></p>
<p>If true, operations on a leaf partition are replicated using the identity and schema of its topmost partitioned ancestor mentioned in the publication instead of its own.</p></td>
</tr>
</tbody>
</table>

## pg_publication_namespace

pg_publication_namespace

The catalog pg_publication_namespace contains the mapping between schemas and publications in the database. This is a many-to-many mapping.

<table>
<caption>pg_publication_namespace Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">pnpubid <code>oid</code> (references <a href="#catalog-pg-publication">pg_publication</a>.oid)</p>
<p>Reference to publication</p></td>
</tr>
<tr>
<td><p role="column_definition">pnnspid <code>oid</code> (references <a href="#catalog-pg-namespace">pg_namespace</a>.oid)</p>
<p>Reference to schema</p></td>
</tr>
</tbody>
</table>

## pg_publication_rel

pg_publication_rel

The catalog pg_publication_rel contains the mapping between relations and publications in the database. This is a many-to-many mapping. See also [???](#view-pg-publication-tables) for a more user-friendly view of this information.

<table>
<caption>pg_publication_rel Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">prpubid <code>oid</code> (references <a href="#catalog-pg-publication">pg_publication</a>.oid)</p>
<p>Reference to publication</p></td>
</tr>
<tr>
<td><p role="column_definition">prrelid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>Reference to relation</p></td>
</tr>
<tr>
<td><p role="column_definition">prqual <code>pg_node_tree</code></p>
<p>Expression tree (in <code>nodeToString()</code> representation) for the relation's publication qualifying condition. Null if there is no publication qualifying condition.</p></td>
</tr>
<tr>
<td><p role="column_definition">prattrs <code>int2vector</code> (references <a href="#catalog-pg-attribute">pg_attribute</a>.attnum)</p>
<p>This is an array of values that indicates which table columns are part of the publication. For example, a value of <code>1 3</code> would mean that the first and the third table columns are published. A null value indicates that all columns are published.</p></td>
</tr>
</tbody>
</table>

## pg_range

pg_range

The catalog pg_range stores information about range types. This is in addition to the types' entries in [pg_type](#catalog-pg-type).

<table>
<caption>pg_range Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">rngtypid <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>OID of the range type</p></td>
</tr>
<tr>
<td><p role="column_definition">rngsubtype <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>OID of the element type (subtype) of this range type</p></td>
</tr>
<tr>
<td><p role="column_definition">rngmultitypid <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>OID of the multirange type for this range type</p></td>
</tr>
<tr>
<td><p role="column_definition">rngcollation <code>oid</code> (references <a href="#catalog-pg-collation">pg_collation</a>.oid)</p>
<p>OID of the collation used for range comparisons, or zero if none</p></td>
</tr>
<tr>
<td><p role="column_definition">rngsubopc <code>oid</code> (references <a href="#catalog-pg-opclass">pg_opclass</a>.oid)</p>
<p>OID of the subtype's operator class used for range comparisons</p></td>
</tr>
<tr>
<td><p role="column_definition">rngcanonical <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>OID of the function to convert a range value into canonical form, or zero if none</p></td>
</tr>
<tr>
<td><p role="column_definition">rngsubdiff <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>OID of the function to return the difference between two element values as <code>double precision</code>, or zero if none</p></td>
</tr>
</tbody>
</table>

rngsubopc (plus rngcollation, if the element type is collatable) determines the sort ordering used by the range type. rngcanonical is used when the element type is discrete. rngsubdiff is optional but should be supplied to improve performance of GiST indexes on the range type.

## pg_replication_origin

pg_replication_origin

The pg_replication_origin catalog contains all replication origins created. For more on replication origins see [???](#replication-origins).

Unlike most system catalogs, pg_replication_origin is shared across all databases of a cluster: there is only one copy of pg_replication_origin per cluster, not one per database.

<table>
<caption>pg_replication_origin Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">roident <code>oid</code></p>
<p>A unique, cluster-wide identifier for the replication origin. Should never leave the system.</p></td>
</tr>
<tr>
<td><p role="column_definition">roname <code>text</code></p>
<p>The external, user defined, name of a replication origin.</p></td>
</tr>
</tbody>
</table>

## pg_rewrite

pg_rewrite

The catalog pg_rewrite stores rewrite rules for tables and views.

<table>
<caption>pg_rewrite Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">rulename <code>name</code></p>
<p>Rule name</p></td>
</tr>
<tr>
<td><p role="column_definition">ev_class <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The table this rule is for</p></td>
</tr>
<tr>
<td><p role="column_definition">ev_type <code>char</code></p>
<p>Event type that the rule is for: 1 = <a href="#sql-select">???</a>, 2 = <a href="#sql-update">???</a>, 3 = <a href="#sql-insert">???</a>, 4 = <a href="#sql-delete">???</a></p></td>
</tr>
<tr>
<td><p role="column_definition">ev_enabled <code>char</code></p>
<p>Controls in which <a href="#guc-session-replication-role">???</a> modes the rule fires. <code>O</code> = rule fires in “origin” and “local” modes, <code>D</code> = rule is disabled, <code>R</code> = rule fires in “replica” mode, <code>A</code> = rule fires always.</p></td>
</tr>
<tr>
<td><p role="column_definition">is_instead <code>bool</code></p>
<p>True if the rule is an <code>INSTEAD</code> rule</p></td>
</tr>
<tr>
<td><p role="column_definition">ev_qual <code>pg_node_tree</code></p>
<p>Expression tree (in the form of a <code>nodeToString()</code> representation) for the rule's qualifying condition</p></td>
</tr>
<tr>
<td><p role="column_definition">ev_action <code>pg_node_tree</code></p>
<p>Query tree (in the form of a <code>nodeToString()</code> representation) for the rule's action</p></td>
</tr>
</tbody>
</table>

> [!NOTE]
> `pg_class.relhasrules` must be true if a table has any rules in this catalog.

## pg_seclabel

pg_seclabel

The catalog pg_seclabel stores security labels on database objects. Security labels can be manipulated with the [`SECURITY LABEL`](#sql-security-label) command. For an easier way to view security labels, see [???](#view-pg-seclabels).

See also [pg_shseclabel](#catalog-pg-shseclabel), which performs a similar function for security labels of database objects that are shared across a database cluster.

<table>
<caption>pg_seclabel Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">objoid <code>oid</code> (references any OID column)</p>
<p>The OID of the object this security label pertains to</p></td>
</tr>
<tr>
<td><p role="column_definition">classoid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The OID of the system catalog this object appears in</p></td>
</tr>
<tr>
<td><p role="column_definition">objsubid <code>int4</code></p>
<p>For a security label on a table column, this is the column number (the objoid and classoid refer to the table itself). For all other object types, this column is zero.</p></td>
</tr>
<tr>
<td><p role="column_definition">provider <code>text</code></p>
<p>The label provider associated with this label.</p></td>
</tr>
<tr>
<td><p role="column_definition">label <code>text</code></p>
<p>The security label applied to this object.</p></td>
</tr>
</tbody>
</table>

## pg_sequence

pg_sequence

The catalog pg_sequence contains information about sequences. Some of the information about sequences, such as the name and the schema, is in [pg_class](#catalog-pg-class)

<table>
<caption>pg_sequence Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">seqrelid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The OID of the <a href="#catalog-pg-class">pg_class</a> entry for this sequence</p></td>
</tr>
<tr>
<td><p role="column_definition">seqtypid <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>Data type of the sequence</p></td>
</tr>
<tr>
<td><p role="column_definition">seqstart <code>int8</code></p>
<p>Start value of the sequence</p></td>
</tr>
<tr>
<td><p role="column_definition">seqincrement <code>int8</code></p>
<p>Increment value of the sequence</p></td>
</tr>
<tr>
<td><p role="column_definition">seqmax <code>int8</code></p>
<p>Maximum value of the sequence</p></td>
</tr>
<tr>
<td><p role="column_definition">seqmin <code>int8</code></p>
<p>Minimum value of the sequence</p></td>
</tr>
<tr>
<td><p role="column_definition">seqcache <code>int8</code></p>
<p>Cache size of the sequence</p></td>
</tr>
<tr>
<td><p role="column_definition">seqcycle <code>bool</code></p>
<p>Whether the sequence cycles</p></td>
</tr>
</tbody>
</table>

## pg_shdepend

pg_shdepend

The catalog pg_shdepend records the dependency relationships between database objects and shared objects, such as roles. This information allows PostgreSQL to ensure that those objects are unreferenced before attempting to delete them.

See also [pg_depend](#catalog-pg-depend), which performs a similar function for dependencies involving objects within a single database.

Unlike most system catalogs, pg_shdepend is shared across all databases of a cluster: there is only one copy of pg_shdepend per cluster, not one per database.

<table>
<caption>pg_shdepend Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">dbid <code>oid</code> (references <a href="#catalog-pg-database">pg_database</a>.oid)</p>
<p>The OID of the database the dependent object is in, or zero for a shared object</p></td>
</tr>
<tr>
<td><p role="column_definition">classid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The OID of the system catalog the dependent object is in</p></td>
</tr>
<tr>
<td><p role="column_definition">objid <code>oid</code> (references any OID column)</p>
<p>The OID of the specific dependent object</p></td>
</tr>
<tr>
<td><p role="column_definition">objsubid <code>int4</code></p>
<p>For a table column, this is the column number (the objid and classid refer to the table itself). For all other object types, this column is zero.</p></td>
</tr>
<tr>
<td><p role="column_definition">refclassid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The OID of the system catalog the referenced object is in (must be a shared catalog)</p></td>
</tr>
<tr>
<td><p role="column_definition">refobjid <code>oid</code> (references any OID column)</p>
<p>The OID of the specific referenced object</p></td>
</tr>
<tr>
<td><p role="column_definition">deptype <code>char</code></p>
<p>A code defining the specific semantics of this dependency relationship; see text</p></td>
</tr>
</tbody>
</table>

In all cases, a pg_shdepend entry indicates that the referenced object cannot be dropped without also dropping the dependent object. However, there are several subflavors identified by deptype:

`SHARED_DEPENDENCY_OWNER` (`o`)  
The referenced object (which must be a role) is the owner of the dependent object.

`SHARED_DEPENDENCY_ACL` (`a`)  
The referenced object (which must be a role) is mentioned in the ACL (access control list, i.e., privileges list) of the dependent object. (A `SHARED_DEPENDENCY_ACL` entry is not made for the owner of the object, since the owner will have a `SHARED_DEPENDENCY_OWNER` entry anyway.)

`SHARED_DEPENDENCY_INITACL` (`i`)  
The referenced object (which must be a role) is mentioned in a [pg_init_privs](#catalog-pg-init-privs) entry for the dependent object.

`SHARED_DEPENDENCY_POLICY` (`r`)  
The referenced object (which must be a role) is mentioned as the target of a dependent policy object.

`SHARED_DEPENDENCY_TABLESPACE` (`t`)  
The referenced object (which must be a tablespace) is mentioned as the tablespace for a relation that doesn't have storage.

Other dependency flavors might be needed in future. Note in particular that the current definition only supports roles and tablespaces as referenced objects.

As in the pg_depend catalog, most objects created during initdb are considered “pinned”. No entries are made in pg_shdepend that would have a pinned object as either referenced or dependent object.

## pg_shdescription

pg_shdescription

The catalog pg_shdescription stores optional descriptions (comments) for shared database objects. Descriptions can be manipulated with the [`COMMENT`](#sql-comment) command and viewed with psql's `\d` commands.

See also [pg_description](#catalog-pg-description), which performs a similar function for descriptions involving objects within a single database.

Unlike most system catalogs, pg_shdescription is shared across all databases of a cluster: there is only one copy of pg_shdescription per cluster, not one per database.

<table>
<caption>pg_shdescription Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">objoid <code>oid</code> (references any OID column)</p>
<p>The OID of the object this description pertains to</p></td>
</tr>
<tr>
<td><p role="column_definition">classoid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The OID of the system catalog this object appears in</p></td>
</tr>
<tr>
<td><p role="column_definition">description <code>text</code></p>
<p>Arbitrary text that serves as the description of this object</p></td>
</tr>
</tbody>
</table>

## pg_shseclabel

pg_shseclabel

The catalog pg_shseclabel stores security labels on shared database objects. Security labels can be manipulated with the [`SECURITY LABEL`](#sql-security-label) command. For an easier way to view security labels, see [???](#view-pg-seclabels).

See also [pg_seclabel](#catalog-pg-seclabel), which performs a similar function for security labels involving objects within a single database.

Unlike most system catalogs, pg_shseclabel is shared across all databases of a cluster: there is only one copy of pg_shseclabel per cluster, not one per database.

<table>
<caption>pg_shseclabel Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">objoid <code>oid</code> (references any OID column)</p>
<p>The OID of the object this security label pertains to</p></td>
</tr>
<tr>
<td><p role="column_definition">classoid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The OID of the system catalog this object appears in</p></td>
</tr>
<tr>
<td><p role="column_definition">provider <code>text</code></p>
<p>The label provider associated with this label.</p></td>
</tr>
<tr>
<td><p role="column_definition">label <code>text</code></p>
<p>The security label applied to this object.</p></td>
</tr>
</tbody>
</table>

## pg_statistic

pg_statistic

The catalog pg_statistic stores statistical data about the contents of the database. Entries are created by [`ANALYZE`](#sql-analyze) and subsequently used by the query planner. Note that all the statistical data is inherently approximate, even assuming that it is up-to-date.

Normally there is one entry, with stainherit = `false`, for each table column that has been analyzed. If the table has inheritance children or partitions, a second entry with stainherit = `true` is also created. This row represents the column's statistics over the inheritance tree, i.e., statistics for the data you'd see with `SELECT column FROM table*`, whereas the stainherit = `false` row represents the results of `SELECT column FROM ONLY table`.

pg_statistic also stores statistical data about the values of index expressions. These are described as if they were actual data columns; in particular, starelid references the index. No entry is made for an ordinary non-expression index column, however, since it would be redundant with the entry for the underlying table column. Currently, entries for index expressions always have stainherit = `false`.

Since different kinds of statistics might be appropriate for different kinds of data, pg_statistic is designed not to assume very much about what sort of statistics it stores. Only extremely general statistics (such as nullness) are given dedicated columns in pg_statistic. Everything else is stored in “slots”, which are groups of associated columns whose content is identified by a code number in one of the slot's columns. For more information see `src/include/catalog/pg_statistic.h`.

pg_statistic should not be readable by the public, since even statistical information about a table's contents might be considered sensitive. (Example: minimum and maximum values of a salary column might be quite interesting.) [pg_stats](#view-pg-stats) is a publicly readable view on pg_statistic that only exposes information about those tables that are readable by the current user.

<table>
<caption>pg_statistic Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">starelid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The table or index that the described column belongs to</p></td>
</tr>
<tr>
<td><p role="column_definition">staattnum <code>int2</code> (references <a href="#catalog-pg-attribute">pg_attribute</a>.attnum)</p>
<p>The number of the described column</p></td>
</tr>
<tr>
<td><p role="column_definition">stainherit <code>bool</code></p>
<p>If true, the stats include values from child tables, not just the values in the specified relation</p></td>
</tr>
<tr>
<td><p role="column_definition">stanullfrac <code>float4</code></p>
<p>The fraction of the column's entries that are null</p></td>
</tr>
<tr>
<td><p role="column_definition">stawidth <code>int4</code></p>
<p>The average stored width, in bytes, of nonnull entries</p></td>
</tr>
<tr>
<td><p role="column_definition">stadistinct <code>float4</code></p>
<p>The number of distinct nonnull data values in the column. A value greater than zero is the actual number of distinct values. A value less than zero is the negative of a multiplier for the number of rows in the table; for example, a column in which about 80% of the values are nonnull and each nonnull value appears about twice on average could be represented by stadistinct = -0.4. A zero value means the number of distinct values is unknown.</p></td>
</tr>
<tr>
<td><p role="column_definition">stakind&lt;N&gt; <code>int2</code></p>
<p>A code number indicating the kind of statistics stored in the &lt;N&gt;th “slot” of the pg_statistic row.</p></td>
</tr>
<tr>
<td><p role="column_definition">staop&lt;N&gt; <code>oid</code> (references <a href="#catalog-pg-operator">pg_operator</a>.oid)</p>
<p>An operator used to derive the statistics stored in the &lt;N&gt;th “slot”. For example, a histogram slot would show the <code>&lt;</code> operator that defines the sort order of the data. Zero if the statistics kind does not require an operator.</p></td>
</tr>
<tr>
<td><p role="column_definition">stacoll&lt;N&gt; <code>oid</code> (references <a href="#catalog-pg-collation">pg_collation</a>.oid)</p>
<p>The collation used to derive the statistics stored in the &lt;N&gt;th “slot”. For example, a histogram slot for a collatable column would show the collation that defines the sort order of the data. Zero for noncollatable data.</p></td>
</tr>
<tr>
<td><p role="column_definition">stanumbers&lt;N&gt; <code>float4[]</code></p>
<p>Numerical statistics of the appropriate kind for the &lt;N&gt;th “slot”, or null if the slot kind does not involve numerical values</p></td>
</tr>
<tr>
<td><p role="column_definition">stavalues&lt;N&gt; <code>anyarray</code></p>
<p>Column data values of the appropriate kind for the &lt;N&gt;th “slot”, or null if the slot kind does not store any data values. Each array's element values are actually of the specific column's data type, or a related type such as an array's element type, so there is no way to define these columns' type more specifically than <code>anyarray</code>.</p></td>
</tr>
</tbody>
</table>

## pg_statistic_ext

pg_statistic_ext

The catalog pg_statistic_ext holds definitions of extended planner statistics. Each row in this catalog corresponds to a statistics object created with [`CREATE STATISTICS`](#sql-createstatistics).

<table>
<caption>pg_statistic_ext Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">stxrelid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>Table containing the columns described by this object</p></td>
</tr>
<tr>
<td><p role="column_definition">stxname <code>name</code></p>
<p>Name of the statistics object</p></td>
</tr>
<tr>
<td><p role="column_definition">stxnamespace <code>oid</code> (references <a href="#catalog-pg-namespace">pg_namespace</a>.oid)</p>
<p>The OID of the namespace that contains this statistics object</p></td>
</tr>
<tr>
<td><p role="column_definition">stxowner <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>Owner of the statistics object</p></td>
</tr>
<tr>
<td><p role="column_definition">stxkeys <code>int2vector</code> (references <a href="#catalog-pg-attribute">pg_attribute</a>.attnum)</p>
<p>An array of attribute numbers, indicating which table columns are covered by this statistics object; for example a value of <code>1 3</code> would mean that the first and the third table columns are covered</p></td>
</tr>
<tr>
<td><p role="column_definition">stxstattarget <code>int2</code></p>
<p>stxstattarget controls the level of detail of statistics accumulated for this statistics object by <a href="#sql-analyze"><code>ANALYZE</code></a>. A zero value indicates that no statistics should be collected. A null value says to use the maximum of the statistics targets of the referenced columns, if set, or the system default statistics target. Positive values of stxstattarget determine the target number of “most common values” to collect.</p></td>
</tr>
<tr>
<td><p role="column_definition">stxkind <code>char[]</code></p>
<p>An array containing codes for the enabled statistics kinds; valid values are: <code>d</code> for n-distinct statistics, <code>f</code> for functional dependency statistics, <code>m</code> for most common values (MCV) list statistics, and <code>e</code> for expression statistics</p></td>
</tr>
<tr>
<td><p role="column_definition">stxexprs <code>pg_node_tree</code></p>
<p>Expression trees (in <code>nodeToString()</code> representation) for statistics object attributes that are not simple column references. This is a list with one element per expression. Null if all statistics object attributes are simple references.</p></td>
</tr>
</tbody>
</table>

The pg_statistic_ext entry is filled in completely during [`CREATE STATISTICS`](#sql-createstatistics), but the actual statistical values are not computed then. Subsequent [`ANALYZE`](#sql-analyze) commands compute the desired values and populate an entry in the [pg_statistic_ext_data](#catalog-pg-statistic-ext-data) catalog.

## pg_statistic_ext_data

pg_statistic_ext_data

The catalog pg_statistic_ext_data holds data for extended planner statistics defined in [pg_statistic_ext](#catalog-pg-statistic-ext). Each row in this catalog corresponds to a statistics object created with [`CREATE STATISTICS`](#sql-createstatistics).

Normally there is one entry, with stxdinherit = `false`, for each statistics object that has been analyzed. If the table has inheritance children or partitions, a second entry with stxdinherit = `true` is also created. This row represents the statistics object over the inheritance tree, i.e., statistics for the data you'd see with `SELECT * FROM table*`, whereas the stxdinherit = `false` row represents the results of `SELECT * FROM ONLY table`.

Like [pg_statistic](#catalog-pg-statistic), pg_statistic_ext_data should not be readable by the public, since the contents might be considered sensitive. (Example: most common combinations of values in columns might be quite interesting.) [pg_stats_ext](#view-pg-stats-ext) is a publicly readable view on pg_statistic_ext_data (after joining with [pg_statistic_ext](#catalog-pg-statistic-ext)) that only exposes information about tables the current user owns.

<table>
<caption>pg_statistic_ext_data Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">stxoid <code>oid</code> (references <a href="#catalog-pg-statistic-ext">pg_statistic_ext</a>.oid)</p>
<p>Extended statistics object containing the definition for this data</p></td>
</tr>
<tr>
<td><p role="column_definition">stxdinherit <code>bool</code></p>
<p>If true, the stats include values from child tables, not just the values in the specified relation</p></td>
</tr>
<tr>
<td><p role="column_definition">stxdndistinct <code>pg_ndistinct</code></p>
<p>N-distinct counts, serialized as pg_ndistinct type</p></td>
</tr>
<tr>
<td><p role="column_definition">stxddependencies <code>pg_dependencies</code></p>
<p>Functional dependency statistics, serialized as pg_dependencies type</p></td>
</tr>
<tr>
<td><p role="column_definition">stxdmcv <code>pg_mcv_list</code></p>
<p>MCV (most-common values) list statistics, serialized as pg_mcv_list type</p></td>
</tr>
<tr>
<td><p role="column_definition">stxdexpr <code>pg_statistic[]</code></p>
<p>Per-expression statistics, serialized as an array of pg_statistic type</p></td>
</tr>
</tbody>
</table>

## pg_subscription

pg_subscription

The catalog pg_subscription contains all existing logical replication subscriptions. For more information about logical replication see [???](#logical-replication).

Unlike most system catalogs, pg_subscription is shared across all databases of a cluster: there is only one copy of pg_subscription per cluster, not one per database.

Access to the column subconninfo is revoked from normal users, because it could contain plain-text passwords.

<table>
<caption>pg_subscription Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">subdbid <code>oid</code> (references <a href="#catalog-pg-database">pg_database</a>.oid)</p>
<p>OID of the database that the subscription resides in</p></td>
</tr>
<tr>
<td><p role="column_definition">subskiplsn <code>pg_lsn</code></p>
<p>Finish LSN of the transaction whose changes are to be skipped, if a valid LSN; otherwise <code>0/0</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">subname <code>name</code></p>
<p>Name of the subscription</p></td>
</tr>
<tr>
<td><p role="column_definition">subowner <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>Owner of the subscription</p></td>
</tr>
<tr>
<td><p role="column_definition">subenabled <code>bool</code></p>
<p>If true, the subscription is enabled and should be replicating</p></td>
</tr>
<tr>
<td><p role="column_definition">subbinary <code>bool</code></p>
<p>If true, the subscription will request that the publisher send data in binary format</p></td>
</tr>
<tr>
<td><p role="column_definition">substream <code>char</code></p>
<p>Controls how to handle the streaming of in-progress transactions: <code>f</code> = disallow streaming of in-progress transactions, <code>t</code> = spill the changes of in-progress transactions to disk and apply at once after the transaction is committed on the publisher and received by the subscriber, <code>p</code> = apply changes directly using a parallel apply worker if available (same as <code>t</code> if no worker is available)</p></td>
</tr>
<tr>
<td><p role="column_definition">subtwophasestate <code>char</code></p>
<p>State codes for two-phase mode: <code>d</code> = disabled, <code>p</code> = pending enablement, <code>e</code> = enabled</p></td>
</tr>
<tr>
<td><p role="column_definition">subdisableonerr <code>bool</code></p>
<p>If true, the subscription will be disabled if one of its workers detects an error</p></td>
</tr>
<tr>
<td><p role="column_definition">subpasswordrequired <code>bool</code></p>
<p>If true, the subscription will be required to specify a password for authentication</p></td>
</tr>
<tr>
<td><p role="column_definition">subrunasowner <code>bool</code></p>
<p>If true, the subscription will be run with the permissions of the subscription owner</p></td>
</tr>
<tr>
<td><p role="column_definition">subfailover <code>bool</code></p>
<p>If true, the associated replication slots (i.e. the main slot and the table sync slots) in the upstream database are enabled to be synchronized to the standbys</p></td>
</tr>
<tr>
<td><p role="column_definition">subconninfo <code>text</code></p>
<p>Connection string to the upstream database</p></td>
</tr>
<tr>
<td><p role="column_definition">subslotname <code>name</code></p>
<p>Name of the replication slot in the upstream database (also used for the local replication origin name); null represents <code>NONE</code></p></td>
</tr>
<tr>
<td><p role="column_definition">subsynccommit <code>text</code></p>
<p>The <code>synchronous_commit</code> setting for the subscription's workers to use</p></td>
</tr>
<tr>
<td><p role="column_definition">subpublications <code>text[]</code></p>
<p>Array of subscribed publication names. These reference publications defined in the upstream database. For more on publications see <a href="#logical-replication-publication">???</a>.</p></td>
</tr>
<tr>
<td><p role="column_definition">suborigin <code>text</code></p>
<p>The origin value must be either <code>none</code> or <code>any</code>. The default is <code>any</code>. If <code>none</code>, the subscription will request the publisher to only send changes that don't have an origin. If <code>any</code>, the publisher sends changes regardless of their origin.</p></td>
</tr>
</tbody>
</table>

## pg_subscription_rel

pg_subscription_rel

The catalog pg_subscription_rel contains the state for each replicated relation in each subscription. This is a many-to-many mapping.

This catalog only contains tables known to the subscription after running either [`CREATE SUBSCRIPTION`](#sql-createsubscription) or [`ALTER SUBSCRIPTION ... REFRESH PUBLICATION`](#sql-altersubscription).

<table>
<caption>pg_subscription_rel Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">srsubid <code>oid</code> (references <a href="#catalog-pg-subscription">pg_subscription</a>.oid)</p>
<p>Reference to subscription</p></td>
</tr>
<tr>
<td><p role="column_definition">srrelid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>Reference to relation</p></td>
</tr>
<tr>
<td><p role="column_definition">srsubstate <code>char</code></p>
<p>State code: <code>i</code> = initialize, <code>d</code> = data is being copied, <code>f</code> = finished table copy, <code>s</code> = synchronized, <code>r</code> = ready (normal replication)</p></td>
</tr>
<tr>
<td><p role="column_definition">srsublsn <code>pg_lsn</code></p>
<p>Remote LSN of the state change used for synchronization coordination when in <code>s</code> or <code>r</code> states, otherwise null</p></td>
</tr>
</tbody>
</table>

## pg_tablespace

pg_tablespace

The catalog pg_tablespace stores information about the available tablespaces. Tables can be placed in particular tablespaces to aid administration of disk layout.

Unlike most system catalogs, pg_tablespace is shared across all databases of a cluster: there is only one copy of pg_tablespace per cluster, not one per database.

<table>
<caption>pg_tablespace Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">spcname <code>name</code></p>
<p>Tablespace name</p></td>
</tr>
<tr>
<td><p role="column_definition">spcowner <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>Owner of the tablespace, usually the user who created it</p></td>
</tr>
<tr>
<td><p role="column_definition">spcacl <code>aclitem[]</code></p>
<p>Access privileges; see <a href="#ddl-priv">???</a> for details</p></td>
</tr>
<tr>
<td><p role="column_definition">spcoptions <code>text[]</code></p>
<p>Tablespace-level options, as “keyword=value” strings</p></td>
</tr>
</tbody>
</table>

## pg_transform

pg_transform

The catalog pg_transform stores information about transforms, which are a mechanism to adapt data types to procedural languages. See [???](#sql-createtransform) for more information.

<table>
<caption>pg_transform Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">trftype <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>OID of the data type this transform is for</p></td>
</tr>
<tr>
<td><p role="column_definition">trflang <code>oid</code> (references <a href="#catalog-pg-language">pg_language</a>.oid)</p>
<p>OID of the language this transform is for</p></td>
</tr>
<tr>
<td><p role="column_definition">trffromsql <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>The OID of the function to use when converting the data type for input to the procedural language (e.g., function parameters). Zero is stored if the default behavior should be used.</p></td>
</tr>
<tr>
<td><p role="column_definition">trftosql <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>The OID of the function to use when converting output from the procedural language (e.g., return values) to the data type. Zero is stored if the default behavior should be used.</p></td>
</tr>
</tbody>
</table>

## pg_trigger

pg_trigger

The catalog pg_trigger stores triggers on tables and views. See [???](#sql-createtrigger) for more information.

<table>
<caption>pg_trigger Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">tgrelid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The table this trigger is on</p></td>
</tr>
<tr>
<td><p role="column_definition">tgparentid <code>oid</code> (references <a href="#catalog-pg-trigger">pg_trigger</a>.oid)</p>
<p>Parent trigger that this trigger is cloned from (this happens when partitions are created or attached to a partitioned table); zero if not a clone</p></td>
</tr>
<tr>
<td><p role="column_definition">tgname <code>name</code></p>
<p>Trigger name (must be unique among triggers of same table)</p></td>
</tr>
<tr>
<td><p role="column_definition">tgfoid <code>oid</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>The function to be called</p></td>
</tr>
<tr>
<td><p role="column_definition">tgtype <code>int2</code></p>
<p>Bit mask identifying trigger firing conditions</p></td>
</tr>
<tr>
<td><p role="column_definition">tgenabled <code>char</code></p>
<p>Controls in which <a href="#guc-session-replication-role">???</a> modes the trigger fires. <code>O</code> = trigger fires in “origin” and “local” modes, <code>D</code> = trigger is disabled, <code>R</code> = trigger fires in “replica” mode, <code>A</code> = trigger fires always.</p></td>
</tr>
<tr>
<td><p role="column_definition">tgisinternal <code>bool</code></p>
<p>True if trigger is internally generated (usually, to enforce the constraint identified by tgconstraint)</p></td>
</tr>
<tr>
<td><p role="column_definition">tgconstrrelid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The table referenced by a referential integrity constraint (zero if trigger is not for a referential integrity constraint)</p></td>
</tr>
<tr>
<td><p role="column_definition">tgconstrindid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>The index supporting a unique, primary key, referential integrity, or exclusion constraint (zero if trigger is not for one of these types of constraint)</p></td>
</tr>
<tr>
<td><p role="column_definition">tgconstraint <code>oid</code> (references <a href="#catalog-pg-constraint">pg_constraint</a>.oid)</p>
<p>The <a href="#catalog-pg-constraint">pg_constraint</a> entry associated with the trigger (zero if trigger is not for a constraint)</p></td>
</tr>
<tr>
<td><p role="column_definition">tgdeferrable <code>bool</code></p>
<p>True if constraint trigger is deferrable</p></td>
</tr>
<tr>
<td><p role="column_definition">tginitdeferred <code>bool</code></p>
<p>True if constraint trigger is initially deferred</p></td>
</tr>
<tr>
<td><p role="column_definition">tgnargs <code>int2</code></p>
<p>Number of argument strings passed to trigger function</p></td>
</tr>
<tr>
<td><p role="column_definition">tgattr <code>int2vector</code> (references <a href="#catalog-pg-attribute">pg_attribute</a>.attnum)</p>
<p>Column numbers, if trigger is column-specific; otherwise an empty array</p></td>
</tr>
<tr>
<td><p role="column_definition">tgargs <code>bytea</code></p>
<p>Argument strings to pass to trigger, each NULL-terminated</p></td>
</tr>
<tr>
<td><p role="column_definition">tgqual <code>pg_node_tree</code></p>
<p>Expression tree (in <code>nodeToString()</code> representation) for the trigger's <code>WHEN</code> condition, or null if none</p></td>
</tr>
<tr>
<td><p role="column_definition">tgoldtable <code>name</code></p>
<p><code>REFERENCING</code> clause name for <code>OLD TABLE</code>, or null if none</p></td>
</tr>
<tr>
<td><p role="column_definition">tgnewtable <code>name</code></p>
<p><code>REFERENCING</code> clause name for <code>NEW TABLE</code>, or null if none</p></td>
</tr>
</tbody>
</table>

Currently, column-specific triggering is supported only for `UPDATE` events, and so tgattr is relevant only for that event type. tgtype might contain bits for other event types as well, but those are presumed to be table-wide regardless of what is in tgattr.

> [!NOTE]
> When tgconstraint is nonzero, tgconstrrelid, tgconstrindid, tgdeferrable, and tginitdeferred are largely redundant with the referenced [pg_constraint](#catalog-pg-constraint) entry. However, it is possible for a non-deferrable trigger to be associated with a deferrable constraint: foreign key constraints can have some deferrable and some non-deferrable triggers.

> [!NOTE]
> `pg_class.relhastriggers` must be true if a relation has any triggers in this catalog.

## pg_ts_config

pg_ts_config

The pg_ts_config catalog contains entries representing text search configurations. A configuration specifies a particular text search parser and a list of dictionaries to use for each of the parser's output token types. The parser is shown in the pg_ts_config entry, but the token-to-dictionary mapping is defined by subsidiary entries in [pg_ts_config_map](#catalog-pg-ts-config-map).

PostgreSQL's text search features are described at length in [???](#textsearch).

<table>
<caption>pg_ts_config Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">cfgname <code>name</code></p>
<p>Text search configuration name</p></td>
</tr>
<tr>
<td><p role="column_definition">cfgnamespace <code>oid</code> (references <a href="#catalog-pg-namespace">pg_namespace</a>.oid)</p>
<p>The OID of the namespace that contains this configuration</p></td>
</tr>
<tr>
<td><p role="column_definition">cfgowner <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>Owner of the configuration</p></td>
</tr>
<tr>
<td><p role="column_definition">cfgparser <code>oid</code> (references <a href="#catalog-pg-ts-parser">pg_ts_parser</a>.oid)</p>
<p>The OID of the text search parser for this configuration</p></td>
</tr>
</tbody>
</table>

## pg_ts_config_map

pg_ts_config_map

The pg_ts_config_map catalog contains entries showing which text search dictionaries should be consulted, and in what order, for each output token type of each text search configuration's parser.

PostgreSQL's text search features are described at length in [???](#textsearch).

<table>
<caption>pg_ts_config_map Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">mapcfg <code>oid</code> (references <a href="#catalog-pg-ts-config">pg_ts_config</a>.oid)</p>
<p>The OID of the <a href="#catalog-pg-ts-config">pg_ts_config</a> entry owning this map entry</p></td>
</tr>
<tr>
<td><p role="column_definition">maptokentype <code>int4</code></p>
<p>A token type emitted by the configuration's parser</p></td>
</tr>
<tr>
<td><p role="column_definition">mapseqno <code>int4</code></p>
<p>Order in which to consult this entry (lower mapseqnos first)</p></td>
</tr>
<tr>
<td><p role="column_definition">mapdict <code>oid</code> (references <a href="#catalog-pg-ts-dict">pg_ts_dict</a>.oid)</p>
<p>The OID of the text search dictionary to consult</p></td>
</tr>
</tbody>
</table>

## pg_ts_dict

pg_ts_dict

The pg_ts_dict catalog contains entries defining text search dictionaries. A dictionary depends on a text search template, which specifies all the implementation functions needed; the dictionary itself provides values for the user-settable parameters supported by the template. This division of labor allows dictionaries to be created by unprivileged users. The parameters are specified by a text string dictinitoption, whose format and meaning vary depending on the template.

PostgreSQL's text search features are described at length in [???](#textsearch).

<table>
<caption>pg_ts_dict Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">dictname <code>name</code></p>
<p>Text search dictionary name</p></td>
</tr>
<tr>
<td><p role="column_definition">dictnamespace <code>oid</code> (references <a href="#catalog-pg-namespace">pg_namespace</a>.oid)</p>
<p>The OID of the namespace that contains this dictionary</p></td>
</tr>
<tr>
<td><p role="column_definition">dictowner <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>Owner of the dictionary</p></td>
</tr>
<tr>
<td><p role="column_definition">dicttemplate <code>oid</code> (references <a href="#catalog-pg-ts-template">pg_ts_template</a>.oid)</p>
<p>The OID of the text search template for this dictionary</p></td>
</tr>
<tr>
<td><p role="column_definition">dictinitoption <code>text</code></p>
<p>Initialization option string for the template</p></td>
</tr>
</tbody>
</table>

## pg_ts_parser

pg_ts_parser

The pg_ts_parser catalog contains entries defining text search parsers. A parser is responsible for splitting input text into lexemes and assigning a token type to each lexeme. Since a parser must be implemented by C-language-level functions, creation of new parsers is restricted to database superusers.

PostgreSQL's text search features are described at length in [???](#textsearch).

<table>
<caption>pg_ts_parser Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">prsname <code>name</code></p>
<p>Text search parser name</p></td>
</tr>
<tr>
<td><p role="column_definition">prsnamespace <code>oid</code> (references <a href="#catalog-pg-namespace">pg_namespace</a>.oid)</p>
<p>The OID of the namespace that contains this parser</p></td>
</tr>
<tr>
<td><p role="column_definition">prsstart <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>OID of the parser's startup function</p></td>
</tr>
<tr>
<td><p role="column_definition">prstoken <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>OID of the parser's next-token function</p></td>
</tr>
<tr>
<td><p role="column_definition">prsend <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>OID of the parser's shutdown function</p></td>
</tr>
<tr>
<td><p role="column_definition">prsheadline <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>OID of the parser's headline function (zero if none)</p></td>
</tr>
<tr>
<td><p role="column_definition">prslextype <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>OID of the parser's lextype function</p></td>
</tr>
</tbody>
</table>

## pg_ts_template

pg_ts_template

The pg_ts_template catalog contains entries defining text search templates. A template is the implementation skeleton for a class of text search dictionaries. Since a template must be implemented by C-language-level functions, creation of new templates is restricted to database superusers.

PostgreSQL's text search features are described at length in [???](#textsearch).

<table>
<caption>pg_ts_template Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">tmplname <code>name</code></p>
<p>Text search template name</p></td>
</tr>
<tr>
<td><p role="column_definition">tmplnamespace <code>oid</code> (references <a href="#catalog-pg-namespace">pg_namespace</a>.oid)</p>
<p>The OID of the namespace that contains this template</p></td>
</tr>
<tr>
<td><p role="column_definition">tmplinit <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>OID of the template's initialization function (zero if none)</p></td>
</tr>
<tr>
<td><p role="column_definition">tmpllexize <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>OID of the template's lexize function</p></td>
</tr>
</tbody>
</table>

## pg_type

pg_type

The catalog pg_type stores information about data types. Base types and enum types (scalar types) are created with [`CREATE TYPE`](#sql-createtype), and domains with [`CREATE DOMAIN`](#sql-createdomain). A composite type is automatically created for each table in the database, to represent the row structure of the table. It is also possible to create composite types with `CREATE TYPE AS`.

<table>
<caption>pg_type Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">typname <code>name</code></p>
<p>Data type name</p></td>
</tr>
<tr>
<td><p role="column_definition">typnamespace <code>oid</code> (references <a href="#catalog-pg-namespace">pg_namespace</a>.oid)</p>
<p>The OID of the namespace that contains this type</p></td>
</tr>
<tr>
<td><p role="column_definition">typowner <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>Owner of the type</p></td>
</tr>
<tr>
<td><p role="column_definition">typlen <code>int2</code></p>
<p>For a fixed-size type, typlen is the number of bytes in the internal representation of the type. But for a variable-length type, typlen is negative. -1 indicates a “varlena” type (one that has a length word), -2 indicates a null-terminated C string.</p></td>
</tr>
<tr>
<td><p role="column_definition">typbyval <code>bool</code></p>
<p>typbyval determines whether internal routines pass a value of this type by value or by reference. typbyval had better be false if typlen is not 1, 2, or 4 (or 8 on machines where Datum is 8 bytes). Variable-length types are always passed by reference. Note that typbyval can be false even if the length would allow pass-by-value.</p></td>
</tr>
<tr>
<td><p role="column_definition">typtype <code>char</code></p>
<p>typtype is <code>b</code> for a base type, <code>c</code> for a composite type (e.g., a table's row type), <code>d</code> for a domain, <code>e</code> for an enum type, <code>p</code> for a pseudo-type, <code>r</code> for a range type, or <code>m</code> for a multirange type. See also typrelid and typbasetype.</p></td>
</tr>
<tr>
<td><p role="column_definition">typcategory <code>char</code></p>
<p>typcategory is an arbitrary classification of data types that is used by the parser to determine which implicit casts should be “preferred”. See <a href="#catalog-typcategory-table"> Codes</a>.</p></td>
</tr>
<tr>
<td><p role="column_definition">typispreferred <code>bool</code></p>
<p>True if the type is a preferred cast target within its typcategory</p></td>
</tr>
<tr>
<td><p role="column_definition">typisdefined <code>bool</code></p>
<p>True if the type is defined, false if this is a placeholder entry for a not-yet-defined type. When typisdefined is false, nothing except the type name, namespace, and OID can be relied on.</p></td>
</tr>
<tr>
<td><p role="column_definition">typdelim <code>char</code></p>
<p>Character that separates two values of this type when parsing array input. Note that the delimiter is associated with the array element data type, not the array data type.</p></td>
</tr>
<tr>
<td><p role="column_definition">typrelid <code>oid</code> (references <a href="#catalog-pg-class">pg_class</a>.oid)</p>
<p>If this is a composite type (see typtype), then this column points to the <a href="#catalog-pg-class">pg_class</a> entry that defines the corresponding table. (For a free-standing composite type, the <a href="#catalog-pg-class">pg_class</a> entry doesn't really represent a table, but it is needed anyway for the type's <a href="#catalog-pg-attribute">pg_attribute</a> entries to link to.) Zero for non-composite types.</p></td>
</tr>
<tr>
<td><p role="column_definition">typsubscript <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>Subscripting handler function's OID, or zero if this type doesn't support subscripting. Types that are “true” array types have typsubscript = <code>array_subscript_handler</code>, but other types may have other handler functions to implement specialized subscripting behavior.</p></td>
</tr>
<tr>
<td><p role="column_definition">typelem <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>If typelem is not zero then it identifies another row in pg_type, defining the type yielded by subscripting. This should be zero if typsubscript is zero. However, it can be zero when typsubscript isn't zero, if the handler doesn't need typelem to determine the subscripting result type. Note that a typelem dependency is considered to imply physical containment of the element type in this type; so DDL changes on the element type might be restricted by the presence of this type.</p></td>
</tr>
<tr>
<td><p role="column_definition">typarray <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>If typarray is not zero then it identifies another row in pg_type, which is the “true” array type having this type as element</p></td>
</tr>
<tr>
<td><p role="column_definition">typinput <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>Input conversion function (text format)</p></td>
</tr>
<tr>
<td><p role="column_definition">typoutput <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>Output conversion function (text format)</p></td>
</tr>
<tr>
<td><p role="column_definition">typreceive <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>Input conversion function (binary format), or zero if none</p></td>
</tr>
<tr>
<td><p role="column_definition">typsend <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>Output conversion function (binary format), or zero if none</p></td>
</tr>
<tr>
<td><p role="column_definition">typmodin <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>Type modifier input function, or zero if type does not support modifiers</p></td>
</tr>
<tr>
<td><p role="column_definition">typmodout <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>Type modifier output function, or zero to use the standard format</p></td>
</tr>
<tr>
<td><p role="column_definition">typanalyze <code>regproc</code> (references <a href="#catalog-pg-proc">pg_proc</a>.oid)</p>
<p>Custom <a href="#sql-analyze">???</a> function, or zero to use the standard function</p></td>
</tr>
<tr>
<td><p role="column_definition">typalign <code>char</code></p>
<p>typalign is the alignment required when storing a value of this type. It applies to storage on disk as well as most representations of the value inside PostgreSQL. When multiple values are stored consecutively, such as in the representation of a complete row on disk, padding is inserted before a datum of this type so that it begins on the specified boundary. The alignment reference is the beginning of the first datum in the sequence. Possible values are:</p>
<ul>
<li><p><code>c</code> = <code>char</code> alignment, i.e., no alignment needed.</p></li>
<li><p><code>s</code> = <code>short</code> alignment (2 bytes on most machines).</p></li>
<li><p><code>i</code> = <code>int</code> alignment (4 bytes on most machines).</p></li>
<li><p><code>d</code> = <code>double</code> alignment (8 bytes on many machines, but by no means all).</p></li>
</ul></td>
</tr>
<tr>
<td><p role="column_definition">typstorage <code>char</code></p>
<p>typstorage tells for varlena types (those with typlen = -1) if the type is prepared for toasting and what the default strategy for attributes of this type should be. Possible values are:</p>
<ul>
<li><p><code>p</code> (plain): Values must always be stored plain (non-varlena types always use this value).</p></li>
<li><p><code>e</code> (external): Values can be stored in a secondary “TOAST” relation (if relation has one, see <code>pg_class.reltoastrelid</code>).</p></li>
<li><p><code>m</code> (main): Values can be compressed and stored inline.</p></li>
<li><p><code>x</code> (extended): Values can be compressed and/or moved to a secondary relation.</p></li>
</ul>
<p><code>x</code> is the usual choice for toast-able types. Note that <code>m</code> values can also be moved out to secondary storage, but only as a last resort (<code>e</code> and <code>x</code> values are moved first).</p></td>
</tr>
<tr>
<td><p role="column_definition">typnotnull <code>bool</code></p>
<p>typnotnull represents a not-null constraint on a type. Used for domains only.</p></td>
</tr>
<tr>
<td><p role="column_definition">typbasetype <code>oid</code> (references <a href="#catalog-pg-type">pg_type</a>.oid)</p>
<p>If this is a domain (see typtype), then typbasetype identifies the type that this one is based on. Zero if this type is not a domain.</p></td>
</tr>
<tr>
<td><p role="column_definition">typtypmod <code>int4</code></p>
<p>Domains use typtypmod to record the <code>typmod</code> to be applied to their base type (-1 if base type does not use a <code>typmod</code>). -1 if this type is not a domain.</p></td>
</tr>
<tr>
<td><p role="column_definition">typndims <code>int4</code></p>
<p>typndims is the number of array dimensions for a domain over an array (that is, typbasetype is an array type). Zero for types other than domains over array types.</p></td>
</tr>
<tr>
<td><p role="column_definition">typcollation <code>oid</code> (references <a href="#catalog-pg-collation">pg_collation</a>.oid)</p>
<p>typcollation specifies the collation of the type. If the type does not support collations, this will be zero. A base type that supports collations will have a nonzero value here, typically <code>DEFAULT_COLLATION_OID</code>. A domain over a collatable type can have a collation OID different from its base type's, if one was specified for the domain.</p></td>
</tr>
<tr>
<td><p role="column_definition">typdefaultbin <code>pg_node_tree</code></p>
<p>If typdefaultbin is not null, it is the <code>nodeToString()</code> representation of a default expression for the type. This is only used for domains.</p></td>
</tr>
<tr>
<td><p role="column_definition">typdefault <code>text</code></p>
<p>typdefault is null if the type has no associated default value. If typdefaultbin is not null, typdefault must contain a human-readable version of the default expression represented by typdefaultbin. If typdefaultbin is null and typdefault is not, then typdefault is the external representation of the type's default value, which can be fed to the type's input converter to produce a constant.</p></td>
</tr>
<tr>
<td><p role="column_definition">typacl <code>aclitem[]</code></p>
<p>Access privileges; see <a href="#ddl-priv">???</a> for details</p></td>
</tr>
</tbody>
</table>

> [!NOTE]
> For fixed-width types used in system tables, it is critical that the size and alignment defined in pg_type agree with the way that the compiler will lay out the column in a structure representing a table row.

[ Codes](#catalog-typcategory-table) lists the system-defined values of typcategory. Any future additions to this list will also be upper-case ASCII letters. All other ASCII characters are reserved for user-defined categories.

| Code | Category              |
|------|-----------------------|
| `A`  | Array types           |
| `B`  | Boolean types         |
| `C`  | Composite types       |
| `D`  | Date/time types       |
| `E`  | Enum types            |
| `G`  | Geometric types       |
| `I`  | Network address types |
| `N`  | Numeric types         |
| `P`  | Pseudo-types          |
| `R`  | Range types           |
| `S`  | String types          |
| `T`  | Timespan types        |
| `U`  | User-defined types    |
| `V`  | Bit-string types      |
| `X`  | `unknown` type        |
| `Z`  | Internal-use types    |

typcategory Codes {#catalog-typcategory-table}

## pg_user_mapping

pg_user_mapping

The catalog pg_user_mapping stores the mappings from local user to remote. Access to this catalog is restricted from normal users, use the view [pg_user_mappings](#view-pg-user-mappings) instead.

<table>
<caption>pg_user_mapping Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">oid <code>oid</code></p>
<p>Row identifier</p></td>
</tr>
<tr>
<td><p role="column_definition">umuser <code>oid</code> (references <a href="#catalog-pg-authid">pg_authid</a>.oid)</p>
<p>OID of the local role being mapped, or zero if the user mapping is public</p></td>
</tr>
<tr>
<td><p role="column_definition">umserver <code>oid</code> (references <a href="#catalog-pg-foreign-server">pg_foreign_server</a>.oid)</p>
<p>The OID of the foreign server that contains this mapping</p></td>
</tr>
<tr>
<td><p role="column_definition">umoptions <code>text[]</code></p>
<p>User mapping specific options, as “keyword=value” strings</p></td>
</tr>
</tbody>
</table>
