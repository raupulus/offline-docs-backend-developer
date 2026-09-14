---
title: ImagickDraw::setFontStretch
description: Configura el estiramiento del texto
source_url: https://www.php.net/manual/es/imagickdraw.setfontstretch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/setfontstretch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 37090
---

ImagickDraw::setFontStretch

Configura el estiramiento del texto

## Descripción

```php
public ImagickDraw::setFontStretch(int $stretch): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Configura el estiramiento del texto para el dibujo de anotaciones. La enumeración `AnyStretch` sirve como comodín y significa "no importa".

## Parámetros

`stretch`  
Una de las constantes [STRETCH](#imagick.constants.stretch) (`imagick::STRETCH_*`).

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ImagickDraw::setFontStretch`

```
<?php
function setFontStretch($fillColor, $strokeColor, $backgroundColor) {

    $draw = new \ImagickDraw();

    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);
    $draw->setStrokeWidth(2);
    $draw->setFontSize(36);

    $fontStretchTypes = [
        \Imagick::STRETCH_ULTRACONDENSED,
        \Imagick::STRETCH_CONDENSED,
        \Imagick::STRETCH_SEMICONDENSED,
        \Imagick::STRETCH_SEMIEXPANDED,
        \Imagick::STRETCH_EXPANDED,
        \Imagick::STRETCH_EXTRAEXPANDED,
        \Imagick::STRETCH_ULTRAEXPANDED,
        \Imagick::STRETCH_ANY
    ];

    $offset = 0;
    foreach ($fontStretchTypes as $fontStretch) {
        $draw->setFontStretch($fontStretch);
        $draw->annotation(50, 75 + $offset, "Lorem Ipsum!");
        $offset += 50;
    }

    $imagick = new \Imagick();
    $imagick->newImage(500, 500, $backgroundColor);
    $imagick->setImageFormat("png");
    $imagick->drawImage($draw);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

     
```php
