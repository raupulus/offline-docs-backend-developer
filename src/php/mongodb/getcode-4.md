---
title: MongoDB\Driver\WriteError::getCode
description: Devuelve el código de error de WriteError
source_url: https://www.php.net/manual/es/mongodb-driver-writeerror.getcode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/writeerror/getcode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51570
---

MongoDB\Driver\WriteError::getCode

Devuelve el código de error de WriteError

## Descripción

```php
final public MongoDB\Driver\WriteError::getCode(): int
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el código de error de WriteError

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo con `MongoDB\Driver\WriteError::getCode`

```
<?php

$manager = new MongoDB\Driver\Manager;

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['_id' => 1]);
$bulk->insert(['_id' => 1]);

try {
    $manager->executeBulkWrite('db.collection', $bulk);
} catch(MongoDB\Driver\Exception\BulkWriteException $e) {
    var_dump($e->getWriteResult()->getWriteErrors()[0]->getCode());
}

?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(11000)
