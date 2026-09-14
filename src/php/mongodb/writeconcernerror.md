---
title: La clase MongoDB\Driver\WriteConcernError
source_url: https://www.php.net/manual/es/class.mongodb-driver-writeconcernerror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/writeconcernerror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 36c32a2a9
order: 51560
---

## Introducción

La clase `MongoDB\Driver\WriteConcernError` contiene información relativa a un error de escritura y puede ser devuelta por MongoDB\Driver\WriteResult::getWriteConcernError.

## Sinopsis de la clase

MongoDB\Driver\WriteConcernError

final

MongoDB\Driver\WriteConcernError

Propiedades

public

readonly

string

message

public

readonly

int

code

public

readonly

object

null

info

Métodos

## Propiedades

`message`  
El mensaje de error.

`code`  
El código de error.

`info`  
El documento de información adicional sobre el error, o `null` si no está disponible.

## Historial de cambios

| Versión            | Descripción                                        |
|--------------------|----------------------------------------------------|
| PECL mongodb 2.3.0 | Las propiedades public readonly han sido añadidas. |
