---
title: La clase MongoDB\Driver\Monitoring\TopologyChangedEvent
source_url: https://www.php.net/manual/es/class.mongodb-driver-monitoring-topologychangedevent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/topologychangedevent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 36c32a2a9
order: 50740
---

## Introducción

La clase `MongoDB\Driver\Monitoring\TopologyChangedEvent` encapsula información sobre una descripción de topología modificada. Por ejemplo, el descubrimiento de un nuevo primario en un conjunto de réplicas resultaría en un cambio en la descripción de la topología.

## Sinopsis de la clase

MongoDB\Driver\Monitoring\TopologyChangedEvent

final

MongoDB\Driver\Monitoring\TopologyChangedEvent

Propiedades

public

readonly

MongoDB\BSON\ObjectId

topologyId

public

readonly

MongoDB\Driver\TopologyDescription

newDescription

public

readonly

MongoDB\Driver\TopologyDescription

previousDescription

Métodos

## Propiedades

`topologyId`  
El identificador de la topología.

`newDescription`  
La nueva descripción de la topología.

`previousDescription`  
La descripción previa de la topología.

## Historial de cambios

| Versión            | Descripción                                 |
|--------------------|---------------------------------------------|
| PECL mongodb 2.3.0 | Se añadieron propiedades públicas readonly. |
