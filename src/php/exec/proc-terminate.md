---
title: proc_terminate
description: Mata un proceso abierto mediante proc_open
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/exec/functions/proc-terminate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: exec
translation_status: ready
translation_reviewed: false
translation_revision: 9af43469f
order: 20610
---

proc_terminate

Mata un proceso abierto mediante proc_open

## Descripción

```php
proc_terminate(resource $process, [int $signal]): bool
```php

Señala un `process` (creado usando `proc_open`) que debe terminar. `proc_terminate` regresa inmediatamente y espera a la terminación del proceso.

`proc_terminate` Permite terminar el proceso y continuar con otras tareas. Puede consultar el estado del proceso (para ver si se ha detenido) usando la función `proc_get_status`.

## Parámetros

`process`  
El `recurso` de `proc_open` que será cerrado.

`signal`  
Este parámetro opcional solo es útil en sistemas operativos POSIX; puede especificar una señal para enviar al proceso utilizando la llamada al sistema `kill(2)`. Por defecto es `SIGTERM`.

## Valores devueltos

Devuelve el estado de terminación del proceso que se ejecutó.

## Véase también

`proc_open`, `proc_close`, `proc_get_status`
