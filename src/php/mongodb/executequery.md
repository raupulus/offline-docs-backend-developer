---
title: MongoDB\Driver\Manager::executeQuery
description: Ejecuta una consulta de base de datos
source_url: https://www.php.net/manual/es/mongodb-driver-manager.executequery.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/manager/executequery.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_revision: 6047c10c1
order: 49750
---

MongoDB\Driver\Manager::executeQuery

Ejecuta una consulta de base de datos

## Descripción

```php
final public MongoDB\Driver\Manager::executeQuery(string $namespace, MongoDB\Driver\Query $query, [array $options]): MongoDB\Driver\Cursor
```php

Selecciona un servidor en función de la opción `"readPreference"` y ejecuta la consulta en ese servidor.

Los valores por omisión de la opción `"readPreference"` y de la opción `"readConcern"` de la consulta serán deducidos a partir de una transacción activa (indicada por la opción `"session"`), seguida de la [URI de conexión](#mongodb-driver-manager.construct-uri).

## Parámetros

`namespace` (`string`)  
Un espacio de nombres completamente calificado (ej. `"databaseName.collectionName"`)

`query` (`MongoDB\Driver\Query`)  
La consulta a ejecutar.

`options`  
| Opción | Tipo | Descripción |
|----|----|----|
| readPreference | `MongoDB\Driver\ReadPreference` | Una preferencia de lectura a utilizar para seleccionar un servidor para la operación. |
| session | `MongoDB\Driver\Session` | Una sesión a asociar a la operación. |

options

## Valores devueltos

Retorna un `MongoDB\Driver\Cursor` en caso de éxito.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una excepción

MongoDB\Driver\Exception\ConnectionException

si la conexión al servidor falla por una razón distinta a un problema de identificación

Lanza una excepción

MongoDB\Driver\Exception\AuthenticationException

si se requiere una identificación pero falla

Lanza una

MongoDB\Driver\Exception\RuntimeException

en caso de otro error (por ejemplo: operadores de consulta inválidos).

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 2.0.0 | El parámetro `options` ya no acepta una instancia de `MongoDB\Driver\ReadPreference`. |
| PECL mongodb 1.21.0 | Pasar un objeto `MongoDB\Driver\ReadPreference` como `options` está obsoleto y será eliminado en la 2.0. |
| PECL mongodb 1.4.0 | El tercer parámetro es ahora un array `options`. Por razones de compatibilidad ascendente, este parámetro siempre aceptará un objeto `MongoDB\Driver\ReadPreference`. |

## Ejemplos

Ejemplo de `MongoDB\Driver\Manager::executeQuery`

```
<?php

$manager = new MongoDB\Driver\Manager("mongodb://localhost:27017");

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['x' => 1]);
$bulk->insert(['x' => 2]);
$bulk->insert(['x' => 3]);
$manager->executeBulkWrite('db.collection', $bulk);

$filter = ['x' => ['$gt' => 1]];
$options = [
    'projection' => ['_id' => 0],
    'sort' => ['x' => -1],
];

$query = new MongoDB\Driver\Query($filter, $options);
$cursor = $manager->executeQuery('db.collection', $query);

foreach ($cursor as $document) {
    var_dump($document);
}

?>

   
```php

El ejemplo anterior mostrará:

    object(stdClass)#6 (1) {
      ["x"]=>
      int(3)
    }
    object(stdClass)#7 (1) {
      ["x"]=>
      int(2)
    }

Limitar el tiempo de ejecución de una consulta

La opción `"maxTimeMS"` de la clase `MongoDB\Driver\Query` puede ser utilizada para limitar el tiempo de ejecución de una consulta. Tenga en cuenta que este límite de tiempo es aplicado en el lado del servidor y no tiene en cuenta la latencia de la red. Ver [Terminar las operaciones en curso ](https://www.mongodb.com/docs/manual/tutorial/terminate-running-operations/#maxtimems) en el manual de MongoDB para más información.

```
<?php

$manager = new MongoDB\Driver\Manager('mongodb://localhost:27017');

$filter = ['x' => ['$gt' => 1]];
$options = [
    'maxTimeMS' => 1000,
];

$query = new MongoDB\Driver\Query($filter, $options);
$cursor = $manager->executeQuery('db.collection', $query);

foreach ($cursor as $document) {
    var_dump($document);
}

?>

   
```php

Si la consulta no logra terminar después de un segundo de ejecución en el servidor, una `MongoDB\Driver\Exception\ExecutionTimeoutException` será lanzada.

## Véase también

MongoDB\Driver\Cursor

MongoDB\Driver\Query

MongoDB\Driver\ReadPreference

MongoDB\Driver\Server::executeQuery
