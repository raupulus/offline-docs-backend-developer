---
title: OS Interface Open File Handle
source_url: https://www.sqlite.org/c3ref/file.html
source_path: c3ref/file.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1240
---

> \
> typedef struct sqlite3_file sqlite3_file;\
> struct sqlite3_file {\
>   const struct sqlite3_io_methods \*pMethods;  /\* Methods for an open file \*/\
> };\

An [sqlite3_file](../c3ref/file.md) object represents an open file in the [OS interface layer](../c3ref/vfs.md). Individual OS interface implementations will want to subclass this object by appending additional fields for their own use. The pMethods entry is a pointer to an [sqlite3_io_methods](../c3ref/io_methods.md) object that defines methods for performing I/O operations on the open file.

See also lists of [Objects](../c3ref/objlist.md), [Constants](../c3ref/constlist.md), and [Functions](../c3ref/funclist.md).
