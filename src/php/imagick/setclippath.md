---
title: ImagickDraw::setClipPath
description: Asocia un trazado de recorte nominado con la imagen
source_url: https://www.php.net/manual/es/imagickdraw.setclippath.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/setclippath.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 668b6fc28
order: 36980
---

ImagickDraw::setClipPath

Asocia un trazado de recorte nominado con la imagen

## Descripción

```php
public ImagickDraw::setClipPath(string $clip_mask): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Asocia un trazado de recorte nominado con la imagen. Sólo las áreas dibujadas por el trazado de recorte serán modificadas mientras permanezca el efecto.

## Parámetros

`clip_mask`  
el nombre del trazado de recorte

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `ImagickDraw::setClipPath`

```
      
<?php
function setClipPath($strokeColor, $fillColor, $backgroundColor) {

    $draw = new \ImagickDraw();
    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);
    $draw->setStrokeOpacity(1);
    $draw->setStrokeWidth(2);

    $clipPathName = 'testClipPath';

    $draw->pushClipPath($clipPathName);
    $draw->rectangle(0, 0, 250, 250);
    $draw->popClipPath();
    $draw->setClipPath($clipPathName);
    $draw->rectangle(100, 100, 400, 400);

    $imagick = new \Imagick();
    $imagick->newImage(500, 500, $backgroundColor);
    $imagick->setImageFormat("png");

    $imagick->drawImage($draw);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

      
```php
