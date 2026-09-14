---
title: MongoDB\Driver\Cursor::getServer
description: Devuelve el servidor asociado con este cursor
source_url: https://www.php.net/manual/es/mongodb-driver-cursor.getserver.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/cursor/getserver.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49270
---

MongoDB\Driver\Cursor::getServer

Devuelve el servidor asociado con este cursor

## Descripción

```php
final public MongoDB\Driver\Cursor::getServer(): MongoDB\Driver\Server
```php

Devuelve el `MongoDB\Driver\Server` asociado con este cursor. Este es el servidor que ejecutó la `MongoDB\Driver\Query` o la `MongoDB\Driver\Command`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el `MongoDB\Driver\Server` asociado con este cursor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo de `MongoDB\Driver\Cursor::getServer`

```
<?php

$manager = new MongoDB\Driver\Manager("mongodb://localhost:27017");
$query = new MongoDB\Driver\Query([]);

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['x' => 1]);
$manager->executeBulkWrite('db.collection', $bulk);

$cursor = $manager->executeQuery('db.collection', $query);
var_dump($cursor->getServer());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(MongoDB\Driver\Server)#5 (10) {
      ["host"]=>
      string(9) "localhost"
      ["port"]=>
      int(27017)
      ["type"]=>
      int(1)
      ["is_primary"]=>
      bool(false)
      ["is_secondary"]=>
      bool(false)
      ["is_arbiter"]=>
      bool(false)
      ["is_hidden"]=>
      bool(false)
      ["is_passive"]=>
      bool(false)
      ["last_hello_response"]=>
      array(8) {
        ["isWritablePrimary"]=>
        bool(true)
        ["maxBsonObjectSize"]=>
        int(16777216)
        ["maxMessageSizeBytes"]=>
        int(48000000)
        ["maxWriteBatchSize"]=>
        int(1000)
        ["localTime"]=>
        object(MongoDB\BSON\UTCDateTime)#6 (1) {
          ["milliseconds"]=>
          int(1446505367907)
        }
        ["maxWireVersion"]=>
        int(3)
        ["minWireVersion"]=>
        int(0)
        ["ok"]=>
        float(1)
      }
      ["round_trip_time"]=>
      int(584)
    }

## Véase también

MongoDB\Driver\Server
