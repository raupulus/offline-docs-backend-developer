---
title: '`heapq`'
description: heap queue algorithm
source_url: https://docs.micropython.org/en/latest/library/heapq.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/heapq.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 200
---

# `heapq` -- heap queue algorithm

heapq

\|see_cpython_module\| `python:heapq`.

This module implements the [min heap queue algorithm](https://en.wikipedia.org/wiki/Heap_%28data_structure%29).

A heap queue is essentially a list that has its elements stored in such a way that the first item of the list is always the smallest.

## Functions

heappush(heap, item)

Push the `item` onto the `heap`.

heappop(heap)

Pop the first item from the `heap`, and return it. Raise `IndexError` if `heap` is empty.

The returned item will be the smallest item in the `heap`.

heapify(x)

Convert the list `x` into a heap. This is an in-place operation.
