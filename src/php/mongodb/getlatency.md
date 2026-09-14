---
title: MongoDB\Driver\Server::getLatency
description: Devuelve la latencia de este servidor en milisegundos
source_url: https://www.php.net/manual/es/mongodb-driver-server.getlatency.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/server/getlatency.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51040
---

MongoDB\Driver\Server::getLatency

Devuelve la latencia de este servidor en milisegundos

## Descripción

```php
final public MongoDB\Driver\Server::getLatency(): integer
```php

Devuelve la latencia de este servidor en milisegundos. Es la medida del cliente del tiempo de [ida y vuelta](https://github.com/mongodb/specifications/blob/master/source/server-discovery-and-monitoring/server-discovery-and-monitoring.md#round-trip-time) de un comando `hello`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la latencia del servidor en milisegundos, o `null` si no se ha medido ninguna latencia (por ejemplo, el cliente está conectado a un balanceador de carga).

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 1.11.0 | Este método devolverá `null` si no se ha medido ninguna latencia. En versiones anteriores, siempre se devolvía un número entero y un valor no definido podía ser señalado como `-1`. |

## Ejemplos

Ejemplo con `MongoDB\Driver\Server::getLatency`

```
<?php

$manager = new MongoDB\Driver\Manager("mongodb://localhost:27017/");

$server = $manager->selectServer();

var_dump($server->getLatency());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(592)

## Véase también

MongoDB\Driver\Server::getInfo

MongoDB\Driver\ServerDescription::getRoundTripTime

La especificación sobre el descubrimiento y la supervisión de un servidor
