---
title: La clase MongoDB\Driver\BulkWrite
source_url: https://www.php.net/manual/es/class.mongodb-driver-bulkwrite.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/bulkwrite.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_revision: 6047c10c1
order: 48890
---

## Introducción

La clase `MongoDB\Driver\BulkWrite` recopila una o más operaciones de escritura que deben enviarse al servidor. Tras añadir cualquier número de operaciones de inserción, actualización y eliminación, la colección puede ejecutarse mediante MongoDB\Driver\Manager::executeBulkWrite.

Las operaciones de escritura pueden ser ordenadas (por omisión) o no ordenadas. Las operaciones de escritura ordenadas se envían al servidor, en el orden proporcionado, para su ejecución secuencial. Si una escritura falla, las operaciones restantes se abortarán. Las operaciones no ordenadas se envían al servidor en un orden arbitrario donde pueden ejecutarse en paralelo. Cualquier error que ocurra se notificará después de que se hayan intentado todas las operaciones.

## Sinopsis de la clase

MongoDB\Driver\BulkWrite

final

MongoDB\Driver\BulkWrite

Countable

Métodos

## Ejemplos

Las operaciones de escritura mixtas se agrupan por tipo

Las operaciones de escritura mixtas (es decir, inserciones, actualizaciones y eliminaciones) se ensamblarán en comandos de escritura tipificados para enviarse secuencialmente al servidor.

```php
<?php

$bulk = new MongoDB\Driver\BulkWrite(['ordered' => true]);
$bulk->insert(['_id' => 1, 'x' => 1]);
$bulk->insert(['_id' => 2, 'x' => 2]);
$bulk->update(['x' => 2], ['$set' => ['x' => 1]]);
$bulk->insert(['_id' => 3, 'x' => 3]);
$bulk->delete(['x' => 1]);

?>

    
```

Dará como resultado la ejecución de cuatro comandos de escritura (es decir, viajes de ida y vuelta). Dado que las operaciones están ordenadas, la tercera inserción no puede enviarse hasta que se ejecute la actualización precedente.

Operaciones de escritura ordenadas que causan un error

```php
<?php

$bulk = new MongoDB\Driver\BulkWrite(['ordered' => true]);
$bulk->delete([]);
$bulk->insert(['_id' => 1]);
$bulk->insert(['_id' => 2]);
$bulk->insert(['_id' => 3, 'hello' => 'world']);
$bulk->update(['_id' => 3], ['$set' => ['hello' => 'earth']]);
$bulk->insert(['_id' => 4, 'hello' => 'pluto']);
$bulk->update(['_id' => 4], ['$set' => ['hello' => 'moon']]);
$bulk->insert(['_id' => 3]);
$bulk->insert(['_id' => 4]);
$bulk->insert(['_id' => 5]);

$manager = new MongoDB\Driver\Manager('mongodb://localhost:27017');
$writeConcern = new MongoDB\Driver\WriteConcern(MongoDB\Driver\WriteConcern::MAJORITY, 1000);

try {
    $result = $manager->executeBulkWrite('db.collection', $bulk, ['writeConcern' => $writeConcern]);
} catch (MongoDB\Driver\Exception\BulkWriteException $e) {
    $result = $e->getWriteResult();

    // Comprobar si la preocupación de escritura no pudo cumplirse
    if ($writeConcernError = $result->getWriteConcernError()) {
        printf("%s (%d): %s\n",
            $writeConcernError->getMessage(),
            $writeConcernError->getCode(),
            var_export($writeConcernError->getInfo(), true)
        );
    }

    // Comprobar si alguna operación de escritura no se completó en absoluto
    foreach ($result->getWriteErrors() as $writeError) {
        printf("Operación#%d: %s (%d)\n",
            $writeError->getIndex(),
            $writeError->getMessage(),
            $writeError->getCode()
        );
    }
} catch (MongoDB\Driver\Exception\Exception $e) {
    printf("Otro error: %s\n", $e->getMessage());
    exit;
}

printf("Insertados %d documento(s)\n", $result->getInsertedCount());
printf("Actualizados %d documento(s)\n", $result->getModifiedCount());

?>

    
```

El ejemplo anterior mostrará:

```php
Operación#7: E11000 duplicate key error index: db.collection.$_id_ dup key: { : 3 } (11000)
Insertados 4 documento(s)
Actualizados  2 documento(s)

   
```

Si la preocupación de escritura no pudiera cumplirse, el ejemplo anterior mostraría algo como:

```php
waiting for replication timed out (64): array (
  'wtimeout' => true,
)
Operación#7: E11000 duplicate key error index: databaseName.collectionName.$_id_ dup key: { : 3 } (11000)
Insertados 4 documento(s)
Actualizados  2 documento(s)

   
```

Si ejecutamos el ejemplo anterior, pero permitimos escrituras no ordenadas:

```php
<?php

$bulk = new MongoDB\Driver\BulkWrite(['ordered' => false]);
/* ... */

?>

   
```

El ejemplo anterior mostrará:

```php
Operación#7: E11000 duplicate key error index: db.collection.$_id_ dup key: { : 3 } (11000)
Operación#8: E11000 duplicate key error index: db.collection.$_id_ dup key: { : 4 } (11000)
Insertados 5 documento(s)
Actualizados  2 documento(s)

   
```

## Véase también

MongoDB\Driver\Manager::executeBulkWrite

MongoDB\Driver\WriteResult

MongoDB\Driver\WriteConcern

MongoDB\Driver\WriteConcernError

MongoDB\Driver\WriteError
