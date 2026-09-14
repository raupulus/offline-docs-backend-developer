---
title: pcntl_sigwaitinfo
description: Espera una señal
source_url: https://www.php.net/manual/es/function.pcntl-sigwaitinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-sigwaitinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: false
translation_revision: 7bc131d65
order: 61390
---

pcntl_sigwaitinfo

Espera una señal

## Descripción

```php
pcntl_sigwaitinfo(array $signals, [array $info]): int
```php

La función `pcntl_sigwaitinfo` suspende su ejecución hasta la recepción de una de las señales indicadas en `signals`. Si una de las señales ya está en espera (i.e., bloqueada por `pcntl_sigprocmask`), `pcntl_sigwaitinfo` se termina inmediatamente.

## Parámetros

`signals`  
Un array de señales a esperar.

`info`  
El parámetro `info` recibe un array que contiene la información sobre la señal.

Los siguientes elementos están siempre disponibles para todas las señales: signo : número de señal, errno : un número de error, code : código de señal

Los siguientes elementos pueden estar disponibles para la señal `SIGCHLD`: status : valor de salida o señal, utime : tiempo de usuario consumido, stime : tiempo de sistema consumido, pid : número de proceso llamante, uid : identificador del usuario llamante, o del proceso llamante

Los siguientes elementos pueden estar disponibles para las señales `SIGILL`, `SIGFPE`, `SIGSEGV` y `SIGBUS`: addr : dirección de memoria que causó el error

Los siguientes elementos pueden estar disponibles para la señal `SIGPOLL`: band : evento de band, fd : número de puntero de fichero

## Valores devueltos

Devuelve un número de señal en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Se lanza una excepción `ValueError` si el `signal` está vacío. |
| 8.4.0 | Se lanza una excepción `TypeError` si el valor de `signal` no es un `int`. |
| 8.4.0 | Se lanza una excepción `ValueError` si el valor de `signal` es inválido. |

## Ejemplos

Ejemplo con `pcntl_sigwaitinfo`

```
<?php
echo "Bloquea la señal SIGHUP\n";
pcntl_sigprocmask(SIG_BLOCK, array(SIGHUP));

echo "Envía la señal SIGHUP a sí mismo\n";
posix_kill(posix_getpid(), SIGHUP);

echo "Espera señales\n";
$info = array();
pcntl_sigwaitinfo(array(SIGHUP), $info);
?>

    
```php

## Véase también

`pcntl_sigprocmask`, `pcntl_sigtimedwait`
