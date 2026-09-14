---
title: proc_get_status
description: Lee las informaciones concernientes a un proceso abierto por proc_open
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/exec/functions/proc-get-status.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: exec
translation_status: ready
translation_reviewed: false
translation_revision: af704f619
order: 20580
---

proc_get_status

Lee las informaciones concernientes a un proceso abierto por

proc_open

## Descripción

```php
proc_get_status(resource $process): array
```php

`proc_get_status` lee los datos concernientes al proceso `process` creado con la función `proc_open`.

## Parámetros

`process`  
El `resource` `proc_open` a evaluar.

## Valores devueltos

Un array que contiene las informaciones recolectadas. El array retornado contiene los siguientes elementos :

| Elemento | Tipo | Descripción |
|----|----|----|
| command | `string` | El comando pasado a la función `proc_open`. |
| pid | `int` | identificador del proceso |
| running | `bool` | `true` si el proceso funciona aún y `false` si ha terminado. |
| signaled | `bool` | `true` si el proceso hijo ha sido terminado por un señal desconocido. Siempre definido a `false` bajo Windows. |
| stopped | `bool` | `true` si el proceso hijo ha sido parado por un señal. Siempre definido a `false` bajo Windows. |
| exitcode | `int` | El código retornado por el proceso (únicamente si el elemento `running` vale `false`). Antes de PHP 8.3.0, solo la primera llamada de esta función retornaba el verdadero valor, las llamadas siguientes retornaban `-1`. |
| en caché | `bool` | A partir de PHP 8.3.0, esto es `true` cuando el código de salida está en caché. La caché es necesaria para asegurarse de que el código de salida no se pierde durante las llamadas siguientes a las API de procesamiento. |
| termsig | `int` | el número del señal que ha causado la terminación de la ejecución del proceso hijo (únicamente significativo si `signaled` vale `true`). |
| stopsig | `int` | el número del señal que ha causado la parada de la ejecución del proceso hijo (únicamente significativo si `signaled` vale `true`). |

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | La entrada `"en caché"` ha sido añadida al array retornado. Antes de PHP 8.3.0, solo la primera llamada retornaba el verdadero código de salida. La entrada `"en caché"` indica que el código de salida ha sido puesto en caché. |

## Véase también

`proc_open`
