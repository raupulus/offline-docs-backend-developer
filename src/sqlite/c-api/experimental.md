---
title: Experimental Interfaces
source_url: https://www.sqlite.org/c3ref/experimental.html
source_path: c3ref/experimental.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: c-api
order: 1220
---

[](../c3ref/intro.md)

## SQLite C Interface

## Experimental And Deprecated Interfaces

SQLite interfaces can be subdivided into three categories:

1.  Stable
2.  Experimental
3.  Deprecated

Stable interfaces will be maintained indefinitely in a backwards compatible way. An application that uses only stable interfaces should always be able to relink against a newer version of SQLite without any changes.

Experimental interfaces are subject to change. Applications that use experimental interfaces may need to be modified when upgrading to a newer SQLite release, though this is rare. When new interfaces are added to SQLite, they generally begin as experimental interfaces. After an interface has been in use for a while and the developers are confident that the design of the interface is sound and worthy of long-term support, the interface is marked as stable.

Deprecated interfaces have been superseded by better methods of accomplishing the same thing and should be avoided in new applications. Deprecated interfaces continue to be supported for the sake of backwards compatibility. At some point in the future, it is possible that deprecated interfaces may be removed.

Key points:

- Experimental interfaces are subject to change and/or removal at any time.
- Deprecated interfaces should not be used in new code and might be removed in some future release.
