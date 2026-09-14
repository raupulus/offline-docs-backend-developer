---
title: MongoDB\Driver\Monitoring\CommandSubscriber::commandFailed
description: Método de notificación para una orden fallida
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-commandsubscriber.commandfailed.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/commandsubscriber/commandfailed.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50120
---

MongoDB\Driver\Monitoring\CommandSubscriber::commandFailed

Método de notificación para una orden fallida

## Descripción

```php
abstract public MongoDB\Driver\Monitoring\CommandSubscriber::commandFailed(MongoDB\Driver\Monitoring\CommandFailedEvent $event): void
```php

Si el observador está registrado, este método es llamado cuando una orden falla.

## Parámetros

`event` (`MongoDB\Driver\Monitoring\CommandFailedEvent`)  
Un objeto de evento que encapsula información sobre la orden fallida.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Monitoring\CommandFailedEvent

MongoDB\Driver\Monitoring\addSubscriber

MongoDB\Driver\Manager::addSubscriber
