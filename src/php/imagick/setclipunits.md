---
title: ImagickDraw::setClipUnits
description: Configura el modo de interpretación de las unidades de ruta
source_url: https://www.php.net/manual/es/imagickdraw.setclipunits.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/setclipunits.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 37000
---

ImagickDraw::setClipUnits

Configura el modo de interpretación de las unidades de ruta

## Descripción

```php
public ImagickDraw::setClipUnits(int $pathunits): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Configura el modo de interpretación de las unidades de ruta.

## Parámetros

`pathunits`  
El número de unidades de clip

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ImagickDraw::setClipUnits`

```
<?php
function setClipUnits($strokeColor, $fillColor, $backgroundColor) {

    $draw = new \ImagickDraw();

    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);
    $draw->setStrokeOpacity(1);
    $draw->setStrokeWidth(2);
    $clipPathName = 'testClipPath';
    $draw->setClipUnits(\Imagick::RESOLUTION_PIXELSPERINCH);
    $draw->pushClipPath($clipPathName);
    $draw->rectangle(0, 0, 250, 250);
    $draw->popClipPath();
    $draw->setClipPath($clipPathName);

    //RESOLUTION_PIXELSPERINCH
    //RESOLUTION_PIXELSPERCENTIMETER

    $draw->rectangle(200, 200, 300, 300);
    $imagick = new \Imagick();
    $imagick->newImage(500, 500, $backgroundColor);
    $imagick->setImageFormat("png");

    $imagick->drawImage($draw);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

     
```php
