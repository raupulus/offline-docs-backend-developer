---
title: About SQLite
source_url: https://www.sqlite.org/about.html
source_path: about.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 30
---

# About SQLite

#### Executive Summary

[Full-featured SQL](fullsql.md)

[Billions and billions of deployments](mostdeployed.md)

[Single-file database](onefile.md)

[Public domain source code](copyright.md)

All source code in one file ([sqlite3.c](amalgamation.md))

[Small footprint](footprint.md)

Max DB size: [281 terabytes](limits.md) (2<sup><span class="small">48</span></sup> bytes)

Max row size: [1 gigabyte](limits.md)

[Faster than direct file I/O](fasterthanfs.md)

[Aviation-grade quality and testing](testing.md)

[Zero-configuration](zeroconf.md)

[ACID transactions, even after power loss](transactional.md)

[Stable, enduring file format](fileformat.md)

[Extensive, detailed documentation](doclist.md)

[Long-term support](lts.md)

SQLite is an in-process library that implements a [self-contained](selfcontained.md), [serverless](serverless.md), [zero-configuration](zeroconf.md), [transactional](transactional.md) SQL database engine. The code for SQLite is in the [public domain](copyright.md) and is thus free for use for any purpose, commercial or private. SQLite is the [most widely deployed](mostdeployed.md) database in the world with more applications than we can count, including several [high-profile projects.](famous.md)

SQLite is an embedded SQL database engine. Unlike most other SQL databases, SQLite does not have a separate server process. SQLite reads and writes directly to ordinary disk files. A complete SQL database with multiple tables, indices, triggers, and views, is contained in a single disk file. The database [file format](fileformat2.md) is cross-platform - you can freely copy a database between 32-bit and 64-bit systems or between [big-endian](http://en.wikipedia.org/wiki/Endianness) and [little-endian](http://en.wikipedia.org/wiki/Endianness) architectures. These features make SQLite a popular choice as an [Application File Format](appfileformat.md). SQLite database files are a [recommended storage format](locrsf.md) by the US Library of Congress. Think of SQLite not as a replacement for [Oracle](http://www.oracle.com/database/index.html) but as a replacement for [fopen()](http://man.he.net/man3/fopen)

SQLite is a compact library. With all features enabled, the [library size](footprint.md) can be less than 900KiB, depending on the target platform and compiler optimization settings. (64-bit code is larger. And some compiler optimizations such as aggressive function inlining and loop unrolling can cause the object code to be much larger.) There is a tradeoff between memory usage and speed. SQLite generally runs faster the more memory you give it. Nevertheless, performance is usually quite good even in low-memory environments. Depending on how it is used, SQLite can be [faster than direct filesystem I/O](fasterthanfs.md).

SQLite is [very carefully tested](testing.md) prior to every release and has a reputation for being very reliable. Most of the SQLite source code is devoted purely to testing and verification. An automated test suite runs millions and millions of test cases involving hundreds of millions of individual SQL statements and achieves [100% branch test coverage](testing.md#coverage). SQLite responds gracefully to memory allocation failures and disk I/O errors. Transactions are [ACID](http://en.wikipedia.org/wiki/ACID) even if interrupted by system crashes or power failures. All of this is verified by the automated tests using special test harnesses which simulate system failures. Of course, even with all this testing, there are still bugs. But unlike some similar projects (especially commercial competitors) SQLite is open and honest about all bugs and provides [bugs lists](https://sqlite.org/src/rptview?rn=1) and minute-by-minute [chronologies](https://sqlite.org/src/timeline) of code changes.

The SQLite code base is supported by an [international team](crew.md) of developers who work on SQLite full-time. The developers continue to expand the capabilities of SQLite and enhance its reliability and performance while maintaining backwards compatibility with the [published interface spec](c3ref/intro.md), [SQL syntax](lang.md), and database [file format](fileformat2.md). The source code is absolutely free to anybody who wants it, but [professional support](prosupport.md) is also available.

The SQLite project was started on [2000-05-09](https://sqlite.org/src/timeline?c=2000-05-29+14:26:00). The future is always hard to predict, but the intent of the developers is to support SQLite through the year 2050. Design decisions are made with that objective in mind.

We the developers hope that you find SQLite useful and we entreat you to use it well: to make good and beautiful products that are fast, reliable, and simple to use. Seek forgiveness for yourself as you forgive others. And just as you have received SQLite for free, so also freely give, paying the debt forward.
