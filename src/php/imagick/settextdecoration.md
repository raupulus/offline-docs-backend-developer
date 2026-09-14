---
title: ImagickDraw::setTextDecoration
description: Especifica los ornamentos de texto
source_url: https://www.php.net/manual/es/imagickdraw.settextdecoration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/settextdecoration.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 0f49e97ee
order: 37270
---

ImagickDraw::setTextDecoration

Especifica los ornamentos de texto

## Descripción

```php
public ImagickDraw::setTextDecoration(int $decoration): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Especifica los ornamentos de texto utilizados para las anotaciones.

## Parámetros

`decoration`  
Una de las constantes [DECORATION](#imagick.constants.decoration) (`imagick::DECORATION_*`).

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ImagickDraw::setTextDecoration`

```
<?php
function setTextDecoration($strokeColor, $fillColor, $backgroundColor, $textDecoration) {

    $draw = new \ImagickDraw();

    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);
    $draw->setStrokeWidth(2);
    $draw->setFontSize(72);
    $draw->setTextDecoration($textDecoration);
    $draw->annotation(50, 75, "Lorem Ipsum!");

    $imagick = new \Imagick();
    $imagick->newImage(500, 200, $backgroundColor);
    $imagick->setImageFormat("png");
    $imagick->drawImage($draw);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

     
```php
