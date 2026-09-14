---
title: MongoDB\Driver\WriteResult::getWriteErrors
description: Devuelve todos los errores de escritura que se han producido
source_url: https://www.php.net/manual/es/mongodb-driver-writeresult.getwriteerrors.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/writeresult/getwriteerrors.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51700
---

MongoDB\Driver\WriteResult::getWriteErrors

Devuelve todos los errores de escritura que se han producido

## Descripción

```php
final public MongoDB\Driver\WriteResult::getWriteErrors(): array
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array de objetos `MongoDBDriverWriteError` para todos los errores de escritura encontrados durante la operación de escritura. El array estará vacío si no se ha producido ningún error de escritura.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

`MongoDB\Driver\WriteResult::getWriteErrors` con un solo error

```
<?php

$manager = new MongoDB\Driver\Manager;

/* Por omisión, las operaciones de escritura en bloque se ejecutan en serie en
 * el orden y la ejecución se detendrá después del primer error.
 */
$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['_id' => 1]);
$bulk->insert(['_id' => 2]);
$bulk->insert(['_id' => 2]);
$bulk->insert(['_id' => 3]);
$bulk->insert(['_id' => 4]);
$bulk->insert(['_id' => 4]);

try {
    $result = $manager->executeBulkWrite('db.collection', $bulk);
} catch (MongoDB\Driver\Exception\BulkWriteException $e) {
    var_dump($e->getWriteResult()->getWriteErrors());
}

?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(1) {
      [0]=>
      object(MongoDB\Driver\WriteError)#5 (4) {
        ["message"]=>
        string(81) "E11000 duplicate key error collection: db.collection index: _id_ dup key: { : 2 }"
        ["code"]=>
        int(11000)
        ["index"]=>
        int(2)
        ["info"]=>
        NULL
      }
    }

`MongoDB\Driver\WriteResult::getWriteErrors` con múltiples errores

```
<?php

$manager = new MongoDB\Driver\Manager;

/* La opción "ordered" puede ser utilizada para permitir que las operaciones
 * de escritura en bloque continúen ejecutándose después del primer error.
 */
$bulk = new MongoDB\Driver\BulkWrite(['ordered' => false]);
$bulk->insert(['_id' => 1]);
$bulk->insert(['_id' => 2]);
$bulk->insert(['_id' => 2]);
$bulk->insert(['_id' => 3]);
$bulk->insert(['_id' => 4]);
$bulk->insert(['_id' => 4]);

try {
    $result = $manager->executeBulkWrite('db.collection', $bulk);
} catch (MongoDB\Driver\Exception\BulkWriteException $e) {
    var_dump($e->getWriteResult()->getWriteErrors());
}

?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(2) {
      [0]=>
      object(MongoDB\Driver\WriteError)#5 (4) {
        ["message"]=>
        string(81) "E11000 duplicate key error collection: db.collection index: _id_ dup key: { : 2 }"
        ["code"]=>
        int(11000)
        ["index"]=>
        int(2)
        ["info"]=>
        NULL
      }
      [1]=>
      object(MongoDB\Driver\WriteError)#6 (4) {
        ["message"]=>
        string(81) "E11000 duplicate key error collection: db.collection index: _id_ dup key: { : 4 }"
        ["code"]=>
        int(11000)
        ["index"]=>
        int(5)
        ["info"]=>
        NULL
      }
    }

## Véase también

MongoDB\Driver\WriteError
