---
title: The Base85() SQL Function
source_url: https://www.sqlite.org/base85.html
source_path: base85.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 160
---

# 1. Overview

The base85() function is an SQL function implemented as a [loadable extension](loadext.md) for SQLite. The function converts a binary BLOB into an equivalent base-85 text encoding or converts that same base-85 text encoding back into a BLOB.

The base85() function is not a standard part of SQLite. It must be loaded as a separate extension. The source code to base85() is in the [base85.c source file](https://sqlite.org/src/file/ext/misc/base85.c) in the [ext/misc/ folder](https://sqlite.org/src/file/ext/misc) of the SQLite source tree.

The base85() function is not included in standard builds of the SQLite library, but it is loaded by default in the [CLI](cli.md). This is typical of the [CLI](cli.md) which loads various extensions above and beyond what are available in the standard SQLite library.

Like [base64()](base64.md) representations, the base85() function can be used to format binary content through any sane ASCII channel unmolested. It also plays nicely in CSV or written as TCL brace-enclosed literals or SQL string literals. It is not suited for unmodified use in XML-like documents.

# 2. Encoding

The encoding used resembles Ascii85, but was devised by the author (Larry Brasfield) before Mozilla, Adobe, ZMODEM or other Ascii85 variant sources existed, in the 1984 timeframe on a VAX mainframe. Further, this is an independent implementation of a base85 system. Hence, the author has rightfully put this into the public domain.

Base85 numerals are taken from the set of 7-bit USASCII codes, excluding control characters and Space ! " ' ( ) { \| } ~ Del in code order representing digit values 0 to 84 (base 10.)

Groups of 4 bytes, interpreted as big-endian 32-bit values, are represented as 5-digit base85 numbers with MS to LS digit order. Groups of 1-3 bytes are represented with 2-4 digits, still big-endian but 8-24 bit values. (Using big-endian yields the simplest transition to byte groups smaller than 4 bytes. These byte groups can also be considered base-256 numbers.) Groups of 0 bytes are represented with 0 digits and vice-versa. No pad characters are used; encoded base85 numeral sequence (aka "group") length maps 1-to-1 to the decoded binary length.

Any character not in the base85 numeral set delimits groups. When base85 is streamed or stored in containers of indefinite size, newline is used to separate it into sub-sequences of no more than 80 digits so that fgets() can be used to read it.

# 3. Features

1.  The base85() function always takes a single argument that must be TEXT (for base85-to-binary conversion) or a BLOB (for binary-to-base85 conversion).

2.  If the argument to base85() is a BLOB, then the return value is TEXT according to the encoding described above.

3.  If the argument to base85() is TEXT as described above then the return value is a BLOB that is the binary data corresponding to that base85 text.

4.  An error is raised if the argument to base85() is something other than TEXT or BLOB.

# 4. See Also

- Build-in SQL function [hex()](lang_corefunc.md#hex).

- Extension function [base64()](base64.md).
