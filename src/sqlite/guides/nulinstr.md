---
title: NUL Characters In Strings
source_url: https://www.sqlite.org/nulinstr.html
source_path: nulinstr.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 3620
---

# 1. Introduction

SQLite allows NUL characters (ASCII 0x00, Unicode \u0000) in the middle of string values stored in the database. However, the use of NUL within strings can lead to surprising behaviors:

1.  The [length() SQL function](lang_corefunc.md#length) only counts characters up to and excluding the first NUL.

2.  The [quote() SQL function](lang_corefunc.md#quote) only shows characters up to and excluding the first NUL.

3.  The [.dump](cli.md#dump) command in the [CLI](cli.md) omits the first NUL character and all subsequent text in the SQL output that it generates. In fact, the [CLI](cli.md) omits everything past the first NUL character in all contexts.

The use of NUL characters in SQL text strings is not recommended.

# 2. Unexpected Behavior

Consider the following SQL:

CREATE TABLE t1(\
  a INTEGER PRIMARY KEY,\
  b TEXT\
);\
INSERT INTO t1(a,b) VALUES(1, 'abc'\|\|char(0)\|\|'xyz');\
\
SELECT a, b, length(b) FROM t1;\

The SELECT statement above shows output of:

1,'abc',3\

(Through this document, we assume that the [CLI](cli.md) has "[.mode quote](climode.md#dotmodequote)" set.) But if you run:

SELECT \* FROM t1 WHERE b='abc';\

Then no rows are returned. SQLite knows that the t1.b column actually holds a 7-character string, and the 7-character string 'abc'\|\|char(0)\|\|'xyz' is not equal to the 3-character string 'abc', and so no rows are returned. But a user might be easily confused by this because the [CLI](cli.md) output seems to show that the string has only 3 characters. This seems like a bug. But it is how SQLite works.

# 3. How To Tell If You Have NUL Characters In Your Strings

If you [CAST](lang_expr.md#castexpr) a string into a BLOB, then the entire length of the string is shown. For example:

SELECT a, CAST(b AS BLOB) FROM t1;\

Gives this result:

1,X'6162630078797a'\

In the BLOB output, you can clearly see the NUL character as the 4th character in the 7-character string.

Another, more automated, way to tell if a string value X contains embedded NUL characters is to use an expression like this:

instr(X,char(0))\

If this expression returns a non-zero value N, then there exists an embedded NUL at the N-th character position. Thus to count the number of rows that contain embedded NUL characters:

SELECT count(\*) FROM t1 WHERE instr(b,char(0))\>0;\

# 4. Removing NUL Characters From A Text Field

The following example shows how to remove NUL character, and all text that follows, from a column of a table. So if you have a database file that contains embedded NULs and you would like to remove them, running UPDATE statements similar to the following might help:

UPDATE t1 SET b=substr(b,1,instr(b,char(0)))\
 WHERE instr(b,char(0));\
