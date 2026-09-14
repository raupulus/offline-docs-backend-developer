---
title: ImagickDraw::pathStart
description: Declara el inicio de una lista de dibujo de trazados
source_url: https://www.php.net/manual/es/imagickdraw.pathstart.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/pathstart.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 668b6fc28
order: 36800
---

ImagickDraw::pathStart

Declara el inicio de una lista de dibujo de trazados

## Descripción

```php
public ImagickDraw::pathStart(): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Declara el inicio de una lista de dibujo de trazados que finaliza con un comando DrawPathFinish() coincidente. Todos los demás comandos DrawPath deben estar encerrados entre comandos DrawPathFinish(). Ésto es debido a que los comandos de dibujo de trazados son comandos subordinados y no funcionan por sí mismos.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `ImagickDraw::pathStart`

```
      
<?php
function pathStart($strokeColor, $fillColor, $backgroundColor) {

    $draw = new \ImagickDraw();

    $draw->setStrokeOpacity(1);
    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);

    $draw->setStrokeWidth(2);
    $draw->setFontSize(72);

    $draw->pathStart();
    $draw->pathMoveToAbsolute(50, 50);
    $draw->pathLineToAbsolute(100, 50);
    $draw->pathLineToRelative(0, 50);
    $draw->pathLineToHorizontalRelative(-50);
    $draw->pathFinish();

    $draw->pathStart();
    $draw->pathMoveToAbsolute(50, 50);
    $draw->pathMoveToRelative(300, 0);
    $draw->pathLineToRelative(50, 0);
    $draw->pathLineToVerticalRelative(50);
    $draw->pathLineToHorizontalAbsolute(350);
    $draw->pathclose();
    $draw->pathFinish();

    $draw->pathStart();
    $draw->pathMoveToAbsolute(50, 300);
    $draw->pathCurveToAbsolute(50, 300, 100, 200, 300, 300);
    $draw->pathLineToVerticalAbsolute(350);
    $draw->pathFinish();

    $imagick = new \Imagick();
    $imagick->newImage(500, 500, $backgroundColor);
    $imagick->setImageFormat("png");

    $imagick->drawImage($draw);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();
}

?>

      
```php
