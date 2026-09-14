---
title: ImagickPixel::setColorValueQuantum
description: Define la valor cuántica de un elemento de color de ImagickPixel
source_url: https://www.php.net/manual/es/imagickpixel.setcolorvaluequantum.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickpixel/setcolorvaluequantum.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 1ef9c7a76
order: 37670
---

ImagickPixel::setColorValueQuantum

Define la valor cuántica de un elemento de color de ImagickPixel

## Descripción

```php
public ImagickPixel::setColorValueQuantum(int $color, int $value): bool
```php

Define la valor cuántica de un elemento de color de ImagickPixel.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`color`  
Color a definir, por ejemplo \Imagick::COLOR_GREEN.

`value`  
Valor cuántica a definir para el elemento de color. Debería ser un float si ImageMagick ha sido compilado con HDRI, de lo contrario un integer en el rango 0 a Imagick::getQuantum().

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

`ImagickPixel::setColorValueQuantum`

```
      
<?php
function setColorValueQuantum() {
    $image = new \Imagick();

    $quantumRange = $image->getQuantumRange();

    $draw = new \ImagickDraw();
    $color = new \ImagickPixel('blue');
    $color->setcolorValueQuantum(\Imagick::COLOR_RED, 128 * $quantumRange['quantumRangeLong'] / 256);

    $draw->setstrokewidth(1.0);
    $draw->setStrokeColor($color);
    $draw->setFillColor($color);
    $draw->rectangle(200, 200, 300, 300);

    $image->newImage(500, 500, "SteelBlue2");
    $image->setImageFormat("png");

    $image->drawImage($draw);

    header("Content-Type: image/png");
    echo $image->getImageBlob();
}

?>

      
```php
