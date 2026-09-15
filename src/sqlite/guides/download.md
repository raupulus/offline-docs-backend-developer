---
title: SQLite Download Page
source_url: https://www.sqlite.org/download.html
source_path: download.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 2770
---

## SQLite Download Page

------------------------------------------------------------------------

<span id="encoding"></span>

### Build Product Names and Info

Build products are named using one of the following templates:

1.  **sqlite-**product**-**version**.zip**
2.  **sqlite-**product**-**version**.tar.gz**
3.  **sqlite-**product**-**os**-**cpu**-**version**.zip**
4.  **sqlite-**product**-**date**.zip**

Templates (1) and (2) are used for source-code products. Template (1) is used for generic source-code products and template (2) is used for source-code products that are generally only useful on unix-like platforms. Template (3) is used for precompiled binaries products. Template (4) is used for unofficial pre-release "snapshots" of source code.

The *version* is encoded so that filenames sort in order of increasing version number when viewed using "ls". For version 3.X.Y the filename encoding is 3XXYY00. For branch version 3.X.Y.Z, the encoding is 3XXYYZZ.

The *date* in template (4) is of the form: YYYYMMDDHHMM

For convenient, script-driven extraction of the downloadable file URLs and associated information, an HTML comment is embedded in this page's source. Its first line (sans leading tag) reads:

> **Download product data for scripts to read**

Its subsequent lines comprise a CSV table with this column header:

> **PRODUCT,VERSION,RELATIVE-URL,SIZE-IN-BYTES,SHA3-HASH**

The column header and following data lines have no leading space. The PRODUCT column is a constant value ("PRODUCT") for convenient regular expression matching. Other columns are self-explanatory. This format will remain stable except for possible new columns appended to the right of older columns. <span id="cvs"></span> <span id="fossil"></span> <span id="srctree"></span>

### Source Code Repositories

The SQLite source code is maintained in three geographically-dispersed self-synchronizing [Fossil](https://www.fossil-scm.org/) repositories that are available for anonymous read-only access. Anyone can view the repository contents and download historical versions of individual files or ZIP archives of historical check-ins. You can also [clone the entire repository](getthecode.md#clone).

See the [How To Compile SQLite](howtocompile.md) page for additional information on how to use the raw SQLite source code. Note that a recent version of [Tcl](https://www.tcl-lang.org/) is required in order to build from the repository sources. The [amalgamation](amalgamation.md) source code files (the "sqlite3.c" and "sqlite3.h" files) build products and are not contained in raw source code tree.

> <https://sqlite.org/src> (Dallas)\
> <https://www2.sqlite.org/src> (Newark)\
> <https://www3.sqlite.org/src> (San Francisco)\

There is a GitHub mirror at

> [https://github.com/sqlite/sqlite/](https://github.com/sqlite/sqlite)

The documentation is maintained in separate [Fossil](https://fossil-scm.org/) repositories located at:

> <https://sqlite.org/docsrc> (Dallas)\
> <https://www2.sqlite.org/docsrc> (Newark)\
> <https://www3.sqlite.org/docsrc> (San Francisco)\
