---
title: ArrayIterator::seek
description: Avance a una posición dada
source_url: https://www.php.net/manual/es/arrayiterator.seek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayiterator/seek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: 434557c58
order: 81270
---

ArrayIterator::seek

Avance a una posición dada

## Descripción

```php
public ArrayIterator::seek(int $offset): void
```php

Avance a una posición dada en el iterador.

## Parámetros

`offset`  
La posición deseada.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Levanta una excepción `OutOfBoundsException` si el `offset` no es accesible.
