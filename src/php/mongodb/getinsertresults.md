---
title: MongoDB\Driver\BulkWriteCommandResult::getInsertResults
description: Devuelve resultados detallados para las inserciones exitosas
source_url: https://www.php.net/manual/es/mongodb-driver-bulkwritecommandresult.getinsertresults.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/bulkwritecommandresult/getinsertresults.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49020
---

MongoDB\Driver\BulkWriteCommandResult::getInsertResults

Devuelve resultados detallados para las inserciones exitosas

## Descripción

```php
final public MongoDB\Driver\BulkWriteCommandResult::getInsertResults(): MongoDB\BSON\Document
```php

Dado que los campos `_id` para los documentos insertados son generados por la extensión, el valor de `insertedId` en cada resultado coincidirá con el valor de retorno de MongoDB\Driver\BulkWriteCommand::insertOne para la operación de inserción correspondiente.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un documento que contiene el resultado de cada operación de inserción exitosa, o `null` si no se solicitaron resultados detallados. Las claves del documento corresponderán al índice de la operación de escritura de `MongoDB\Driver\BulkWriteCommand`.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Levanta una excepción

MongoDB\Driver\Exception\LogicException

si la escritura no ha sido reconocida.

## Ejemplos

Ejemplo de `MongoDB\Driver\BulkWriteCommandResult::getInsertResults`

```
<?php

$manager = new MongoDB\Driver\Manager;

$bulk = new MongoDB\Driver\BulkWriteCommand(['verboseResults' => true]);

$generatedId = $bulk->insertOne('db.coll', ['x' => 1]);

$bulk->updateOne('db.coll', ['x' => 1], ['$set' => ['y' => 3]]);
$bulk->updateOne('db.coll', ['x' => 2], ['$set' => ['y' => 1]], ['upsert' => true]);
$bulk->updateOne('db.coll', ['x' => 3], ['$set' => ['y' => 2]], ['upsert' => true]);
$bulk->deleteMany('db.coll', []);

$result = $manager->executeBulkWriteCommand($bulk);

var_dump($generatedId);

var_dump($result->getInsertResults()->toPHP());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(MongoDB\BSON\ObjectId)#3 (1) {
      ["oid"]=>
      string(24) "67f7ee69783dcce702097b41"
    }
    object(stdClass)#8 (1) {
      ["0"]=>
      object(stdClass)#7 (1) {
        ["insertedId"]=>
        object(MongoDB\BSON\ObjectId)#6 (1) {
          ["oid"]=>
          string(24) "67f7ee69783dcce702097b41"
        }
      }
    }

## Véase también

MongoDB\Driver\BulkWriteCommandResult::getInsertedCount

MongoDB\Driver\BulkWriteCommandResult::isAcknowledged

MongoDB\Driver\BulkWriteCommand::insertOne
