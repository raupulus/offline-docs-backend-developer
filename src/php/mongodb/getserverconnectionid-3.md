---
title: MongoDB\Driver\Monitoring\CommandSucceededEvent::getServerConnectionId
description: Devuelve el identificador de conexión del servidor para la orden
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-commandsucceededevent.getserverconnectionid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/commandsucceededevent/getserverconnectionid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50250
---

MongoDB\Driver\Monitoring\CommandSucceededEvent::getServerConnectionId

Devuelve el identificador de conexión del servidor para la orden

## Descripción

```php
final public MongoDB\Driver\Monitoring\CommandSucceededEvent::getServerConnectionId(): int
```php

Devuelve el identificador de conexión del servidor para la orden. El identificador de conexión del servidor es distinto del servidor (es decir, `MongoDB\Driver\Monitoring\CommandSucceededEvent::getServer`) y es devuelto en el campo "connectionId" de una respuesta de orden `hello` MongoDB 4.2+.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el identificador de conexión del servidor, o `null` si no está disponible.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.
