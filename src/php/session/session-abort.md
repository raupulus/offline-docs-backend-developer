---
title: session_abort
description: Interrumpe los cambios en el array de sesión y finaliza la sesión
source_url: https://www.php.net/manual/es/function.session-abort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/functions/session-abort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_revision: 35b95a56c
order: 73710
---

session_abort

Interrumpe los cambios en el array de sesión y finaliza la sesión

## Descripción

```php
session_abort(): bool
```php

`session_abort` finaliza la sesión sin guardar los datos. Los valores originales de la sesión se conservan.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.2.0 | El tipo de retorno de esta función es ahora `bool`. Anteriormente, era [void](#language.types.declarations.void). |

## Véase también

`$_SESSION`, La directiva de configuración [session.auto_start](#ini.session.auto-start), `session_start`, `session_reset`, `session_commit`
