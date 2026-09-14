---
title: ImagickDraw::setFillOpacity
description: Configura la opacidad a utilizar para el relleno
source_url: https://www.php.net/manual/es/imagickdraw.setfillopacity.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/setfillopacity.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 37030
---

ImagickDraw::setFillOpacity

Configura la opacidad a utilizar para el relleno

## Descripción

```php
public ImagickDraw::setFillOpacity(float $opacity): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Configura la opacidad a utilizar para el relleno. Totalmente opaco es 1.0.

## Parámetros

`opacity`  
La opacidad de relleno.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ImagickDraw::setFillOpacity`

```
<?php
function setFillOpacity($strokeColor, $fillColor, $backgroundColor) {

    $draw = new \ImagickDraw();

    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);
    $draw->setStrokeOpacity(1);
    $draw->setStrokeWidth(2);

    $draw->rectangle(100, 200, 200, 300);

    $draw->setFillOpacity(0.4);
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
