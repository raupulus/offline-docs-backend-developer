---
title: LimitIterator::seek
description: Coloca el iterador en una posición dada
source_url: https://www.php.net/manual/es/limititerator.seek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/limititerator/seek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: d51166ca1
order: 82580
---

LimitIterator::seek

Coloca el iterador en una posición dada

## Descripción

```php
public LimitIterator::seek(int $offset): int
```php

Mueve el iterador interno a la posición `offset`.

## Parámetros

`offset`  
La posición en la que se desea situar.

## Valores devueltos

Devuelve la posición después del desplazamiento.

## Errores/Excepciones

Envía una `OutOfBoundsException` si la posición está fuera de los límites indicados en LimitIterator::\_\_construct.

## Véase también

LimitIterator::current, LimitIterator::key, LimitIterator::rewind, LimitIterator::next, LimitIterator::valid
