---
title: MongoDB\BSON\Int64::jsonSerialize
description: Devuelve una representación que puede ser convertida a JSON
source_url: https://www.php.net/manual/es/mongodb-bson-int64.jsonserialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/int64/jsonserialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47740
---

MongoDB\BSON\Int64::jsonSerialize

Devuelve una representación que puede ser convertida a JSON

## Descripción

```php
final public MongoDB\BSON\Int64::jsonSerialize(): mixed
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve datos que pueden ser serializados por `json_encode` para producir una representación JSON extendida de `MongoDB\BSON\Int64`.

> [!NOTE]
> La salida es concordante con la función `MongoDB\BSON\toCanonicalExtendedJSON`, que utiliza el formato JSON extendido [canonical](https://github.com/mongodb/specifications/blob/master/source/extended-json/extended-json.md#canonical-extended-json-example). Esto difiere de otras clases BDON, que utilizan el formato JSON extendido heredado del controlador específico (`MongoDB\BSON\toJSON`), para asegurar que los valores enteros de 64 bits sean correctamente representados en plataformas de 32 bits.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

JsonSerializable::jsonSerialize

json_encode

MongoDB\BSON\toCanonicalExtendedJSON

MongoDB\BSON\toRelaxedExtendedJSON

MongoDB JSON Extendido
