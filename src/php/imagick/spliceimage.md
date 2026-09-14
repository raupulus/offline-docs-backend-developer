---
title: Imagick::spliceImage
description: Une un color sólido en la imagen
source_url: https://www.php.net/manual/es/imagick.spliceimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/spliceimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35840
---

Imagick::spliceImage

Une un color sólido en la imagen

## Descripción

```php
public Imagick::spliceImage(int $width, int $height, int $x, int $y): bool
```php

Une un color sólido en la imagen.

## Parámetros

`width`  

`height`  

`x`  

`y`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::spliceImage`

```
      
<?php
function spliceImage($imagePath, $startX, $startY, $width, $height) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->spliceImage($width, $height, $startX, $startY);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

      
```php
