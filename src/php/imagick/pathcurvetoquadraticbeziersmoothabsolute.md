---
title: ImagickDraw::pathCurveToQuadraticBezierSmoothAbsolute
description: Dibuja una curva Bézier cuadrática
source_url: https://www.php.net/manual/es/imagickdraw.pathcurvetoquadraticbeziersmoothabsolute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/pathcurvetoquadraticbeziersmoothabsolute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0f49e97ee
order: 36640
---

ImagickDraw::pathCurveToQuadraticBezierSmoothAbsolute

Dibuja una curva Bézier cuadrática

## Descripción

```php
public ImagickDraw::pathCurveToQuadraticBezierSmoothAbsolute(float $x, float $y): bool
```php

Dibuja una curva Bézier cuadrática (usando coordenadas absolutas) desde el punto actual a (x, y). Se asume que el punto de control es la refelxión del punto de control del comando previo relativo al punto actual. (Si no hay comando previo o el comando previo no es DrawPathCurveToQuadraticBezierAbsolute, DrawPathCurveToQuadraticBezierRelative, DrawPathCurveToQuadraticBezierSmoothAbsolute DrawPathCurveToQuadraticBezierSmoothRelative, se asume que el punto de control coincide con el punto actual). Al final del comando, el nuevo punto actual se convierte en el par de coordenadas final (x, y) usado en el Bezígono.

Esta función no se puede utilizar para continuar de forma suave una curva Bézier cúbica. Solamente puede continuarse suavemente desde una curva cuadrática.

## Parámetros

`x`  
coordenada x final

`y`  
coordenada y final

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de ImagickDraw::pathCurveToQuadraticBezierSmoothAbsolute

```
<?php
$draw = new \ImagickDraw();

$draw->setStrokeOpacity(1);
$draw->setStrokeColor("black");
$draw->setFillColor("blue");

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
?>

    
```php
