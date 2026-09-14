---
title: MongoDB\Driver\BulkWrite::delete
description: Añade una operación de eliminación al lote masivo
source_url: https://www.php.net/manual/es/mongodb-driver-bulkwrite.delete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/bulkwrite/delete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48860
---

MongoDB\Driver\BulkWrite::delete

Añade una operación de eliminación al lote masivo

## Descripción

```php
public MongoDB\Driver\BulkWrite::delete(array $filter, [array $deleteOptions]): void
```php

Añade una operación de eliminación al `MongoDB\Driver\BulkWrite`.

## Parámetros

`filter` (`arrayobject`)  
El [atributo de la consulta](https://www.mongodb.com/docs/manual/tutorial/query-documents/). Un atributo vacío hará coincidir todos los documentos de la colección.

> [!NOTE]
> Al evaluar los criterios de consulta, MongoDB compara los tipos y los valores según sus propias [reglas de comparación para los tipos BSON](https://www.mongodb.com/docs/manual/reference/bson-type-comparison-order/), que difieren de las reglas de [comparación](#types.comparisons) y de [manipulación de tipos](#language.types.type-juggling) de PHP. Al hacer coincidir un tipo BSON especial, los criterios de consulta deben utilizar la [clase BSON](#mongodb.bson) (ej.: utilizar `MongoDB\BSON\ObjectId` para hacer coincidir un [ObjectId](https://www.mongodb.com/docs/manual/reference/bson-types/#objectid)).

`deleteOptions`  
<table>
<caption>deleteOptions</caption>
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
<td><p>Especificación del índice. Especifique ya sea el nombre del índice como un string o el patrón de clave del índice. Si se especifica, entonces el sistema de consultas solo considerará planes que utilicen el índice indicado.</p>
<p>Esta opción está disponible en MongoDB 4.4+ y generará una excepción en tiempo de ejecución si se especifica para una versión anterior del servidor.</p></td>
<td></td>
</tr>
<tr>
<td>limit</td>
<td><code>bool</code></td>
<td>Eliminar todos los documentos coincidentes (<code>false</code>), o solo el primer documento coincidente (<code>true</code>)</td>
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

| Versión            | Descripción                        |
|--------------------|------------------------------------|
| PECL mongodb 1.8.0 | Se añadió la opción `"hint"`.      |
| PECL mongodb 1.2.0 | Se añadió la opción `"collation"`. |

## Ejemplos

Ejemplo de `MongoDB\Driver\BulkWrite::delete`

```
<?php

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->delete(['x' => 1], ['limit' => 1]);
$bulk->delete(['x' => 2], ['limit' => 0]);

$manager = new MongoDB\Driver\Manager('mongodb://localhost:27017');
$result = $manager->executeBulkWrite('db.collection', $bulk);

?>

   
```php

## Véase también

MongoDB\Driver\Manager::executeBulkWrite

MongoDB\Driver\WriteResult
