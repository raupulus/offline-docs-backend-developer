---
title: ImagickDraw::push
description: Clona el objeto ImagickDraw actual y lo mete en la pila
source_url: https://www.php.net/manual/es/imagickdraw.push.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/push.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 668b6fc28
order: 36880
---

ImagickDraw::push

Clona el objeto ImagickDraw actual y lo mete en la pila

## Descripción

```php
public ImagickDraw::push(): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Clona el objeto ImagickDraw actual para crear un nuevo objeto ImagickDraw, que es añadido a la pila de ImagickDraw. Los objetos de dibujo ImagickDraw originales pueden ser devueltos invocando a ImagickDraw::pop. Los objetos ImagickDraw son almacenados en una pila ImagickDraw. Por cada Pop debe haber habido un Push equivalente.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `ImagickDraw::push`

```
      
<?php
function push($strokeColor, $fillColor, $backgroundColor, $fillModifiedColor) {

    $draw = new \ImagickDraw();
    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillModifiedColor);
    $draw->setStrokeWidth(2);
    $draw->setFontSize(72);
    $draw->push();
    $draw->translate(50, 50);
    $draw->rectangle(200, 200, 300, 300);
    $draw->pop();
    $draw->setFillColor($fillColor);
    $draw->rectangle(200, 200, 300, 300);

    $imagick = new \Imagick();
    $imagick->newImage(500, 500, $backgroundColor);
    $imagick->setImageFormat("png");

    $imagick->drawImage($draw);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

      
```php
