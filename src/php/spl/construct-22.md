---
title: RecursiveTreeIterator::__construct
description: Construye un nuevo RecursiveTreeIterator
source_url: https://www.php.net/manual/es/recursivetreeiterator.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/recursivetreeiterator/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: c142be811
order: 83490
---

RecursiveTreeIterator::\_\_construct

Construye un nuevo RecursiveTreeIterator

## Descripción

```php
public RecursiveTreeIterator::__construct(RecursiveIterator $iterator, [int $flags], [int $cachingIteratorFlags], [int $mode])
```php

Construye un nuevo `RecursiveTreeIterator` desde un iterador recursivo suministrado.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`iterator`  
El `RecursiveIterator` o `IteratorAggregate` a iterar.

`flags`  
Se pueden proporcionar flags que afectarán el comportamiento de algunos métodos. Una lista de flags puede verse en [Constantes predefinidas RecursiveTreeIterator](#recursivetreeiterator.constants).

`caching_it_flags`  
Flags que afectan el comportamiento interno de `RecursiveCachingIterator`.

`mode`  
Flags que afectan el comportamiento interno de `RecursiveIteratorIterator`.
