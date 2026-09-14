---
title: fflush
description: Envía todo el contenido generado en un fichero
source_url: https://www.php.net/manual/es/function.fflush.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/fflush.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 23410
---

fflush

Envía todo el contenido generado en un fichero

## Descripción

```php
fflush(resource $stream): bool
```php

Fuerza la escritura de todos los datos bufferizados en el fichero designado por `stream`.

## Parámetros

`stream`  
El puntero de fichero debe ser válido y apuntar a un archivo abierto con éxito por `fopen` o `fsockopen` (y no cerrado aún por `fclose`).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Escritura de un fichero utilizando `fflush`

```
<?php
$filename = 'bar.txt';

$file = fopen($filename, 'r+');
rewind($file);
fwrite($file, 'Foo');
fflush($file);
ftruncate($file, ftell($file));
fclose($file);
?>

    
```php

## Véase también

`clearstatcache`, `fwrite`
