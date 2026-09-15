---
title: Change in Default Page Size in SQLite Version 3.12.0
source_url: https://www.sqlite.org/pgszchng2016.html
source_path: pgszchng2016.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 3710
---

# The Default Page Size Change of SQLite 3.12.0

## 1.0 Introduction

An SQLite database file consists of one or more "pages". For a single database file, all pages are the same size, though for different database files, the page size can be any power of two between 512 and 65536, inclusive.

Since the SQLite database file format was designed (in 2003) the default [page size](pragma.md#pragma_page_size) for new databases has been 1024 bytes. This was a reasonable choice in 2003. But on modern hardware, a 4096 byte page is a faster and better choice. So, beginning with SQLite [version 3.12.0](releaselog/3_12_0.md) (2016-03-29)) the default page size for new database files has been increased to 4096 bytes.

The upper bound on the database [cache size](pragma.md#pragma_cache_size) has traditionally defaulted to 2000 pages. SQLite [version 3.12.0](releaselog/3_12_0.md) also changes this default setting to be "-2000" which means 2000\*1024 bytes, regardless of page size. So, the upper bound on the amount of memory used for the page cache is unchanged.

## 2.0 <u>Not</u> a Compatibility Break

These changes in the default behavior of SQLite are not a compatibility break. All legacy database files continue to be readable and writable by newer versions of SQLite, and all newly created database files continue to be readable and writable by legacy versions of the SQLite library. The only thing that is changing is some default settings. This should result in a performance increase for many applications.

Though most applications should not notice any change (except that they run a little faster), if problems arise then the legacy behavior can be restored at compile-time by using the following options to the C-compiler:

> \
> -DSQLITE_DEFAULT_PAGE_SIZE=1024 \
> -DSQLITE_DEFAULT_CACHE_SIZE=2000\

The page size and cache size can also be set or changed at run-time using the [page_size pragma](pragma.md#pragma_page_size) and [cache_size pragma](pragma.md#pragma_cache_size), respectively.

## 3.0 Possible Negative Consequences Of This Change

The minimum size of an SQLite database is one page for each table and each index. With a larger page size, the size of an empty database for a given schema will grow by a factor of four, therefore. However, once the database begins to fill with content the size of the older 1024-byte page databases and the newer 4096-byte page databases will quickly converge. Due to relaxed bin-packing constraints, the 4096-byte page size might actually result in a smaller file, once substantial content is added.
