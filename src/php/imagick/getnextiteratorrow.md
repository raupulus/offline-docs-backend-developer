---
title: ImagickPixelIterator::getNextIteratorRow
description: Devuelve la siguiente línea del iterador de píxeles
source_url: https://www.php.net/manual/es/imagickpixeliterator.getnextiteratorrow.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickpixeliterator/getnextiteratorrow.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: fa0c88f1e
order: 37770
---

ImagickPixelIterator::getNextIteratorRow

Devuelve la siguiente línea del iterador de píxeles

## Descripción

```php
public ImagickPixelIterator::getNextIteratorRow(): array
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Devuelve la siguiente línea, en forma de `array`, desde el iterador de píxeles.

## Valores devueltos

Devuelve la siguiente línea, en forma de `array` de objetos ImagickPixel, o lanza una excepción ImagickPixelIteratorException en caso de error.

## Ejemplos

Ejemplo con `ImagickPixelIterator::getNextIteratorRow`

```
<?php
function getNextIteratorRow($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $imageIterator = $imagick->getPixelIterator();

    $count = 0;
    while ($pixels = $imageIterator->getNextIteratorRow()) {
        if (($count % 3) == 0) {
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

        $count += 1;
    }

    header("Content-Type: image/jpg");
    echo $imagick;
}

?>

     
```php
