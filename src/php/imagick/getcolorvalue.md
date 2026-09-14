---
title: ImagickPixel::getColorValue
description: Obtiene el valor normalizado del canal de color proporcionado
source_url: https://www.php.net/manual/es/imagickpixel.getcolorvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickpixel/getcolorvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: fa0c88f1e
order: 37570
---

ImagickPixel::getColorValue

Obtiene el valor normalizado del canal de color proporcionado

## Descripción

```php
public ImagickPixel::getColorValue(int $color): float
```php

Obtiene el valor del canal de color especificado, en forma de número de punto flotante comprendido entre 0 y 1.

## Parámetros

`color`  
El color para el cual se obtendrá el valor, especificado en forma de constante de colores Imagick. Puede ser colores RGB, colores CMYK, alpha y opacidad, i.e. Imagick::COLOR_BLUE o Imagick::COLOR_MAGENTA.

## Valores devueltos

El valor del canal, en forma de número de punto flotante normalizado, o lanza una excepción `ImagickPixelException` si ocurre un error.

## Ejemplos

Uso básico del método `Imagick::getColorValue`

```
<?php

$color = new ImagickPixel('rgba(90%, 20%, 20%, 0.75)');

echo "El valor alpha es ".$color->getColorValue(Imagick::COLOR_ALPHA).PHP_EOL;
echo "".PHP_EOL;
echo "El valor rojo es ".$color->getColorValue(Imagick::COLOR_RED).PHP_EOL;
echo "El valor verde es ".$color->getColorValue(Imagick::COLOR_GREEN).PHP_EOL;
echo "El valor azul es ".$color->getColorValue(Imagick::COLOR_BLUE).PHP_EOL;
echo "".PHP_EOL;
echo "El valor Cian es ".$color->getColorValue(Imagick::COLOR_CYAN).PHP_EOL;
echo "El valor Magenta es ".$color->getColorValue(Imagick::COLOR_MAGENTA).PHP_EOL;
echo "El valor amarillo es ".$color->getColorValue(Imagick::COLOR_YELLOW).PHP_EOL;
echo "El valor negro es ".$color->getColorValue(Imagick::COLOR_BLACK).PHP_EOL;

?>

    
```php

El ejemplo anterior mostrará:

    El valor alpha es 0.74999618524453

    El valor rojo es 0.90000762951095
    El valor verde es 0.2
    El valor azul es 0.2

    El valor Cian es 0.90000762951095
    El valor Magenta es 0.2
    El valor amarillo es 0.2
    El valor negro es 0
