---
title: MongoDB\Driver\Server::getServerDescription
description: Devuelve una ServerDescription para este servidor
source_url: https://www.php.net/manual/es/mongodb-driver-server.getserverdescription.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/server/getserverdescription.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51060
---

MongoDB\Driver\Server::getServerDescription

Devuelve una ServerDescription para este servidor

## Descripción

```php
final public MongoDB\Driver\Server::getServerDescription(): MongoDB\Driver\ServerDescription
```php

Devuelve una `MongoDB\Driver\ServerDescription` para este servidor. Es un objeto de valor inmutable que describirá el servidor en el momento en que se llame a este método.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una `MongoDB\Driver\ServerDescription` para este servidor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.
