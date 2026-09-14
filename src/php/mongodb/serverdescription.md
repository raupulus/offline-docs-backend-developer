---
title: La clase MongoDB\Driver\ServerDescription
source_url: https://www.php.net/manual/es/class.mongodb-driver-serverdescription.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/serverdescription.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51240
---

## Introducción

La clase `MongoDB\Driver\ServerDescription` es un objeto valor que representa un servidor al que el controlador está conectado. Las instancias de esta clase son devueltas por los métodos `MongoDB\Driver\Server::getServerDescription` y `MongoDB\Driver\Monitoring\ServerChangedEvent`.

## Sinopsis de la clase

MongoDB\Driver\ServerDescription

final

MongoDB\Driver\ServerDescription

Constantes

const

string

MongoDB\Driver\ServerDescription::TYPE_UNKNOWN

"Unknown"

const

string

MongoDB\Driver\ServerDescription::TYPE_STANDALONE

"Standalone"

const

string

MongoDB\Driver\ServerDescription::TYPE_MONGOS

"Mongos"

const

string

MongoDB\Driver\ServerDescription::TYPE_POSSIBLE_PRIMARY

"PossiblePrimary"

const

string

MongoDB\Driver\ServerDescription::TYPE_RS_PRIMARY

"RSPrimary"

const

string

MongoDB\Driver\ServerDescription::TYPE_RS_SECONDARY

"RSSecondary"

const

string

MongoDB\Driver\ServerDescription::TYPE_RS_ARBITER

"RSArbiter"

const

string

MongoDB\Driver\ServerDescription::TYPE_RS_OTHER

"RSOther"

const

string

MongoDB\Driver\ServerDescription::TYPE_RS_GHOST

"RSGhost"

const

string

MongoDB\Driver\ServerDescription::TYPE_LOAD_BALANCER

"LoadBalancer"

Métodos

## Constantes predefinidas

`MongoDB\Driver\ServerDescription::TYPE_UNKNOWN`  
Tipo de servidor desconocido, devuelto por MongoDB\Driver\ServerDescription::getType.

`MongoDB\Driver\ServerDescription::TYPE_STANDALONE`  
Tipo de servidor independiente, devuelto por MongoDB\Driver\ServerDescription::getType.

`MongoDB\Driver\ServerDescription::TYPE_MONGOS`  
Tipo de servidor Mongos, devuelto por MongoDB\Driver\ServerDescription::getType.

`MongoDB\Driver\ServerDescription::TYPE_POSSIBLE_PRIMARY`  
Tipo de servidor posible primario de conjunto de réplicas, devuelto por MongoDB\Driver\ServerDescription::getType.

Un servidor puede ser identificado como posible primario si aún no ha sido verificado pero otro miembro del conjunto de réplicas considera que es el primario.

`MongoDB\Driver\ServerDescription::TYPE_RS_PRIMARY`  
Tipo de servidor primario de conjunto de réplicas, devuelto por MongoDB\Driver\ServerDescription::getType.

`MongoDB\Driver\ServerDescription::TYPE_RS_SECONDARY`  
Tipo de servidor secundario de conjunto de réplicas, devuelto por MongoDB\Driver\ServerDescription::getType.

`MongoDB\Driver\ServerDescription::TYPE_RS_ARBITER`  
Tipo de servidor árbitro de conjunto de réplicas, devuelto por MongoDB\Driver\ServerDescription::getType.

`MongoDB\Driver\ServerDescription::ServerDescription::TYPE_RS_OTHER`  
Tipo de servidor de conjunto de réplicas de otro tipo, devuelto por MongoDB\Driver\ServerDescription::getType.

Estos servidores pueden estar ocultos, iniciándose o en recuperación. No pueden ser consultados, pero sus listas de hosts son útiles para descubrir la configuración actual del conjunto de réplicas.

`MongoDB\Driver\ServerDescription::TYPE_RS_GHOST`  
Tipo de servidor fantasma de conjunto de réplicas, devuelto por MongoDB\Driver\ServerDescription::getType.

Los servidores pueden ser identificados como tales en al menos tres situaciones: brevemente durante el inicio del servidor; en un conjunto de réplicas no inicializado; o cuando el servidor es excluido (es decir, eliminado de la configuración del conjunto de réplicas). No pueden ser consultados, ni su lista de hosts puede usarse para descubrir la configuración actual del conjunto de réplicas; sin embargo, el cliente puede monitorear este servidor con la esperanza de que pase a un estado más útil.

`MongoDB\Driver\ServerDescription::TYPE_LOAD_BALANCER`  
Tipo de servidor equilibrador de carga, devuelto por MongoDB\Driver\ServerDescription::getType.
