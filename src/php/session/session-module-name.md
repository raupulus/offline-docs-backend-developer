---
title: session_module_name
description: Lee y/o modifica el módulo de sesión actual
source_url: https://www.php.net/manual/es/function.session-module-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/functions/session-module-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: false
translation_revision: 151e61773
order: 73820
---

session_module_name

Lee y/o modifica el módulo de sesión actual

## Descripción

```php
session_module_name([string $module]): string
```php

`session_module_name` recupera el nombre del módulo de sesión actual, que también es conocido como [session.save_handler](#ini.session.save-handler).

## Parámetros

`module`  
Si `module` es proporcionado y no es `null`, este valor será utilizado y reemplazará el valor actual. Pasar `"user"` a este argumento está prohibido. En su lugar, `session_set_save_handler` debe ser llamado para definir un manejador de sesión definido por el usuario.

## Valores devueltos

Retorna el nombre del módulo de sesión actual, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `module` ahora es nullable. |
| 7.2.0 | Ahora está explícitamente prohibido definir el nombre del modo como `"user"`. Anteriormente, esto era ignorado silenciosamente. |
