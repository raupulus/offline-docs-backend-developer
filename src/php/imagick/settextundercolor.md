---
title: ImagickDraw::setTextUnderColor
description: Especifica el color de fondo de un rectángulo
source_url: https://www.php.net/manual/es/imagickdraw.settextundercolor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/settextundercolor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 37320
---

ImagickDraw::setTextUnderColor

Especifica el color de fondo de un rectángulo

## Descripción

```php
public ImagickDraw::setTextUnderColor(ImagickPixel $under_color): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Especifica el color de fondo de un rectángulo a colocar bajo los textos.

## Parámetros

`under_color`  
El color de fondo

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ImagickDraw::setTextUnderColor`

```
<?php
function setTextUnderColor($strokeColor, $fillColor, $backgroundColor, $textUnderColor) {
    $draw = new \ImagickDraw();

    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);
    $draw->setStrokeWidth(2);
    $draw->setFontSize(72);
    $draw->annotation(50, 75, "Lorem Ipsum!");
    $draw->setTextUnderColor($textUnderColor);
    $draw->annotation(50, 175, "Lorem Ipsum!");

    $imagick = new \Imagick();
    $imagick->newImage(500, 500, $backgroundColor);
    $imagick->setImageFormat("png");

    $imagick->drawImage($draw);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

     
```php
