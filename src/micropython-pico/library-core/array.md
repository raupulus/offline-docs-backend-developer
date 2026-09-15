---
title: '`array`'
description: arrays of numeric data
source_url: https://docs.micropython.org/en/latest/library/array.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/array.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 20
---

# `array` -- arrays of numeric data

array

\|see_cpython_module\| `python:array`.

Supported format codes: `b`, `B`, `h`, `H`, `i`, `I`, `l`, `L`, `q`, `Q`, `f`, `d` (the latter 2 depending on the floating-point support).

## Classes

Create array with elements of given type. Initial contents of the array are given by *iterable*. If it is not provided, an empty array is created.

In addition to the methods below, array objects also implement the buffer protocol. This means the contents of the entire array can be accessed as raw bytes via a `memoryview` or other interfaces which use this protocol.

append(val)

Append new element *val* to the end of array, growing it.

extend(iterable)

Append new elements as contained in *iterable* to the end of array, growing it.

\_\_getitem\_\_(index)

Indexed read of the array, called as `a[index]` (where `a` is an `array`). Returns a value if *index* is an `int` and an `array` if *index* is a slice. Negative indices count from the end and `IndexError` is thrown if the index is out of range.

**Note:** `__getitem__` cannot be called directly (`a.__getitem__(index)` fails) and is not present in `__dict__`, however `a[index]` does work.

\_\_setitem\_\_(index, value)

Indexed write into the array, called as `a[index] = value` (where `a` is an `array`). `value` is a single value if *index* is an `int` and an `array` if *index* is a slice. Negative indices count from the end and `IndexError` is thrown if the index is out of range.

**Note:** `__setitem__` cannot be called directly (`a.__setitem__(index, value)` fails) and is not present in `__dict__`, however `a[index] = value` does work.

\_\_len\_\_()

Returns the number of items in the array, called as `len(a)` (where `a` is an `array`).

**Note:** `__len__` cannot be called directly (`a.__len__()` fails) and the method is not present in `__dict__`, however `len(a)` does work.

\_\_add\_\_(other)

Return a new `array` that is the concatenation of the array with *other*, called as `a + other` (where `a` and *other* are both `arrays`).

**Note:** `__add__` cannot be called directly (`a.__add__(other)` fails) and is not present in `__dict__`, however `a + other` does work.

\_\_iadd\_\_(other)

Concatenates the array with *other* in-place, called as `a += other` (where `a` and *other* are both `arrays`). Equivalent to `extend(other)`.

**Note:** `__iadd__` cannot be called directly (`a.__iadd__(other)` fails) and is not present in `__dict__`, however `a += other` does work.

\_\_repr\_\_()

Returns the string representation of the array, called as `str(a)` or `repr(a)`` (where ``a`` is an ``array``). Returns the string ``"array(\<type\>, \[\<elements\>\])"``, where ``\<type\>`` is the type code letter for the array and ``\<elements\>`\` is a comma separated list of the elements of the array.

**Note:** `__repr__` cannot be called directly (`a.__repr__()` fails) and is not present in `__dict__`, however `str(a)` and `repr(a)` both work.
