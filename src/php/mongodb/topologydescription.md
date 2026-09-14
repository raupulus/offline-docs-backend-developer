---
title: La clase MongoDB\Driver\TopologyDescription
source_url: https://www.php.net/manual/es/class.mongodb-driver-topologydescription.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/topologydescription.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51450
---

## Introducción

La clase `MongoDB\Driver\TopologyDescription` es un objeto valor que representa una topología a la que el controlador está conectado. Las instancias de esta clase son devueltas por los métodos de `MongoDB\Driver\Monitoring\TopologyChangedEvent`.

## Sinopsis de la clase

MongoDB\Driver\TopologyDescription

final

MongoDB\Driver\TopologyDescription

Constantes

const

string

MongoDB\Driver\TopologyDescription::TYPE_UNKNOWN

"Unknown"

const

string

MongoDB\Driver\TopologyDescription::TYPE_SINGLE

"Single"

const

string

MongoDB\Driver\TopologyDescription::TYPE_SHARDED

"Sharded"

const

string

MongoDB\Driver\TopologyDescription::TYPE_REPLICA_SET_NO_PRIMARY

"ReplicaSetNoPrimary"

const

string

MongoDB\Driver\TopologyDescription::TYPE_REPLICA_SET_WITH_PRIMARY

"ReplicaSetWithPrimary"

const

string

MongoDB\Driver\TopologyDescription::TYPE_LOAD_BALANCED

"LoadBalanced"

Métodos

## Constantes predefinidas

`MongoDB\Driver\TopologyDescription::TYPE_UNKNOWN`  
Tipo de topología desconocido, devuelto por MongoDB\Driver\TopologyDescription::getType.

`MongoDB\Driver\TopologyDescription::TYPE_SINGLE`  
Servidor único (es decir, conexión directa), devuelto por MongoDB\Driver\TopologyDescription::getType.

`MongoDB\Driver\TopologyDescription::TYPE_SHARDED`  
Agrupación particionada, devuelto por MongoDB\Driver\TopologyDescription::getType.

`MongoDB\Driver\TopologyDescription::TYPE_REPLICA_SET_NO_PRIMARY`  
Conjunto de réplicas sin servidor primario, devuelto por MongoDB\Driver\TopologyDescription::getType.

`MongoDB\Driver\TopologyDescription::TYPE_REPLICA_SET_WITH_PRIMARY`  
Conjunto de réplicas con un servidor primario, devuelto por MongoDB\Driver\TopologyDescription::getType.

`MongoDB\Driver\TopologyDescription::TYPE_LOAD_BALANCED`  
Topología con equilibrio de carga, devuelto por MongoDB\Driver\TopologyDescription::getType.
