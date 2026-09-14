---
title: ImagickPixel::getColor
description: Devuelve el color
source_url: https://www.php.net/manual/es/imagickpixel.getcolor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickpixel/getcolor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: f80105b4f
order: 37530
---

ImagickPixel::getColor

Devuelve el color

## Descripción

```php
public ImagickPixel::getColor([int $normalized]): array
```php

Devuelve el color descrito por el objeto `ImagickPixel`, en forma de un `array`. Si el color contiene un canal de opacidad, este será proporcionado como cuarta valor de la lista.

## Parámetros

`normalized`  
Normaliza los valores de color. Los valores posibles son `0`, `1` o `2`.

| `normalized` | Descripción |
|----|----|
| `0` | Los valores RGB son devueltos como `int`s en el intervalo (inclusivo) `0` a `255`. El valor alpha es devuelto como `int` y es `0` o `1`. |
| `1` | Los valores RGBA son devueltos como `float`s en el intervalo (inclusivo) `0` a `1`. |
| `2` | Los valores RGBA son devueltos como `int`s en el intervalo (inclusivo) `0` a `255`. |

Lista de valores posibles para `normalized`

## Valores devueltos

Un array de los valores de los canales. Genera `ImagickPixelException` en caso de error.

## Ejemplos

Uso simple del método `Imagick::getColor`

```
<?php

// Crea un objeto ImagickPixel con el color predeterminado 'marron'
$color = new ImagickPixel('brown');

// Define el color para tener un canal alpha del 25%
$color->setColorValue(Imagick::COLOR_ALPHA, 64 / 256.0);

$colorInfo = $color->getColor();

echo "Valores estándar :".PHP_EOL;
print_r($colorInfo);

$colorInfo = $color->getColor(1);

echo "Valores normalizados :".PHP_EOL;
print_r($colorInfo);

?>

    
```php

El ejemplo anterior mostrará:

        
    Valores estándar :
    Array
    (
        [r] => 165
        [g] => 42
        [b] => 42
        [a] => 0
    )
    Valores normalizados :
    Array
    (
        [r] => 0.64705882352941
        [g] => 0.16470588235294
        [b] => 0.16470588235294
        [a] => 0.25000381475547
    )
