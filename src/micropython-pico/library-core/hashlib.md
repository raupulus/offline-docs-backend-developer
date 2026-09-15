---
title: '`hashlib`'
description: hashing algorithms
source_url: https://docs.micropython.org/en/latest/library/hashlib.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/hashlib.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 190
---

# `hashlib` -- hashing algorithms

hashlib

\|see_cpython_module\| `python:hashlib`.

This module implements binary data hashing algorithms. The exact inventory of available algorithms depends on a board. Among the algorithms which may be implemented:

- SHA256 - The current generation, modern hashing algorithm (of SHA2 series). It is suitable for cryptographically-secure purposes. Included in the MicroPython core and any board is recommended to provide this, unless it has particular code size constraints.
- SHA1 - A previous generation algorithm. Not recommended for new usages, but SHA1 is a part of number of Internet standards and existing applications, so boards targeting network connectivity and interoperability will try to provide this.
- MD5 - A legacy algorithm, not considered cryptographically secure. Only selected boards, targeting interoperability with legacy applications, will offer this.

## Constructors

Create an SHA256 hasher object and optionally feed `data` into it.

Create an SHA1 hasher object and optionally feed `data` into it.

Create an MD5 hasher object and optionally feed `data` into it.

## Methods

hash.update(data)

Feed more binary data into hash.

hash.digest()

Return hash for all data passed through hash, as a bytes object. After this method is called, more data cannot be fed into the hash any longer.

hash.hexdigest()

This method is NOT implemented. Use `binascii.hexlify(hash.digest())` to achieve a similar effect.
