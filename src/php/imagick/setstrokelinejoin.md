---
title: ImagickDraw::setStrokeLineJoin
description: Especifica la forma a utilizar para dibujar los extremos de las líneas
source_url: https://www.php.net/manual/es/imagickdraw.setstrokelinejoin.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/setstrokelinejoin.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 0f49e97ee
order: 37200
---

ImagickDraw::setStrokeLineJoin

Especifica la forma a utilizar para dibujar los extremos de las líneas

## Descripción

```php
public ImagickDraw::setStrokeLineJoin(int $linejoin): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Especifica la forma a utilizar para dibujar los extremos de las líneas y otras formas vectoriales cuando utilizan un trazo.

## Parámetros

`linejoin`  
Una de las constantes [LINEJOIN](#imagick.constants.linejoin) (`imagick::LINEJOIN_*`).

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ImagickDraw::setStrokeLineJoin`

```
<?php
function setStrokeLineJoin($strokeColor, $fillColor, $backgroundColor) {

    $draw = new \ImagickDraw();
    $draw->setStrokeWidth(1);
    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);

    $draw->setStrokeWidth(20);

    $offset = 220;

    $lineJoinStyle = [
        \Imagick::LINEJOIN_MITER,
        \Imagick::LINEJOIN_ROUND,
        \Imagick::LINEJOIN_BEVEL,
        ];

    for ($x = 0; $x < count($lineJoinStyle); $x++) {
        $draw->setStrokeLineJoin($lineJoinStyle[$x]);
        $points = [
            ['x' => 40 * 5, 'y' => 10 * 5 + $x * $offset],
            ['x' => 20 * 5, 'y' => 20 * 5 + $x * $offset],
            ['x' => 70 * 5, 'y' => 50 * 5 + $x * $offset],
            ['x' => 40 * 5, 'y' => 10 * 5 + $x * $offset],
        ];

        $draw->polyline($points);
    }

    $image = new \Imagick();
    $image->newImage(500, 700, $backgroundColor);
    $image->setImageFormat("png");

    $image->drawImage($draw);

    header("Content-Type: image/png");
    echo $image->getImageBlob();
}

?>

     
```php
