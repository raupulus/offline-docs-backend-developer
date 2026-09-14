---
title: MongoDB\Driver\Exception\BulkWriteCommandException::getWriteErrors
description: Devuelve los errores de escritura
source_url: https://www.php.net/manual/es/mongodb-driver-bulkwritecommandexception.getwriteerrors.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/exception/bulkwritecommandexception/getwriteerrors.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: true
translation_revision: 9f4cb232d
order: 49490
---

MongoDB\Driver\Exception\BulkWriteCommandException::getWriteErrors

Devuelve los errores de escritura

## Descripción

```php
final public MongoDB\Driver\Exception\BulkWriteCommandException::getWriteErrors(): array
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array de `MongoDB\Driver\WriteError` que se produjeron durante la ejecución de la escritura individual. Las claves del array corresponden al índice de la operación de escritura en `MongoDB\Driver\BulkWriteCommand`. Esta lista contendrá como máximo una entrada si la escritura masiva estaba ordenada.

## Ejemplos

Ejemplo de `MongoDB\Driver\Exception\BulkWriteCommandException::getWriteErrors`

```
<?php

$manager = new MongoDB\Driver\Manager;

$bulk = new MongoDB\Driver\BulkWriteCommand(['ordered' => false]);
$bulk->deleteMany('db.coll', []);
$bulk->insertOne('db.coll', ['_id' => 1]);
$bulk->insertOne('db.coll', ['_id' => 1]);
$bulk->insertOne('db.coll', ['_id' => 1]);

try {
    $result = $manager->executeBulkWriteCommand($bulk);
} catch (MongoDB\Driver\Exception\BulkWriteCommandException $e) {
    var_dump($e->getWriteErrors());
}

?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(2) {
      [2]=>
      object(MongoDB\Driver\WriteError)#5 (4) {
        ["message"]=>
        string(78) "E11000 duplicate key error collection: db.coll index: _id_ dup key: { _id: 1 }"
        ["code"]=>
        int(11000)
        ["index"]=>
        int(2)
        ["info"]=>
        object(stdClass)#6 (0) {
        }
      }
      [3]=>
      object(MongoDB\Driver\WriteError)#7 (4) {
        ["message"]=>
        string(78) "E11000 duplicate key error collection: db.coll index: _id_ dup key: { _id: 1 }"
        ["code"]=>
        int(11000)
        ["index"]=>
        int(3)
        ["info"]=>
        object(stdClass)#8 (0) {
        }
      }
    }

## Véase también

MongoDB\Driver\Manager::executeBulkWriteCommand

MongoDB\Driver\WriteError
