---
title: ImagickDraw::setViewbox
description: Configura el tamaño del lienzo
source_url: https://www.php.net/manual/es/imagickdraw.setviewbox.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/setviewbox.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 37340
---

ImagickDraw::setViewbox

Configura el tamaño del lienzo

## Descripción

```php
public ImagickDraw::setViewbox(int $left_x, int $top_y, int $right_x, int $bottom_y): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Configura el tamaño general del lienzo, a registrar con los datos vectoriales. Generalmente, este valor se configura con el mismo tamaño que la imagen. Cuando los datos vectoriales se guardan en SVG o MVG, la caja de vista se utiliza para especificar el tamaño de la imagen en la que el visualizador dibujará los datos.

## Parámetros

`left_x`  
Abscisa izquierda

`top_y`  
Ordenada superior

`right_x`  
Abscisa derecha

`bottom_y`  
Ordenada inferior

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ImagickDraw::setViewBox`

```
<?php
function setViewBox($strokeColor, $fillColor, $backgroundColor) {

    $draw = new \ImagickDraw();

    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);
    $draw->setStrokeWidth(2);
    $draw->setFontSize(72);

    /*
      Configura el tamaño general del lienzo a registrar con los datos vectoriales. Generalmente, este valor se configura con el mismo tamaño que la imagen. Cuando los datos vectoriales se guardan en SVG o MVG, la caja de vista se utiliza para especificar el tamaño de la imagen en la que el visualizador dibujará los datos.
     */

    $draw->circle(250, 250, 250, 0);
    $draw->setviewbox(0, 0, 200, 200);
    $draw->circle(125, 250, 250, 250);
    $draw->translate(250, 125);
    $draw->circle(0, 0, 125, 0);

    $imagick = new \Imagick();
    $imagick->newImage(500, 500, $backgroundColor);
    $imagick->setImageFormat("png");

    $imagick->drawImage($draw);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

     
```php
