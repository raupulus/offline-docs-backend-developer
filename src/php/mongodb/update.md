---
title: MongoDB\Driver\BulkWrite::update
description: Añade una operación de actualización al lote
source_url: https://www.php.net/manual/es/mongodb-driver-bulkwrite.update.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/bulkwrite/update.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48880
---

MongoDB\Driver\BulkWrite::update

Añade una operación de actualización al lote

## Descripción

```php
public MongoDB\Driver\BulkWrite::update(array $filter, array $newObj, [array $updateOptions]): void
```php

Añade una operación de actualización al `MongoDB\Driver\BulkWrite`.

## Parámetros

`filter` (`arrayobject`)  
El [atributo de la consulta](https://www.mongodb.com/docs/manual/tutorial/query-documents/). Un atributo vacío hará coincidir todos los documentos de la colección.

> [!NOTE]
> Al evaluar los criterios de consulta, MongoDB compara los tipos y los valores según sus propias [reglas de comparación para los tipos BSON](https://www.mongodb.com/docs/manual/reference/bson-type-comparison-order/), que difieren de las reglas de [comparación](#types.comparisons) y de [manipulación de tipos](#language.types.type-juggling) de PHP. Al hacer coincidir un tipo BSON especial, los criterios de consulta deben utilizar la [clase BSON](#mongodb.bson) (ej.: utilizar `MongoDB\BSON\ObjectId` para hacer coincidir un [ObjectId](https://www.mongodb.com/docs/manual/reference/bson-types/#objectid)).

`newObj` (`arrayobject`)  
Un documento que contiene operadores de actualización (por ejemplo, `$set`), un documento de reemplazo (es decir, *únicamente* expresiones `campo:valor`), o una [tubería de agregación](https://www.mongodb.com/docs/manual/reference/command/update/#update-with-an-aggregation-pipeline).

`updateOptions`  
<table>
<caption>updateOptions</caption>
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
<td>arrayFilters</td>
<td><code>array</code></td>
<td><p>Un array de documentos de filtro que determina qué elementos de array modificar para una operación de actualización en un campo de array. Consulte <a href="https://www.mongodb.com/docs/manual/reference/command/update/#update-command-arrayfilters">Especificar arrayFilters para operaciones de actualización de arrays</a> en el manual de MongoDB para más información.</p>
<p>Esta opción está disponible en MongoDB 3.6+ y generará una excepción en tiempo de ejecución si se especifica para una versión anterior del servidor.</p></td>
<td></td>
</tr>
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
<td><p>Especificación de índice. Especifique ya sea el nombre del índice como string o el patrón de clave de índice. Si se especifica, entonces el sistema de consultas solo considerará planes que usen el índice indicado.</p>
<p>Esta opción está disponible en MongoDB 4.2+ y generará una excepción en tiempo de ejecución si se especifica para una versión anterior del servidor.</p></td>
<td></td>
</tr>
<tr>
<td>multi</td>
<td><code>bool</code></td>
<td>Actualizar solo el primer documento coincidente si <code>false</code>, o todos los documentos coincidentes <code>true</code>. Esta opción no puede ser <code>true</code> si <code>newObj</code> es un documento de reemplazo.</td>
<td><code>false</code></td>
</tr>
<tr>
<td>sort</td>
<td><code>arrayobject</code></td>
<td><p>Especifica qué documento actualizará la operación si la consulta coincide con múltiples documentos. Se actualizará el primer documento coincidente según el orden de clasificación.</p>
<p>Esta opción no puede usarse si <code>"multi"</code> es <code>true</code>.</p>
<p>Esta opción está disponible en MongoDB 8.0+ y generará una excepción en tiempo de ejecución si se especifica para una versión anterior del servidor.</p></td>
<td></td>
</tr>
<tr>
<td>upsert</td>
<td><code>bool</code></td>
<td>Si <code>filter</code> no coincide con un documento existente, inserta un <em>único</em> documento. El documento se creará a partir de <code>newObj</code> si es un documento de reemplazo (es decir, sin operadores de actualización); de lo contrario, los operadores en <code>newObj</code> se aplicarán a <code>filter</code> para crear el nuevo documento.</td>
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

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 1.21.0 | Se añadió la opción `"sort"`. |
| PECL mongodb 1.7.0 | Se añadió la opción `"hint"`. |
| PECL mongodb 1.6.0 | El parámetro `newObj` ahora acepta una tubería de agregación. Esta característica requiere MongoDB 4.2+ y generará una excepción en tiempo de ejecución si se especifica para una versión anterior del servidor. |
| PECL mongodb 1.5.0 | Usar la opción `"arrayFilters"` generará una excepción en tiempo de ejecución si el servidor no la soporta. Anteriormente, no se generaba ninguna excepción y la opción podía ignorarse. |
| PECL mongodb 1.4.0 | Se añadió la opción `"arrayFilters"`. |
| PECL mongodb 1.2.0 | Se añadió la opción `"collation"`. |

## Ejemplos

Ejemplo de `MongoDB\Driver\BulkWrite::update`

```
<?php

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->update(
    ['x' => 2],
    ['$set' => ['y' => 3]],
    ['multi' => false, 'upsert' => false]
);

$manager = new MongoDB\Driver\Manager('mongodb://localhost:27017');
$result = $manager->executeBulkWrite('db.collection', $bulk);

?>

   
```php

## Véase también

MongoDB\Driver\Manager::executeBulkWrite

MongoDB\Driver\WriteResult
