---
title: MongoDB\Driver\Query::__construct
description: Crear una nueva consulta
source_url: https://www.php.net/manual/es/mongodb-driver-query.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/query/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50790
---

MongoDB\Driver\Query::\_\_construct

Crear una nueva consulta

## Descripción

```php
final public MongoDB\Driver\Query::__construct(array $filter, [array $queryOptions])
```php

Construye un nuevo objeto `MongoDB\Driver\Query`, que es un objeto de valor inmutable que representa una consulta de base de datos. La consulta puede luego ser ejecutada con MongoDB\Driver\Manager::executeQuery.

## Parámetros

`filter` (`arrayobject`)  
El [atributo de la consulta](https://www.mongodb.com/docs/manual/tutorial/query-documents/). Un atributo vacío hará coincidir todos los documentos de la colección.

> [!NOTE]
> Al evaluar los criterios de consulta, MongoDB compara los tipos y los valores según sus propias [reglas de comparación para los tipos BSON](https://www.mongodb.com/docs/manual/reference/bson-type-comparison-order/), que difieren de las reglas de [comparación](#types.comparisons) y de [manipulación de tipos](#language.types.type-juggling) de PHP. Al hacer coincidir un tipo BSON especial, los criterios de consulta deben utilizar la [clase BSON](#mongodb.bson) (ej.: utilizar `MongoDB\BSON\ObjectId` para hacer coincidir un [ObjectId](https://www.mongodb.com/docs/manual/reference/bson-types/#objectid)).

`queryOptions`  
<table id="mongodb-driver-query.construct-queryOptions">
<caption>queryOptions</caption>
<thead>
<tr>
<th>Opción</th>
<th>Tipo</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>allowDiskUse</td>
<td><code>bool</code></td>
<td><p>Autoriza a MongoDB a utilizar ficheros temporales en el disco para almacenar datos que excedan el límite de memoria del sistema de 100 megabytes al procesar una operación de clasificación bloqueante.</p></td>
</tr>
<tr>
<td>allowPartialResults</td>
<td><code>bool</code></td>
<td><p>Para las consultas en una colección fragmentada, devuelve resultados parciales del mongos si algunos fragmentos no están disponibles en lugar de generar un error.</p>
<p>Retoma la opción deprecada <code>"partial"</code> si no se especifica.</p></td>
</tr>
<tr>
<td>awaitData</td>
<td><code>bool</code></td>
<td>Utilizar en conjunción con la opción <code>"tailable"</code> para bloquear temporalmente una operación getMore en el cursor si al final de los datos en lugar de no devolver datos. Después de un período de espera, la consulta termina normalmente.</td>
</tr>
<tr>
<td>batchSize</td>
<td><code>int</code></td>
<td><p>El número de documentos a devolver en el primer lote. Por omisión a 101. Un tamaño de lote de 0 significa que el cursor será establecido, pero ningún documento será devuelto en el primer lote.</p>
<p>En las versiones de MongoDB anteriores a 3.2, donde las consultas utilizan el protocolo de filaire heredado OP_QUERY, un tamaño de lote de 1 cerrará el cursor independientemente del número de documentos.</p></td>
</tr>
<tr>
<td>collation</td>
<td><code>arrayobject</code></td>
<td><p><a href="https://www.mongodb.com/docs/upcoming/reference/collation/">Collation</a> permite a los usuarios especificar reglas específicas del lenguaje para la comparación de cadenas, por ejemplo, reglas para mayúsculas o acentos. Al especificar una collation, el campo <code>"locale"</code> es obligatorio; todos los demás campos de la collation son opcionales. Para la descripción de estos campos, consúltese el <a href="https://www.mongodb.com/docs/upcoming/reference/collation/#collation-document">documento Collation</a>.</p>
<p>Si la collation no es especificada pero la colección tiene una collation predeterminada, la operación utilizará la collation especificada para la colección. Si ninguna collation es especificada para la colección o para la operación, MongoDB utilizará el binario simple de comparación utilizado en versiones anteriores para las comparaciones de cadenas.</p>
<p>Esta opción está disponible en MongoDB 3.4+ y una excepción será emitida en tiempo de ejecución si es especificada en una versión anterior.</p></td>
</tr>
<tr>
<td>comment</td>
<td><code>mixed</code></td>
<td><p>Un comentario arbitrario para ayudar a rastrear la operación a través del perfil de la base de datos, la salida currentOp y los registros.</p>
<p>El comentario puede ser cualquier tipo BSON válido para MongoDB 4.4+. Las versiones de servidor anteriores solo admiten valores de cadena.</p>
<p>Retoma la opción deprecada <code>"$comment"</code> si no se especifica.</p></td>
</tr>
<tr>
<td>exhaust</td>
<td><code>bool</code></td>
<td><p>El flujo de datos aguas abajo a plena potencia en varios paquetes "more", asumiendo que el cliente leerá completamente todos los datos consultados. Más rápido cuando se extraen muchos datos y se sabe que se quiere extraer todo. Nota: el cliente no está autorizado a no leer todos los datos a menos que cierre la conexión.</p>
<p>Esta opción no es admitida por el comando find en MongoDB 3.2+ y forzará al controlador a utilizar la versión del protocolo de filaire heredado (es decir, OP_QUERY).</p></td>
</tr>
<tr>
<td>explain</td>
<td><code>bool</code></td>
<td><p>Si <code>true</code> el cursor <code>MongoDB\Driver\Cursor</code> devuelto contendrá un solo documento que describe el proceso y los índices utilizados para devolver la consulta.</p>
<p>Retoma la opción deprecada <code>"$explain"</code> si no se especifica.</p>
<p>Esta opción no es admitida por el comando find en MongoDB 3.2+ y solo será respetada al utilizar la versión del protocolo de filaire heredado (es decir, OP_QUERY). El comando <a href="https://www.mongodb.com/docs/manual/reference/command/explain/">explain</a> debe ser utilizado en MongoDB 3.0+.</p></td>
</tr>
<tr>
<td>hint</td>
<td><code>stringarrayobject</code></td>
<td><p>Especificación del índice. Especifique el nombre del índice como cadena, o el patrón de clave de índice. Si se especifica, el sistema de consulta solo considerará los planes que utilicen el índice sugerido.</p>
<p>Retoma la opción deprecada <code>"hint"</code> si no se especifica.</p></td>
</tr>
<tr>
<td>let</td>
<td><code>arrayobject</code></td>
<td><p>Diccionario de nombres y valores de parámetros. Los valores deben ser constantes o expresiones cerradas que no hagan referencia a campos del documento. Los parámetros pueden ser accedidos luego como variables en un contexto de expresión agregada (por ejemplo <code>$$var</code>).</p>
<p>Esta opción está disponible en MongoDB 5.0+ y resultará en una excepción en tiempo de ejecución si es especificada para una versión anterior del servidor.</p></td>
</tr>
<tr>
<td>limit</td>
<td><code>int</code></td>
<td><p>El número máximo de documentos a devolver. Si no se especifica, entonces por omisión a ningún límite. Un límite de 0 es equivalente a no establecer un límite.</p></td>
</tr>
<tr>
<td>max</td>
<td><code>arrayobject</code></td>
<td><p>El límite superior <em>exclusivo</em> para un índice específico.</p>
<p>Retoma la opción deprecada <code>"$max"</code> si no se especifica.</p></td>
</tr>
<tr>
<td>maxAwaitTimeMS</td>
<td><code>int</code></td>
<td><p>Entero positivo que indica el límite de tiempo en milisegundos para que el servidor bloquee una operación getMore si no hay datos disponibles. Esta opción solo debe ser utilizada en conjunción con las opciones <code>"tailable"</code> y <code>"awaitData"</code>.</p></td>
</tr>
<tr>
<td>maxTimeMS</td>
<td><code>int</code></td>
<td><p>El límite de tiempo acumulativo en milisegundos para el procesamiento de las operaciones en el cursor. MongoDB detiene la operación en el primer punto de interrupción más cercano.</p>
<p>Retoma la opción deprecada <code>"$maxTimeMS"</code> si no se especifica.</p></td>
</tr>
<tr>
<td>min</td>
<td><code>arrayobject</code></td>
<td><p>El límite inferior <em>inclusivo</em> para un índice específico.</p>
<p>Retoma la opción deprecada <code>"$min"</code> si no se especifica.</p></td>
</tr>
<tr>
<td>noCursorTimeout</td>
<td><code>bool</code></td>
<td>Evita que el servidor finalice los cursores inactivos después de un período de inactividad (10 minutos).</td>
</tr>
<tr>
<td>projection</td>
<td><code>arrayobject</code></td>
<td><p>Las <a href="https://www.mongodb.com/docs/manual/tutorial/project-fields-from-query-results/">especificaciones de proyección</a> para determinar qué campos incluir en los documentos devueltos.</p>
<p>Si se utiliza la <a href="#mongodb.persistence.deserialization">funcionalidad ODM</a> para deserializar los documentos como su clase PHP original, asegúrese de incluir el campo __pclass en la proyección. Esto es necesario para que la deserialización funcione y sin ello, la extensión devolverá (por omisión) un objeto <code>stdClass</code> en su lugar.</p></td>
</tr>
<tr>
<td>readConcern</td>
<td><code>MongoDB\Driver\ReadConcern</code></td>
<td><p>Un read concern a aplicar a la operación. Por omisión, el read concern de la <a href="#mongodb-driver-manager.construct-uri">URI de conexión MongoDB</a> será utilizado.</p>
<p>Esta opción está disponible en MongoDB 3.2+ y provocará una excepción en el momento de la ejecución si se especifica para una versión de servidor más antigua.</p></td>
</tr>
<tr>
<td>returnKey</td>
<td><code>bool</code></td>
<td><p>Si <code>true</code>, solo devuelve las claves de índice en los documentos resultantes. El valor por omisión es <code>false</code>. Si <code>true</code> y la comando find no utiliza un índice, los documentos devueltos estarán vacíos.</p>
<p>Retoma la opción deprecada <code>"$returnKey"</code> si no se especifica.</p></td>
</tr>
<tr>
<td>showRecordId</td>
<td><code>bool</code></td>
<td><p>Determina si el identificador de registro debe ser devuelto para cada documento. Si <code>true</code>, añade un campo <code>"$recordId"</code> de primer nivel a los documentos devueltos.</p>
<p>Retoma la opción deprecada <code>"$showDiskLoc"</code> si no se especifica.</p></td>
</tr>
<tr>
<td>singleBatch</td>
<td><code>bool</code></td>
<td>Determina si el cursor debe ser cerrado después del primer lote. Por omisión a <code>false</code>.</td>
</tr>
<tr>
<td>skip</td>
<td><code>int</code></td>
<td>Número de documentos a saltar. Por omisión a 0.</td>
</tr>
<tr>
<td>sort</td>
<td><code>arrayobject</code></td>
<td><p>La especificación de clasificación para el ordenamiento de los resultados.</p>
<p>Retoma la opción deprecada <code>"$orderby"</code> si no se especifica.</p></td>
</tr>
<tr>
<td>tailable</td>
<td><code>bool</code></td>
<td>Devuelve un cursor tailable para una colección acotada.</td>
</tr>
</tbody>
</table>

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Historial de cambios

<table>
<thead>
<tr>
<th>Versión</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>PECL mongodb 2.0.0</td>
<td><p>La opción <code>"partial"</code> ha sido eliminada. Utilice <code>"allowPartialResults"</code> en su lugar.</p>
<p>La opción <code>"maxScan"</code> ha sido eliminada. El soporte para esta opción ha sido eliminado en MongoDB 4.2.</p>
<p>La opción <code>"modifiers"</code> ha sido eliminada. Esta opción era utilizada para los modificadores de consulta antigua, que están todos deprecados.</p>
<p>La opción <code>"oplogReplay"</code> ha sido eliminada. Esto es ignorado en MongoDB 4.4 y versiones más recientes.</p>
<p>La opción <code>"snapshot"</code> ha sido eliminada. Su soporte ha sido eliminado en MongoDB 4.0.</p>
<p>Un valor negativo para la opción <code>"limit"</code> ya no implica <code>true</code> para la opción <code>"singleBatch"</code>. Para recibir solo un lote de resultados, combine un valor positivo <code>"limit"</code> con la opción <code>"singleBatch"</code>.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.14.0</td>
<td><p>Añadida la opción <code>"let"</code>. La opción <code>"comment"</code> ahora acepta cualquier tipo.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.8.0</td>
<td><p>Añadida la opción <code>"allowDiskUse"</code>.</p>
<p>La opción <code>"oplogReplay"</code> está deprecada.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.5.0</td>
<td><p>Las opciones <code>"maxScan"</code> y <code>"snapshot"</code> están deprecadas.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.3.0</td>
<td><p>Añadida la opción <code>"maxAwaitTimeMS"</code></p></td>
</tr>
<tr>
<td>PECL mongodb 1.2.0</td>
<td><p>Añadidas las opciones <code>"allowPartialResults"</code>, <code>"collation"</code>, <code>"comment"</code>, <code>"hint"</code>, <code>"max"</code>, <code>"maxScan"</code>, <code>"maxTimeMS"</code>, <code>"min"</code>, <code>"returnKey"</code>, <code>"showRecordId"</code>, y <code>"snapshot"</code>.</p>
<p>Renombrada la opción <code>"partial"</code> a <code>"allowPartialResults"</code>. Por compatibilidad ascendente, <code>"partial"</code> será siempre leído si <code>"allowPartialResults"</code> no está especificado.</p>
<p>Eliminada la opción <code>"secondaryOk"</code> obsoleta. Para las consultas que utilizan el protocolo de filaire heredado OP_QUERY, el controlador establecerá el bit <code>secondaryOk</code> según sea necesario conforme a la <a href="https://github.com/mongodb/specifications/blob/master/source/server-selection/server-selection.md">Especificación de selección del servidor</a>.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.1.0</td>
<td>Añadida la opción <code>"readConcern"</code>.</td>
</tr>
</tbody>
</table>

## Ejemplos

Ejemplo de `MongoDB\Driver\Query::__construct`

```
<?php
/* Selecciona solo los documentos escritos por "bjori" con al menos 100 vistas */
$filter = [
    'author' => 'bjori',
    'views' => [
        '$gte' => 100,
    ],
];

$options = [
    /* Devuelve solo los siguientes campos en los documentos correspondientes */
    'projection' => [
        'title' => 1,
        'article' => 1,
    ],
    /* Devuelve los documentos en orden descendente de vistas */
    'sort' => [
        'views' => -1
    ],
];

$query = new MongoDB\Driver\Query($filter, $options);

$manager = new MongoDB\Driver\Manager('mongodb://localhost:27017');
$readPreference = new MongoDB\Driver\ReadPreference(MongoDB\Driver\ReadPreference::PRIMARY);
$cursor = $manager->executeQuery('databaseName.collectionName', $query, ['readPreference' => $readPreference]);

foreach($cursor as $document) {
    var_dump($document);
}

?>

   
```php

## Véase también

MongoDB\Driver\Manager::executeQuery

MongoDB\Driver\Cursor
