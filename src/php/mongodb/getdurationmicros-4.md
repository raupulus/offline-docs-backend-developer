---
title: MongoDB\Driver\Monitoring\ServerHeartbeatSucceededEvent::getDurationMicros
description: Devuelve la duración del latido en microsegundos
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-serverheartbeatsucceededevent.getdurationmicros.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/serverheartbeatsucceededevent/getdurationmicros.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50600
---

MongoDB\Driver\Monitoring\ServerHeartbeatSucceededEvent::getDurationMicros

Devuelve la duración del latido en microsegundos

## Descripción

```php
final public MongoDB\Driver\Monitoring\ServerHeartbeatSucceededEvent::getDurationMicros(): int
```php

La duración del latido es un valor calculado que incluye el tiempo para enviar el mensaje y recibir la respuesta del servidor.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la duración del latido en microsegundos.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.
