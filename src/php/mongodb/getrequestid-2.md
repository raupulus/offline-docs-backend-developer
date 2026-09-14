---
title: MongoDB\Driver\Monitoring\CommandStartedEvent::getRequestId
description: Devuelve el identificador de la solicitud de la orden
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-commandstartedevent.getrequestid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/commandstartedevent/getrequestid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50070
---

MongoDB\Driver\Monitoring\CommandStartedEvent::getRequestId

Devuelve el identificador de la solicitud de la orden

## Descripción

```php
final public MongoDB\Driver\Monitoring\CommandStartedEvent::getRequestId(): string
```php

El identificador de la solicitud es generado por la extensión y puede ser utilizado para asociar este evento `MongoDB\Driver\Monitoring\CommandStartedEvent` con un `MongoDB\Driver\Monitoring\CommandFailedEvent` o `MongoDB\Driver\Monitoring\CommandSucceededEvent` posterior.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el identificador de la solicitud de la orden.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Monitoring\CommandFailedEvent::getRequestId

MongoDB\Driver\Monitoring\CommandSucceededEvent::getRequestId
