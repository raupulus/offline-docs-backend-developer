---
title: Imagick::shadowImage
description: Simula una sombra de imagen
source_url: https://www.php.net/manual/es/imagick.shadowimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/shadowimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35750
---

Imagick::shadowImage

Simula una sombra de imagen

## Descripción

```php
public Imagick::shadowImage(float $opacity, float $sigma, int $x, int $y): bool
```php

Simula una sombra de imagen.

## Parámetros

`opacity`  

`sigma`  

`x`  

`y`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::shadowImage`

```
<?php
function shadowImage($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->shadowImage(0.4, 10, 50, 5);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

     
```php
