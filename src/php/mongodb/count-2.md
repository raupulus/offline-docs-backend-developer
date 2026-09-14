---
title: MongoDB\Driver\BulkWriteCommand::count
description: Cuenta el número de operaciones de escritura en el BulkWriteCommand
source_url: https://www.php.net/manual/es/mongodb-driver-bulkwritecommand.count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/bulkwritecommand/count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48910
---

MongoDB\Driver\BulkWriteCommand::count

Cuenta el número de operaciones de escritura en el BulkWriteCommand

## Descripción

```php
public MongoDB\Driver\BulkWriteCommand::count(): int
```php

Devuelve el número de operaciones de escritura añadidas al objeto `MongoDB\Driver\BulkWriteCommand`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de operaciones de escritura añadidas al objeto `MongoDB\Driver\BulkWriteCommand`.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo de `MongoDB\Driver\BulkWriteCommand::count`

```
<?php

$bulk = new MongoDB\Driver\BulkWriteCommand;
$bulk->insertOne('db.coll', ['_id' => 1, 'x' => 1]);
$bulk->insertOne('db.coll', ['_id' => 2, 'x' => 2]);
$bulk->updateOne('db.coll', ['x' => 2], ['$set' => ['x' => 1]]);
$bulk->deleteMany('db.coll', ['x' => 1]);

var_dump(count($bulk));

?>

   
```php

El ejemplo anterior mostrará:

    int(4)
