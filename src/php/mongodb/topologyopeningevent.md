---
title: La clase MongoDB\Driver\Monitoring\TopologyOpeningEvent
source_url: https://www.php.net/manual/es/class.mongodb-driver-monitoring-topologyopeningevent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/topologyopeningevent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 36c32a2a9
order: 50780
---

## Introducción

La clase `MongoDB\Driver\Monitoring\TopologyOpeningEvent` encapsula información sobre una topología abierta.

> [!NOTE]
> Debido al comportamiento [de gestión y persistencia de las conexiones](#mongodb.connection-handling) del controlador, este evento puede no ser observado si un `MongoDB\Driver\Manager` utiliza un cliente [libmongoc](https://github.com/mongodb/mongo-c-driver) previamente persistente.

## Sinopsis de la clase

MongoDB\Driver\Monitoring\TopologyOpeningEvent

final

MongoDB\Driver\Monitoring\TopologyOpeningEvent

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
