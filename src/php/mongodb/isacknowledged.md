---
title: MongoDB\Driver\BulkWriteCommandResult::isAcknowledged
description: Devuelve si la escritura fue reconocida
source_url: https://www.php.net/manual/es/mongodb-driver-bulkwritecommandresult.isacknowledged.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/bulkwritecommandresult/isacknowledged.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49070
---

MongoDB\Driver\BulkWriteCommandResult::isAcknowledged

Devuelve si la escritura fue reconocida

## Descripción

```php
final public MongoDB\Driver\BulkWriteCommandResult::isAcknowledged(): bool
```php

Si la escritura es reconocida, otros campos estarán disponibles en el objeto `MongoDB\Driver\BulkWriteCommandResult`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si la escritura fue reconocida, y `false` en caso contrario.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

`MongoDB\Driver\BulkWriteCommandResult::isAcknowledged` con preocupación de escritura reconocida

```
<?php

$manager = new MongoDB\Driver\Manager;

$bulk = new MongoDB\Driver\BulkWriteCommand;
$bulk->insertOne('db.coll', ['x' => 1]);

$result = $manager->executeBulkWriteCommand($bulk);

var_dump($result->isAcknowledged());

?>

   
```php

El ejemplo anterior mostrará:

    bool(true)

`MongoDB\Driver\BulkWriteCommandResult::isAcknowledged` con preocupación de escritura no reconocida

```
<?php

$manager = new MongoDB\Driver\Manager;

$bulk = new MongoDB\Driver\BulkWriteCommand(['ordered' => false]);
$bulk->insertOne('db.coll', ['x' => 1]);

$writeConcern = new MongoDB\Driver\WriteConcern(0);

$result = $manager->executeBulkWriteCommand($bulk, ['writeConcern' => $writeConcern]);

var_dump($result->isAcknowledged());

?>

   
```php

El ejemplo anterior mostrará:

    bool(false)

## Véase también

MongoDB\Driver\WriteConcern

Referencia de preocupación de escritura
