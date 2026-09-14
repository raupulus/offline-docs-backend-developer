---
title: MongoDB\Driver\Manager::executeCommand
description: Ejecuta un comando de base de datos
source_url: https://www.php.net/manual/es/mongodb-driver-manager.executecommand.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/manager/executecommand.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_revision: 6047c10c1
order: 49740
---

MongoDB\Driver\Manager::executeCommand

Ejecuta un comando de base de datos

## Descripción

```php
final public MongoDB\Driver\Manager::executeCommand(string $db, MongoDB\Driver\Command $command, [array $options]): MongoDB\Driver\Cursor
```php

Selecciona un servidor en función de la opción `"readPreference"` y ejecuta el comando en ese servidor.

Este método no aplica ninguna lógica especial al comando. Los valores por defecto de las opciones `"readPreference"`, `"readConcern"` y `"writeConcern"` serán deducidos a partir de una transacción activa (indicada por la opción `"session"`). Si no hay una transacción activa, se utilizará una preferencia de lectura primaria para la selección del servidor.

Los valores por defecto no serán *no* deducidos a partir de la [URI de conexión](#mongodb-driver-manager.construct-uri). Por lo tanto, se recomienda a los usuarios utilizar métodos de comando de lectura y/o escritura específicos si es posible.

## Parámetros

`db` (`string`)  
El nombre de la base de datos sobre la cual se ejecutará el comando.

`command` (`MongoDB\Driver\Command`)  
El comando a ejecutar.

`options`  
<table>
<caption>options</caption>
<thead>
<tr>
<th>Opción</th>
<th>Tipo</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>readConcern</td>
<td><code>MongoDB\Driver\ReadConcern</code></td>
<td><p>Una preocupación de lectura a aplicar a la operación.</p>
<p>Esta opción está disponible en MongoDB 3.2+ y se traducirá en una excepción en el momento de la ejecución si se especifica para una versión más antigua del servidor.</p></td>
</tr>
<tr>
<td>readPreference</td>
<td><code>MongoDB\Driver\ReadPreference</code></td>
<td><p>Una preferencia de lectura a utilizar para seleccionar un servidor para la operación.</p></td>
</tr>
<tr>
<td>session</td>
<td><code>MongoDB\Driver\Session</code></td>
<td><p>Una sesión a asociar a la operación.</p></td>
</tr>
<tr>
<td>writeConcern</td>
<td><code>MongoDB\Driver\WriteConcern</code></td>
<td><p>Una preocupación de escritura a aplicar a la operación.</p></td>
</tr>
</tbody>
</table>

> [!WARNING]
> Si se utiliza una `"session"` que tiene una transacción en curso, no se puede especificar la opción `"readConcern"` o `"writeConcern"`. Intentar hacer esto lanzará una excepción `MongoDB\Driver\Exception\InvalidArgumentException` . En su lugar, debe definir estas opciones cuando se crea la transacción con MongoDB\Driver\Session::startTransaction.

## Valores devueltos

Retorna un `MongoDB\Driver\Cursor` en caso de éxito.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

si la opción

"session"

se utiliza con una transacción asociada en combinación con una opción

"readConcern"

o

"writeConcern"

.

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

Lanza una

MongoDB\Driver\Exception\RuntimeException

en otros errores (por ejemplo: comando inválido, entrega de un comando de escritura a un secundario).

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 2.0.0 | El parámetro `options` ya no acepta una instancia de `MongoDB\Driver\ReadPreference`. |
| PECL mongodb 1.21.0 | Pasar un objeto `MongoDB\Driver\ReadPreference` como `options` está obsoleto y será eliminado en la 2.0. |
| PECL mongodb 1.4.4 | Se lanzará una `MongoDB\Driver\Exception\InvalidArgumentException` si la opción `"session"` se utiliza en combinación con una preferencia de escritura no reconocida. |
| PECL mongodb 1.4.0 | Este tercer parámetro es ahora un array de `options`. Por razones de compatibilidad ascendente, este parámetro siempre aceptará un objeto `MongoDB\Driver\ReadPreference`. |

## Ejemplos

`MongoDB\Driver\Manager::executeCommand` con un comando que devuelve un solo documento de resultado

```
<?php

$manager = new MongoDB\Driver\Manager('mongodb://localhost:27017');
$command = new MongoDB\Driver\Command(['ping' => 1]);

try {
    $cursor = $manager->executeCommand('admin', $command);
} catch(MongoDB\Driver\Exception $e) {
    echo $e->getMessage(), "\n";
    exit;
}

/* El comando ping devuelve un solo documento de resultado, por lo que
 * se debe acceder al primer resultado en el cursor. */
$response = $cursor->toArray()[0];

var_dump($response);

?>

   
```php

El ejemplo anterior mostrará:

    array(1) {
      ["ok"]=>
      float(1)
    }

`MongoDB\Driver\Manager::executeCommand` con un comando que devuelve un cursor

```
<?php

$manager = new MongoDB\Driver\Manager("mongodb://localhost:27017");

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['x' => 1, 'y' => 'foo']);
$bulk->insert(['x' => 2, 'y' => 'bar']);
$bulk->insert(['x' => 3, 'y' => 'bar']);
$manager->executeBulkWrite('db.collection', $bulk);

$command = new MongoDB\Driver\Command([
    'aggregate' => 'collection',
    'pipeline' => [
        ['$group' => ['_id' => '$y', 'sum' => ['$sum' => '$x']]],
    ],
    'cursor' => new stdClass,
]);
$cursor = $manager->executeCommand('db', $command);

/* El comando de agregación puede eventualmente devolver sus resultados en
 * un cursor en lugar de un solo documento de resultado. En este caso, se puede
 * iterar directamente sobre el cursor para acceder a estos resultados. */
foreach ($cursor as $document) {
    var_dump($document);
}

?>

   
```php

El ejemplo anterior mostrará:

    object(stdClass)#6 (2) {
      ["_id"]=>
      string(3) "bar"
      ["sum"]=>
      int(10)
    }
    object(stdClass)#7 (2) {
      ["_id"]=>
      string(3) "foo"
      ["sum"]=>
      int(2)
    }

Limitar el tiempo de ejecución de un comando

El tiempo de ejecución de un comando puede ser limitado especificando un valor para `"maxTimeMS"` en el documento `MongoDB\Driver\Command`. Tenga en cuenta que este límite de tiempo se aplica en el lado del servidor y no tiene en cuenta la latencia de la red. Ver [Terminar las operaciones en curso ](https://www.mongodb.com/docs/manual/tutorial/terminate-running-operations/#maxtimems) en el manual de MongoDB para más información.

```
<?php

$manager = new MongoDB\Driver\Manager('mongodb://localhost:27017');

$command = new MongoDB\Driver\Command([
    'count' => 'collection',
    'query' => ['x' => ['$gt' => 1]],
    'maxTimeMS' => 1000,
]);

$cursor = $manager->executeCommand('db', $command);

var_dump($cursor->toArray()[0]);

?>

   
```php

Si el comando no logra completarse después de un segundo de ejecución en el servidor, se lanzará una `MongoDB\Driver\Exception\ExecutionTimeoutException`.

## Notas

> [!NOTE]
> Si se utiliza una segunda `readPreference`, es responsabilidad del llamante asegurarse de que el `comando` pueda ser ejecutado en un secundario. No se realiza ninguna validación por parte del controlador.

> [!NOTE]
> Este método no utiliza por defecto la preferencia de lectura de la [URI de conexión MongoDB](#mongodb-driver-manager.construct-uri). Las aplicaciones que lo necesiten deberían considerar el uso de `MongoDB\Driver\Manager::executeReadCommand`.

## Véase también

MongoDB\Driver\Command

MongoDB\Driver\Cursor

MongoDB\Driver\Manager::executeReadCommand

MongoDB\Driver\Manager::executeReadWriteCommand

MongoDB\Driver\Manager::executeWriteCommand

MongoDB\Driver\Server::executeCommand
