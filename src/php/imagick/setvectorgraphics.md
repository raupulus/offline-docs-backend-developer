---
title: ImagickDraw::setVectorGraphics
description: Establece los gráficos vectoriales
source_url: https://www.php.net/manual/es/imagickdraw.setvectorgraphics.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/setvectorgraphics.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0f49e97ee
order: 37330
---

ImagickDraw::setVectorGraphics

Establece los gráficos vectoriales

## Descripción

```php
public ImagickDraw::setVectorGraphics(string $xml): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Establece los gráficos vectoriales asociados al objeto ImagickDraw especificado. Use este método con ImagickDraw::getVectorGraphics como un método de persistencia del estado de los gráficos vectoriales.

## Parámetros

`xml`  
archivo xml que contiene los gráficos vectoriales

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `ImagickDraw::setVectorGraphics`

```
      
<?php
function setVectorGraphics() {
    //Setup a draw object with some drawing in it.
    $draw = new \ImagickDraw();
    $draw->setFillColor("red");
    $draw->circle(20, 20, 50, 50);
    $draw->setFillColor("blue");
    $draw->circle(50, 70, 50, 50);
    $draw->rectangle(50, 120, 80, 150);

    //Get the drawing as a string
    $SVG = $draw->getVectorGraphics();

    //$svg is a string, and could be saved anywhere a string can be saved

    //Use the saved drawing to generate a new draw object
    $draw2 = new \ImagickDraw();
    //Apparently the SVG text is missing the root element.
    $draw2->setVectorGraphics("<root>".$SVG."</root>");

    $imagick = new \Imagick();
    $imagick->newImage(200, 200, 'white');
    $imagick->setImageFormat("png");

    $imagick->drawImage($draw2);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

      
```php
