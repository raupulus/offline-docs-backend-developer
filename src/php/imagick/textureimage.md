---
title: Imagick::textureImage
description: Repite los mosaicos de la textura de una imagen
source_url: https://www.php.net/manual/es/imagick.textureimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/textureimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 0ffb9c9fc
order: 35920
---

Imagick::textureImage

Repite los mosaicos de la textura de una imagen

## Descripción

```php
Imagick::textureImage(Imagick $texture_wand): Imagick
```php

Repite los mosaicos de la textura de una imagen mediante el lienzo de la imagen.

## Parámetros

`texture_wand`  
Objeto Imagick a utilizar como imagen de textura

## Valores devueltos

Devuelve un nuevo objeto Imagick, al que se le ha aplicado la textura repetida.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Ejemplo con `Imagick::textureImage`

```
      
<?php
function textureImage($imagePath) {
    $image = new \Imagick();
    $image->newImage(640, 480, new \ImagickPixel('pink'));
    $image->setImageFormat("jpg");
    $texture = new \Imagick(realpath($imagePath));
    $texture->scaleimage($image->getimagewidth() / 4, $image->getimageheight() / 4);
    $image = $image->textureImage($texture);
    header("Content-Type: image/jpg");
    echo $image;
}

?>

      
```php
