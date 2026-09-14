---
title: Imagick::deskewImage
description: Elimina la torción de la imagen
source_url: https://www.php.net/manual/es/imagick.deskewimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/deskewimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 18dc6d0d4
order: 33090
---

Imagick::deskewImage

Elimina la torción de la imagen

## Descripción

```php
public Imagick::deskewImage(float $threshold): bool
```php

Eeste método se puede usar para eliminar la torción de, por ejemplo, imágenes escaneadas donde el papel no estaba debidamente colocado en la superfice del escáner. Este método solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.5 o superior.

## Parámetros

`threshold`  
Umbral de detorción

## Valores devueltos

## Ejemplos

`Imagick::deskewImage`

```
<?php
function deskewImage($threshold) {
    $imagick = new \Imagick(realpath("images/NYTimes-Page1-11-11-1918.jpg"));
    $deskewImagick = clone $imagick;

    //Esto es lo único que se requiere para eliminar la torción.
    $deskewImagick->deskewImage($threshold);

    //El resto de este ejemplo es para hacer el resultado obvio, ya que
    //de lo contrario no sería obvio.
    $trim = 9;

    $deskewImagick->cropImage($deskewImagick->getImageWidth() - $trim, $deskewImagick->getImageHeight(), $trim, 0);
    $imagick->cropImage($imagick->getImageWidth() - $trim, $imagick->getImageHeight(), $trim, 0);
    $deskewImagick->resizeimage($deskewImagick->getImageWidth() / 2, $deskewImagick->getImageHeight() / 2, \Imagick::FILTER_LANCZOS, 1);
    $imagick->resizeimage($imagick->getImageWidth() / 2, $imagick->getImageHeight() / 2, \Imagick::FILTER_LANCZOS, 1);
    $newCanvas = new \Imagick();
    $newCanvas->newimage($imagick->getImageWidth() + $deskewImagick->getImageWidth() + 20, $imagick->getImageHeight(), 'red', 'jpg');
    $newCanvas->compositeimage($imagick, \Imagick::COMPOSITE_COPY, 5, 0);
    $newCanvas->compositeimage($deskewImagick, \Imagick::COMPOSITE_COPY, $imagick->getImageWidth() + 10, 0);

    header("Content-Type: image/jpg");
    echo $newCanvas->getImageBlob();
}

?>

    
```php
