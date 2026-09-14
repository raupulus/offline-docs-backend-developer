---
title: ImagickPixel::__construct
description: El constructor ImagickPixel
source_url: https://www.php.net/manual/es/imagickpixel.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickpixel/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: fa0c88f1e
order: 37510
---

ImagickPixel::\_\_construct

El constructor

ImagickPixel

## Descripción

```php
public ImagickPixel::__construct([string $color])
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Construye un objeto `ImagickPixel`. Si se especifica un color, el objeto se construye, luego se inicializa con ese color antes de ser devuelto.

## Parámetros

`color`  
Una cadena que representa el color opcional a utilizar como valor inicial del objeto.

## Valores devueltos

Devuelve un objeto `ImagickPixel` en caso de éxito o lanza una excepción `ImagickPixelException` si ocurre un error.

## Ejemplos

Ejemplo con `ImagickPixel::construct`

```
<?php
function construct() {

    $columns = 4;

    $exampleColors = array(
        "rgba(100%, 0%, 0%, 0.5)",
        "hsb(33.3333%, 100%,  75%)", // verde medio
        "hsl(120, 255,   191.25)", //verde medio
        "graya(50%, 0.5)", // gris medio, semi-transparente
        "LightCoral", "none", //"cmyk(0.9, 0.48, 0.83, 0.50)",
        "#f00", //  #rgb
        "#ff0000", //  #rrggbb
        "#ff0000ff", //  #rrggbbaa
        "#ffff00000000", //  #rrrrggggbbbb
        "#ffff00000000ffff", //  #rrrrggggbbbbaaaa
        "rgb(255, 0, 0)", //  un entero en el rango 0—255 para cada componente
        "rgb(100.0%, 0.0%, 0.0%)", //  un valor de punto flotante, en el rango 0—100% para cada componente
        "rgb(255, 0, 0)", //  rango 0 - 255
        "rgba(255, 0, 0, 1.0)", //  lo mismo, pero con un valor alpha explícito
        "rgb(100%, 0%, 0%)", //  rango 0.0% - 100.0%
        "rgba(100%, 0%, 0%, 1.0)", //  lo mismo, pero con un valor alpha explícito
    );

    $draw = new \ImagickDraw();
    $count = 0;
    $black = new \ImagickPixel('rgb(0, 0, 0)');

    foreach ($exampleColors as $exampleColor) {
        $color = new \ImagickPixel($exampleColor);

        $draw->setstrokewidth(1.0);
        $draw->setStrokeColor($black);
        $draw->setFillColor($color);
        $offsetX = ($count % $columns) * 50 + 5;
        $offsetY = intval($count / $columns) * 50 + 5;
        $draw->rectangle(0 + $offsetX, 0 + $offsetY, 40 + $offsetX, 40 + $offsetY);
        $count++;
    }

    $image = new \Imagick();
    $image->newImage(350, 350, "blue");
    $image->setImageFormat("png");
    $image->drawImage($draw);
    header("Content-Type: image/png");
    echo $image->getImageBlob();
}

?>

     
```php
