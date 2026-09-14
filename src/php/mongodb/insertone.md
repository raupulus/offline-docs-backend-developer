---
title: MongoDB\Driver\BulkWriteCommand::insertOne
description: Añade una operación insertOne
source_url: https://www.php.net/manual/es/mongodb-driver-bulkwritecommand.insertone.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/bulkwritecommand/insertone.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48940
---

MongoDB\Driver\BulkWriteCommand::insertOne

Añade una operación insertOne

## Descripción

```php
public MongoDB\Driver\BulkWriteCommand::insertOne(string $namespace, array $document): mixed
```php

Añade una operación insertOne al `MongoDB\Driver\BulkWriteCommand`. El documento se insertará en la colección identificada por `namespace`.

## Parámetros

`namespace` (`string`)  
Un espacio de nombres completamente calificado (ej. `"databaseName.collectionName"`)

`document` (`arrayobject`)  
Un documento a insertar.

## Valores devueltos

Devuelve el `_id` del documento insertado. Si el `document` no tenía un `_id`, se devolverá el `MongoDB\BSON\ObjectId` generado para la inserción.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo de `MongoDB\Driver\BulkWriteCommand::insertOne`

```
<?php

$manager = new MongoDB\Driver\Manager;

$bulk = new MongoDB\Driver\BulkWriteCommand;

$doc1 = ['x' => 1];
$doc2 = ['_id' => 'custom-id', 'x' => 2];
$doc3 = ['_id' => new MongoDB\BSON\ObjectId('0123456789abcdef01234567'), 'x' => 3];

$id1 = $bulk->insertOne('db.coll', $doc1);
$id2 = $bulk->insertOne('db.coll', $doc2);
$id3 = $bulk->insertOne('db.coll', $doc3);

var_dump($id1, $id2, $id3);

$result = $manager->executeBulkWriteCommand($bulk);

?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(MongoDB\BSON\ObjectId)#3 (1) {
      ["oid"]=>
      string(24) "67f58058d1a0aa2fd80d55d0"
    }
    string(9) "custom-id"
    object(MongoDB\BSON\ObjectId)#4 (1) {
      ["oid"]=>
      string(24) "0123456789abcdef01234567"
    }

## Véase también

MongoDB\Driver\Manager::executeBulkWriteCommand

MongoDB\Driver\BulkWriteCommandResult

MongoDB\BSON\ObjectId
