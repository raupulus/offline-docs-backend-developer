---
title: Imagick::colorMatrixImage
description: Aplica una transformación de color a una imagen
source_url: https://www.php.net/manual/es/imagick.colormatriximage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/colormatriximage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: cf2b27998
order: 32890
---

Imagick::colorMatrixImage

Aplica una transformación de color a una imagen

## Descripción

```php
public Imagick::colorMatrixImage(array $color_matrix): bool
```php

Aplica una transformación de color a una imagen. El método permite cambios de saturación, rotación de tono, luminancia en alfa y diversos otros efectos. Aunque se pueden utilizar matrices de transformación de tamaño variable, generalmente se usa una matriz 5x5 para una imagen RGBA y una 6x6 para CMYKA (o RGBA con desplazamientos). La matriz es similar a las utilizadas por Adobe Flash, excepto que los desplazamientos están en la columna 6 en lugar de la 5 (para soportar imágenes CMYKA) y los desplazamientos están normalizados (divida el desplazamiento Flash por 255).

## Parámetros

`color_matrix`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::colorMatrixImage`

```
      
<?php
function colorMatrixImage($imagePath, $colorMatrix) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->setImageOpacity(1);

    //Una matriz de color debería ser similar a:
    //    $colorMatrix = [
    //        1.5, 0.0, 0.0, 0.0, 0.0, -0.157,
    //        0.0, 1.0, 0.5, 0.0, 0.0, -0.157,
    //        0.0, 0.0, 1.5, 0.0, 0.0, -0.157,
    //        0.0, 0.0, 0.0, 1.0, 0.0,  0.0,
    //        0.0, 0.0, 0.0, 0.0, 1.0,  0.0,
    //        0.0, 0.0, 0.0, 0.0, 0.0,  1.0
    //    ];

    $background = new \Imagick();
    $background->newPseudoImage($imagick->getImageWidth(), $imagick->getImageHeight(),  "pattern:checkerboard");

    $background->setImageFormat('png');

    $imagick->setImageFormat('png');
    $imagick->colorMatrixImage($colorMatrix);

    $background->compositeImage($imagick, \Imagick::COMPOSITE_ATOP, 0, 0);

    header("Content-Type: image/png");
    echo $background->getImageBlob();
}

?>

      
```php
