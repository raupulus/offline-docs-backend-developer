---
title: ImagickDraw::matte
description: Dibuja sobre el canal de opacidad de la imagen
source_url: https://www.php.net/manual/es/imagickdraw.matte.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/matte.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 36590
---

ImagickDraw::matte

Dibuja sobre el canal de opacidad de la imagen

## Descripción

```php
public ImagickDraw::matte(float $x, float $y, int $paint): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Dibuja sobre el canal de opacidad de la imagen, con el fin de hacer transparentes los píxeles indicados.

## Parámetros

`x`  
Abscisa del mate

`y`  
Ordenada del mate

`paint`  
Una de las constantes [PAINT](#imagick.constants.paint) (`imagick::PAINT_*`).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `ImagickDraw::matte`

```
<?php
function matte($strokeColor, $fillColor, $backgroundColor, $paintType) {
    $draw = new \ImagickDraw();

    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);

    $draw->setStrokeWidth(2);
    $draw->setFontSize(72);

    $draw->matte(120, 120, $paintType);
    $draw->rectangle(100, 100, 300, 200);

    $imagick = new \Imagick();
    $imagick->newImage(500, 500, $backgroundColor);
    $imagick->setImageFormat("png");
    $imagick->drawImage($draw);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

     
```php
