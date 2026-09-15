---
title: '`zlib`'
description: zlib compression & decompression
source_url: https://docs.micropython.org/en/latest/library/zlib.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/zlib.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 1080
---

# `zlib` -- zlib compression & decompression

zlib

\|see_cpython_module\| `python:zlib`.

This module allows compression and decompression of binary data with the [DEFLATE algorithm](https://en.wikipedia.org/wiki/DEFLATE) (commonly used in the zlib library and gzip archiver).

> [!NOTE]
> Prefer to use `deflate.DeflateIO` instead of the functions in this module as it provides a streaming interface to compression and decompression which is convenient and more memory efficient when working with reading or writing compressed data to a file, socket, or stream.

**Availability:**

- From MicroPython v1.21 onwards, this module may not be present by default on all MicroPython firmware as it duplicates functionality available in the `deflate <deflate>` module.
- A copy of this module can be installed (or frozen) from `micropython-lib` ([source](https://github.com/micropython/micropython-lib/blob/master/python-stdlib/zlib/zlib.py)). See `packages` for more information. This documentation describes that module.
- Requires the built-in `deflate <deflate>` module (available since MicroPython v1.21)
- Compression support will only be available if compression support is enabled in the built-in `deflate <deflate>` module.

## Functions

decompress(data, wbits=15, /)

Decompresses *data* into a bytes object.

The *wbits* parameter works the same way as for `zlib.compress` with the following additional valid values:

- `0`: Automatically determine the window size from the zlib header (*data* must be in zlib format).
- `35` to `47`: Auto-detect either the zlib or gzip format.

As for `zlib.compress`, see the `CPython documentation for zlib <python:zlib>` for more information about the *wbits* parameter. As for `zlib.compress`, MicroPython also supports smaller window sizes than CPython. See more `MicroPython-specific details <deflate_wbits>` in the `deflate <deflate>` module documentation.

If the data to be decompressed requires a larger window size, it will fail during decompression.

compress(data, wbits=15, /)

Compresses *data* into a bytes object.

*wbits* allows you to configure the DEFLATE dictionary window size and the output format. The window size allows you to trade-off memory usage for compression level. A larger window size will allow the compressor to reference fragments further back in the input. The output formats are "raw" DEFLATE (no header/footer), zlib, and gzip, where the latter two include a header and checksum.

The low four bits of the absolute value of *wbits* set the base-2 logarithm of the DEFLATE dictionary window size. So for example, `wbits=10`, `wbits=-10`, and `wbits=26` all set the window size to 1024 bytes. Valid window sizes are `5` to `15` inclusive (corresponding to 32 to 32k bytes).

Negative values of *wbits* between `-5` and `-15` correspond to "raw" output mode, positive values between `5` and `15` correspond to zlib output mode, and positive values between `21` and `31` correspond to gzip output mode.

See the `CPython documentation for zlib <python:zlib>` for more information about the *wbits* parameter. Note that MicroPython allows for smaller window sizes, which is useful when memory is constrained while still achieving a reasonable level of compression. It also speeds up the compressor. See more `MicroPython-specific details <deflate_wbits>` in the `deflate <deflate>` module documentation.
