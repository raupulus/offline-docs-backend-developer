---
title: MongoDB\Driver\Session::isDirty
description: Indica si la sesión ha sido marcada como sucia
source_url: https://www.php.net/manual/es/mongodb-driver-session.isdirty.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/session/isdirty.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51370
---

MongoDB\Driver\Session::isDirty

Indica si la sesión ha sido marcada como sucia

## Descripción

```php
final public MongoDB\Driver\Session::isDirty(): bool
```php

Indica si la sesión ha sido marcada como sucia (es decir, que ha sido utilizada con un comando que ha encontrado un error de red).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Indica si la sesión ha sido marcada como sucia.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.
