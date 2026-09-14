---
title: MongoDB\Driver\Cursor::getId
description: Devuelve el ID del cursor
source_url: https://www.php.net/manual/es/mongodb-driver-cursor.getid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/cursor/getid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49260
---

MongoDB\Driver\Cursor::getId

Devuelve el ID del cursor

## Descripción

```php
final public MongoDB\Driver\Cursor::getId(): MongoDB\BSON\Int64
```php

Devuelve el ID de este cursor, que identifica de manera única al cursor en el servidor.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el ID de este cursor. El ID se devolverá como un objeto `MongoDB\BSON\Int64`.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 2.0.0 | Se cambió el tipo de retorno a `MongoDB\BSON\Int64`. Se eliminó el parámetro `asInt64`. |
| PECL mongodb 1.20.0 | Se desaconsejó devolver un `MongoDB\Driver\CursorId`. Se añadió el argumento `asInt64` para facilitar la migración en versiones futuras. Si `asInt64` es `true`, el ID se devolverá como un `MongoDB\BSON\Int64`. |

## Ejemplos

Ejemplo de `MongoDB\Driver\Cursor::getId`

```
<?php

/* En este ejemplo, insertamos varios documentos en la colección y especificamos
 * un batchSize más pequeño para asegurar que el primer lote contenga solo un
 * subconjunto de nuestros resultados y el cursor permanezca abierto en el servidor. */
$manager = new MongoDB\Driver\Manager("mongodb://localhost:27017");
$query = new MongoDB\Driver\Query([], ['batchSize' => 2]);

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['x' => 1]);
$bulk->insert(['x' => 2]);
$bulk->insert(['x' => 3]);
$manager->executeBulkWrite('db.collection', $bulk);

$cursor = $manager->executeQuery('db.collection', $query);
var_dump($cursor->getId(true));

?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(MongoDB\BSON\Int64)#5 (1) {
      ["integer"]=>
      string(11) "94810124093"
    }

## Véase también

MongoDB\BSON\Int64
