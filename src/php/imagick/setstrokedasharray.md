---
title: ImagickDraw::setStrokeDashArray
description: Especifica el patrón de trazo discontinuo
source_url: https://www.php.net/manual/es/imagickdraw.setstrokedasharray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/setstrokedasharray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 37170
---

ImagickDraw::setStrokeDashArray

Especifica el patrón de trazo discontinuo

## Descripción

```php
public ImagickDraw::setStrokeDashArray(array $dashes): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Especifica el patrón de trazo discontinuo, los segmentos de línea continua y los espacios. El objeto strokeDashArray representa un array de números que especifican las longitudes de los segmentos de línea continua y los espacios, en píxeles. Si se proporciona un número impar de valores, entonces la lista se repite para obtener un número par de valores. Para eliminar un array de patrón existente, se debe pasar un array con cero elementos, y `null` como segundo valor. Un array strokeDashArray típico contiene los miembros 5 3 2.

## Parámetros

`dashes`  
Un array de números decimales

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo con `ImagickDraw::setStrokeDashArray`

```
<?php
function setStrokeDashArray($strokeColor, $fillColor, $backgroundColor) {

    $draw = new \ImagickDraw();

    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);
    $draw->setStrokeWidth(4);

    $draw->setStrokeDashArray([10, 10]);
    $draw->rectangle(100, 50, 225, 175);

    $draw->setStrokeDashArray([20, 5, 20, 5, 5, 5,]);
    $draw->rectangle(275, 50, 400, 175);

    $draw->setStrokeDashArray([20, 5, 20, 5, 5]);
    $draw->rectangle(100, 200, 225, 350);

    $draw->setStrokeDashArray([1, 1, 1, 1, 2, 2, 3, 3, 5, 5, 8, 8, 13, 13, 21, 21, 34, 34, 55, 55, 89, 89, 144, 144, 233, 233, 377, 377, 610, 610, 987, 987, 1597, 1597, 2584, 2584, 4181, 4181,]);

    $draw->rectangle(275, 200, 400, 350);

    $image = new \Imagick();
    $image->newImage(500, 400, $backgroundColor);
    $image->setImageFormat("png");
    $image->drawImage($draw);

    header("Content-Type: image/png");
    echo $image->getImageBlob();
}

?>

     
```php
