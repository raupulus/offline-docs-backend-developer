---
title: Imagick::shearImage
description: Crea un paralelogramo
source_url: https://www.php.net/manual/es/imagick.shearimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/shearimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35780
---

Imagick::shearImage

Crea un paralelogramo

## Descripción

```php
public Imagick::shearImage(mixed $background, float $x_shear, float $y_shear): bool
```php

Desliza un extremo de una imagen a lo largo del eje X o Y, creando un paralelogramo. Un recorte en la dirección X desliza un extremo a lo largo del eje X, mientras que un recorte en la dirección Y desliza un extremo a lo largo del eje Y. La cantidad del recorte se controla por un ángulo de recorte. Para recortes en la dirección X, x_shear se mide relativo al eje Y, y de forma similar, para recortes en la dirección Y, y_shear se mide relativo al eje X. Los triángulos vacíos sobrantes del recorte de la imagen se rellenan con el color de fondo.

## Parámetros

`background`  
El color de fondo

`x_shear`  
El número de grados a recortar sobre el eje x

`y_shear`  
El número de grados a recortar sobre el eje y

## Valores devueltos

Devuelve `true` en caso de éxito.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL imagick 2.1.0 | Ahora se permite que un string represente el color como primer parámetro. Versiones previas sólo permitían un objeto ImagickPixel. |

## Ejemplos

`Imagick::shearImage`

```
      
<?php
function shearImage($imagePath, $color, $shearX, $shearY) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->shearimage($color, $shearX, $shearY);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
