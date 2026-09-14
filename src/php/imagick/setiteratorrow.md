---
title: ImagickPixelIterator::setIteratorRow
description: Define la línea del iterador de píxeles
source_url: https://www.php.net/manual/es/imagickpixeliterator.setiteratorrow.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickpixeliterator/setiteratorrow.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: fa0c88f1e
order: 37840
---

ImagickPixelIterator::setIteratorRow

Define la línea del iterador de píxeles

## Descripción

```php
public ImagickPixelIterator::setIteratorRow(int $row): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Define la línea del iterador de píxeles.

## Parámetros

`row`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo con `ImagickPixelIterator::setIteratorRow`

```
<?php
function setIteratorRow($imagePath) {
    $imagick = new \Imagick(realpath($imagePath));
    $imageIterator = $imagick->getPixelRegionIterator(200, 100, 200, 200);

    for ($x = 0; $x < 20; $x++) {
        $imageIterator->setIteratorRow($x * 5);
        $pixels = $imageIterator->getCurrentIteratorRow();
        /* Se recorren los píxeles de la línea (columna) */
        foreach ($pixels as $pixel) {
            /** @var $pixel \ImagickPixel */
            /* Se tiñen todos los píxeles en negro */
            $pixel->setColor("rgba(0, 0, 0, 0)");
        }

        /* Se sincroniza el iterador; esto es importante en cada iteración */
        $imageIterator->syncIterator();
    }

    header("Content-Type: image/jpg");
    echo $imagick;
}

?>

     
```php
