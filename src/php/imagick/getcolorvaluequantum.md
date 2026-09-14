---
title: ImagickPixel::getColorValueQuantum
description: Devuelve el valor cuántico de un color en ImagickPixel
source_url: https://www.php.net/manual/es/imagickpixel.getcolorvaluequantum.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickpixel/getcolorvaluequantum.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 1ef9c7a76
order: 37580
---

ImagickPixel::getColorValueQuantum

Devuelve el valor cuántico de un color en ImagickPixel

## Descripción

```php
public ImagickPixel::getColorValueQuantum(int $color): int
```php

Devuelve el valor cuántico de un color en ImagickPixel. El valor de retorno es un float si ImageMagick ha sido compilado con HDRI, de lo contrario un integer.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El valor cuántico del elemento de color. Float si ImageMagick ha sido compilado con HDRI, de lo contrario un integer.

## Ejemplos

`ImagickPixel::getColorValueQuantum`

```
      
<?php
        $color = new \ImagickPixel('rgb(128, 5, 255)');
        $colorRed = $color->getColorValueQuantum(\Imagick::COLOR_RED);
        $colorGreen = $color->getColorValueQuantum(\Imagick::COLOR_GREEN);
        $colorBlue = $color->getColorValueQuantum(\Imagick::COLOR_BLUE);
        $colorAlpha = $color->getColorValueQuantum(\Imagick::COLOR_ALPHA);

        printf(
            "Red: %s Green: %s  Blue %s Alpha: %s",
            $colorRed,
            $colorGreen,
            $colorBlue,
            $colorAlpha
        );

?>

      
```php
