---
title: Imagick::blackThresholdImage
description: Fuerza a todos los píxeles bajo un umbral a ser negros
source_url: https://www.php.net/manual/es/imagick.blackthresholdimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/blackthresholdimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 0ffb9c9fc
order: 32720
---

Imagick::blackThresholdImage

Fuerza a todos los píxeles bajo un umbral a ser negros

## Descripción

```php
public Imagick::blackThresholdImage(mixed $threshold): bool
```php

Es como Imagick::thresholdImage() pero fuerza a todos los píxeles bajo un umbral a ser negros mientras deja todos los píxeles por encima del umbral sin cambios.

## Parámetros

`threshold`  
El umbral por debajo del cual todo se vuelve de color negro

## Valores devueltos

Devuelve `true` en caso de éxito.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL imagick 2.1.0 | Ahora se permite que una cadena represente el color como un parámetro. Versiones anteriores sólo permitían un objeto ImagickPixel. |

## Ejemplos

`Imagick::blackThresholdImage`

```
      
<?php
function blackThresholdImage($imagePath, $thresholdColor) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->blackthresholdimage($thresholdColor);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
