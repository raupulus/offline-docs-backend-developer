---
title: Iteradores
source_url: https://www.php.net/manual/es/spl.iterators.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/iterators.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: e93feee28
order: 82500
---

## Iteradores

SPL provee un conjunto de iteradores para recorrer objetos.

## Árbol de las Clases de Iteradores de SPL

- `ArrayIterator`

  - `RecursiveArrayIterator`

- `EmptyIterator`

- `IteratorIterator`

  - `AppendIterator`

  - `CachingIterator`

    - `RecursiveCachingIterator`

  - `FilterIterator`

    - `CallbackFilterIterator`

      - `RecursiveCallbackFilterIterator`

    - `RecursiveFilterIterator`

      - `ParentIterator`

    - `RegexIterator`

      - `RecursiveRegexIterator`

  - `InfiniteIterator`

  - `LimitIterator`

  - `NoRewindIterator`

- `MultipleIterator`

- `RecursiveIteratorIterator`

  - `RecursiveTreeIterator`

- `DirectoryIterator` (extends `SplFileInfo`)

  - `FilesystemIterator`

    - `GlobIterator`

    - `RecursiveDirectoryIterator`
