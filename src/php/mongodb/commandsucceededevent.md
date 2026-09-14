---
title: La clase MongoDB\Driver\Monitoring\CommandSucceededEvent
source_url: https://www.php.net/manual/es/class.mongodb-driver-monitoring-commandsucceededevent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/commandsucceededevent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 36c32a2a9
order: 50270
---

## Introducción

La clase `MongoDB\Driver\Monitoring\CommandSucceededEvent` encapsula información sobre un comando exitoso.

## Sinopsis de la clase

MongoDB\Driver\Monitoring\CommandSucceededEvent

final

MongoDB\Driver\Monitoring\CommandSucceededEvent

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

string

commandName

public

readonly

string

databaseName

public

readonly

int

duration

public

readonly

object

reply

public

readonly

string

operationId

public

readonly

string

requestId

public

readonly

MongoDB\BSON\ObjectId

null

serviceId

public

readonly

int

null

serverConnectionId

Métodos

## Propiedades

`host`  
El nombre del host del servidor que ejecutó el comando.

`port`  
El puerto del servidor que ejecutó el comando.

`commandName`  
El nombre del comando.

`databaseName`  
El nombre de la base de datos.

`duration`  
La duración del comando en microsegundos. La duración es un valor calculado que incluye el tiempo necesario para enviar el mensaje y recibir la respuesta del servidor.

`reply`  
El documento de respuesta devuelto por el servidor.

`operationId`  
El identificador de operación. Puede usarse para vincular eventos entre sí, como en escrituras en bloque, que pueden despachar varios comandos.

`requestId`  
El identificador de la petición. Puede usarse para asociar este `MongoDB\Driver\Monitoring\CommandSucceededEvent` con un `MongoDB\Driver\Monitoring\CommandStartedEvent` correspondiente.

`serviceId`  
El identificador de servicio, o `null` si el servidor no lo soporta (es decir, cuando no se utiliza el modo de balanceo de carga).

`serverConnectionId`  
El identificador de la conexión al servidor, o `null` si no está disponible.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 2.3.0 | Se añadieron propiedades públicas readonly. La propiedad `duration` reemplaza al método getDurationMicros. |
