---
title: ImagickDraw::setStrokeOpacity
description: Especifica la opacidad para dibujar los contornos
source_url: https://www.php.net/manual/es/imagickdraw.setstrokeopacity.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/setstrokeopacity.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 37220
---

ImagickDraw::setStrokeOpacity

Especifica la opacidad para dibujar los contornos

## Descripción

```php
public ImagickDraw::setStrokeOpacity(float $opacity): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Especifica la opacidad para dibujar los contornos.

## Parámetros

`opacity`  
La opacidad del trazo. 1.0 es completamente opaco.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ImagickDraw::setStrokeOpacity`

```
<?php
function setStrokeOpacity($strokeColor, $fillColor, $backgroundColor) {
    $draw = new \ImagickDraw();

    $draw->setStrokeWidth(1);
    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);
    $draw->setStrokeWidth(10);
    $draw->setStrokeOpacity(1);
    $draw->line(100, 80, 400, 125);
    $draw->rectangle(25, 200, 150, 350);
    $draw->setStrokeOpacity(0.5);
    $draw->line(100, 100, 400, 145);
    $draw->rectangle(200, 200, 325, 350);
    $draw->setStrokeOpacity(0.2);
    $draw->line(100, 120, 400, 165);
    $draw->rectangle(375, 200, 500, 350);

    $image = new \Imagick();
    $image->newImage(550, 400, $backgroundColor);
    $image->setImageFormat("png");
    $image->drawImage($draw);

    header("Content-Type: image/png");
    echo $image->getImageBlob();
}

?>

     
```php
