---
title: jpeg2wbmp
description: Convierte una imagen JPEG en imagen WBMP
source_url: https://www.php.net/manual/es/function.jpeg2wbmp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/jpeg2wbmp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 4e32d05f7
order: 32520
---

jpeg2wbmp

Convierte una imagen JPEG en imagen WBMP

> [!WARNING]
> Esta funcionalidad está *OBSOLETA* a partir de PHP 7.2.0 y ha sido *ELIMINADA* a partir de PHP 8.0.0.

## Descripción

```php
jpeg2wbmp(string $jpegname, string $wbmpname, int $dest_height, int $dest_width, int $threshold): bool
```php

Convierte una imagen JPEG en imagen WBMP.

## Parámetros

`jpegname`  
Ruta hacia el fichero JPEG.

`wbmpname`  
Ruta hacia el fichero final WBMP.

`dest_height`  
Altura de la imagen de destino.

`dest_width`  
Ancho de la imagen de destino.

`threshold`  
Valor del umbral, entre 0 y 8 inclusive.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

> [!CAUTION]
> Sin embargo, si libgd no logra producir la imagen, esta función devuelve `true`.

## Ejemplos

Ejemplo con `jpeg2wbmp`

```
<?php
// Ruta hacia el objetivo jpeg
$path = './test.jpg';

// Obtención del tamaño de la imagen
$image = getimagesize($path);

// Conversión de la imagen
jpeg2wbmp($path, './test.wbmp', $image[1], $image[0], 5);
?>

    
```php

## Véase también

png2wbmp
