---
title: ArrayIterator::natsort
description: Ordena naturalmente las entradas
source_url: https://www.php.net/manual/es/arrayiterator.natsort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayiterator/natsort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 56b048277
order: 81200
---

ArrayIterator::natsort

Ordena naturalmente las entradas

## Descripción

```php
public ArrayIterator::natsort(): true
```php

Ordena las entradas por los valores, utilizando el algoritmo de orden natural.

> [!NOTE]
> Si dos miembros se comparan como iguales, mantienen su orden original. Anterior a PHP 8.0.0, su orden relativo en el array ordenado no está definido.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.2.0   | El tipo de retorno es ahora `true`, anteriormente era `bool`. |

## Véase también

ArrayIterator::asort, ArrayIterator::ksort, ArrayIterator::natcasesort, ArrayIterator::uasort, ArrayIterator::uksort, `natsort`
