---
title: MongoDB\Driver\CursorId::__toString
description: Representación en forma de string del identificador del cursor
source_url: https://www.php.net/manual/es/mongodb-driver-cursorid.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/cursorid/tostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49370
---

MongoDB\Driver\CursorId::\_\_toString

Representación en forma de string del identificador del cursor

## Descripción

```php
final public MongoDB\Driver\CursorId::__toString(): string
```php

Devuelve la representación en forma de `string` del identificador del cursor.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la representación en forma de `string` del identificador del cursor.

## Ejemplos

Ejemplo de `MongoDB\Driver\CursorId::__toString`

```
<?php

/* En este ejemplo, insertamos varios documentos en la colección y especificamos
 * un tamaño de lote (batchSize) más pequeño para asegurarnos de que el primer lote
 * contenga solo un subconjunto de nuestros resultados y el cursor permanezca abierto
 * en el servidor. */
$manager = new MongoDB\Driver\Manager("mongodb://localhost:27017");
$query = new MongoDB\Driver\Query([], ['batchSize' => 2]);

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['x' => 1]);
$bulk->insert(['x' => 2]);
$bulk->insert(['x' => 3]);
$manager->executeBulkWrite('db.collection', $bulk);

$cursor = $manager->executeQuery('db.collection', $query);
var_dump((string) $cursor->getId());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(11) "98061641158"

## Véase también

MongoDB\Driver\Cursor::getId
