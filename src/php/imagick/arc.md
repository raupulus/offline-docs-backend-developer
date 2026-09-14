---
title: ImagickDraw::arc
description: Dibuja un arco
source_url: https://www.php.net/manual/es/imagickdraw.arc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/arc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 36160
---

ImagickDraw::arc

Dibuja un arco

## Descripción

```php
public ImagickDraw::arc(float $start_x, float $start_y, float $end_x, float $end_y, float $start_angle, float $end_angle): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Dibuja un arco, situado dentro de un rectángulo.

## Parámetros

`start_x`  
Abscisa del punto de inicio del arco en el rectángulo de contorno

`start_y`  
Ordenada del punto de inicio del arco en el rectángulo de contorno

`end_x`  
Abscisa del punto final del arco en el rectángulo de contorno

`end_y`  
Ordenada del punto final del arco en el rectángulo de contorno

`start_angle`  
Grado de rotación inicial

`end_angle`  
Grado de rotación final

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ImagickDraw::arc`

```
<?php
function arc($strokeColor, $fillColor, $backgroundColor, $startX, $startY, $endX, $endY, $startAngle, $endAngle) {

    //Create a ImagickDraw object to draw into.
    $draw = new \ImagickDraw();
    $draw->setStrokeWidth(1);
    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);
    $draw->setStrokeWidth(2);

    $draw->arc($startX, $startY, $endX, $endY, $startAngle, $endAngle);

    //Create an image object which the draw commands can be rendered into
    $image = new \Imagick();
    $image->newImage(IMAGE_WIDTH, IMAGE_HEIGHT, $backgroundColor);
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
