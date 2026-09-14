---
title: ArrayIterator::offsetUnset
description: Borra el valor de una posición
source_url: https://www.php.net/manual/es/arrayiterator.offsetunset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayiterator/offsetunset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: d51166ca1
order: 81250
---

ArrayIterator::offsetUnset

Borra el valor de una posición

## Descripción

```php
public ArrayIterator::offsetUnset(mixed $key): void
```php

Borra el valor de una posición.

Si una iteración está en curso, y ArrayIterator::offsetUnset se utiliza para unset el índice actual de la iteración, la posición de la iteración será avanzada al próximo índice. Como la posición de la iteración también se avanza al final de la declaración de bucle [`foreach`](#control-structures.foreach), el uso de ArrayIterator::offsetUnset dentro de un bucle [`foreach`](#control-structures.foreach) puede resultar en índices que serán omitidos.

## Parámetros

`key`  
La posición a borrar.

## Valores devueltos

No se retorna ningún valor.

## Véase también

ArrayIterator::offsetGet, ArrayIterator::offsetSet
