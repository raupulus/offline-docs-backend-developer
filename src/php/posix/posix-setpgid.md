---
title: posix_setpgid
description: Establecer el id de grupo de procesos para el control de trabajo
source_url: https://www.php.net/manual/es/function.posix-setpgid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-setpgid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: 42ed815ea
order: 65420
---

posix_setpgid

Establecer el id de grupo de procesos para el control de trabajo

## Descripción

```php
posix_setpgid(int $process_id, int $process_group_id): bool
```php

Permite al proceso `process_id` unirse al grupo de procesos `process_group_id`.

## Parámetros

`process_id`  
El id del proceso.

`process_group_id`  
El id de grupo de procesos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Ahora lanza una ValueError cuando `process_id` o `process_group_id` es menor que cero o mayor que lo que la plataforma soporta. |

## Véase también

Véase POSIX.1 y la página del manual setsid(2) del sistema POSIX para más información sobre grupos de proceoss y control de trabajo.
