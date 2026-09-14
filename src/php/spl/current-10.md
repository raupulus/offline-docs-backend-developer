---
title: MultipleIterator::current
description: Recupera las instancias de los iteradores adjuntos
source_url: https://www.php.net/manual/es/multipleiterator.current.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/multipleiterator/current.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 82660
---

MultipleIterator::current

Recupera las instancias de los iteradores adjuntos

## Descripción

```php
public MultipleIterator::current(): array
```php

Recupera las instancias actuales de los iteradores adjuntos.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array que contiene los valores actuales de cada iterador adjunto.

## Errores/Excepciones

Una excepción `RuntimeException` si el iterador es inválido (a partir de PHP 8.1.0), o el modo `MIT_NEED_ALL` está definido y al menos un iterador inválido. O una excepción `IllegalValueException` si una clave es `null` y el modo `MIT_KEYS_ASSOC` está definido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Una `RuntimeException` es ahora lanzada cuando MultipleIterator::current es llamado sobre un iterador inválido. Anteriormente, `false` era devuelto. |

## Véase también

MultipleIterator::valid
