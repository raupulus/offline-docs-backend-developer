---
title: MongoDB\Driver\Exception\BulkWriteCommandException::getErrorReply
description: Devuelve un error de comando de nivel superior
source_url: https://www.php.net/manual/es/mongodb-driver-bulkwritecommandexception.geterrorreply.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/exception/bulkwritecommandexception/geterrorreply.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: true
translation_revision: 9f4cb232d
order: 49460
---

MongoDB\Driver\Exception\BulkWriteCommandException::getErrorReply

Devuelve un error de comando de nivel superior

## Descripción

```php
final public MongoDB\Driver\Exception\BulkWriteCommandException::getErrorReply(): MongoDB\BSON\Document
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un error de comando de nivel superior que ocurrió al intentar comunicarse con el servidor o al ejecutar la escritura masiva. Este valor puede ser `null` si la excepción fue lanzada debido a errores que ocurrieron en escrituras individuales.

## Ejemplos

Ejemplo de `MongoDB\Driver\Exception\BulkWriteCommandException::getErrorReply`

```
<?php

$manager = new MongoDB\Driver\Manager;

// Este ejemplo utiliza configureFailPoint para simular un error de comando de nivel superior
$manager->executeCommand('admin', new MongoDB\Driver\Command([
    'configureFailPoint' => 'failCommand',
    'mode' => ['times' => 1],
    'data' => [
        'failCommands' => ['bulkWrite'],
        'errorCode' => 8, /* UnknownError */
    ],
]));

$bulk = new MongoDB\Driver\BulkWriteCommand;
$bulk->insertOne('db.coll', ['x' => 1]);

try {
    $result = $manager->executeBulkWriteCommand($bulk);
} catch (MongoDB\Driver\Exception\BulkWriteCommandException $e) {
    var_dump($e->getErrorReply()?->toPHP());
}

?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(stdClass)#12 (6) {
      ["ok"]=>
      float(0)
      ["errmsg"]=>
      string(43) "Failing command via 'failCommand' failpoint"
      ["code"]=>
      int(8)
      ["codeName"]=>
      string(12) "UnknownError"
      ["$clusterTime"]=>
      object(stdClass)#10 (2) {
        ["clusterTime"]=>
        object(MongoDB\BSON\Timestamp)#6 (2) {
          ["increment"]=>
          string(1) "7"
          ["timestamp"]=>
          string(10) "1744319389"
        }
        ["signature"]=>
        object(stdClass)#9 (2) {
          ["hash"]=>
          object(MongoDB\BSON\Binary)#7 (2) {
            ["data"]=>
            string(20) ""
            ["type"]=>
            int(0)
          }
          ["keyId"]=>
          object(MongoDB\BSON\Int64)#8 (1) {
            ["integer"]=>
            string(1) "0"
          }
        }
      }
      ["operationTime"]=>
      object(MongoDB\BSON\Timestamp)#11 (2) {
        ["increment"]=>
        string(1) "7"
        ["timestamp"]=>
        string(10) "1744319389"
      }
    }

## Véase también

MongoDB\Driver\Manager::executeBulkWriteCommand
