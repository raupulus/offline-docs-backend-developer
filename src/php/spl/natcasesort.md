---
title: ArrayIterator::natcasesort
description: Ordena naturalmente las entradas, sin tener en cuenta la casilla
source_url: https://www.php.net/manual/es/arrayiterator.natcasesort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayiterator/natcasesort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 2ca090342
order: 81190
---

ArrayIterator::natcasesort

Ordena naturalmente las entradas, sin tener en cuenta la casilla

## Descripción

```php
public ArrayIterator::natcasesort(): true
```php

Ordena las entradas por los valores, utilizando un algoritmo insensible a la casilla de orden natural.

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

ArrayIterator::asort, ArrayIterator::ksort, ArrayIterator::natsort, ArrayIterator::uasort, ArrayIterator::uksort, `natcasesort`
