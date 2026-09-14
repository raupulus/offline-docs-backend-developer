---
title: posix_mknod
description: Crear un fichero especial u ordinario (POSIX.1)
source_url: https://www.php.net/manual/es/function.posix-mknod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-mknod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: 265acc36e
order: 65370
---

posix_mknod

Crear un fichero especial u ordinario (POSIX.1)

## Descripción

```php
posix_mknod(string $filename, int $flags, [int $major], [int $minor]): bool
```php

Crea un fichero especial u ordinario.

## Parámetros

`filename`  
El fichero a crear

`flags`  
Este parámetro se construye mediante un operador a nivel de bits OR entre el tipo de fichero (una de las siguientes constantes: `POSIX_S_IFREG`, `POSIX_S_IFCHR`, `POSIX_S_IFBLK`, `POSIX_S_IFIFO` o `POSIX_S_IFSOCK`) y los permisos.

`major`  
El identificador de kernel mayor del dispositivo (necesario pasarlo al usar `S_IFCHR` o `S_IFBLK`).

`minor`  
El identificador de kernel menor del dispositivo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Un ejemplo de `posix_mknod`

```
<?php

$fichero = '/tmp/fich_tmp';  // nombre del fichero
$tipo = POSIX_S_IFBLK;   // tipo de fichero
$permisos = 0777;     // octal
$mayor = 1;
$menor = 8;              // /dev/random

if (!posix_mknod($fichero, $tipo | $permisos, $mayor, $menor)) {
    die('Error ' . posix_get_last_error() . ': ' . posix_strerror(posix_get_last_error()));
}

?>

    
```php

## Véase también

`posix_mkfifo`
