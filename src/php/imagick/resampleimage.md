---
title: Imagick::resampleImage
description: Remuestrea la imagen a la resolución deseada
source_url: https://www.php.net/manual/es/imagick.resampleimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/resampleimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34930
---

Imagick::resampleImage

Remuestrea la imagen a la resolución deseada

## Descripción

```php
public Imagick::resampleImage(float $x_resolution, float $y_resolution, int $filter, float $blur): bool
```php

Remuestrea la imagen a la resolución deseada.

## Parámetros

`x_resolution`  

`y_resolution`  

`filter`  

`blur`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::resampleImage`

```
      
<?php
function resampleImage($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));

    $imagick->resampleImage(200, 200, \Imagick::FILTER_LANCZOS, 1);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
