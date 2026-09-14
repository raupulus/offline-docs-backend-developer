---
title: MongoDB\Driver\CursorInterface::toArray
description: Devuelve un array que contiene todos los resultados de este cursor
source_url: https://www.php.net/manual/es/mongodb-driver-cursorinterface.toarray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/cursorinterface/toarray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49430
---

MongoDB\Driver\CursorInterface::toArray

Devuelve un array que contiene todos los resultados de este cursor

## Descripción

```php
abstract public MongoDB\Driver\CursorInterface::toArray(): array
```php

Itera el cursor y devuelve sus resultados en un array. Se puede usar `MongoDB\Driver\CursorInterface::setTypeMap` para controlar cómo los documentos son deserializados en valores de PHP.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `array` que contiene todos los resultados de este cursor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Cursor::toArray

MongoDB\Driver\CursorInterface::setTypeMap
