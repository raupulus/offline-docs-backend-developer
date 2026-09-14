---
title: ImagickDraw::setFontWeight
description: Configura el peso de la fuente
source_url: https://www.php.net/manual/es/imagickdraw.setfontweight.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/setfontweight.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 37110
---

ImagickDraw::setFontWeight

Configura el peso de la fuente

## Descripción

```php
public ImagickDraw::setFontWeight(int $weight): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Configura el peso de la fuente para dibujar anotaciones.

## Parámetros

`weight`  

## Valores devueltos

## Ejemplos

Ejemplo con `ImagickDraw::setFontWeight`

```
<?php
function setFontWeight($fillColor, $strokeColor, $backgroundColor) {

    $draw = new \ImagickDraw();

    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);

    $draw->setStrokeWidth(1);

    $draw->setFontSize(36);

    $draw->setFontWeight(100);
    $draw->annotation(50, 50, "Lorem Ipsum!");

    $draw->setFontWeight(200);
    $draw->annotation(50, 100, "Lorem Ipsum!");

    $draw->setFontWeight(400);
    $draw->annotation(50, 150, "Lorem Ipsum!");

    $draw->setFontWeight(800);
    $draw->annotation(50, 200, "Lorem Ipsum!");

    $imagick = new \Imagick();
    $imagick->newImage(500, 500, $backgroundColor);
    $imagick->setImageFormat("png");
    $imagick->drawImage($draw);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

     
```php
