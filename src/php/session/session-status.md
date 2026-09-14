---
title: session_status
description: Determina el estado de la sesión actual
source_url: https://www.php.net/manual/es/function.session-status.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/functions/session-status.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: false
translation_revision: 35b95a56c
order: 73910
---

session_status

Determina el estado de la sesión actual

## Descripción

```php
session_status(): int
```php

`session_status` se utiliza para conocer el estado de la sesión actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

- `PHP_SESSION_DISABLED` si las sesiones están desactivadas.

- `PHP_SESSION_NONE` si las sesiones están activadas, pero no existe ninguna.

- `PHP_SESSION_ACTIVE` si las sesiones están activadas y existe una.

## Véase también

session_start
