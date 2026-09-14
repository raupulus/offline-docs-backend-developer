---
title: MongoDB\Driver\WriteConcernError::getInfo
description: Devuelve el documento de metadatos para WriteConcernError
source_url: https://www.php.net/manual/es/mongodb-driver-writeconcernerror.getinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/writeconcernerror/getinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51540
---

MongoDB\Driver\WriteConcernError::getInfo

Devuelve el documento de metadatos para WriteConcernError

## Descripción

```php
final public MongoDB\Driver\WriteConcernError::getInfo(): object
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el documento de metadatos para WriteConcernError, o `null` si no hay metadatos disponibles.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo con `MongoDB\Driver\WriteConcernError::getInfo`

```
<?php

$manager = new MongoDB\Driver\Manager("mongodb://rs1.example.com,rs2.example.com/?replicaSet=myReplicaSet");

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['x' => 1]);

$writeConcern = new MongoDB\Driver\WriteConcern(2, 1);

try {
    $manager->executeBulkWrite('db.collection', $bulk, ['writeConcern' => $writeConcern]);
} catch(MongoDB\Driver\Exception\BulkWriteException $e) {
    var_dump($e->getWriteResult()->getWriteConcernError()->getInfo());
}

?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(stdClass)#1 (1) {
      ["wtimeout"]=>
      bool(true)
    }

## Véase también

Referencia Write Concern
