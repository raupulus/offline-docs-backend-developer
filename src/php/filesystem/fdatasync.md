---
title: fdatasync
description: Sincroniza los datos (pero no los metadatos) con el fichero
source_url: https://www.php.net/manual/es/function.fdatasync.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/fdatasync.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_revision: 21129de17
order: 23390
---

fdatasync

Sincroniza los datos (pero no los metadatos) con el fichero

## Descripción

```php
fdatasync(resource $stream): bool
```php

Esta función sincroniza el contenido del `stream` en el soporte de almacenamiento, al igual que `fsync`, pero no sincroniza los metadatos de los ficheros. Cabe señalar que esta función es diferente solo en sistemas POSIX. En Windows, esta función es un alias de `fsync`.

## Parámetros

`stream`  
El puntero de fichero debe ser válido y apuntar a un archivo abierto con éxito por `fopen` o `fsockopen` (y no cerrado aún por `fclose`).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `fdatasync`

```
<?php
$file = 'test.txt';
$stream = fopen($file, 'w');
fwrite($stream, 'test data');
fwrite($stream, "\r\n");
fwrite($stream, 'additional data');
fdatasync($stream);
fclose($stream);
?>

    
```php

## Véase también

`fflush`, `fsync`
