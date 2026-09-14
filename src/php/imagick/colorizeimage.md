---
title: Imagick::colorizeImage
description: Mezcla el color de relleno con la imagen
source_url: https://www.php.net/manual/es/imagick.colorizeimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/colorizeimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 32880
---

Imagick::colorizeImage

Mezcla el color de relleno con la imagen

## Descripción

```php
public Imagick::colorizeImage(mixed $colorize, mixed $opacity, [bool $legacy]): bool
```php

Mezcla el color de relleno de cada píxel con la imagen.

## Parámetros

`colorize`  
Objeto ImagickPixel o una cadena que contiene el color

`opacity`  
Objeto ImagickPixel o un valor float que contiene el valor de la opacidad. 1.0 es completamente opaco y 0.0 es completamente transparente.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL imagick 2.1.0 | Ahora se permite que una cadena represente el color como el primer parámetro y que un valor float represente el valor de la opacidad como el segundo parámetro. Versiones anteriores sólo permitían objetos ImagickPixel. |

## Ejemplos

`Imagick::colorizeImage`

```
      
<?php
function colorizeImage($imagePath, $color, $opacity) {
    $imagick = new \Imagick(realpath($imagePath));
    $opacity = $opacity / 255.0;
    $opacityColor = new \ImagickPixel("rgba(0, 0, 0, $opacity)");
    $imagick->colorizeImage($color, $opacityColor);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
