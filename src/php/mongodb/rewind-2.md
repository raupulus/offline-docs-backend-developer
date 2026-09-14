---
title: MongoDB\Driver\Cursor::rewind
description: Rebobinar el cursor a la primera posición
source_url: https://www.php.net/manual/es/mongodb-driver-cursor.rewind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/cursor/rewind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49310
---

MongoDB\Driver\Cursor::rewind

Rebobinar el cursor a la primera posición

## Descripción

```php
public MongoDB\Driver\Cursor::rewind(): void
```php

Si el cursor ha avanzado más allá de su primera posición, ya no podrá rebobinarse.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`null`.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una excepción

MongoDB\Driver\Exception\ConnectionException

si la conexión al servidor falla por una razón distinta a un problema de identificación

Lanza una excepción

MongoDB\Driver\Exception\AuthenticationException

si se requiere una identificación pero falla

Lanza

MongoDB\Driver\Exception\LogicException

si este método se invoca después de que el cursor haya avanzado más allá de su primera posición.

## Véase también

Iterator::rewind
