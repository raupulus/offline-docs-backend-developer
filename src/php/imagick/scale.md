---
title: ImagickDraw::scale
description: Ajusta el factor de escala
source_url: https://www.php.net/manual/es/imagickdraw.scale.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/scale.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0f49e97ee
order: 36970
---

ImagickDraw::scale

Ajusta el factor de escala

## Descripción

```php
public ImagickDraw::scale(float $x, float $y): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Ajusta el factor de escala a aplicar en las direcciones horizontal y vertical al espacio de coordenadas actual.

## Parámetros

`x`  
factor horizontal

`y`  
factor vertical

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `ImagickDraw::scale`

```
      
<?php
function scale($strokeColor, $fillColor, $backgroundColor, $fillModifiedColor) {

    $draw = new \ImagickDraw();
    $draw->setStrokeColor($strokeColor);
    $draw->setStrokeWidth(4);
    $draw->setFillColor($fillColor);
    $draw->rectangle(200, 200, 300, 300);
    $draw->setFillColor($fillModifiedColor);
    $draw->scale(1.4, 1.4);
    $draw->rectangle(200, 200, 300, 300);

    $image = new \Imagick();
    $image->newImage(500, 500, $backgroundColor);
    $image->setImageFormat("png");
    $image->drawImage($draw);

    header("Content-Type: image/png");
    echo $image->getImageBlob();
}

?>

      
```php
