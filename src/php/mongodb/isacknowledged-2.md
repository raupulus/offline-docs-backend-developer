---
title: MongoDB\Driver\WriteResult::isAcknowledged
description: Indica si la escritura ha sido reconocida
source_url: https://www.php.net/manual/es/mongodb-driver-writeresult.isacknowledged.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/writeresult/isacknowledged.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51710
---

MongoDB\Driver\WriteResult::isAcknowledged

Indica si la escritura ha sido reconocida

## Descripción

```php
final public MongoDB\Driver\WriteResult::isAcknowledged(): bool
```php

Si la escritura ha sido reconocida, otros campos de conteo estarán disponibles para el objeto `MongoDB\Driver\WriteResult`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si la escritura ha sido reconocida, y `false` en caso contrario.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

`MongoDB\Driver\WriteResult::isAcknowledged` con la preocupación de escritura reconocida

```
<?php

$manager = new MongoDB\Driver\Manager;

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['x' => 1]);

$result = $manager->executeBulkWrite('db.collection', $bulk);

var_dump($result->isAcknowledged());

?>

   
```php

El ejemplo anterior mostrará:

    bool(true)

`MongoDB\Driver\WriteResult::isAcknowledged` con la preocupación de escritura no reconocida

```
<?php

$manager = new MongoDB\Driver\Manager;

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['x' => 1]);

$writeConcern = new MongoDB\Driver\WriteConcern(0);

$result = $manager->executeBulkWrite('db.collection', $bulk, ['writeConcern' => $writeConcern]);

var_dump($result->isAcknowledged());

?>

   
```php

El ejemplo anterior mostrará:

    bool(false)

## Véase también

MongoDB\Driver\WriteConcern

Referencia sobre la Preocupación de Escritura
