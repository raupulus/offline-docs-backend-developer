---
title: Imagick::whiteThresholdImage
description: Fuerza a todos los píxeles por encima del umbral a ser blancos
source_url: https://www.php.net/manual/es/imagick.whitethresholdimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/whitethresholdimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 36080
---

Imagick::whiteThresholdImage

Fuerza a todos los píxeles por encima del umbral a ser blancos

## Descripción

```php
public Imagick::whiteThresholdImage(mixed $threshold): bool
```php

Es como Imagick::ThresholdImage() excepto que fuerza a todos los píxeles por encima del umbral a ser blancos dejando todos los píxeles por debajo del umbral sin cambios.

## Parámetros

`threshold`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL imagick 2.1.0 | Ahora se permite que una cadena represente el color como parámetro. Versiones previas sólo permitían un objeto ImagickPixel. |

## Ejemplos

`Imagick::whiteThresholdImage`

```
      
<?php
function whiteThresholdImage($imagePath, $color) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->whiteThresholdImage($color);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
