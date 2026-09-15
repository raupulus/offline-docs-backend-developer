---
title: '`errno`'
description: system error codes
source_url: https://docs.micropython.org/en/latest/library/errno.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/errno.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 120
---

# `errno` -- system error codes

errno

\|see_cpython_module\| `python:errno`.

This module provides access to symbolic error codes for `OSError` exception. A particular inventory of codes depends on `MicroPython port`.

## Constants

EEXIST, EAGAIN, etc.

Error codes, based on ANSI C/POSIX standard. All error codes start with "E". As mentioned above, inventory of the codes depends on `MicroPython port`. Errors are usually accessible as `exc.errno` where `exc` is an instance of `OSError`. Usage example:

    try:
        os.mkdir("my_dir")
    except OSError as exc:
        if exc.errno == errno.EEXIST:
            print("Directory already exists")

errorcode

Dictionary mapping numeric error codes to strings with symbolic error code (see above):

    >>> print(errno.errorcode[errno.EEXIST])
    EEXIST
