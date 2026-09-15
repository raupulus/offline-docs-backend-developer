---
title: '`weakref`'
description: Python object lifetime management
source_url: https://docs.micropython.org/en/latest/library/weakref.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/weakref.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 1000
---

# `weakref` -- Python object lifetime management

weakref

\|see_cpython_module\| `python:weakref`.

This module allows creation of weak references to Python objects. A weak reference is a non-traceable reference to a heap-allocated Python object, so the garbage collector can still reclaim the object even though the weak reference refers to it.

Python callbacks can be registered to be called when an object is reclaimed by the garbage collector. This provides a safe way to clean up when objects are no longer needed.

**Availability:** the weakref module requires `MICROPY_PY_WEAKREF` to be enabled at compile time. It is enabled on the unix coverage variant and the webassembly pyscript variant.

## ref objects

A ref object is the simplest way to make a weak reference.

Return a weak reference to the given *object*.

If *callback* is given and is not `None` then, when *object* is reclaimed by the garbage collector and if the weak reference object is still alive, the *callback* will be called. The *callback* will be passed the weak reference object as its single argument.

ref.\_\_call\_\_()

Calling the weak reference object will return its referenced object if that object is still alive. Otherwise `None` will be returned.

## finalize objects

A finalize object is an extended version of a ref object that is more convenient to use, and allows more control over the callback.

Return a weak reference to the given *object*. In contrast to *weakref.ref* objects, finalize objects are held onto internally and will not be collected until *object* is collected.

A finalize object starts off alive. It transitions to the dead state when the finalize object is called, either explicitly or when *object* is collected. It also transitions to dead if the `finalize.detach()` method is called.

When *object* is reclaimed by the garbage collector (or the finalize object is explicitly called by user code) and the finalize object is still in the alive state, the *callback* will be called. The *callback* will be passed arguments as: `callback(*args, **kwargs)`.

finalize.\_\_call\_\_()

If the finalize object is alive then it transitions to the dead state and returns the value of `callback(*args, **kwargs)`. Otherwise `None` will be returned.

finalize.alive

Read-only boolean attribute that indicates if the finalizer is in the alive state.

finalize.peek()

If the finalize object is alive then return `(object, callback, args, kwargs)`. Otherwise return `None`.

finalize.detach()

If the finalize object is alive then it transitions to the dead state and returns `(object, callback, args, kwargs)`. Otherwise `None` will be returned.
