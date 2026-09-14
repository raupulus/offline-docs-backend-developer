---
title: MongoDB\Driver\TopologyDescription::getServers
description: Devuelve los servidores de la topología
source_url: https://www.php.net/manual/es/mongodb-driver-topologydescription.getservers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/topologydescription/getservers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51410
---

MongoDB\Driver\TopologyDescription::getServers

Devuelve los servidores de la topología

## Descripción

```php
final public MongoDB\Driver\TopologyDescription::getServers(): array
```php

Devuelve un array de objetos `MongoDB\Driver\ServerDescription` correspondiente a los servidores conocidos en la topología.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array de objetos `MongoDB\Driver\ServerDescription` correspondiente a los servidores conocidos en la topología.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.
