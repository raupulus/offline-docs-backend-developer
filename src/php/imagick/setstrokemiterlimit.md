---
title: ImagickDraw::setStrokeMiterLimit
description: Especifica el límite del inglete
source_url: https://www.php.net/manual/es/imagickdraw.setstrokemiterlimit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/setstrokemiterlimit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 668b6fc28
order: 37210
---

ImagickDraw::setStrokeMiterLimit

Especifica el límite del inglete

## Descripción

```php
public ImagickDraw::setStrokeMiterLimit(int $miterlimit): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Especifica el límite del inglete. Cuando dos segmentos de línea se encuentran en un águlo agudo y la unión del inglete ha sido especificada para 'lineJoin', es posible que el inglete se extienda más allá del grosor de la línea que contornea el trazado. 'miterLimit' impone un límite en la proporción de la longitud del inglete a 'lineWidth'.

## Parámetros

`miterlimit`  
el límite del inglete

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `ImagickDraw::setStrokeMiterLimit`

```
      
<?php
function setStrokeMiterLimit($strokeColor, $fillColor, $backgroundColor) {

    $draw = new \ImagickDraw();

    $draw->setStrokeColor($strokeColor);
    $draw->setStrokeOpacity(0.6);
    $draw->setFillColor($fillColor);
    $draw->setStrokeWidth(10);

    $yOffset = 100;

    $draw->setStrokeLineJoin(\Imagick::LINEJOIN_MITER);

    for ($y = 0; $y < 3; $y++) {

        $draw->setStrokeMiterLimit(40 * $y);

        $points = [
            ['x' => 22 * 3, 'y' => 15 * 4 + $y * $yOffset],
            ['x' => 20 * 3, 'y' => 20 * 4 + $y * $yOffset],
            ['x' => 70 * 5, 'y' => 45 * 4 + $y * $yOffset],
        ];

        $draw->polygon($points);
    }

    $image = new \Imagick();
    $image->newImage(500, 500, $backgroundColor);
    $image->setImageFormat("png");
    $image->drawImage($draw);

    $image->setImageType(\Imagick::IMGTYPE_PALETTE);
    $image->setImageCompressionQuality(100);
    $image->stripImage();

    header("Content-Type: image/png");
    echo $image->getImageBlob();
}

?>

      
```php
