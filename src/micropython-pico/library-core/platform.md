---
title: '`platform`'
description: access to underlying platform’s identifying data
source_url: https://docs.micropython.org/en/latest/library/platform.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/platform.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 630
---

# `platform` -- access to underlying platform’s identifying data

platform

\|see_cpython_module\| `python:platform`.

This module tries to retrieve as much platform-identifying data as possible. It makes this information available via function APIs.

## Functions

platform()

Returns a string identifying the underlying platform. This string is composed of several substrings in the following order, delimited by dashes (`-`):

- the name of the platform system (e.g. Unix, Windows or MicroPython)
- the MicroPython version
- the architecture of the platform
- the version of the underlying platform
- the concatenation of the name of the libc that MicroPython is linked to and its corresponding version.

For example, this could be `"MicroPython-1.20.0-xtensa-IDFv4.2.4-with-newlib3.0.0"`.

python_compiler()

Returns a string identifying the compiler used for compiling MicroPython.

libc_ver()

Returns a tuple of strings *(lib, version)*, where *lib* is the name of the libc that MicroPython is linked to, and *version* the corresponding version of this libc.

processor()

Returns a string with a detailed name of the processor, if one is available. If no name for the processor is known, it will return an empty string instead.

This is currently available only on RISC-V targets (both 32 and 64 bits).
