---
title: ImagickDraw::skewX
description: Tuerce el sistema de coordenadas actual en la dirección horizontal
source_url: https://www.php.net/manual/es/imagickdraw.skewx.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/skewx.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 668b6fc28
order: 37350
---

ImagickDraw::skewX

Tuerce el sistema de coordenadas actual en la dirección horizontal

## Descripción

```php
public ImagickDraw::skewX(float $degrees): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Tuerce el sistema de coordenadas actual en la dirección horizontal.

## Parámetros

`degrees`  
grados de torción

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `ImagickDraw::skewX`

```
      
<?php
function skewX($strokeColor, $fillColor, $backgroundColor, $fillModifiedColor,
               $startX, $startY, $endX, $endY, $skew) {

    $draw = new \ImagickDraw();

    $draw->setStrokeColor($strokeColor);
    $draw->setStrokeWidth(2);
    $draw->setFillColor($fillColor);
    $draw->rectangle($startX, $startY, $endX, $endY);
    $draw->setFillColor($fillModifiedColor);
    $draw->skewX($skew);
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
