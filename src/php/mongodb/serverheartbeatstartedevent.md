---
title: La clase MongoDB\Driver\Monitoring\ServerHeartbeatStartedEvent
source_url: https://www.php.net/manual/es/class.mongodb-driver-monitoring-serverheartbeatstartedevent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/serverheartbeatstartedevent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 36c32a2a9
order: 50590
---

## Introducción

La clase `MongoDB\Driver\Monitoring\ServerHeartbeatStartedEvent` encapsula información sobre un latido de servidor iniciado (es decir, [comando hello](https://www.mongodb.com/docs/manual/reference/command/hello/) emitido a través de [la supervisión del servidor](https://github.com/mongodb/specifications/blob/master/source/server-discovery-and-monitoring/server-discovery-and-monitoring.md)).

## Sinopsis de la clase

MongoDB\Driver\Monitoring\ServerHeartbeatStartedEvent

final

MongoDB\Driver\Monitoring\ServerHeartbeatStartedEvent

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

bool

awaited

Métodos

## Propiedades

`host`  
El host del servidor.

`port`  
El puerto del servidor.

`awaited`  
Indica si el latido utilizó un protocolo de transmisión continua. La extensión no utiliza el protocolo de transmisión continua para la supervisión, por lo que este método siempre devolverá `false`.

## Historial de cambios

| Versión            | Descripción                                 |
|--------------------|---------------------------------------------|
| PECL mongodb 2.3.0 | Se añadieron propiedades públicas readonly. |
