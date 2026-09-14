---
title: ImagickPixel::setColor
description: Define la color
source_url: https://www.php.net/manual/es/imagickpixel.setcolor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickpixel/setcolor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: fa0c88f1e
order: 37640
---

ImagickPixel::setColor

Define la color

## Descripción

```php
public ImagickPixel::setColor(string $color): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Define la color, descrita por el objeto ImagickPixel, con un `string` (por ejemplo, `"blue"`, `"#0000ff"`, `"rgb(0,0,255)"`, `"cmyk(100,100,100,10)"`, etc.).

## Parámetros

`color`  
La definición de la color a utilizar para inicializar el objeto ImagickPixel.

## Valores devueltos

Retorna `true` si la color especificada ha sido definida o `false` en caso contrario.

## Ejemplos

Ejemplo con `ImagickPixel::setColor`

```
<?php
function setColor() {
    $draw = new \ImagickDraw();

    $strokeColor = new \ImagickPixel('green');
    $fillColor = new \ImagickPixel();
    $fillColor->setColor('rgba(100%, 75%, 0%, 1.0)');

    $draw->setstrokewidth(3.0);
    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);
    $draw->rectangle(200, 200, 300, 300);

    $image = new \Imagick();
    $image->newImage(500, 500, "SteelBlue2");
    $image->setImageFormat("png");

    $image->drawImage($draw);

    header("Content-Type: image/png");
    echo $image->getImageBlob();
}

?>

     
```php
