---
title: ImagickDraw::circle
description: Dibuja un círculo
source_url: https://www.php.net/manual/es/imagickdraw.circle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/circle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 36180
---

ImagickDraw::circle

Dibuja un círculo

## Descripción

```php
public ImagickDraw::circle(float $origin_x, float $origin_y, float $perimeter_x, float $perimeter_y): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Dibuja un círculo.

## Parámetros

`origin_x`  
Abscisa del origen

`origin_y`  
Ordenada del origen

`perimeter_x`  
Abscisa del perímetro

`perimeter_y`  
Ordenada del perímetro

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ImagickDraw::circle`

```
<?php
function circle($strokeColor, $fillColor, $backgroundColor, $originX, $originY, $endX, $endY) {

    //Creación de un objeto ImagickDraw.
    $draw = new \ImagickDraw();

    $strokeColor = new \ImagickPixel($strokeColor);
    $fillColor = new \ImagickPixel($fillColor);

    $draw->setStrokeOpacity(1);
    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);

    $draw->setStrokeWidth(2);
    $draw->setFontSize(72);

    $draw->circle($originX, $originY, $endX, $endY);

    $imagick = new \Imagick();
    $imagick->newImage(500, 500, $backgroundColor);
    $imagick->setImageFormat("png");
    $imagick->drawImage($draw);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

     
```php
