---
title: La clase MongoDB\Driver\Exception\WriteException
source_url: https://www.php.net/manual/es/class.mongodb-driver-exception-writeexception.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/exception/writeexception.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49680
---

> [!WARNING]
> Esta clase de excepción está *DEPRECADA* desde la versión 1.20.0 de la extensión y ha sido eliminada en la versión 2.0. Esta excepción nunca fue lanzada directamente por la extensión. Las aplicaciones deberían utilizar `MongoDB\Driver\Exception\BulkWriteException` en su lugar.

## Introducción

Clase base para las excepciones lanzadas por una operación de escritura fallida. La excepción encapsula un objeto `MongoDB\Driver\WriteResult`.

## Sinopsis de la clase

MongoDB\Driver\Exception\WriteException

abstract

MongoDB\Driver\Exception\WriteException

extends

MongoDB\Driver\Exception\ServerException

MongoDB\Driver\Exception\Exception

Propiedades

protected

MongoDB\Driver\WriteResult

writeResult

Propiedades heredadas

Métodos

Métodos heredados

## Propiedades

`writeResult`  
`MongoDB\Driver\WriteResult` asociado a la operación de escritura fallida.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 2.0.0 | Esta clase ha sido eliminada. |
| PECL mongodb 1.20.0 | Esta clase ha sido deprecada y será eliminada en la versión 2.0. |
| PECL mongodb 1.5.0 | Esta clase ahora extiende `MongoDB\Driver\Exception\ServerException` en lugar de `MongoDB\Driver\Exception\RuntimeException`. |
