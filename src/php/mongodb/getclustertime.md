---
title: MongoDB\Driver\Session::getClusterTime
description: Devuelve el tiempo del cluster para esta sesión
source_url: https://www.php.net/manual/es/mongodb-driver-session.getclustertime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/session/getclustertime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51310
---

MongoDB\Driver\Session::getClusterTime

Devuelve el tiempo del cluster para esta sesión

## Descripción

```php
final public MongoDB\Driver\Session::getClusterTime(): object
```php

Devuelve el tiempo del cluster para esta sesión. Si la sesión no ha sido utilizada para una operación y MongoDB\Driver\Session::advanceClusterTime no ha sido llamado, el tiempo del cluster será `null`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el tiempo del cluster para esta sesión, o `null` si la sesión no tiene tiempo del cluster.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Session::advanceClusterTime
