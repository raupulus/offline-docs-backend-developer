---
title: MongoDB\Driver\ServerApi::bsonSerialize
description: Devuelve un objeto para la serialización BSON
source_url: https://www.php.net/manual/es/mongodb-driver-serverapi.bsonserialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/serverapi/bsonserialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51150
---

MongoDB\Driver\ServerApi::bsonSerialize

Devuelve un objeto para la serialización BSON

## Descripción

```php
final public MongoDB\Driver\ServerApi::bsonSerialize(): stdClass
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un objeto para la serialización del ServerApi en BSON.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\BSON\Serializable::bsonSerialize
