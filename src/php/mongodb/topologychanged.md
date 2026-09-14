---
title: MongoDB\Driver\Monitoring\SDAMSubscriber::topologyChanged
description: Método de notificación para un cambio de descripción de topología
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-sdamsubscriber.topologychanged.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/sdamsubscriber/topologychanged.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50360
---

MongoDB\Driver\Monitoring\SDAMSubscriber::topologyChanged

Método de notificación para un cambio de descripción de topología

## Descripción

```php
abstract public MongoDB\Driver\Monitoring\SDAMSubscriber::topologyChanged(MongoDB\Driver\Monitoring\TopologyChangedEvent $event): void
```php

Si un observador está registrado, este método es llamado cuando una descripción de topología cambia. Por ejemplo, el descubrimiento de un nuevo primario en un conjunto de réplicas resultaría en un cambio de la descripción de la topología.

## Parámetros

`event` (`MongoDB\Driver\Monitoring\TopologyChangedEvent`)  
Un objeto de evento que encapsula información sobre la descripción de topología modificada.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Monitoring\TopologyChangedEvent

MongoDB\Driver\Monitoring\addSubscriber

MongoDB\Driver\Manager::addSubscriber
