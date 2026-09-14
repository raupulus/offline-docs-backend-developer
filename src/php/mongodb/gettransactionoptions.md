---
title: MongoDB\Driver\Session::getTransactionOptions
description: Devuelve las opciones para la transacción en curso
source_url: https://www.php.net/manual/es/mongodb-driver-session.gettransactionoptions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/session/gettransactionoptions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51350
---

MongoDB\Driver\Session::getTransactionOptions

Devuelve las opciones para la transacción en curso

## Descripción

```php
final public MongoDB\Driver\Session::getTransactionOptions(): array
```php

Devuelve las opciones para la transacción en curso.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `array` que contiene las opciones de transacción actuales, o `null` si no hay ninguna transacción en curso.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Session::getTransactionState
