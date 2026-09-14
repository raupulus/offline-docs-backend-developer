---
title: ImagickDraw::pathCurveToQuadraticBezierRelative
description: Dibuja una curva de Bézier cuadrática, en coordenadas relativas
source_url: https://www.php.net/manual/es/imagickdraw.pathcurvetoquadraticbezierrelative.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickdraw/pathcurvetoquadraticbezierrelative.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: e4ec40195
order: 36630
---

ImagickDraw::pathCurveToQuadraticBezierRelative

Dibuja una curva de Bézier cuadrática, en coordenadas relativas

## Descripción

```php
public ImagickDraw::pathCurveToQuadraticBezierRelative(float $x1, float $y1, float $x_end, float $y): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Dibuja una curva de Bézier cuadrática, en coordenadas relativas, respecto al punto actual (`x`,`y`), utilizando el punto (`x1`,`y1`) como punto de control. Al finalizar el dibujo, el nuevo punto actual se convierte en el punto final (`x`,`y`) utilizado por el polybezier.

## Parámetros

`x1`  
coordenada x de inicio

`y1`  
coordenada y de inicio

`x_end`  
coordenada x de fin

`y`  
coordenada y de fin

## Valores devueltos

No se retorna ningún valor.
