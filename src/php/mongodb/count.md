---
title: MongoDB\Driver\BulkWrite::count
description: Cuenta el número de operaciones de escritura en la operación masiva
source_url: https://www.php.net/manual/es/mongodb-driver-bulkwrite.count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/bulkwrite/count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48850
---

MongoDB\Driver\BulkWrite::count

Cuenta el número de operaciones de escritura en la operación masiva

## Descripción

```php
public MongoDB\Driver\BulkWrite::count(): int
```php

Devuelve el número de operaciones de escritura añadidas al objeto `MongoDB\Driver\BulkWrite`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de operaciones de escritura añadidas al objeto `MongoDB\Driver\BulkWrite`.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 1.2.0 | Devuelve el número de operaciones de escritura añadidas al objeto `MongoDB\Driver\BulkWrite`. Las versiones anteriores devolvían el número esperado de viajes de ida y vuelta del cliente al servidor necesarios para ejecutar todas las operaciones de escritura. |

## Ejemplos

Ejemplo de `MongoDB\Driver\BulkWrite::count`

```
<?php

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['_id' => 1, 'x' => 1]);
$bulk->insert(['_id' => 2, 'x' => 2]);
$bulk->update(['x' => 2], ['$set' => ['x' => 1]]);
$bulk->delete(['x' => 1]);

var_dump(count($bulk));

?>

   
```php

El ejemplo anterior mostrará:

    int(4)
