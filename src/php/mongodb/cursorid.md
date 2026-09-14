---
title: La clase MongoDB\Driver\CursorId
source_url: https://www.php.net/manual/es/class.mongodb-driver-cursorid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/cursorid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49380
---

## Introducción

La clase `MongoDB\Driver\CursorID` es un objeto de valor que representa un identificador de cursor. Las instancias de esta clase son devueltas por `MongoDB\Driver\Cursor::getId`.

> [!WARNING]
> Esta clase ha sido *DEPRECADA* a partir de la versión 1.20.0 de la extensión y fue eliminada en la versión 2.0. Las aplicaciones deben actualizar su uso de MongoDB\Driver\Cursor::getId para devolver `MongoDB\BSON\Int64` en su lugar.

## Sinopsis de la clase

MongoDB\Driver\CursorId

final

MongoDB\Driver\CursorId

Serializable

Stringable

Métodos

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 2.0.0 | Esta clase ha sido eliminada. |
| PECL mongodb 1.20.0 | Esta clase ha sido deprecada y será eliminada en la versión 2.0. |
| PECL mongodb 1.12.0 | Implementa Stringable para PHP 8.0+. |
| PECL mongodb 1.7.0 | Implementa Serializable. |
