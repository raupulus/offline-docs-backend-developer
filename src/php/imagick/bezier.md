---
title: ImagickDraw::bezier
description: Dibuja una curva de Bézier
source_url: https://www.php.net/manual/es/imagickdraw.bezier.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/bezier.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 668b6fc28
order: 36170
---

ImagickDraw::bezier

Dibuja una curva de Bézier

## Descripción

```php
public ImagickDraw::bezier(array $coordinates): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Dibuja una curva de Bézier a través de un conjunto de puntos en la imagen.

## Parámetros

`coordinates`  
Array multidimensional como array( array( 'x' =\> 1, 'y' =\> 2 ), array( 'x' =\> 3, 'y' =\> 4 ) )

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `ImagickDraw::bezier`

```
      
<?php
function bezier($strokeColor, $fillColor, $backgroundColor) {

    $draw = new \ImagickDraw();

    $strokeColor = new \ImagickPixel($strokeColor);
    $fillColor = new \ImagickPixel($fillColor);

    $draw->setStrokeOpacity(1);
    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);

    $draw->setStrokeWidth(2);

    $smoothPointsSet = [
        [
            ['x' => 10.0 * 5, 'y' => 10.0 * 5],
            ['x' => 30.0 * 5, 'y' => 90.0 * 5],
            ['x' => 25.0 * 5, 'y' => 10.0 * 5],
            ['x' => 50.0 * 5, 'y' => 50.0 * 5],
        ],
        [
            ['x' => 50.0 * 5, 'y' => 50.0 * 5],
            ['x' => 75.0 * 5, 'y' => 90.0 * 5],
            ['x' => 70.0 * 5, 'y' => 10.0 * 5],
            ['x' => 90.0 * 5, 'y' => 40.0 * 5],
        ],
    ];

    foreach ($smoothPointsSet as $points) {
        $draw->bezier($points);
    }

    $disjointPoints = [
        [
            ['x' => 10 * 5, 'y' => 10 * 5],
            ['x' => 30 * 5, 'y' => 90 * 5],
            ['x' => 25 * 5, 'y' => 10 * 5],
            ['x' => 50 * 5, 'y' => 50 * 5],
        ],
        [
            ['x' => 50 * 5, 'y' => 50 * 5],
            ['x' => 80 * 5, 'y' => 50 * 5],
            ['x' => 70 * 5, 'y' => 10 * 5],
            ['x' => 90 * 5, 'y' => 40 * 5],
         ]
    ];
    $draw->translate(0, 200);

    foreach ($disjointPoints as $points) {
        $draw->bezier($points);
    }

    //Create an image object which the draw commands can be rendered into
    $imagick = new \Imagick();
    $imagick->newImage(500, 500, $backgroundColor);
    $imagick->setImageFormat("png");

    //Render the draw commands in the ImagickDraw object
    //into the image.
    $imagick->drawImage($draw);

    //Send the image to the browser
    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

      
```php
