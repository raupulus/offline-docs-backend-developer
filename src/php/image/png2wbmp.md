---
title: png2wbmp
description: Convierte una imagen PNG en imagen WBMP
source_url: https://www.php.net/manual/es/function.png2wbmp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/png2wbmp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 4e32d05f7
order: 32530
---

png2wbmp

Convierte una imagen PNG en imagen WBMP

> [!WARNING]
> Esta funcionalidad está *OBSOLETA* a partir de PHP 7.2.0 y ha sido *ELIMINADA* a partir de PHP 8.0.0.

## Descripción

```php
png2wbmp(string $pngname, string $wbmpname, int $dest_height, int $dest_width, int $threshold): bool
```php

Convierte una imagen PNG en imagen WBMP.

## Parámetros

`pngname`  
Ruta al fichero PNG.

`wbmpname`  
Ruta al fichero final WBMP.

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

Ejemplo con `png2wbmp`

```
<?php
// Ruta a la imagen PNG
$path = './test.png';

// Obtención del tamaño de la imagen
$image = getimagesize($path);

// Conversión de la imagen
png2wbmp($path, './test.wbmp', $image[1], $image[0], 7);
?>

    
```php

## Véase también

jpeg2wbmp
