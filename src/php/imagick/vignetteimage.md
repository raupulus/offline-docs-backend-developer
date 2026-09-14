---
title: Imagick::vignetteImage
description: Añade un filtro de viñeta a la imagen
source_url: https://www.php.net/manual/es/imagick.vignetteimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/vignetteimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 65c4446ab
order: 36060
---

Imagick::vignetteImage

Añade un filtro de viñeta a la imagen

## Descripción

```php
public Imagick::vignetteImage(float $blackPoint, float $whitePoint, int $x, int $y): bool
```php

Suaviza los contornos de la imagen, al estilo de las viñetas. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

## Parámetros

`blackPoint`  
El radio del desenfoque

`whitePoint`  
La desviación estándar

`x`  
La abscisa de la elipse.

`y`  
La ordenada de la elipse.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo con `Imagick::vignetteImage`

```
      
<?php
function vignetteImage($imagePath, $blackPoint, $whitePoint, $x, $y) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->vignetteImage($blackPoint, $whitePoint, $x, $y);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php

## Véase también

`Imagick::waveImage`, `Imagick::swirlImage`
