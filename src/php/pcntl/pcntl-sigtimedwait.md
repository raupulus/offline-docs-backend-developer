---
title: pcntl_sigtimedwait
description: Espera una señal en un tiempo dado
source_url: https://www.php.net/manual/es/function.pcntl-sigtimedwait.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-sigtimedwait.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: true
translation_revision: 7bc131d65
order: 61380
---

pcntl_sigtimedwait

Espera una señal en un tiempo dado

## Descripción

```php
pcntl_sigtimedwait(array $signals, [array $info], [int $seconds], [int $nanoseconds]): int
```php

La función `pcntl_sigtimedwait` opera exactamente como `pcntl_sigwaitinfo` excepto por el hecho de que toma dos parámetros adicionales: `seconds` y `nanoseconds`, que establecen una duración máxima de espera.

## Parámetros

`signals`  
Una lista de señales a esperar.

`info`  
El parámetro `info` recibe la información de la señal, en forma de array. Véase `pcntl_sigwaitinfo`.

`seconds`  
Tiempo máximo de espera en segundos.

`nanoseconds`  
Tiempo máximo de espera en nanosegundos.

## Valores devueltos

`pcntl_sigtimedwait` devuelve un número de señal en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Se lanza una excepción `ValueError` si el `signal` está vacío. |
| 8.4.0 | Se lanza una excepción `TypeError` si el valor de `signal` no es un `int`. |
| 8.4.0 | Se lanza una excepción `ValueError` si el valor de `signal` es inválido. |
| 8.4.0 | Se lanza una excepción `ValueError` si el valor de `seconds` es inferior a `0`. |
| 8.4.0 | Se lanza una excepción `ValueError` si el valor de `nanoseconds` es inferior a `0`. |
| 8.4.0 | Se lanza una excepción `ValueError` si los valores de `seconds` y de `nanoseconds` son ambos iguales a `0`. |

## Véase también

`pcntl_sigprocmask`, `pcntl_sigwaitinfo`
