---
title: MongoDB\Driver\TopologyDescription::hasReadableServer
description: Indica si la topología tiene un servidor legible
source_url: https://www.php.net/manual/es/mongodb-driver-topologydescription.hasreadableserver.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/topologydescription/hasreadableserver.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51430
---

MongoDB\Driver\TopologyDescription::hasReadableServer

Indica si la topología tiene un servidor legible

## Descripción

```php
final public MongoDB\Driver\TopologyDescription::hasReadableServer([MongoDB\Driver\ReadPreference $readPreference]): bool
```php

Indica si la topología tiene un servidor legible o, si `readPreference` está especificado, un servidor que corresponde a la preferencia de lectura especificada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Indica si la topología tiene un servidor legible o, si `readPreference` está especificado, un servidor que corresponde a la preferencia de lectura especificada.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.
