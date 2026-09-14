---
title: MongoDB\Driver\Monitoring\CommandStartedEvent::getPort
description: Devuelve el puerto del servidor para la orden
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-commandstartedevent.getport.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/commandstartedevent/getport.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50060
---

MongoDB\Driver\Monitoring\CommandStartedEvent::getPort

Devuelve el puerto del servidor para la orden

## Descripción

```php
final public MongoDB\Driver\Monitoring\CommandStartedEvent::getPort(): int
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el puerto del servidor en el que se ejecutó la orden.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.
