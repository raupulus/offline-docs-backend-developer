---
title: Imagick::setSamplingFactors
description: Establece los factores de muestreo de la imagen
source_url: https://www.php.net/manual/es/imagick.setsamplingfactors.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setsamplingfactors.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 35700
---

Imagick::setSamplingFactors

Establece los factores de muestreo de la imagen

## Descripción

```php
public Imagick::setSamplingFactors(array $factors): bool
```php

Establece los factores de muestreo de la imagen.

## Parámetros

`factors`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`Imagick::setSamplingFactors`

```
      
<?php
function setSamplingFactors($imagePath) {

    $imagePath = "../imagick/images/FineDetail.png";
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->setImageFormat('jpg');
    $imagick->setSamplingFactors(array('2x2', '1x1', '1x1'));

    $compressed = $imagick->getImageBlob();

    $reopen = new \Imagick();
    $reopen->readImageBlob($compressed);

    $reopen->resizeImage(
        $reopen->getImageWidth() * 4,
        $reopen->getImageHeight() * 4,
        \Imagick::FILTER_POINT,
        1
    );

    header("Content-Type: image/jpg");
    echo $reopen->getImageBlob();
}

?>

      
```php
