---
title: session_save_path
description: Lee y/o modifica la ruta de guardado de las sesiones
source_url: https://www.php.net/manual/es/function.session-save-path.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/functions/session-save-path.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: true
translation_revision: '802973134'
order: 73870
---

session_save_path

Lee y/o modifica la ruta de guardado de las sesiones

## Descripción

```php
session_save_path([string $path]): string
```php

`session_save_path` devuelve la ruta del directorio actualmente utilizado para guardar los datos de las sesiones.

## Parámetros

`path`  
Ruta de los datos de sesión. Si `path` está especificado y no es `null`, la ruta del directorio será modificada. `session_save_path` debe ser llamado antes que `session_start`.

> [!NOTE]
> En ciertos sistemas operativos, será necesario elegir una ruta hacia un directorio capaz de manejar un gran número de pequeños ficheros de manera eficiente.

## Valores devueltos

Devuelve la ruta del directorio actual utilizado para almacenar los datos, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción               |
|---------|---------------------------|
| 8.0.0   | `path` ahora es nullable. |

## Véase también

La directiva de configuración [session.save_path](#ini.session.save-path)
