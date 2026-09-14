---
title: ImagickDraw::affine
description: Ajusta la matriz de transformación afín actual
source_url: https://www.php.net/manual/es/imagickdraw.affine.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/affine.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 6047c10c1
order: 36140
---

ImagickDraw::affine

Ajusta la matriz de transformación afín actual

## Descripción

```php
public ImagickDraw::affine(array $affine): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Ajusta la matriz de transformación afín actual con la matriz de transformación afín especificada.

## Parámetros

`affine`  
Los parámetros de la matriz afín

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `ImagickDraw::affine`

```
      
<?php
function affine($strokeColor, $fillColor, $backgroundColor) {

    $draw = new \ImagickDraw();

    $draw->setStrokeWidth(1);
    $draw->setStrokeOpacity(1);
    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);

    $draw->setStrokeWidth(2);

    $PI = 3.141592653589794;
    $angle = 60 * $PI / 360;

    //Scale the drawing co-ordinates.
    $affineScale = array("sx" => 1.75, "sy" => 1.75, "rx" => 0, "ry" => 0, "tx" => 0, "ty" => 0);

    //Shear the drawing co-ordinates.
    $affineShear = array("sx" => 1, "sy" => 1, "rx" => sin($angle), "ry" => -sin($angle), "tx" => 0, "ty" => 0);

    //Rotate the drawing co-ordinates. The shear affine matrix
    //produces incorrectly scaled drawings.
    $affineRotate = array("sx" => cos($angle), "sy" => cos($angle), "rx" => sin($angle), "ry" => -sin($angle), "tx" => 0, "ty" => 0,);

    //Translate (offset) the drawing
    $affineTranslate = array("sx" => 1, "sy" => 1, "rx" => 0, "ry" => 0, "tx" => 30, "ty" => 30);

    //The identity affine matrix
    $affineIdentity = array("sx" => 1, "sy" => 1, "rx" => 0, "ry" => 0, "tx" => 0, "ty" => 0);

    $examples = [$affineScale, $affineShear, $affineRotate, $affineTranslate, $affineIdentity,];

    $count = 0;

    foreach ($examples as $example) {
        $draw->push();
        $draw->translate(($count % 2) * 250, intval($count / 2) * 250);
        $draw->translate(100, 100);
        $draw->affine($example);
        $draw->rectangle(-50, -50, 50, 50);
        $draw->pop();
        $count++;
    }

    //Create an image object which the draw commands can be rendered into
    $image = new \Imagick();
    $image->newImage(500, 750, $backgroundColor);
    $image->setImageFormat("png");

    //Render the draw commands in the ImagickDraw object
    //into the image.
    $image->drawImage($draw);

    //Send the image to the browser
    header("Content-Type: image/png");
    echo $image->getImageBlob();
}

?>

      
```php
