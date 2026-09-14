---
title: MongoDB\BSON\Binary::toArray
description: Devuelve el vector como un array para un Binary con subtipo MongoDB\BSON\Binary::SUBTYPE_VECTOR
source_url: https://www.php.net/manual/es/mongodb-bson-binary.toarray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/binary/toarray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_revision: 9f4cb232d
order: 47400
---

MongoDB\BSON\Binary::toArray

Devuelve el vector como un array para un Binary con subtipo

MongoDB\BSON\Binary::SUBTYPE_VECTOR

## Descripción

```php
final public MongoDB\BSON\Binary::toArray(): array
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array que contiene los datos del vector.

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

MongoDB\BSON\Binary::fromVector

BSON Types
