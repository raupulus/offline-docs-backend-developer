---
title: MongoDB\Driver\Monitoring\ServerOpeningEvent::getTopologyId
description: Devuelve el ID de topología asociado a este servidor
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-serveropeningevent.gettopologyid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/serveropeningevent/gettopologyid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50680
---

MongoDB\Driver\Monitoring\ServerOpeningEvent::getTopologyId

Devuelve el ID de topología asociado a este servidor

## Descripción

```php
final public MongoDB\Driver\Monitoring\ServerOpeningEvent::getTopologyId(): MongoDB\BSON\ObjectId
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el ID de topología.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.
