---
title: MongoDB\Driver\ServerDescription::getHost
description: Devuelve el nombre de host de este servidor
source_url: https://www.php.net/manual/es/mongodb-driver-serverdescription.gethost.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/serverdescription/gethost.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51190
---

MongoDB\Driver\ServerDescription::getHost

Devuelve el nombre de host de este servidor

## Descripción

```php
final public MongoDB\Driver\ServerDescription::getHost(): string
```php

Devuelve el nombre de host de este servidor.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el nombre de host de este servidor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Server::getHost
