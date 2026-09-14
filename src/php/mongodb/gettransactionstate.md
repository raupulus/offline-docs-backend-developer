---
title: MongoDB\Driver\Session::getTransactionState
description: Devuelve el estado de la transacción actual para esta sesión
source_url: https://www.php.net/manual/es/mongodb-driver-session.gettransactionstate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/session/gettransactionstate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51360
---

MongoDB\Driver\Session::getTransactionState

Devuelve el estado de la transacción actual para esta sesión

## Descripción

```php
final public MongoDB\Driver\Session::getTransactionState(): string
```php

Devuelve el estado de la transacción para esta sesión.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el estado de la transacción actual para esta sesión.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Session::isInTransaction

MongoDB\Driver\Session::getTransactionOptions
