---
title: Imagick::frameImage
description: Añade un borde tridimensional simulado
source_url: https://www.php.net/manual/es/imagick.frameimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/frameimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 33300
---

Imagick::frameImage

Añade un borde tridimensional simulado

## Descripción

```php
public Imagick::frameImage(mixed $matte_color, int $width, int $height, int $inner_bevel, int $outer_bevel): bool
```php

Añade un borde tridimensional simulado alrededor de la imagen. El ancho y alto especifican el ancho del borde de las caras verticales y horizontales del marco. Los biseles interior y exterior indican el ancho de las sombras interiores y exteriores del marco.

## Parámetros

`matte_color`  
Objeto ImagickPixel o una cadena que representa el color mate

`width`  
El ancho del borde

`height`  
El alto del borde

`inner_bevel`  
El ancho del bisel interior

`outer_bevel`  
El ancho del bisel exterior

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL imagick 2.1.0 | Ahora se permite que una cadena represente el color como el primer parámetro. Versiones anteriores sólo permitían un objeto ImagickPixel. |

## Ejemplos

`Imagick::frameImage`

```
      
<?php
function frameImage($imagePath, $color, $width, $height, $innerBevel, $outerBevel) {
    $imagick = new \Imagick(realpath($imagePath));

    $width = $width + $innerBevel + $outerBevel;
    $height = $height + $innerBevel + $outerBevel;

    $imagick->frameimage(
        $color,
        $width,
        $height,
        $innerBevel,
        $outerBevel
    );
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
