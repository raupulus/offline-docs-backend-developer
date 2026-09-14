---
title: MongoDB\Driver\WriteError::getInfo
description: Devuelve el documento de metadatos para WriteError
source_url: https://www.php.net/manual/es/mongodb-driver-writeerror.getinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/writeerror/getinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51590
---

MongoDB\Driver\WriteError::getInfo

Devuelve el documento de metadatos para WriteError

## Descripción

```php
final public MongoDB\Driver\WriteError::getInfo(): object
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el documento de metadatos para WriteError, o `null` si no hay metadatos disponibles.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.
