---
title: pcntl_sigprocmask
description: Lista y configura las señales bloqueadas
source_url: https://www.php.net/manual/es/function.pcntl-sigprocmask.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-sigprocmask.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: false
translation_revision: 7bc131d65
order: 61370
---

pcntl_sigprocmask

Lista y configura las señales bloqueadas

## Descripción

```php
pcntl_sigprocmask(int $mode, array $signals, [array $old_signals]): bool
```php

La función `pcntl_sigprocmask` añade, retira o configura las señales bloqueadas, en función del parámetro `mode`.

## Parámetros

`mode`  
Configura el comportamiento de `pcntl_sigprocmask`. Los valores posibles son : `SIG_BLOCK` : añade la señal a la lista de señales bloqueadas., `SIG_UNBLOCK`: retira la señal de la lista de señales bloqueadas., `SIG_SETMASK` : reemplaza la lista actual de señales bloqueadas por una nueva lista.

`signals`  
Lista de señales.

`old_signals`  
El parámetro `old_signals` es un array que contiene la lista anterior de señales bloqueadas.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Se lanza una excepción `ValueError` si el `signal` está vacío. |
| 8.4.0 | Se lanza una excepción `TypeError` si el valor de `signal` no es un `int`. |
| 8.4.0 | Se lanza una excepción `ValueError` si el valor de `signal` es inválido. |
| 8.4.0 | Se lanza una excepción `ValueError` si el valor de `mode` no es `SIG_BLOCK`, `SIG_UNBLOCK` o `SIG_SETMASK`. |

## Ejemplos

Ejemplo con `pcntl_sigprocmask`

```
<?php
pcntl_sigprocmask(SIG_BLOCK, array(SIGHUP));
$oldset = array();
pcntl_sigprocmask(SIG_UNBLOCK, array(SIGHUP), $oldset);
?>

    
```php

## Véase también

`pcntl_sigwaitinfo`, `pcntl_sigtimedwait`
