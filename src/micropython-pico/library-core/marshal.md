---
title: '`marshal`'
description: Python object serialization
source_url: https://docs.micropython.org/en/latest/library/marshal.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/marshal.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 480
---

# `marshal` -- Python object serialization

marshal

\|see_cpython_module\| `python:marshal`.

This module implements conversion between Python objects and a binary format. The format is specific to MicroPython but does not depend on the machine architecture, so the data can be transferred and used on a different MicroPython instance, as long as the version of the binary data matches (it's currently versioned as the mpy file version, see `mpy_files`).

## Functions

dumps(value, /)

Convert the given *value* to binary format and return a corresponding `bytes` object.

Currently, code objects are the only supported values that can be converted.

loads(data, /)

Convert the given bytes-like *data* to its corresponding Python object, and return it.
