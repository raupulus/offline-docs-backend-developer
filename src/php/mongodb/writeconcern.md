---
title: La clase MongoDB\Driver\WriteConcern
source_url: https://www.php.net/manual/es/class.mongodb-driver-writeconcern.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/writeconcern.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 36c32a2a9
order: 51520
---

## Introducción

`MongoDB\Driver\WriteConcern` describe el nivel de acuse de recibo solicitado por MongoDB para las operaciones de escritura a un `mongod` autónomo o a conjuntos de réplicas o a clusters fragmentados. En los clusters fragmentados, las instancias de `mongos` transmiten el control de escritura a los fragmentos.

## Sinopsis de la clase

MongoDB\Driver\WriteConcern

final

MongoDB\Driver\WriteConcern

MongoDB\BSON\Serializable

Serializable

Constantes

const

string

MongoDB\Driver\WriteConcern::MAJORITY

"majority"

Propiedades

public

readonly

string

int

null

w

public

readonly

bool

null

j

public

readonly

int

wtimeout

Métodos

## Propiedades

`w`  
El número de réplicas necesarias (entero correspondiente al número de nodos, la cadena `"majority"`, o el nombre de un tag de write concern personalizado), o `null` si no está definido.

`j`  
Indica si el journal es requerido, es decir, si las operaciones de escritura deben ser confirmadas en el journal antes de ser reconocidas, o `null` si no se especificó.

`wtimeout`  
El timeout de espera en milisegundos para el reconocimiento del write concern. Un valor de `0` significa esperar indefinidamente.

## Constantes predefinidas

`MongoDB\Driver\WriteConcern::MAJORITY`  
La mayoría de todos los miembros del conjunto; árbitros, los mismos no votantes, los miembros pasivos, los miembros ocultos y los miembros en espera están todos incluidos en la definición de una preocupación de escritura de la mayoría.

## Historial de cambios

| Versión            | Descripción                                     |
|--------------------|-------------------------------------------------|
| PECL mongodb 2.3.0 | Se añadieron las propiedades públicas readonly. |
| PECL mongodb 1.7.0 | Implementa Serializable.                        |
| PECL mongodb 1.2.0 | Implementa MongoDB\BSON\Serializable.           |
