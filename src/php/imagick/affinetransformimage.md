---
title: Imagick::affineTransformImage
description: Transforma una imagen
source_url: https://www.php.net/manual/es/imagick.affinetransformimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/affinetransformimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 0ffb9c9fc
order: 32660
---

Imagick::affineTransformImage

Transforma una imagen

## Descripción

```php
public Imagick::affineTransformImage(ImagickDraw $matrix): bool
```php

Transforma una imagen como está establecido en la matriz afín.

## Parámetros

`matrix`  
La matriz afín

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::affineTransformImage`

```
<?php
function affineTransformImage($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $draw = new \ImagickDraw();

    $angle = deg2rad(40);

    $affineRotate = array(
        "sx" => cos($angle), "sy" => cos($angle),
        "rx" => sin($angle), "ry" => -sin($angle),
        "tx" => 0, "ty" => 0,
    );

    $draw->affine($affineRotate);

    $imagick->affineTransformImage($draw);

    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

    
```php
