---
title: 4. Construyendo extensiones C y C++
source_url: https://docs.python.org/es/3
source_path: extending/building.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: extending
order: 970
---

# 4. Construyendo extensiones C y C++

A C extension for CPython is a shared library (for example, a ".so"
file on Linux, ".pyd" on Windows), which exports an *initialization
function*.

See Defining extension modules for details.

## 4.1. Building C and C++ Extensions with setuptools

Building, packaging and distributing extension modules is best done
with third-party tools, and is out of scope of this document. One
suitable tool is Setuptools, whose documentation can be found at
https://setuptools.pypa.io/en/latest/setuptools.html.

The "distutils" module, which was included in the standard library
until Python 3.12, is now maintained as part of Setuptools.
