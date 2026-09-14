---
title: La clase MongoDB\Driver\Exception\BulkWriteCommandException
source_url: https://www.php.net/manual/es/class.mongodb-driver-exception-bulkwritecommandexception.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/exception/bulkwritecommandexception.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49500
---

## Introducción

Excepción lanzada debido a la ejecución fallida de una `MongoDB\Driver\BulkWriteCommand`. Los métodos de esta clase proporcionan más detalles sobre el error que ocurrió, incluyendo la respuesta de error y los resultados parciales de la escritura masiva.

## Sinopsis de la clase

MongoDB\Driver\Exception\BulkWriteCommandException

MongoDB\Driver\Exception\BulkWriteCommandException

extends

MongoDB\Driver\Exception\ServerException

MongoDB\Driver\Exception\Exception

Propiedades

private

MongoDB\BSON\Document

null

errorReply

private

MongoDB\Driver\BulkWriteCommandResult

null

partialResult

private

array

writeConcernErrors

private

array

writeErrors

Propiedades heredadas

Métodos

Métodos heredados

## Propiedades

`errorReply`  
Cualquier error de nivel superior que ocurrió al intentar comunicarse con el servidor o ejecutar la escritura masiva. Este valor puede ser `null` si la excepción se lanzó debido a errores que ocurrieron en escrituras individuales.

`partialResult`  
Un `MongoDB\Driver\BulkWriteCommandResult` que informa sobre el resultado de cualquier operación exitosa que se realizó antes de que se encontrara el error. Este valor puede ser `null` si no se puede determinar que al menos una escritura se realizó con éxito (y fue confirmada).

`writeConcernErrors`  
Un array de cualquier `MongoDB\Driver\WriteConcernError` que ocurrió al ejecutar la escritura masiva. Esta lista puede tener múltiples elementos si se requirieron más de un comando de servidor para ejecutar la escritura masiva.

`writeErrors`  
Un array de cualquier `MongoDB\Driver\WriteError` que ocurrió durante la ejecución de operaciones de escritura individuales. Las claves del array corresponderán al índice de la operación de escritura de `MongoDB\Driver\BulkWriteCommand`. Este mapa contendrá como máximo una entrada si la escritura masiva estaba ordenada.
