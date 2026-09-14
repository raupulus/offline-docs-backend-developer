---
title: pcntl_signal
description: Instala un gestor de señales
source_url: https://www.php.net/manual/es/function.pcntl-signal.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-signal.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: false
translation_revision: 5fe0f8494
order: 61360
---

pcntl_signal

Instala un gestor de señales

## Descripción

```php
pcntl_signal(int $signal, callable $handler, [bool $restart_syscalls]): bool
```php

`pcntl_signal` instala un nuevo gestor de señales o reemplaza el gestor de señales actual para la señal indicada por el parámetro `signal`.

## Parámetros

`signal`  
El número de la señal.

`handler`  
El gestor de señales. Puede ser un `callable`, que será llamado para gestionar la señal, o bien una de las dos constantes globales `SIG_IGN` o `SIG_DFL`, que, respectivamente, ignorarán la señal o restaurarán el gestor de señales por defecto.

Si se proporciona un `callable`, debe implementar la siguiente firma:

```php
handler(int $signo, mixed $siginfo): void
```

`signal`  
La señal a gestionar.

`siginfo`  
Si el sistema operativo soporta las estructuras siginfo_t, esto será un array de información de la señal que depende de la señal.

> [!NOTE]
> Téngase en cuenta que cuando se configura el gestor con un método de objeto, el contador de referencia del objeto se incrementa, lo que lo hace persistente hasta que se cambie el gestor de señales por otro, o hasta que el script termine.

`restart_syscalls`  
Especifica si la llamada al sistema de reinicio (restarting) debe ser utilizada cuando llega esta señal.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.1.0 | A partir de PHP 7.1.0 el gestor de la función de retrollamada tiene un segundo argumento que contiene el siginfo de esa señal específica. Estos datos solo se proporcionan si el sistema operativo tiene la estructura siginfo_t. Si el sistema operativo no implementa siginfo_t, se proporciona NULL. |

## Ejemplos

Ejemplo con `pcntl_signal`

```php
<?php
pcntl_async_signals(true);

// gestor de señales del sistema
function sig_handler($signo)
{

     switch ($signo) {
         case SIGTERM:
             // gestión de la extinción
             exit;
             break;
         case SIGHUP:
             // gestión del reinicio
             break;
         case SIGUSR1:
             echo "Recibida la señal SIGUSR1...\n";
             break;
         default:
             // gestión de otras señales
     }

}

echo "Instalación del gestor de señales...\n";

// Instalación de los gestores de señales
pcntl_signal(SIGTERM, "sig_handler");
pcntl_signal(SIGHUP,  "sig_handler");
pcntl_signal(SIGUSR1, "sig_handler");

// o bien utilice un objeto
// pcntl_signal(SIGUSR1, array($obj, "hacer_algo"));

echo"Generación de una señal SIGUSR1 a mí mismo...\n";

// envío de SIGUSR1 al identificador de proceso actual
// las funciones posix_* requieren la extensión posix
posix_kill(posix_getpid(), SIGUSR1);

echo "Hecho\n";

?>

    
```

## Notas

La función `pcntl_signal` no apila los gestores de señales, sino que los reemplaza.

## Método de dispatch

Existen varios métodos para dispatchar los gestores de señales: Dispatch asíncrono con `pcntl_async_signals` activado. Este es el método recomendado, Establecer la frecuencia de los [ticks](#control-structures.declare.ticks), Dispatch manual con `pcntl_signal_dispatch`

Cuando las señales son dispatchadas de manera asíncrona o utilizando una ejecución basada en ticks, las funciones bloqueantes como `sleep` pueden ser interrumpidas.

## Véase también

[Signal (IPC)](https://en.wikipedia.org/wiki/Signal_(IPC)) en Wikipedia, `pcntl_async_signals`, `pcntl_fork`, `pcntl_signal_dispatch`, `pcntl_waitpid`
