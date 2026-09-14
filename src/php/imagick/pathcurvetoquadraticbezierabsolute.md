---
title: ImagickDraw::pathCurveToQuadraticBezierAbsolute
description: Dibuja una curva de Bézier cuadrática, en coordenadas absolutas
source_url: https://www.php.net/manual/es/imagickdraw.pathcurvetoquadraticbezierabsolute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/pathcurvetoquadraticbezierabsolute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 36620
---

ImagickDraw::pathCurveToQuadraticBezierAbsolute

Dibuja una curva de Bézier cuadrática, en coordenadas absolutas

## Descripción

```php
public ImagickDraw::pathCurveToQuadraticBezierAbsolute(float $x1, float $y1, float $x_end, float $y): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Dibuja una curva de Bézier cuadrática, en coordenadas relativas, con respecto al punto actual (`x`,`y`), utilizando el punto (`x1`,`y1`) como punto de control. Al finalizar el dibujo, el nuevo punto actual se convierte en el punto final (`x`,`y`) utilizado por el polybezier.

## Parámetros

`x1`  
Abscisa del punto de control

`y1`  
Ordenada del punto de control

`x_end`  
Abscisa del punto final

`y`  
Ordenada del punto final

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ImagickDraw::pathCurveToQuadraticBezierAbsolute`

```
<?php
function pathCurveToQuadraticBezierAbsolute($strokeColor, $fillColor, $backgroundColor) {

    $draw = new \ImagickDraw();

    $draw->setStrokeOpacity(1);
    $draw->setStrokeColor($strokeColor);
    $draw->setFillColor($fillColor);

    $draw->setStrokeWidth(2);
    $draw->setFontSize(72);

    $draw->pathStart();
    $draw->pathMoveToAbsolute(50,250);

    // This specifies a quadratic bezier curve with the current position as the start
    // point, the control point is the first two params, and the end point is the last two params.
    $draw->pathCurveToQuadraticBezierAbsolute(
        150,50,
        250,250
    );

    // This specifies a quadratic bezier curve with the current position as the start
    // point, the control point is mirrored from the previous curves control point
    // and the end point is defined by the x, y values.
    $draw->pathCurveToQuadraticBezierSmoothAbsolute(
        450,250
    );

    // This specifies a quadratic bezier curve with the current position as the start
    // point, the control point is mirrored from the previous curves control point
    // and the end point is defined relative from the current position by the x, y values.
    $draw->pathCurveToQuadraticBezierSmoothRelative(
        200,-100
    );

    $draw->pathFinish();

    $imagick = new \Imagick();
    $imagick->newImage(700, 500, $backgroundColor);
    $imagick->setImageFormat("png");

    $imagick->drawImage($draw);

    header("Content-Type: image/png");
    echo $imagick->getImageBlob();

}

?>

     
```php
