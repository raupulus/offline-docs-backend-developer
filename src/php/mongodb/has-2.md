---
title: MongoDB\BSON\PackedArray::has
description: Indica si un índice está presente en el array
source_url: https://www.php.net/manual/es/mongodb-bson-packedarray.has.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/packedarray/has.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48150
---

MongoDB\BSON\PackedArray::has

Indica si un índice está presente en el array

## Descripción

```php
final public MongoDB\BSON\PackedArray::has(int $index): bool
```php

## Parámetros

`index` (`int`)  
El índice a buscar en el array.

## Valores devueltos

Devuelve `true` si el índice está presente en el array, de lo contrario `false`.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\BSON\PackedArray::get

Tipos BSON
