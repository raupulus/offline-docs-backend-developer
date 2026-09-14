---
title: MongoDB\Driver\Server::getPort
description: Devuelve el puerto en el que el servidor está escuchando
source_url: https://www.php.net/manual/es/mongodb-driver-server.getport.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/server/getport.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51050
---

MongoDB\Driver\Server::getPort

Devuelve el puerto en el que el servidor está escuchando

## Descripción

```php
final public MongoDB\Driver\Server::getPort(): int
```php

Devuelve el puerto en el que el servidor está escuchando.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el puerto en el que el servidor está escuchando.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo con `MongoDB\Driver\Server::getPort`

```
<?php

$manager = new MongoDB\Driver\Manager("mongodb://localhost:27017/");

$server = $manager->selectServer();

var_dump($server->getPort());

?>

   
```php

El ejemplo anterior mostrará:

    int(27017)

## Véase también

MongoDB\Driver\Server::getInfo

MongoDB\Driver\ServerDescription::getPort
