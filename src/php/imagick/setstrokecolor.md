---
title: ImagickDraw::setStrokeColor
description: Configura el color utilizado para dibujar objetos
source_url: https://www.php.net/manual/es/imagickdraw.setstrokecolor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/setstrokecolor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 37160
---

ImagickDraw::setStrokeColor

Configura el color utilizado para dibujar objetos

## Descripción

```php
public ImagickDraw::setStrokeColor(ImagickPixel $color): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Configura el color utilizado para dibujar objetos.

## Parámetros

`color`  
El color del trazo.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ImagickDraw::setStrokeColor`

```
<?php
function setStrokeColor($strokeColor, $fillColor, $backgroundColor) {

    $draw = new \ImagickDraw();

    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);

    $draw->setStrokeWidth(5);

    $draw->line(100, 100, 400, 145);
    $draw->rectangle(100, 200, 225, 350);

    $draw->setStrokeOpacity(0.1);
    $draw->line(100, 120, 400, 165);
    $draw->rectangle(275, 200, 400, 350);

    $image = new \Imagick();
    $image->newImage(500, 400, $backgroundColor);
    $image->setImageFormat("png");

    $image->drawImage($draw);

    header("Content-Type: image/png");
    echo $image->getImageBlob();
}

?>

     
```php
