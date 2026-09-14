---
title: Imagick::despeckleImage
description: Reduce el ruido speckle de una imagen
source_url: https://www.php.net/manual/es/imagick.despeckleimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/despeckleimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 65c4446ab
order: 33100
---

Imagick::despeckleImage

Reduce el ruido speckle de una imagen

## Descripción

```php
public Imagick::despeckleImage(): bool
```php

Reduce el ruido speckle de una imagen, preservando los bordes de la imagen original.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Ejemplo con `Imagick::despeckleImage`

```
<?php
function despeckleImage($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->despeckleImage();
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

     
```php
