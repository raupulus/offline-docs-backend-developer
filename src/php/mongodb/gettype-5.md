---
title: MongoDB\Driver\TopologyDescription::getType
description: Devuelve un string que denota el tipo de esta topología
source_url: https://www.php.net/manual/es/mongodb-driver-topologydescription.gettype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/topologydescription/gettype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51420
---

MongoDB\Driver\TopologyDescription::getType

Devuelve un string que denota el tipo de esta topología

## Descripción

```php
final public MongoDB\Driver\TopologyDescription::getType(): string
```php

Devuelve un `string` que denota el tipo de esta topología. El valor estará correlacionado con una constante de `MongoDB\Driver\TopologyDescription`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `string` que denota el tipo de esta topología.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.
