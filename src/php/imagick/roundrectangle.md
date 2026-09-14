---
title: ImagickDraw::roundRectangle
description: Dibuja un rectángulo con esquinas redondeadas
source_url: https://www.php.net/manual/es/imagickdraw.roundrectangle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/roundrectangle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 36960
---

ImagickDraw::roundRectangle

Dibuja un rectángulo con esquinas redondeadas

## Descripción

```php
public ImagickDraw::roundRectangle(float $top_left_x, float $top_left_y, float $bottom_right_x, float $bottom_right_y, float $rounding_x, float $rounding_y): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Dibuja un rectángulo con esquinas redondeadas, a partir de dos coordenadas, x & y, el radio de esquina y utilizando el trazo actual, su grosor y su color de relleno.

## Parámetros

`top_left_x`  
La abscisa de la esquina superior izquierda

`top_left_y`  
La ordenada de la esquina superior izquierda

`bottom_right_x`  
La abscisa de la esquina inferior derecha

`bottom_right_y`  
La ordenada de la esquina inferior derecha

`rounding_x`  
El radio en x

`rounding_y`  
El radio en y

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ImagickDraw::roundRectangle`

```
<?php
function roundRectangle($strokeColor, $fillColor, $backgroundColor, $startX, $startY, $endX, $endY, $roundX, $roundY) {

    $draw = new \ImagickDraw();

    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);
    $draw->setStrokeOpacity(1);
    $draw->setStrokeWidth(2);

    $draw->roundRectangle($startX, $startY, $endX, $endY, $roundX, $roundY);

    $imagick = new \Imagick();
    $imagick->newImage(500, 500, $backgroundColor);
    $imagick->setImageFormat("png");

    $imagick->drawImage($draw);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

     
```php
