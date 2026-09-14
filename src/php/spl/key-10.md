---
title: MultipleIterator::key
description: Recupera las instancias de los iteradores registrados
source_url: https://www.php.net/manual/es/multipleiterator.key.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/multipleiterator/key.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 82690
---

MultipleIterator::key

Recupera las instancias de los iteradores registrados

## Descripción

```php
public MultipleIterator::key(): array
```php

Recupera las claves de las instancias de los iteradores registrados.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array de todos los iteradores registrados.

## Errores/Excepciones

Una excepción `RuntimeException` si el iterador es inválido (a partir de PHP 8.1.0), o el modo `MIT_NEED_ALL` está definido y al menos un iterador inválido.

La llamada a este método desde [???](#control-structures.foreach) provoca una advertencia de tipo "Illegal type returned".

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Una `RuntimeException` es lanzada cuando MultipleIterator::key es llamado sobre un iterador inválido. Anteriormente, `false` era devuelto. |

## Véase también

MultipleIterator::current
