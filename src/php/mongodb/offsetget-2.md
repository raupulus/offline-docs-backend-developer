---
title: MongoDB\BSON\PackedArray::offsetGet
description: Devuelve el valor de un índice del array
source_url: https://www.php.net/manual/es/mongodb-bson-packedarray.offsetget.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/packedarray/offsetget.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48170
---

MongoDB\BSON\PackedArray::offsetGet

Devuelve el valor de un índice del array

## Descripción

```php
final public MongoDB\BSON\PackedArray::offsetGet(mixed $key): mixed
```php

## Parámetros

`key`  
El índice a recuperar del array. Solo `int` es soportado.

## Valores devueltos

Devuelve el valor asociado al índice dado. Si el índice no está presente en el array, se lanza una excepción.

> [!NOTE]
> Cuando se encuentra un valor codificado como un entero de 64 bits en el array BSON, el valor de retorno de este método será una instancia de `MongoDB\BSON\Int64`.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una

MongoDB\Driver\Exception\RuntimeException

si el índice no está presente en el array.

## Véase también

ArrayAccess::offsetGet, MongoDB\BSON\PackedArray::get
