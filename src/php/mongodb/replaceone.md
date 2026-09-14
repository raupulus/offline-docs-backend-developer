---
title: MongoDB\Driver\BulkWriteCommand::replaceOne
description: Añade una operación replaceOne
source_url: https://www.php.net/manual/es/mongodb-driver-bulkwritecommand.replaceone.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/bulkwritecommand/replaceone.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 8e2cfbdce
order: 48950
---

MongoDB\Driver\BulkWriteCommand::replaceOne

Añade una operación replaceOne

## Descripción

```php
public MongoDB\Driver\BulkWriteCommand::replaceOne(string $namespace, array $filter, array $replacement, [array $options]): void
```php

Añade una operación replaceOne al `MongoDB\Driver\BulkWriteCommand`. El primer documento que coincida con `filter` en la colección identificada por `namespace` será reemplazado.

## Parámetros

`namespace` (`string`)  
Un espacio de nombres completamente calificado (ej. `"databaseName.collectionName"`)

`filter` (`arrayobject`)  
El [atributo de la consulta](https://www.mongodb.com/docs/manual/tutorial/query-documents/). Un atributo vacío hará coincidir todos los documentos de la colección.

> [!NOTE]
> Al evaluar los criterios de consulta, MongoDB compara los tipos y los valores según sus propias [reglas de comparación para los tipos BSON](https://www.mongodb.com/docs/manual/reference/bson-type-comparison-order/), que difieren de las reglas de [comparación](#types.comparisons) y de [manipulación de tipos](#language.types.type-juggling) de PHP. Al hacer coincidir un tipo BSON especial, los criterios de consulta deben utilizar la [clase BSON](#mongodb.bson) (ej.: utilizar `MongoDB\BSON\ObjectId` para hacer coincidir un [ObjectId](https://www.mongodb.com/docs/manual/reference/bson-types/#objectid)).

`replacement` (`arrayobject`)  
Un documento de reemplazo.

`options`  
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
<td>collation</td>
<td><code>arrayobject</code></td>
<td><p><a href="https://www.mongodb.com/docs/upcoming/reference/collation/">Collation</a> permite a los usuarios especificar reglas específicas del lenguaje para la comparación de cadenas, por ejemplo, reglas para mayúsculas o acentos. Al especificar una collation, el campo <code>"locale"</code> es obligatorio; todos los demás campos de la collation son opcionales. Para la descripción de estos campos, consúltese el <a href="https://www.mongodb.com/docs/upcoming/reference/collation/#collation-document">documento Collation</a>.</p>
<p>Si la collation no es especificada pero la colección tiene una collation predeterminada, la operación utilizará la collation especificada para la colección. Si ninguna collation es especificada para la colección o para la operación, MongoDB utilizará el binario simple de comparación utilizado en versiones anteriores para las comparaciones de cadenas.</p>
<p>Esta opción está disponible en MongoDB 3.4+ y una excepción será emitida en tiempo de ejecución si es especificada en una versión anterior.</p></td>
<td></td>
</tr>
<tr>
<td>hint</td>
<td><code>stringarrayobject</code></td>
<td><p>Especificación de índice. Especifique ya sea el nombre del índice como string o el patrón de clave del índice. Si se especifica, entonces el sistema de consultas solo considerará planes que usen el índice indicado.</p></td>
<td></td>
</tr>
<tr>
<td>sort</td>
<td><code>arrayobject</code></td>
<td><p>Especifique qué documento reemplaza la operación si la consulta coincide con múltiples documentos. El primer documento coincidente según el orden de clasificación será reemplazado.</p></td>
<td></td>
</tr>
<tr>
<td>upsert</td>
<td><code>bool</code></td>
<td>Si <code>filter</code> no coincide con un documento existente, inserta un <em>único</em> documento. El documento será creado a partir de <code>replacement</code>.</td>
<td><code>false</code></td>
</tr>
</tbody>
</table>

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo de `MongoDB\Driver\BulkWriteCommand::replaceOne`

```
<?php

$manager = new MongoDB\Driver\Manager;

$bulk = new MongoDB\Driver\BulkWriteCommand;
$bulk->replaceOne('db.coll', ['x' => 1], ['x' => 1, 'y' => 2]);

$result = $manager->executeBulkWriteCommand($bulk);

?>

   
```php

## Véase también

MongoDB\Driver\BulkWriteCommand::updateOne

MongoDB\Driver\BulkWriteCommand::updateMany

MongoDB\Driver\Manager::executeBulkWriteCommand

MongoDB\Driver\BulkWriteCommandResult
