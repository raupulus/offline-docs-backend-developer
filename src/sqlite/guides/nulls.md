---
title: NULL Handling in SQLite
source_url: https://www.sqlite.org/nulls.html
source_path: nulls.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 3630
---

## NULL Handling in SQLite Versus Other Database Engines

The goal is to make SQLite handle NULLs in a standards-compliant way. But the descriptions in the SQL standards on how to handle NULLs seem ambiguous. It is not clear from the standards documents exactly how NULLs should be handled in all circumstances.

So instead of going by the standards documents, various popular SQL engines were tested to see how they handle NULLs. The idea was to make SQLite work like all the other engines. An SQL test script was developed and run by volunteers on various SQL RDBMSes and the results of those tests were used to deduce how each engine processed NULL values. The original tests were run in May of 2002. A copy of the test script is found at the end of this document.

SQLite was originally coded in such a way that the answer to all questions in the chart below would be "Yes". But the experiments run on other SQL engines showed that none of them worked this way. So SQLite was modified to work the same as Oracle, PostgreSQL, and DB2. This involved making NULLs indistinct for the purposes of the SELECT DISTINCT statement and for the UNION operator in a SELECT. NULLs are still distinct in a UNIQUE column. This seems somewhat arbitrary, but the desire to be compatible with other engines outweighed that objection.

It is possible to make SQLite treat NULLs as distinct for the purposes of the SELECT DISTINCT and UNION. To do so, one should change the value of the NULL_ALWAYS_DISTINCT \#define in the `sqliteInt.h` source file and recompile.

> *Update 2003-07-13:* Since this document was originally written some of the database engines tested have been updated and users have been kind enough to send in corrections to the chart below. The original data showed a wide variety of behaviors, but over time the range of behaviors has converged toward the PostgreSQL/Oracle model. The only significant difference is that Informix and MS-SQL both treat NULLs as indistinct in a UNIQUE column.
>
> The fact that NULLs are distinct for UNIQUE columns but are indistinct for SELECT DISTINCT and UNION continues to be puzzling. It seems that NULLs should be either distinct everywhere or nowhere. And the SQL standards documents suggest that NULLs should be distinct everywhere. Yet as of this writing, no SQL engine tested treats NULLs as distinct in a SELECT DISTINCT statement or in a UNION.

The following table shows the results of the NULL handling experiments.

|    | SQLite | PostgreSQL | Oracle | Informix | DB2 | MS-SQL | OCELOT |
|----|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Adding anything to null gives null | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Multiplying null by zero gives null | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| nulls are distinct in a UNIQUE column | Yes | Yes | Yes | No | (Note 4) | No | Yes |
| nulls are distinct in SELECT DISTINCT | No | No | No | No | No | No | No |
| nulls are distinct in a UNION | No | No | No | No | No | No | No |
| "CASE WHEN null THEN 1 ELSE 0 END" is 0? | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| "null OR true" is true | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| "not (null AND false)" is true | Yes | Yes | Yes | Yes | Yes | Yes | Yes |

<table style="width:100%;" data-border="1" data-cellpadding="3" width="100%">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th>  </th>
<th style="text-align: center;">MySQL<br />
3.23.41</th>
<th style="text-align: center;">MySQL<br />
4.0.16</th>
<th style="text-align: center;">Firebird</th>
<th style="text-align: center;">SQL<br />
Anywhere</th>
<th style="text-align: center;">Borland<br />
Interbase</th>
</tr>
</thead>
<tbody>
<tr>
<td>Adding anything to null gives null</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
</tr>
<tr>
<td>Multiplying null by zero gives null</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
</tr>
<tr>
<td>nulls are distinct in a UNIQUE column</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#aaaad2">(Note 4)</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#aaaad2">(Note 4)</td>
</tr>
<tr>
<td>nulls are distinct in SELECT DISTINCT</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#c7a9a9">No</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#c7a9a9">No</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#c7a9a9">No (Note 1)</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#c7a9a9">No</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#c7a9a9">No</td>
</tr>
<tr>
<td>nulls are distinct in a UNION</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#aaaad2">(Note 3)</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#c7a9a9">No</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#c7a9a9">No (Note 1)</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#c7a9a9">No</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#c7a9a9">No</td>
</tr>
<tr>
<td>"CASE WHEN null THEN 1 ELSE 0 END" is 0?</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#aaaad2">(Note 5)</td>
</tr>
<tr>
<td>"null OR true" is true</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
</tr>
<tr>
<td>"not (null AND false)" is true</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#c7a9a9">No</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
<td style="text-align: center;" data-valign="center" data-bgcolor="#a9c7a9">Yes</td>
</tr>
</tbody>
</table>

<table data-border="0" data-align="right" data-cellpadding="0" data-cellspacing="0">
<tbody>
<tr>
<td rowspan="5" data-valign="top">Notes:  </td>
<td>1. </td>
<td>Older versions of firebird omit all NULLs from SELECT DISTINCT and from UNION.</td>
</tr>
<tr>
<td>2. </td>
<td>Test data unavailable.</td>
</tr>
<tr>
<td>3. </td>
<td>MySQL version 3.23.41 does not support UNION.</td>
</tr>
<tr>
<td>4. </td>
<td>DB2, SQL Anywhere, and Borland Interbase do not allow NULLs in a UNIQUE column.</td>
</tr>
<tr>
<td>5. </td>
<td>Borland Interbase does not support CASE expressions.</td>
</tr>
</tbody>
</table>

\

 

The following script was used to gather information for the table above.

\
-- I have about decided that SQL's treatment of NULLs is capricious and cannot be\
-- deduced by logic.  It must be discovered by experiment.  To that end, I have \
-- prepared the following script to test how various SQL databases deal with NULL.\
-- My aim is to use the information gathered from this script to make SQLite as\
-- much like other databases as possible.\
--\
-- If you could please run this script in your database engine and mail the results\
-- to me at drh@hwaci.com, that will be a big help.  Please be sure to identify the\
-- database engine you use for this test.  Thanks.\
--\
-- If you have to change anything to get this script to run with your database\
-- engine, please send your revised script together with your results.\
--\
\
-- Create a test table with data\
create table t1(a int, b int, c int);\
insert into t1 values(1,0,0);\
insert into t1 values(2,0,1);\
insert into t1 values(3,1,0);\
insert into t1 values(4,1,1);\
insert into t1 values(5,null,0);\
insert into t1 values(6,null,1);\
insert into t1 values(7,null,null);\
\
-- Check to see what CASE does with NULLs in its test expressions\
select a, case when b\<\>0 then 1 else 0 end from t1;\
select a+10, case when not b\<\>0 then 1 else 0 end from t1;\
select a+20, case when b\<\>0 and c\<\>0 then 1 else 0 end from t1;\
select a+30, case when not (b\<\>0 and c\<\>0) then 1 else 0 end from t1;\
select a+40, case when b\<\>0 or c\<\>0 then 1 else 0 end from t1;\
select a+50, case when not (b\<\>0 or c\<\>0) then 1 else 0 end from t1;\
select a+60, case b when c then 1 else 0 end from t1;\
select a+70, case c when b then 1 else 0 end from t1;\
\
-- What happens when you multiply a NULL by zero?\
select a+80, b\*0 from t1;\
select a+90, b\*c from t1;\
\
-- What happens to NULL for other operators?\
select a+100, b+c from t1;\
\
-- Test the treatment of aggregate operators\
select count(\*), count(b), sum(b), avg(b), min(b), max(b) from t1;\
\
-- Check the behavior of NULLs in WHERE clauses\
select a+110 from t1 where b\<10;\
select a+120 from t1 where not b\>10;\
select a+130 from t1 where b\<10 OR c=1;\
select a+140 from t1 where b\<10 AND c=1;\
select a+150 from t1 where not (b\<10 AND c=1);\
select a+160 from t1 where not (c=1 AND b\<10);\
\
-- Check the behavior of NULLs in a DISTINCT query\
select distinct b from t1;\
\
-- Check the behavior of NULLs in a UNION query\
select b from t1 union select b from t1;\
\
-- Create a new table with a unique column.  Check to see if NULLs are considered\
-- to be distinct.\
create table t2(a int, b int unique);\
insert into t2 values(1,1);\
insert into t2 values(2,null);\
insert into t2 values(3,null);\
select \* from t2;\
\
drop table t1;\
drop table t2;\
