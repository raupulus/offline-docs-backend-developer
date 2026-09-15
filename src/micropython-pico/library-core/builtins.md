---
title: '`builtins`'
description: builtin functions and exceptions
source_url: https://docs.micropython.org/en/latest/library/builtins.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/builtins.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 70
---

# `builtins` -- builtin functions and exceptions

All builtin functions and exceptions are described here. They are also available via `builtins` module.

## Functions and types

abs()

all()

any()

bin()

\|see_cpython\| `python:bytearray`.

\|see_cpython\| `python:bytes`.

bytes.decode(encoding='utf-8', errors='strict')

Decode the bytes object to a string using the specified *encoding*.

MicroPython supports the following encodings:

- `'utf-8'` or `'utf8'` - UTF-8 encoding (default)
- `'ascii'` - ASCII encoding (subset of UTF-8)

The *errors* parameter controls how decoding errors are handled:

- `'strict'` - Raise a `UnicodeError` on invalid UTF-8 (default)
- `'ignore'` - Skip invalid bytes (requires `MICROPY_PY_BUILTINS_BYTES_DECODE_ERRORS`)
- `'replace'` - Replace invalid bytes with U+FFFD '�' (requires `MICROPY_PY_BUILTINS_BYTES_DECODE_ERRORS`)

> [!NOTE]
> Error handler support depends on build configuration. On constrained systems, only `'strict'` mode may be available.

Example:

    >>> b'\xc2\xa9 2024'.decode('utf-8')  # © symbol
    '© 2024'
    >>> b'hello\xffworld'.decode('utf-8', 'ignore')  # Skip invalid bytes
    'helloworld'

Raises `LookupError` if the encoding is not supported, or `UnicodeError` if the data contains invalid UTF-8 and `errors='strict'`.

callable()

chr()

classmethod()

compile()

delattr(obj, name)

The argument *name* should be a string, and this function deletes the named attribute from the object given by *obj*.

dir()

divmod()

enumerate()

eval()

exec()

filter()

getattr()

globals()

hasattr()

hash()

hex()

id()

input()

from_bytes(bytes, byteorder)

In MicroPython, `byteorder` parameter must be positional (this is compatible with CPython).

to_bytes(size, byteorder, /, \*, signed=False)

In MicroPython, `byteorder` parameter must be positional (this is compatible with CPython).

isinstance()

issubclass()

iter()

len()

locals()

map()

max()

\|see_cpython\| `python:memoryview`.

min()

next()

oct()

open()

ord()

pow()

print()

property()

range()

repr()

reversed()

round()

setattr()

The *slice* builtin is the type that slice objects have.

sorted()

staticmethod()

str.encode(encoding='utf-8')

Encode the string to bytes using the specified *encoding*.

MicroPython supports the following encodings:

- `'utf-8'` or `'utf8'` - UTF-8 encoding (default)
- `'ascii'` - ASCII encoding (subset of UTF-8)

Example:

    >>> '© 2024'.encode('utf-8')  # Copyright symbol
    b'\xc2\xa9 2024'

Raises `LookupError` if the encoding is not supported.

str.center(width)

Return a centered string of length *width*. Padding is done using spaces.

When Unicode support is enabled (`MICROPY_PY_BUILTINS_STR_UNICODE`), this method counts Unicode characters rather than bytes, ensuring proper alignment for multi-byte UTF-8 characters.

Example:

    >>> 'café'.center(10)  # é is 2 bytes in UTF-8
    '   café   '

sum()

super()

type()

zip()

## Exceptions

AssertionError

AttributeError

Exception

ImportError

IndexError

KeyboardInterrupt

\|see_cpython\| `python:KeyboardInterrupt`.

See also in the context of `soft_bricking`.

KeyError

MemoryError

NameError

NotImplementedError

OSError

RuntimeError

StopIteration

SyntaxError

SystemExit

\|see_cpython\| `python:SystemExit`.

On non-embedded ports (i.e. Windows and Unix), an unhandled `SystemExit` exits the MicroPython process in a similar way to CPython.

On embedded ports, an unhandled `SystemExit` currently causes a `soft_reset` of MicroPython.

TypeError

\|see_cpython\| `python:TypeError`.

ValueError

ZeroDivisionError
