---
title: The Base64() SQL Function
source_url: https://www.sqlite.org/base64.html
source_path: base64.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 150
---

# 1. Overview

The base64() function is an SQL function implemented as a [loadable extension](loadext.md) for SQLite. The function converts a binary BLOB into equivalent [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648) text or converts RFC 4648 text into the equivalent BLOB.

The base64() function is not a standard part of SQLite. It must be loaded as a separate extension. The source code to base64() is in the [base64.c source file](https://sqlite.org/src/file/ext/misc/base64.c) in the [ext/misc/ folder](https://sqlite.org/src/file/ext/misc) of the SQLite source tree.

The base64() function is not included in standard builds of the SQLite library, but it is loaded by default in the [CLI](cli.md). This is typical of the [CLI](cli.md) which loads various extensions above and beyond what are available in the standard SQLite library.

# 2. Features

1.  The base64() function always takes a single argument.

2.  If the argument to base64() is a BLOB, then the return value is TEXT that is the [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648) encoding of that BLOB.

3.  If the argument to base64() is base64 TEXT then the return value is a BLOB that is the binary data corresponding to that base64 TEXT.

4.  If the argument to base64() is NULL, then NULL is returned.

5.  An error is raised if the argument to base64() is something other than TEXT, BLOB, or NULL.

6.  If the argument is TEXT, leading and trailing whitespace is ignored.

7.  If the argument is TEXT that has a prefix that looks like base64 but contains non-base64 characters, then as much of the input as possible is translated into a BLOB and that BLOB is returned.

8.  The base64() function uses the standard [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648) alphabet: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".

# 3. See Also

- Build-in SQL functions [hex()](lang_corefunc.md#hex) and [unhex()](lang_corefunc.md#unhex).

- Extension function [base85()](base85.md).
