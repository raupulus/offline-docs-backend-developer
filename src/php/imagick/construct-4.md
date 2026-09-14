---
title: ImagickPixelIterator::__construct
description: El constructor de la clase ImagickPixelIterator
source_url: https://www.php.net/manual/es/imagickpixeliterator.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickpixeliterator/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: fa0c88f1e
order: 37730
---

ImagickPixelIterator::\_\_construct

El constructor de la clase

ImagickPixelIterator

## Descripción

```php
public ImagickPixelIterator::__construct(Imagick $wand)
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

El constructor de la clase `ImagickPixelIterator`.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo con `ImagickPixelIterator::construct`

```
<?php
function construct($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $imageIterator = new \ImagickPixelIterator($imagick);

    /* Se recorren las líneas de píxeles */
    foreach ($imageIterator as $pixels) {
        /* Se recorren los píxeles de la línea (columna) */
        foreach ($pixels as $column => $pixel) {
            /** @var $pixel \ImagickPixel */
            if ($column % 2) {
                /* Se tiñen todos los dos píxeles en negro */
                $pixel->setColor("rgba(0, 0, 0, 0)");
            }
        }
        /* Se sincroniza el iterador, esto es importante en cada iteración */
        $imageIterator->syncIterator();
    }

    header("Content-Type: image/jpg");
    echo $imagick;
}

?>

     
```php
