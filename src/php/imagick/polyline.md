---
title: ImagickDraw::polyline
description: Dibuja una poli-línea
source_url: https://www.php.net/manual/es/imagickdraw.polyline.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/polyline.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0f49e97ee
order: 36830
---

ImagickDraw::polyline

Dibuja una poli-línea

## Descripción

```php
public ImagickDraw::polyline(array $coordinates): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Dibuja una poli-línea usando el contorno, el ancho del contorno, y el color de relleno o de la textura actuales, usando el array de coordenadas especificado.

## Parámetros

`coordinates`  
array de coordenadas x e y: array( array( 'x' =\> 4, 'y' =\> 6 ), array( 'x' =\> 8, 'y' =\> 10 ) )

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo de `ImagickDraw::polyline`

```
      
<?php
function polyline($strokeColor, $fillColor, $backgroundColor) {
    $draw = new \ImagickDraw();

    $draw->setStrokeOpacity(1);
    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);

    $draw->setStrokeWidth(5);

    $points = [
        ['x' => 40 * 5, 'y' => 10 * 5],
        ['x' => 20 * 5, 'y' => 20 * 5],
        ['x' => 70 * 5, 'y' => 50 * 5],
        ['x' => 60 * 5, 'y' => 15 * 5]
    ];

    $draw->polyline($points);

    $image = new \Imagick();
    $image->newImage(500, 300, $backgroundColor);
    $image->setImageFormat("png");
    $image->drawImage($draw);

    header("Content-Type: image/png");
    echo $image->getImageBlob();
}

?>

      
```php
