---
title: MongoDB\Driver\Manager::executeBulkWriteCommand
description: Ejecuta operaciones de escritura utilizando el comando bulkWrite
source_url: https://www.php.net/manual/es/mongodb-driver-manager.executebulkwritecommand.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/manager/executebulkwritecommand.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: true
translation_revision: 9f4cb232d
order: 49730
---

MongoDB\Driver\Manager::executeBulkWriteCommand

Ejecuta operaciones de escritura utilizando el comando bulkWrite

## Descripción

```php
final public MongoDB\Driver\Manager::executeBulkWriteCommand(MongoDB\Driver\BulkWriteCommand $bulk, [array $options]): MongoDB\Driver\BulkWriteCommandResult
```php

Ejecuta una o varias operaciones de escritura en el servidor primario utilizando el comando [bulkWrite](https://www.mongodb.com/docs/manual/reference/command/bulkWrite) introducido en MongoDB 8.0.

Una `MongoDB\Driver\BulkWriteCommand` puede ser construida con una o varias operaciones de escritura de tipos variados (por ejemplo, inserciones, actualizaciones y eliminaciones). Cada operación de escritura puede apuntar a una colección diferente.

El valor por omisión para la opción `"writeConcern"` será deducido de una transacción activa (indicada por la opción `"session"`), seguida por [la URI de conexión](#mongodb-driver-manager.construct-uri).

## Parámetros

`bulk` (`MongoDB\Driver\BulkWriteCommand`)  
Escritura(s) a ejecutar.

`options`  
| Opción | Tipo | Descripción |
|----|----|----|
| session | `MongoDB\Driver\Session` | Una sesión a asociar a la operación. |
| writeConcern | `MongoDB\Driver\WriteConcern` | Una preocupación de escritura a aplicar a la operación. |

options

## Valores devueltos

Retorna un `MongoDB\Driver\BulkWriteCommandResult` en caso de éxito.

## Errores/Excepciones

Lanza una

MongoDB\Driver\Exception\InvalidArgumentException

si

bulk

no contiene operaciones de escritura válidas.

Lanza una

MongoDB\Driver\Exception\InvalidArgumentException

si

bulk

ya ha sido ejecutada. Los objetos

MongoDB\Driver\BulkWriteCommand

no pueden ser ejecutados múltiples veces.

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

si la opción

"session"

se utiliza junto con una preocupación de escritura no reconocida.

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una excepción

MongoDB\Driver\Exception\ConnectionException

si la conexión al servidor falla por una razón distinta a un problema de identificación

Lanza una excepción

MongoDB\Driver\Exception\AuthenticationException

si se requiere una identificación pero falla

Lanza una excepción

MongoDB\Driver\Exception\BulkWriteCommandException

en caso de error de escritura (por ejemplo, fallo de comando, error de escritura o preocupación de escritura)

Lanza

MongoDB\Driver\Exception\RuntimeException

en caso de otro error.

## Ejemplos

Operaciones de escritura mixtas

Las operaciones de escritura mixtas (por ejemplo, inserción, actualización y eliminación) serán enviadas al servidor utilizando una sola comando [bulkWrite](https://www.mongodb.com/docs/manual/reference/command/bulkWrite)

```
<?php

$manager = new MongoDB\Driver\Manager;

$bulk = new MongoDB\Driver\BulkWriteCommand;

// Elimina documentos de dos colecciones
$bulk->deleteMany('db.coll_one', []);
$bulk->deleteMany('db.coll_two', []);

// Añade documentos a dos colecciones
$bulk->insertOne('db.coll_one', ['_id' => 1]);
$bulk->insertOne('db.coll_two', ['_id' => 2]);
$bulk->insertOne('db.coll_two', ['_id' => 3]);

// Actualiza un documento en "coll_one"
$bulk->updateOne('db.coll_one', ['_id' => 1], ['$set' => ['x' => 1]]);

$result = $manager->executeBulkWriteCommand($bulk);

printf("Insertados %d documento(s)\n", $result->getInsertedCount());
printf("Actualizados %d documento(s)\n", $result->getModifiedCount());

?>

   
```php

El ejemplo anterior mostrará:

    Insertados 3 documento(s)
    Actualizados 1 documento(s)

Operación de escritura ordenada que provoca un error

```
<?php

$manager = new MongoDB\Driver\Manager;

$bulk = new MongoDB\Driver\BulkWriteCommand;

$bulk->deleteMany('db.coll', []);
$bulk->insertOne('db.coll', ['_id' => 1]);
$bulk->insertOne('db.coll', ['_id' => 2]);
$bulk->insertOne('db.coll', ['_id' => 1]);
$bulk->insertOne('db.coll', ['_id' => 3]);

try {
    $result = $manager->executeBulkWriteCommand($bulk);
} catch (MongoDB\Driver\Exception\BulkWriteCommandException $e) {
    $result = $e->getPartialResult();

    var_dump($e->getWriteErrors());
}

printf("Insertados %d documento(s)\n", $result->getInsertedCount());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(1) {
      [3]=>
      object(MongoDB\Driver\WriteError)#5 (4) {
        ["message"]=>
        string(78) "E11000 duplicate key error collection: db.coll index: _id_ dup key: { _id: 1 }"
        ["code"]=>
        int(11000)
        ["index"]=>
        int(3)
        ["info"]=>
        object(stdClass)#6 (0) {
        }
      }
    }
    Insertados 2 documento(s)

## Véase también

MongoDB\Driver\BulkWriteCommand

MongoDB\Driver\BulkWriteCommandResult

MongoDB\Driver\WriteConcern

MongoDB\Driver\Server::executeBulkWriteCommand
