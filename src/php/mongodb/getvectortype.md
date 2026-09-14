---
title: MongoDB\BSON\Binary::getVectorType
description: Devuelve el tipo de datos para un Binary con el subtipo vector
source_url: https://www.php.net/manual/es/mongodb-bson-binary.getvectortype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/binary/getvectortype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_revision: 9f4cb232d
order: 47380
---

MongoDB\BSON\Binary::getVectorType

Devuelve el tipo de datos para un Binary con el subtipo vector

## Descripción

```php
final public MongoDB\BSON\Binary::getVectorType(): MongoDB\BSON\VectorType
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el tipo de datos del vector Binary.

## Errores/Excepciones

Lanza

MongoDB\Driver\Exception\LogicException

si el subtipo no es

MongoDB\BSON\Binary::SUBTYPE_VECTOR

.

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

BSON Types

MongoDB\BSON\VectorType
