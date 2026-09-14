---
title: ftruncate
description: Tronca un fichero
source_url: https://www.php.net/manual/es/function.ftruncate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/ftruncate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 23710
---

ftruncate

Tronca un fichero

## Descripción

```php
ftruncate(resource $stream, int $size): bool
```php

Se toma el puntero de fichero `stream` y se trunca a la longitud de `size`.

## Parámetros

`stream`  
El puntero de fichero.

> [!NOTE]
> El puntero `stream` debe haber sido abierto en modo escritura.

`size`  
La longitud que debe conservarse.

> [!NOTE]
> Si `size` es mayor que la longitud del fichero, este último será extendido con octetos nulos.
>
> Si `size` es menor que la longitud del fichero, el resto de los datos se perderá.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `ftruncate`

```
<?php
$filename = 'lorem_ipsum.txt';

$handle = fopen($filename, 'r+');
ftruncate($handle, rand(1, filesize($filename)));
rewind($handle);
echo fread($handle, filesize($filename));
fclose($handle);
?>

    
```php

## Notas

> [!NOTE]
> El puntero de fichero no es *modificado*.

## Véase también

`fopen`, `fseek`
