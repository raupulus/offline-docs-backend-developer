---
title: MongoDB\Driver\BulkWrite::insert
description: Añade una operación de inserción al lote masivo
source_url: https://www.php.net/manual/es/mongodb-driver-bulkwrite.insert.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/bulkwrite/insert.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48870
---

MongoDB\Driver\BulkWrite::insert

Añade una operación de inserción al lote masivo

## Descripción

```php
public MongoDB\Driver\BulkWrite::insert(array $documento): mixed
```php

Añade una operación de inserción a la `MongoDB\Driver\BulkWrite`.

## Parámetros

`documento` (`arrayobject`)  
Un documento a insertar.

## Valores devueltos

Devuelve el `_id` del documento insertado. Si el `documento` no tenía un `_id`, se devolverá el `MongoDB\BSON\ObjectId` generado para la inserción.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 1.3.0 | Siempre se devuelve el `_id` del documento insertado. Anteriormente, el método solo devolvía un valor si se generaba un `MongoDB\BSON\ObjectId`. |

## Ejemplos

Ejemplo de `MongoDB\Driver\BulkWrite::insert`

```
<?php

$bulk = new MongoDB\Driver\BulkWrite;

$doc1 = ['x' => 1];
$doc2 = ['_id' => 'id-personalizado', 'x' => 2];
$doc3 = ['_id' => new MongoDB\BSON\ObjectId('0123456789abcdef01234567'), 'x' => 3];

$id1 = $bulk->insert($doc1);
$id2 = $bulk->insert($doc2);
$id3 = $bulk->insert($doc3);

var_dump($id1, $id2, $id3);

$manager = new MongoDB\Driver\Manager('mongodb://localhost:27017');
$result = $manager->executeBulkWrite('db.collection', $bulk);

?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(MongoDB\BSON\ObjectId)#3 (1) {
      ["oid"]=>
      string(24) "67f58058d1a0aa2fd80d55d0"
    }
    string(18) "id-personalizado"
    object(MongoDB\BSON\ObjectId)#4 (1) {
      ["oid"]=>
      string(24) "0123456789abcdef01234567"
    }

## Véase también

MongoDB\Driver\Manager::executeBulkWrite

MongoDB\Driver\WriteResult

MongoDB\BSON\ObjectId

MongoDB\BSON\Persistable
