---
title: Imagick::setCompressionQuality
description: Configura la compresión por defecto del objeto
source_url: https://www.php.net/manual/es/imagick.setcompressionquality.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/setcompressionquality.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 0ffb9c9fc
order: 35090
---

Imagick::setCompressionQuality

Configura la compresión por defecto del objeto

## Descripción

```php
public Imagick::setCompressionQuality(int $quality): bool
```php

Configura la compresión por defecto del objeto.

> [!CAUTION]
> Este método solo funciona con nuevas imágenes, es decir, aquellas creadas con el método Imagick::newPseudoImage. Para imágenes existentes, debería utilizarse el método Imagick::setImageCompressionQuality.

## Parámetros

`quality`  
Un `int` entre 1 y 100, 1 = compresión alta, 100 compresión baja.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo con `Imagick::setCompressionQuality`

```
<?php
function setCompressionQuality($imagePath, $quality) {

    $backgroundImagick = new \Imagick(realpath($imagePath));
    $imagick = new \Imagick();
    $imagick->setCompressionQuality($quality);
    $imagick->newPseudoImage(
        $backgroundImagick->getImageWidth(),
        $backgroundImagick->getImageHeight(),
        'canvas:white'
    );

    $imagick->compositeImage(
        $backgroundImagick,
        \Imagick::COMPOSITE_ATOP,
        0,
        0
    );

    $imagick->setFormat("jpg");
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();
}

?>

     
```php
