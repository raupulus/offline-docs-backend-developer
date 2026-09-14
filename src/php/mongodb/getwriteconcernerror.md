---
title: MongoDB\Driver\WriteResult::getWriteConcernError
description: Devuelve cualquier error de WriteConcern que haya ocurrido
source_url: https://www.php.net/manual/es/mongodb-driver-writeresult.getwriteconcernerror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/writeresult/getwriteconcernerror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51690
---

MongoDB\Driver\WriteResult::getWriteConcernError

Devuelve cualquier error de WriteConcern que haya ocurrido

## Descripción

```php
final public MongoDB\Driver\WriteResult::getWriteConcernError(): MongoDB\Driver\WriteConcernError
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `MongoDBDriverWriteConcernError` si se encontró un error de preocupación de escritura durante la operación de escritura, y `null` en caso contrario.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo con `MongoDB\Driver\WriteResult::getWriteConcernError`

```
<?php

$manager = new MongoDB\Driver\Manager("mongodb://rs1.example.com,rs2.example.com/?replicaSet=myReplicaSet");

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['x' => 1]);

$writeConcern = new MongoDB\Driver\WriteConcern(2, 1);

try {
    $manager->executeBulkWrite('db.collection', $bulk, ['writeConcern' => $writeConcern]);
} catch(MongoDB\Driver\Exception\BulkWriteException $e) {
    var_dump($e->getWriteResult()->getWriteConcernError());
}

?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(MongoDB\Driver\WriteConcernError)#6 (3) {
      ["message"]=>
      string(33) "waiting for replication timed out"
      ["code"]=>
      int(64)
      ["info"]=>
      object(stdClass)#7 (1) {
        ["wtimeout"]=>
        bool(true)
      }
    }

## Véase también

MongoDB\Driver\WriteConcern

Referencia Write Concern
