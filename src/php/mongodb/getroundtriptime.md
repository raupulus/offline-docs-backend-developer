---
title: MongoDB\Driver\ServerDescription::getRoundTripTime
description: Devuelve el tiempo de ida y vuelta del servidor en milisegundos
source_url: https://www.php.net/manual/es/mongodb-driver-serverdescription.getroundtriptime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/serverdescription/getroundtriptime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51220
---

MongoDB\Driver\ServerDescription::getRoundTripTime

Devuelve el tiempo de ida y vuelta del servidor en milisegundos

## Descripción

```php
final public MongoDB\Driver\ServerDescription::getRoundTripTime(): int
```php

Devuelve el tiempo de ida y vuelta del servidor en milisegundos. Se trata de la medida del cliente de la duración de una comando [hello](https://www.mongodb.com/docs/manual/reference/command/hello/).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el tiempo de ida y vuelta del servidor en milisegundos.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Server::getLatency
