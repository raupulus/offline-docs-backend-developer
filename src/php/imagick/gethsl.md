---
title: ImagickPixel::getHSL
description: Retorna el color HSL normalizado del objeto ImagickPixel
source_url: https://www.php.net/manual/es/imagickpixel.gethsl.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickpixel/gethsl.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 65c4446ab
order: 37590
---

ImagickPixel::getHSL

Retorna el color HSL normalizado del objeto

ImagickPixel

## Descripción

```php
public ImagickPixel::getHSL(): array
```php

Retorna el color HSL normalizado, descrito por el objeto `ImagickPixel`, donde cada una de las tres valores será un número decimal, comprendido entre 0.0 y 1.0.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna el valor HSL en un array que contiene las claves `"hue"`, `"saturation"` y `"luminosity"`. Genera una excepción `ImagickPixelException` en caso de error.

## Ejemplos

Ejemplo con `Imagick::getHSL`

```
<?php

$color = new ImagickPixel('rgb(90%, 10%, 10%)');

$colorInfo = $color->getHSL();

print_r($colorInfo);

?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [hue] => 0
        [saturation] => 0.80001220740379
        [luminosity] => 0.50000762951095
    )

## Notas

> [!NOTE]
> Disponible a partir de la versión 6.2.9 y superior de la biblioteca ImageMagick.
