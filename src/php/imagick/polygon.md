---
title: ImagickDraw::polygon
description: Dibuja un polígono
source_url: https://www.php.net/manual/es/imagickdraw.polygon.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/polygon.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0f49e97ee
order: 36820
---

ImagickDraw::polygon

Dibuja un polígono

## Descripción

```php
public ImagickDraw::polygon(array $coordinates): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Dibuja un polígono usando el contorno, el ancho del contorno, y el color de relleno o de la textura actuales, usando el array de coordenadas especificado.

## Parámetros

`coordinates`  
array multidimensional como array( array( 'x' =\> 3, 'y' =\> 4 ), array( 'x' =\> 2, 'y' =\> 6 ) );

## Valores devueltos

Devuelve `true` en caso de éxito.

## Ejemplos

Ejemplo de `ImagickDraw::polygon`

```
      
<?php
function polygon($strokeColor, $fillColor, $backgroundColor) {

    $draw = new \ImagickDraw();

    $draw->setStrokeOpacity(1);
    $draw->setStrokeColor($strokeColor);
    $draw->setStrokeWidth(4);

    $draw->setFillColor($fillColor);

    $points = [
        ['x' => 40 * 5, 'y' => 10 * 5],
        ['x' => 20 * 5, 'y' => 20 * 5],
        ['x' => 70 * 5, 'y' => 50 * 5],
        ['x' => 60 * 5, 'y' => 15 * 5],
    ];

    $draw->polygon($points);

    $image = new \Imagick();
    $image->newImage(500, 300, $backgroundColor);
    $image->setImageFormat("png");
    $image->drawImage($draw);

    header("Content-Type: image/png");
    echo $image->getImageBlob();
}

?>

      
```php
