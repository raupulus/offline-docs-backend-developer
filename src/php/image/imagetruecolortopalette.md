---
title: imagetruecolortopalette
description: Convierte una imagen en colores verdaderos a imagen con paleta
source_url: https://www.php.net/manual/es/function.imagetruecolortopalette.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagetruecolortopalette.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 32430
---

imagetruecolortopalette

Convierte una imagen en colores verdaderos a imagen con paleta

## Descripción

```php
imagetruecolortopalette(GdImage $image, bool $dither, int $num_colors): bool
```php

`imagetruecolortopalette` convierte la imagen en colores verdaderos `image` a imagen con paleta. El código de esta función es directamente tomado de la biblioteca del `Independent JPEG Group`, que es simplemente genial. El código ha sido modificado para preservar la mayor parte del canal alfa en la nueva paleta, además de conservar las colores lo mejor posible. Pero esto no siempre funciona como se desea. En ese caso, es preferible generar un resultado en colores verdaderos, lo que siempre proporciona el mejor rendimiento.

## Parámetros

`image`  
Un objeto `GdImage`, retornado por una de las funciones de creación de imágenes, como `imagecreatetruecolor`.

`dither`  
Indica si la imagen debe ser granulada - si se define como `true`, entonces la imagen será un poco más granulada pero la aproximación de los colores será mejor.

`num_colors`  
El número máximo de colores en la paleta final.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `image` ahora espera una instancia de `GdImage` ; anteriormente, se esperaba un recurso `gd` de tipo `resource` válido. |

## Ejemplos

Conversión de una imagen truecolor a una paleta

```
<?php
// Creación de una imagen truecolor
$im = imagecreatetruecolor(100, 100);

// Conversión a paleta de 255 colores
imagetruecolortopalette($im, false, 255);

// Guardado de la imagen
imagepng($im, './paletteimage.png');
?>

    
```php
