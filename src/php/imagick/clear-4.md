---
title: ImagickPixelIterator::clear
description: Elimina todos los recursos asociados a PixelIterator
source_url: https://www.php.net/manual/es/imagickpixeliterator.clear.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickpixeliterator/clear.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: fa0c88f1e
order: 37720
---

ImagickPixelIterator::clear

Elimina todos los recursos asociados a PixelIterator

## Descripción

```php
public ImagickPixelIterator::clear(): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Elimina todos los recursos asociados a PixelIterator.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo con `ImagickPixelIterator::clear`

```
<?php
function clear($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));

    $imageIterator = $imagick->getPixelRegionIterator(100, 100, 250, 200);

    /* Se recorren las líneas de píxeles */
    foreach ($imageIterator as $pixels) {
        /** @var $pixel \ImagickPixel */
        /* Se recorren los píxeles de la línea (columna) */
        foreach ($pixels as $column => $pixel) {
            if ($column % 2) {
                /* Pintar cada segundo píxel de negro */
                $pixel->setColor("rgba(0, 0, 0, 0)");
            }
        }
        /* Se sincroniza el iterador, esto es importante en cada iteración */
        $imageIterator->syncIterator();
    }

    $imageIterator->clear();

    header("Content-Type: image/jpg");
    echo $imagick;
}

?>

     
```php
