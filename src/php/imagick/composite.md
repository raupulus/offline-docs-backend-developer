---
title: ImagickDraw::composite
description: Componer una imagen con otra
source_url: https://www.php.net/manual/es/imagickdraw.composite.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/composite.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 36230
---

ImagickDraw::composite

Componer una imagen con otra

## Descripción

```php
public ImagickDraw::composite(int $composite, float $x, float $y, float $width, float $height, Imagick $image): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Componer una imagen con otra, utilizando el operador de composición, en la posición y tamaño indicados.

## Parámetros

`composite`  
El operador de composición. Una de las constantes de [operador de composición](#imagick.constants.compositeop) (`imagick::COMPOSITE_*`).

`x`  
Abscisa del ángulo superior izquierdo.

`y`  
Ordenada del ángulo superior izquierdo.

`width`  
Ancho de la imagen de composición.

`height`  
Alto de la imagen de composición.

`image`  
El objeto `Imagick` donde se toma la composición.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo con `ImagickDraw::composite`

```
<?php
function composite($strokeColor, $fillColor, $backgroundColor) {

    $draw = new \ImagickDraw();

    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);
    $draw->setFillOpacity(1);
    $draw->setStrokeWidth(2);
    $draw->setFontSize(72);
    $draw->setStrokeOpacity(1);
    $draw->setStrokeColor($strokeColor);
    $draw->setStrokeWidth(2);
    $draw->setFont("../fonts/CANDY.TTF");
    $draw->setFontSize(140);
    $draw->rectangle(0, 0, 1000, 300);
    $draw->setFillColor('white');
    $draw->setfillopacity(1);
    $draw->annotation(50, 180, "Lorem Ipsum!");

    //Crea un objeto imagen que sirve de base
    $imagick = new \Imagick();
    $imagick->newImage(1000, 302, $backgroundColor);
    $imagick->setImageFormat("png");

    //Se aplican las órdenes de dibujo en el objeto ImagickDraw
    //y en la imagen.
    $imagick->drawImage($draw);

    //Se envía la imagen al navegador
    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

     
```php
