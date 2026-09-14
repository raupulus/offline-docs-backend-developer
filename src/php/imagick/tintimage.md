---
title: Imagick::tintImage
description: Aplica un vector de color a cada píxel en la imagen
source_url: https://www.php.net/manual/es/imagick.tintimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/tintimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35950
---

Imagick::tintImage

Aplica un vector de color a cada píxel en la imagen

## Descripción

```php
public Imagick::tintImage(mixed $tint, mixed $opacity, [bool $legacy]): bool
```php

Aplica un vector de color a cada píxel en la imagen. La longitud del vector es 0 para blanco y negro y su máximo para los medios-tonos. La función de precisión del vector es f(x)=(1-(4.0\*((x-0.5)\*(x-0.5)))).

## Parámetros

`tint`  

`opacity`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL imagick 2.1.0 | Ahora se permite que una string represente el color como primer parámetro y que un valor de tipo float represente la opacidad como segundo parámetro. Versiones previas sólo permitían un objeto ImagickPixel. |

## Ejemplos

`Imagick::tintImage`

```
      
<?php
function tintImage($r, $g, $b, $a) {
    $a = $a / 100;

    $imagick = new \Imagick();
    $imagick->newPseudoImage(400, 400, 'gradient:black-white');

    $tint = new \ImagickPixel("rgb($r, $g, $b)");
    $opacity = new \ImagickPixel("rgb(128, 128, 128, $a)");
    $imagick->tintImage($tint, $opacity);
    $imagick->setImageFormat('png');
    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

      
```php
