---
title: La clase MongoDB\Driver\WriteError
source_url: https://www.php.net/manual/es/class.mongodb-driver-writeerror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/writeerror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 36c32a2a9
order: 51610
---

## Introducción

La clase `MongoDB\Driver\WriteError` contiene información sobre un error de escritura y puede ser devuelta como elemento de un array a partir de MongoDB\Driver\WriteResult::getWriteErrors.

## Sinopsis de la clase

MongoDB\Driver\WriteError

final

MongoDB\Driver\WriteError

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

int

index

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

`index`  
El índice de la operación de escritura dentro del `MongoDB\Driver\BulkWrite` que ha provocado el error.

`info`  
El documento de información adicional sobre el error, o `null` si no está disponible.

## Historial de cambios

| Versión            | Descripción                                        |
|--------------------|----------------------------------------------------|
| PECL mongodb 2.3.0 | Las propiedades public readonly han sido añadidas. |
