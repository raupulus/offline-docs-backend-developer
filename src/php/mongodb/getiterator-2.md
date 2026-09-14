---
title: MongoDB\BSON\PackedArray::getIterator
description: Devuelve el iterador para el array BSON
source_url: https://www.php.net/manual/es/mongodb-bson-packedarray.getiterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/packedarray/getiterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48140
---

MongoDB\BSON\PackedArray::getIterator

Devuelve el iterador para el array BSON

## Descripción

```php
final public MongoDB\BSON\PackedArray::getIterator(): MongoDB\BSON\Iterator
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una instancia de `MongoDB\BSON\Iterator` que puede ser utilizada para iterar sobre todos los índices del array.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una

MongoDB\Driver\Exception\UnexpectedValueException

si el iterador BSON no puede ser instanciado.

## Véase también

Tipos BSON
