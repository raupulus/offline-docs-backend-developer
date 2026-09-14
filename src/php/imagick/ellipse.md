---
title: ImagickDraw::ellipse
description: Dibuja una elipse sobre una imagen
source_url: https://www.php.net/manual/es/imagickdraw.ellipse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/ellipse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 36260
---

ImagickDraw::ellipse

Dibuja una elipse sobre una imagen

## Descripción

```php
public ImagickDraw::ellipse(float $origin_x, float $origin_y, float $radius_x, float $radius_y, float $angle_start, float $angle_end): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Dibuja una elipse sobre una imagen.

## Parámetros

`origin_x`  

`origin_y`  

`radius_x`  

`radius_y`  

`angle_start`  

`angle_end`  

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ImagickDraw::ellipse`

```
<?php
function ellipse($strokeColor, $fillColor, $backgroundColor) {

    $draw = new \ImagickDraw();
    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);

    $draw->setStrokeWidth(2);
    $draw->setFontSize(72);

    $draw->ellipse(125, 70, 100, 50, 0, 360);
    $draw->ellipse(350, 70, 100, 50, 0, 315);

    $draw->push();
    $draw->translate(125, 250);
    $draw->rotate(30);
    $draw->ellipse(0, 0, 100, 50, 0, 360);
    $draw->pop();

    $draw->push();
    $draw->translate(350, 250);
    $draw->rotate(30);
    $draw->ellipse(0, 0, 100, 50, 0, 315);
    $draw->pop();

    $imagick = new \Imagick();
    $imagick->newImage(500, 500, $backgroundColor);
    $imagick->setImageFormat("png");

    $imagick->drawImage($draw);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

     
```php
