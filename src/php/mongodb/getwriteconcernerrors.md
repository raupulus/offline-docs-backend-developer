---
title: MongoDB\Driver\Exception\BulkWriteCommandException::getWriteConcernErrors
description: Devuelve los errores de preocupación de escritura
source_url: https://www.php.net/manual/es/mongodb-driver-bulkwritecommandexception.getwriteconcernerrors.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/exception/bulkwritecommandexception/getwriteconcernerrors.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: true
translation_revision: 9f4cb232d
order: 49480
---

MongoDB\Driver\Exception\BulkWriteCommandException::getWriteConcernErrors

Devuelve los errores de preocupación de escritura

## Descripción

```php
final public MongoDB\Driver\Exception\BulkWriteCommandException::getWriteConcernErrors(): array
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array de cada uno de los `MongoDB\Driver\WriteConcernError`s que se produjeron durante la ejecución de la escritura masiva. Esta lista puede tener múltiples entradas si se necesitó más de un comando de servidor para ejecutar la escritura masiva.

## Ejemplos

Ejemplo de `MongoDB\Driver\Exception\BulkWriteCommandException::getWriteConcernErrors`

```
<?php

$manager = new MongoDB\Driver\Manager;

$bulk = new MongoDB\Driver\BulkWriteCommand;
$bulk->insertOne('db.coll', ['x' => 1]);

$writeConcern = new MongoDB\Driver\WriteConcern(50);

try {
    $result = $manager->executeBulkWriteCommand($bulk, ['writeConcern' => $writeConcern]);
} catch (MongoDB\Driver\Exception\BulkWriteCommandException $e) {
    var_dump($e->getWriteConcernErrors());
}

?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(1) {
      [0]=>
      object(MongoDB\Driver\WriteConcernError)#6 (3) {
        ["message"]=>
        string(29) "Not enough data-bearing nodes"
        ["code"]=>
        int(100)
        ["info"]=>
        object(stdClass)#8 (1) {
          ["writeConcern"]=>
          object(stdClass)#7 (3) {
            ["w"]=>
            int(50)
            ["wtimeout"]=>
            int(0)
            ["provenance"]=>
            string(14) "clientSupplied"
          }
        }
      }
    }

## Véase también

MongoDB\Driver\Manager::executeBulkWriteCommand

MongoDB\Driver\WriteConcern

MongoDB\Driver\WriteConcernError
