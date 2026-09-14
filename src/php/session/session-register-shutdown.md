---
title: session_register_shutdown
description: Función de cierre de sesiones
source_url: https://www.php.net/manual/es/function.session-register-shutdown.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/functions/session-register-shutdown.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_revision: 67525a12b
order: 73850
---

session_register_shutdown

Función de cierre de sesiones

## Descripción

```php
session_register_shutdown(): void
```php

Registra `session_write_close` como una función de cierre.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Emite un error de nivel `E_WARNING` si la función de cierre falla.
