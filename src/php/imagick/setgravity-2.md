---
title: ImagickDraw::setGravity
description: Configura la gravedad de colocación de texto
source_url: https://www.php.net/manual/es/imagickdraw.setgravity.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/setgravity.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 0f49e97ee
order: 37120
---

ImagickDraw::setGravity

Configura la gravedad de colocación de texto

## Descripción

```php
public ImagickDraw::setGravity(int $gravity): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Configura la gravedad de colocación de texto, a utilizar para dibujar las anotaciones.

## Parámetros

`gravity`  
Una de las constantes [GRAVITY](#imagick.constants.gravity) (`imagick::GRAVITY_*`).

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ImagickDraw::setGravity`

```
<?php
function setGravity($fillColor, $strokeColor, $backgroundColor) {

    $draw = new \ImagickDraw();
    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);
    $draw->setStrokeWidth(1);
    $draw->setFontSize(24);

    $gravitySettings = array(
        \Imagick::GRAVITY_NORTHWEST => 'NorthWest',
        \Imagick::GRAVITY_NORTH => 'North',
        \Imagick::GRAVITY_NORTHEAST => 'NorthEast',
        \Imagick::GRAVITY_WEST => 'West',
        \Imagick::GRAVITY_CENTER => 'Centro',
        \Imagick::GRAVITY_SOUTHWEST => 'SouthWest',
        \Imagick::GRAVITY_SOUTH => 'South',
        \Imagick::GRAVITY_SOUTHEAST => 'SouthEast',
        \Imagick::GRAVITY_EAST => 'East'
    );

    $draw->setFont("../fonts/Arial.ttf");

    foreach ($gravitySettings as $type => $description) {
        $draw->setGravity($type);
        $draw->annotation(50, 50, '"' . $description . '"');
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
