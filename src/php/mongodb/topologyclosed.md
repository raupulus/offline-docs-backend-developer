---
title: MongoDB\Driver\Monitoring\SDAMSubscriber::topologyClosed
description: Método de notificación para el cierre de topología
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-sdamsubscriber.topologyclosed.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/sdamsubscriber/topologyclosed.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50370
---

MongoDB\Driver\Monitoring\SDAMSubscriber::topologyClosed

Método de notificación para el cierre de topología

## Descripción

```php
abstract public MongoDB\Driver\Monitoring\SDAMSubscriber::topologyClosed(MongoDB\Driver\Monitoring\TopologyClosedEvent $event): void
```php

Si un observador está registrado, este método es llamado cuando una topología es cerrada.

> [!NOTE]
> Debido al comportamiento del controlador [de gestión y persistencia de conexiones](#mongodb.connection-handling), este evento solo puede ser observado cuando un `MongoDB\Driver\Manager` es creado con la opción del controlador `"disableClientPersistence"` y liberado antes del cierre de la solicitud (RSHUTDOWN).

## Parámetros

`event` (`MongoDB\Driver\Monitoring\TopologyClosedEvent`)  
Un objeto de evento que encapsula información sobre la topología cerrada.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Monitoring\TopologyClosedEvent

MongoDB\Driver\Monitoring\addSubscriber

MongoDB\Driver\Manager::addSubscriber
