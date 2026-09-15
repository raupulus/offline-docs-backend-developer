---
title: '`json`'
description: JSON encoding and decoding
source_url: https://docs.micropython.org/en/latest/library/json.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/json.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 230
---

# `json` -- JSON encoding and decoding

json

\|see_cpython_module\| `python:json`.

This modules allows to convert between Python objects and the JSON data format.

## Functions

dump(obj, stream, separators=None)

Serialise *obj* to a JSON string, writing it to the given *stream*.

If specified, separators should be an `(item_separator, key_separator)` tuple. The default is `(', ', ': ')`. To get the most compact JSON representation, you should specify `(',', ':')` to eliminate whitespace.

dumps(obj, separators=None)

Return *obj* represented as a JSON string.

The arguments have the same meaning as in `dump`.

load(stream)

Parse the given *stream*, interpreting it as a JSON string and deserialising the data to a Python object. The resulting object is returned.

Parsing continues until end-of-file is encountered. A `ValueError` is raised if the data in *stream* is not correctly formed.

loads(str)

Parse the JSON *str* and return an object. Raises `ValueError` if the string is not correctly formed.
