---
title: MongoDB\Driver\Server::getType
description: Devuelve un integer que representa el tipo del servidor
source_url: https://www.php.net/manual/es/mongodb-driver-server.gettype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/server/gettype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51080
---

MongoDB\Driver\Server::getType

Devuelve un integer que representa el tipo del servidor

## Descripción

```php
final public MongoDB\Driver\Server::getType(): int
```php

Devuelve un `int` que representa el tipo del servidor. El valor corresponderá a una constante `MongoDB\Driver\Server`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `int` que representa el tipo del servidor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Server::getInfo

MongoDB\Driver\ServerDescription::getType
