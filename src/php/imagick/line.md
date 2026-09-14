---
title: ImagickDraw::line
description: Dibuja una línea
source_url: https://www.php.net/manual/es/imagickdraw.line.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/line.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 36580
---

ImagickDraw::line

Dibuja una línea

## Descripción

```php
public ImagickDraw::line(float $start_x, float $start_y, float $end_x, float $end_y): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Dibuja una línea utilizando el color de trazo actual, su opacidad y su grosor.

## Parámetros

`start_x`  
La coordenada X de inicio

`start_y`  
La coordenada Y de inicio

`end_x`  
La coordenada X de fin

`end_y`  
La coordenada Y de fin

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ImagickDraw::line`

```
<?php
function line($strokeColor, $fillColor, $backgroundColor) {

    $draw = new \ImagickDraw();

    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);

    $draw->setStrokeWidth(2);
    $draw->setFontSize(72);

    $draw->line(125, 70, 100, 50);
    $draw->line(350, 170, 100, 150);

    $imagick = new \Imagick();
    $imagick->newImage(500, 500, $backgroundColor);
    $imagick->setImageFormat("png");
    $imagick->drawImage($draw);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

     
```php
