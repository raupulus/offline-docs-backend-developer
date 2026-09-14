---
title: MongoDB\Driver\Session::abortTransaction
description: Anula una transacción
source_url: https://www.php.net/manual/es/mongodb-driver-session.aborttransaction.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/session/aborttransaction.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51250
---

MongoDB\Driver\Session::abortTransaction

Anula una transacción

## Descripción

```php
final public MongoDB\Driver\Session::abortTransaction(): void
```php

Termina la transacción multi-documento y anula todas las modificaciones de datos realizadas por las operaciones en la transacción. Es decir, la transacción se termina sin guardar ninguna de las modificaciones realizadas por las operaciones en la transacción.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una

MongoDB\Driver\Exception\RuntimeException

si la transacción no puede ser anulada (por ejemplo, una transacción no ha sido iniciada).

## Véase también

MongoDB\Driver\Manager::startSession

MongoDB\Driver\Session::commitTransaction

MongoDB\Driver\Session::startTransaction
