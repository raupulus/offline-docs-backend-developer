---
title: MongoDB\Driver\ServerDescription::getPort
description: Devuelve el puerto en el que este servidor escucha
source_url: https://www.php.net/manual/es/mongodb-driver-serverdescription.getport.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/serverdescription/getport.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51210
---

MongoDB\Driver\ServerDescription::getPort

Devuelve el puerto en el que este servidor escucha

## Descripción

```php
final public MongoDB\Driver\ServerDescription::getPort(): int
```php

Devuelve el puerto en el que este servidor escucha.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el puerto en el que este servidor escucha.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Server::getPort
