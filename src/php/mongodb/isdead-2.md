---
title: MongoDB\Driver\CursorInterface::isDead
description: Comprueba si el cursor puede tener resultados adicionales
source_url: https://www.php.net/manual/es/mongodb-driver-cursorinterface.isdead.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/cursorinterface/isdead.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49410
---

MongoDB\Driver\CursorInterface::isDead

Comprueba si el cursor puede tener resultados adicionales

## Descripción

```php
abstract public MongoDB\Driver\CursorInterface::isDead(): bool
```php

Comprueba si el cursor puede tener resultados adicionales disponibles para leer. Un cursor está inicialmente "activo" pero puede volverse "inactivo" por cualquiera de las siguientes razones: Avanzar un cursor no orientable no devolvió un documento, El cursor encontró un error, El cursor leyó su último lote hasta completarse, El cursor alcanzó su límite configurado Esto es principalmente útil con cursores orientables.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si no hay resultados adicionales disponibles, y `false` en caso contrario.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Cursor::isDead
