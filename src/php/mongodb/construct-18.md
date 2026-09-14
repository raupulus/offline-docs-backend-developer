---
title: MongoDB\Driver\BulkWriteCommand::__construct
description: Crea un nuevo BulkWriteCommand
source_url: https://www.php.net/manual/es/mongodb-driver-bulkwritecommand.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/bulkwritecommand/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48900
---

MongoDB\Driver\BulkWriteCommand::\_\_construct

Crea un nuevo BulkWriteCommand

## Descripción

```php
public MongoDB\Driver\BulkWriteCommand::__construct([array $options])
```php

Construye un nuevo `MongoDB\Driver\BulkWriteCommand`, que puede usarse para realizar muchas operaciones de inserción, actualización y eliminación en múltiples colecciones en una sola petición usando el [comando bulkWrite](https://www.mongodb.com/docs/manual/reference/command/bulkWrite) introducido en MongoDB 8.0. Esto difiere de `MongoDB\Driver\BulkWrite`, que es compatible con todas las versiones del servidor pero limitado a una sola colección.

Después de añadir todas las operaciones de escritura, este objeto puede ejecutarse con MongoDB\Driver\Manager::executeBulkWriteCommand.

## Parámetros

`options` (`array`)  
<table>
<caption>options</caption>
<thead>
<tr>
<th>Opción</th>
<th>Tipo</th>
<th>Descripción</th>
<th>Valor por omisión</th>
</tr>
</thead>
<tbody>
<tr>
<td>bypassDocumentValidation</td>
<td><code>bool</code></td>
<td><p>Si es <code>true</code>, permite que las operaciones de inserción y actualización eviten la validación a nivel de documento.</p></td>
<td><code>false</code></td>
</tr>
<tr>
<td>comment</td>
<td><code>mixed</code></td>
<td><p>Un comentario arbitrario para ayudar a rastrear la operación a través del perfilador de la base de datos, la salida de currentOp y los registros.</p></td>
<td></td>
</tr>
<tr>
<td>let</td>
<td><code>arrayobject</code></td>
<td><p>Diccionario de nombres y valores de parámetros. Los valores deben ser constantes o expresiones cerradas que no hagan referencia a campos del documento. Los parámetros pueden ser accedidos luego como variables en un contexto de expresión agregada (por ejemplo <code>$$var</code>).</p>
<p>Esta opción está disponible en MongoDB 5.0+ y resultará en una excepción en tiempo de ejecución si es especificada para una versión anterior del servidor.</p></td>
<td></td>
</tr>
<tr>
<td>ordered</td>
<td><code>bool</code></td>
<td><p>Si las operaciones en esta escritura masiva deben ejecutarse en el orden en que fueron especificadas. Si es <code>false</code>, las escrituras continuarán ejecutándose si una escritura individual falla. Si es <code>true</code>, las escrituras se detendrán si una escritura individual falla.</p></td>
<td><code>true</code></td>
</tr>
<tr>
<td>verboseResults</td>
<td><code>bool</code></td>
<td><p>Si los resultados detallados de cada operación exitosa deben incluirse en el <code>MongoDB\Driver\BulkWriteCommandResult</code> devuelto.</p></td>
<td><code>false</code></td>
</tr>
</tbody>
</table>

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo de `MongoDB\Driver\BulkWriteCommand::__construct`

```
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

   
```php

El ejemplo anterior mostrará:

    Insertados 3 documento(s)
    Actualizados 1 documento(s)

## Véase también

MongoDB\Driver\Manager::executeBulkWriteCommand

MongoDB\Driver\BulkWriteCommandResult
