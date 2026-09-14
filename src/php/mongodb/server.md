---
title: La clase MongoDB\Driver\Server
source_url: https://www.php.net/manual/es/class.mongodb-driver-server.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/server.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 51140
---

## Introducción

## Sinopsis de la clase

MongoDB\Driver\Server

final

MongoDB\Driver\Server

Constantes

const

int

MongoDB\Driver\Server::TYPE_UNKNOWN

0

const

int

MongoDB\Driver\Server::TYPE_STANDALONE

1

const

int

MongoDB\Driver\Server::TYPE_MONGOS

2

const

int

MongoDB\Driver\Server::TYPE_POSSIBLE_PRIMARY

3

const

int

MongoDB\Driver\Server::TYPE_RS_PRIMARY

4

const

int

MongoDB\Driver\Server::TYPE_RS_SECONDARY

5

const

int

MongoDB\Driver\Server::TYPE_RS_ARBITER

6

const

int

MongoDB\Driver\Server::TYPE_RS_OTHER

7

const

int

MongoDB\Driver\Server::TYPE_RS_GHOST

8

const

int

MongoDB\Driver\Server::TYPE_LOAD_BALANCER

9

Métodos

## Constantes predefinidas

`MongoDB\Driver\Server::TYPE_UNKNOWN`  
Tipo de servidor desconocido, devuelto por MongoDB\Driver\Server::getType.

`MongoDB\Driver\Server::TYPE_STANDALONE`  
Tipo de servidor independiente, devuelto por MongoDB\Driver\Server::getType.

`MongoDB\Driver\Server::TYPE_MONGOS`  
Tipo de servidor Mongos, devuelto por MongoDB\Driver\Server::getType.

`MongoDB\Driver\Server::TYPE_POSSIBLE_PRIMARY`  
Tipo de servidor posible primario de conjunto de réplicas, devuelto por MongoDB\Driver\Server::getType.

Un servidor puede identificarse como posible primario si aún no ha sido verificado pero otro miembro del conjunto de réplicas cree que es el primario.

`MongoDB\Driver\Server::TYPE_RS_PRIMARY`  
Tipo de servidor primario de conjunto de réplicas, devuelto por MongoDB\Driver\Server::getType.

`MongoDB\Driver\Server::TYPE_RS_SECONDARY`  
Tipo de servidor secundario de conjunto de réplicas, devuelto por MongoDB\Driver\Server::getType.

`MongoDB\Driver\Server::TYPE_RS_ARBITER`  
Tipo de servidor árbitro de conjunto de réplicas, devuelto por MongoDB\Driver\Server::getType.

`MongoDB\Driver\Server::TYPE_RS_OTHER`  
Tipo de servidor de conjunto de réplicas de otro tipo, devuelto por MongoDB\Driver\Server::getType.

Estos servidores pueden estar ocultos, iniciándose o recuperándose. No pueden ser consultados, pero sus listas de hosts son útiles para descubrir la configuración actual del conjunto de réplicas.

`MongoDB\Driver\Server::TYPE_RS_GHOST`  
Tipo de servidor fantasma de conjunto de réplicas, devuelto por MongoDB\Driver\Server::getType.

Los servidores pueden identificarse como tales en al menos tres situaciones: brevemente durante el inicio del servidor; en un conjunto de réplicas no inicializado; o cuando el servidor es rechazado (es decir, eliminado de la configuración del conjunto de réplicas). No pueden ser consultados, ni se puede usar su lista de hosts para descubrir la configuración actual del conjunto de réplicas; sin embargo, el cliente puede monitorear este servidor con la esperanza de que pase a un estado más útil.

`MongoDB\Driver\Server::TYPE_LOAD_BALANCER`  
Tipo de servidor equilibrador de carga, devuelto por MongoDB\Driver\Server::getType.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 1.11.0 | Se añadió la constante `MongoDB\Driver\Server::TYPE_LOAD_BALANCER`. |
