---
title: La clase MongoDB\Driver\Monitoring\ServerOpeningEvent
source_url: https://www.php.net/manual/es/class.mongodb-driver-monitoring-serveropeningevent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/serveropeningevent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 36c32a2a9
order: 50690
---

## Introducción

La clase `MongoDB\Driver\Monitoring\ServerOpeningEvent` encapsula información sobre un servidor abierto. Esto corresponde a un nuevo servidor que se añade a la topología.

## Sinopsis de la clase

MongoDB\Driver\Monitoring\ServerOpeningEvent

final

MongoDB\Driver\Monitoring\ServerOpeningEvent

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

Métodos

## Propiedades

`host`  
El host del servidor.

`port`  
El puerto del servidor.

`topologyId`  
El identificador de la topología.

## Historial de cambios

| Versión            | Descripción                                 |
|--------------------|---------------------------------------------|
| PECL mongodb 2.3.0 | Se añadieron propiedades públicas readonly. |
