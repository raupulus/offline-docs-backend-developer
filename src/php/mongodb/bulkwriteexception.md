---
title: La clase MongoDB\Driver\Exception\BulkWriteException
source_url: https://www.php.net/manual/es/class.mongodb-driver-exception-bulkwriteexception.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/exception/bulkwriteexception.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 36c32a2a9
order: 49520
---

## Introducción

Se levanta cuando una operación de escritura en bloque falla.

## Sinopsis de la clase

MongoDB\Driver\Exception\BulkWriteException

final

MongoDB\Driver\Exception\BulkWriteException

extends

MongoDB\Driver\Exception\ServerException

MongoDB\Driver\Exception\Exception

Propiedades

public

readonly

MongoDB\Driver\WriteResult

writeResult

Propiedades heredadas

Métodos

Métodos heredados

## Propiedades

`writeResult`  
El `MongoDB\Driver\WriteResult` asociado a la operación de escritura fallida.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 2.3.0 | La propiedad `writeResult` ahora es public readonly. |
| PECL mongodb 2.0.0 | Esta clase extiende ahora `MongoDB\Driver\Exception\ServerException` en lugar de `MongoDB\Driver\Exception\WriteException`. |
