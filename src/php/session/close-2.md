---
title: SessionHandlerInterface::close
description: Cerrar la sesión
source_url: https://www.php.net/manual/es/sessionhandlerinterface.close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/sessionhandlerinterface/close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_revision: 601f6f4ce
order: 74040
---

SessionHandlerInterface::close

Cerrar la sesión

## Descripción

```php
public SessionHandlerInterface::close(): bool
```php

Cierra la sesión actual. Esta función se ejecuta automáticamente al cerrar la sesión, o explícitamente mediante `session_write_close`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El valor devuelto (habitualmente `true` en caso de éxito, `false` si ocurre un error). Tenga en cuenta que este valor es devuelto internamente a PHP para análisis.
