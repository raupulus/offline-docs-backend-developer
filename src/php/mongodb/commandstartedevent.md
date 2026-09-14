---
title: La clase MongoDB\Driver\Monitoring\CommandStartedEvent
source_url: https://www.php.net/manual/es/class.mongodb-driver-monitoring-commandstartedevent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/commandstartedevent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 36c32a2a9
order: 50110
---

## Introducción

La clase `MongoDB\Driver\Monitoring\CommandStartedEvent` contiene la información sobre una orden que ha comenzado.

## Sinopsis de la clase

MongoDB\Driver\Monitoring\CommandStartedEvent

final

MongoDB\Driver\Monitoring\CommandStartedEvent

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

object

command

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

`command`  
El documento del comando.

`operationId`  
El identificador de operación. Puede usarse para vincular eventos entre sí, como en escrituras en bloque, que pueden despachar varios comandos.

`requestId`  
El identificador de la petición. Puede usarse para asociar este `MongoDB\Driver\Monitoring\CommandStartedEvent` con un `MongoDB\Driver\Monitoring\CommandSucceededEvent` o `MongoDB\Driver\Monitoring\CommandFailedEvent` correspondiente.

`serviceId`  
El identificador de servicio, o `null` si el servidor no lo soporta (es decir, cuando no se utiliza el modo de balanceo de carga).

`serverConnectionId`  
El identificador de la conexión al servidor, o `null` si no está disponible.

## Historial de cambios

| Versión            | Descripción                                 |
|--------------------|---------------------------------------------|
| PECL mongodb 2.3.0 | Se añadieron propiedades públicas readonly. |
