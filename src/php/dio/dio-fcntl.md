---
title: dio_fcntl
description: Lleva a cabo la función fcntl de la biblioteca C en el fichero fd
source_url: https://www.php.net/manual/es/function.dio-fcntl.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dio/functions/dio-fcntl.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dio
translation_status: ready
translation_revision: ee1ce6a0e
order: 11860
---

dio_fcntl

Lleva a cabo la función fcntl de la biblioteca C en el fichero fd

## Descripción

```php
dio_fcntl(resource $fd, int $cmd, [mixed $args]): mixed
```php

La función `dio_fcntl` realiza la operación especificada por `cmd` sobre el descriptor de fichero `fd`. Algunos comandos requieren que se proporcionen parámetros adicionales en `args`.

## Parámetros

`fd`  
Descriptor de fichero devuelto por `dio_open`.

`cmd`  
Puede ser una de las siguientes operaciones:

- `F_SETLK` - Se asigna o quita el bloqueo. Si está bloqueado por otro proceso, `dio_fcntl` devuelve -1.

- `F_SETLKW` - como `F_SETLK`, pero en caso de que esté bloqueado por otro proceso, `dio_fcntl` espera a que éste se libere.

- `F_GETLK` - `dio_fcntl` devuelve un array asociativo (como se describe a continuación) si algún proceso previene el bloqueo. Si no hubiera impedimento, se asignará la clave "type" a `F_UNLCK`.

- `F_DUPFD` - encuentra el número de descriptor más bajo disponible que sea igual o superior a `args` y lo devuelve.

- `F_SETFL` - Establece al descriptor de fichero las banderas especificadas en `args`, de entre `O_APPEND`, `O_NONBLOCK` o `O_ASYNC`. Para usar `O_ASYNC` debe usarse la extensión [PCNTL](#ref.pcntl).

`args`  
`args` es un array asociativo, cuando `cmd` sea `F_SETLK` o `F_SETLKW`, con las siguientes claves:

- `start` - posición donde comienza el bloqueo

- `length` - tamaño del area bloqueada. Cero significa hasta el final del fichero

- `whence` - Desde dónde se contabiliza l_start: puede ser `SEEK_SET`, `SEEK_END` y `SEEK_CUR`

- `type` - tipo de bloqueo: puede ser `F_RDLCK` (bloqueo de lectura), `F_WRLCK` (bloqueo de escritura) o `F_UNLCK` (desbloqueo)

## Valores devueltos

Devuelve el resultado de la llamada a C.

## Ejemplos

Bloqueando y desbloqueando

```
<?php

$fd = dio_open('/dev/ttyS0', O_RDWR);

if (dio_fcntl($fd, F_SETLK, Array("type"=>F_WRLCK)) == -1) {
   // parece el descriptor de fichero está bloqueado
   echo "No se puede desbloquear. Pertenece a algún otro proceso.";
} else {
   echo "Bloqueo/desbloqueo con éxito";
}

dio_close($fd);
?>

    
```php

## Notas

> [!NOTE]
> Esta función no está implementada en las plataformas Windows.
