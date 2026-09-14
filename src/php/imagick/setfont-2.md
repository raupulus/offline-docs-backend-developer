---
title: ImagickDraw::setFont
description: Establece la fuente especificada completamente para usarla cuando se
  escribe texto
source_url: https://www.php.net/manual/es/imagickdraw.setfont.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/setfont.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 668b6fc28
order: 37060
---

ImagickDraw::setFont

Establece la fuente especificada completamente para usarla cuando se escribe texto

## Descripción

```php
public ImagickDraw::setFont(string $font_name): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Establece la fuente especificada completamente para usarla cuando se escribe texto.

## Parámetros

`font_name`  

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo de `ImagickDraw::setFont`

```
      
<?php
function setFont($fillColor, $strokeColor, $backgroundColor) {

    $draw = new \ImagickDraw();

    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);

    $draw->setStrokeWidth(2);
    $draw->setFontSize(36);

    $draw->setFont("../fonts/Arial.ttf");
    $draw->annotation(50, 50, "Lorem Ipsum!");

    $draw->setFont("../fonts/Consolas.ttf");
    $draw->annotation(50, 100, "Lorem Ipsum!");

    $draw->setFont("../fonts/CANDY.TTF");
    $draw->annotation(50, 150, "Lorem Ipsum!");

    $draw->setFont("../fonts/Inconsolata-dz.otf");
    $draw->annotation(50, 200, "Lorem Ipsum!");

    $imagick = new \Imagick();
    $imagick->newImage(500, 300, $backgroundColor);
    $imagick->setImageFormat("png");
    $imagick->drawImage($draw);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

      
```php
