---
title: Imagick::borderImage
description: Rodea la imagen con un borde
source_url: https://www.php.net/manual/es/imagick.borderimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/borderimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 0ffb9c9fc
order: 32750
---

Imagick::borderImage

Rodea la imagen con un borde

## Descripción

```php
public Imagick::borderImage(mixed $bordercolor, int $width, int $height): bool
```php

Rodea la imagen con un borde del color definido por el objeto ImagickPixel de color de borde.

## Parámetros

`bordercolor`  
Objeto ImagickPixel o una cadena que contiene el color del borde

`width`  
Ancho del borde

`height`  
Alto del borde

## Valores devueltos

Devuelve `true` en caso de éxito.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL imagick 2.1.0 | Ahora se permite que una cadena represente el color como el primer parámetro. Versiones anteriores sólo permitían un objeto ImagickPixel. |

## Ejemplos

`Imagick::borderImage`

```
      
<?php
function borderImage($imagePath, $color, $width, $height) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->borderImage($color, $width, $height);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
