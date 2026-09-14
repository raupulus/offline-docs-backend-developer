---
title: proc_close
description: Cierra los pipes hacia un proceso abierto por proc_open, espera a que
  termine y devuelve su código de salida
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/exec/functions/proc-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: exec
translation_status: ready
translation_reviewed: false
translation_revision: 970d3aa7f
order: 20570
---

proc_close

Cierra los pipes hacia un proceso abierto por

proc_open

, espera a que termine y devuelve su código de salida

## Descripción

```php
proc_close(resource $process): int
```php

`proc_close` es similar a `pclose` excepto que funciona con los procesos abiertos por `proc_open`. `proc_close` espera a que el proceso `process` termine, luego devuelve su código de salida. Los pipes abiertos con este proceso son cerrados cuando esta función es llamada para evitar bloqueos: el proceso puede no poder salir mientras los pipes estén abiertos.

## Parámetros

`process`  
El `resource` `proc_open` a cerrar

## Valores devueltos

Devuelve el estado de terminación del proceso que se ejecutó. En caso de error, se devuelve `-1`.

> [!NOTE]
> Si PHP ha sido compilado con la opción de configuración --enable-sigchild, el valor devuelto de esta función será indefinido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | `proc_close` ahora devuelve el código de salida correcto incluso cuando se ha llamado previamente a `proc_get_status`. Anteriormente se devolvía `-1` en ese caso. |
