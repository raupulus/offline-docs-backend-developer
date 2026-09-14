---
title: La clase MongoDB\Driver\WriteResult
source_url: https://www.php.net/manual/es/class.mongodb-driver-writeresult.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/writeresult.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 36c32a2a9
order: 51720
---

## Introducción

La clase `MongoDB\Driver\WriteResult` contiene las informaciones sobre una ejecución `MongoDB\Driver\BulkWrite` y puede ser retornado por MongoDB\Driver\Manager::executeBulkWrite.

## Sinopsis de la clase

MongoDB\Driver\WriteResult

final

MongoDB\Driver\WriteResult

Propiedades

public

readonly

int

null

insertedCount

public

readonly

int

null

matchedCount

public

readonly

int

null

modifiedCount

public

readonly

int

null

deletedCount

public

readonly

int

null

upsertedCount

public

readonly

MongoDB\Driver\Server

server

public

readonly

array

upsertedIds

public

readonly

array

writeErrors

public

readonly

MongoDB\Driver\WriteConcernError

null

writeConcernError

public

readonly

MongoDB\Driver\WriteConcern

null

writeConcern

public

readonly

array

errorReplies

Métodos

## Propiedades

`insertedCount`  
El número de documentos insertados (excluyendo los upserts), o `null` si el write concern no ha solicitado acuse de recibo.

`matchedCount`  
El número de documentos coincidentes con las operaciones de actualización y reemplazo, o `null` si el write concern no ha solicitado acuse de recibo.

`modifiedCount`  
El número de documentos modificados por las operaciones de actualización y reemplazo, o `null` si el write concern no ha solicitado acuse de recibo o si el servidor no ha proporcionado esta información.

`deletedCount`  
El número de documentos eliminados, o `null` si el write concern no ha solicitado acuse de recibo.

`upsertedCount`  
El número de documentos upserted, o `null` si el write concern no ha solicitado acuse de recibo.

`server`  
El servidor que ha ejecutado el bulk write.

`upsertedIds`  
Un array de valores `_id` para los documentos upserted. Las claves del array corresponden al índice de la operación de escritura de `MongoDB\Driver\BulkWrite`.

`writeErrors`  
Un array de `MongoDB\Driver\WriteError` para los errores de escritura producidos durante la ejecución.

`writeConcernError`  
El `MongoDB\Driver\WriteConcernError` que ha ocurrido, o `null` si no ha ocurrido ningún error de write concern.

`writeConcern`  
El `MongoDB\Driver\WriteConcern` utilizado para el bulk write, o `null` si no está disponible.

`errorReplies`  
Un array de documentos de respuesta de error procedentes del servidor.

## Historial de cambios

| Versión            | Descripción                                        |
|--------------------|----------------------------------------------------|
| PECL mongodb 2.3.0 | Las propiedades public readonly han sido añadidas. |
