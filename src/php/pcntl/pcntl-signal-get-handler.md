---
title: pcntl_signal_get_handler
description: Recupera el gestor actual para la señal especificada
source_url: https://www.php.net/manual/es/function.pcntl-signal-get-handler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-signal-get-handler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: false
translation_revision: b890f28c0
order: 61350
---

pcntl_signal_get_handler

Recupera el gestor actual para la señal especificada

## Descripción

```php
pcntl_signal_get_handler(int $signal): callable
```php

La función `pcntl_signal_get_handler` recupera el gestor actual para la `signal` especificada.

## Parámetros

`signal`  
El número de la señal.

## Valores devueltos

Esta función puede devolver un valor entero que se refiere a `SIG_DFL` o a `SIG_IGN`. Si se ha definido un gestor personalizado, este `callable` es devuelto.

## Historial de cambios

| Versión | Descripción                                        |
|---------|----------------------------------------------------|
| 7.1.0   | La función `pcntl_signal_get_handler` fue añadida. |

## Ejemplos

Ejemplo con `pcntl_signal_get_handler`

```
<?php
var_dump(pcntl_signal_get_handler(SIGUSR1)); // Muestra: int(0)

function pcntl_test($signo) {}
pcntl_signal(SIGUSR1, 'pcntl_test');
var_dump(pcntl_signal_get_handler(SIGUSR1)); // Muestra: string(10) "pcntl_test"

pcntl_signal(SIGUSR1, SIG_DFL);
var_dump(pcntl_signal_get_handler(SIGUSR1)); // Muestra: int(0)

pcntl_signal(SIGUSR1, SIG_IGN);
var_dump(pcntl_signal_get_handler(SIGUSR1)); // Muestra: int(1)
?>

    
```php

## Véase también

pcntl_signal
