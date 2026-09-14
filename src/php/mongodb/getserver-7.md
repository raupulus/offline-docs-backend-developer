---
title: MongoDB\Driver\WriteResult::getServer
description: Devuelve el servidor asociado a este resultado de escritura
source_url: https://www.php.net/manual/es/mongodb-driver-writeresult.getserver.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/writeresult/getserver.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51660
---

MongoDB\Driver\WriteResult::getServer

Devuelve el servidor asociado a este resultado de escritura

## Descripción

```php
final public MongoDB\Driver\WriteResult::getServer(): MongoDB\Driver\Server
```php

Devuelve el `MongoDB\Driver\Server` asociado a este resultado de escritura. Se trata del servidor que ejecutó el `MongoDB\Driver\BulkWrite`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el `MongoDB\Driver\Server` asociado a este resultado de escritura.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo con `MongoDB\Driver\WriteResult::getServer`

```
<?php

$manager = new MongoDB\Driver\Manager;
$server = $manager->selectServer();

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['x' => 1]);

$result = $server->executeBulkWrite('db.collection', $bulk);

var_dump($result->getServer() == $server);

?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(true)

## Véase también

MongoDB\Driver\Server
