---
title: La clase MongoDB\BSON\Timestamp
source_url: https://www.php.net/manual/es/class.mongodb-bson-timestamp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/timestamp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48480
---

## Introducción

Representa un [timestamp BSON](https://www.mongodb.com/docs/manual/reference/bson-types/#timestamps). El valor consiste en un timestamp de 4 bytes (es decir, segundos desde la época) y un incremento de 4 bytes.

> [!NOTE]
> Este es un tipo interno de MongoDB utilizado para replicación y particionamiento. No está destinado al almacenamiento general de fechas (debería usarse `MongoDB\BSON\UTCDateTime` en su lugar).

## Sinopsis de la clase

MongoDB\BSON\Timestamp

final

MongoDB\BSON\Timestamp

MongoDB\BSON\TimestampInterface

MongoDB\BSON\Type

JsonSerializable

Stringable

Métodos

## Historial de cambios

| Versión             | Descripción                                           |
|---------------------|-------------------------------------------------------|
| PECL mongodb 2.0.0  | Esta clase ya no implementa la interfaz Serializable. |
| PECL mongodb 1.12.0 | Implementa Stringable para PHP 8.0+.                  |
| PECL mongodb 1.3.0  | Implementa MongoDB\BSON\TimestampInterface.           |
| PECL mongodb 1.2.0  | Implementa Serializable y JsonSerializable.           |
