---
title: MongoDB\Driver\BulkWriteCommandResult::getModifiedCount
description: Devuelve el número de documentos existentes que se actualizaron
source_url: https://www.php.net/manual/es/mongodb-driver-bulkwritecommandresult.getmodifiedcount.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/bulkwritecommandresult/getmodifiedcount.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49040
---

MongoDB\Driver\BulkWriteCommandResult::getModifiedCount

Devuelve el número de documentos existentes que se actualizaron

## Descripción

```php
final public MongoDB\Driver\BulkWriteCommandResult::getModifiedCount(): int
```php

Si la operación de actualización no produce cambios en el documento (por ejemplo, establecer el valor de un campo a su valor actual), el recuento de documentos modificados puede ser menor que el valor devuelto por MongoDB\Driver\BulkWriteCommandResult::getMatchedCount.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número total de documentos existentes que fueron actualizados por todas las operaciones.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Levanta una excepción

MongoDB\Driver\Exception\LogicException

si la escritura no ha sido reconocida.

## Ejemplos

Ejemplo de `MongoDB\Driver\BulkWriteCommandResult::getModifiedCount`

```
<?php

$manager = new MongoDB\Driver\Manager;

$bulk = new MongoDB\Driver\BulkWriteCommand;
$bulk->insertOne('db.coll', ['x' => 1]);
$bulk->updateOne('db.coll', ['x' => 1], ['$set' => ['y' => 3]]);
$bulk->updateOne('db.coll', ['x' => 2], ['$set' => ['y' => 1]], ['upsert' => true]);
$bulk->updateOne('db.coll', ['x' => 3], ['$set' => ['y' => 2]], ['upsert' => true]);
$bulk->deleteMany('db.coll', []);

$result = $manager->executeBulkWriteCommand($bulk);

var_dump($result->getModifiedCount());

?>

   
```php

El ejemplo anterior mostrará:

    int(1)

## Véase también

MongoDB\Driver\BulkWriteCommandResult::getMatchedCount

MongoDB\Driver\BulkWriteCommandResult::getUpdateResults

MongoDB\Driver\BulkWriteCommandResult::isAcknowledged
