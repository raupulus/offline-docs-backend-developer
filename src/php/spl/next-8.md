---
title: InfiniteIterator::next
description: Mueve el iterador interno hacía adelante o se rebobina
source_url: https://www.php.net/manual/es/infiniteiterator.next.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/infiniteiterator/next.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 82380
---

InfiniteIterator::next

Mueve el iterador interno hacía adelante o se rebobina

## Descripción

```php
public InfiniteIterator::next(): void
```php

Mueve el elemento del `Iterator` interno al siguiente elemento si hay alguno, en caso contrario rebobina el `Iterator` interno hasta el inicio.

> [!NOTE]
> Incluso un `InfiniteIterator` se detiene si un `Iterator` está vacío.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Véase también

InfiniteIterator::\_\_construct
