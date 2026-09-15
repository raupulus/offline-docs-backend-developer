---
title: '`cmath`'
description: mathematical functions for complex numbers
source_url: https://docs.micropython.org/en/latest/library/cmath.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/cmath.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 80
---

# `cmath` -- mathematical functions for complex numbers

cmath

\|see_cpython_module\| `python:cmath`.

The `cmath` module provides some basic mathematical functions for working with complex numbers.

Availability: not available on WiPy and ESP8266. Floating point support required for this module.

## Functions

cos(z)

Return the cosine of `z`.

exp(z)

Return the exponential of `z`.

log(z)

Return the natural logarithm of `z`. The branch cut is along the negative real axis.

log10(z)

Return the base-10 logarithm of `z`. The branch cut is along the negative real axis.

phase(z)

Returns the phase of the number `z`, in the range (-pi, +pi\].

polar(z)

Returns, as a tuple, the polar form of `z`.

rect(r, phi)

Returns the complex number with modulus `r` and phase `phi`.

sin(z)

Return the sine of `z`.

sqrt(z)

Return the square-root of `z`.

## Constants

e

base of the natural logarithm

pi

the ratio of a circle's circumference to its diameter
