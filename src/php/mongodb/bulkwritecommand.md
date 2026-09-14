---
title: La clase MongoDB\Driver\BulkWriteCommand
source_url: https://www.php.net/manual/es/class.mongodb-driver-bulkwritecommand.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/bulkwritecommand.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48980
---

## Introducción

La clase `MongoDB\Driver\BulkWriteCommand` recopila una o más operaciones de escritura que deben enviarse al servidor usando el [comando bulkWrite](https://www.mongodb.com/docs/manual/reference/command/bulkWrite) introducido en MongoDB 8.0. Tras añadir cualquier número de operaciones de inserción, actualización y eliminación, el comando puede ejecutarse mediante MongoDB\Driver\Manager::executeBulkWriteCommand.

A diferencia de `MongoDB\Driver\BulkWrite`, donde todas las operaciones de escritura deben dirigirse a la misma colección, cada operación de escritura dentro de `MongoDB\Driver\BulkWriteCommand` puede dirigirse a una colección diferente.

Las operaciones de escritura pueden ser ordenadas (por omisión) o no ordenadas. Las operaciones de escritura ordenadas se envían al servidor, en el orden proporcionado, para su ejecución serial. Si una escritura falla, las operaciones restantes se abortarán. Las operaciones no ordenadas se envían al servidor en un orden arbitrario donde pueden ejecutarse en paralelo. Cualquier error que ocurra se reporta después de que se hayan intentado todas las operaciones.

## Sinopsis de la clase

MongoDB\Driver\BulkWriteCommand

final

MongoDB\Driver\BulkWriteCommand

Countable

Métodos

## Ejemplos

Operaciones de escritura mixtas

Las operaciones de escritura mixtas (es decir, inserciones, actualizaciones y eliminaciones) se enviarán al servidor usando un único [comando bulkWrite](https://www.mongodb.com/docs/manual/reference/command/bulkWrite).

```php
<?php

$manager = new MongoDB\Driver\Manager;

$bulk = new MongoDB\Driver\BulkWriteCommand;

// Eliminar documentos de ambas colecciones
$bulk->deleteMany('db.coll_one', []);
$bulk->deleteMany('db.coll_two', []);

// Insertar documentos en dos colecciones
$bulk->insertOne('db.coll_one', ['_id' => 1]);
$bulk->insertOne('db.coll_two', ['_id' => 2]);
$bulk->insertOne('db.coll_two', ['_id' => 3]);

// Actualizar un documento en "coll_one"
$bulk->updateOne('db.coll_one', ['_id' => 1], ['$set' => ['x' => 1]]);

$result = $manager->executeBulkWriteCommand($bulk);

printf("Insertados %d documento(s)\n", $result->getInsertedCount());
printf("Actualizados %d documento(s)\n", $result->getModifiedCount());

?>

    
```

El ejemplo anterior mostrará:

    Insertados 3 documento(s)
    Actualizados  1 documento(s)

Operaciones de escritura ordenadas que causan un error

```php
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

    
```

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

MongoDB\Driver\Manager::executeBulkWriteCommand

MongoDB\Driver\BulkWriteCommandResult

MongoDB\Driver\Exception\BulkWriteCommandException

MongoDB\Driver\WriteConcern

MongoDB\Driver\WriteConcernError

MongoDB\Driver\WriteError
