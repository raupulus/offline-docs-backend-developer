---
title: RarEntry::getHostOs
description: Obtener sistema operativo anfitrión del archivo de entrada
source_url: https://www.php.net/manual/es/rarentry.gethostos.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rarentry/gethostos.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_reviewed: false
translation_revision: ee741f54f
order: 68540
---

RarEntry::getHostOs

Obtener sistema operativo anfitrión del archivo de entrada

## Descripción

```php
public RarEntry::getHostOs(): int
```php

Devuelve el código del sistema operativo anfitrión del archivo de entrada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el código del sistema operativo anfitrión, o `false` en caso de error.

## Ejemplos

Ejemplo de RarEntry::getHostOs (version \>= 2.0.0)

```
<?php

$rar_file = rar_open('example.rar') or die("Failed to open Rar archive");

$entry = rar_entry_get($rar_file, 'Dir/file.txt') or die("Failed to find such entry");

switch ($entry->getHostOs()) {
    case RarEntry::HOST_MSDOS:
        echo "MS-DOS\n";
        break;
    case RarEntry::HOST_OS2:
        echo "OS2\n";
        break;
    case RarEntry::HOST_WIN32:
        echo "Win32\n";
        break;
    case RarEntry::HOST_MACOS:
        echo "MacOS\n";
        break;
    case RarEntry::HOST_UNIX:
        echo "Unix/Linux\n";
        break;
    case RarEntry::HOST_BEOS:
        echo "BeOS\n";
        break;
}

?>

    
```php

RarEntry::getHostOs example (version \<= 1.0.0)

```
<?php

$rar_file = rar_open('example.rar') or die("Failed to open Rar archive");

$entry = rar_entry_get($rar_file, 'Dir/file.txt') or die("Failed to find such entry");

switch ($entry->getHostOs()) {
    case RAR_HOST_MSDOS:
        echo "MS-DOS\n";
        break;
    case RAR_HOST_OS2:
        echo "OS2\n";
        break;
    case RAR_HOST_WIN32:
        echo "Win32\n";
        break;
    case RAR_HOST_MACOS:
        echo "MacOS\n";
        break;
    case RAR_HOST_UNIX:
        echo "Unix/Linux\n";
        break;
    case RAR_HOST_BEOS:
        echo "BeOS\n";
        break;
}

?>

    
```php

## Véase también

RarEntry::extract
