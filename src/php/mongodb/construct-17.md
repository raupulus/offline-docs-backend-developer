---
title: MongoDB\Driver\BulkWrite::__construct
description: Crea un nuevo BulkWrite
source_url: https://www.php.net/manual/es/mongodb-driver-bulkwrite.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/bulkwrite/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48840
---

MongoDB\Driver\BulkWrite::\_\_construct

Crea un nuevo BulkWrite

## Descripción

```php
public MongoDB\Driver\BulkWrite::__construct([array $options])
```php

Construye un nuevo `MongoDB\Driver\BulkWrite`, que es un objeto mutable al cual se pueden añadir una o más operaciones de escritura. Las escritura(s) pueden entonces ser ejecutadas con MongoDB\Driver\Manager::executeBulkWrite.

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
<td><p>Si es <code>true</code>, permite que las operaciones de inserción y actualización eviten la validación a nivel de documento.</p>
<p>Esta opción está disponible en MongoDB 3.2+ y es ignorada en versiones anteriores del servidor, que no soportan validación a nivel de documento.</p></td>
<td><code>false</code></td>
</tr>
<tr>
<td>comment</td>
<td><code>mixed</code></td>
<td><p>Un comentario arbitrario para ayudar a rastrear la operación a través del perfilador de la base de datos, la salida currentOp y los registros.</p>
<p>Esta opción está disponible en MongoDB 4.4+ y generará una excepción en tiempo de ejecución si se especifica para una versión anterior del servidor.</p></td>
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
<td>Las operaciones ordenadas (<code>true</code>) se ejecutan de forma serial en el servidor de MongoDB, mientras que las operaciones no ordenadas (<code>false</code>) son enviadas al servidor en un orden arbitrario y pueden ser ejecutadas en paralelo.</td>
<td><code>true</code></td>
</tr>
</tbody>
</table>

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Historial de cambios

| Versión             | Descripción                                       |
|---------------------|---------------------------------------------------|
| PECL mongodb 1.14.0 | Se añadieron las opciones `"comment"` y `"let"`.  |
| PECL mongodb 1.1.0  | Se añadió la opción `"bypassDocumentValidation"`. |

## Ejemplos

Ejemplo de `MongoDB\Driver\BulkWrite::__construct`

```
<?php

$bulk = new MongoDB\Driver\BulkWrite(['ordered' => true]);
$bulk->delete([]);
$bulk->insert(['_id' => 1, 'x' => 1]);
$bulk->insert(['_id' => 2, 'x' => 2]);
$bulk->update(
    ['x' => 2],
    ['$set' => ['x' => 1]],
    ['limit' => 1, 'upsert' => false]
);
$bulk->delete(['x' => 1], ['limit' => 1]);
$bulk->update(
    ['_id' => 3],
    ['$set' => ['x' => 3]],
    ['limit' => 1, 'upsert' => true]
);

$manager = new MongoDB\Driver\Manager('mongodb://localhost:27017');
$writeConcern = new MongoDB\Driver\WriteConcern(1);

try {
    $result = $manager->executeBulkWrite('db.collection', $bulk, ['writeConcern' => $writeConcern]);
} catch (MongoDB\Driver\Exception\BulkWriteException $e) {
    $result = $e->getWriteResult();

    // Comprobar si la preocupación de escritura no pudo ser cumplida
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
printf("Incluidos %d documento(s)\n", $result->getUpsertedCount());
printf("Eliminados %d documento(s)\n", $result->getDeletedCount());

?>

   
```php

El ejemplo anterior mostrará:

    Insertados 2 documento(s)
    Actualizados  1 documento(s)
    Incluidos 1 documento(s)
    Eliminados  1 documento(s)

## Véase también

MongoDB\Driver\Manager::executeBulkWrite

MongoDB\Driver\WriteResult
