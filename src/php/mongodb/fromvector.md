---
title: MongoDB\BSON\Binary::fromVector
description: Crea un nuevo binario con subtipo MongoDB\BSON\Binary::SUBTYPE_VECTOR
  a partir del array y tipo de vector dados
source_url: https://www.php.net/manual/es/mongodb-bson-binary.fromvector.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/binary/fromvector.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_revision: 9f4cb232d
order: 47350
---

MongoDB\BSON\Binary::fromVector

Crea un nuevo binario con subtipo

MongoDB\BSON\Binary::SUBTYPE_VECTOR

a partir del array y tipo de vector dados

## Descripción

```php
final public static MongoDB\BSON\Binary::fromVector(array $vector, MongoDB\BSON\VectorType $vectorType): MongoDB\BSON\Binary
```php

## Parámetros

`vector` (`array`)  
Un array de valores que representa los datos del vector. El tipo de cada valor debe coincidir con el tipo indicado por el parámetro `vectorType`:

- para `MongoDB\BSON\VectorType::Float32`, cada valor debe ser un `float`

- para `MongoDB\BSON\VectorType::Int8`, cada valor debe ser un `int` de 8 bits, es decir, de `-127` a `128`

- para `MongoDB\BSON\VectorType::PackedBit`, cada valor debe ser un `bool` o un `int` de 1 bit, es decir, `0` o `1`

`vectorType` (`MongoDB\BSON\VectorType`)  
El tipo de datos del vector.

## Valores devueltos

Devuelve un nuevo Binary con subtipo `MongoDB\BSON\Binary::SUBTYPE_VECTOR`.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\BSON\Binary::toArray

MongoDB\BSON\Binary::getVectorType

MongoDB\BSON\VectorType

BSON Types
