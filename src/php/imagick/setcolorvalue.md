---
title: ImagickPixel::setColorValue
description: Define el valor normalizado de uno de los canales
source_url: https://www.php.net/manual/es/imagickpixel.setcolorvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickpixel/setcolorvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: fa0c88f1e
order: 37660
---

ImagickPixel::setColorValue

Define el valor normalizado de uno de los canales

## Descripción

```php
public ImagickPixel::setColorValue(int $color, float $value): bool
```php

Define el valor del canal especificado del objeto al valor especificado, que debe estar comprendido entre 0 y 1. Esta función puede ser utilizada para proporcionar un canal de opacidad al objeto ImagickPixel.

## Parámetros

`color`  
Una constante de color Imagick, i.e. \Imagick::COLOR_GREEN o \Imagick::COLOR_ALPHA.

`value`  
El valor a definir para este canal, comprendido entre 0 y 1.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo con `Imagick::setColorValue`

```
<?php

$color  = new \ImagickPixel('firebrick');

$color->setColorValue(Imagick::COLOR_ALPHA, 0.5);

print_r($color->getcolor(true));
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [r] => 0.69803921568627
        [g] => 0.13333333333333
        [b] => 0.13333333333333
        [a] => 0.50000762951095
    )
