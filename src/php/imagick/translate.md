---
title: ImagickDraw::translate
description: Aplica una traslación del sistema de coordenadas actual
source_url: https://www.php.net/manual/es/imagickdraw.translate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/translate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 668b6fc28
order: 37370
---

ImagickDraw::translate

Aplica una traslación del sistema de coordenadas actual

## Descripción

```php
public ImagickDraw::translate(float $x, float $y): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Aplica una traslación del sistema de coordenadas actual el cuál mueve el origen del sistema de coordenadas a las coordenadas especifiacadas.

## Parámetros

`x`  
traslación horizontal

`y`  
traslación vertical

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `ImagickDraw::translate`

```
      
<?php
function translate($strokeColor, $fillColor, $backgroundColor, $fillModifiedColor,
                   $startX, $startY, $endX, $endY, $translateX, $translateY) {

    $draw = new \ImagickDraw();

    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);
    $draw->rectangle($startX, $startY, $endX, $endY);

    $draw->setFillColor($fillModifiedColor);
    $draw->translate($translateX, $translateY);
    $draw->rectangle($startX, $startY, $endX, $endY);

    $image = new \Imagick();
    $image->newImage(500, 500, $backgroundColor);
    $image->setImageFormat("png");

    $image->drawImage($draw);

    header("Content-Type: image/png");
    echo $image->getImageBlob();
}

?>

      
```php
