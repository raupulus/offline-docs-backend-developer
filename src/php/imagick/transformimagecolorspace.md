---
title: Imagick::transformImageColorspace
description: Transforma una imagen en un nuevo espacio de color
source_url: https://www.php.net/manual/es/imagick.transformimagecolorspace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/transformimagecolorspace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 65c4446ab
order: 35980
---

Imagick::transformImageColorspace

Transforma una imagen en un nuevo espacio de color

## Descripción

```php
public Imagick::transformImageColorspace(int $colorspace): bool
```php

Transforma una imagen en un nuevo espacio de color.

## Parámetros

`colorspace`  
El espacio de color al que debe transformarse la imagen, una de las [constantes COLORSPACE](#imagick.constants.colorspace), por ejemplo Imagick::COLORSPACE_CMYK.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Imagick::transformImageColorspace ejemplo

Transforma una imagen en un nuevo espacio de color, luego extrae un solo canal para que los valores individuales de canal puedan visualizarse.

```
<?php
function transformImageColorspace($imagePath, $colorSpace, $channel) {
    $imagick = new \Imagick(realpath($imagePath));
    $imagick->transformimagecolorspace($colorSpace);
    //channel debe ser una de las constantes de canal, por ejemplo \Imagick::CHANNEL_BLUE
    $imagick->separateImageChannel($channel);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}
?>

   
```php

## Véase también

Imagick::setColorSpace
