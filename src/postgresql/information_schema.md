---
title: The Information Schema
source_url: https://www.postgresql.org/docs/17/information-schema.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: information_schema.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 710
---

## The Information Schema

information schema

The information schema consists of a set of views that contain information about the objects defined in the current database. The information schema is defined in the SQL standard and can therefore be expected to be portable and remain stable unlike the system catalogs, which are specific to PostgreSQL and are modeled after implementation concerns. The information schema views do not, however, contain information about PostgreSQL-specific features; to inquire about those you need to query the system catalogs or other PostgreSQL-specific views.

> [!NOTE]
> When querying the database for constraint information, it is possible for a standard-compliant query that expects to return one row to return several. This is because the SQL standard requires constraint names to be unique within a schema, but PostgreSQL does not enforce this restriction. PostgreSQL automatically-generated constraint names avoid duplicates in the same schema, but users can specify such duplicate names.
>
> This problem can appear when querying information schema views such as `check_constraint_routine_usage`, `check_constraints`, `domain_constraints`, and `referential_constraints`. Some other views have similar issues but contain the table name to help distinguish duplicate rows, e.g., `constraint_column_usage`, `constraint_table_usage`, `table_constraints`.

## The Schema

The information schema itself is a schema named `information_schema`. This schema automatically exists in all databases. The owner of this schema is the initial database user in the cluster, and that user naturally has all the privileges on this schema, including the ability to drop it (but the space savings achieved by that are minuscule).

By default, the information schema is not in the schema search path, so you need to access all objects in it through qualified names. Since the names of some of the objects in the information schema are generic names that might occur in user applications, you should be careful if you want to put the information schema in the path.

## Data Types

The columns of the information schema views use special data types that are defined in the information schema. These are defined as simple domains over ordinary built-in types. You should not use these types for work outside the information schema, but your applications must be prepared for them if they select from the information schema.

These types are:

`cardinal_number`  
A nonnegative integer.

`character_data`  
A character string (without specific maximum length).

`sql_identifier`  
A character string. This type is used for SQL identifiers, the type `character_data` is used for any other kind of text data.

`time_stamp`  
A domain over the type `timestamp with time zone`

`yes_or_no`  
A character string domain that contains either `YES` or `NO`. This is used to represent Boolean (true/false) data in the information schema. (The information schema was invented before the type `boolean` was added to the SQL standard, so this convention is necessary to keep the information schema backward compatible.)

Every column in the information schema has one of these five types.

## `information_schema_catalog_name`

`information_schema_catalog_name` is a table that always contains one row and one column containing the name of the current database (current catalog, in SQL terminology).

<table>
<caption>information_schema_catalog_name Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">catalog_name <code>sql_identifier</code></p>
<p>Name of the database that contains this information schema</p></td>
</tr>
</tbody>
</table>

## `administrable_role_​authorizations`

The view `administrable_role_authorizations` identifies all roles that the current user has the admin option for.

<table>
<caption>administrable_role_authorizations Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">grantee <code>sql_identifier</code></p>
<p>Name of the role to which this role membership was granted (can be the current user, or a different role in case of nested role memberships)</p></td>
</tr>
<tr>
<td><p role="column_definition">role_name <code>sql_identifier</code></p>
<p>Name of a role</p></td>
</tr>
<tr>
<td><p role="column_definition">is_grantable <code>yes_or_no</code></p>
<p>Always <code>YES</code></p></td>
</tr>
</tbody>
</table>

## `applicable_roles`

The view `applicable_roles` identifies all roles whose privileges the current user can use. This means there is some chain of role grants from the current user to the role in question. The current user itself is also an applicable role. The set of applicable roles is generally used for permission checking. <span class="indexterm"></span> <span class="indexterm"></span>

<table>
<caption>applicable_roles Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">grantee <code>sql_identifier</code></p>
<p>Name of the role to which this role membership was granted (can be the current user, or a different role in case of nested role memberships)</p></td>
</tr>
<tr>
<td><p role="column_definition">role_name <code>sql_identifier</code></p>
<p>Name of a role</p></td>
</tr>
<tr>
<td><p role="column_definition">is_grantable <code>yes_or_no</code></p>
<p><code>YES</code> if the grantee has the admin option on the role, <code>NO</code> if not</p></td>
</tr>
</tbody>
</table>

## `attributes`

The view `attributes` contains information about the attributes of composite data types defined in the database. (Note that the view does not give information about table columns, which are sometimes called attributes in PostgreSQL contexts.) Only those attributes are shown that the current user has access to (by way of being the owner of or having some privilege on the type).

<table>
<caption>attributes Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">udt_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the data type (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the data type</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_name <code>sql_identifier</code></p>
<p>Name of the data type</p></td>
</tr>
<tr>
<td><p role="column_definition">attribute_name <code>sql_identifier</code></p>
<p>Name of the attribute</p></td>
</tr>
<tr>
<td><p role="column_definition">ordinal_position <code>cardinal_number</code></p>
<p>Ordinal position of the attribute within the data type (count starts at 1)</p></td>
</tr>
<tr>
<td><p role="column_definition">attribute_default <code>character_data</code></p>
<p>Default expression of the attribute</p></td>
</tr>
<tr>
<td><p role="column_definition">is_nullable <code>yes_or_no</code></p>
<p><code>YES</code> if the attribute is possibly nullable, <code>NO</code> if it is known not nullable.</p></td>
</tr>
<tr>
<td><p role="column_definition">data_type <code>character_data</code></p>
<p>Data type of the attribute, if it is a built-in type, or <code>ARRAY</code> if it is some array (in that case, see the view <code>element_types</code>), else <code>USER-DEFINED</code> (in that case, the type is identified in <code>attribute_udt_name</code> and associated columns).</p></td>
</tr>
<tr>
<td><p role="column_definition">character_maximum_length <code>cardinal_number</code></p>
<p>If <code>data_type</code> identifies a character or bit string type, the declared maximum length; null for all other data types or if no maximum length was declared.</p></td>
</tr>
<tr>
<td><p role="column_definition">character_octet_length <code>cardinal_number</code></p>
<p>If <code>data_type</code> identifies a character type, the maximum possible length in octets (bytes) of a datum; null for all other data types. The maximum octet length depends on the declared character maximum length (see above) and the server encoding.</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_catalog <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_schema <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_name <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the collation of the attribute (always the current database), null if default or the data type of the attribute is not collatable</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the collation of the attribute, null if default or the data type of the attribute is not collatable</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_name <code>sql_identifier</code></p>
<p>Name of the collation of the attribute, null if default or the data type of the attribute is not collatable</p></td>
</tr>
<tr>
<td><p role="column_definition">numeric_precision <code>cardinal_number</code></p>
<p>If <code>data_type</code> identifies a numeric type, this column contains the (declared or implicit) precision of the type for this attribute. The precision indicates the number of significant digits. It can be expressed in decimal (base 10) or binary (base 2) terms, as specified in the column <code>numeric_precision_radix</code>. For all other data types, this column is null.</p></td>
</tr>
<tr>
<td><p role="column_definition">numeric_precision_radix <code>cardinal_number</code></p>
<p>If <code>data_type</code> identifies a numeric type, this column indicates in which base the values in the columns <code>numeric_precision</code> and <code>numeric_scale</code> are expressed. The value is either 2 or 10. For all other data types, this column is null.</p></td>
</tr>
<tr>
<td><p role="column_definition">numeric_scale <code>cardinal_number</code></p>
<p>If <code>data_type</code> identifies an exact numeric type, this column contains the (declared or implicit) scale of the type for this attribute. The scale indicates the number of significant digits to the right of the decimal point. It can be expressed in decimal (base 10) or binary (base 2) terms, as specified in the column <code>numeric_precision_radix</code>. For all other data types, this column is null.</p></td>
</tr>
<tr>
<td><p role="column_definition">datetime_precision <code>cardinal_number</code></p>
<p>If <code>data_type</code> identifies a date, time, timestamp, or interval type, this column contains the (declared or implicit) fractional seconds precision of the type for this attribute, that is, the number of decimal digits maintained following the decimal point in the seconds value. For all other data types, this column is null.</p></td>
</tr>
<tr>
<td><p role="column_definition">interval_type <code>character_data</code></p>
<p>If <code>data_type</code> identifies an interval type, this column contains the specification which fields the intervals include for this attribute, e.g., <code>YEAR TO MONTH</code>, <code>DAY TO SECOND</code>, etc. If no field restrictions were specified (that is, the interval accepts all fields), and for all other data types, this field is null.</p></td>
</tr>
<tr>
<td><p role="column_definition">interval_precision <code>cardinal_number</code></p>
<p>Applies to a feature not available in PostgreSQL (see <code>datetime_precision</code> for the fractional seconds precision of interval type attributes)</p></td>
</tr>
<tr>
<td><p role="column_definition">attribute_udt_catalog <code>sql_identifier</code></p>
<p>Name of the database that the attribute data type is defined in (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">attribute_udt_schema <code>sql_identifier</code></p>
<p>Name of the schema that the attribute data type is defined in</p></td>
</tr>
<tr>
<td><p role="column_definition">attribute_udt_name <code>sql_identifier</code></p>
<p>Name of the attribute data type</p></td>
</tr>
<tr>
<td><p role="column_definition">scope_catalog <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">scope_schema <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">scope_name <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">maximum_cardinality <code>cardinal_number</code></p>
<p>Always null, because arrays always have unlimited maximum cardinality in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">dtd_identifier <code>sql_identifier</code></p>
<p>An identifier of the data type descriptor of the attribute, unique among the data type descriptors pertaining to the composite type. This is mainly useful for joining with other instances of such identifiers. (The specific format of the identifier is not defined and not guaranteed to remain the same in future versions.)</p></td>
</tr>
<tr>
<td><p role="column_definition">is_derived_reference_attribute <code>yes_or_no</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
</tbody>
</table>

See also under [](#infoschema-columns), a similarly structured view, for further information on some of the columns.

## `character_sets`

The view `character_sets` identifies the character sets available in the current database. Since PostgreSQL does not support multiple character sets within one database, this view only shows one, which is the database encoding.

Take note of how the following terms are used in the SQL standard:

character repertoire  
An abstract collection of characters, for example `UNICODE`, `UCS`, or `LATIN1`. Not exposed as an SQL object, but visible in this view.

character encoding form  
An encoding of some character repertoire. Most older character repertoires only use one encoding form, and so there are no separate names for them (e.g., `LATIN2` is an encoding form applicable to the `LATIN2` repertoire). But for example Unicode has the encoding forms `UTF8`, `UTF16`, etc. (not all supported by PostgreSQL). Encoding forms are not exposed as an SQL object, but are visible in this view.

character set  
A named SQL object that identifies a character repertoire, a character encoding, and a default collation. A predefined character set would typically have the same name as an encoding form, but users could define other names. For example, the character set `UTF8` would typically identify the character repertoire `UCS`, encoding form `UTF8`, and some default collation.

You can think of an “encoding” in PostgreSQL either as a character set or a character encoding form. They will have the same name, and there can only be one in one database.

<table>
<caption>character_sets Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">character_set_catalog <code>sql_identifier</code></p>
<p>Character sets are currently not implemented as schema objects, so this column is null.</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_schema <code>sql_identifier</code></p>
<p>Character sets are currently not implemented as schema objects, so this column is null.</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_name <code>sql_identifier</code></p>
<p>Name of the character set, currently implemented as showing the name of the database encoding</p></td>
</tr>
<tr>
<td><p role="column_definition">character_repertoire <code>sql_identifier</code></p>
<p>Character repertoire, showing <code>UCS</code> if the encoding is <code>UTF8</code>, else just the encoding name</p></td>
</tr>
<tr>
<td><p role="column_definition">form_of_use <code>sql_identifier</code></p>
<p>Character encoding form, same as the database encoding</p></td>
</tr>
<tr>
<td><p role="column_definition">default_collate_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the default collation (always the current database, if any collation is identified)</p></td>
</tr>
<tr>
<td><p role="column_definition">default_collate_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the default collation</p></td>
</tr>
<tr>
<td><p role="column_definition">default_collate_name <code>sql_identifier</code></p>
<p>Name of the default collation. The default collation is identified as the collation that matches the <code>COLLATE</code> and <code>CTYPE</code> settings of the current database. If there is no such collation, then this column and the associated schema and catalog columns are null.</p></td>
</tr>
</tbody>
</table>

## `check_constraint_routine_usage`

The view `check_constraint_routine_usage` identifies routines (functions and procedures) that are used by a check constraint. Only those routines are shown that are owned by a currently enabled role.

<table>
<caption>check_constraint_routine_usage Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">constraint_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the constraint (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">constraint_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">constraint_name <code>sql_identifier</code></p>
<p>Name of the constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the function (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the function</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_name <code>sql_identifier</code></p>
<p>The “specific name” of the function. See <a href="#infoschema-routines"></a> for more information.</p></td>
</tr>
</tbody>
</table>

## `check_constraints`

The view `check_constraints` contains all check constraints, either defined on a table or on a domain, that are owned by a currently enabled role. (The owner of the table or domain is the owner of the constraint.)

The SQL standard considers not-null constraints to be check constraints with a `CHECK (column_name IS NOT NULL)` expression. So not-null constraints are also included here and don't have a separate view.

<table>
<caption>check_constraints Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">constraint_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the constraint (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">constraint_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">constraint_name <code>sql_identifier</code></p>
<p>Name of the constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">check_clause <code>character_data</code></p>
<p>The check expression of the check constraint</p></td>
</tr>
</tbody>
</table>

## `collations`

The view `collations` contains the collations available in the current database.

<table>
<caption>collations Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">collation_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the collation (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the collation</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_name <code>sql_identifier</code></p>
<p>Name of the default collation</p></td>
</tr>
<tr>
<td><p role="column_definition">pad_attribute <code>character_data</code></p>
<p>Always <code>NO PAD</code> (The alternative <code>PAD SPACE</code> is not supported by PostgreSQL.)</p></td>
</tr>
</tbody>
</table>

## `collation_character_set_​applicability`

The view `collation_character_set_applicability` identifies which character set the available collations are applicable to. In PostgreSQL, there is only one character set per database (see explanation in [](#infoschema-character-sets)), so this view does not provide much useful information.

<table>
<caption>collation_character_set_applicability Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">collation_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the collation (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the collation</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_name <code>sql_identifier</code></p>
<p>Name of the default collation</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_catalog <code>sql_identifier</code></p>
<p>Character sets are currently not implemented as schema objects, so this column is null</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_schema <code>sql_identifier</code></p>
<p>Character sets are currently not implemented as schema objects, so this column is null</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_name <code>sql_identifier</code></p>
<p>Name of the character set</p></td>
</tr>
</tbody>
</table>

## `column_column_usage`

The view `column_column_usage` identifies all generated columns that depend on another base column in the same table. Only tables owned by a currently enabled role are included.

<table>
<caption>column_column_usage Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">table_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the table (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">table_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the table</p></td>
</tr>
<tr>
<td><p role="column_definition">table_name <code>sql_identifier</code></p>
<p>Name of the table</p></td>
</tr>
<tr>
<td><p role="column_definition">column_name <code>sql_identifier</code></p>
<p>Name of the base column that a generated column depends on</p></td>
</tr>
<tr>
<td><p role="column_definition">dependent_column <code>sql_identifier</code></p>
<p>Name of the generated column</p></td>
</tr>
</tbody>
</table>

## `column_domain_usage`

The view `column_domain_usage` identifies all columns (of a table or a view) that make use of some domain defined in the current database and owned by a currently enabled role.

<table>
<caption>column_domain_usage Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">domain_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the domain (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">domain_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the domain</p></td>
</tr>
<tr>
<td><p role="column_definition">domain_name <code>sql_identifier</code></p>
<p>Name of the domain</p></td>
</tr>
<tr>
<td><p role="column_definition">table_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the table (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">table_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the table</p></td>
</tr>
<tr>
<td><p role="column_definition">table_name <code>sql_identifier</code></p>
<p>Name of the table</p></td>
</tr>
<tr>
<td><p role="column_definition">column_name <code>sql_identifier</code></p>
<p>Name of the column</p></td>
</tr>
</tbody>
</table>

## `column_options`

The view `column_options` contains all the options defined for foreign table columns in the current database. Only those foreign table columns are shown that the current user has access to (by way of being the owner or having some privilege).

<table>
<caption>column_options Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">table_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the foreign table (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">table_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the foreign table</p></td>
</tr>
<tr>
<td><p role="column_definition">table_name <code>sql_identifier</code></p>
<p>Name of the foreign table</p></td>
</tr>
<tr>
<td><p role="column_definition">column_name <code>sql_identifier</code></p>
<p>Name of the column</p></td>
</tr>
<tr>
<td><p role="column_definition">option_name <code>sql_identifier</code></p>
<p>Name of an option</p></td>
</tr>
<tr>
<td><p role="column_definition">option_value <code>character_data</code></p>
<p>Value of the option</p></td>
</tr>
</tbody>
</table>

## `column_privileges`

The view `column_privileges` identifies all privileges granted on columns to a currently enabled role or by a currently enabled role. There is one row for each combination of column, grantor, and grantee.

If a privilege has been granted on an entire table, it will show up in this view as a grant for each column, but only for the privilege types where column granularity is possible: `SELECT`, `INSERT`, `UPDATE`, `REFERENCES`.

<table>
<caption>column_privileges Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">grantor <code>sql_identifier</code></p>
<p>Name of the role that granted the privilege</p></td>
</tr>
<tr>
<td><p role="column_definition">grantee <code>sql_identifier</code></p>
<p>Name of the role that the privilege was granted to</p></td>
</tr>
<tr>
<td><p role="column_definition">table_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the table that contains the column (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">table_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the table that contains the column</p></td>
</tr>
<tr>
<td><p role="column_definition">table_name <code>sql_identifier</code></p>
<p>Name of the table that contains the column</p></td>
</tr>
<tr>
<td><p role="column_definition">column_name <code>sql_identifier</code></p>
<p>Name of the column</p></td>
</tr>
<tr>
<td><p role="column_definition">privilege_type <code>character_data</code></p>
<p>Type of the privilege: <code>SELECT</code>, <code>INSERT</code>, <code>UPDATE</code>, or <code>REFERENCES</code></p></td>
</tr>
<tr>
<td><p role="column_definition">is_grantable <code>yes_or_no</code></p>
<p><code>YES</code> if the privilege is grantable, <code>NO</code> if not</p></td>
</tr>
</tbody>
</table>

## `column_udt_usage`

The view `column_udt_usage` identifies all columns that use data types owned by a currently enabled role. Note that in PostgreSQL, built-in data types behave like user-defined types, so they are included here as well. See also [](#infoschema-columns) for details.

<table>
<caption>column_udt_usage Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">udt_catalog <code>sql_identifier</code></p>
<p>Name of the database that the column data type (the underlying type of the domain, if applicable) is defined in (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_schema <code>sql_identifier</code></p>
<p>Name of the schema that the column data type (the underlying type of the domain, if applicable) is defined in</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_name <code>sql_identifier</code></p>
<p>Name of the column data type (the underlying type of the domain, if applicable)</p></td>
</tr>
<tr>
<td><p role="column_definition">table_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the table (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">table_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the table</p></td>
</tr>
<tr>
<td><p role="column_definition">table_name <code>sql_identifier</code></p>
<p>Name of the table</p></td>
</tr>
<tr>
<td><p role="column_definition">column_name <code>sql_identifier</code></p>
<p>Name of the column</p></td>
</tr>
</tbody>
</table>

## `columns`

The view `columns` contains information about all table columns (or view columns) in the database. System columns (`ctid`, etc.) are not included. Only those columns are shown that the current user has access to (by way of being the owner or having some privilege).

<table>
<caption>columns Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">table_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the table (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">table_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the table</p></td>
</tr>
<tr>
<td><p role="column_definition">table_name <code>sql_identifier</code></p>
<p>Name of the table</p></td>
</tr>
<tr>
<td><p role="column_definition">column_name <code>sql_identifier</code></p>
<p>Name of the column</p></td>
</tr>
<tr>
<td><p role="column_definition">ordinal_position <code>cardinal_number</code></p>
<p>Ordinal position of the column within the table (count starts at 1)</p></td>
</tr>
<tr>
<td><p role="column_definition">column_default <code>character_data</code></p>
<p>Default expression of the column</p></td>
</tr>
<tr>
<td><p role="column_definition">is_nullable <code>yes_or_no</code></p>
<p><code>YES</code> if the column is possibly nullable, <code>NO</code> if it is known not nullable. A not-null constraint is one way a column can be known not nullable, but there can be others.</p></td>
</tr>
<tr>
<td><p role="column_definition">data_type <code>character_data</code></p>
<p>Data type of the column, if it is a built-in type, or <code>ARRAY</code> if it is some array (in that case, see the view <code>element_types</code>), else <code>USER-DEFINED</code> (in that case, the type is identified in <code>udt_name</code> and associated columns). If the column is based on a domain, this column refers to the type underlying the domain (and the domain is identified in <code>domain_name</code> and associated columns).</p></td>
</tr>
<tr>
<td><p role="column_definition">character_maximum_length <code>cardinal_number</code></p>
<p>If <code>data_type</code> identifies a character or bit string type, the declared maximum length; null for all other data types or if no maximum length was declared.</p></td>
</tr>
<tr>
<td><p role="column_definition">character_octet_length <code>cardinal_number</code></p>
<p>If <code>data_type</code> identifies a character type, the maximum possible length in octets (bytes) of a datum; null for all other data types. The maximum octet length depends on the declared character maximum length (see above) and the server encoding.</p></td>
</tr>
<tr>
<td><p role="column_definition">numeric_precision <code>cardinal_number</code></p>
<p>If <code>data_type</code> identifies a numeric type, this column contains the (declared or implicit) precision of the type for this column. The precision indicates the number of significant digits. It can be expressed in decimal (base 10) or binary (base 2) terms, as specified in the column <code>numeric_precision_radix</code>. For all other data types, this column is null.</p></td>
</tr>
<tr>
<td><p role="column_definition">numeric_precision_radix <code>cardinal_number</code></p>
<p>If <code>data_type</code> identifies a numeric type, this column indicates in which base the values in the columns <code>numeric_precision</code> and <code>numeric_scale</code> are expressed. The value is either 2 or 10. For all other data types, this column is null.</p></td>
</tr>
<tr>
<td><p role="column_definition">numeric_scale <code>cardinal_number</code></p>
<p>If <code>data_type</code> identifies an exact numeric type, this column contains the (declared or implicit) scale of the type for this column. The scale indicates the number of significant digits to the right of the decimal point. It can be expressed in decimal (base 10) or binary (base 2) terms, as specified in the column <code>numeric_precision_radix</code>. For all other data types, this column is null.</p></td>
</tr>
<tr>
<td><p role="column_definition">datetime_precision <code>cardinal_number</code></p>
<p>If <code>data_type</code> identifies a date, time, timestamp, or interval type, this column contains the (declared or implicit) fractional seconds precision of the type for this column, that is, the number of decimal digits maintained following the decimal point in the seconds value. For all other data types, this column is null.</p></td>
</tr>
<tr>
<td><p role="column_definition">interval_type <code>character_data</code></p>
<p>If <code>data_type</code> identifies an interval type, this column contains the specification which fields the intervals include for this column, e.g., <code>YEAR TO MONTH</code>, <code>DAY TO SECOND</code>, etc. If no field restrictions were specified (that is, the interval accepts all fields), and for all other data types, this field is null.</p></td>
</tr>
<tr>
<td><p role="column_definition">interval_precision <code>cardinal_number</code></p>
<p>Applies to a feature not available in PostgreSQL (see <code>datetime_precision</code> for the fractional seconds precision of interval type columns)</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_catalog <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_schema <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_name <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the collation of the column (always the current database), null if default or the data type of the column is not collatable</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the collation of the column, null if default or the data type of the column is not collatable</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_name <code>sql_identifier</code></p>
<p>Name of the collation of the column, null if default or the data type of the column is not collatable</p></td>
</tr>
<tr>
<td><p role="column_definition">domain_catalog <code>sql_identifier</code></p>
<p>If the column has a domain type, the name of the database that the domain is defined in (always the current database), else null.</p></td>
</tr>
<tr>
<td><p role="column_definition">domain_schema <code>sql_identifier</code></p>
<p>If the column has a domain type, the name of the schema that the domain is defined in, else null.</p></td>
</tr>
<tr>
<td><p role="column_definition">domain_name <code>sql_identifier</code></p>
<p>If the column has a domain type, the name of the domain, else null.</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_catalog <code>sql_identifier</code></p>
<p>Name of the database that the column data type (the underlying type of the domain, if applicable) is defined in (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_schema <code>sql_identifier</code></p>
<p>Name of the schema that the column data type (the underlying type of the domain, if applicable) is defined in</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_name <code>sql_identifier</code></p>
<p>Name of the column data type (the underlying type of the domain, if applicable)</p></td>
</tr>
<tr>
<td><p role="column_definition">scope_catalog <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">scope_schema <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">scope_name <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">maximum_cardinality <code>cardinal_number</code></p>
<p>Always null, because arrays always have unlimited maximum cardinality in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">dtd_identifier <code>sql_identifier</code></p>
<p>An identifier of the data type descriptor of the column, unique among the data type descriptors pertaining to the table. This is mainly useful for joining with other instances of such identifiers. (The specific format of the identifier is not defined and not guaranteed to remain the same in future versions.)</p></td>
</tr>
<tr>
<td><p role="column_definition">is_self_referencing <code>yes_or_no</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">is_identity <code>yes_or_no</code></p>
<p>If the column is an identity column, then <code>YES</code>, else <code>NO</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">identity_generation <code>character_data</code></p>
<p>If the column is an identity column, then <code>ALWAYS</code> or <code>BY DEFAULT</code>, reflecting the definition of the column.</p></td>
</tr>
<tr>
<td><p role="column_definition">identity_start <code>character_data</code></p>
<p>If the column is an identity column, then the start value of the internal sequence, else null.</p></td>
</tr>
<tr>
<td><p role="column_definition">identity_increment <code>character_data</code></p>
<p>If the column is an identity column, then the increment of the internal sequence, else null.</p></td>
</tr>
<tr>
<td><p role="column_definition">identity_maximum <code>character_data</code></p>
<p>If the column is an identity column, then the maximum value of the internal sequence, else null.</p></td>
</tr>
<tr>
<td><p role="column_definition">identity_minimum <code>character_data</code></p>
<p>If the column is an identity column, then the minimum value of the internal sequence, else null.</p></td>
</tr>
<tr>
<td><p role="column_definition">identity_cycle <code>yes_or_no</code></p>
<p>If the column is an identity column, then <code>YES</code> if the internal sequence cycles or <code>NO</code> if it does not; otherwise null.</p></td>
</tr>
<tr>
<td><p role="column_definition">is_generated <code>character_data</code></p>
<p>If the column is a generated column, then <code>ALWAYS</code>, else <code>NEVER</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">generation_expression <code>character_data</code></p>
<p>If the column is a generated column, then the generation expression, else null.</p></td>
</tr>
<tr>
<td><p role="column_definition">is_updatable <code>yes_or_no</code></p>
<p><code>YES</code> if the column is updatable, <code>NO</code> if not (Columns in base tables are always updatable, columns in views not necessarily)</p></td>
</tr>
</tbody>
</table>

Since data types can be defined in a variety of ways in SQL, and PostgreSQL contains additional ways to define data types, their representation in the information schema can be somewhat difficult. The column `data_type` is supposed to identify the underlying built-in type of the column. In PostgreSQL, this means that the type is defined in the system catalog schema `pg_catalog`. This column might be useful if the application can handle the well-known built-in types specially (for example, format the numeric types differently or use the data in the precision columns). The columns `udt_name`, `udt_schema`, and `udt_catalog` always identify the underlying data type of the column, even if the column is based on a domain. (Since PostgreSQL treats built-in types like user-defined types, built-in types appear here as well. This is an extension of the SQL standard.) These columns should be used if an application wants to process data differently according to the type, because in that case it wouldn't matter if the column is really based on a domain. If the column is based on a domain, the identity of the domain is stored in the columns `domain_name`, `domain_schema`, and `domain_catalog`. If you want to pair up columns with their associated data types and treat domains as separate types, you could write `coalesce(domain_name, udt_name)`, etc.

## `constraint_column_usage`

The view `constraint_column_usage` identifies all columns in the current database that are used by some constraint. Only those columns are shown that are contained in a table owned by a currently enabled role. For a check constraint, this view identifies the columns that are used in the check expression. For a not-null constraint, this view identifies the column that the constraint is defined on. For a foreign key constraint, this view identifies the columns that the foreign key references. For a unique or primary key constraint, this view identifies the constrained columns.

<table>
<caption>constraint_column_usage Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">table_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the table that contains the column that is used by some constraint (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">table_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the table that contains the column that is used by some constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">table_name <code>sql_identifier</code></p>
<p>Name of the table that contains the column that is used by some constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">column_name <code>sql_identifier</code></p>
<p>Name of the column that is used by some constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">constraint_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the constraint (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">constraint_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">constraint_name <code>sql_identifier</code></p>
<p>Name of the constraint</p></td>
</tr>
</tbody>
</table>

## `constraint_table_usage`

The view `constraint_table_usage` identifies all tables in the current database that are used by some constraint and are owned by a currently enabled role. (This is different from the view `table_constraints`, which identifies all table constraints along with the table they are defined on.) For a foreign key constraint, this view identifies the table that the foreign key references. For a unique or primary key constraint, this view simply identifies the table the constraint belongs to. Check constraints and not-null constraints are not included in this view.

<table>
<caption>constraint_table_usage Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">table_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the table that is used by some constraint (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">table_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the table that is used by some constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">table_name <code>sql_identifier</code></p>
<p>Name of the table that is used by some constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">constraint_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the constraint (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">constraint_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">constraint_name <code>sql_identifier</code></p>
<p>Name of the constraint</p></td>
</tr>
</tbody>
</table>

## `data_type_privileges`

The view `data_type_privileges` identifies all data type descriptors that the current user has access to, by way of being the owner of the described object or having some privilege for it. A data type descriptor is generated whenever a data type is used in the definition of a table column, a domain, or a function (as parameter or return type) and stores some information about how the data type is used in that instance (for example, the declared maximum length, if applicable). Each data type descriptor is assigned an arbitrary identifier that is unique among the data type descriptor identifiers assigned for one object (table, domain, function). This view is probably not useful for applications, but it is used to define some other views in the information schema.

<table>
<caption>data_type_privileges Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">object_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the described object (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">object_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the described object</p></td>
</tr>
<tr>
<td><p role="column_definition">object_name <code>sql_identifier</code></p>
<p>Name of the described object</p></td>
</tr>
<tr>
<td><p role="column_definition">object_type <code>character_data</code></p>
<p>The type of the described object: one of <code>TABLE</code> (the data type descriptor pertains to a column of that table), <code>DOMAIN</code> (the data type descriptors pertains to that domain), <code>ROUTINE</code> (the data type descriptor pertains to a parameter or the return data type of that function).</p></td>
</tr>
<tr>
<td><p role="column_definition">dtd_identifier <code>sql_identifier</code></p>
<p>The identifier of the data type descriptor, which is unique among the data type descriptors for that same object.</p></td>
</tr>
</tbody>
</table>

## `domain_constraints`

The view `domain_constraints` contains all constraints belonging to domains defined in the current database. Only those domains are shown that the current user has access to (by way of being the owner or having some privilege).

<table>
<caption>domain_constraints Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">constraint_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the constraint (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">constraint_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">constraint_name <code>sql_identifier</code></p>
<p>Name of the constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">domain_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the domain (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">domain_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the domain</p></td>
</tr>
<tr>
<td><p role="column_definition">domain_name <code>sql_identifier</code></p>
<p>Name of the domain</p></td>
</tr>
<tr>
<td><p role="column_definition">is_deferrable <code>yes_or_no</code></p>
<p><code>YES</code> if the constraint is deferrable, <code>NO</code> if not</p></td>
</tr>
<tr>
<td><p role="column_definition">initially_deferred <code>yes_or_no</code></p>
<p><code>YES</code> if the constraint is deferrable and initially deferred, <code>NO</code> if not</p></td>
</tr>
</tbody>
</table>

## `domain_udt_usage`

The view `domain_udt_usage` identifies all domains that are based on data types owned by a currently enabled role. Note that in PostgreSQL, built-in data types behave like user-defined types, so they are included here as well.

<table>
<caption>domain_udt_usage Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">udt_catalog <code>sql_identifier</code></p>
<p>Name of the database that the domain data type is defined in (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_schema <code>sql_identifier</code></p>
<p>Name of the schema that the domain data type is defined in</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_name <code>sql_identifier</code></p>
<p>Name of the domain data type</p></td>
</tr>
<tr>
<td><p role="column_definition">domain_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the domain (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">domain_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the domain</p></td>
</tr>
<tr>
<td><p role="column_definition">domain_name <code>sql_identifier</code></p>
<p>Name of the domain</p></td>
</tr>
</tbody>
</table>

## `domains`

The view `domains` contains all domains defined in the current database. Only those domains are shown that the current user has access to (by way of being the owner or having some privilege).

<table>
<caption>domains Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">domain_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the domain (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">domain_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the domain</p></td>
</tr>
<tr>
<td><p role="column_definition">domain_name <code>sql_identifier</code></p>
<p>Name of the domain</p></td>
</tr>
<tr>
<td><p role="column_definition">data_type <code>character_data</code></p>
<p>Data type of the domain, if it is a built-in type, or <code>ARRAY</code> if it is some array (in that case, see the view <code>element_types</code>), else <code>USER-DEFINED</code> (in that case, the type is identified in <code>udt_name</code> and associated columns).</p></td>
</tr>
<tr>
<td><p role="column_definition">character_maximum_length <code>cardinal_number</code></p>
<p>If the domain has a character or bit string type, the declared maximum length; null for all other data types or if no maximum length was declared.</p></td>
</tr>
<tr>
<td><p role="column_definition">character_octet_length <code>cardinal_number</code></p>
<p>If the domain has a character type, the maximum possible length in octets (bytes) of a datum; null for all other data types. The maximum octet length depends on the declared character maximum length (see above) and the server encoding.</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_catalog <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_schema <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_name <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the collation of the domain (always the current database), null if default or the data type of the domain is not collatable</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the collation of the domain, null if default or the data type of the domain is not collatable</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_name <code>sql_identifier</code></p>
<p>Name of the collation of the domain, null if default or the data type of the domain is not collatable</p></td>
</tr>
<tr>
<td><p role="column_definition">numeric_precision <code>cardinal_number</code></p>
<p>If the domain has a numeric type, this column contains the (declared or implicit) precision of the type for this domain. The precision indicates the number of significant digits. It can be expressed in decimal (base 10) or binary (base 2) terms, as specified in the column <code>numeric_precision_radix</code>. For all other data types, this column is null.</p></td>
</tr>
<tr>
<td><p role="column_definition">numeric_precision_radix <code>cardinal_number</code></p>
<p>If the domain has a numeric type, this column indicates in which base the values in the columns <code>numeric_precision</code> and <code>numeric_scale</code> are expressed. The value is either 2 or 10. For all other data types, this column is null.</p></td>
</tr>
<tr>
<td><p role="column_definition">numeric_scale <code>cardinal_number</code></p>
<p>If the domain has an exact numeric type, this column contains the (declared or implicit) scale of the type for this domain. The scale indicates the number of significant digits to the right of the decimal point. It can be expressed in decimal (base 10) or binary (base 2) terms, as specified in the column <code>numeric_precision_radix</code>. For all other data types, this column is null.</p></td>
</tr>
<tr>
<td><p role="column_definition">datetime_precision <code>cardinal_number</code></p>
<p>If <code>data_type</code> identifies a date, time, timestamp, or interval type, this column contains the (declared or implicit) fractional seconds precision of the type for this domain, that is, the number of decimal digits maintained following the decimal point in the seconds value. For all other data types, this column is null.</p></td>
</tr>
<tr>
<td><p role="column_definition">interval_type <code>character_data</code></p>
<p>If <code>data_type</code> identifies an interval type, this column contains the specification which fields the intervals include for this domain, e.g., <code>YEAR TO MONTH</code>, <code>DAY TO SECOND</code>, etc. If no field restrictions were specified (that is, the interval accepts all fields), and for all other data types, this field is null.</p></td>
</tr>
<tr>
<td><p role="column_definition">interval_precision <code>cardinal_number</code></p>
<p>Applies to a feature not available in PostgreSQL (see <code>datetime_precision</code> for the fractional seconds precision of interval type domains)</p></td>
</tr>
<tr>
<td><p role="column_definition">domain_default <code>character_data</code></p>
<p>Default expression of the domain</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_catalog <code>sql_identifier</code></p>
<p>Name of the database that the domain data type is defined in (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_schema <code>sql_identifier</code></p>
<p>Name of the schema that the domain data type is defined in</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_name <code>sql_identifier</code></p>
<p>Name of the domain data type</p></td>
</tr>
<tr>
<td><p role="column_definition">scope_catalog <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">scope_schema <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">scope_name <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">maximum_cardinality <code>cardinal_number</code></p>
<p>Always null, because arrays always have unlimited maximum cardinality in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">dtd_identifier <code>sql_identifier</code></p>
<p>An identifier of the data type descriptor of the domain, unique among the data type descriptors pertaining to the domain (which is trivial, because a domain only contains one data type descriptor). This is mainly useful for joining with other instances of such identifiers. (The specific format of the identifier is not defined and not guaranteed to remain the same in future versions.)</p></td>
</tr>
</tbody>
</table>

## `element_types`

The view `element_types` contains the data type descriptors of the elements of arrays. When a table column, composite-type attribute, domain, function parameter, or function return value is defined to be of an array type, the respective information schema view only contains `ARRAY` in the column `data_type`. To obtain information on the element type of the array, you can join the respective view with this view. For example, to show the columns of a table with data types and array element types, if applicable, you could do:

    SELECT c.column_name, c.data_type, e.data_type AS element_type
    FROM information_schema.columns c LEFT JOIN information_schema.element_types e
         ON ((c.table_catalog, c.table_schema, c.table_name, 'TABLE', c.dtd_identifier)
           = (e.object_catalog, e.object_schema, e.object_name, e.object_type, e.collection_type_identifier))
    WHERE c.table_schema = '...' AND c.table_name = '...'
    ORDER BY c.ordinal_position;

This view only includes objects that the current user has access to, by way of being the owner or having some privilege.

<table>
<caption>element_types Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">object_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the object that uses the array being described (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">object_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the object that uses the array being described</p></td>
</tr>
<tr>
<td><p role="column_definition">object_name <code>sql_identifier</code></p>
<p>Name of the object that uses the array being described</p></td>
</tr>
<tr>
<td><p role="column_definition">object_type <code>character_data</code></p>
<p>The type of the object that uses the array being described: one of <code>TABLE</code> (the array is used by a column of that table), <code>USER-DEFINED TYPE</code> (the array is used by an attribute of that composite type), <code>DOMAIN</code> (the array is used by that domain), <code>ROUTINE</code> (the array is used by a parameter or the return data type of that function).</p></td>
</tr>
<tr>
<td><p role="column_definition">collection_type_identifier <code>sql_identifier</code></p>
<p>The identifier of the data type descriptor of the array being described. Use this to join with the <code>dtd_identifier</code> columns of other information schema views.</p></td>
</tr>
<tr>
<td><p role="column_definition">data_type <code>character_data</code></p>
<p>Data type of the array elements, if it is a built-in type, else <code>USER-DEFINED</code> (in that case, the type is identified in <code>udt_name</code> and associated columns).</p></td>
</tr>
<tr>
<td><p role="column_definition">character_maximum_length <code>cardinal_number</code></p>
<p>Always null, since this information is not applied to array element data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">character_octet_length <code>cardinal_number</code></p>
<p>Always null, since this information is not applied to array element data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_catalog <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_schema <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_name <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the collation of the element type (always the current database), null if default or the data type of the element is not collatable</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the collation of the element type, null if default or the data type of the element is not collatable</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_name <code>sql_identifier</code></p>
<p>Name of the collation of the element type, null if default or the data type of the element is not collatable</p></td>
</tr>
<tr>
<td><p role="column_definition">numeric_precision <code>cardinal_number</code></p>
<p>Always null, since this information is not applied to array element data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">numeric_precision_radix <code>cardinal_number</code></p>
<p>Always null, since this information is not applied to array element data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">numeric_scale <code>cardinal_number</code></p>
<p>Always null, since this information is not applied to array element data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">datetime_precision <code>cardinal_number</code></p>
<p>Always null, since this information is not applied to array element data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">interval_type <code>character_data</code></p>
<p>Always null, since this information is not applied to array element data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">interval_precision <code>cardinal_number</code></p>
<p>Always null, since this information is not applied to array element data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_catalog <code>sql_identifier</code></p>
<p>Name of the database that the data type of the elements is defined in (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_schema <code>sql_identifier</code></p>
<p>Name of the schema that the data type of the elements is defined in</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_name <code>sql_identifier</code></p>
<p>Name of the data type of the elements</p></td>
</tr>
<tr>
<td><p role="column_definition">scope_catalog <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">scope_schema <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">scope_name <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">maximum_cardinality <code>cardinal_number</code></p>
<p>Always null, because arrays always have unlimited maximum cardinality in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">dtd_identifier <code>sql_identifier</code></p>
<p>An identifier of the data type descriptor of the element. This is currently not useful.</p></td>
</tr>
</tbody>
</table>

## `enabled_roles`

The view `enabled_roles` identifies the currently “enabled roles”. The enabled roles are recursively defined as the current user together with all roles that have been granted to the enabled roles with automatic inheritance. In other words, these are all roles that the current user has direct or indirect, automatically inheriting membership in. <span class="indexterm"></span> <span class="indexterm"></span>

For permission checking, the set of “applicable roles” is applied, which can be broader than the set of enabled roles. So generally, it is better to use the view `applicable_roles` instead of this one; See [](#infoschema-applicable-roles) for details on `applicable_roles` view.

<table>
<caption>enabled_roles Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">role_name <code>sql_identifier</code></p>
<p>Name of a role</p></td>
</tr>
</tbody>
</table>

## `foreign_data_wrapper_options`

The view `foreign_data_wrapper_options` contains all the options defined for foreign-data wrappers in the current database. Only those foreign-data wrappers are shown that the current user has access to (by way of being the owner or having some privilege).

<table>
<caption>foreign_data_wrapper_options Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">foreign_data_wrapper_catalog <code>sql_identifier</code></p>
<p>Name of the database that the foreign-data wrapper is defined in (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">foreign_data_wrapper_name <code>sql_identifier</code></p>
<p>Name of the foreign-data wrapper</p></td>
</tr>
<tr>
<td><p role="column_definition">option_name <code>sql_identifier</code></p>
<p>Name of an option</p></td>
</tr>
<tr>
<td><p role="column_definition">option_value <code>character_data</code></p>
<p>Value of the option</p></td>
</tr>
</tbody>
</table>

## `foreign_data_wrappers`

The view `foreign_data_wrappers` contains all foreign-data wrappers defined in the current database. Only those foreign-data wrappers are shown that the current user has access to (by way of being the owner or having some privilege).

<table>
<caption>foreign_data_wrappers Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">foreign_data_wrapper_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the foreign-data wrapper (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">foreign_data_wrapper_name <code>sql_identifier</code></p>
<p>Name of the foreign-data wrapper</p></td>
</tr>
<tr>
<td><p role="column_definition">authorization_identifier <code>sql_identifier</code></p>
<p>Name of the owner of the foreign server</p></td>
</tr>
<tr>
<td><p role="column_definition">library_name <code>character_data</code></p>
<p>File name of the library that implementing this foreign-data wrapper</p></td>
</tr>
<tr>
<td><p role="column_definition">foreign_data_wrapper_language <code>character_data</code></p>
<p>Language used to implement this foreign-data wrapper</p></td>
</tr>
</tbody>
</table>

## `foreign_server_options`

The view `foreign_server_options` contains all the options defined for foreign servers in the current database. Only those foreign servers are shown that the current user has access to (by way of being the owner or having some privilege).

<table>
<caption>foreign_server_options Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">foreign_server_catalog <code>sql_identifier</code></p>
<p>Name of the database that the foreign server is defined in (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">foreign_server_name <code>sql_identifier</code></p>
<p>Name of the foreign server</p></td>
</tr>
<tr>
<td><p role="column_definition">option_name <code>sql_identifier</code></p>
<p>Name of an option</p></td>
</tr>
<tr>
<td><p role="column_definition">option_value <code>character_data</code></p>
<p>Value of the option</p></td>
</tr>
</tbody>
</table>

## `foreign_servers`

The view `foreign_servers` contains all foreign servers defined in the current database. Only those foreign servers are shown that the current user has access to (by way of being the owner or having some privilege).

<table>
<caption>foreign_servers Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">foreign_server_catalog <code>sql_identifier</code></p>
<p>Name of the database that the foreign server is defined in (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">foreign_server_name <code>sql_identifier</code></p>
<p>Name of the foreign server</p></td>
</tr>
<tr>
<td><p role="column_definition">foreign_data_wrapper_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the foreign-data wrapper used by the foreign server (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">foreign_data_wrapper_name <code>sql_identifier</code></p>
<p>Name of the foreign-data wrapper used by the foreign server</p></td>
</tr>
<tr>
<td><p role="column_definition">foreign_server_type <code>character_data</code></p>
<p>Foreign server type information, if specified upon creation</p></td>
</tr>
<tr>
<td><p role="column_definition">foreign_server_version <code>character_data</code></p>
<p>Foreign server version information, if specified upon creation</p></td>
</tr>
<tr>
<td><p role="column_definition">authorization_identifier <code>sql_identifier</code></p>
<p>Name of the owner of the foreign server</p></td>
</tr>
</tbody>
</table>

## `foreign_table_options`

The view `foreign_table_options` contains all the options defined for foreign tables in the current database. Only those foreign tables are shown that the current user has access to (by way of being the owner or having some privilege).

<table>
<caption>foreign_table_options Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">foreign_table_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the foreign table (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">foreign_table_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the foreign table</p></td>
</tr>
<tr>
<td><p role="column_definition">foreign_table_name <code>sql_identifier</code></p>
<p>Name of the foreign table</p></td>
</tr>
<tr>
<td><p role="column_definition">option_name <code>sql_identifier</code></p>
<p>Name of an option</p></td>
</tr>
<tr>
<td><p role="column_definition">option_value <code>character_data</code></p>
<p>Value of the option</p></td>
</tr>
</tbody>
</table>

## `foreign_tables`

The view `foreign_tables` contains all foreign tables defined in the current database. Only those foreign tables are shown that the current user has access to (by way of being the owner or having some privilege).

<table>
<caption>foreign_tables Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">foreign_table_catalog <code>sql_identifier</code></p>
<p>Name of the database that the foreign table is defined in (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">foreign_table_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the foreign table</p></td>
</tr>
<tr>
<td><p role="column_definition">foreign_table_name <code>sql_identifier</code></p>
<p>Name of the foreign table</p></td>
</tr>
<tr>
<td><p role="column_definition">foreign_server_catalog <code>sql_identifier</code></p>
<p>Name of the database that the foreign server is defined in (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">foreign_server_name <code>sql_identifier</code></p>
<p>Name of the foreign server</p></td>
</tr>
</tbody>
</table>

## `key_column_usage`

The view `key_column_usage` identifies all columns in the current database that are restricted by some unique, primary key, or foreign key constraint. Check constraints are not included in this view. Only those columns are shown that the current user has access to, by way of being the owner or having some privilege.

<table>
<caption>key_column_usage Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">constraint_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the constraint (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">constraint_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">constraint_name <code>sql_identifier</code></p>
<p>Name of the constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">table_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the table that contains the column that is restricted by this constraint (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">table_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the table that contains the column that is restricted by this constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">table_name <code>sql_identifier</code></p>
<p>Name of the table that contains the column that is restricted by this constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">column_name <code>sql_identifier</code></p>
<p>Name of the column that is restricted by this constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">ordinal_position <code>cardinal_number</code></p>
<p>Ordinal position of the column within the constraint key (count starts at 1)</p></td>
</tr>
<tr>
<td><p role="column_definition">position_in_unique_constraint <code>cardinal_number</code></p>
<p>For a foreign-key constraint, ordinal position of the referenced column within its unique constraint (count starts at 1); otherwise null</p></td>
</tr>
</tbody>
</table>

## `parameters`

The view `parameters` contains information about the parameters (arguments) of all functions in the current database. Only those functions are shown that the current user has access to (by way of being the owner or having some privilege).

<table>
<caption>parameters Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">specific_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the function (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the function</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_name <code>sql_identifier</code></p>
<p>The “specific name” of the function. See <a href="#infoschema-routines"></a> for more information.</p></td>
</tr>
<tr>
<td><p role="column_definition">ordinal_position <code>cardinal_number</code></p>
<p>Ordinal position of the parameter in the argument list of the function (count starts at 1)</p></td>
</tr>
<tr>
<td><p role="column_definition">parameter_mode <code>character_data</code></p>
<p><code>IN</code> for input parameter, <code>OUT</code> for output parameter, and <code>INOUT</code> for input/output parameter.</p></td>
</tr>
<tr>
<td><p role="column_definition">is_result <code>yes_or_no</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">as_locator <code>yes_or_no</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">parameter_name <code>sql_identifier</code></p>
<p>Name of the parameter, or null if the parameter has no name</p></td>
</tr>
<tr>
<td><p role="column_definition">data_type <code>character_data</code></p>
<p>Data type of the parameter, if it is a built-in type, or <code>ARRAY</code> if it is some array (in that case, see the view <code>element_types</code>), else <code>USER-DEFINED</code> (in that case, the type is identified in <code>udt_name</code> and associated columns).</p></td>
</tr>
<tr>
<td><p role="column_definition">character_maximum_length <code>cardinal_number</code></p>
<p>Always null, since this information is not applied to parameter data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">character_octet_length <code>cardinal_number</code></p>
<p>Always null, since this information is not applied to parameter data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_catalog <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_schema <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_name <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_catalog <code>sql_identifier</code></p>
<p>Always null, since this information is not applied to parameter data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_schema <code>sql_identifier</code></p>
<p>Always null, since this information is not applied to parameter data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_name <code>sql_identifier</code></p>
<p>Always null, since this information is not applied to parameter data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">numeric_precision <code>cardinal_number</code></p>
<p>Always null, since this information is not applied to parameter data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">numeric_precision_radix <code>cardinal_number</code></p>
<p>Always null, since this information is not applied to parameter data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">numeric_scale <code>cardinal_number</code></p>
<p>Always null, since this information is not applied to parameter data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">datetime_precision <code>cardinal_number</code></p>
<p>Always null, since this information is not applied to parameter data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">interval_type <code>character_data</code></p>
<p>Always null, since this information is not applied to parameter data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">interval_precision <code>cardinal_number</code></p>
<p>Always null, since this information is not applied to parameter data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_catalog <code>sql_identifier</code></p>
<p>Name of the database that the data type of the parameter is defined in (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_schema <code>sql_identifier</code></p>
<p>Name of the schema that the data type of the parameter is defined in</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_name <code>sql_identifier</code></p>
<p>Name of the data type of the parameter</p></td>
</tr>
<tr>
<td><p role="column_definition">scope_catalog <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">scope_schema <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">scope_name <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">maximum_cardinality <code>cardinal_number</code></p>
<p>Always null, because arrays always have unlimited maximum cardinality in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">dtd_identifier <code>sql_identifier</code></p>
<p>An identifier of the data type descriptor of the parameter, unique among the data type descriptors pertaining to the function. This is mainly useful for joining with other instances of such identifiers. (The specific format of the identifier is not defined and not guaranteed to remain the same in future versions.)</p></td>
</tr>
<tr>
<td><p role="column_definition">parameter_default <code>character_data</code></p>
<p>The default expression of the parameter, or null if none or if the function is not owned by a currently enabled role.</p></td>
</tr>
</tbody>
</table>

## `referential_constraints`

The view `referential_constraints` contains all referential (foreign key) constraints in the current database. Only those constraints are shown for which the current user has write access to the referencing table (by way of being the owner or having some privilege other than `SELECT`).

<table>
<caption>referential_constraints Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">constraint_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the constraint (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">constraint_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">constraint_name <code>sql_identifier</code></p>
<p>Name of the constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">unique_constraint_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the unique or primary key constraint that the foreign key constraint references (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">unique_constraint_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the unique or primary key constraint that the foreign key constraint references</p></td>
</tr>
<tr>
<td><p role="column_definition">unique_constraint_name <code>sql_identifier</code></p>
<p>Name of the unique or primary key constraint that the foreign key constraint references</p></td>
</tr>
<tr>
<td><p role="column_definition">match_option <code>character_data</code></p>
<p>Match option of the foreign key constraint: <code>FULL</code>, <code>PARTIAL</code>, or <code>NONE</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">update_rule <code>character_data</code></p>
<p>Update rule of the foreign key constraint: <code>CASCADE</code>, <code>SET NULL</code>, <code>SET DEFAULT</code>, <code>RESTRICT</code>, or <code>NO ACTION</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">delete_rule <code>character_data</code></p>
<p>Delete rule of the foreign key constraint: <code>CASCADE</code>, <code>SET NULL</code>, <code>SET DEFAULT</code>, <code>RESTRICT</code>, or <code>NO ACTION</code>.</p></td>
</tr>
</tbody>
</table>

## `role_column_grants`

The view `role_column_grants` identifies all privileges granted on columns where the grantor or grantee is a currently enabled role. Further information can be found under `column_privileges`. The only effective difference between this view and `column_privileges` is that this view omits columns that have been made accessible to the current user by way of a grant to `PUBLIC`.

<table>
<caption>role_column_grants Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">grantor <code>sql_identifier</code></p>
<p>Name of the role that granted the privilege</p></td>
</tr>
<tr>
<td><p role="column_definition">grantee <code>sql_identifier</code></p>
<p>Name of the role that the privilege was granted to</p></td>
</tr>
<tr>
<td><p role="column_definition">table_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the table that contains the column (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">table_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the table that contains the column</p></td>
</tr>
<tr>
<td><p role="column_definition">table_name <code>sql_identifier</code></p>
<p>Name of the table that contains the column</p></td>
</tr>
<tr>
<td><p role="column_definition">column_name <code>sql_identifier</code></p>
<p>Name of the column</p></td>
</tr>
<tr>
<td><p role="column_definition">privilege_type <code>character_data</code></p>
<p>Type of the privilege: <code>SELECT</code>, <code>INSERT</code>, <code>UPDATE</code>, or <code>REFERENCES</code></p></td>
</tr>
<tr>
<td><p role="column_definition">is_grantable <code>yes_or_no</code></p>
<p><code>YES</code> if the privilege is grantable, <code>NO</code> if not</p></td>
</tr>
</tbody>
</table>

## `role_routine_grants`

The view `role_routine_grants` identifies all privileges granted on functions where the grantor or grantee is a currently enabled role. Further information can be found under `routine_privileges`. The only effective difference between this view and `routine_privileges` is that this view omits functions that have been made accessible to the current user by way of a grant to `PUBLIC`.

<table>
<caption>role_routine_grants Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">grantor <code>sql_identifier</code></p>
<p>Name of the role that granted the privilege</p></td>
</tr>
<tr>
<td><p role="column_definition">grantee <code>sql_identifier</code></p>
<p>Name of the role that the privilege was granted to</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the function (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the function</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_name <code>sql_identifier</code></p>
<p>The “specific name” of the function. See <a href="#infoschema-routines"></a> for more information.</p></td>
</tr>
<tr>
<td><p role="column_definition">routine_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the function (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">routine_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the function</p></td>
</tr>
<tr>
<td><p role="column_definition">routine_name <code>sql_identifier</code></p>
<p>Name of the function (might be duplicated in case of overloading)</p></td>
</tr>
<tr>
<td><p role="column_definition">privilege_type <code>character_data</code></p>
<p>Always <code>EXECUTE</code> (the only privilege type for functions)</p></td>
</tr>
<tr>
<td><p role="column_definition">is_grantable <code>yes_or_no</code></p>
<p><code>YES</code> if the privilege is grantable, <code>NO</code> if not</p></td>
</tr>
</tbody>
</table>

## `role_table_grants`

The view `role_table_grants` identifies all privileges granted on tables or views where the grantor or grantee is a currently enabled role. Further information can be found under `table_privileges`. The only effective difference between this view and `table_privileges` is that this view omits tables that have been made accessible to the current user by way of a grant to `PUBLIC`.

<table>
<caption>role_table_grants Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">grantor <code>sql_identifier</code></p>
<p>Name of the role that granted the privilege</p></td>
</tr>
<tr>
<td><p role="column_definition">grantee <code>sql_identifier</code></p>
<p>Name of the role that the privilege was granted to</p></td>
</tr>
<tr>
<td><p role="column_definition">table_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the table (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">table_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the table</p></td>
</tr>
<tr>
<td><p role="column_definition">table_name <code>sql_identifier</code></p>
<p>Name of the table</p></td>
</tr>
<tr>
<td><p role="column_definition">privilege_type <code>character_data</code></p>
<p>Type of the privilege: <code>SELECT</code>, <code>INSERT</code>, <code>UPDATE</code>, <code>DELETE</code>, <code>TRUNCATE</code>, <code>REFERENCES</code>, or <code>TRIGGER</code></p></td>
</tr>
<tr>
<td><p role="column_definition">is_grantable <code>yes_or_no</code></p>
<p><code>YES</code> if the privilege is grantable, <code>NO</code> if not</p></td>
</tr>
<tr>
<td><p role="column_definition">with_hierarchy <code>yes_or_no</code></p>
<p>In the SQL standard, <code>WITH HIERARCHY OPTION</code> is a separate (sub-)privilege allowing certain operations on table inheritance hierarchies. In PostgreSQL, this is included in the <code>SELECT</code> privilege, so this column shows <code>YES</code> if the privilege is <code>SELECT</code>, else <code>NO</code>.</p></td>
</tr>
</tbody>
</table>

## `role_udt_grants`

The view `role_udt_grants` is intended to identify `USAGE` privileges granted on user-defined types where the grantor or grantee is a currently enabled role. Further information can be found under `udt_privileges`. The only effective difference between this view and `udt_privileges` is that this view omits objects that have been made accessible to the current user by way of a grant to `PUBLIC`. Since data types do not have real privileges in PostgreSQL, but only an implicit grant to `PUBLIC`, this view is empty.

<table>
<caption>role_udt_grants Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">grantor <code>sql_identifier</code></p>
<p>The name of the role that granted the privilege</p></td>
</tr>
<tr>
<td><p role="column_definition">grantee <code>sql_identifier</code></p>
<p>The name of the role that the privilege was granted to</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the type (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the type</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_name <code>sql_identifier</code></p>
<p>Name of the type</p></td>
</tr>
<tr>
<td><p role="column_definition">privilege_type <code>character_data</code></p>
<p>Always <code>TYPE USAGE</code></p></td>
</tr>
<tr>
<td><p role="column_definition">is_grantable <code>yes_or_no</code></p>
<p><code>YES</code> if the privilege is grantable, <code>NO</code> if not</p></td>
</tr>
</tbody>
</table>

## `role_usage_grants`

The view `role_usage_grants` identifies `USAGE` privileges granted on various kinds of objects where the grantor or grantee is a currently enabled role. Further information can be found under `usage_privileges`. The only effective difference between this view and `usage_privileges` is that this view omits objects that have been made accessible to the current user by way of a grant to `PUBLIC`.

<table>
<caption>role_usage_grants Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">grantor <code>sql_identifier</code></p>
<p>The name of the role that granted the privilege</p></td>
</tr>
<tr>
<td><p role="column_definition">grantee <code>sql_identifier</code></p>
<p>The name of the role that the privilege was granted to</p></td>
</tr>
<tr>
<td><p role="column_definition">object_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the object (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">object_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the object, if applicable, else an empty string</p></td>
</tr>
<tr>
<td><p role="column_definition">object_name <code>sql_identifier</code></p>
<p>Name of the object</p></td>
</tr>
<tr>
<td><p role="column_definition">object_type <code>character_data</code></p>
<p><code>COLLATION</code> or <code>DOMAIN</code> or <code>FOREIGN DATA WRAPPER</code> or <code>FOREIGN SERVER</code> or <code>SEQUENCE</code></p></td>
</tr>
<tr>
<td><p role="column_definition">privilege_type <code>character_data</code></p>
<p>Always <code>USAGE</code></p></td>
</tr>
<tr>
<td><p role="column_definition">is_grantable <code>yes_or_no</code></p>
<p><code>YES</code> if the privilege is grantable, <code>NO</code> if not</p></td>
</tr>
</tbody>
</table>

## `routine_column_usage`

The view `routine_column_usage` identifies all columns that are used by a function or procedure, either in the SQL body or in parameter default expressions. (This only works for unquoted SQL bodies, not quoted bodies or functions in other languages.) A column is only included if its table is owned by a currently enabled role.

<table>
<caption><code>routine_column_usage</code> Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">specific_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the function (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the function</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_name <code>sql_identifier</code></p>
<p>The “specific name” of the function. See <a href="#infoschema-routines"></a> for more information.</p></td>
</tr>
<tr>
<td><p role="column_definition">routine_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the function (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">routine_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the function</p></td>
</tr>
<tr>
<td><p role="column_definition">routine_name <code>sql_identifier</code></p>
<p>Name of the function (might be duplicated in case of overloading)</p></td>
</tr>
<tr>
<td><p role="column_definition">table_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the table that is used by the function (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">table_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the table that is used by the function</p></td>
</tr>
<tr>
<td><p role="column_definition">table_name <code>sql_identifier</code></p>
<p>Name of the table that is used by the function</p></td>
</tr>
<tr>
<td><p role="column_definition">column_name <code>sql_identifier</code></p>
<p>Name of the column that is used by the function</p></td>
</tr>
</tbody>
</table>

## `routine_privileges`

The view `routine_privileges` identifies all privileges granted on functions to a currently enabled role or by a currently enabled role. There is one row for each combination of function, grantor, and grantee.

<table>
<caption>routine_privileges Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">grantor <code>sql_identifier</code></p>
<p>Name of the role that granted the privilege</p></td>
</tr>
<tr>
<td><p role="column_definition">grantee <code>sql_identifier</code></p>
<p>Name of the role that the privilege was granted to</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the function (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the function</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_name <code>sql_identifier</code></p>
<p>The “specific name” of the function. See <a href="#infoschema-routines"></a> for more information.</p></td>
</tr>
<tr>
<td><p role="column_definition">routine_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the function (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">routine_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the function</p></td>
</tr>
<tr>
<td><p role="column_definition">routine_name <code>sql_identifier</code></p>
<p>Name of the function (might be duplicated in case of overloading)</p></td>
</tr>
<tr>
<td><p role="column_definition">privilege_type <code>character_data</code></p>
<p>Always <code>EXECUTE</code> (the only privilege type for functions)</p></td>
</tr>
<tr>
<td><p role="column_definition">is_grantable <code>yes_or_no</code></p>
<p><code>YES</code> if the privilege is grantable, <code>NO</code> if not</p></td>
</tr>
</tbody>
</table>

## `routine_routine_usage`

The view `routine_routine_usage` identifies all functions or procedures that are used by another (or the same) function or procedure, either in the SQL body or in parameter default expressions. (This only works for unquoted SQL bodies, not quoted bodies or functions in other languages.) An entry is included here only if the used function is owned by a currently enabled role. (There is no such restriction on the using function.)

Note that the entries for both functions in the view refer to the “specific” name of the routine, even though the column names are used in a way that is inconsistent with other information schema views about routines. This is per SQL standard, although it is arguably a misdesign. See [](#infoschema-routines) for more information about specific names.

<table>
<caption><code>routine_routine_usage</code> Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">specific_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the using function (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the using function</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_name <code>sql_identifier</code></p>
<p>The “specific name” of the using function.</p></td>
</tr>
<tr>
<td><p role="column_definition">routine_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the function that is used by the first function (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">routine_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the function that is used by the first function</p></td>
</tr>
<tr>
<td><p role="column_definition">routine_name <code>sql_identifier</code></p>
<p>The “specific name” of the function that is used by the first function.</p></td>
</tr>
</tbody>
</table>

## `routine_sequence_usage`

The view `routine_sequence_usage` identifies all sequences that are used by a function or procedure, either in the SQL body or in parameter default expressions. (This only works for unquoted SQL bodies, not quoted bodies or functions in other languages.) A sequence is only included if that sequence is owned by a currently enabled role.

<table>
<caption><code>routine_sequence_usage</code> Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">specific_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the function (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the function</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_name <code>sql_identifier</code></p>
<p>The “specific name” of the function. See <a href="#infoschema-routines"></a> for more information.</p></td>
</tr>
<tr>
<td><p role="column_definition">routine_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the function (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">routine_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the function</p></td>
</tr>
<tr>
<td><p role="column_definition">routine_name <code>sql_identifier</code></p>
<p>Name of the function (might be duplicated in case of overloading)</p></td>
</tr>
<tr>
<td><p role="column_definition">schema_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the sequence that is used by the function (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">sequence_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the sequence that is used by the function</p></td>
</tr>
<tr>
<td><p role="column_definition">sequence_name <code>sql_identifier</code></p>
<p>Name of the sequence that is used by the function</p></td>
</tr>
</tbody>
</table>

## `routine_table_usage`

The view `routine_table_usage` is meant to identify all tables that are used by a function or procedure. This information is currently not tracked by PostgreSQL.

<table>
<caption><code>routine_table_usage</code> Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">specific_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the function (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the function</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_name <code>sql_identifier</code></p>
<p>The “specific name” of the function. See <a href="#infoschema-routines"></a> for more information.</p></td>
</tr>
<tr>
<td><p role="column_definition">routine_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the function (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">routine_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the function</p></td>
</tr>
<tr>
<td><p role="column_definition">routine_name <code>sql_identifier</code></p>
<p>Name of the function (might be duplicated in case of overloading)</p></td>
</tr>
<tr>
<td><p role="column_definition">table_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the table that is used by the function (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">table_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the table that is used by the function</p></td>
</tr>
<tr>
<td><p role="column_definition">table_name <code>sql_identifier</code></p>
<p>Name of the table that is used by the function</p></td>
</tr>
</tbody>
</table>

## `routines`

The view `routines` contains all functions and procedures in the current database. Only those functions and procedures are shown that the current user has access to (by way of being the owner or having some privilege).

<table>
<caption>routines Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">specific_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the function (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the function</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_name <code>sql_identifier</code></p>
<p>The “specific name” of the function. This is a name that uniquely identifies the function in the schema, even if the real name of the function is overloaded. The format of the specific name is not defined, it should only be used to compare it to other instances of specific routine names.</p></td>
</tr>
<tr>
<td><p role="column_definition">routine_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the function (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">routine_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the function</p></td>
</tr>
<tr>
<td><p role="column_definition">routine_name <code>sql_identifier</code></p>
<p>Name of the function (might be duplicated in case of overloading)</p></td>
</tr>
<tr>
<td><p role="column_definition">routine_type <code>character_data</code></p>
<p><code>FUNCTION</code> for a function, <code>PROCEDURE</code> for a procedure</p></td>
</tr>
<tr>
<td><p role="column_definition">module_catalog <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">module_schema <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">module_name <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_catalog <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_schema <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_name <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">data_type <code>character_data</code></p>
<p>Return data type of the function, if it is a built-in type, or <code>ARRAY</code> if it is some array (in that case, see the view <code>element_types</code>), else <code>USER-DEFINED</code> (in that case, the type is identified in <code>type_udt_name</code> and associated columns). Null for a procedure.</p></td>
</tr>
<tr>
<td><p role="column_definition">character_maximum_length <code>cardinal_number</code></p>
<p>Always null, since this information is not applied to return data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">character_octet_length <code>cardinal_number</code></p>
<p>Always null, since this information is not applied to return data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_catalog <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_schema <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_name <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_catalog <code>sql_identifier</code></p>
<p>Always null, since this information is not applied to return data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_schema <code>sql_identifier</code></p>
<p>Always null, since this information is not applied to return data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_name <code>sql_identifier</code></p>
<p>Always null, since this information is not applied to return data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">numeric_precision <code>cardinal_number</code></p>
<p>Always null, since this information is not applied to return data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">numeric_precision_radix <code>cardinal_number</code></p>
<p>Always null, since this information is not applied to return data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">numeric_scale <code>cardinal_number</code></p>
<p>Always null, since this information is not applied to return data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">datetime_precision <code>cardinal_number</code></p>
<p>Always null, since this information is not applied to return data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">interval_type <code>character_data</code></p>
<p>Always null, since this information is not applied to return data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">interval_precision <code>cardinal_number</code></p>
<p>Always null, since this information is not applied to return data types in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">type_udt_catalog <code>sql_identifier</code></p>
<p>Name of the database that the return data type of the function is defined in (always the current database). Null for a procedure.</p></td>
</tr>
<tr>
<td><p role="column_definition">type_udt_schema <code>sql_identifier</code></p>
<p>Name of the schema that the return data type of the function is defined in. Null for a procedure.</p></td>
</tr>
<tr>
<td><p role="column_definition">type_udt_name <code>sql_identifier</code></p>
<p>Name of the return data type of the function. Null for a procedure.</p></td>
</tr>
<tr>
<td><p role="column_definition">scope_catalog <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">scope_schema <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">scope_name <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">maximum_cardinality <code>cardinal_number</code></p>
<p>Always null, because arrays always have unlimited maximum cardinality in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">dtd_identifier <code>sql_identifier</code></p>
<p>An identifier of the data type descriptor of the return data type of this function, unique among the data type descriptors pertaining to the function. This is mainly useful for joining with other instances of such identifiers. (The specific format of the identifier is not defined and not guaranteed to remain the same in future versions.)</p></td>
</tr>
<tr>
<td><p role="column_definition">routine_body <code>character_data</code></p>
<p>If the function is an SQL function, then <code>SQL</code>, else <code>EXTERNAL</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">routine_definition <code>character_data</code></p>
<p>The source text of the function (null if the function is not owned by a currently enabled role). (According to the SQL standard, this column is only applicable if <code>routine_body</code> is <code>SQL</code>, but in PostgreSQL it will contain whatever source text was specified when the function was created.)</p></td>
</tr>
<tr>
<td><p role="column_definition">external_name <code>character_data</code></p>
<p>If this function is a C function, then the external name (link symbol) of the function; else null. (This works out to be the same value that is shown in <code>routine_definition</code>.)</p></td>
</tr>
<tr>
<td><p role="column_definition">external_language <code>character_data</code></p>
<p>The language the function is written in</p></td>
</tr>
<tr>
<td><p role="column_definition">parameter_style <code>character_data</code></p>
<p>Always <code>GENERAL</code> (The SQL standard defines other parameter styles, which are not available in PostgreSQL.)</p></td>
</tr>
<tr>
<td><p role="column_definition">is_deterministic <code>yes_or_no</code></p>
<p>If the function is declared immutable (called deterministic in the SQL standard), then <code>YES</code>, else <code>NO</code>. (You cannot query the other volatility levels available in PostgreSQL through the information schema.)</p></td>
</tr>
<tr>
<td><p role="column_definition">sql_data_access <code>character_data</code></p>
<p>Always <code>MODIFIES</code>, meaning that the function possibly modifies SQL data. This information is not useful for PostgreSQL.</p></td>
</tr>
<tr>
<td><p role="column_definition">is_null_call <code>yes_or_no</code></p>
<p>If the function automatically returns null if any of its arguments are null, then <code>YES</code>, else <code>NO</code>. Null for a procedure.</p></td>
</tr>
<tr>
<td><p role="column_definition">sql_path <code>character_data</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">schema_level_routine <code>yes_or_no</code></p>
<p>Always <code>YES</code> (The opposite would be a method of a user-defined type, which is a feature not available in PostgreSQL.)</p></td>
</tr>
<tr>
<td><p role="column_definition">max_dynamic_result_sets <code>cardinal_number</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">is_user_defined_cast <code>yes_or_no</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">is_implicitly_invocable <code>yes_or_no</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">security_type <code>character_data</code></p>
<p>If the function runs with the privileges of the current user, then <code>INVOKER</code>, if the function runs with the privileges of the user who defined it, then <code>DEFINER</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">to_sql_specific_catalog <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">to_sql_specific_schema <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">to_sql_specific_name <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">as_locator <code>yes_or_no</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">created <code>time_stamp</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">last_altered <code>time_stamp</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">new_savepoint_level <code>yes_or_no</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">is_udt_dependent <code>yes_or_no</code></p>
<p>Currently always <code>NO</code>. The alternative <code>YES</code> applies to a feature not available in PostgreSQL.</p></td>
</tr>
<tr>
<td><p role="column_definition">result_cast_from_data_type <code>character_data</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">result_cast_as_locator <code>yes_or_no</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">result_cast_char_max_length <code>cardinal_number</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">result_cast_char_octet_length <code>cardinal_number</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">result_cast_char_set_catalog <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">result_cast_char_set_schema <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">result_cast_char_set_name <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">result_cast_collation_catalog <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">result_cast_collation_schema <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">result_cast_collation_name <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">result_cast_numeric_precision <code>cardinal_number</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">result_cast_numeric_precision_radix <code>cardinal_number</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">result_cast_numeric_scale <code>cardinal_number</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">result_cast_datetime_precision <code>cardinal_number</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">result_cast_interval_type <code>character_data</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">result_cast_interval_precision <code>cardinal_number</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">result_cast_type_udt_catalog <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">result_cast_type_udt_schema <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">result_cast_type_udt_name <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">result_cast_scope_catalog <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">result_cast_scope_schema <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">result_cast_scope_name <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">result_cast_maximum_cardinality <code>cardinal_number</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">result_cast_dtd_identifier <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
</tbody>
</table>

## `schemata`

The view `schemata` contains all schemas in the current database that the current user has access to (by way of being the owner or having some privilege).

<table>
<caption>schemata Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">catalog_name <code>sql_identifier</code></p>
<p>Name of the database that the schema is contained in (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">schema_name <code>sql_identifier</code></p>
<p>Name of the schema</p></td>
</tr>
<tr>
<td><p role="column_definition">schema_owner <code>sql_identifier</code></p>
<p>Name of the owner of the schema</p></td>
</tr>
<tr>
<td><p role="column_definition">default_character_set_catalog <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">default_character_set_schema <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">default_character_set_name <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">sql_path <code>character_data</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
</tbody>
</table>

## `sequences`

The view `sequences` contains all sequences defined in the current database. Only those sequences are shown that the current user has access to (by way of being the owner or having some privilege).

<table>
<caption>sequences Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">sequence_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the sequence (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">sequence_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the sequence</p></td>
</tr>
<tr>
<td><p role="column_definition">sequence_name <code>sql_identifier</code></p>
<p>Name of the sequence</p></td>
</tr>
<tr>
<td><p role="column_definition">data_type <code>character_data</code></p>
<p>The data type of the sequence.</p></td>
</tr>
<tr>
<td><p role="column_definition">numeric_precision <code>cardinal_number</code></p>
<p>This column contains the (declared or implicit) precision of the sequence data type (see above). The precision indicates the number of significant digits. It can be expressed in decimal (base 10) or binary (base 2) terms, as specified in the column <code>numeric_precision_radix</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">numeric_precision_radix <code>cardinal_number</code></p>
<p>This column indicates in which base the values in the columns <code>numeric_precision</code> and <code>numeric_scale</code> are expressed. The value is either 2 or 10.</p></td>
</tr>
<tr>
<td><p role="column_definition">numeric_scale <code>cardinal_number</code></p>
<p>This column contains the (declared or implicit) scale of the sequence data type (see above). The scale indicates the number of significant digits to the right of the decimal point. It can be expressed in decimal (base 10) or binary (base 2) terms, as specified in the column <code>numeric_precision_radix</code>.</p></td>
</tr>
<tr>
<td><p role="column_definition">start_value <code>character_data</code></p>
<p>The start value of the sequence</p></td>
</tr>
<tr>
<td><p role="column_definition">minimum_value <code>character_data</code></p>
<p>The minimum value of the sequence</p></td>
</tr>
<tr>
<td><p role="column_definition">maximum_value <code>character_data</code></p>
<p>The maximum value of the sequence</p></td>
</tr>
<tr>
<td><p role="column_definition">increment <code>character_data</code></p>
<p>The increment of the sequence</p></td>
</tr>
<tr>
<td><p role="column_definition">cycle_option <code>yes_or_no</code></p>
<p><code>YES</code> if the sequence cycles, else <code>NO</code></p></td>
</tr>
</tbody>
</table>

Note that in accordance with the SQL standard, the start, minimum, maximum, and increment values are returned as character strings.

## `sql_features`

The table `sql_features` contains information about which formal features defined in the SQL standard are supported by PostgreSQL. This is the same information that is presented in [???](#features). There you can also find some additional background information.

<table>
<caption>sql_features Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">feature_id <code>character_data</code></p>
<p>Identifier string of the feature</p></td>
</tr>
<tr>
<td><p role="column_definition">feature_name <code>character_data</code></p>
<p>Descriptive name of the feature</p></td>
</tr>
<tr>
<td><p role="column_definition">sub_feature_id <code>character_data</code></p>
<p>Identifier string of the subfeature, or a zero-length string if not a subfeature</p></td>
</tr>
<tr>
<td><p role="column_definition">sub_feature_name <code>character_data</code></p>
<p>Descriptive name of the subfeature, or a zero-length string if not a subfeature</p></td>
</tr>
<tr>
<td><p role="column_definition">is_supported <code>yes_or_no</code></p>
<p><code>YES</code> if the feature is fully supported by the current version of PostgreSQL, <code>NO</code> if not</p></td>
</tr>
<tr>
<td><p role="column_definition">is_verified_by <code>character_data</code></p>
<p>Always null, since the PostgreSQL development group does not perform formal testing of feature conformance</p></td>
</tr>
<tr>
<td><p role="column_definition">comments <code>character_data</code></p>
<p>Possibly a comment about the supported status of the feature</p></td>
</tr>
</tbody>
</table>

## `sql_implementation_info`

The table `sql_implementation_info` contains information about various aspects that are left implementation-defined by the SQL standard. This information is primarily intended for use in the context of the ODBC interface; users of other interfaces will probably find this information to be of little use. For this reason, the individual implementation information items are not described here; you will find them in the description of the ODBC interface.

<table>
<caption>sql_implementation_info Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">implementation_info_id <code>character_data</code></p>
<p>Identifier string of the implementation information item</p></td>
</tr>
<tr>
<td><p role="column_definition">implementation_info_name <code>character_data</code></p>
<p>Descriptive name of the implementation information item</p></td>
</tr>
<tr>
<td><p role="column_definition">integer_value <code>cardinal_number</code></p>
<p>Value of the implementation information item, or null if the value is contained in the column <code>character_value</code></p></td>
</tr>
<tr>
<td><p role="column_definition">character_value <code>character_data</code></p>
<p>Value of the implementation information item, or null if the value is contained in the column <code>integer_value</code></p></td>
</tr>
<tr>
<td><p role="column_definition">comments <code>character_data</code></p>
<p>Possibly a comment pertaining to the implementation information item</p></td>
</tr>
</tbody>
</table>

## `sql_parts`

The table `sql_parts` contains information about which of the several parts of the SQL standard are supported by PostgreSQL.

<table>
<caption>sql_parts Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">feature_id <code>character_data</code></p>
<p>An identifier string containing the number of the part</p></td>
</tr>
<tr>
<td><p role="column_definition">feature_name <code>character_data</code></p>
<p>Descriptive name of the part</p></td>
</tr>
<tr>
<td><p role="column_definition">is_supported <code>yes_or_no</code></p>
<p><code>YES</code> if the part is fully supported by the current version of PostgreSQL, <code>NO</code> if not</p></td>
</tr>
<tr>
<td><p role="column_definition">is_verified_by <code>character_data</code></p>
<p>Always null, since the PostgreSQL development group does not perform formal testing of feature conformance</p></td>
</tr>
<tr>
<td><p role="column_definition">comments <code>character_data</code></p>
<p>Possibly a comment about the supported status of the part</p></td>
</tr>
</tbody>
</table>

## `sql_sizing`

The table `sql_sizing` contains information about various size limits and maximum values in PostgreSQL. This information is primarily intended for use in the context of the ODBC interface; users of other interfaces will probably find this information to be of little use. For this reason, the individual sizing items are not described here; you will find them in the description of the ODBC interface.

<table>
<caption>sql_sizing Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">sizing_id <code>cardinal_number</code></p>
<p>Identifier of the sizing item</p></td>
</tr>
<tr>
<td><p role="column_definition">sizing_name <code>character_data</code></p>
<p>Descriptive name of the sizing item</p></td>
</tr>
<tr>
<td><p role="column_definition">supported_value <code>cardinal_number</code></p>
<p>Value of the sizing item, or 0 if the size is unlimited or cannot be determined, or null if the features for which the sizing item is applicable are not supported</p></td>
</tr>
<tr>
<td><p role="column_definition">comments <code>character_data</code></p>
<p>Possibly a comment pertaining to the sizing item</p></td>
</tr>
</tbody>
</table>

## `table_constraints`

The view `table_constraints` contains all constraints belonging to tables that the current user owns or has some privilege other than `SELECT` on.

<table>
<caption>table_constraints Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">constraint_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the constraint (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">constraint_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">constraint_name <code>sql_identifier</code></p>
<p>Name of the constraint</p></td>
</tr>
<tr>
<td><p role="column_definition">table_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the table (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">table_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the table</p></td>
</tr>
<tr>
<td><p role="column_definition">table_name <code>sql_identifier</code></p>
<p>Name of the table</p></td>
</tr>
<tr>
<td><p role="column_definition">constraint_type <code>character_data</code></p>
<p>Type of the constraint: <code>CHECK</code> (includes not-null constraints), <code>FOREIGN KEY</code>, <code>PRIMARY KEY</code>, or <code>UNIQUE</code></p></td>
</tr>
<tr>
<td><p role="column_definition">is_deferrable <code>yes_or_no</code></p>
<p><code>YES</code> if the constraint is deferrable, <code>NO</code> if not</p></td>
</tr>
<tr>
<td><p role="column_definition">initially_deferred <code>yes_or_no</code></p>
<p><code>YES</code> if the constraint is deferrable and initially deferred, <code>NO</code> if not</p></td>
</tr>
<tr>
<td><p role="column_definition">enforced <code>yes_or_no</code></p>
<p>Applies to a feature not available in PostgreSQL (currently always <code>YES</code>)</p></td>
</tr>
<tr>
<td><p role="column_definition">nulls_distinct <code>yes_or_no</code></p>
<p>If the constraint is a unique constraint, then <code>YES</code> if the constraint treats nulls as distinct or <code>NO</code> if it treats nulls as not distinct, otherwise null for other types of constraints.</p></td>
</tr>
</tbody>
</table>

## `table_privileges`

The view `table_privileges` identifies all privileges granted on tables or views to a currently enabled role or by a currently enabled role. There is one row for each combination of table, grantor, and grantee.

<table>
<caption>table_privileges Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">grantor <code>sql_identifier</code></p>
<p>Name of the role that granted the privilege</p></td>
</tr>
<tr>
<td><p role="column_definition">grantee <code>sql_identifier</code></p>
<p>Name of the role that the privilege was granted to</p></td>
</tr>
<tr>
<td><p role="column_definition">table_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the table (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">table_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the table</p></td>
</tr>
<tr>
<td><p role="column_definition">table_name <code>sql_identifier</code></p>
<p>Name of the table</p></td>
</tr>
<tr>
<td><p role="column_definition">privilege_type <code>character_data</code></p>
<p>Type of the privilege: <code>SELECT</code>, <code>INSERT</code>, <code>UPDATE</code>, <code>DELETE</code>, <code>TRUNCATE</code>, <code>REFERENCES</code>, or <code>TRIGGER</code></p></td>
</tr>
<tr>
<td><p role="column_definition">is_grantable <code>yes_or_no</code></p>
<p><code>YES</code> if the privilege is grantable, <code>NO</code> if not</p></td>
</tr>
<tr>
<td><p role="column_definition">with_hierarchy <code>yes_or_no</code></p>
<p>In the SQL standard, <code>WITH HIERARCHY OPTION</code> is a separate (sub-)privilege allowing certain operations on table inheritance hierarchies. In PostgreSQL, this is included in the <code>SELECT</code> privilege, so this column shows <code>YES</code> if the privilege is <code>SELECT</code>, else <code>NO</code>.</p></td>
</tr>
</tbody>
</table>

## `tables`

The view `tables` contains all tables and views defined in the current database. Only those tables and views are shown that the current user has access to (by way of being the owner or having some privilege).

<table>
<caption>tables Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">table_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the table (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">table_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the table</p></td>
</tr>
<tr>
<td><p role="column_definition">table_name <code>sql_identifier</code></p>
<p>Name of the table</p></td>
</tr>
<tr>
<td><p role="column_definition">table_type <code>character_data</code></p>
<p>Type of the table: <code>BASE TABLE</code> for a persistent base table (the normal table type), <code>VIEW</code> for a view, <code>FOREIGN</code> for a foreign table, or <code>LOCAL TEMPORARY</code> for a temporary table</p></td>
</tr>
<tr>
<td><p role="column_definition">self_referencing_column_name <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">reference_generation <code>character_data</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">user_defined_type_catalog <code>sql_identifier</code></p>
<p>If the table is a typed table, the name of the database that contains the underlying data type (always the current database), else null.</p></td>
</tr>
<tr>
<td><p role="column_definition">user_defined_type_schema <code>sql_identifier</code></p>
<p>If the table is a typed table, the name of the schema that contains the underlying data type, else null.</p></td>
</tr>
<tr>
<td><p role="column_definition">user_defined_type_name <code>sql_identifier</code></p>
<p>If the table is a typed table, the name of the underlying data type, else null.</p></td>
</tr>
<tr>
<td><p role="column_definition">is_insertable_into <code>yes_or_no</code></p>
<p><code>YES</code> if the table is insertable into, <code>NO</code> if not (Base tables are always insertable into, views not necessarily.)</p></td>
</tr>
<tr>
<td><p role="column_definition">is_typed <code>yes_or_no</code></p>
<p><code>YES</code> if the table is a typed table, <code>NO</code> if not</p></td>
</tr>
<tr>
<td><p role="column_definition">commit_action <code>character_data</code></p>
<p>Not yet implemented</p></td>
</tr>
</tbody>
</table>

## `transforms`

The view `transforms` contains information about the transforms defined in the current database. More precisely, it contains a row for each function contained in a transform (the “from SQL” or “to SQL” function).

<table>
<caption>transforms Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">udt_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the type the transform is for (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the type the transform is for</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_name <code>sql_identifier</code></p>
<p>Name of the type the transform is for</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the function (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the function</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_name <code>sql_identifier</code></p>
<p>The “specific name” of the function. See <a href="#infoschema-routines"></a> for more information.</p></td>
</tr>
<tr>
<td><p role="column_definition">group_name <code>sql_identifier</code></p>
<p>The SQL standard allows defining transforms in “groups”, and selecting a group at run time. PostgreSQL does not support this. Instead, transforms are specific to a language. As a compromise, this field contains the language the transform is for.</p></td>
</tr>
<tr>
<td><p role="column_definition">transform_type <code>character_data</code></p>
<p><code>FROM SQL</code> or <code>TO SQL</code></p></td>
</tr>
</tbody>
</table>

## `triggered_update_columns`

For triggers in the current database that specify a column list (like `UPDATE OF column1, column2`), the view `triggered_update_columns` identifies these columns. Triggers that do not specify a column list are not included in this view. Only those columns are shown that the current user owns or has some privilege other than `SELECT` on.

<table>
<caption>triggered_update_columns Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">trigger_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the trigger (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">trigger_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the trigger</p></td>
</tr>
<tr>
<td><p role="column_definition">trigger_name <code>sql_identifier</code></p>
<p>Name of the trigger</p></td>
</tr>
<tr>
<td><p role="column_definition">event_object_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the table that the trigger is defined on (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">event_object_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the table that the trigger is defined on</p></td>
</tr>
<tr>
<td><p role="column_definition">event_object_table <code>sql_identifier</code></p>
<p>Name of the table that the trigger is defined on</p></td>
</tr>
<tr>
<td><p role="column_definition">event_object_column <code>sql_identifier</code></p>
<p>Name of the column that the trigger is defined on</p></td>
</tr>
</tbody>
</table>

## `triggers`

The view `triggers` contains all triggers defined in the current database on tables and views that the current user owns or has some privilege other than `SELECT` on.

<table>
<caption>triggers Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">trigger_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the trigger (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">trigger_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the trigger</p></td>
</tr>
<tr>
<td><p role="column_definition">trigger_name <code>sql_identifier</code></p>
<p>Name of the trigger</p></td>
</tr>
<tr>
<td><p role="column_definition">event_manipulation <code>character_data</code></p>
<p>Event that fires the trigger (<code>INSERT</code>, <code>UPDATE</code>, or <code>DELETE</code>)</p></td>
</tr>
<tr>
<td><p role="column_definition">event_object_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the table that the trigger is defined on (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">event_object_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the table that the trigger is defined on</p></td>
</tr>
<tr>
<td><p role="column_definition">event_object_table <code>sql_identifier</code></p>
<p>Name of the table that the trigger is defined on</p></td>
</tr>
<tr>
<td><p role="column_definition">action_order <code>cardinal_number</code></p>
<p>Firing order among triggers on the same table having the same <code>event_manipulation</code>, <code>action_timing</code>, and <code>action_orientation</code>. In PostgreSQL, triggers are fired in name order, so this column reflects that.</p></td>
</tr>
<tr>
<td><p role="column_definition">action_condition <code>character_data</code></p>
<p><code>WHEN</code> condition of the trigger, null if none (also null if the table is not owned by a currently enabled role)</p></td>
</tr>
<tr>
<td><p role="column_definition">action_statement <code>character_data</code></p>
<p>Statement that is executed by the trigger (currently always <code>EXECUTE FUNCTION function(...)</code>)</p></td>
</tr>
<tr>
<td><p role="column_definition">action_orientation <code>character_data</code></p>
<p>Identifies whether the trigger fires once for each processed row or once for each statement (<code>ROW</code> or <code>STATEMENT</code>)</p></td>
</tr>
<tr>
<td><p role="column_definition">action_timing <code>character_data</code></p>
<p>Time at which the trigger fires (<code>BEFORE</code>, <code>AFTER</code>, or <code>INSTEAD OF</code>)</p></td>
</tr>
<tr>
<td><p role="column_definition">action_reference_old_table <code>sql_identifier</code></p>
<p>Name of the “old” transition table, or null if none</p></td>
</tr>
<tr>
<td><p role="column_definition">action_reference_new_table <code>sql_identifier</code></p>
<p>Name of the “new” transition table, or null if none</p></td>
</tr>
<tr>
<td><p role="column_definition">action_reference_old_row <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">action_reference_new_row <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">created <code>time_stamp</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
</tbody>
</table>

Triggers in PostgreSQL have two incompatibilities with the SQL standard that affect the representation in the information schema. First, trigger names are local to each table in PostgreSQL, rather than being independent schema objects. Therefore there can be duplicate trigger names defined in one schema, so long as they belong to different tables. (`trigger_catalog` and `trigger_schema` are really the values pertaining to the table that the trigger is defined on.) Second, triggers can be defined to fire on multiple events in PostgreSQL (e.g., `ON INSERT OR UPDATE`), whereas the SQL standard only allows one. If a trigger is defined to fire on multiple events, it is represented as multiple rows in the information schema, one for each type of event. As a consequence of these two issues, the primary key of the view `triggers` is really `(trigger_catalog, trigger_schema, event_object_table, trigger_name, event_manipulation)` instead of `(trigger_catalog, trigger_schema, trigger_name)`, which is what the SQL standard specifies. Nonetheless, if you define your triggers in a manner that conforms with the SQL standard (trigger names unique in the schema and only one event type per trigger), this will not affect you.

> [!NOTE]
> Prior to PostgreSQL 9.1, this view's columns action_timing, action_reference_old_table, action_reference_new_table, action_reference_old_row, and action_reference_new_row were named condition_timing, condition_reference_old_table, condition_reference_new_table, condition_reference_old_row, and condition_reference_new_row respectively. That was how they were named in the SQL:1999 standard. The new naming conforms to SQL:2003 and later.

## `udt_privileges`

The view `udt_privileges` identifies `USAGE` privileges granted on user-defined types to a currently enabled role or by a currently enabled role. There is one row for each combination of type, grantor, and grantee. This view shows only composite types (see under [](#infoschema-user-defined-types) for why); see [](#infoschema-usage-privileges) for domain privileges.

<table>
<caption>udt_privileges Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">grantor <code>sql_identifier</code></p>
<p>Name of the role that granted the privilege</p></td>
</tr>
<tr>
<td><p role="column_definition">grantee <code>sql_identifier</code></p>
<p>Name of the role that the privilege was granted to</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the type (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the type</p></td>
</tr>
<tr>
<td><p role="column_definition">udt_name <code>sql_identifier</code></p>
<p>Name of the type</p></td>
</tr>
<tr>
<td><p role="column_definition">privilege_type <code>character_data</code></p>
<p>Always <code>TYPE USAGE</code></p></td>
</tr>
<tr>
<td><p role="column_definition">is_grantable <code>yes_or_no</code></p>
<p><code>YES</code> if the privilege is grantable, <code>NO</code> if not</p></td>
</tr>
</tbody>
</table>

## `usage_privileges`

The view `usage_privileges` identifies `USAGE` privileges granted on various kinds of objects to a currently enabled role or by a currently enabled role. In PostgreSQL, this currently applies to collations, domains, foreign-data wrappers, foreign servers, and sequences. There is one row for each combination of object, grantor, and grantee.

Since collations do not have real privileges in PostgreSQL, this view shows implicit non-grantable `USAGE` privileges granted by the owner to `PUBLIC` for all collations. The other object types, however, show real privileges.

In PostgreSQL, sequences also support `SELECT` and `UPDATE` privileges in addition to the `USAGE` privilege. These are nonstandard and therefore not visible in the information schema.

<table>
<caption>usage_privileges Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">grantor <code>sql_identifier</code></p>
<p>Name of the role that granted the privilege</p></td>
</tr>
<tr>
<td><p role="column_definition">grantee <code>sql_identifier</code></p>
<p>Name of the role that the privilege was granted to</p></td>
</tr>
<tr>
<td><p role="column_definition">object_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the object (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">object_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the object, if applicable, else an empty string</p></td>
</tr>
<tr>
<td><p role="column_definition">object_name <code>sql_identifier</code></p>
<p>Name of the object</p></td>
</tr>
<tr>
<td><p role="column_definition">object_type <code>character_data</code></p>
<p><code>COLLATION</code> or <code>DOMAIN</code> or <code>FOREIGN DATA WRAPPER</code> or <code>FOREIGN SERVER</code> or <code>SEQUENCE</code></p></td>
</tr>
<tr>
<td><p role="column_definition">privilege_type <code>character_data</code></p>
<p>Always <code>USAGE</code></p></td>
</tr>
<tr>
<td><p role="column_definition">is_grantable <code>yes_or_no</code></p>
<p><code>YES</code> if the privilege is grantable, <code>NO</code> if not</p></td>
</tr>
</tbody>
</table>

## `user_defined_types`

The view `user_defined_types` currently contains all composite types defined in the current database. Only those types are shown that the current user has access to (by way of being the owner or having some privilege).

SQL knows about two kinds of user-defined types: structured types (also known as composite types in PostgreSQL) and distinct types (not implemented in PostgreSQL). To be future-proof, use the column `user_defined_type_category` to differentiate between these. Other user-defined types such as base types and enums, which are PostgreSQL extensions, are not shown here. For domains, see [](#infoschema-domains) instead.

<table>
<caption>user_defined_types Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">user_defined_type_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the type (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">user_defined_type_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the type</p></td>
</tr>
<tr>
<td><p role="column_definition">user_defined_type_name <code>sql_identifier</code></p>
<p>Name of the type</p></td>
</tr>
<tr>
<td><p role="column_definition">user_defined_type_category <code>character_data</code></p>
<p>Currently always <code>STRUCTURED</code></p></td>
</tr>
<tr>
<td><p role="column_definition">is_instantiable <code>yes_or_no</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">is_final <code>yes_or_no</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">ordering_form <code>character_data</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">ordering_category <code>character_data</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">ordering_routine_catalog <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">ordering_routine_schema <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">ordering_routine_name <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">reference_type <code>character_data</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">data_type <code>character_data</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">character_maximum_length <code>cardinal_number</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">character_octet_length <code>cardinal_number</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_catalog <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_schema <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">character_set_name <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_catalog <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_schema <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">collation_name <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">numeric_precision <code>cardinal_number</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">numeric_precision_radix <code>cardinal_number</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">numeric_scale <code>cardinal_number</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">datetime_precision <code>cardinal_number</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">interval_type <code>character_data</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">interval_precision <code>cardinal_number</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">source_dtd_identifier <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
<tr>
<td><p role="column_definition">ref_dtd_identifier <code>sql_identifier</code></p>
<p>Applies to a feature not available in PostgreSQL</p></td>
</tr>
</tbody>
</table>

## `user_mapping_options`

The view `user_mapping_options` contains all the options defined for user mappings in the current database. Only those user mappings are shown where the current user has access to the corresponding foreign server (by way of being the owner or having some privilege).

<table>
<caption>user_mapping_options Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">authorization_identifier <code>sql_identifier</code></p>
<p>Name of the user being mapped, or <code>PUBLIC</code> if the mapping is public</p></td>
</tr>
<tr>
<td><p role="column_definition">foreign_server_catalog <code>sql_identifier</code></p>
<p>Name of the database that the foreign server used by this mapping is defined in (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">foreign_server_name <code>sql_identifier</code></p>
<p>Name of the foreign server used by this mapping</p></td>
</tr>
<tr>
<td><p role="column_definition">option_name <code>sql_identifier</code></p>
<p>Name of an option</p></td>
</tr>
<tr>
<td><p role="column_definition">option_value <code>character_data</code></p>
<p>Value of the option. This column will show as null unless the current user is the user being mapped, or the mapping is for <code>PUBLIC</code> and the current user is the server owner, or the current user is a superuser. The intent is to protect password information stored as user mapping option.</p></td>
</tr>
</tbody>
</table>

## `user_mappings`

The view `user_mappings` contains all user mappings defined in the current database. Only those user mappings are shown where the current user has access to the corresponding foreign server (by way of being the owner or having some privilege).

<table>
<caption>user_mappings Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">authorization_identifier <code>sql_identifier</code></p>
<p>Name of the user being mapped, or <code>PUBLIC</code> if the mapping is public</p></td>
</tr>
<tr>
<td><p role="column_definition">foreign_server_catalog <code>sql_identifier</code></p>
<p>Name of the database that the foreign server used by this mapping is defined in (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">foreign_server_name <code>sql_identifier</code></p>
<p>Name of the foreign server used by this mapping</p></td>
</tr>
</tbody>
</table>

## `view_column_usage`

The view `view_column_usage` identifies all columns that are used in the query expression of a view (the `SELECT` statement that defines the view). A column is only included if the table that contains the column is owned by a currently enabled role.

> [!NOTE]
> Columns of system tables are not included. This should be fixed sometime.

<table>
<caption>view_column_usage Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">view_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the view (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">view_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the view</p></td>
</tr>
<tr>
<td><p role="column_definition">view_name <code>sql_identifier</code></p>
<p>Name of the view</p></td>
</tr>
<tr>
<td><p role="column_definition">table_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the table that contains the column that is used by the view (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">table_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the table that contains the column that is used by the view</p></td>
</tr>
<tr>
<td><p role="column_definition">table_name <code>sql_identifier</code></p>
<p>Name of the table that contains the column that is used by the view</p></td>
</tr>
<tr>
<td><p role="column_definition">column_name <code>sql_identifier</code></p>
<p>Name of the column that is used by the view</p></td>
</tr>
</tbody>
</table>

## `view_routine_usage`

The view `view_routine_usage` identifies all routines (functions and procedures) that are used in the query expression of a view (the `SELECT` statement that defines the view). A routine is only included if that routine is owned by a currently enabled role.

<table>
<caption>view_routine_usage Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">table_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the view (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">table_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the view</p></td>
</tr>
<tr>
<td><p role="column_definition">table_name <code>sql_identifier</code></p>
<p>Name of the view</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_catalog <code>sql_identifier</code></p>
<p>Name of the database containing the function (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_schema <code>sql_identifier</code></p>
<p>Name of the schema containing the function</p></td>
</tr>
<tr>
<td><p role="column_definition">specific_name <code>sql_identifier</code></p>
<p>The “specific name” of the function. See <a href="#infoschema-routines"></a> for more information.</p></td>
</tr>
</tbody>
</table>

## `view_table_usage`

The view `view_table_usage` identifies all tables that are used in the query expression of a view (the `SELECT` statement that defines the view). A table is only included if that table is owned by a currently enabled role.

> [!NOTE]
> System tables are not included. This should be fixed sometime.

<table>
<caption>view_table_usage Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">view_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the view (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">view_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the view</p></td>
</tr>
<tr>
<td><p role="column_definition">view_name <code>sql_identifier</code></p>
<p>Name of the view</p></td>
</tr>
<tr>
<td><p role="column_definition">table_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the table that is used by the view (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">table_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the table that is used by the view</p></td>
</tr>
<tr>
<td><p role="column_definition">table_name <code>sql_identifier</code></p>
<p>Name of the table that is used by the view</p></td>
</tr>
</tbody>
</table>

## `views`

The view `views` contains all views defined in the current database. Only those views are shown that the current user has access to (by way of being the owner or having some privilege).

<table>
<caption>views Columns</caption>
<thead>
<tr>
<th><p role="column_definition">Column Type</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="column_definition">table_catalog <code>sql_identifier</code></p>
<p>Name of the database that contains the view (always the current database)</p></td>
</tr>
<tr>
<td><p role="column_definition">table_schema <code>sql_identifier</code></p>
<p>Name of the schema that contains the view</p></td>
</tr>
<tr>
<td><p role="column_definition">table_name <code>sql_identifier</code></p>
<p>Name of the view</p></td>
</tr>
<tr>
<td><p role="column_definition">view_definition <code>character_data</code></p>
<p>Query expression defining the view (null if the view is not owned by a currently enabled role)</p></td>
</tr>
<tr>
<td><p role="column_definition">check_option <code>character_data</code></p>
<p><code>CASCADED</code> or <code>LOCAL</code> if the view has a <code>CHECK OPTION</code> defined on it, <code>NONE</code> if not</p></td>
</tr>
<tr>
<td><p role="column_definition">is_updatable <code>yes_or_no</code></p>
<p><code>YES</code> if the view is updatable (allows <code>UPDATE</code> and <code>DELETE</code>), <code>NO</code> if not</p></td>
</tr>
<tr>
<td><p role="column_definition">is_insertable_into <code>yes_or_no</code></p>
<p><code>YES</code> if the view is insertable into (allows <code>INSERT</code>), <code>NO</code> if not</p></td>
</tr>
<tr>
<td><p role="column_definition">is_trigger_updatable <code>yes_or_no</code></p>
<p><code>YES</code> if the view has an <code>INSTEAD OF</code> <code>UPDATE</code> trigger defined on it, <code>NO</code> if not</p></td>
</tr>
<tr>
<td><p role="column_definition">is_trigger_deletable <code>yes_or_no</code></p>
<p><code>YES</code> if the view has an <code>INSTEAD OF</code> <code>DELETE</code> trigger defined on it, <code>NO</code> if not</p></td>
</tr>
<tr>
<td><p role="column_definition">is_trigger_insertable_into <code>yes_or_no</code></p>
<p><code>YES</code> if the view has an <code>INSTEAD OF</code> <code>INSERT</code> trigger defined on it, <code>NO</code> if not</p></td>
</tr>
</tbody>
</table>
