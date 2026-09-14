---
title: ImagickDraw::setFillAlpha
description: Configura la opacidad del color de relleno
source_url: https://www.php.net/manual/es/imagickdraw.setfillalpha.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/setfillalpha.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 37010
---

ImagickDraw::setFillAlpha

Configura la opacidad del color de relleno

## Descripción

```php
public ImagickDraw::setFillAlpha(float $alpha): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Configura la opacidad a utilizar cuando el color de relleno es usado. 1.0 es completamente opaco.

## Parámetros

`alpha`  
Canal alpha del color de relleno

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ImagickDraw::setFillAlpha`

```
<?php
function setFillAlpha($strokeColor, $fillColor, $backgroundColor) {

    $draw = new \ImagickDraw();

    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);
    $draw->setStrokeOpacity(1);
    $draw->setStrokeWidth(2);
    $draw->rectangle(100, 200, 200, 300);
    @$draw->setFillAlpha(0.4);
    $draw->rectangle(300, 200, 400, 300);

    $imagick = new \Imagick();
    $imagick->newImage(500, 500, $backgroundColor);
    $imagick->setImageFormat("png");
    $imagick->drawImage($draw);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

     
```php
