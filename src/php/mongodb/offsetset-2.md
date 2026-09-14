---
title: MongoDB\BSON\PackedArray::offsetSet
description: Implementación de ArrayAccess
source_url: https://www.php.net/manual/es/mongodb-bson-packedarray.offsetset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/packedarray/offsetset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48180
---

MongoDB\BSON\PackedArray::offsetSet

Implementación de

ArrayAccess

## Descripción

```php
final public MongoDB\BSON\PackedArray::offsetSet(mixed $key, mixed $value): void
```php

Cambia el valor de `key` a `value`.

## Parámetros

`key`  
El índice a modificar.

`value`  
El nuevo valor de `key`.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Siempre lanza una

MongoDB\Driver\Exception\LogicException

.
