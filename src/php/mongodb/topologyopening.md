---
title: MongoDB\Driver\Monitoring\SDAMSubscriber::topologyOpening
description: Método de notificación para la apertura de topología
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-sdamsubscriber.topologyopening.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/sdamsubscriber/topologyopening.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50380
---

MongoDB\Driver\Monitoring\SDAMSubscriber::topologyOpening

Método de notificación para la apertura de topología

## Descripción

```php
abstract public MongoDB\Driver\Monitoring\SDAMSubscriber::topologyOpening(MongoDB\Driver\Monitoring\TopologyOpeningEvent $event): void
```php

Si un observador está registrado, este método es llamado cuando una topología es abierta.

> [!NOTE]
> Debido al comportamiento del controlador [de gestión y persistencia de conexiones](#mongodb.connection-handling), este evento puede no ser observado si un `MongoDB\Driver\Manager` utiliza un cliente [libmongoc](https://github.com/mongodb/mongo-c-driver) previamente persistente.

## Parámetros

`event` (`MongoDB\Driver\Monitoring\TopologyOpeningEvent`)  
Un objeto de evento que encapsula información sobre la topología abierta.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Monitoring\TopologyOpeningEvent

MongoDB\Driver\Monitoring\addSubscriber

MongoDB\Driver\Manager::addSubscriber
