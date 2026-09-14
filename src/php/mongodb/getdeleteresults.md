---
title: MongoDB\Driver\BulkWriteCommandResult::getDeleteResults
description: Devuelve resultados detallados para eliminaciones exitosas
source_url: https://www.php.net/manual/es/mongodb-driver-bulkwritecommandresult.getdeleteresults.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/bulkwritecommandresult/getdeleteresults.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49000
---

MongoDB\Driver\BulkWriteCommandResult::getDeleteResults

Devuelve resultados detallados para eliminaciones exitosas

## Descripción

```php
final public MongoDB\Driver\BulkWriteCommandResult::getDeleteResults(): MongoDB\BSON\Document
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un documento que contiene el resultado de cada operación de eliminación exitosa, o `null` si no se solicitaron resultados detallados. Las claves del documento corresponderán al índice de la operación de escritura desde `MongoDB\Driver\BulkWriteCommand`.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Levanta una excepción

MongoDB\Driver\Exception\LogicException

si la escritura no ha sido reconocida.

## Ejemplos

Ejemplo de `MongoDB\Driver\BulkWriteCommandResult::getDeleteResults`

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

var_dump($result->getDeleteResults()->toPHP());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(stdClass)#7 (1) {
      ["4"]=>
      object(stdClass)#6 (1) {
        ["deletedCount"]=>
        object(MongoDB\BSON\Int64)#5 (1) {
          ["integer"]=>
          string(1) "3"
        }
      }
    }

## Véase también

MongoDB\Driver\BulkWriteCommandResult::getDeletedCount

MongoDB\Driver\BulkWriteCommandResult::isAcknowledged
