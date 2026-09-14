---
title: MongoDB\Driver\Manager::executeBulkWrite
description: Ejecuta una o varias operaciones de escritura
source_url: https://www.php.net/manual/es/mongodb-driver-manager.executebulkwrite.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/manager/executebulkwrite.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_revision: 6047c10c1
order: 49720
---

MongoDB\Driver\Manager::executeBulkWrite

Ejecuta una o varias operaciones de escritura

## Descripción

```php
final public MongoDB\Driver\Manager::executeBulkWrite(string $namespace, MongoDB\Driver\BulkWrite $bulk, [array $options]): MongoDB\Driver\WriteResult
```php

Ejecuta una o varias operaciones de escritura en el servidor primario.

Un `MongoDB\Driver\BulkWrite` puede ser construido con una o varias operaciones de escritura de tipos variados (por ejemplo, actualizaciones, eliminaciones e inserciones). El controlador intentará enviar las operaciones del mismo tipo al servidor en el menor número de solicitudes posible para optimizar los intercambios.

El valor por omisión de la opción `"writeConcern"` será deducido a partir de una transacción activa (indicada por la opción `"session"`), seguida de la [URI de conexión](#mongodb-driver-manager.construct-uri).

## Parámetros

`namespace` (`string`)  
Un espacio de nombres completamente calificado (ej. `"databaseName.collectionName"`)

`bulk` (`MongoDB\Driver\BulkWrite`)  
Escritura(s) a ejecutar.

`options`  
| Opción | Tipo | Descripción |
|----|----|----|
| session | `MongoDB\Driver\Session` | Una sesión a asociar a la operación. |
| writeConcern | `MongoDB\Driver\WriteConcern` | Una preocupación de escritura a aplicar a la operación. |

options

## Valores devueltos

Retorna un `MongoDB\Driver\WriteResult` en caso de éxito.

## Errores/Excepciones

Lanza una

MongoDB\Driver\Exception\InvalidArgumentException

si

bulk

no contiene ninguna operación de escritura.

Lanza una

MongoDB\Driver\Exception\InvalidArgumentException

si

bulk

ya ha sido ejecutado. Los objetos

MongoDB\Driver\BulkWrite

no pueden ser ejecutados varias veces.

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

MongoDB\Driver\Exception\BulkWriteException

en caso de error de una operación de escritura (un error WriteError y WriteConcern)

Lanza una

MongoDB\Driver\Exception\RuntimeException

en caso de otros errores.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 2.0.0 | El parámetro `options` ya no acepta una instancia de `MongoDB\Driver\WriteConcern`. |
| PECL mongodb 1.21.0 | Pasar un objeto `MongoDB\Driver\WriteConcern` como `options` está obsoleto y será eliminado en la versión 2.0. |
| PECL mongodb 1.4.4 | Se lanzará una `MongoDB\Driver\Exception\InvalidArgumentException` si la opción `"session"` se utiliza en combinación con un `"writeConcern"` no-acknowledged. |
| PECL mongodb 1.4.0 | El tercer parámetro es ahora un array de `options`. Por razones de compatibilidad ascendente, este parámetro siempre aceptará un objeto `MongoDB\Driver\WriteConcern`. |
| PECL mongodb 1.3.0 | Se lanza una `MongoDB\Driver\Exception\InvalidArgumentException` si `bulk` no contiene ninguna operación de escritura. Anteriormente, se lanzaba una `MongoDB\Driver\Exception\BulkWriteException`. |

## Ejemplos

Ejemplo de `MongoDB\Driver\Manager::executeBulkWrite`

```
<?php

$bulk = new MongoDB\Driver\BulkWrite();

$bulk->insert(['_id' => 1, 'x' => 1]);
$bulk->insert(['_id' => 2, 'x' => 2]);

$bulk->update(['x' => 2], ['$set' => ['x' => 1]], ['multi' => false, 'upsert' => false]);
$bulk->update(['x' => 3], ['$set' => ['x' => 3]], ['multi' => false, 'upsert' => true]);
$bulk->update(['_id' => 3], ['$set' => ['x' => 3]], ['multi' => false, 'upsert' => true]);

$bulk->insert(['_id' => 4, 'x' => 2]);

$bulk->delete(['x' => 1], ['limit' => 1]);

$manager = new MongoDB\Driver\Manager('mongodb://localhost:27017');
$writeConcern = new MongoDB\Driver\WriteConcern(MongoDB\Driver\WriteConcern::MAJORITY, 100);
$result = $manager->executeBulkWrite('db.collection', $bulk, ['writeConcern' => $writeConcern]);

printf("Inserted %d document(s)\n", $result->getInsertedCount());
printf("Matched  %d document(s)\n", $result->getMatchedCount());
printf("Updated  %d document(s)\n", $result->getModifiedCount());
printf("Upserted %d document(s)\n", $result->getUpsertedCount());
printf("Deleted  %d document(s)\n", $result->getDeletedCount());

foreach ($result->getUpsertedIds() as $index => $id) {
    printf('upsertedId[%d]: ', $index);
    var_dump($id);
}

/* Si el WriteConcern no ha podido ser satisfecho */
if ($writeConcernError = $result->getWriteConcernError()) {
    printf("%s (%d): %s\n", $writeConcernError->getMessage(), $writeConcernError->getCode(), var_export($writeConcernError->getInfo(), true));
}

/* Si una escritura no ha podido hacerse en absoluto */
foreach ($result->getWriteErrors() as $writeError) {
    printf("Operation#%d: %s (%d)\n", $writeError->getIndex(), $writeError->getMessage(), $writeError->getCode());
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Inserted 3 document(s)
    Matched  1 document(s)
    Updated  1 document(s)
    Upserted 2 document(s)
    Deleted  1 document(s)
    upsertedId[3]: object(MongoDB\BSON\ObjectId)#5 (1) {
      ["oid"]=>
      string(24) "54d3adc3ce7a792f4d703756"
    }
    upsertedId[4]: int(3)

## Véase también

MongoDB\Driver\BulkWrite

MongoDB\Driver\WriteResult

MongoDB\Driver\WriteConcern

MongoDB\Driver\Server::executeBulkWrite
