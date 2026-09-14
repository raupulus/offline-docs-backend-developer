---
title: MongoDB\Driver\Session::isInTransaction
description: Indica si una transacción multi-documento está en curso
source_url: https://www.php.net/manual/es/mongodb-driver-session.isintransaction.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/session/isintransaction.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51380
---

MongoDB\Driver\Session::isInTransaction

Indica si una transacción multi-documento está en curso

## Descripción

```php
final public MongoDB\Driver\Session::isInTransaction(): bool
```php

Indica si una transacción multi-documento está actualmente en curso para esta sesión. Una transacción se considera "en curso" si ha sido iniciada pero no ha sido confirmada o anulada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si una transacción está actualmente en curso para esta sesión, y `false` en caso contrario.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Session::getTransactionState
