---
title: Imagick::uniqueImageColors
description: Se conserva únicamente un color de píxel
source_url: https://www.php.net/manual/es/imagick.uniqueimagecolors.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/uniqueimagecolors.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 65c4446ab
order: 36030
---

Imagick::uniqueImageColors

Se conserva únicamente un color de píxel

## Descripción

```php
public Imagick::uniqueImageColors(): bool
```php

Se conserva únicamente un color de píxel y se eliminan los demás. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo con `Imagick::uniqueImageColors`

```
<?php
function uniqueImageColors($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    //Reduce la imagen a 256 colores de forma agradable.
    $imagick->quantizeImage(256, \Imagick::COLORSPACE_YIQ, 0, false, false);
    $imagick->uniqueImageColors();
    $imagick->scaleimage($imagick->getImageWidth(), $imagick->getImageHeight() * 20);
    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

     
```php
