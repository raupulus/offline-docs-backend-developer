---
title: ImagickDraw::setStrokeAntialias
description: Controla el anti-aliasing de los trazos
source_url: https://www.php.net/manual/es/imagickdraw.setstrokeantialias.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/setstrokeantialias.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 37150
---

ImagickDraw::setStrokeAntialias

Controla el anti-aliasing de los trazos

## Descripción

```php
public ImagickDraw::setStrokeAntialias(bool $enabled): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Controla el anti-aliasing de los trazos. Los contornos a trazos están anti-aliaseados por omisión. Cuando el anti-aliasing está desactivado, los trazos utilizan un valor de umbral para definir si el píxel subyacente debe ser coloreado o no.

## Parámetros

`enabled`  
La configuración de uso del anti-aliasing

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ImagickDraw::setStrokeAntialias`

```
<?php
function setStrokeAntialias($strokeColor, $fillColor, $backgroundColor) {

    $draw = new \ImagickDraw();

    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);
    $draw->setStrokeWidth(1);
    $draw->setStrokeAntialias(false);
    $draw->line(100, 100, 400, 105);

    $draw->line(100, 140, 400, 185);

    $draw->setStrokeAntialias(true);
    $draw->line(100, 110, 400, 115);
    $draw->line(100, 150, 400, 195);

    $image = new \Imagick();
    $image->newImage(500, 250, $backgroundColor);
    $image->setImageFormat("png");

    $image->drawImage($draw);

    header("Content-Type: image/png");
    echo $image->getImageBlob();
}

?>

     
```php
