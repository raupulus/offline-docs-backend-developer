---
title: '`gzip`'
description: gzip compression & decompression
source_url: https://docs.micropython.org/en/latest/library/gzip.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/gzip.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 180
---

# `gzip` -- gzip compression & decompression

gzip

\|see_cpython_module\| `python:gzip`.

This module allows compression and decompression of binary data with the [DEFLATE algorithm](https://en.wikipedia.org/wiki/DEFLATE) used by the gzip file format.

> [!NOTE]
> Prefer to use `deflate.DeflateIO` instead of the functions in this module as it provides a streaming interface to compression and decompression which is convenient and more memory efficient when working with reading or writing compressed data to a file, socket, or stream.

**Availability:**

- This module is **not present by default** in official MicroPython firmware releases as it duplicates functionality available in the `deflate
  <deflate>` module.
- A copy of this module can be installed (or frozen) from `micropython-lib` ([source](https://github.com/micropython/micropython-lib/blob/master/python-stdlib/gzip/gzip.py)). See `packages` for more information. This documentation describes that module.
- Compression support will only be available if compression support is enabled in the built-in `deflate <deflate>` module.

## Functions

open(filename, mode, /)

Wrapper around built-in `open` returning a GzipFile instance.

decompress(data, /)

Decompresses *data* into a bytes object.

compress(data, /)

Compresses *data* into a bytes object.

## Classes

This class can be used to wrap a *fileobj* which is any `stream-like <stream>` object such as a file, socket, or stream (including `io.BytesIO`). It is itself a stream and implements the standard read/readinto/write/close methods.

When the *mode* argument is `"rb"`, reads from the GzipFile instance will decompress the data in the underlying stream and return decompressed data.

If compression support is enabled then the *mode* argument can be set to `"wb"`, and writes to the GzipFile instance will be compressed and written to the underlying stream.

By default the GzipFile class will read and write data using the gzip file format, including a header and footer with checksum and a window size of 512 bytes.

The **file**, **compresslevel**, and **mtime** arguments are not supported. **fileobj** and **mode** must always be specified as keyword arguments.

## Examples

A typical use case for `gzip.GzipFile` is to read or write a compressed file from storage:

``` python
import gzip

# Reading:
with open("data.gz", "rb") as f:
    with gzip.GzipFile(fileobj=f, mode="rb") as g:
        # Use g.read(), g.readinto(), etc.

 # Same, but using gzip.open:
with gzip.open("data.gz", "rb") as f:
     # Use f.read(), f.readinto(), etc.

# Writing:
with open("data.gz", "wb") as f:
    with gzip.GzipFile(fileobj=f, mode="wb") as g:
        # Use g.write(...) etc

# Same, but using gzip.open:
with gzip.open("data.gz", "wb") as f:
    # Use f.write(...) etc

# Write a dictionary as JSON in gzip format, with a
# small (64 byte) window size.
config = { ... }
with gzip.open("config.gz", "wb") as f:
    json.dump(config, f)
```

For guidance on working with gzip sources and choosing the window size see the note at the `end of the deflate documentation <deflate_wbits>`.
