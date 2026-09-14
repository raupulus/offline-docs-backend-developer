---
title: MongoDB\Driver\Monitoring\CommandSucceededEvent::getOperationId
description: Devuelve el identificador de la operación de la orden
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-commandsucceededevent.getoperationid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/commandsucceededevent/getoperationid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50200
---

MongoDB\Driver\Monitoring\CommandSucceededEvent::getOperationId

Devuelve el identificador de la operación de la orden

## Descripción

```php
final public MongoDB\Driver\Monitoring\CommandSucceededEvent::getOperationId(): string
```php

El identificador de la operación es generado por la extensión y puede ser utilizado para vincular eventos juntos tales como operaciones de escritura en masa, que pueden haber sido divididas en varias órdenes a nivel del protocolo.

> [!NOTE]
> Dado que varias órdenes pueden compartir el mismo identificador de operación, no es fiable utilizar este valor para asociar objetos de evento entre sí. El identificador de la petición devuelto por MongoDB\Driver\Monitoring\CommandSucceededEvent::getRequestId debería ser utilizado en su lugar.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el identificador de la operación de la orden.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Monitoring\CommandStartedEvent::getOperationId

MongoDB\Driver\Monitoring\CommandSucceededEvent::getRequestId
