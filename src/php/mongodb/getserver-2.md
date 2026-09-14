---
title: MongoDB\Driver\CursorInterface::getServer
description: Devuelve el servidor asociado a este cursor
source_url: https://www.php.net/manual/es/mongodb-driver-cursorinterface.getserver.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/cursorinterface/getserver.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49400
---

MongoDB\Driver\CursorInterface::getServer

Devuelve el servidor asociado a este cursor

## Descripción

```php
abstract public MongoDB\Driver\CursorInterface::getServer(): MongoDB\Driver\Server
```php

Devuelve el `MongoDB\Driver\Server` asociado a este cursor. Este es el servidor que ejecutó la `MongoDB\Driver\Query` o la `MongoDB\Driver\Command`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el `MongoDB\Driver\Server` asociado a este cursor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Cursor::getServer

MongoDB\Driver\Server
