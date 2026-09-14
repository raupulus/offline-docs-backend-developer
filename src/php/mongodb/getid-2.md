---
title: MongoDB\Driver\CursorInterface::getId
description: Devuelve el ID de este cursor
source_url: https://www.php.net/manual/es/mongodb-driver-cursorinterface.getid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/cursorinterface/getid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49390
---

MongoDB\Driver\CursorInterface::getId

Devuelve el ID de este cursor

## Descripción

```php
abstract public MongoDB\Driver\CursorInterface::getId(): MongoDB\BSON\Int64
```php

Devuelve el ID de este cursor, que identifica de manera única el cursor en el servidor.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el ID de este cursor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 1.20.0 | Se añadió `MongoDB\BSON\Int64` al tipo de retorno tentativo de este método. `MongoDB\Driver\CursorId` será eliminado del tipo de retorno en la versión 2.0. |

## Véase también

MongoDB\Driver\Cursor::getId

MongoDB\Driver\CursorId

MongoDB\BSON\Int64
