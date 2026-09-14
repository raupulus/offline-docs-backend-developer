---
title: MongoDB\Driver\BulkWriteCommandResult::getUpdateResults
description: Devuelve resultados detallados para las actualizaciones exitosas
source_url: https://www.php.net/manual/es/mongodb-driver-bulkwritecommandresult.getupdateresults.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/bulkwritecommandresult/getupdateresults.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49050
---

MongoDB\Driver\BulkWriteCommandResult::getUpdateResults

Devuelve resultados detallados para las actualizaciones exitosas

## Descripción

```php
final public MongoDB\Driver\BulkWriteCommandResult::getUpdateResults(): MongoDB\BSON\Document
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un documento que contiene el resultado de cada operación de actualización exitosa, o `null` si no se solicitaron resultados detallados. Las claves del documento corresponderán al índice de la operación de escritura de `MongoDB\Driver\BulkWriteCommand`.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Levanta una excepción

MongoDB\Driver\Exception\LogicException

si la escritura no ha sido reconocida.

## Ejemplos

Ejemplo de `MongoDB\Driver\BulkWriteCommandResult::getUpdateResults`

```
<?php

$manager = new MongoDB\Driver\Manager;

$bulk = new MongoDB\Driver\BulkWriteCommand(['verboseResults' => true]);
$bulk->insertOne('db.coll', ['x' => 1]);
$bulk->updateOne('db.coll', ['x' => 1], ['$set' => ['y' => 3]]);
$bulk->updateOne('db.coll', ['x' => 2], ['$set' => ['y' => 1]], ['upsert' => true]);
$bulk->updateOne('db.coll', ['x' => 3], ['$set' => ['y' => 2]], ['upsert' => true]);
$bulk->deleteMany('db.coll', []);

$result = $manager->executeBulkWriteCommand($bulk);

var_dump($result->getUpdateResults()->toPHP());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(stdClass)#16 (3) {
      ["1"]=>
      object(stdClass)#7 (2) {
        ["matchedCount"]=>
        object(MongoDB\BSON\Int64)#5 (1) {
          ["integer"]=>
          string(1) "1"
        }
        ["modifiedCount"]=>
        object(MongoDB\BSON\Int64)#6 (1) {
          ["integer"]=>
          string(1) "1"
        }
      }
      ["2"]=>
      object(stdClass)#11 (3) {
        ["matchedCount"]=>
        object(MongoDB\BSON\Int64)#8 (1) {
          ["integer"]=>
          string(1) "1"
        }
        ["modifiedCount"]=>
        object(MongoDB\BSON\Int64)#9 (1) {
          ["integer"]=>
          string(1) "0"
        }
        ["upsertedId"]=>
        object(MongoDB\BSON\ObjectId)#10 (1) {
          ["oid"]=>
          string(24) "67f7eb9b1f198bbcb880d575"
        }
      }
      ["3"]=>
      object(stdClass)#15 (3) {
        ["matchedCount"]=>
        object(MongoDB\BSON\Int64)#12 (1) {
          ["integer"]=>
          string(1) "1"
        }
        ["modifiedCount"]=>
        object(MongoDB\BSON\Int64)#13 (1) {
          ["integer"]=>
          string(1) "0"
        }
        ["upsertedId"]=>
        object(MongoDB\BSON\Int64)#14 (1) {
          ["oid"]=>
          string(24) "67f7eb9b1f198bbcb880d576"
        }
      }
    }

## Véase también

MongoDB\Driver\BulkWriteCommandResult::getMatchedCount

MongoDB\Driver\BulkWriteCommandResult::getModifiedCount

MongoDB\Driver\BulkWriteCommandResult::getUpsertedCount

MongoDB\Driver\BulkWriteCommandResult::isAcknowledged
