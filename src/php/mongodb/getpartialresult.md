---
title: MongoDB\Driver\Exception\BulkWriteCommandException::getPartialResult
description: Devuelve el resultado de todas las operaciones de escritura exitosas
source_url: https://www.php.net/manual/es/mongodb-driver-bulkwritecommandexception.getpartialresult.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/exception/bulkwritecommandexception/getpartialresult.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: true
translation_revision: 9f4cb232d
order: 49470
---

MongoDB\Driver\Exception\BulkWriteCommandException::getPartialResult

Devuelve el resultado de todas las operaciones de escritura exitosas

## Descripción

```php
final public MongoDB\Driver\Exception\BulkWriteCommandException::getPartialResult(): MongoDB\Driver\BulkWriteCommandResult
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `MongoDB\Driver\BulkWriteCommandResult` que proporciona los resultados de cada una de las operaciones exitosas que se realizaron antes de que se encontrara el error. El valor devuelto será `null` si no se puede determinar si al menos una escritura se realizó con éxito (y fue reconocida).

## Ejemplos

Resultado parcial si al menos una escritura es exitosa

```
<?php

$manager = new MongoDB\Driver\Manager;

$bulk = new MongoDB\Driver\BulkWriteCommand;
$bulk->deleteMany('db.coll', []);
$bulk->insertOne('db.coll', ['_id' => 1]);
$bulk->insertOne('db.coll', ['_id' => 1]);

try {
    $result = $manager->executeBulkWriteCommand($bulk);
} catch (MongoDB\Driver\Exception\BulkWriteCommandException $e) {
    $result = $e->getPartialResult();
}

var_dump($result?->getInsertedCount());

?>

   
```php

El ejemplo anterior mostrará:

    int(1)

Ningún resultado parcial si ninguna escritura es exitosa

```
<?php

$manager = new MongoDB\Driver\Manager;

$bulk = new MongoDB\Driver\BulkWriteCommand;
$bulk->deleteMany('db.coll', []);
$bulk->insertOne('db.coll', ['_id' => 1]);
$manager->executeBulkWriteCommand($bulk);

$bulk = new MongoDB\Driver\BulkWriteCommand;
$bulk->insertOne('db.coll', ['_id' => 1]);

try {
    $result = $manager->executeBulkWriteCommand($bulk);
} catch (MongoDB\Driver\Exception\BulkWriteCommandException $e) {
    $result = $e->getPartialResult();
}

var_dump($result?->getInsertedCount());

?>

   
```php

El ejemplo anterior mostrará:

    NULL

## Véase también

MongoDB\Driver\BulkWriteCommandResult

MongoDB\Driver\Manager::executeBulkWriteCommand
