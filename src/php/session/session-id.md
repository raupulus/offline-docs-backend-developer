---
title: session_id
description: Lee y/o modifica el identificador de sesión actual
source_url: https://www.php.net/manual/es/function.session-id.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/functions/session-id.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: true
translation_revision: f5c124bef
order: 73810
---

session_id

Lee y/o modifica el identificador de sesión actual

## Descripción

```php
session_id([string $id]): string
```php

`session_id` se utiliza para recuperar o definir el identificador de sesión para la sesión actual.

La constante `SID` también puede ser utilizada para leer el nombre de la sesión actual y el identificador de sesión a proporcionar en las URL. Véase también [Gestión de sesión](#ref.session).

## Parámetros

`id`  
Si `id` es proporcionado y no es `null`, reemplazará el identificador de sesión actual. `session_id` debe ser llamado antes de `session_start`. Dependiendo del gestor de sesiones que se utilice, no todos los caracteres serán aceptados en este valor. Por ejemplo, el gestor de sesiones por defecto, basado en archivos, solo acepta caracteres dentro del intervalo `[a-zA-Z0-9,-]`!

> [!NOTE]
> Cuando se utilizan sesiones con cookies, el hecho de especificar un `id` para `session_id` hará que una nueva cookie siempre sea enviada al llamar a `session_start`, independientemente de si el identificador de sesión actual es idéntico al que acaba de ser definido.

## Valores devueltos

`session_id` devuelve el identificador de sesión para la sesión actual o una cadena vacía (`""`) si no hay sesión actual (ningún identificador de sesión existe). En caso de error, `false` es devuelto.

## Historial de cambios

| Versión | Descripción             |
|---------|-------------------------|
| 8.0.0   | `id` ahora es nullable. |

## Véase también

`session_regenerate_id`, `session_start`, `session_set_save_handler`, [session.save_handler](#ini.session.save-handler)
