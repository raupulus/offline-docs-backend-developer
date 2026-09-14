---
title: ImagickDraw::rectangle
description: Dibuja un rectángulo
source_url: https://www.php.net/manual/es/imagickdraw.rectangle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/rectangle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 36920
---

ImagickDraw::rectangle

Dibuja un rectángulo

## Descripción

```php
public ImagickDraw::rectangle(float $top_left_x, float $top_left_y, float $bottom_right_x, float $bottom_right_y): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Dibuja un rectángulo a partir de sus coordenadas y utilizando el trazo actual, su ancho y su patrón.

## Parámetros

`top_left_x`  

`top_left_y`  
ordenada del ángulo superior izquierdo

`bottom_right_x`  
abscisa del ángulo inferior derecho

`bottom_right_y`  
ordenada del ángulo inferior derecho

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ImagickDraw::rectangle`

```
<?php
function rectangle($strokeColor, $fillColor, $backgroundColor) {
    $draw = new \ImagickDraw();
    $strokeColor = new \ImagickPixel($strokeColor);
    $fillColor = new \ImagickPixel($fillColor);

    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);
    $draw->setStrokeOpacity(1);
    $draw->setStrokeWidth(2);

    $draw->rectangle(200, 200, 300, 300);
    $imagick = new \Imagick();
    $imagick->newImage(500, 500, $backgroundColor);
    $imagick->setImageFormat("png");

    $imagick->drawImage($draw);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

     
```php
