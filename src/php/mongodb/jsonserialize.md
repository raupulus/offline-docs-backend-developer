---
title: MongoDB\BSON\Binary::jsonSerialize
description: Devuelve una representación que puede ser convertida en JSON
source_url: https://www.php.net/manual/es/mongodb-bson-binary.jsonserialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/binary/jsonserialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 47390
---

MongoDB\BSON\Binary::jsonSerialize

Devuelve una representación que puede ser convertida en JSON

## Descripción

```php
final public MongoDB\BSON\Binary::jsonSerialize(): mixed
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve datos que pueden ser serializados por `json_encode` para producir una representación JSON extendida de `MongoDB\BSON\Binary`.

> [!NOTE]
> La salida es coherente con la función `MongoDB\BSON\toJSON` , que utiliza el formato JSON extendido específico del controlador. Esto no corresponde necesariamente a las representaciones JSON extendidas [relajadas](https://github.com/mongodb/specifications/blob/master/source/extended-json/extended-json.md#relaxed-extended-json-example) o [canónicas](https://github.com/mongodb/specifications/blob/master/source/extended-json/extended-json.md#canonical-extended-json-example) utilizadas por `MongoDB\BSON\toRelaxedExtendedJSON` y `MongoDB\BSON\toCanonicalExtendedJSON`, respectivamente.

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
