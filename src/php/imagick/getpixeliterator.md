---
title: Imagick::getPixelIterator
description: Devuelve un MagickPixelIterator
source_url: https://www.php.net/manual/es/imagick.getpixeliterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getpixeliterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 65c4446ab
order: 34160
---

Imagick::getPixelIterator

Devuelve un MagickPixelIterator

## Descripción

```php
public Imagick::getPixelIterator(): ImagickPixelIterator
```php

Devuelve un MagickPixelIterator.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un objeto ImagickPixelIterator.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Ejemplo con `Imagick::getPixelIterator`

```
<?php
function getPixelIterator($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $imageIterator = $imagick->getPixelIterator();

    foreach ($imageIterator as $row => $pixels) { /* Se recorren las líneas de píxeles */
        foreach ($pixels as $column => $pixel) { /* Se recorren los píxeles en la línea (columna) */
            /** @var $pixel \ImagickPixel */
            if ($column % 2) {
                $pixel->setColor("rgba(0, 0, 0, 0)"); /* Se pintan todos los segundos píxeles en negro */
            }
        }
        $imageIterator->syncIterator(); /* Se sincroniza el iterador, es importante hacerlo en cada iteración */
    }

    header("Content-Type: image/jpg");
    echo $imagick;
}

?>

     
```php
