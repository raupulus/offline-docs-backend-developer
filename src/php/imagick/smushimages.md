---
title: Imagick::smushImages
description: Toma todas las imágenes del puntero de imagen actual hasta el final de
  la lista de imágenes y las comprime
source_url: https://www.php.net/manual/es/imagick.smushimages.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/smushimages.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 1ef9c7a76
order: 35810
---

Imagick::smushImages

Toma todas las imágenes del puntero de imagen actual hasta el final de la lista de imágenes y las comprime

## Descripción

```php
public Imagick::smushImages(bool $stack, int $offset): Imagick
```php

Toma todas las imágenes del puntero de imagen actual hasta el final de la lista de imágenes y las comprime unas sobre otras de arriba hacia abajo si el argumento stack es verdadero, de lo contrario de izquierda a derecha.

## Parámetros

`stack`  

`offset`  

## Valores devueltos

La nueva imagen comprimida.

## Ejemplos

`Imagick::smushImages`

```
      
<?php
function smushImages($imagePath, $imagePath2) {

    $imagick = new \Imagick(realpath($imagePath));
    $imagick2 = new \Imagick(realpath($imagePath2));

    $imagick->addimage($imagick2);
    $smushed = $imagick->smushImages(false, 50);
    $smushed->setImageFormat('jpg');
    header("Content-Type: image/jpg");
    echo $smushed->getImageBlob();
}

?>

      
```php
