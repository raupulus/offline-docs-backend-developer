---
title: Imagick::posterizeImage
description: Reduce la imagen a un número limitado de niveles de color
source_url: https://www.php.net/manual/es/imagick.posterizeimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/posterizeimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34710
---

Imagick::posterizeImage

Reduce la imagen a un número limitado de niveles de color

## Descripción

```php
public Imagick::posterizeImage(int $levels, bool $dither): bool
```php

Reduce la imagen a un número limitado de niveles de color.

## Parámetros

`levels`  

`dither`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::posterizeImage`

```
      
<?php
function posterizeImage($imagePath, $posterizeType, $numberLevels) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->posterizeImage($numberLevels, $posterizeType);
    $imagick->setImageFormat('png');
    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

posterizeImage($imagePath, \Imagick::DITHERMETHOD_RIEMERSMA, 8);

?>

      
```php
