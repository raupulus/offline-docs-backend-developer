---
title: ImagickDraw::rotate
description: Aplica la rotación especificada al espacio de coordenadas actual
source_url: https://www.php.net/manual/es/imagickdraw.rotate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/rotate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 668b6fc28
order: 36950
---

ImagickDraw::rotate

Aplica la rotación especificada al espacio de coordenadas actual

## Descripción

```php
public ImagickDraw::rotate(float $degrees): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Aplica la rotación especificada al espacio de coordenadas actual.

## Parámetros

`degrees`  
grados a rotar.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `ImagickDraw::rotate`

```
      
<?php
function rotate($strokeColor, $fillColor, $backgroundColor, $fillModifiedColor) {
    $draw = new \ImagickDraw();
    $draw->setStrokeColor($strokeColor);
    $draw->setStrokeOpacity(1);
    $draw->setFillColor($fillColor);
    $draw->rectangle(200, 200, 300, 300);
    $draw->setFillColor($fillModifiedColor);
    $draw->rotate(15);
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
