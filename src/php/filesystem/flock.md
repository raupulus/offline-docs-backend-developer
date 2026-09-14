---
title: flock
description: Bloqueo de ficheros portátil y consultivo
source_url: https://www.php.net/manual/es/function.flock.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/flock.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 75a76afb6
order: 23590
---

flock

Bloqueo de ficheros portátil y consultivo

## Descripción

```php
flock(resource $stream, int $operation, [int $would_block]): bool
```php

`flock` permite realizar un modelo simple de lectura/escritura que puede usarse en casi cualquier plataforma (incluyendo la mayoría de derivados de Unix e incluso Windows).

El bloqueo también se libera mediante `fclose`, o cuando el `stream` es recolectado por el recolector de basura.

PHP soporta una forma portátil de bloquear ficheros completos de manera consultiva (lo que significa que todos los programas que acceden deben usar el mismo método de bloqueo o no funcionará). Por omisión, esta función bloqueará hasta que se adquiera el bloqueo solicitado; esto puede controlarse con la opción `LOCK_NB` documentada más abajo.

## Parámetros

`stream`  
Un puntero al sistema de ficheros de tipo `resource` que típicamente se crea utilizando `fopen`.

`operation`  
`operation` es uno de los siguientes:

- `LOCK_SH` para adquirir un bloqueo compartido (lector).

- `LOCK_EX` para adquirir un bloqueo exclusivo (escritor).

- `LOCK_UN` para liberar un bloqueo (compartido o exclusivo).

También es posible añadir `LOCK_NB` como máscara de bits a una de las operaciones anteriores, si `flock` no debe bloquear durante el intento de bloqueo.

`would_block`  
El tercer argumento opcional se establece a 1 si el bloqueo bloquearía (condición de error EWOULDBLOCK).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `flock`

```
<?php

$fp = fopen("/tmp/lock.txt", "r+");

if (flock($fp, LOCK_EX)) {  // adquirir un bloqueo exclusivo
    ftruncate($fp, 0);      // truncar el fichero
    rewind($fp);
    fwrite($fp, "Escribir algo aquí\n");
    fflush($fp);            // volcar la salida antes de liberar el bloqueo
    flock($fp, LOCK_UN);    // liberar el bloqueo
} else {
    echo "¡No se pudo obtener el bloqueo!";
}

fclose($fp);

?>

    
```php

`flock` usando la opción `LOCK_NB`

```
<?php
$fp = fopen('/tmp/lock.txt', 'r+');

/* Activar la opción LOCK_NB en una operación LOCK_EX */
if(!flock($fp, LOCK_EX | LOCK_NB)) {
    echo 'No se pudo obtener el bloqueo';
    exit(-1);
}

/* ... */

fclose($fp);
?>

    
```php

## Notas

> [!NOTE]
> `flock` usa bloqueo obligatorio en lugar de bloqueo consultivo en Windows. El bloqueo obligatorio también es compatible en Linux y sistemas operativos basados en System V mediante el mecanismo habitual soportado por la llamada al sistema fcntl(): es decir, si el fichero en cuestión tiene establecido el bit de permiso setgid y el bit de ejecución del grupo desactivado. En Linux, el sistema de ficheros también deberá montarse con la opción mand para que esto funcione.

> [!NOTE]
> Dado que `flock` requiere un puntero a fichero, puede que necesite usar un fichero de bloqueo especial para proteger el acceso a un fichero que intente truncar abriéndolo en modo escritura (con un argumento "w" o "w+" a `fopen`).

> [!NOTE]
> Solo puede usarse en punteros a ficheros devueltos por `fopen` para ficheros locales, o punteros a ficheros que apunten a flujos en espacio de usuario que implementen el método `streamWrapper::stream_lock`.

> [!WARNING]
> Asignar otro valor al argumento `stream` en el código posterior liberará el bloqueo.

> [!WARNING]
> En algunos sistemas operativos, `flock` se implementa a nivel de proceso. ¡Cuando se usa una API de servidor multihilo, puede que no se pueda confiar en `flock` para proteger ficheros contra otros scripts PHP que se ejecuten en paralelo en la misma instancia del servidor!
>
> `flock` no es compatible con sistemas de ficheros anticuados como `FAT` y sus derivados, y por lo tanto siempre devolverá `false` en estos entornos.

> [!NOTE]
> En Windows, si el proceso de bloqueo abre el fichero una segunda vez, no podrá acceder al fichero a través de este segundo manejador hasta que desbloquee el fichero.
