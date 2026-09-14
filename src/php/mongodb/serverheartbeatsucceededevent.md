---
title: La clase MongoDB\Driver\Monitoring\ServerHeartbeatSucceededEvent
source_url: https://www.php.net/manual/es/class.mongodb-driver-monitoring-serverheartbeatsucceededevent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/serverheartbeatsucceededevent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 36c32a2a9
order: 50650
---

## Introducción

La clase `MongoDB\Driver\Monitoring\ServerHeartbeatSucceededEvent` encapsula información sobre un latido de servidor exitoso (es decir, [comando hello](https://www.mongodb.com/docs/manual/reference/command/hello/) emitido a través de [la supervisión del servidor](https://github.com/mongodb/specifications/blob/master/source/server-discovery-and-monitoring/server-discovery-and-monitoring.md)).

## Sinopsis de la clase

MongoDB\Driver\Monitoring\ServerHeartbeatSucceededEvent

final

MongoDB\Driver\Monitoring\ServerHeartbeatSucceededEvent

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

object

reply

Métodos

## Propiedades

`host`  
El host del servidor.

`port`  
El puerto del servidor.

`awaited`  
Indica si el latido utilizó un protocolo de transmisión continua. La extensión no utiliza el protocolo de transmisión continua para la supervisión, por lo que este método siempre devolverá `false`.

`duration`  
La duración del latido en microsegundos. La duración es un valor calculado que incluye el tiempo necesario para enviar el mensaje y recibir la respuesta del servidor.

`reply`  
El documento de respuesta devuelto por el servidor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 2.3.0 | Se añadieron propiedades públicas readonly. La propiedad `duration` reemplaza al método getDurationMicros. |
