---
title: fsync
description: Sincroniza los cambios realizados en el fichero (incluyendo los metadatos)
source_url: https://www.php.net/manual/es/function.fsync.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/fsync.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_revision: 21129de17
order: 23690
---

fsync

Sincroniza los cambios realizados en el fichero (incluyendo los metadatos)

## Descripción

```php
fsync(resource $stream): bool
```php

Esta función sincroniza los cambios realizados en el fichero, incluyendo sus metadatos. Es similar a `fflush`, pero además solicita al sistema operativo que escriba en el soporte de almacenamiento.

## Parámetros

`stream`  
El puntero de fichero debe ser válido y apuntar a un archivo abierto con éxito por `fopen` o `fsockopen` (y no cerrado aún por `fclose`).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `fsync`

```
<?php
$file = 'test.txt';
$stream = fopen($file, 'w');
fwrite($stream, 'test data');
fwrite($stream, "\r\n");
fwrite($stream, 'additional data');
fsync($stream);
fclose($stream);
?>

    
```php

## Véase también

`fdatasync`, `fflush`
