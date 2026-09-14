---
title: Imagick::transparentPaintImage
description: Pinta píxeles transparentes
source_url: https://www.php.net/manual/es/imagick.transparentpaintimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/transparentpaintimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35990
---

Imagick::transparentPaintImage

Pinta píxeles transparentes

## Descripción

```php
public Imagick::transparentPaintImage(mixed $target, float $alpha, float $fuzz, bool $invert): bool
```php

Pinta píxeles transparente que coincidan con el color objetivo. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.8 o superior.

## Parámetros

`target`  
El color objetivo a pintar

`alpha`  
El grado de transparencia: 1.0 corresponde a totalmente opaco y 0.0 a totalmente transparente.

`fuzz`  
La cantidad de polvo de papel. Por ejemplo, definir el polvo de papel a 10 y el color rojo a una intensidad de 100 y 102 no será interpretado como el mismo color.

`invert`  
Si es `true` pinta cualquier píxel que no coincida con el color objetivo.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::transparentPaintImage`

```
      
<?php
function transparentPaintImage($color, $alpha, $fuzz) {
    $imagick = new \Imagick(realpath("images/BlueScreen.jpg"));

    //Need to be in a format that supports transparency
    $imagick->setimageformat('png');

    $imagick->transparentPaintImage(
        $color, $alpha, $fuzz * \Imagick::getQuantum(), false
    );

    //Not required, but helps tidy up left over pixels
    $imagick->despeckleimage();

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

      
```php
