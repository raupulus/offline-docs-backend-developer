---
title: ImagickDraw::setFontFamily
description: Establece la familia de fuentes para usarla cuando se escribe texto
source_url: https://www.php.net/manual/es/imagickdraw.setfontfamily.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/setfontfamily.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 668b6fc28
order: 37070
---

ImagickDraw::setFontFamily

Establece la familia de fuentes para usarla cuando se escribe texto

## Descripción

```php
public ImagickDraw::setFontFamily(string $font_family): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Establece la familia de fuentes para usarla cuando se escribe texto.

## Parámetros

`font_family`  
la familia de fuentes

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo de `ImagickDraw::setFontFamily`

```
      
<?php
function setFontFamily($fillColor, $strokeColor, $backgroundColor) {

    $draw = new \ImagickDraw();

    $strokeColor = new \ImagickPixel($strokeColor);
    $fillColor = new \ImagickPixel($fillColor);

    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);

    $draw->setStrokeWidth(2);

    $draw->setFontSize(48);

    $draw->setFontFamily("Times");
    $draw->annotation(50, 50, "Lorem Ipsum!");

    $draw->setFontFamily("AvantGarde");
    $draw->annotation(50, 100, "Lorem Ipsum!");

    $draw->setFontFamily("NewCenturySchlbk");
    $draw->annotation(50, 150, "Lorem Ipsum!");

    $draw->setFontFamily("Palatino");
    $draw->annotation(50, 200, "Lorem Ipsum!");

    $imagick = new \Imagick();
    $imagick->newImage(450, 250, $backgroundColor);
    $imagick->setImageFormat("png");
    $imagick->drawImage($draw);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

      
```php
