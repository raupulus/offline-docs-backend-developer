---
title: La clase MongoDB\Driver\Monitoring\ServerHeartbeatFailedEvent
source_url: https://www.php.net/manual/es/class.mongodb-driver-monitoring-serverheartbeatfailedevent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/serverheartbeatfailedevent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 36c32a2a9
order: 50550
---

## Introducción

La clase `MongoDB\Driver\Monitoring\ServerHeartbeatFailedEvent` encapsula información sobre un fallo de latido de servidor (es decir, [hello](https://www.mongodb.com/docs/manual/reference/command/hello/) comando emitido por [monitoreo del servidor](https://github.com/mongodb/specifications/blob/master/source/server-discovery-and-monitoring/server-discovery-and-monitoring.md)).

## Sinopsis de la clase

MongoDB\Driver\Monitoring\ServerHeartbeatFailedEvent

final

MongoDB\Driver\Monitoring\ServerHeartbeatFailedEvent

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

public

readonly

int

duration

public

readonly

Exception

error

Métodos

## Propiedades

`host`  
El nombre de host del servidor.

`port`  
El puerto del servidor.

`awaited`  
Indica si el latido utilizó un protocolo de streaming. La extensión no utiliza el protocolo de streaming para la monitorización, por lo que este método siempre devolverá `false`.

`duration`  
La duración del latido en microsegundos. La duración es un valor calculado que incluye el tiempo de envío del mensaje y de recepción de la respuesta del servidor.

`error`  
La excepción lanzada cuando el latido falló.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 2.3.0 | Se añadieron propiedades públicas readonly. La propiedad `duration` reemplaza al método getDurationMicros. |
