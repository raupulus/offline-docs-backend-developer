---
title: getrusage
description: Devuelve el nivel de utilización de los recursos
source_url: https://www.php.net/manual/es/function.getrusage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/getrusage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: a277389c9
order: 39020
---

getrusage

Devuelve el nivel de utilización de los recursos

## Descripción

```php
getrusage([int $mode]): array
```php

Es una interfaz a la función del sistema `getrusage(2)`. Devuelve un array asociativo que contiene las informaciones devueltas por esta llamada al sistema.

## Parámetros

`mode`  
Si `mode` es igual a 1, `getrusage` será llamado con el argumento `RUSAGE_CHILDREN`.

## Valores devueltos

Devuelve un array asociativo que contiene los datos devueltos desde la llamada al sistema. Todas las entradas son accesibles utilizando sus nombres de campos documentados. Devuelve `false` en caso de error.

## Ejemplos

Ejemplo con `getrusage`

```
<?php
$dat = getrusage();
echo $dat["ru_oublock"];       // número de operaciones de bloque de salida
echo $dat["ru_inblock"];       // número de operaciones de bloque de entrada
echo $dat["ru_msgsnd"];        // número de mensajes IPC enviados
echo $dat["ru_msgrcv"];        // número de mensajes IPC recibidos
echo $dat["ru_maxrss"];        // tamaño máximo del grupo de residentes
echo $dat["ru_ixrss"];         // tamaño de la memoria compartida integral
echo $dat["ru_idrss"];         // tamaño integral de los datos no compartidos
echo $dat["ru_minflt"];        // número de páginas recuperadas (falta de página menor)
echo $dat["ru_majflt"];        // número de faltas de página (falta de página mayor)
echo $dat["ru_nsignals"];      // número de señales recibidas
echo $dat["ru_nvcsw"];         // número de cambios de contexto voluntarios
echo $dat["ru_nivcsw"];        // número de cambios de contexto involuntarios
echo $dat["ru_nswap"];         // tamaño de la memoria swap
echo $dat["ru_utime.tv_usec"]; // tiempo de usuario utilizado (en microsegundos)
echo $dat["ru_utime.tv_sec"];  // tiempo de usuario utilizado (en segundos)
echo $dat["ru_stime.tv_usec"]; // tiempo de sistema utilizado (en microsegundos)
echo $dat["ru_stime.tv_sec"]; // tiempo de sistema utilizado (en segundos)
?>

    
```php

## Notas

> [!NOTE]
> Bajo Windows, la función `getrusage` solo va a devolver los siguientes miembros:
>
> `"ru_stime.tv_sec"`, `"ru_stime.tv_usec"`, `"ru_utime.tv_sec"`, `"ru_utime.tv_usec"`, `"ru_majflt"` (solo si `mode` vale `RUSAGE_SELF`), `"ru_maxrss"` (solo si `mode` vale `RUSAGE_SELF`)
>
> Si `getrusage` es llamado con el argumento `mode` valiendo `1` (`RUSAGE_CHILDREN`), entonces la utilización de los recursos para los hilos son recolectados (lo que significa que, internamente, la función es llamada con `RUSAGE_THREAD`).

> [!NOTE]
> Bajo BeOS 2000, solo los siguientes miembros son devueltos:
>
> `"ru_stime.tv_sec"`, `"ru_stime.tv_usec"`, `"ru_utime.tv_sec"`, `"ru_utime.tv_usec"`

## Véase también

La página del manual `getrusage(2)` de su sistema
