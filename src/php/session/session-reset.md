---
title: session_reset
description: Restablece el array de sesión con los valores originales
source_url: https://www.php.net/manual/es/function.session-reset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/functions/session-reset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_revision: 35b95a56c
order: 73860
---

session_reset

Restablece el array de sesión con los valores originales

## Descripción

```php
session_reset(): bool
```php

`session_reset` restablece una sesión con los valores originales almacenados en el almacenamiento de sesión. Esta función requiere una sesión activa y anula los cambios en \$\_SESSION.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.2.0 | El tipo de retorno de esta función es ahora `bool`. Anteriormente, era [void](#language.types.declarations.void). |

## Véase también

`$_SESSION`, La directiva de configuración [session.auto_start](#ini.session.auto-start), `session_start`, `session_abort`, `session_commit`
