---
title: MongoDB\Driver\Monitoring\SDAMSubscriber::serverOpening
description: Método de notificación para la apertura de un servidor
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-sdamsubscriber.serveropening.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/sdamsubscriber/serveropening.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50350
---

MongoDB\Driver\Monitoring\SDAMSubscriber::serverOpening

Método de notificación para la apertura de un servidor

## Descripción

```php
abstract public MongoDB\Driver\Monitoring\SDAMSubscriber::serverOpening(MongoDB\Driver\Monitoring\ServerOpeningEvent $event): void
```php

Si un observador está registrado, este método es llamado cuando un servidor existente es retirado de la topología.

## Parámetros

`event` (`MongoDB\Driver\Monitoring\ServerOpeningEvent`)  
Un objeto de evento que encapsula información sobre el servidor abierto.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Monitoring\ServerOpeningEvent

MongoDB\Driver\Monitoring\addSubscriber

MongoDB\Driver\Manager::addSubscriber
