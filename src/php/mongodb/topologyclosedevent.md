---
title: La clase MongoDB\Driver\Monitoring\TopologyClosedEvent
source_url: https://www.php.net/manual/es/class.mongodb-driver-monitoring-topologyclosedevent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/topologyclosedevent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 36c32a2a9
order: 50760
---

## Introducción

La clase `MongoDB\Driver\Monitoring\TopologyClosedEvent` encapsula información sobre una topología cerrada.

> [!NOTE]
> Debido al comportamiento [de gestión y persistencia de las conexiones](#mongodb.connection-handling) del controlador, este evento solo puede ser observado cuando un `MongoDB\Driver\Manager` es creado con la opción del controlador `"disableClientPersistence"` y liberado antes del cierre de la solicitud (RSHUTDOWN).

## Sinopsis de la clase

MongoDB\Driver\Monitoring\TopologyClosedEvent

final

MongoDB\Driver\Monitoring\TopologyClosedEvent

Propiedades

public

readonly

MongoDB\BSON\ObjectId

topologyId

Métodos

## Propiedades

`topologyId`  
El identificador de la topología.

## Historial de cambios

| Versión            | Descripción                                 |
|--------------------|---------------------------------------------|
| PECL mongodb 2.3.0 | Se añadieron propiedades públicas readonly. |
