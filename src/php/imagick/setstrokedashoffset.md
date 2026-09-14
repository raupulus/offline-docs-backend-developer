---
title: ImagickDraw::setStrokeDashOffset
description: Especifica el índice dentro del patrón de discontinuidad para iniciar
  la discontinuidad
source_url: https://www.php.net/manual/es/imagickdraw.setstrokedashoffset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/setstrokedashoffset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 668b6fc28
order: 37180
---

ImagickDraw::setStrokeDashOffset

Especifica el índice dentro del patrón de discontinuidad para iniciar la discontinuidad

## Descripción

```php
public ImagickDraw::setStrokeDashOffset(float $dash_offset): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Especifica el índice dentro del patrón de discontinuidad para iniciar la discontinuidad.

## Parámetros

`dash_offset`  
índice de discontinuidad

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `ImagickDraw::setStrokeDashOffset`

```
      
<?php
function setStrokeDashOffset($strokeColor, $fillColor, $backgroundColor) {

    $draw = new \ImagickDraw();

    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);
    $draw->setStrokeWidth(4);
    $draw->setStrokeDashArray([20, 20]);
    $draw->setStrokeDashOffset(0);
    $draw->rectangle(100, 50, 225, 175);

    //Start the dash effect halfway through the solid portion
    $draw->setStrokeDashOffset(10);
    $draw->rectangle(275, 50, 400, 175);

    //Start the dash effect on the space portion
    $draw->setStrokeDashOffset(20);
    $draw->rectangle(100, 200, 225, 350);
    $draw->setStrokeDashOffset(5);
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
