---
title: Imagick::linearStretchImage
description: Estrecha con saturación la intensidad de la imagen
source_url: https://www.php.net/manual/es/imagick.linearstretchimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/linearstretchimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34400
---

Imagick::linearStretchImage

Estrecha con saturación la intensidad de la imagen

## Descripción

```php
public Imagick::linearStretchImage(float $blackPoint, float $whitePoint): bool
```php

Estrecha con saturación la intensidad de la imagen.

## Parámetros

`blackPoint`  
El punto negro de la imagen

`whitePoint`  
El punto blanco de la imagen

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::linearStretchImage`

```
      
<?php
function linearStretchImage($imagePath, $blackThreshold, $whiteThreshold) {
    $imagick = new \Imagick(realpath($imagePath));
    $pixels = $imagick->getImageWidth() * $imagick->getImageHeight();
    $imagick->linearStretchImage($blackThreshold * $pixels, $whiteThreshold * $pixels);

    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
