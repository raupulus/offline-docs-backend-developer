---
title: MongoDB\Driver\Monitoring\CommandFailedEvent::getRequestId
description: Devuelve el identificador de la petición de la orden
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-commandfailedevent.getrequestid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/commandfailedevent/getrequestid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49960
---

MongoDB\Driver\Monitoring\CommandFailedEvent::getRequestId

Devuelve el identificador de la petición de la orden

## Descripción

```php
final public MongoDB\Driver\Monitoring\CommandFailedEvent::getRequestId(): string
```php

El identificador de la petición es generado por la extensión y puede ser utilizado para asociar este `MongoDB\Driver\Monitoring\CommandFailedEvent` con un `MongoDB\Driver\Monitoring\CommandStartedEvent` anterior.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el identificador de la petición de la orden.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Monitoring\CommandStartedEvent::getRequestId
