---
title: La clase MongoDB\Driver\Monitoring\ServerClosedEvent
source_url: https://www.php.net/manual/es/class.mongodb-driver-monitoring-serverclosedevent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/serverclosedevent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 36c32a2a9
order: 50490
---

## Introducción

La clase `MongoDB\Driver\Monitoring\ServerClosedEvent` encapsula información sobre un servidor cerrado. Esto corresponde a un servidor existente que ha sido retirado de la topología.

## Sinopsis de la clase

MongoDB\Driver\Monitoring\ServerClosedEvent

final

MongoDB\Driver\Monitoring\ServerClosedEvent

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
El nombre de host del servidor.

`port`  
El puerto del servidor.

`topologyId`  
El identificador de la topología.

## Historial de cambios

| Versión            | Descripción                                 |
|--------------------|---------------------------------------------|
| PECL mongodb 2.3.0 | Se añadieron propiedades públicas readonly. |
