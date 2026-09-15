---
title: intarray — manipulate arrays of integers
source_url: https://www.postgresql.org/docs/17/intarray.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: intarray.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 750
---

## intarray manipulate arrays of integers

intarray

The `intarray` module provides a number of useful functions and operators for manipulating null-free arrays of integers. There is also support for indexed searches using some of the operators.

All of these operations will throw an error if a supplied array contains any NULL elements.

Many of these operations are only sensible for one-dimensional arrays. Although they will accept input arrays of more dimensions, the data is treated as though it were a linear array in storage order.

This module is considered “trusted”, that is, it can be installed by non-superusers who have `CREATE` privilege on the current database.

## `intarray` Functions and Operators

The functions provided by the `intarray` module are shown in [ Functions](#intarray-func-table), the operators in [ Operators](#intarray-op-table).

<table id="intarray-func-table">
<caption><code>intarray</code> Functions</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p>
<p>Example(s)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>icount</code> ( <code>integer[]</code> ) integer</p>
<p>Returns the number of elements in the array.</p>
<p><code>icount('{1,2,3}'::integer[])</code> 3</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>sort</code> ( <code>integer[]</code>, <code>dir</code> <code>text</code> ) integer[]</p>
<p>Sorts the array in either ascending or descending order. <code>dir</code> must be <code>asc</code> or <code>desc</code>.</p>
<p><code>sort('{1,3,2}'::integer[], 'desc')</code> {3,2,1}</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>sort</code> ( <code>integer[]</code> ) integer[]</p>
<p role="func_signature"><span class="indexterm"></span> <code>sort_asc</code> ( <code>integer[]</code> ) integer[]</p>
<p>Sorts in ascending order.</p>
<p><code>sort(array[11,77,44])</code> {11,44,77}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>sort_desc</code> ( <code>integer[]</code> ) integer[]</p>
<p>Sorts in descending order.</p>
<p><code>sort_desc(array[11,77,44])</code> {77,44,11}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>uniq</code> ( <code>integer[]</code> ) integer[]</p>
<p>Removes adjacent duplicates. Often used with <code>sort</code> to remove all duplicates.</p>
<p><code>uniq('{1,2,2,3,1,1}'::integer[])</code> {1,2,3,1}</p>
<p><code>uniq(sort('{1,2,3,2,1}'::integer[]))</code> {1,2,3}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>idx</code> ( <code>integer[]</code>, <code>item</code> <code>integer</code> ) integer</p>
<p>Returns index of the first array element matching <code>item</code>, or 0 if no match.</p>
<p><code>idx(array[11,22,33,22,11], 22)</code> 2</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>subarray</code> ( <code>integer[]</code>, <code>start</code> <code>integer</code>, <code>len</code> <code>integer</code> ) integer[]</p>
<p>Extracts the portion of the array starting at position <code>start</code>, with <code>len</code> elements.</p>
<p><code>subarray('{1,2,3,2,1}'::integer[], 2, 3)</code> {2,3,2}</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>subarray</code> ( <code>integer[]</code>, <code>start</code> <code>integer</code> ) integer[]</p>
<p>Extracts the portion of the array starting at position <code>start</code>.</p>
<p><code>subarray('{1,2,3,2,1}'::integer[], 2)</code> {2,3,2,1}</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>intset</code> ( <code>integer</code> ) integer[]</p>
<p>Makes a single-element array.</p>
<p><code>intset(42)</code> {42}</p></td>
</tr>
</tbody>
</table>

<table id="intarray-op-table">
<caption><code>intarray</code> Operators</caption>
<thead>
<tr>
<th><p role="func_signature">Operator</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><code>integer[]</code> <code>&amp;&amp;</code> <code>integer[]</code> boolean</p>
<p>Do arrays overlap (have at least one element in common)?</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>integer[]</code> <code>@&gt;</code> <code>integer[]</code> boolean</p>
<p>Does left array contain right array?</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>integer[]</code> <code>&lt;@</code> <code>integer[]</code> boolean</p>
<p>Is left array contained in right array?</p></td>
</tr>
<tr>
<td><p role="func_signature"><code></code> <code>#</code> <code>integer[]</code> integer</p>
<p>Returns the number of elements in the array.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>integer[]</code> <code>#</code> <code>integer</code> integer</p>
<p>Returns index of the first array element matching the right argument, or 0 if no match. (Same as <code>idx</code> function.)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>integer[]</code> <code>+</code> <code>integer</code> integer[]</p>
<p>Adds element to end of array.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>integer[]</code> <code>+</code> <code>integer[]</code> integer[]</p>
<p>Concatenates the arrays.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>integer[]</code> <code>-</code> <code>integer</code> integer[]</p>
<p>Removes entries matching the right argument from the array.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>integer[]</code> <code>-</code> <code>integer[]</code> integer[]</p>
<p>Removes elements of the right array from the left array.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>integer[]</code> <code>|</code> <code>integer</code> integer[]</p>
<p>Computes the union of the arguments.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>integer[]</code> <code>|</code> <code>integer[]</code> integer[]</p>
<p>Computes the union of the arguments.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>integer[]</code> <code>&amp;</code> <code>integer[]</code> integer[]</p>
<p>Computes the intersection of the arguments.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>integer[]</code> <code>@@</code> <code>query_int</code> boolean</p>
<p>Does array satisfy query? (see below)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>query_int</code> <code>~~</code> <code>integer[]</code> boolean</p>
<p>Does array satisfy query? (commutator of <code>@@</code>)</p></td>
</tr>
</tbody>
</table>

The operators `&&`, `@>` and `<@` are equivalent to PostgreSQL's built-in operators of the same names, except that they work only on integer arrays that do not contain nulls, while the built-in operators work for any array type. This restriction makes them faster than the built-in operators in many cases.

The `@@` and `~~` operators test whether an array satisfies a query, which is expressed as a value of a specialized data type `query_int`. A query consists of integer values that are checked against the elements of the array, possibly combined using the operators `&` (AND), `|` (OR), and `!` (NOT). Parentheses can be used as needed. For example, the query `1&(2|3)` matches arrays that contain 1 and also contain either 2 or 3.

## Index Support

`intarray` provides index support for the `&&`, `@>`, and `@@` operators, as well as regular array equality.

Two parameterized GiST index operator classes are provided: `gist__int_ops` (used by default) is suitable for small- to medium-size data sets, while `gist__intbig_ops` uses a larger signature and is more suitable for indexing large data sets (i.e., columns containing a large number of distinct array values). The implementation uses an RD-tree data structure with built-in lossy compression.

`gist__int_ops` approximates an integer set as an array of integer ranges. Its optional integer parameter `numranges` determines the maximum number of ranges in one index key. The default value of `numranges` is 100. Valid values are between 1 and 253. Using larger arrays as GiST index keys leads to a more precise search (scanning a smaller fraction of the index and fewer heap pages), at the cost of a larger index.

`gist__intbig_ops` approximates an integer set as a bitmap signature. Its optional integer parameter `siglen` determines the signature length in bytes. The default signature length is 16 bytes. Valid values of signature length are between 1 and 2024 bytes. Longer signatures lead to a more precise search (scanning a smaller fraction of the index and fewer heap pages), at the cost of a larger index.

There is also a non-default GIN operator class `gin__int_ops`, which supports these operators as well as `<@`.

The choice between GiST and GIN indexing depends on the relative performance characteristics of GiST and GIN, which are discussed elsewhere.

## Example

    -- a message can be in one or more sections
    CREATE TABLE message (mid INT PRIMARY KEY, sections INT[], ...);

    -- create specialized index with signature length of 32 bytes
    CREATE INDEX message_rdtree_idx ON message USING GIST (sections gist__intbig_ops (siglen = 32));

    -- select messages in section 1 OR 2 - OVERLAP operator
    SELECT message.mid FROM message WHERE message.sections && '{1,2}';

    -- select messages in sections 1 AND 2 - CONTAINS operator
    SELECT message.mid FROM message WHERE message.sections @> '{1,2}';

    -- the same, using QUERY operator
    SELECT message.mid FROM message WHERE message.sections @@ '1&2'::query_int;

## Benchmark

The source directory `contrib/intarray/bench` contains a benchmark test suite, which can be run against an installed PostgreSQL server. (It also requires `DBD::Pg` to be installed.) To run:

    cd .../contrib/intarray/bench
    createdb TEST
    psql -c "CREATE EXTENSION intarray" TEST
    ./create_test.pl | psql TEST
    ./bench.pl

The `bench.pl` script has numerous options, which are displayed when it is run without any arguments.

## Authors

All work was done by Teodor Sigaev (<teodor@sigaev.ru>) and Oleg Bartunov (<oleg@sai.msu.su>). See [](http://www.sai.msu.su/~megera/postgres/gist/) for additional information. Andrey Oktyabrski did a great work on adding new functions and operations.
