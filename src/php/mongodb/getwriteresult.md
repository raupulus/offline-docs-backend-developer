---
title: MongoDB\Driver\Exception\BulkWriteException::getWriteResult
description: Devuelve el WriteResult para la operación de escritura fallida
source_url: https://www.php.net/manual/es/mongodb-driver-bulkwriteexception.getwriteresult.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/exception/bulkwriteexception/getwriteresult.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49510
---

MongoDB\Driver\Exception\BulkWriteException::getWriteResult

Devuelve el WriteResult para la operación de escritura fallida

## Descripción

```php
final public MongoDB\Driver\Exception\BulkWriteException::getWriteResult(): MongoDB\Driver\WriteResult
```php

Devuelve el `MongoDB\Driver\WriteResult` para la operación de escritura fallida. Los métodos `MongoDB\Driver\WriteResult::getWriteErrors` y `MongoDB\Driver\WriteResult::getWriteConcernError` pueden ser utilizados para obtener detalles adicionales sobre el error.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El `MongoDB\Driver\WriteResult` para la operación de escritura fallida.

## Ejemplos

Ejemplo de `MongoDB\Driver\Exception\BulkWriteException::getWriteResult`

```
<?php

$manager = new MongoDB\Driver\Manager('mongodb://localhost');
$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['_id' => 1]);
$bulk->insert(['_id' => 1]);

try {
    $manager->executeBulkWrite('db.collection', $bulk);
} catch (MongoDB\Driver\Exception\BulkWriteException $e) {
    $writeResult = $e->getWriteResult();

    if ($writeConcernError = $writeResult->getWriteConcernError()) {
        var_dump($writeConcernError);
    }

    if ($writeErrors = $writeResult->getWriteErrors()) {
        var_dump($writeErrors);
    }
}

?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(1) {
      [0]=>
      object(MongoDB\Driver\WriteError)#5 (4) {
        ["message"]=>
        string(70) "E11000 duplicate key error index: db.collection.$_id_ dup key: { : 1 }"
        ["code"]=>
        int(11000)
        ["index"]=>
        int(1)
        ["info"]=>
        NULL
      }
    }

## Véase también

MongoDB\Driver\WriteResult

MongoDB\Driver\Manager::executeBulkWrite
