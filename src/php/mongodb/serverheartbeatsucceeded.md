---
title: MongoDB\Driver\Monitoring\SDAMSubscriber::serverHeartbeatSucceeded
description: Método de notificación para un latido de servidor exitoso
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-sdamsubscriber.serverheartbeatsucceeded.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/sdamsubscriber/serverheartbeatsucceeded.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50340
---

MongoDB\Driver\Monitoring\SDAMSubscriber::serverHeartbeatSucceeded

Método de notificación para un latido de servidor exitoso

## Descripción

```php
abstract public MongoDB\Driver\Monitoring\SDAMSubscriber::serverHeartbeatSucceeded(MongoDB\Driver\Monitoring\ServerHeartbeatSucceededEvent $event): void
```php

Si un observador está registrado, este método es llamado cuando un latido de servidor (es decir, una comando [hello](https://www.mongodb.com/docs/manual/reference/command/hello/) emitido a través de [monitoreo de servidor](https://github.com/mongodb/specifications/blob/master/source/server-discovery-and-monitoring/server-discovery-and-monitoring.md)) tiene éxito.

## Parámetros

`event` (`MongoDB\Driver\Monitoring\ServerHeartbeatSucceededEvent`)  
Un objeto de evento que encapsula información sobre el latido de servidor exitoso.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Monitoring\ServerHeartbeatSucceededEvent

MongoDB\Driver\Monitoring\addSubscriber

MongoDB\Driver\Manager::addSubscriber
