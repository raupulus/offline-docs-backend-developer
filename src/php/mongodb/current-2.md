---
title: MongoDB\Driver\Cursor::current
description: Devuelve el elemento actual
source_url: https://www.php.net/manual/es/mongodb-driver-cursor.current.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/cursor/current.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49250
---

MongoDB\Driver\Cursor::current

Devuelve el elemento actual

## Descripción

```php
public MongoDB\Driver\Cursor::current(): array
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el documento de resultado actual como un array u objeto, dependiendo del mapa de tipos del cursor. Si la iteración no ha comenzado o la posición actual no es válida, se devolverá `null`.

## Véase también

Iterator::current
