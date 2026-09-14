---
title: ImagickKernel::fromMatrix
description: Crear un núcleo a partir de una matriz 2D de valores
source_url: https://www.php.net/manual/es/imagickkernel.frommatrix.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickkernel/frommatrix.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 1534707f6
order: 37440
---

ImagickKernel::fromMatrix

Crear un núcleo a partir de una matriz 2D de valores

## Descripción

```php
public static ImagickKernel::fromMatrix(array $matrix, [array $origin]): ImagickKernel
```php

Crear un núcleo a partir de una matriz 2D de valores. Cada valor debe ser un float (si el elemento debe ser utilizado) o 'false' si el elemento debe ser ignorado. Para las matrices que tienen tamaños impares en ambas dimensiones, el píxel de origen será por defecto en el centro del núcleo. Para todas las demás dimensiones de núcleo, el píxel de origen debe ser especificado.

## Parámetros

`array`  
Una matriz (es decir, un array 2D) de valores que definen el núcleo. Cada elemento debe ser un valor float, o FALSE si este elemento no debe ser utilizado por el núcleo.

`array`  
Cuál elemento del núcleo debe ser utilizado como píxel de origen. Por ejemplo, para una matriz 3x3 especificando el origen como \[2, 2\] especificaría que el elemento en la parte inferior derecha debería ser el píxel de origen.

## Valores devueltos

El objeto ImagickKernel generado.

## Ejemplos

`ImagickKernel::fromMatrix`

```
      
<?php

function renderKernel(ImagickKernel $imagickKernel) {
    $matrix = $imagickKernel->getMatrix();

    $imageMargin = 20;

    $tileSize = 20;
    $tileSpace = 4;
    $shadowSigma = 4;
    $shadowDropX = 20;
    $shadowDropY = 0;

    $radius = ($tileSize / 2) * 0.9;

    $rows = count($matrix);
    $columns = count($matrix[0]);

    $imagickDraw = new \ImagickDraw();

    $imagickDraw->setFillColor('#afafaf');
    $imagickDraw->setStrokeColor('none');

    $imagickDraw->translate($imageMargin, $imageMargin);
    $imagickDraw->push();

    ksort($matrix);

    foreach ($matrix as $row) {
        ksort($row);
        $imagickDraw->push();
        foreach ($row as $cell) {
            if ($cell !== false) {
                $color = intval(255 * $cell);
                $colorString = sprintf("rgb(%f, %f, %f)", $color, $color, $color);
                $imagickDraw->setFillColor($colorString);
                $imagickDraw->rectangle(0, 0, $tileSize, $tileSize);
            }
            $imagickDraw->translate(($tileSize + $tileSpace), 0);
        }
        $imagickDraw->pop();
        $imagickDraw->translate(0, ($tileSize + $tileSpace));
    }

    $imagickDraw->pop();

    $width = ($columns * $tileSize) + (($columns - 1) * $tileSpace);
    $height = ($rows * $tileSize) + (($rows - 1) * $tileSpace);

    $imagickDraw->push();
    $imagickDraw->translate($width/2 , $height/2);
    $imagickDraw->setFillColor('rgba(0, 0, 0, 0)');
    $imagickDraw->setStrokeColor('white');
    $imagickDraw->circle(0, 0, $radius - 1, 0);
    $imagickDraw->setStrokeColor('black');
    $imagickDraw->circle(0, 0, $radius, 0);
    $imagickDraw->pop();

    $canvasWidth = $width + (2 * $imageMargin);
    $canvasHeight = $height + (2 * $imageMargin);

    $kernel = new \Imagick();
    $kernel->newPseudoImage(
        $canvasWidth,
        $canvasHeight,
        'canvas:none'
    );

    $kernel->setImageFormat('png');
    $kernel->drawImage($imagickDraw);

    /* crear una sombra paralela en su propia capa */
    $canvas = $kernel->clone();
    $canvas->setImageBackgroundColor(new \ImagickPixel('rgb(0, 0, 0)'));
    $canvas->shadowImage(100, $shadowSigma, $shadowDropX, $shadowDropY);

    $canvas->setImagePage($canvasWidth, $canvasHeight, -5, -5);
    $canvas->cropImage($canvasWidth, $canvasHeight, 0, 0);

    /* composite original text_layer onto shadow_layer */
    $canvas->compositeImage($kernel, \Imagick::COMPOSITE_OVER, 0, 0);
    $canvas->setImageFormat('png');

    return $canvas;
}

function createFromMatrix() {
    $matrix = [
        [0.5, 0, 0.2],
        [0, 1, 0],
        [0.9, 0, false],
    ];

    $kernel = \ImagickKernel::fromMatrix($matrix);

    return $kernel;
}

function fromMatrix() {
    $kernel = createFromMatrix();
    $imagick = renderKernel($kernel);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

      
```php
