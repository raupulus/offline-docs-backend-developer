---
title: La clase MongoDB\Driver\Monitoring\ServerChangedEvent
source_url: https://www.php.net/manual/es/class.mongodb-driver-monitoring-serverchangedevent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/serverchangedevent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 36c32a2a9
order: 50450
---

## Introducción

La clase `MongoDB\Driver\Monitoring\ServerChangedEvent` encapsula información sobre una descripción de servidor modificada. Por ejemplo, el tipo de un servidor pasando de secundario a primario entraînerait un cambio en la descripción de este servidor.

## Sinopsis de la clase

MongoDB\Driver\Monitoring\ServerChangedEvent

final

MongoDB\Driver\Monitoring\ServerChangedEvent

Propiedades

public

readonly

string

host

public

readonly

int

port

public

readonly

MongoDB\BSON\ObjectId

topologyId

public

readonly

MongoDB\Driver\ServerDescription

newDescription

public

readonly

MongoDB\Driver\ServerDescription

previousDescription

Métodos

## Propiedades

`host`  
El nombre de host del servidor.

`port`  
El puerto del servidor.

`topologyId`  
El identificador de la topología.

`newDescription`  
La nueva descripción del servidor.

`previousDescription`  
La descripción previa del servidor.

## Historial de cambios

| Versión            | Descripción                                 |
|--------------------|---------------------------------------------|
| PECL mongodb 2.3.0 | Se añadieron propiedades públicas readonly. |
