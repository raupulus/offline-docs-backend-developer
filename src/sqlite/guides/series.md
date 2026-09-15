---
title: The generate_series Table-Valued Function
source_url: https://www.sqlite.org/series.html
source_path: series.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 6580
---

# 1. Overview

The generate_series(START,STOP,STEP) [table-valued function](vtab.md#tabfunc2) is a [loadable extension](loadext.md) included in the SQLite source tree, and compiled into the [command-line shell](cli.md). The generate_series() table has one visible result column named "value" holding integer values and a number of rows determined by the parameters START, STOP, and STEP. The first row of the table has a value of START. Subsequent rows increment by STEP to a value not exceeding STOP.

The generate_series() table has additional, hidden columns named "start", "stop", and "step" whose values are the effective values of START, STOP and STEP as provided or defaulted. It also has a rowid, accessible by its usual names.

Omitted parameters take on default values. STEP defaults to 1. STOP defaults to 4294967295. The START parameter is required as of version 3.37.0 (2021-11-27) and later and an error will be raised if START is omitted or has a self-referential or otherwise uncomputable value. Older versions used a default of 0 for START. The legacy behavior can be obtained from recent code by compiling with -DZERO_ARGUMENT_GENERATE_SERIES.

## 1.1. Equivalent Recursive Common Table Expression

The generate_series table can be simulated for positive step values using a [recursive common table expression](lang_with.md#recursivecte). If the three parameters are \$start, \$end, and \$step, then the equivalent common table expression is:

WITH RECURSIVE generate_series(value) AS (\
  SELECT \$start\
  UNION ALL\
  SELECT value+\$step FROM generate_series\
   WHERE value+\$step\<=\$end\
) ...\

The common table expression works without having to load an extension. On the other hand, the extension is easier to program and faster.

# 2. Usage Examples

Generate all multiples of 5 less than or equal to 100:

SELECT value FROM generate_series(5,100,5);\

Generate the 20 random integer values:

SELECT random() FROM generate_series(1,20);\

Find the name of every customer whose account number is an even multiple of 100 between 10000 and 20000.

SELECT customer.name\
  FROM customer, generate_series(10000,20000,100)\
 WHERE customer.id=value;\
/\* or \*/\
SELECT name FROM customer\
 WHERE id IN (SELECT value\
                FROM generate_series(10000,20000,200));\
