---
title: ImagickPixelIterator::resetIterator
description: Reinicia el iterador de píxeles
source_url: https://www.php.net/manual/es/imagickpixeliterator.resetiterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickpixeliterator/resetiterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 6047c10c1
order: 37810
---

ImagickPixelIterator::resetIterator

Reinicia el iterador de píxeles

## Descripción

```php
public ImagickPixelIterator::resetIterator(): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Reinicia el iterador de píxeles. Utilice este método con ImagickPixelIterator::getNextIteratorRow() para iterar sobre todos los píxeles de un contenedor de píxeles.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo con `ImagickPixelIterator::resetIterator`

```
<?php
function resetIterator($imagePath) {

    $imagick = new \Imagick(realpath($imagePath));

    $imageIterator = $imagick->getPixelIterator();

    /* Se recorren las líneas de píxeles */
    foreach ($imageIterator as $pixels) {
        /* Se recorren los píxeles de la línea (columna) */
        foreach ($pixels as $column => $pixel) {
            /** @var $pixel \ImagickPixel */
            if ($column % 2) {

                /* Cada dos píxeles, se añade un 25% de rojo */
                $pixel->setColorValue(\Imagick::COLOR_RED, 64);
            }
        }
        /* Se sincroniza el iterador, esto es importante en cada iteración */
        $imageIterator->syncIterator();
    }

    $imageIterator->resetiterator();

    /* Se recorren las líneas de píxeles */
    foreach ($imageIterator as $pixels) {
        /* Se recorren los píxeles de la línea (columna) */
        foreach ($pixels as $column => $pixel) {
            /** @var $pixel \ImagickPixel */
            if ($column % 3) {
                $pixel->setColorValue(\Imagick::COLOR_BLUE, 64); /* Cada dos píxeles, se los hace un poco más azules */
                //$pixel->setColor("rgba(0, 0, 128, 0)"); /* Se tiñen todos los dos píxeles en negro */
            }
        }
        $imageIterator->syncIterator(); /* Se sincroniza el iterador, esto es importante en cada iteración */
    }

    $imageIterator->clear();

    header("Content-Type: image/jpg");
    echo $imagick;
}

?>

     
```php
