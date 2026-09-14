---
title: ImagickDraw::setTextAntialias
description: Controla el anti-aliaseo del texto
source_url: https://www.php.net/manual/es/imagickdraw.settextantialias.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/settextantialias.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 37260
---

ImagickDraw::setTextAntialias

Controla el anti-aliaseo del texto

## Descripción

```php
public ImagickDraw::setTextAntialias(bool $antialias): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Controla el anti-aliaseo del texto. El texto es anti-aliaseado por omisión.

## Parámetros

`antialias`  

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ImagickDraw::setTextAntialias`

```
<?php
function setTextAntialias($fillColor, $backgroundColor) {

    $draw = new \ImagickDraw();
    $draw->setStrokeColor('none');
    $draw->setFillColor($fillColor);
    $draw->setStrokeWidth(1);
    $draw->setFontSize(32);
    $draw->setTextAntialias(false);
    $draw->annotation(5, 30, "Lorem Ipsum!");
    $draw->setTextAntialias(true);
    $draw->annotation(5, 65, "Lorem Ipsum!");

    $imagick = new \Imagick();
    $imagick->newImage(220, 80, $backgroundColor);
    $imagick->setImageFormat("png");
    $imagick->drawImage($draw);

    //Scale the image so that people can see the aliasing.
    $imagick->scaleImage(220 * 6, 80 * 6);
    $imagick->cropImage(640, 480, 0, 0);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

     
```php
