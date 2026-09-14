---
title: MongoDB\Driver\WriteResult::getUpsertedIds
description: Devuelve un array de identificadores para los documentos upserted
source_url: https://www.php.net/manual/es/mongodb-driver-writeresult.getupsertedids.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/writeresult/getupsertedids.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51680
---

MongoDB\Driver\WriteResult::getUpsertedIds

Devuelve un array de identificadores para los documentos upserted

## Descripción

```php
final public MongoDB\Driver\WriteResult::getUpsertedIds(): array
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array de identificadores (por ejemplo, el valor del campo `"_id"`) para los documentos upserted. Las claves del array corresponden al índice de la operación de escritura (desde `MongoDBDriverBulkWrite`) responsable del upsert.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo con `MongoDB\Driver\WriteResult::getUpsertedIds`

```
<?php

$manager = new MongoDB\Driver\Manager;

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['x' => 1]);
$bulk->update(['x' => 1], ['$set' => ['y' => 3]]);
$bulk->update(['x' => 2], ['$set' => ['y' => 1]], ['upsert' => true]);
$bulk->update(['x' => 3], ['$set' => ['y' => 2]], ['upsert' => true]);
$bulk->delete(['x' => 1]);

$result = $manager->executeBulkWrite('db.collection', $bulk);

var_dump($result->getUpsertedIds());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(2) {
      [2]=>
      object(MongoDB\BSON\ObjectId)#4 (1) {
        ["oid"]=>
        string(24) "580e62a224f2302f191b880b"
      }
      [3]=>
      object(MongoDB\BSON\ObjectId)#5 (1) {
        ["oid"]=>
        string(24) "580e62a224f2302f191b880c"
      }
    }

## Véase también

MongoDB\Driver\WriteResult::getUpsertedCount

MongoDB\Driver\WriteResult::isAcknowledged
