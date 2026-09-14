---
title: ImagickDraw::setStrokeLineCap
description: Especifica la forma a utilizar al final de los subcampos
source_url: https://www.php.net/manual/es/imagickdraw.setstrokelinecap.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/setstrokelinecap.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 0f49e97ee
order: 37190
---

ImagickDraw::setStrokeLineCap

Especifica la forma a utilizar al final de los subcampos

## Descripción

```php
public ImagickDraw::setStrokeLineCap(int $linecap): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Especifica la forma a utilizar al final de los subcaminos.

## Parámetros

`linecap`  
Una de las constantes [LINECAP](#imagick.constants.linecap) (`imagick::LINECAP_*`).

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ImagickDraw::setStrokeLineCap`

```
<?php
function setStrokeLineCap($strokeColor, $fillColor, $backgroundColor) {

    $draw = new \ImagickDraw();
    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);
    $draw->setStrokeWidth(25);

    $lineTypes = [\Imagick::LINECAP_BUTT, \Imagick::LINECAP_ROUND, \Imagick::LINECAP_SQUARE,];

    $offset = 0;

    foreach ($lineTypes as $lineType) {
        $draw->setStrokeLineCap($lineType);
        $draw->line(50 + $offset, 50, 50 + $offset, 250);
        $offset += 50;
    }

    $imagick = new \Imagick();
    $imagick->newImage(300, 300, $backgroundColor);
    $imagick->setImageFormat("png");
    $imagick->drawImage($draw);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

     
```php
