---
title: MongoDB\Driver\Session::getOperationTime
description: Devuelve el tiempo de operación para esta sesión
source_url: https://www.php.net/manual/es/mongodb-driver-session.getoperationtime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/session/getoperationtime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51330
---

MongoDB\Driver\Session::getOperationTime

Devuelve el tiempo de operación para esta sesión

## Descripción

```php
final public MongoDB\Driver\Session::getOperationTime(): MongoDB\BSON\Timestamp
```php

Devuelve el tiempo de operación para esta sesión. Si la sesión no ha sido utilizada para una operación y MongoDB\Driver\Session::advanceOperationTime no ha sido llamado, el tiempo de operación será `null`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el tiempo de operación para esta sesión, o `null` si la sesión no tiene tiempo de operación.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Session::advanceOperationTime
