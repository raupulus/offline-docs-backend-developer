---
title: ImagickPixel::getColorCount
description: Devuelve el número de colores asociados con un color
source_url: https://www.php.net/manual/es/imagickpixel.getcolorcount.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickpixel/getcolorcount.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 65c4446ab
order: 37550
---

ImagickPixel::getColorCount

Devuelve el número de colores asociados con un color

## Descripción

```php
public ImagickPixel::getColorCount(): int
```php

Devuelve el número de colores asociados con el color.

El número de píxeles de la imagen que tienen el mismo color que este ImagickPixel.

ImagickPixel::getColorCount parece funcionar únicamente para los objetos ImagickPixel creados mediante Imagick::getImageHistogram()

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de colores, en forma de `int` en caso de éxito o lanza una excepción `ImagickPixelException` si ocurre un error.

## Ejemplos

ImagickPixel `getColorCount`

```
<?php
    $imagick = new \Imagick();
    $imagick->newPseudoImage(640, 480, "magick:logo");
    $histogramElements = $imagick->getImageHistogram();
    $lastColor = array_pop($histogramElements);
    echo "Last pixel color count is: ".$lastColor->getColorCount();
?>

    
```php

La salida para esto será similar a:

```
Last pixel color count is: 256244

    
```php
