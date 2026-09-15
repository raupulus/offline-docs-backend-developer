---
title: '`struct`'
description: pack and unpack primitive data types
source_url: https://docs.micropython.org/en/latest/library/struct.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/struct.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 950
---

# `struct` -- pack and unpack primitive data types

struct

\|see_cpython_module\| `python:struct`.

The following byte orders are supported:

| Character | Byte order             | Size     | Alignment |
|-----------|------------------------|----------|-----------|
| @         | native                 | native   | native    |
| \<        | little-endian          | standard | none      |
| \>        | big-endian             | standard | none      |
| !         | network (= big-endian) | standard | none      |

The following data types are supported:

| Format | C Type | Python type | Standard size |
|----|----|----|----|
| b | signed char | integer | 1 |
| B | unsigned char | integer | 1 |
| h | short | integer | 2 |
| H | unsigned short | integer | 2 |
| i | int | integer (`1\<fn\>`) | 4 |
| I | unsigned int | integer (`1\<fn\>`) | 4 |
| l | long | integer (`1\<fn\>`) | 4 |
| L | unsigned long | integer (`1\<fn\>`) | 4 |
| q | long long | integer (`1\<fn\>`) | 8 |
| Q | unsigned long long | integer (`1\<fn\>`) | 8 |
| e | n/a (half-float) | float (`2\<fn\>`) | 2 |
| f | float | float (`2\<fn\>`) | 4 |
| d | double | float (`2\<fn\>`) | 8 |
| s | char\[\] | bytes |  |
| P | void \* | integer |  |

1)  Requires long support when used with values larger than 30 bits.
2)  Requires floating point support.

Difference to CPython

Whitespace is not supported in format strings.

## Functions

calcsize(fmt)

Return the number of bytes needed to store the given *fmt*.

pack(fmt, v1, v2, ...)

Pack the values *v1*, *v2*, ... according to the format string *fmt*. The return value is a bytes object encoding the values.

pack_into(fmt, buffer, offset, v1, v2, ...)

Pack the values *v1*, *v2*, ... according to the format string *fmt* into a *buffer* starting at *offset*. *offset* may be negative to count from the end of *buffer*.

unpack(fmt, data)

Unpack from the *data* according to the format string *fmt*. The return value is a tuple of the unpacked values.

unpack_from(fmt, data, offset=0, /)

Unpack from the *data* starting at *offset* according to the format string *fmt*. *offset* may be negative to count from the end of *data*. The return value is a tuple of the unpacked values.
