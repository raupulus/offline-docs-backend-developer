---
title: La clase MongoDB\BSON\UTCDateTime
source_url: https://www.php.net/manual/es/class.mongodb-bson-utcdatetime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/utcdatetime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48650
---

## Introducción

Representa una [fecha BSON](https://www.mongodb.com/docs/manual/reference/bson-types/#date). El valor es un entero de 64 bits que representa el número de milisegundos transcurridos desde la época Unix (1 de enero de 1970). Los valores negativos representan fechas anteriores a 1970.

## Sinopsis de la clase

MongoDB\BSON\UTCDateTime

final

MongoDB\BSON\UTCDateTime

MongoDB\BSON\UTCDateTimeInterface

MongoDB\BSON\Type

JsonSerializable

Stringable

Métodos

## Historial de cambios

| Versión             | Descripción                                           |
|---------------------|-------------------------------------------------------|
| PECL mongodb 2.0.0  | Esta clase ya no implementa la interfaz Serializable. |
| PECL mongodb 1.12.0 | Implementa Stringable para PHP 8.0+.                  |
| PECL mongodb 1.3.0  | Implementa MongoDB\BSON\UTCDateTimeInterface.         |
| PECL mongodb 1.2.0  | Implementa Serializable y JsonSerializable.           |
