---
title: MongoDB\Driver\ServerDescription::getType
description: Devuelve un string que indica el tipo de este servidor
source_url: https://www.php.net/manual/es/mongodb-driver-serverdescription.gettype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/serverdescription/gettype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51230
---

MongoDB\Driver\ServerDescription::getType

Devuelve un string que indica el tipo de este servidor

## Descripción

```php
final public MongoDB\Driver\ServerDescription::getType(): string
```php

Devuelve un `string` que indica el tipo de este servidor. El valor estará correlacionado con una constante `MongoDB\Driver\ServerDescription`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `string` que indica el tipo de este servidor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Server::getType
