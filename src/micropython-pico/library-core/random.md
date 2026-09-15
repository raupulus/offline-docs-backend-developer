---
title: '`random`'
description: generate random numbers
source_url: https://docs.micropython.org/en/latest/library/random.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/random.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 830
---

# `random` -- generate random numbers

random

This module implements a pseudo-random number generator (PRNG).

\|see_cpython_module\| `python:random` .

> [!NOTE]
> The following notation is used for intervals:
>
> - () are open interval brackets and do not include their endpoints. For example, (0, 1) means greater than 0 and less than 1. In set notation: (0, 1) = {x \| 0 \< x \< 1}.
> - \[\] are closed interval brackets which include all their limit points. For example, \[0, 1\] means greater than or equal to 0 and less than or equal to 1. In set notation: \[0, 1\] = {x \| 0 \<= x \<= 1}.

> [!NOTE]
> The `randrange`, `randint` and `choice` functions are only available if the `MICROPY_PY_RANDOM_EXTRA_FUNCS` configuration option is enabled.

## Functions for integers

getrandbits(n)

Return an integer with *n* random bits (0 \<= n \<= 32).

randint(a, b)

Return a random integer in the range \[*a*, *b*\].

randrange(stop) randrange(start, stop) randrange(start, stop\[, step\])

The first form returns a random integer from the range \[0, *stop*). The second form returns a random integer from the range \[*start*, *stop*). The third form returns a random integer from the range \[*start*, *stop*) in steps of *step*. For instance, calling `randrange(1, 10, 2)` will return odd numbers between 1 and 9 inclusive.

## Functions for floats

random()

Return a random floating point number in the range \[0.0, 1.0).

uniform(a, b)

Return a random floating point number N such that *a* \<= N \<= *b* for *a* \<= *b*, and *b* \<= N \<= *a* for *b* \< *a*.

## Other Functions

seed(n=None, /)

Initialise the random number generator module with the seed *n* which should be an integer. When no argument (or `None`) is passed in it will (if supported by the port) initialise the PRNG with a true random number (usually a hardware generated random number).

The `None` case only works if `MICROPY_PY_RANDOM_SEED_INIT_FUNC` is enabled by the port, otherwise it raises `ValueError`.

choice(sequence)

Chooses and returns one item at random from *sequence* (tuple, list or any object that supports the subscript operation).
