---
title: MongoDB\Driver\Server::getHost
description: Devuelve el nombre del host del servidor
source_url: https://www.php.net/manual/es/mongodb-driver-server.gethost.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/server/gethost.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51020
---

MongoDB\Driver\Server::getHost

Devuelve el nombre del host del servidor

## Descripción

```php
final public MongoDB\Driver\Server::getHost(): string
```php

Devuelve el nombre del host del servidor.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el nombre del host del servidor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo con `MongoDB\Driver\Server::getHost`

```
<?php

$manager = new MongoDB\Driver\Manager("mongodb://localhost:27017/");

$server = $manager->selectServer();

var_dump($server->getHost());

?>

   
```php

El ejemplo anterior mostrará:

    string(9) "localhost"

## Véase también

MongoDB\Driver\Server::getInfo

MongoDB\Driver\ServerDescription::getHost
