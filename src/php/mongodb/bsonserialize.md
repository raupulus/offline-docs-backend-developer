---
title: MongoDB\BSON\Persistable::bsonSerialize
description: Proporciona un array o un documento a serializar como BSON
source_url: https://www.php.net/manual/es/mongodb-bson-persistable.bsonserialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/persistable/bsonserialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: true
translation_revision: 9f4cb232d
order: 48250
---

MongoDB\BSON\Persistable::bsonSerialize

Proporciona un array o un documento a serializar como BSON

## Descripción

```php
abstract public MongoDB\BSON\Persistable::bsonSerialize(): array
```php

Se invoca durante la serialización del objeto en BSON. El método debe devolver un `array`, `stdClass`, o `MongoDB\BSON\Document`.

El valor devuelto será siempre serializado como documento BSON. El documento serializado incluirá un campo que contiene el nombre de la clase del objeto. Por esta razón, no es posible devolver una instancia de `MongoDB\BSON\PackedArray` en este método.

Se recomienda incluir una propiedad \_id (por ejemplo un `MongoDB\BSON\ObjectId` inicializado en el constructor) al devolver datos para un documento BSON raíz. En ausencia de una propiedad \_id, la extensión o el servidor generará un `MongoDB\BSON\ObjectId` para las operaciones de inserción o upsert, respectivamente.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array`, `stdClass`, o `MongoDB\BSON\Document` a serializar como documento BSON.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 2.0.0 | Los tipos de retorno previamente declarados como provisionales ahora son aplicados. |
| PECL mongodb 1.17.0 | Este método puede ahora también devolver instancias de `MongoDB\BSON\Document` además de `array` y `stdClass`. |

## Véase también

MongoDB\BSON\Serializable::bsonSerialize

MongoDB\BSON\Unserializable::bsonUnserialize

MongoDB\BSON\Persistable
