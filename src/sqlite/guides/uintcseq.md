---
title: The UINT Collating Sequence
source_url: https://www.sqlite.org/uintcseq.html
source_path: uintcseq.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 8160
---

# 1. Overview

The UINT collating sequence is a [loadable extension](loadext.md) for SQLite that implements a new collating sequence that compares text containing unsigned integers in numeric order.

The UINT collating sequence is not a standard part of SQLite. It must be loaded as a separate extension. The source code to UINT is in the [uint.c source file](https://sqlite.org/src/file/ext/misc/uint.c) in the [ext/misc/ folder](https://sqlite.org/src/file/ext/misc) of the SQLite source tree.

The UINT collating sequence is not included in standard builds of the SQLite library, but it is loaded by default in the [CLI](cli.md). This is typical of the [CLI](cli.md) which loads various extensions above and beyond what are available in the standard SQLite library.

The UINT collating sequence works just like the default BINARY collating sequence for text, except that embedded strings of digits compare in numeric order.

- Leading zeros are handled properly, in the sense that they do not mess with the maginitude comparison of embedded strings of digits. "x00123y" is equal to "x123y".

- Only unsigned integers are recognized. Plus and minus signs are ignored. Decimal points and exponential notation are ignored.

- Embedded integers can be of arbitrary length. Comparison is not limited to integers that can be expressed as a 64-bit machine integer.

# 2. Example:

> <table data-border="1" data-cellspacing="0" data-cellpadding="10">
> <colgroup>
> <col style="width: 50%" />
> <col style="width: 50%" />
> </colgroup>
> <thead>
> <tr>
> <th style="text-align: left;">COLLATE binary</th>
> <th style="text-align: left;">COLLATE uint</th>
> </tr>
> </thead>
> <tbody>
> <tr>
> <td style="text-align: left;" data-valign="top"><br />
> '0000123457'<br />
> '123456'<br />
> 'abc0000000010xyz'<br />
> 'abc0010xyy'<br />
> 'abc10xzz'<br />
> 'abc674xyz'<br />
> 'abc87xyz'<br />
> 'abc9xyz'</td>
> <td style="text-align: left;" data-valign="top"><br />
> '123456'<br />
> '0000123457'<br />
> 'abc9xyz'<br />
> 'abc0010xyy'<br />
> 'abc0000000010xyz'<br />
> 'abc10xzz'<br />
> 'abc87xyz'<br />
> 'abc674xyz'</td>
> </tr>
> </tbody>
> </table>
