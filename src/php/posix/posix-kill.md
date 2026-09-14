---
title: posix_kill
description: Enviar una señal a un proceso
source_url: https://www.php.net/manual/es/function.posix-kill.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-kill.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: 42ed815ea
order: 65350
---

posix_kill

Enviar una señal a un proceso

## Descripción

```php
posix_kill(int $process_id, int $signal): bool
```php

Envía la señal `signal` al proceso con el identificador de proceso `process_id`.

## Parámetros

`process_id`  
El identificador de proceso.

`signal`  
Una de las [constantes de señales PCNTL](#pcntl.constants).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Ahora lanza una ValueError cuando `process_id` es menor o mayor que lo que la plataforma soporta (rango de entero con signo o long). |

## Véase también

La página del manual kill(2) del sistema POSIX, la cual contiene información información sobre identificadores de procesos negativos, el pid especial 0, el pid especial -1, y la señal número 0.
