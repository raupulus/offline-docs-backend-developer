---
title: MongoDB\Driver\Cursor::toArray
description: Devuelve un array que contiene todos los resultados de este cursor
source_url: https://www.php.net/manual/es/mongodb-driver-cursor.toarray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/cursor/toarray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49330
---

MongoDB\Driver\Cursor::toArray

Devuelve un array que contiene todos los resultados de este cursor

## Descripción

```php
final public MongoDB\Driver\Cursor::toArray(): array
```php

Itera el cursor y devuelve sus resultados en un array. Se puede usar `MongoDB\Driver\Cursor::setTypeMap` para controlar cómo se deserializan los documentos en valores de PHP.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `array` que contiene todos los resultados de este cursor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo de `MongoDB\Driver\Cursor::toArray`

```
<?php

$manager = new MongoDB\Driver\Manager("mongodb://localhost:27017");

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['x' => 1]);
$bulk->insert(['x' => 2]);
$bulk->insert(['x' => 3]);
$manager->executeBulkWrite('db.collection', $bulk);

$query = new MongoDB\Driver\Query([]);
$cursor = $manager->executeQuery('db.collection', $query);

var_dump($cursor->toArray());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(3) {
      [0]=>
      object(stdClass)#6 (2) {
        ["_id"]=>
        object(MongoDB\BSON\ObjectId)#5 (1) {
          ["oid"]=>
          string(24) "564259a96118fd40b41bcf61"
        }
        ["x"]=>
        int(1)
      }
      [1]=>
      object(stdClass)#8 (2) {
        ["_id"]=>
        object(MongoDB\BSON\ObjectId)#7 (1) {
          ["oid"]=>
          string(24) "564259a96118fd40b41bcf62"
        }
        ["x"]=>
        int(2)
      }
      [2]=>
      object(stdClass)#10 (2) {
        ["_id"]=>
        object(MongoDB\BSON\ObjectId)#9 (1) {
          ["oid"]=>
          string(24) "564259a96118fd40b41bcf63"
        }
        ["x"]=>
        int(3)
      }
    }

## Véase también

MongoDB\Driver\Cursor::setTypeMap
